#!/usr/bin/env python3
"""Public domain-status scan for Phoenix sites. Read-only: DNS lookup + one HTTPS GET each.
Usage: python3 scan_domains.py > domain_scan.csv   (stdlib only)"""
import socket, ssl, urllib.request, datetime, csv, sys, zoneinfo
SITES = [
 ("Phoenix Mobile Advertising","https://phoenix-mobile-advertising-site.phoenixboyd.chatgpt.site/"),
 ("Phoenix Systems AI (custom domain)","https://phoenixsystemsai.com/"),
 ("Phoenix Systems AI (temp host)","https://phoenix-systems-ai.phoenixboyd.chatgpt.site/"),
 ("Phoenix AI Builders","https://phoenix-ai-builders-site.phoenixboyd.chatgpt.site/"),
 ("Phoenix Hospitality","https://phoenix-hospitality-site.phoenixboyd.chatgpt.site/"),
 ("Phoenix Boutique","https://phoenix-everyday-extraordinary.phoenixboyd.chatgpt.site/"),
 ("Phoenix Mobile Network","https://phoenix-express-site.phoenixboyd.chatgpt.site/"),
 ("Phoenix Amazon","https://phoenix-amazon-site.phoenixboyd.chatgpt.site/"),
 ("Phoenix Media","https://phoenix-media-site.phoenixboyd.chatgpt.site/"),
 ("Phoenix Forecast Intelligence","https://phoenix-forecast-intelligence-site.phoenixboyd.chatgpt.site/"),
 ("Phoenix Auto Traders","https://phoenix-auto-traders.phoenixboyd.chatgpt.site/"),
 ("Phoenix parent site","https://phoenix-parent-site.phoenixboyd.chatgpt.site/"),
]
tz = zoneinfo.ZoneInfo("America/Los_Angeles")
w = csv.writer(sys.stdout)
w.writerow(["checked_pt","name","url","host","host_type","dns_resolves","http_status","note"])
for name,url in SITES:
    host = url.split("/")[2]
    htype = "custom domain" if not host.endswith("chatgpt.site") and not host.endswith("vercel.app") else "temporary host subdomain"
    try: socket.getaddrinfo(host,443); dns="yes"
    except Exception as e: dns="no"
    status=note=""
    if dns=="yes":
        try:
            req=urllib.request.Request(url,headers={"User-Agent":"Mozilla/5.0 (PhoenixDomainScan/1.0)"})
            with urllib.request.urlopen(req,timeout=20) as r: status=str(r.status)
        except urllib.error.HTTPError as e: status=str(e.code)
        except Exception as e: status="error"; note=type(e).__name__
    else: note="host does not resolve"
    w.writerow([datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S %Z"),name,url,host,htype,dns,status,note])
