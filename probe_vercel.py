import urllib.request
import re

url = "https://laptop-ai.vercel.app/"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
try:
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode("utf-8")
        print("Status:", resp.status)
        print("HTML length:", len(html))
        scripts = re.findall(r'src="([^"]+)"', html)
        print("Scripts found:", scripts)
        for s in scripts:
            target = "https://laptop-ai.vercel.app" + s if s.startswith("/") else "https://laptop-ai.vercel.app/" + s
            with urllib.request.urlopen(urllib.request.Request(target, headers={"User-Agent": "Mozilla/5.0"})) as s_resp:
                text = s_resp.read().decode("utf-8", errors="ignore")
                print("Fetched:", target)
                print("Content-Type:", s_resp.headers.get("Content-Type"))
                print("Starts with:", repr(text[:80]))
except Exception as e:
    print("Fetch error:", e)
