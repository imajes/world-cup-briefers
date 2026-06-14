# Automation Prompt

Use this prompt as the research-and-render loop for a scheduled or manual briefer run.

```text
Check current FIFA World Cup match schedule, standings, team news, disciplinary status, injury/player availability, credible local/reporting context, venue details, ticket/crowd information if available, and newly interesting storylines.

If a match is starting in roughly the next 45–90 minutes and it matches James's allegiance teams (United States, England, Scotland, Ireland if applicable) or has become interesting because of standings, advancement math, rivalry, upset potential, country/culture story, player news, venue/crowd context, or wider tournament implications, create a very up-to-date pre-match dossier.

For each dossier, write a YAML artifact matching this repository's schema, then render HTML and Markdown with the briefer CLI. Include kickoff time in Central Time; teams and flags; group/cup status; advancement implications; yellow/red card and player-health notes; win/draw/loss meaning; stadium, capacity, and reliable crowd/ticket context; country origin stories, stats, trivia, kid-friendly teaching points; external influences such as local events, home-country context, player/family stories, weather/travel; and one concise recommendation for how James should frame the match for his household.

If no match is imminent and worth surfacing, do not notify.
```

Recommended command after writing YAML:

```zsh
uv run world-cup-briefer path/to/dossier.yaml --output out/dossier.html
uv run world-cup-briefer path/to/dossier.yaml --format markdown --output out/dossier.md
```
