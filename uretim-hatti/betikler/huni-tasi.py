#!/usr/bin/python3 -I
"""Huni satırlarını uretim-tutanagi/huni-surumler.json'dan paket surumler.json'a taşır (kayit dağıtımı sonrası, 15.11).

Aynı kimlik zaten varsa eklemez. Taşınan huni-surumler.json ~/Silinecekler/2026-11-15-0204/ altına gider (silme yok).
Son satır: 02-04-ydt-temel öğesinin kaynaktaki bütün sürüm adları (budama gövdesi için) → ~/is/uretim-0204/buda-0204.json
"""
import json
import shutil
from pathlib import Path

K = Path.home() / "01dev/_worktrees/kalem-0204/projeler"
COP = Path.home() / "Silinecekler/2026-11-15-0204"
COP.mkdir(parents=True, exist_ok=True)
adlar: list[str] = []
for n in (1, 2, 3):
    paket = K / f"02-04-ydt-temel-s{n}"
    hedef = paket / "surumler.json"
    veri = json.loads(hedef.read_text(encoding="utf-8"))
    kaynak = paket / "uretim-tutanagi/huni-surumler.json"
    eklenen = 0
    if kaynak.exists():
        var = {s.get("kimlik") for s in veri["surumler"]}
        for s in json.loads(kaynak.read_text(encoding="utf-8"))["surumler"]:
            if s["kimlik"] not in var:
                veri["surumler"].append(s)
                eklenen += 1
        hedef.write_text(json.dumps(veri, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        shutil.move(str(kaynak), str(COP / f"huni-surumler-s{n}.json"))
    adlar += [s["ad"] for s in veri["surumler"]]
    print(f"s{n}: +{eklenen} satır, toplam {len(veri['surumler'])}")
for paket, kimlik in (("02-04-ydt-temel", "ana-yatay"), ("02-04-ydt-temel-dikey", "dikey-tam")):
    veri = json.loads((K / paket / "surumler.json").read_text(encoding="utf-8"))
    adlar += [s["ad"] for s in veri["surumler"] if s.get("kimlik") == kimlik]
govde = {"ogeler": [{"kimlik": "02-04-ydt-temel", "surumler": adlar}]}
(Path.home() / "is/uretim-0204/buda-0204.json").write_text(json.dumps(govde, ensure_ascii=False), encoding="utf-8")
print(f"budama gövdesi: {len(adlar)} ad")
