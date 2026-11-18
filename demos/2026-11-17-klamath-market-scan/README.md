# Demo #000: Klamath Falls market scan (Nov 17, 2026)

**Status: DONE (research demo).** Built by the Phoenix research agent for Phoenix Mobile Advertising LLC, Eugene, Oregon.
**Date:** Tuesday, November 17, 2026 (all times Pacific, PT).
**Why this is here:** GitHub is the permanent proof record. This folder shows what was researched, how, when, and what came out, so anyone can re-run it and check.

## What was done
| Step | What | When (PT) | Output |
|---|---|---|---|
| 1 | Population: read the PSU Population Research Center 2025 certified estimates spreadsheet and the U.S. Census QuickFacts pages for Klamath Falls and Klamath County | Nov 17, 2026, about 6:00 to 6:30 PM | [population.md](population.md) |
| 2 | Competitor scan: 53 pages across 20 providers that serve Klamath Falls (local, regional, remote), plus directory results | Nov 17, 2026, about 6:00 to 6:45 PM | [competitor_scan_public.md](competitor_scan_public.md) |
| 3 | Domain scan: DNS and HTTPS status of 12 Phoenix web addresses | Nov 17, 2026, 7:42 to 7:43 PM (timestamps in the CSV) | [domain_scan.csv](domain_scan.csv), re-run with [scan_domains.py](scan_domains.py) |
| 4 | Partner-program terms check: read a software vendor's published partner and affiliate terms and noted where pages disagree | Nov 17, 2026, about 7:45 PM | [partner_program_terms_check.md](partner_program_terms_check.md) |

## Headline results
- **Klamath Falls population:** city **22,135** and county **69,135** (PSU Population Research Center, 2025 certified estimate, as of July 1, 2025). Census Vintage 2025 estimate is 22,111 and 70,274; the two sources use different methods.
- **Providers found serving Klamath Falls:** 20 (11 local, 4 regional, 5 remote with a Klamath Falls page).
- **Domain scan:** 12 of 12 addresses answered HTTP 200 on Nov 17, 2026, between 7:42 and 7:43 PM PT. 1 is on a custom domain (phoenixsystemsai.com) and 11 are on temporary host subdomains.

## Demo unit (standard slots)
See [DEMO_UNIT.md](DEMO_UNIT.md). Media slots with nothing recorded yet say **pending**. Nothing is faked.

## Reproduce
```
python3 scan_domains.py > domain_scan.csv
```
Needs only Python 3 (standard library). Method details: [METHOD.md](METHOD.md).

*Provable. Clickable. No fakes. Call 541-632-9043 or book a Business X-Ray.*
