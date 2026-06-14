# YAML Schema Guide

The dossier source is a single YAML mapping. The renderer deliberately uses a lightweight schema rather than a strict JSON Schema so the format can evolve during the tournament without heavy migration work.

## Required top-level sections

`report`, `match`, `brief`, `cup_status`, `possible_futures`, `teams`, `players_to_watch`, `tactical_watchlist`, `crowd_weather`, `discipline_availability`, `country_culture_notes`, and `sources_confidence` are required.

`teams`, `cup_status.teams`, `discipline_availability`, and `country_culture_notes` must each contain at least two teams/countries. Other list sections must be non-empty.

## Field conventions

Use `team_a`, `team_b`, and `wider` under `possible_futures` so the same template works for any fixture. Use lists for injuries, card risks, and availability even when empty. Keep uncertainty in `sources_confidence.watch` or `sources_confidence.unknown` instead of hiding it in prose.

## Flags

The renderer embeds simplified SVG flags for known teams. Unknown teams fall back to a neutral three-letter placeholder from `team_code()`.

## Source confidence

Use four lanes:

- `high`: official or strongly confirmed facts.
- `medium`: credible reporting or likely-but-not-final context.
- `watch`: time-sensitive facts to refresh before publishing.
- `unknown`: information explicitly not found or not yet available.
