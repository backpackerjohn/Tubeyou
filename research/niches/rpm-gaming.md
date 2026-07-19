# RPM Research: Gaming (commentary / retrospectives / game history & analysis)

Researched: 2026-07-19

## IMPORTANT DATA-QUALITY CAVEAT

**No source page could actually be fetched.** Every WebFetch attempt in this session returned
HTTP 403 from the sandbox's egress proxy — the organization's egress policy for this session
blocks general-web hosts (confirmed by a control fetch of en.wikipedia.org also returning 403;
per `/root/.ccr/README.md`, proxy 403 = "destination host not allowed by egress policy — do not
retry or route around"). Blocked hosts attempted: vidiq.com, isthischannelmonetized.com,
blackhatworld.com, fluxnote.io, tubeanalytics.net, ytmoneycalculator.com, checktheworth.com,
influencermarketinghub.com, digitalinformationworld.com, old.reddit.com, en.wikipedia.org.

Therefore **every figure below comes only from WebSearch result snippets/summaries, not from
verified page content**. Under this task's own evidence standard (figures must come from fetched
URLs), this evidence is thin. Treat all numbers as UNVERIFIED and confidence as LOW. Re-run this
research in an environment with open egress before relying on it.

## Summary (unverified, snippet-derived)

For **long-form gaming commentary / retrospectives / analysis with a mostly-US/EN audience**,
the snippet evidence converges on a credible RPM band of roughly:

- **~$2–$6 RPM** (creator take) as the working planning range
- Pure gameplay / Let's Play / global-audience content skews to **$0.80–$3**
- The higher-RPM sub-angles — **game reviews & "is it worth buying" analysis, esports/competitive
  analysis, business-of-gaming and industry-history angles** — are claimed at **$5–$8 RPM**
  (vidIQ snippet) up to **$6–$10** (fluxnote snippet), but these upper figures are unverified
- One creator-reported data point (BlackHatWorld thread snippet): 7.6M views over 10 months →
  ~$6.1k, i.e. **~$0.80 RPM** — a floor case, likely broad/young/global audience

## Per-source table

All rows: figure taken from search-result snippet only; page fetch blocked (proxy 403).

| URL | Title | Figure reported (per snippet) | RPM or CPM | Reliability |
|---|---|---|---|---|
| https://vidiq.com/blog/post/make-money-gaming-channel-youtube/ | How to Make Money with a Gaming Channel on YouTube (vidIQ) | Game reviews/analysis $5–8; esports commentary $3–6; Let's Play $2–4; mobile gaming $1–3 | RPM (stated as RPM) | Reputable secondary (vidIQ) — but UNFETCHED |
| https://www.blackhatworld.com/seo/i-made-6k-with-my-gaming-channel-how-much-are-you-getting-paid-per-1000-views.1566260/ | "I made $6k with my gaming channel..." | 7.6M views / 10 months → $6.1k ≈ $0.80 RPM | RPM (derived from creator-reported totals) | Weak-anecdotal creator report — UNFETCHED |
| https://ytmoneycalculator.com/blog/gaming-youtuber-earnings/ | How Much Do Gaming YouTubers Make in 2026? | Gaming average $1.90 RPM; range $0.80 (gameplay highlights, global) to $3.20 (esports analysis, US) | RPM | Unknown-quality secondary — UNFETCHED |
| https://fluxnote.io/guides/youtube-rpm-gaming-niche-2026 | Gaming YouTube RPM [2026]: $2–$8 RPM | Long-form gaming $2–8 RPM; US median ~$3.50; adult-audience game-review channels $6–10 | RPM | Unknown-quality secondary — UNFETCHED |
| https://fluxnote.io/guides/youtube-rpm-seasonality-gaming | Gaming YouTube RPM 2026: $8-15 Peak, $1.50 Low | Seasonality: Nov–Dec peak $8–15; January trough $1.50–3 | RPM | Unknown-quality secondary — UNFETCHED |
| https://isthischannelmonetized.com/data/youtube-cpm/ | YouTube CPM in 2025 (Full Data Analysis) | Gaming CPM ~$1–4; gameplay niche CPM ~$1.40 (advertiser cost, NOT creator take; creator RPM ≈ 40–55% of CPM after revenue share and unmonetized views) | CPM | Reputable secondary (aggregated channel data) — UNFETCHED |
| https://www.tastyedits.com/most-profitable-youtube-niches/ | The 15 Most Profitable YouTube Niches (by CPM) | Gaming CPM ~$4–15 (lower than expected for its popularity; young audience) | CPM | Reputable secondary — UNFETCHED |
| https://www.tubeanalytics.net/blog/youtube-rpm-benchmarks-by-niche | YouTube RPM by Niche: What Is a Good RPM in 2026? | Gaming/entertainment $1–5 RPM vs finance $8–22 RPM | RPM | Unknown-quality secondary — UNFETCHED |

## RPM vs CPM handling

- vidIQ, ytmoneycalculator, fluxnote, tubeanalytics figures were presented (in snippets) as **RPM** (creator take).
- isthischannelmonetized and tastyedits figures are **CPM** (advertiser cost on monetized playbacks).
  Converting CPM→RPM: creator receives ~55% of ad revenue, and not all views are monetized, so
  RPM is typically ~40–55% of CPM at best. Gaming CPM of $1–4 implies RPM well under $2 for
  gameplay-heavy content — consistent with the $0.80 anecdote.

## Nuances

- **Sub-angle matters more than "gaming" as a label.** Purchase-intent formats (reviews,
  "is X worth playing", buying-guide-adjacent retrospectives) and analysis for adult audiences
  are consistently claimed to be the top of the gaming range ($5–8+). Pure Let's Plays and
  clip/highlight content sit at the bottom ($0.80–$3).
- **Finance/business-adjacent gaming angles raise RPM**: "business of gaming", industry
  collapse/history-of-studio stories, gaming-stocks/economics angles attract finance-tier
  advertisers (finance niches claimed at $8–22 RPM) — plausible but not directly documented
  in any gaming-specific source found.
- **Audience geography**: US/UK/CA/AU audiences pay multiples of global-average; mobile-gaming
  and global-skewing content was cited at $1–3 RPM.
- **Audience age**: gaming skews young (lower advertiser demand); retrospectives/history content
  targeting 25–40 year-old nostalgia viewers should sit above gaming median (claimed, unverified).
- **Seasonality is extreme**: claimed Nov–Dec peak of $8–15 vs January trough of $1.50–3
  (single unverified source).
- **Ad-supported RPM understates gaming creator income**: sponsorships, memberships, Patreon
  dominate above ~10k subs per the vidIQ snippet.

## Bottom line

Evidence is thin by this project's standard (zero fetched sources — environment egress policy
blocked all fetches). Snippet-level convergence supports planning at **$2–4 RPM baseline** for
US/EN long-form gaming commentary/retrospectives, with **$5–8 achievable** for review/analysis/
industry-angle content — but every number needs re-verification. Confidence: LOW.
