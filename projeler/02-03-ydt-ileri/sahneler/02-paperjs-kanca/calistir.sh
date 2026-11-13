#!/bin/bash
# Sahne 02 (02-03 YDT ileri, Paper.js, 384 kare): önizleme hazırlığı yok (sayfa canlı sunucudan açılır); render bölümü
# yakala -> olaylar.json -> video.mp4 -> kontrol.png. Tema: --tema acik|koyu (varsayılan acik, K19).
# Önizleme: ONIZLE_YALNIZ=1 bash calistir.sh [--tema koyu]
set -eo pipefail
D="$(cd "$(dirname "$0")" && pwd)"; K="$(cd "$D/../../../.." && pwd)"; KARE_DIR="$D/kareler"; N=${KARE_SAYISI:-384}
. "$D/../../ortak/tema.sh" "$@"
[ -n "$ONIZLE_YALNIZ" ] && { echo "önizleme hazır"; exit 0; }
cd "$K"
BAS=$(date +%s)
perl -e 'alarm 480; exec @ARGV' /usr/bin/python3 ortak/yakala.py projeler/02-03-ydt-ileri/sahneler/02-paperjs-kanca/sayfa.html$SORGU "$KARE_DIR" | tee "$D/yakala.log"
grep '^\[sayfa\] OLAYLAR ' "$D/yakala.log" | sed 's/^\[sayfa\] OLAYLAR //' > "$D/olaylar.json"
[ -s "$D/olaylar.json" ] || { echo "olaylar.json boş"; exit 1; }
C=$(ls "$KARE_DIR" | grep -c '\.png$'); [ "$C" -eq "$N" ] || { echo "kare sayısı $C ($N olmalı)"; exit 1; }
ffmpeg -y -loglevel error -framerate 30 -i "$KARE_DIR/%04d.png" -frames:v "$N" -c:v libx264 -pix_fmt yuv420p -crf 16 -r 30 "$D/video.mp4"
S=$((N - 13)); SEL="eq(n\,0)+eq(n\,$((N/5)))+eq(n\,$((N*2/5)))+eq(n\,$((N*3/5)))+eq(n\,$((N*4/5)))+eq(n\,$S)"
ffmpeg -y -loglevel error -i "$D/video.mp4" -vf "select='$SEL',scale=640:-1,tile=3x2" -frames:v 1 "$D/kontrol.png"
mkdir -p "$D/k"
if [ "${KAREYI_TUT:-0}" != "1" ]; then
  H="$HOME/Silinecekler/2026-11-13-02-03-ydt-ileri"; mkdir -p "$H"; mv "$KARE_DIR" "$H/kareler-02-$(date +%H%M%S)"
fi
tema_bitir "$D"
echo "tamam: $(( $(date +%s) - BAS )) sn"
