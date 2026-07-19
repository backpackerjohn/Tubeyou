# Source Log

Every factual claim in the deliverables traces to an entry here (Guardrail 3).

Format per entry:

| Field | Meaning |
|---|---|
| ID | S-### referenced from deliverables |
| URL | The URL actually fetched |
| Title | Page/resource title |
| Accessed | Date fetched (UTC) |
| Supports | What claim(s) this evidences |
| Reliability | Assessment (primary data / reputable secondary / weak-anecdotal) |

Tool-derived data (vidIQ MCP, YouTube Data API) is logged with the query used instead of a URL,
since these are authenticated API calls, and stored as raw JSON under `research/raw/` where practical.

---

## Evidence-tier definitions (environment constraint, logged 2026-07-19)

This execution environment's egress proxy **blocks fetching general web pages** (HTTP 403 for all
non-dev hosts; verified against support.google.com, web.archive.org, suggestqueries.google.com).
Reachable: googleapis.com (YouTube Data API) and github.com. Therefore:

- **Tier A — API-verified:** data returned by the YouTube Data API v3. Strongest evidence; treated as fetched primary data.
- **Tier B — search-verified:** claims supported by real WebSearch results (URL + title + indexed snippet recorded) where the underlying page could NOT be fetched due to the proxy. These are real URLs from real searches, but page content is unverified. Every Tier B claim is labeled as such in deliverables.
- **Tier C — inference:** clearly labeled analytical inference from Tier A/B evidence.

Guardrail 3 compliance note: full fetch-verification of web sources is impossible in this
environment; this is documented rather than hidden, per Guardrail 5's 80%-with-documentation rule.

## Entries

### S-001 … S-018 — Taste-reference channel profiles (Tier A)
YouTube Data API v3 calls on 2026-07-19, three per channel (channels?forHandle, playlistItems, videos)
for @ancientindy, @oversimplified, @pitchmeetings, @bozuse, @recommendedplaying, @atlasadamhq.
Exact URLs (key redacted) are listed in the "Sources" section of each file in `research/taste-profiles/`.
Supports: all stats/claims in taste profiles and taste-signals.md. Reliability: primary API data.

### S-020 group — RPM evidence, history (Tier B)
Source table with URLs, titles, figures, and reliability grades in `research/niches/rpm-history.md`.
Supports: history RPM range $4–9 (snippet consensus; unverified pages).

### S-021 group — RPM evidence, gaming (Tier B)
Table in `research/niches/rpm-gaming.md`. Supports: gaming RPM $2–6; sub-angle nuances.

### S-022 group — RPM evidence, AI (Tier B)
Table in `research/niches/rpm-ai.md`. Supports: AI/tech RPM $8–20.

### S-023 group — RPM evidence, travel (Tier B)
Table in `research/niches/rpm-travel.md`. Supports: travel RPM $3–8.

### S-030 group — Tier A competition audit (Tier A)
YouTube Data API v3, 2026-07-19: 16 `search` calls (one probe per candidate, maxResults=8,
type=video), 3 batched `channels` calls (~110 channel IDs; snippet+statistics), 3 batched `videos`
calls (128 video IDs; statistics). Exact queries and all returned numbers are reproduced in
`candidates/tier-a-audit.md`. Supports: every demand/competition claim in the audit and downstream
scoring. Reliability: primary API data.

### S-031 group — Candidate generation web evidence (Tier B)
WebSearch-result URLs captured by the 4 pitch agents, embedded per-candidate in
`candidates/raw-pitches.json` and `candidates/candidate-field.md` (webEvidence fields), labeled
Tier B throughout. Supports: "why now" demand rationales only; never load-bearing for scoring.

### S-024 group — YPP eligibility & content policy (Tier B, multi-source corroborated → medium confidence)
Table in `research/niches/ypp-policy.md`. Supports: YPP thresholds (1,000 subs + 4,000 watch-hours),
July 2025 "inauthentic content" policy rename, AI-content monetization rules, disclosure requirements.
