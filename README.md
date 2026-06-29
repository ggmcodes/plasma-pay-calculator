# Plasma Pay Calculator — Site + Google Ranking Playbook

Plasma donation calculator and resource hub (CSL, BioLife, Grifols, Octapharma, KEDPLASMA).
Static HTML + PWA, deployed via **Cloudflare Pages** (push to `main` → auto-build → **purge cache**, HTML is edge-cached up to 1 year so changes are invisible until purged).

Live: [plasmapaycalculator.com](https://plasmapaycalculator.com)

---

# RANKING PLAYBOOK

This is the operating doc for getting pages onto Google page 1. It is data-backed (Google Search Console + the portfolio analytics dashboard), prioritized by effort, and meant to be executed top-to-bottom and re-measured every 2 weeks. **No move is off the table because of effort** — the high-effort authority work (Tier 3) is where the ceiling actually is.

## 0. The ranking reality (as of 2026-06-29)

- Plasma is the portfolio's **only strong Google performer**: ~525 Google clicks / 30d, 5.2% CTR, ~10,000 impressions. (For comparison, sister sites rank Google pos 76–86 and live off Bing + ChatGPT.)
- The money cluster is **branded "[brand] plasma pay chart 2026"** queries. Where the page is dialed, it wins big: `biolife plasma pay chart 2026` ranks **pos 2.7 at 19% CTR (188 clicks)**. Where it isn't, the same query shape sits at **pos 8–10 with ~1% CTR** — page-1-adjacent but leaking nearly all the traffic.
- **The #1 lever is consolidation, not new content.** The site has heavy near-duplicate cannibalization: multiple pages competing for one query, splitting authority, so none reaches the top 5.

**Proven cause/effect:** a single page owning a query (Biolife) hits pos 2.7. The same brand's query split across 2–3 pages (CSL) sits at pos 9. Fix the split → the survivor rises.

## 1. How to re-pull the data (do this before each pass)

```bash
# Fresh GA4 + Bing + GSC snapshot for the whole portfolio
cd ~/Projects/analytics-dashboard && ./run-fetch.sh        # writes data/snapshot.json
# Per-page / per-query GSC pulls (positions, CTR, cannibalization) are scripted ad-hoc
# against sc-domain:plasmapaycalculator.com with the webmasters.readonly scope.
```
Key reports to regenerate: **page-2 near-misses** (pos 11–20, impressions ≥120), **cannibalization clusters** (one query served by ≥2 pages each with impressions), **high-impression/low-CTR** pages (title-rewrite candidates).

---

## TIER 1 — Consolidation & on-page (highest ROI, low effort, days)

### 1A. Kill cannibalization — one query, one page (IN PROGRESS)

Each brand should have exactly **one** pay-chart authority page. Every other "pay rates / pay chart" variant for that brand must 301 into it.

**Done 2026-06-29:**
- CSL collapsed from 3 competing pages → root `/csl-plasma-pay-chart-2026` (the URL holding 233 internal links). Canonicals + 301s added.
- 301'd all brand `*-pay-rates-2026` pages → their `*-pay-chart-2026` winner (biolife, grifols, kedplasma, octapharma, csl). GSC-verified these had **zero unique winning queries** — they only ranked for "pay chart" terms the winner owns better, so consolidation is pure upside.

**Live cannibalization backlog (next):**
| Query | Competing pages | Action |
|---|---|---|
| `octapharma plasma pay chart 2026` | `/centers/octapharma/` (pos 10.2) vs `/blog/octapharma-plasma-pay-chart-2026` (pos 10.3) | Differentiate: retitle the centers page to location intent ("Octapharma Locations Near You"); keep the blog page as the pay-chart authority. Internal-link blog→centers, not competing. |
| `csl plasma weight chart 2026` | `/blog/csl-plasma-weight-chart-2026` (pos 2.1) vs `/blog/plasma-donation-weight-chart-visual-guide-2026` (pos 9.1) | Canonical the generic visual-guide → the CSL weight chart for CSL terms, or de-target its title. |
| `biolife vs csl` (4 pages!) | `biolife-vs-csl-plasma-2026`, `biolife-vs-csl-plasma-comparison`, `biolife-vs-csl-plasma-comparison-2026`, `csl-plasma-vs-biolife-2026-comparison` | Pick one, 301 the other three into it. Same audit for every `X-vs-Y` brand pair. |

**Rule going forward:** before publishing any new brand page, grep existing pages for the target query. If one exists, **refresh it, don't add a sibling.**

### 1B. Push the page-2 near-misses onto page 1

Pages at pos 11–20 with real impressions need a nudge (consolidation above often does it; otherwise internal links + on-page). Re-pull the near-miss report each pass. Current standouts after consolidation should be re-checked: the consolidated brand pay-chart pages (grifols pos ~7.5, octapharma, kedplasma) and the `how much does grifols plasma pay new donor` (pos 4.1, already near top).

### 1C. CTR rewrites on high-impression, low-CTR pages

Where a page ranks pos 5–10 but CTR is <3%, the title/meta is the bottleneck. Mirror the winner's pattern: **`[Brand] Plasma Pay Chart [Current Month] 2026: $X–$Y/Visit + $Z New Donor Bonus`** with a fresh dated table and FAQ schema. The Biolife winner's 19% CTR is the template. Update the **month** site-wide monthly (the root CSL page already auto-shows "June 2026" — extend that pattern to all money pages).

### 1D. Freshness cadence

"2026" pages must stay genuinely current: refresh pay tables, bump the visible "Last updated [Month] 2026", and re-ping IndexNow/Bing (`submit-indexnow.js`, `submit-to-bing.js`). Stale "2026" content decays fast on YMYL money queries.

---

## TIER 2 — Architecture & content systems (medium effort, weeks)

### 2A. Internal-linking architecture
- Build a **brand hub → spoke** model: one hub per brand (the pay-chart page) linking to all that brand's spokes (bonus, weight chart, busy times, locations), and every spoke linking back to the hub with exact-match anchor ("CSL plasma pay chart").
- Push internal links from the **highest-authority pages** (homepage, calculators, top blog) into the page-2 near-misses with descriptive anchors. Audit with the repo's `audit_ppc_internal_links.py` / `analyze_linking_opportunities.py`.
- Cap thin doorway pages; consolidate the long tail of programmatic city/state pages that get 0 clicks and only dilute crawl budget.

### 2B. Structured data depth
- FAQ + `HowMuch`/`Table`-style structured data on every pay-chart page (drives PAA + featured snippets, which is how to leapfrog from pos 5 to pos 1 without more links).
- `BreadcrumbList`, `Organization`, and author `Person` schema for E-E-A-T (see Tier 3).
- Validate against Rich Results; the welding-chart-style "Quick Answer" block is the AI-citation magnet — replicate it on every reference page.

### 2C. Content depth & intent match
- The winners are comprehensive single pages. Bring laggard brand pages to parity: real per-tier pay tables, new-donor bonus calendar, debit-card details, weight requirements, FAQ. Depth + freshness is what closes the pos 8 → pos 3 gap once cannibalization is gone.
- Map every page to **one** primary intent. Pay-chart = transactional money query. Comparisons = consideration. Don't let a comparison page rank for a pay-chart query.

### 2D. Programmatic expansion (controlled)
- The state/city calculator system can target "[brand] plasma [city] pay" long-tail — but only with unique local data per page, indexed selectively. Mass-thin pages hurt more than help; expand where GSC shows impressions, prune where it shows none.

---

## TIER 3 — Authority & off-page (high effort, months — this is the real ceiling)

Plasma ranks pos 7–10 on commercial queries because on-page is good but **domain authority/trust is the gap**. Page 1 top-5 on YMYL money queries requires off-page signals. This is slow but it is the difference-maker; do it in parallel with Tiers 1–2.

- **Digital PR / backlinks:** pitch data studies ("2026 plasma pay rates by state/center" — the site already has the dataset) to personal-finance, gig-economy, and college-budget writers. Original data + a clean chart is linkable. Reuse the portfolio's `digital-pr-kit`.
- **E-E-A-T / YMYL trust:** real author bios with credentials, medical-reviewer byline, "fact-checked", sourced citations (FDA, center official rate pages), visible last-updated, about/editorial-policy pages. Google demands this on health+money topics; it directly affects ranking, not just CTR.
- **Brand signals:** get the brand into the consideration set — Reddit/forum presence (r/plasma), YouTube explainers, a newsletter, social proof. Branded search volume lifts non-branded rankings.
- **Unlinked-mention reclamation + competitor backlink gap:** find sites citing plasma pay data without linking; find who links to competitor calculators and pitch them.
- **Listicle/aggregator placement:** get listed in "best plasma pay calculators / gig apps" roundups.

---

## TIER 4 — Technical SEO baseline (keep green, ongoing)

- **Indexation hygiene:** keep `sitemap.xml` accurate, submit via GSC + IndexNow on every meaningful change. Watch GSC Coverage for "Crawled – not indexed" (a thin-content/dupe signal) and prune offenders.
- **Redirect hygiene:** no chains, no loops. Every retired/duplicate URL 301s **directly** to its final target (we just removed a 2025→2026→root chain on CSL). Audit `_redirects` quarterly.
- **Core Web Vitals:** static HTML is fast — keep it that way. Defer non-critical JS/ads, lazy-load images, preconnect only what's used. CWV is a tiebreaker at the top of page 1.
- **Canonical discipline:** every page self-canonical unless it is a deliberate consolidation target. Never canonical a strong page into a weak one (the mistake we just reversed on the sister site).
- **Crawl budget:** with thousands of programmatic pages, make sure crawl goes to money pages. Noindex/prune dead-weight tail.

---

## The AI-citation flywheel (don't neglect — it's real traffic now)

ChatGPT and other assistants already cite the reference/chart pages and send engaged traffic. This channel rewards the same things as Tier 2: clean dated tables, explicit "Quick Answer" blocks, structured data, and being the canonical single source for a fact. Every consolidation that makes one page THE answer for "[brand] pay chart 2026" also makes it the page an LLM cites. Track AI-assistant sessions in the dashboard snapshot (`ai_citations`).

---

## Measurement & cadence

- **Every 2 weeks:** re-pull GSC, diff positions on the money cluster, regenerate the near-miss + cannibalization reports, knock out the top 3 backlog items.
- **Leading indicators (weeks):** impressions up, avg position down (better), CTR up after title rewrites.
- **Lagging indicators (1–3 months):** clicks up, money queries entering top 5, branded search volume rising.
- **Target:** move the branded "[brand] plasma pay chart 2026" set (CSL, Grifols, Octapharma — ~2,000 impressions combined currently at pos 8–10) into the top 5, matching Biolife. Modeled upside ≈ +600–800 Google clicks/mo from consolidation alone, before any Tier 3 lift.

---

## Project / build notes

- **Stack:** static HTML/CSS/JS + PWA, Schema.org structured data, Cloudflare Pages.
- **Deploy:** push to `main` → Cloudflare Pages builds → **purge the zone cache** (HTML cached up to 1yr) or changes won't show.
- **Useful repo scripts:** `audit_ppc_seo.py`, `audit_ppc_internal_links.py`, `analyze_linking_opportunities.py`, `comprehensive_link_audit.py`, `submit-indexnow.js`, `submit-to-bing.js`, `regenerate_sitemap.py`.
- **History:** migrated from bestplasmacenters.com (full 301 map in `_redirects`); Spanish site (369 pages) migrated Jan 2025.

## License
MIT
