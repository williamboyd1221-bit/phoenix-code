# Method

All times Pacific (PT), Tuesday November 17, 2026.

## Tools
Web search, a page reader, direct page and file fetches from a server (single requests, desktop browser identity), Python 3 standard library for the domain scan. An AI research agent ran the reads; a person reviews before anything is published.

## Rules
1. A fact counts only if it was read on a live page, directory or file on the run date, and the source URL is recorded.
2. A company's own numbers are labeled "self-stated". Review ratings were not readable, so none are claimed.
3. "Not found" means the pages named were checked and the item was not seen. It does not prove it exists nowhere.
4. Nothing was posted, sent, joined or spent. Read-only.

## Population (step 1)
- PSU Population Research Center, "2025 Certified Population Estimates" spreadsheet, from https://www.pdx.edu/population-research/population-estimate-reports. Klamath Falls row: 21,842 / 21,877 / 21,938 / 22,131 / 22,058 / 22,089 / **22,135** (the last four values are the 2022, 2023, 2024 and 2025 estimates).
- U.S. Census QuickFacts for the city and county. census.gov returned HTTP 403 to a direct fetch, so the Census numbers come from the search-index copy of those pages and cross-check to FRED (https://fred.stlouisfed.org/data/ORKLAM5POP).

## Competitors (step 2)
Providers were found with web search and business directories, then each provider's own site was read for services, published prices, AI use, proof and presence. Full per-provider notes and the 53-page source list are in [competitor_scan_public.md](competitor_scan_public.md).

## Domain scan (step 3)
For each address: DNS lookup, then one HTTPS GET. Classification: "custom domain" if the host is not a chatgpt.site or vercel.app subdomain, else "temporary host subdomain". Script: [scan_domains.py](scan_domains.py). Output: [domain_scan.csv](domain_scan.csv).

## Partner-program terms check (step 4)
Official terms pages were read and compared against the vendor's partner marketplace listing and third-party summaries. Where they disagree, the official, most recently dated page wins and the disagreement is recorded.
