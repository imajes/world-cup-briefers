# World Cup Briefers

YAML-driven match dossiers for FIFA World Cup matches: one structured source file, repeatable renderers, and human-readable HTML/Markdown outputs.

This repo makes the pre-match dossier workflow repeatable instead of one-off: gather current facts, write a structured YAML artifact, render a polished HTML briefer, and keep the source reusable for later automation.

## What this produces

- A **machine-readable YAML dossier** with match status, standings, storylines, player availability, crowd/weather notes, and source-confidence fields.
- A **polished HTML report** intended for reading, sharing, and printing.
- A **plain Markdown report** for chat, notes, archives, or low-friction review.
- A small Python CLI that validates input before rendering.

## Quick start

```zsh
uv sync
uv run pytest
uv run world-cup-briefer examples/haiti_scotland_dossier.yaml --output out/haiti_scotland_dossier.html
open out/haiti_scotland_dossier.html
```

Without installing the package:

```zsh
python scripts/build_report.py examples/haiti_scotland_dossier.yaml --output out/haiti_scotland_dossier.html
```

Render Markdown instead of HTML:

```zsh
uv run world-cup-briefer examples/haiti_scotland_dossier.yaml \
  --format markdown \
  --output out/haiti_scotland_dossier.md
```

Validate only:

```zsh
uv run world-cup-briefer examples/haiti_scotland_dossier.yaml --validate-only
```

Use a custom template:

```zsh
uv run world-cup-briefer examples/haiti_scotland_dossier.yaml \
  --template templates/report_template.html \
  --output out/custom.html
```

## Repository map

```text
.
├── data/
│   ├── blank_report.yaml          # starter dossier
│   └── schema_reference.yaml      # annotated YAML contract
├── docs/
│   ├── automation_prompt.md       # reusable automation/check prompt
│   ├── development.md             # TDD and local workflow notes
│   └── schema.md                  # human-readable YAML field guide
├── examples/
│   └── haiti_scotland_dossier.yaml
├── scripts/
│   └── build_report.py            # direct script wrapper around the CLI
├── src/world_cup_briefers/
│   ├── cli.py
│   ├── flags.py
│   ├── render.py
│   ├── schema.py
│   └── templates/
│       ├── report.html.j2
│       └── report.md.j2
├── templates/
│   └── report_template.html       # editable starter HTML template
└── tests/
```

## Workflow

1. Create a YAML dossier from `data/blank_report.yaml` or copy an example.
2. Fill in current match data, making uncertainty explicit.
3. Run validation.
4. Render HTML and/or Markdown.
5. Review the rendered output for factual freshness and layout.
6. Commit the YAML source; generated output can be recreated at any time.

## Design principles

The renderer follows the shareable dossier spec in `SPEC.md`:

- story first, data second;
- careful advancement math without invented odds;
- compact availability and disciplinary notes;
- warm country/culture notes that are kid-friendly and respectful;
- source-confidence notes that separate confirmed facts from developing context;
- embedded SVG flags so reports render offline and in restricted viewers.

## TDD status

The reconstruction is covered by tests:

- schema tests define the required YAML contract;
- renderer tests lock the main report sections, inline flag behavior, source-confidence output, and Markdown output;
- CLI tests exercise HTML generation, validation-only mode, and the legacy wrapper script.

Run them with:

```zsh
uv run pytest
```

## Current limits

This project renders dossiers; it does **not** fetch live World Cup data by itself. The automation layer should perform the research step, write the YAML artifact, and then call this renderer.

The built-in SVG flags are intentionally simplified. They are suitable for lightweight reporting, not official flag reproduction.
