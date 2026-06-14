from __future__ import annotations

import argparse
from pathlib import Path
from typing import Sequence

from .render import render_html, render_markdown, write_rendered
from .schema import DossierValidationError, load_and_validate


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Render a World Cup dossier YAML file to HTML or Markdown.")
    parser.add_argument("input", type=Path, help="Path to dossier YAML file")
    parser.add_argument("-o", "--output", type=Path, help="Output path. Prints to stdout when omitted.")
    parser.add_argument(
        "--format",
        choices=("html", "markdown", "md"),
        default="html",
        help="Output format. Default: html.",
    )
    parser.add_argument("--template", type=Path, help="Optional custom Jinja template path.")
    parser.add_argument("--validate-only", action="store_true", help="Validate the YAML and exit without rendering.")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        data = load_and_validate(args.input)
        if args.validate_only:
            print(f"OK: {args.input}")
            return 0

        output_format = "markdown" if args.format == "md" else args.format
        if args.output:
            write_rendered(data, args.output, output_format=output_format, template_path=args.template)
            print(f"Wrote {args.output}")
            return 0

        if output_format == "html":
            rendered = render_html(data, template_path=args.template)
        else:
            rendered = render_markdown(data, template_path=args.template)
        print(rendered)
        return 0
    except DossierValidationError as exc:
        parser.exit(2, f"error: {exc}\n")


if __name__ == "__main__":
    raise SystemExit(main())
