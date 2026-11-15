"""Sahne oturumlarında kod dosyası nasıl yazıldı: yazim-analiz.py <ad>…"""
import glob, json, re, sys
from pathlib import Path
D = Path.home() / "is" / "uretim-0204"
for ad in sys.argv[1:]:
  sid = json.loads((D / f"D-{ad}.json").read_text())["session_id"]
  yol = (glob.glob(str(Path.home() / ".claude" / "projects" / "*" / f"{sid}.jsonl")) or [None])[0]
  if not yol: print(ad, "transcript yok"); continue
  sayac = {"Write": 0, "Edit": 0, "bash_yazim": 0, "gate_blok": 0}
  for satir in open(yol, encoding="utf-8"):
    if "BLOCK write_gate" in satir: sayac["gate_blok"] += 1
    try: d = json.loads(satir)
    except Exception: continue
    for p in (d.get("message") or {}).get("content") or []:
      if isinstance(p, dict) and p.get("type") == "tool_use":
        n = p.get("name"); i = p.get("input") or {}
        if n in ("Write", "Edit"): sayac[n] += 1
        if n == "Bash" and re.search(r"(cat|tee)\s*>+\s*\S+\.(py|js)|>\s*\S+\.(py|js)\s*<<|open\([^)]*\.(py|js)['\"],\s*['\"]w", i.get("command", "")):
          sayac["bash_yazim"] += 1
  print(ad, sayac)
