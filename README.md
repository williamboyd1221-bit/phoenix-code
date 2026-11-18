# Phoenix Code

*Tooling notes from Phoenix Mobile Advertising.* Examples of how an AI coding agent can use MCP tools to drive a browser and read public websites, so local businesses get clear, checkable advice.

This supports work for small businesses in **Eugene, Springfield, Salem, Portland and Roseburg, Oregon**: the same class of tools the big platforms use, set up for local businesses. We are not affiliated with Google, Meta or OpenAI.

**Call 541-632-9043 or book a Business X-Ray.**

## What is here

| File | What it is |
|------|-----------|
| [examples/mcp.json](examples/mcp.json) | Sample MCP client config: Playwright MCP and Firecrawl MCP |
| [examples/site-intel.md](examples/site-intel.md) | A repeatable local business site intelligence checklist |

## The two MCP servers

- **Playwright MCP** (`@playwright/mcp`) lets an agent open pages in a real browser, click, fill forms and take snapshots. Docs: [github.com/microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp)
- **Firecrawl MCP** (`firecrawl-mcp`) lets an agent scrape and crawl public pages into clean text. It needs your own API key. Docs: [docs.firecrawl.dev/mcp-server](https://docs.firecrawl.dev/mcp-server) and [github.com/firecrawl/firecrawl-mcp-server](https://github.com/firecrawl/firecrawl-mcp-server)

Package names were checked against the npm registry on 2026-11-17: `@playwright/mcp` and `firecrawl-mcp`.

## Ground rules

- **Never commit a key.** Use an environment variable. The sample config uses the placeholder `FIRECRAWL_API_KEY=<your-key>`.
- **Public pages only.** No logins, no private data, and respect each site's terms and robots rules.
- **No fakes.** The checklist reports what was seen on the page. It never invents findings.
- **A person decides.** The checklist is a starting point for a conversation with the owner.

## Sibling repos

[phoenix-portfolio](https://github.com/williamboyd1221-bit/phoenix-portfolio) | [phoenix-mobile](https://github.com/williamboyd1221-bit/phoenix-mobile) | [rise-brand](https://github.com/williamboyd1221-bit/rise-brand) | [phoenix-vows](https://github.com/williamboyd1221-bit/phoenix-vows)

Site: [Phoenix Systems AI](https://phoenix-systems-ai.vercel.app)
