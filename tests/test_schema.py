from __future__ import annotations

import copy

import pytest

from world_cup_briefers.schema import DossierValidationError, load_and_validate, validate_dossier
from conftest import EXAMPLE


def test_example_yaml_is_valid() -> None:
    data = load_and_validate(EXAMPLE)
    assert data["report"]["title"] == "Haiti vs Scotland — Match Dossier"
    assert data["match"]["team_a"] == "Haiti"


def test_missing_required_field_reports_dotted_path() -> None:
    data = load_and_validate(EXAMPLE)
    broken = copy.deepcopy(data)
    del broken["report"]["title"]

    with pytest.raises(DossierValidationError, match="report.title"):
        validate_dossier(broken)


def test_team_sections_require_two_teams() -> None:
    data = load_and_validate(EXAMPLE)
    broken = copy.deepcopy(data)
    broken["teams"] = broken["teams"][:1]

    with pytest.raises(DossierValidationError, match="teams"):
        validate_dossier(broken)
