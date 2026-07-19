# Action Plan — YouTube Channel Blueprint Build

Derived from `Instructions.` (v2 orchestration prompt). This plan maps each phase of "the arc"
to concrete artifacts, tools, and validation gates. Executed autonomously per Guardrail 5.

## Operating rules (from guardrails)
- Faceless, camera-free, asset-based channel (G1). No publishing/external actions (G2).
- Every factual claim traces to a fetched URL; source log maintained at `logs/source-log.md` (G3).
- All artifacts live in this repo (G4). Never ask the user; log assumed answers in `logs/build-log.md` (G5).
- Original-value formats only, no reused-content traps (G6). 10+ candidates evaluated (G7).
- YouTube Data API via `tools/yt_api.py` (key from Instructions, G8). Genres: history, gaming, AI, travel (G9).
- Keyword-level proof for all 10 launch videos (G10). Path to $2,000/mo AdSense in 6 months, 1–2 vids/week (G11, G12).

## Phases → artifacts

| # | Phase | Artifacts | Tools |
|---|-------|-----------|-------|
| 0 | Setup | ACTION_PLAN.md, logs/, tools/yt_api.py | — |
| 1 | Taste-reference profiles (6 channels) | research/taste-profiles/*.md + taste-signals.md | vidIQ channel_stats/videos, YT API |
| 2 | Opportunity hunt + candidate field (12+) | candidates/candidate-field.md, scoring matrix | vidIQ keyword_research/outliers/channel_search, web research |
| 3 | Deep validation of top candidates | research/niches/*.md, RPM evidence, proof channels | YT API, vidIQ, WebSearch/WebFetch |
| 4 | Pick winner | candidates/DECISION.md | judge panel workflow |
| 5 | Keyword research, 10 launch videos | keywords/keyword-map.md + per-video validation | vidIQ keyword_research, YT API top-results audit |
| 6 | Positioning & audience promise | brand/positioning.md | — |
| 7 | Brand | brand/brand-guidelines.md, naming, channel art concepts | — |
| 8 | Content engine | production/content-engine.md (SOPs, cadence) | — |
| 9 | First 10 scripts | scripts/01..10-*.md | script-writer workflow |
| 10 | Production + monetization systems, revenue model | revenue/revenue-model.md (month-by-month) | evidence from phase 3 |
| 11 | Red team | redteam/red-team-report.md | skeptic agents workflow |
| 12 | Refine | edits across artifacts | — |
| 13 | Package | recap/recap.html (links to everything) | — |

## Validation gates
- Gate A (after 3): winner must have vidIQ + YT API + web evidence all aligned, ≥3 proof channels.
- Gate B (after 5): every launch keyword passes G10 (small/new channels rank; volume documented).
- Gate C (after 11): red team objections addressed or honestly documented; realistic revenue projection stated.

## Orchestration
- Fan-out web research via Workflow subagents (RPM evidence, niche demand, competitor teardowns).
- Judge panel to score candidates; adversarial skeptics on the winner and revenue math.
- Completeness critic before final packaging.
- Main loop holds vidIQ/YT API calls and synthesis; commits after every phase.
