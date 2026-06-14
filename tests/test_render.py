from __future__ import annotations

from world_cup_briefers.render import render_html, render_markdown, team_code
from world_cup_briefers.schema import load_and_validate
from conftest import EXAMPLE


def test_html_render_contains_core_sections_and_inline_flags() -> None:
    data = load_and_validate(EXAMPLE)
    html = render_html(data)

    assert "Haiti vs Scotland" in html
    assert "90-Second Brief" in html
    assert "Three Possible Futures" in html
    assert "Sources and Confidence" in html
    assert "HAI" in html
    assert "SCO" in html
    assert "mini-flag" in html
    assert "{" + "{" not in html


def test_markdown_render_contains_tables_and_caveats() -> None:
    data = load_and_validate(EXAMPLE)
    markdown = render_markdown(data)

    assert markdown.startswith("# Haiti vs Scotland")
    assert "| Team | Points | Position |" in markdown
    assert "## Source / Confidence Notes" in markdown
    assert "Official attendance before kickoff" in markdown


def test_team_code_knows_haiti_and_scotland() -> None:
    assert team_code("Haiti") == "HAI"
    assert team_code("Scotland") == "SCO"
