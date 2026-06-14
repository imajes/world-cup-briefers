from __future__ import annotations

from importlib import resources
from pathlib import Path
from typing import Any

from jinja2 import Environment, FileSystemLoader, PackageLoader, select_autoescape

from .flags import flag_svg
from .schema import validate_dossier


def render_html(data: dict[str, Any], template_path: str | Path | None = None) -> str:
    validate_dossier(data)
    return _environment(template_path=template_path).get_template(_template_name(template_path, "report.html.j2")).render(
        report=data,
        fmt=_formatters(),
    )


def render_markdown(data: dict[str, Any], template_path: str | Path | None = None) -> str:
    validate_dossier(data)
    return _environment(autoescape=False, template_path=template_path).get_template(
        _template_name(template_path, "report.md.j2")
    ).render(report=data, fmt=_formatters())


def write_rendered(
    data: dict[str, Any],
    output_path: str | Path,
    output_format: str = "html",
    template_path: str | Path | None = None,
) -> Path:
    target = Path(output_path)
    target.parent.mkdir(parents=True, exist_ok=True)
    if output_format == "html":
        content = render_html(data, template_path=template_path)
    elif output_format in {"markdown", "md"}:
        content = render_markdown(data, template_path=template_path)
    else:
        raise ValueError(f"unsupported output format: {output_format}")
    target.write_text(content, encoding="utf-8")
    return target


def _environment(autoescape: bool = True, template_path: str | Path | None = None) -> Environment:
    if template_path is not None:
        template = Path(template_path)
        loader = FileSystemLoader(str(template.parent))
    else:
        try:
            loader = PackageLoader("world_cup_briefers", "templates")
        except Exception:
            template_dir = resources.files("world_cup_briefers").joinpath("templates")
            loader = FileSystemLoader(str(template_dir))

    env = Environment(
        loader=loader,
        autoescape=select_autoescape(["html", "xml"]) if autoescape else False,
        trim_blocks=True,
        lstrip_blocks=True,
    )
    env.filters["join_list"] = join_list
    env.filters["fallback"] = fallback
    env.filters["team_code"] = team_code
    env.filters["comma_int"] = comma_int
    env.filters["status_label"] = status_label
    env.filters["player_icon"] = player_icon
    env.globals["flag_svg"] = flag_svg
    return env


def _template_name(template_path: str | Path | None, default: str) -> str:
    return Path(template_path).name if template_path is not None else default


def _formatters() -> dict[str, Any]:
    return {
        "join_list": join_list,
        "fallback": fallback,
        "team_code": team_code,
        "comma_int": comma_int,
    }


def join_list(value: Any, empty: str = "None confirmed") -> str:
    if value is None:
        return empty
    if isinstance(value, str):
        return value or empty
    if isinstance(value, list):
        return ", ".join(str(item) for item in value) if value else empty
    return str(value)


def fallback(value: Any, default: str = "Not specified") -> str:
    if value is None:
        return default
    if isinstance(value, str) and not value.strip():
        return default
    if isinstance(value, list) and not value:
        return default
    return str(value)


def team_code(value: str) -> str:
    known = {
        "haiti": "HAI",
        "scotland": "SCO",
        "united states": "USA",
        "usa": "USA",
        "england": "ENG",
        "ireland": "IRL",
        "germany": "GER",
        "curacao": "CUW",
        "curaçao": "CUW",
        "netherlands": "NED",
        "japan": "JPN",
        "australia": "AUS",
        "türkiye": "TUR",
        "turkiye": "TUR",
        "turkey": "TUR",
    }
    return known.get(value.strip().casefold(), value[:3].upper())


def comma_int(value: Any) -> str:
    try:
        return f"{int(value):,}"
    except (TypeError, ValueError):
        return str(value)


def status_label(value: str) -> str:
    return value.replace("_", " ").replace("-", " ").title()


def player_icon(category: str) -> str:
    normalized = category.casefold()
    if "win" in normalized or "spotlight" in normalized:
        return "i-spark"
    if "break" in normalized or "trouble" in normalized or "risk" in normalized:
        return "i-warning"
    if "pressure" in normalized or "calm" in normalized:
        return "i-calm"
    if "sub" in normalized or "swing" in normalized:
        return "i-swap"
    return "i-player"
