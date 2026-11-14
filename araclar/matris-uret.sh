#!/bin/bash
# Bir kalem projesinin bütün sahnelerini sırayla yakalar ve birleştirir; tema başına çıktı üretir.
#   araclar/matris-uret.sh projeler/<proje> [acik|koyu|ikisi]   (varsayılan ikisi)
# Çıktı: <proje>/cikti.mp4 (açık) ve <proje>/cikti-koyu.mp4 (koyu); günlük <proje>/_matris.log (süreler, yük).
# Sahne sırası zaman.json'daki klasör sırasıdır; her sahnenin calistir.sh'ı kendi yük bekçisini taşır.
set -eo pipefail
[ -d /opt/homebrew/bin ] && export PATH="/opt/homebrew/bin:$PATH"
P="${1:?proje dizini gerekli (ör. projeler/present-continuous)}"; T="${2:-ikisi}"
K="$(cd "$(dirname "$0")/.." && pwd)"; cd "$K"
[ -f "$P/zaman.json" ] || { echo "zaman.json yok: $P" >&2; exit 2; }
LOG="$P/_matris.log"; : > "$LOG"
case "$T" in acik | koyu) TEMALAR="$T" ;; ikisi) TEMALAR="acik koyu" ;; *) echo "tema: acik|koyu|ikisi" >&2; exit 2 ;; esac
KLASORLER=$(/usr/bin/python3 -I -c 'import json,sys;[print(s["klasor"]) for s in json.load(open(sys.argv[1]))["sahneler"]]' "$P/zaman.json")
BAS0=$(date +%s)
for tema in $TEMALAR; do
  for kl in $KLASORLER; do
    d="$P/sahneler/$kl"
    [ -f "$d/calistir.sh" ] || { echo "HATA: $d/calistir.sh yok" | tee -a "$LOG"; exit 1; }
    B=$(date +%s)
    echo "== $tema $kl başla $(date +%H:%M:%S) yük $(uptime | sed 's/.*averages*: *//')" | tee -a "$LOG"
    KALEM_TEMA=$tema bash "$d/calistir.sh" --tema "$tema" >> "$LOG" 2>&1 || { echo "HATA: $kl ($tema)" | tee -a "$LOG"; exit 1; }
    echo "== $kl $tema bitti: $(( $(date +%s) - B )) sn" | tee -a "$LOG"
  done
  /usr/bin/python3 birlestir.py "$P" --tema "$tema" --gecis BookFlip --efekt hisirti 2>&1 | tail -3 | tee -a "$LOG"
done
echo "== toplam $(( $(date +%s) - BAS0 )) sn" | tee -a "$LOG"
