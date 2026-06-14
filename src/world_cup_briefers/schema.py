from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml


class DossierValidationError(ValueError):
    """Raised when a dossier YAML file is missing required report fields."""


@dataclass(frozen=True)
class RequiredPath:
    path: tuple[str, ...]
    expected_type: type | tuple[type, ...] | None = None

    @property
    def dotted(self) -> str:
        return ".".join(self.path)


REQUIRED_PATHS: tuple[RequiredPath, ...] = (
    RequiredPath(("report",), dict),
    RequiredPath(("report", "title"), str),
    RequiredPath(("report", "competition"), str),
    RequiredPath(("report", "stage"), str),
    RequiredPath(("report", "status"), str),
    RequiredPath(("report", "thesis"), str),
    RequiredPath(("match",), dict),
    RequiredPath(("match", "team_a"), str),
    RequiredPath(("match", "team_b"), str),
    RequiredPath(("match", "kickoff_local"), (str, int)),
    RequiredPath(("match", "kickoff_timezone"), str),
    RequiredPath(("match", "venue"), dict),
    RequiredPath(("match", "venue", "name"), str),
    RequiredPath(("match", "venue", "city"), str),
    RequiredPath(("match", "venue", "capacity"), int),
    RequiredPath(("brief",), list),
    RequiredPath(("cup_status",), dict),
    RequiredPath(("cup_status", "teams"), list),
    RequiredPath(("possible_futures",), list),
    RequiredPath(("teams",), list),
    RequiredPath(("players_to_watch",), list),
    RequiredPath(("tactical_watchlist",), list),
    RequiredPath(("crowd_weather",), dict),
    RequiredPath(("discipline_availability",), list),
    RequiredPath(("country_culture_notes",), list),
    RequiredPath(("sources_confidence",), dict),
)

NON_EMPTY_LISTS = (
    "brief",
    "possible_futures",
    "teams",
    "players_to_watch",
    "tactical_watchlist",
    "discipline_availability",
    "country_culture_notes",
)

MINIMUM_LIST_LENGTHS = {
    "teams": 2,
    "cup_status.teams": 2,
    "discipline_availability": 2,
    "country_culture_notes": 2,
}


def load_yaml_file(path: str | Path) -> dict[str, Any]:
    """Load a UTF-8 YAML file and return a mapping."""
    yaml_path = Path(path)
    with yaml_path.open("r", encoding="utf-8") as handle:
        loaded = yaml.safe_load(handle)
    if not isinstance(loaded, dict):
        raise DossierValidationError(f"{yaml_path} must contain a YAML mapping at the top level")
    return loaded


def validate_dossier(data: dict[str, Any]) -> None:
    """Validate the minimum schema required by the renderers.

    This is intentionally a lightweight contract rather than a full JSON Schema
    implementation. It catches missing or structurally invalid data before the
    template stage while staying easy to evolve during a tournament.
    """
    errors: list[str] = []
    for required in REQUIRED_PATHS:
        value: Any = data
        for key in required.path:
            if not isinstance(value, dict) or key not in value:
                errors.append(f"missing required field: {required.dotted}")
                break
            value = value[key]
        else:
            if required.expected_type is not None and not isinstance(value, required.expected_type):
                expected = _type_name(required.expected_type)
                actual = type(value).__name__
                errors.append(f"field {required.dotted} must be {expected}, got {actual}")

    if not errors:
        _validate_list_lengths(data, errors)

    if errors:
        joined = "\n".join(f"- {error}" for error in errors)
        raise DossierValidationError(f"invalid dossier:\n{joined}")


def load_and_validate(path: str | Path) -> dict[str, Any]:
    data = load_yaml_file(path)
    validate_dossier(data)
    return data


def _validate_list_lengths(data: dict[str, Any], errors: list[str]) -> None:
    for key in NON_EMPTY_LISTS:
        value = data.get(key)
        if isinstance(value, list) and len(value) == 0:
            errors.append(f"field {key} must contain at least one item")

    for dotted, minimum in MINIMUM_LIST_LENGTHS.items():
        value: Any = data
        for part in dotted.split("."):
            if not isinstance(value, dict) or part not in value:
                break
            value = value[part]
        else:
            if isinstance(value, list) and len(value) < minimum:
                errors.append(f"field {dotted} must contain at least {minimum} items")


def _type_name(expected_type: type | tuple[type, ...]) -> str:
    if isinstance(expected_type, tuple):
        return " or ".join(t.__name__ for t in expected_type)
    return expected_type.__name__
