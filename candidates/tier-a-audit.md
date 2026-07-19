# Tier A Competition Audit — YouTube Data API, 2026-07-19

One search probe per candidate (search?part=snippet&type=video&maxResults=8, US relevance order),
then batched channels?part=snippet,statistics and videos?part=statistics lookups for every ranked
result. All numbers are exact API returns fetched 2026-07-19. Key redacted in URLs; query pattern:
`https://www.googleapis.com/youtube/v3/{search|channels|videos}?...&key=REDACTED`.

**What this audits (per scoring-framework dimensions 1–2):** Do the top results show (a) real
viewing demand and (b) small (<100K subs) and/or young (<2 yr) channels ranking — the precondition
Guardrail 10 will later apply to individual keywords?

Legend: 🟢 small/young channel with strong views in top results · subs = channel subscribers ·
"ch. created" = channel creation date.

---

## C01 The Ledger Breaks — probe: "how did the ottoman empire go bankrupt"

| Rank | Channel | Subs | Ch. created | Video views | Video date |
|---|---|---|---|---|---|
| 1 | Madmam | 145,000 | 2025-03 | 2,929,812 | 2025-05 |
| 2 | History Matters | 1,910,000 | 2015 | 2,044,724 | 2019 |
| 3 | The Scholars Vault | 1,720 | 2024-05 | 121,385 | 2024-10 |
| 4 | Financial Empires | 1,000 | 2026-01 | 340 | 2026-02 |
| 5 | Financial Timeline | 12 | 2025-08 | 9 | 2025-12 |
| 6 | Capital Decode | 55 | 2025-11 | 17 | 2025-12 |
| 7 | Financial Historian | 161,000 | 2025-07 | 95,056 | 2025-12 |
| 8 | The Wealth Records | 27,800 | 2026-01 | 1,431 | 2026-01 |

**Reading:** The finance-history lane is *hot right now*: Madmam went 0→145K subs in ~16 months with
a 2.9M-view collapse video; **Financial Historian went 0→161K subs in under 12 months** (381
videos); The Wealth Records 0→27.8K in ~6 months. A 1,720-sub channel ranks #3 with 121K views.
Counter-signal: ranks 4–6 are near-identical-title clone channels (12–1,000 subs) with dead views —
a visible slop wave where undifferentiated copies fail. Demand: multi-million views at top.
**Verdict: strong demand + repeated recent new-channel breakouts + differentiation required.** 🟢🟢

## C02 Margin of Failure — probe: "how was the pantheon dome built"

| Rank | Channel | Subs | Ch. created | Video views |
|---|---|---|---|---|
| 1 | Learn History Simply | 418,000 | 2021 | 4,545,870 (Short) |
| 2 | SLICE History | 286,000 | 2023 | 68,582 |
| 3 | Naked Science | 1,730,000 | 2009 | 221,193 |
| 4 | Manuel Bravo | 699,000 | 2020 | 1,141,200 |
| 5 | History Learnt in Minutes | 377 | 2024 | 20,992 (Short) |
| 6 | toldinstone | 642,000 | 2018 | 672,804 |
| 7 | Eternal Rome | 19,700 | **2025-06** | 4,667 |
| 8 | Industrial Evolution | 7,030 | **2025-12** | 28,396 |

**Reading:** Deep evergreen demand (1.1M on a dedicated architecture explainer, 673K toldinstone).
Two brand-new faceless-style channels already surface: Industrial Evolution (7 months old, 7K subs)
ranks top-8 with 28.4K views. Mid-size incumbents present but not exclusive.
**Verdict: solid evergreen demand; young channels get in; winner titles are mechanism-curiosity.** 🟢

## C03 True Campaign — probe: "real history behind age of empires 2 civilizations"

Top results mix AoE2 *gameplay* channels (Spirit of the Law 393K/435K views; Hera 259K) with
history-explainer hybrids: **History for Gamers (18,900 subs) pulls 127,516 and 261,829 views** on
battle-recreation videos (6.7–13.8x subs); Connected Histories (2,010 subs) 29,663 views; History in
Bits (24,900 subs) 9,561. **Verdict: the intersection audience is real and small channels overperform,
but search intent is fragmented between gameplay and history — demand ceiling unclear.** 🟢(moderate)

## C04 Paper Trail — probe: "declassified cia documents explained"

Every strong result is a mega-channel: The Infographics Show (15.5M subs; 1.23M / 2.99M / 2.59M
views), MorgueOfficial (759K; 919K), Origins Explained (3.88M), Video Advice (3.78M; 2.39M).
Smallest ranking channel: 210K subs. Results also skew to woo/"Gateway Process" content.
**Verdict: FAILS the small-channel precondition on its core probe — big-channel dominated.** 🔴

## C05 Sunk Cost — probe: "biggest video game financial disasters"

