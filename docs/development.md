# Development

## Local setup

```zsh
uv sync
uv run pytest
```

The package can also be run without installation:

```zsh
python scripts/build_report.py examples/haiti_scotland_dossier.yaml --validate-only
python scripts/build_report.py examples/haiti_scotland_dossier.yaml --output out/example.html
```

## TDD workflow

The project was reconstructed test-first around three seams:

1. **Schema seam:** YAML must fail early with useful dotted-path errors.
2. **Render seam:** HTML and Markdown must contain the major dossier sections and inline flag output.
3. **CLI seam:** the console command and legacy script wrapper must both render successfully.

When adding a field, update `data/schema_reference.yaml`, add or adjust an example, then add a renderer test for the user-visible behavior.

## Generated files

Generated reports belong in `out/` during development. Commit YAML sources and renderer code. Commit rendered samples only when they are useful review artifacts.
