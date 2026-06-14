# Shareable World Cup Match Dossier Spec

**Version:** 0.1  
**Canonical flow:** current research → YAML dossier → HTML/Markdown renderers → PDF or chat artifact when needed.

## Purpose

A good match dossier should explain why a match matters, not just who is playing. It should work for casual fans, families watching together, and people who want both football context and country/culture context.

The report has three spines:

1. **Football:** schedule, group status, advancement math, tactics, player availability, cards, injuries.
2. **Human:** national story, pressure, player/family/diaspora context, crowd and local context.
3. **Learning:** geography, history, flags, language, culture, kid-friendly questions, and respectful trivia.

## Required output sections

### 1. Hero / match card

Include title, competition, stage, status, kickoff in Central Time, venue, capacity, teams, flags, and a one-sentence thesis.

### 2. 90-second brief

Use short cards or bullets for stakes, pressure, storyline, watch-for cue, and household/family hook.

### 3. Current cup status

Show the group or knockout context, current standings/status, advancement rules, remaining fixtures, and a qualitative advancement read. Do not invent odds.

### 4. Three possible futures

Use a table with exactly three rows when appropriate: Team A win, draw, Team B win. Each row should say what the result means for Team A, Team B, and the wider tournament.

### 5. Team story cards

For each team include classic story, modern story, truly interesting note, country snapshot, and what to watch tactically.

### 6. Players to watch

Use player cards or a table. Good categories include Can win it, Can break it, Pressure valve, Substitution swing, Tactical key, and Kid-friendly watch cue.

### 7. Tactical watchlist

Explain what casual viewers should notice: possession, counters, set pieces, pressing, fatigue, substitutions, or one game-state trigger.

### 8. Venue, crowd, and weather

Include stadium, capacity, expected crowd feel, ticket/crowd context when reliable, local travel or event context, and weather when relevant.

### 9. Discipline, availability, and health

Keep this compact. Separate confirmed absences from doubtful/managed players and card/suspension risk. Avoid overstating unconfirmed availability.

### 10. Country and culture notes

Use respectful teaching points. Avoid flattening countries into stereotypes. Add a kid-friendly question for each country.

### 11. Time capsule

Optional. Use when a long absence or historic return benefits from pop-culture context.

### 12. Sources and confidence

Always include a confidence section with four lanes:

- **high:** official or strongly confirmed facts.
- **medium:** credible reporting that could still change.
- **watch:** facts to refresh before kickoff.
- **unknown:** information explicitly not found.

## YAML conventions

Use `data/blank_report.yaml` as the starter and `data/schema_reference.yaml` as the annotated contract. The renderer requires the main sections but intentionally leaves detailed source citations and live research to the dossier author or automation layer.

## Visual guidance

Reports should be readable first and decorative second. Prefer high contrast, large headings, cards for story sections, tables for standings and result math, and inline SVG flags so the report works offline.

## Source policy

Separate confirmed facts from reported context. For time-sensitive football data, refresh lineups, injuries, weather, and attendance/ticket context as close to kickoff as practical. If official attendance is not available before kickoff, say that plainly.

## Production checklist

Before publishing a dossier:

1. Validate YAML.
2. Render HTML and Markdown.
3. Confirm kickoff time and venue.
4. Refresh lineups, injuries, suspensions, and cards.
5. Check group table and advancement math.
6. Mark crowd/ticket/weather context with proper confidence.
7. Read the household framing paragraph out loud once for clarity.