| Notable | Subs | Ch. created | Video views |
|---|---|---|---|
| gameranx | 8,620,000 | 2012 | 1,534,637 |
| **GameIsition** | **125** | 2024-11 | **153,875** |
| **Selwen** | 58,600 | 2015 | 544,691 |
| WhatCulture Gaming | 1,690,000 | 2015 | 549,989 |
| WatchMojo | 25,800,000 | 2007 | 229,373 |

**Reading:** A 125-subscriber channel holds rank 4 with 153,875 views (EVE Online heist doc);
Selwen's "Most Expensive Flop" pulled 545K on 58.6K subs. Demand robust at the top (1.5M).
**Verdict: strong small-channel breakout evidence; business-of-gaming angle may lift gaming's weak RPM.** 🟢🟢

## C06 Patch Verdict — probe: "is cyberpunk 2077 worth playing in 2026"

| Notable | Subs | Ch. created | Video views |
|---|---|---|---|
| MrHulthen | 100,000 | 2011 | 237,468 |
| TimeWellPlayed | **671** | **2025-06** | 6,387 (rank 2) |
| Nyxson | 47,100 | 2017 | **1,636,293** |
| BigWynter | **5,850** | 2019 | **480,920** |
| MrGeeBee | 5,050 | 2022 | 1,851 |

**Reading:** The "[game] worth playing in [year]" query family is a small-channel playground: a
671-sub channel created 13 months ago ranks #2; a 5,850-sub channel has 480K views on the 2025
variant; a 47K channel 1.64M. Template repeats across hundreds of back-catalog games × every year.
**Verdict: excellent rankability + infinite template; demand per-title moderate but recurring.** 🟢🟢

## C07 The Real Campaign — probe: "assassins creed historical accuracy"

**Ezio Explains: 5,230 subs, channel created 2025-09, and its "Most Historically Accurate
Assassinations Explained" holds rank 2 with 101,049 views.** Strong incumbent demand above it
(GameSpot 937K; Overly Sarcastic Productions 1.13M; Skallagrim 632K). PokeMaster (159 subs) shows
even micro-channels get long-tail views (15.3K). **Verdict: proven demand + a 10-month-old
sub-6K channel outranking mega-channels = strong Guardrail-10-style evidence.** 🟢🟢

## C08 Delisted — probe: "delisted games you cant buy anymore"

| Notable | Subs | Ch. created | Video views |
|---|---|---|---|
| **Tactic Zombies** | 10,200 | 2022 | **1,628,076** |
| PositivePressure | 123,000 | 2014 | **2,866,126** / 51,753 |
| Rocket Sloth | 414,000 | 2017 | 892,365 |
| Austin Eruption | 314,000 | 2013 | 991,492 |

**Reading:** Massive topic demand (2.87M, 1.63M, 991K, 892K) and a 10.2K-sub channel owning a
1.63M-view hit. Gaming-history/preservation angle has emotional stakes (loss, legal erasure).
**Verdict: very strong demand + small-channel breakout; watch reused-footage policy design.** 🟢🟢

## C09 Black Box Down — probe: "AI disaster explained algorithm failure"

Results are intent-fragmented: Kurzgesagt's adjacent "AI Slop" (10.4M views), AI In Context (408K
subs, created 2025-04, **15 videos → 3.98M views on one**), Infographics (1.54M), TED (685K), plus
several near-zero-view results (17, 250, 4, 99 views). No established "AI failure forensics" genre
found — the lane is empty but unproven. AI In Context's 0→408K-in-15-months shows explosive appetite
for serious AI explainers. **Verdict: high-upside speculative — demand adjacent, format unproven,
RPM highest of all genres.** 🟡

## C10 Enemy Logic — probe: "games where the AI cheats"

Search intent has been captured by a *different* topic: "making cheats WITH AI" (Nessiel 118K views,
HaiX 203K, DeadOverflow, Enigma). Only one result matches the intended topic (game-AI rubber-banding
etc.): WhatAmISaiyan, 467 subs, 93,827 views — but from 2018. **Verdict: probe reveals intent
mismatch; the candidate's actual topic lacks clean search demand validation.** 🔴(moderate)

## C11 The Complete AI Stack — probe: "AI tools for accountants complete guide"

| Notable | Subs | Ch. created | Video views |
|---|---|---|---|
| **Corporate Catalyst** | 9,980 | 2022 | **3,248,435** |
| **Pynade Devs** | 8,480 | 2019 | **1,323,920** |
| SetupsAI | 542,000 | **2024-04** | 943,537 |
| Jason On Firms | 49,800 | 2021 | 107,227 |
| NorthStar Academy | 77,800 | 2018 | 32,958 / 147,569 |

**Reading:** Two sub-10K channels hold 3.2M and 1.3M-view videos in this exact space; SetupsAI went
0→542K subs since April 2024. Top-of-market RPM ($8–20, Tier B). Risk: tool churn shortens shelf
life; per-profession "complete workflow" positioning is genuinely unoccupied in these results
(everything ranking is a listicle, not a workflow).
**Verdict: strongest raw demand + rankability + RPM combination; decay risk must be engineered around.** 🟢🟢🟢

