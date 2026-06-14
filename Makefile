.PHONY: test render-example validate-example

test:
	python -m pytest

validate-example:
	python scripts/build_report.py examples/haiti_scotland_dossier.yaml --validate-only

render-example:
	python scripts/build_report.py examples/haiti_scotland_dossier.yaml --output examples/rendered/haiti_scotland_dossier.html
