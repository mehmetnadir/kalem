#!/usr/bin/python3 -I
"""Ajan kapasite izleyicisi (Nadir 15.11: "kaç ajan çalıştırabilir bulsun ve sana söylesin").

60 sn'de bir ölçer, ~/.claude/state/ajan-kapasite.json dosyasına yazar (bütün oturumlar okur),
kapasite DEĞİŞİNCE stdout'a tek satır basar (Monitor şefi uyandırır). Salt ölçer; süreç başlatmaz, durdurmaz.

  srv21.ek = min((çekirdek×0,8 − yük1)/oturumCpu, (boş bellek − 8 G)/oturumG)      → başsız oturum şeridi
  mac.ek   = min(boş CPU% × çekirdek / 0,5 çekirdek, (boş bellek% − 15) × RAM / 1,5 G) → ağır komut koşan alt ajan
  mac.alt_ajan = ~/.claude/state/serit/*.json içindeki canlı alt ajan sayısı (son 6 sa dokunulan dosyalar)
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

CIKTI = Path.home() / ".claude/state/ajan-kapasite.json"
SERIT = Path.home() / ".claude/state/serit"
SSH = ["ssh", "-p", "2222", "-o", "BatchMode=yes", "-o", "ControlPath=none", "-o", "ConnectTimeout=8",
       "root@10.0.0.21", "bash /home/sef/is/uretim-0204/kapasite.sh"]
ARALIK = 60
EN_AZ_ARA = 120


def kos(komut: list[str], sure: int = 20) -> str:
    try:
        return subprocess.run(komut, capture_output=True, text=True, timeout=sure).stdout
    except (subprocess.TimeoutExpired, OSError):
        return ""


def srv21() -> dict[str, object] | None:
    p = kos(SSH).split()
    if len(p) != 10:
        return None
    return {"aktif": int(p[0]), "yuk1": float(p[1]), "cekirdek": int(p[2]), "bos_bellek_g": float(p[3]),
            "oturum_cpu": float(p[4]), "oturum_g": float(p[5]), "ek": int(p[6]), "sinir": p[7],
            "hata_30dk": int(p[8]), "takili": int(p[9])}


def alt_ajanlar() -> dict[str, int]:
    canli: dict[str, int] = {}
    esik = time.time() - 6 * 3600
    for f in SERIT.glob("*.json"):
        try:
            if f.stat().st_mtime < esik:
                continue
            n = len(json.loads(f.read_text(encoding="utf-8")).get("aktif") or {})
        except (OSError, ValueError):
            continue
        if n:
            canli[f.stem[:8]] = n
    return canli


def mac() -> dict[str, object]:
    ust = [s for s in kos(["top", "-l", "2", "-n", "0"]).splitlines() if s.startswith("CPU usage")]
    m = re.search(r"([\d.]+)% idle", ust[-1]) if ust else None
    bos_cpu = float(m.group(1)) if m else 0.0
    m = re.search(r"free percentage: (\d+)%", kos(["memory_pressure"]))
    bos_bellek = int(m.group(1)) if m else 0
    cekirdek = os.cpu_count() or 1
    ram_g = int(kos(["sysctl", "-n", "hw.memsize"]).strip() or 0) / 2**30
    yuk1 = os.getloadavg()[0]
    ek_cpu = bos_cpu / 100 * cekirdek / 0.5
    ek_bellek = (bos_bellek - 15) / 100 * ram_g / 1.5
    ek = max(0, min(40, int(min(ek_cpu, ek_bellek))))
    canli = alt_ajanlar()
    return {"bos_cpu_yuzde": round(bos_cpu, 1), "yuk1": round(yuk1, 1), "cekirdek": cekirdek,
            "bos_bellek_yuzde": bos_bellek, "alt_ajan": sum(canli.values()), "alt_ajan_oturum": canli,
            "ek": ek, "sinir": "cpu" if ek_cpu < ek_bellek else "bellek"}


def yaz(veri: dict[str, object]) -> None:
    gecici = CIKTI.with_suffix(".json.tmp")
    gecici.write_text(json.dumps(veri, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    os.replace(gecici, CIKTI)


def kova(ek: int, onceki: int) -> int:
    """0 = dolu, 1 = yer var; 1–3 arası önceki durumu korur (titreme olmasın)."""
    if ek < 1:
        return 0
    return 1 if ek >= 4 else onceki


def main() -> None:
    son_s: dict[str, object] | None = None
    son_kova = -1
    son_t = 0.0
    dustu = 0
    while True:
        s = srv21()
        m = mac()
        dustu = 0 if s else dustu + 1
        yaz({
            "olcum": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
            "gecerlilik_sn": 180,
            "kaynak": "kapasite-izleyici.py (60 sn; oturum 7541766e Monitor)",
            "kural": "ek = şu an açılabilecek EK ajan (bütün oturumların toplamı). Bir oturum bir ölçümde ek'in "
                     "en çok yarısını alır (en az 1), 60 sn sonra yeniden okur. olcum 180 sn'den eskiyse sayı geçersiz.",
            "mac": m,
            "mac_not": "mac.ek ağır komut (test, derleme, tarayıcı) koşan alt ajan içindir; yalnız okuyan/yazan "
                       "ajanı CPU sınırlamaz, Claude kotası sınırlar (ölçülmüyor).",
            "srv21": s if s else {"erisim": "yok", "ardisik": dustu},
        })
        simdi = time.time()
        neden = ""
        mk = kova(int(m["ek"]), max(son_kova, 0))
        if dustu == 5:
            print("KAPASİTE: srv21'e 5 ölçümdür ulaşılamıyor", flush=True)
        if s:
            if son_s is None:
                neden = "ilk ölçüm"
            elif int(s["takili"]) > int(son_s["takili"]):
                neden = "TAKILI oturum (kendini bekleyen pgrep döngüsü; bekleyen bash'i durdur)"
            elif int(s["hata_30dk"]) > int(son_s["hata_30dk"]):
                neden = "yeni hata"
            elif int(s["ek"]) == 0 and int(son_s["ek"]) > 0:
                neden = "sunucu doldu"
            elif int(s["aktif"]) <= int(son_s["aktif"]) - 3:
                neden = "şerit boşaldı"
            elif abs(int(s["ek"]) - int(son_s["ek"])) >= 6:
                neden = "sunucu kapasitesi değişti"
            elif mk != son_kova:
                neden = "Mac'te yer açıldı" if mk else "Mac doldu"
            ara = 900 if neden.startswith("Mac") else EN_AZ_ARA  # Mac başka oturumların yüküyle sık oynar
            if neden and (son_s is None or simdi - son_t >= ara):
                print(f"KAPASİTE ({neden}): srv21 aktif {s['aktif']} şerit · yük {s['yuk1']}/{s['cekirdek']} · "
                      f"boş bellek {s['bos_bellek_g']}G → +{s['ek']} şerit (sınır: {s['sinir']}) · hata {s['hata_30dk']} "
                      f"· takılı {s['takili']} "
                      f"| Mac boş CPU %{m['bos_cpu_yuzde']} · yük {m['yuk1']}/{m['cekirdek']} · alt ajan "
                      f"{m['alt_ajan']} → +{m['ek']} ağır ajan (sınır: {m['sinir']})", flush=True)
                son_s, son_kova, son_t = s, mk, simdi
        time.sleep(ARALIK)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