## C12 Deciphered by Machine — probe: "AI deciphered ancient scroll herculaneum"

Best results: Infographics 284K; Dig It With Raven (110K subs) 223K; everything else <16K views
including multiple sub-10K-view results from small channels. Demand is news-spike-driven and
moderate; the topic pool (AI×archaeology breakthroughs) is thin — a depth problem for 100+ videos.
**Verdict: charming intersection, insufficient topic depth and mid demand.** 🟡(weak)

## C13 Exit Economics — probe: "cheapest countries to live in 2026"

**Four Corners Travel: channel created 2026-01-13, 2,360 subs, ranks twice — 30,843 views on
"Safest Cheap Countries 2026".** Traveling with Kristin (305K) 167K views; Adventure Freaksss
(185K) 44.7K. Fresh-year variants re-mint demand annually. Some ranked videos have <1K views
(recency-boosted), showing the door is open but per-video demand is uneven.
**Verdict: new channels rank immediately; finance-adjacent travel RPM; moderate but recurring demand.** 🟢

## C14 The No-Go Atlas — probe: "forbidden places you cant visit"

| Notable | Subs | Ch. created | Video views |
|---|---|---|---|
| Top Fives | 3,140,000 | 2015 | **11,565,544** |
| The Paint Explainer | 1,950,000 | 2023 | 3,684,207 / 2,102,151 / 2,068,767 (a series) |
| Trust Me Bro | 1,330,000 | 2023 | 2,567,064 |
| **Hidden Planet Docs** | 66,900 | **2026-02-22** | **862,456** |
| Untouched Mysteries | 23,400 | 2025-04 | 807 |

**Reading:** Enormous demand (11.5M top result). **Hidden Planet Docs was created five months ago,
has 66.9K subs, and its TOP-10 forbidden-places video has 862K views** — the single strongest
new-channel breakout in this audit. But mega-channels farm the same lane, and it overlaps Ancient
Indy's taste-reference territory (differentiation duty under Guardrail 6).
**Verdict: proven monster demand + newest-channel breakout; heaviest big-channel competition.** 🟢🟢

## C15 What Killed This City? — probe: "what happened to hashima island"

neo (3M subs) 4.68M views at top, then a striking long tail of micro-channels: Tezorb (405 subs)
81,993 views; World in 2 Minutes (1,690 subs) 94,356; Whispers From The Dark (325 subs) 25,957;
Simories (660 subs) 17,787; Places (416K, created 2023) 201K.
**Verdict: micro-channels reliably harvest 18K–94K views per dead-city topic; deep topic pool
(hundreds of cities); demand strong at top.** 🟢🟢

## C16 Ranked: All of Them — probe: "all 63 national parks ranked"

National Park Wild (11,000 subs) owns the lane: 680,668 views on a ranked-parks video plus 3 more
ranked results (52.9K, 37.2K, 10.9K). Erik The Travel Guy (29.7K subs) 227K. Demand moderate;
closed-set format is finite by design. **Verdict: small channels rank well; demand moderate;
depth is the constraint.** 🟢(moderate)

---

## Audit summary → advance/kill recommendation (pre-judging)

| ID | Candidate | Demand | Small-ch. rankability | Flag |
|---|---|---|---|---|
| C01 | Ledger Breaks | Very strong | Proven, repeated | **Advance** |
| C02 | Margin of Failure | Strong evergreen | Proven | **Advance** |
| C03 | True Campaign | Fragmented | Good | Hold |
| C04 | Paper Trail | Strong | **None** | **Kill (G10 premise)** |
| C05 | Sunk Cost | Strong | Exceptional (125-sub case) | **Advance** |
| C06 | Patch Verdict | Recurring | Exceptional | **Advance** |
| C07 | Real Campaign | Strong | Exceptional (Ezio case) | **Advance** |
| C08 | Delisted | Very strong | Exceptional | **Advance** |
| C09 | Black Box Down | Adjacent/unproven | Unclear | Hold (upside) |
| C10 | Enemy Logic | Intent mismatch | — | **Kill (demand)** |
| C11 | Complete AI Stack | Very strong | Exceptional | **Advance** |
| C12 | Deciphered by Machine | Moderate, thin pool | Mixed | Kill (depth) |
| C13 | Exit Economics | Moderate recurring | Proven, immediate | **Advance** |
| C14 | No-Go Atlas | Enormous | Proven (newest case) | **Advance** |
| C15 | What Killed This City | Strong | Proven micro-tail | **Advance** |
| C16 | Ranked: All of Them | Moderate | Proven | Hold |

Final scoring and the top-3/4 cut happen in the judge panel (next step), which weighs these audit
results against RPM, production sustainability, topic depth, policy defensibility, and the taste
rubric.
