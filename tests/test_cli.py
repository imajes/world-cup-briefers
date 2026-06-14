from __future__ import annotations

import subprocess
import sys
from pathlib import Path

from world_cup_briefers.cli import main
from conftest import EXAMPLE, ROOT


def test_cli_writes_html(tmp_path: Path) -> None:
    output = tmp_path / "dossier.html"
    exit_code = main([str(EXAMPLE), "--output", str(output)])

    assert exit_code == 0
    assert output.exists()
    assert "Haiti vs Scotland" in output.read_text(encoding="utf-8")


def test_cli_validation_only(capsys) -> None:  # type: ignore[no-untyped-def]
    exit_code = main([str(EXAMPLE), "--validate-only"])

    assert exit_code == 0
    assert "OK:" in capsys.readouterr().out


def test_legacy_script_wrapper_renders_markdown(tmp_path: Path) -> None:
    output = tmp_path / "dossier.md"
    result = subprocess.run(
        [
            sys.executable,
            str(ROOT / "scripts" / "build_report.py"),
            str(EXAMPLE),
            "--format",
            "markdown",
            "--output",
            str(output),
        ],
        cwd=ROOT,
        check=False,
        text=True,
        capture_output=True,
    )

    assert result.returncode == 0, result.stderr
    assert output.read_text(encoding="utf-8").startswith("# Haiti vs Scotland")
