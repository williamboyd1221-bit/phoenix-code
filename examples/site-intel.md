# Local business site intelligence (example workflow)

A short, repeatable scan of a **public** business website. The output is a checklist the owner can read in two minutes. Everything in the sample output below is **example data**, not a real business.

Setup: see [mcp.json](mcp.json) for Playwright MCP and Firecrawl MCP. Docs: [Playwright MCP](https://github.com/microsoft/playwright-mcp) and [Firecrawl MCP](https://docs.firecrawl.dev/mcp-server).

## What to check

| Area | Question | How |
|------|----------|-----|
| Contact clarity | Is a phone number and a way to reach the business visible without scrolling or clicking? Is the phone a tap-to-call link? | Firecrawl scrape of the home page; look for `tel:` links |
| Mobile speed hints | Does the page load a mobile view? Are images huge? Any blocking pop-ups? | Playwright at a phone-sized viewport; take a snapshot and note what appears first |
| Booking / CTA | Is there one clear next step (call, book, order) above the fold? | Playwright snapshot: find buttons and links with action words |
| Google Business Profile | Does the site link to the business's Google Business Profile or Maps listing? | Scan page links for Google Maps or Business Profile URLs |

## Steps for the agent

1. Take a public URL the owner gave you. Do not log in to anything.
2. **Firecrawl:** scrape the home page and contact page into text. Record phone, hours, address presence and any `tel:` or booking links.
3. **Playwright:** resize to a phone viewport, open the page, take a snapshot, and note the first call to action you can see.
4. Check the page links for a Google Business Profile or Maps link.
5. Write the checklist below using only what you saw. If you could not tell, write "not checked".
6. Hand it to a person. Do not send anything to the business automatically.

## Output template

```markdown
## Site check: <business name> (<town>)
URL: <public url>   Checked: <date>

- [ ] Phone number visible near the top
- [ ] Phone is a tap-to-call link
- [ ] Hours and service area stated
- [ ] Page opens cleanly on a phone-sized screen
- [ ] Images look sized for mobile (not obviously oversized)
- [ ] One clear call to action visible without scrolling
- [ ] Booking or contact path works
- [ ] Link to Google Business Profile or Maps present

Notes (only what was seen):
- ...

Suggested next step for the owner:
- ...
```

## Sample output (EXAMPLE DATA, not a real business)

```markdown
## Site check: Example Bakery (Salem)
URL: https://example.com   Checked: <date>

- [x] Phone number visible near the top
- [ ] Phone is a tap-to-call link
- [x] Hours and service area stated
- [x] Page opens cleanly on a phone-sized screen
- [ ] Images look sized for mobile   (not checked)
- [x] One clear call to action visible without scrolling
- [ ] Booking or contact path works   (not checked)
- [ ] Link to Google Business Profile or Maps present

Suggested next step for the owner:
- Make the phone number tap-to-call and link your Google Business Profile.
```

## Optional script sketch

A minimal Playwright sketch for the link checks (run locally, public pages only):

```ts
import { chromium } from "playwright";

const url = process.argv[2]; // a public business URL
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 390, height: 844 } });
await page.goto(url, { waitUntil: "domcontentloaded" });

const links = await page.$$eval("a[href]", (as) => as.map((a) => a.getAttribute("href") ?? ""));
const hasTel = links.some((h) => h.startsWith("tel:"));
const hasMaps = links.some((h) => /google\.[a-z.]+\/maps|maps\.app\.goo\.gl|g\.page|business\.google\.com/.test(h));

console.log({ url, hasTapToCall: hasTel, hasGoogleMapsOrProfileLink: hasMaps });
await browser.close();
```

Back to the [README](../README.md).
