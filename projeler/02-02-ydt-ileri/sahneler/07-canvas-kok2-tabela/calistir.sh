#!/bin/bash
# Sahne 07-canvas-kok2-tabela (Düz canvas, yatay 1920x1080, 858 kare, t_bas 129.38): yakala -> olaylar.json -> video.mp4 -> kontrol.png -> k/*.png
# Tema: --tema acik|koyu (varsayılan acik, K19). Geçici kareler ~/Silinecekler/2026-11-13-02-02-ydt-ileri/ altına taşınır (silme yok).
# P2 (render yok): ONIZLE_YALNIZ=1 bash calistir.sh [--tema koyu] → yalnız önizleme hazırlığı (canvas sahnesinde hazırlık yok).
set -eo pipefail
export PATH=/opt/homebrew/bin:$PATH
D="$(cd "$(dirname "$0")" && pwd)"; K="$(cd "$D/../../../.." && pwd)"; KARE_DIR="$D/kareler"; N=858
KLASOR=07-canvas-kok2-tabela; PROJE=02-02-ydt-ileri; TBAS=129.38; GLOBAL_SN="133.5 140.5 148.0 152.9 156.9"
. "$D/../../ortak/tema.sh" "$@"
[ -n "$ONIZLE_YALNIZ" ] && { echo "önizleme hazır"; exit 0; }
cd "$K"
BAS=$(date +%s)
for i in 1 2 3 4 5; do
  Y=$(uptime | sed 's/.*averages*: *//' | awk '{gsub(",","",$1); print int($1)}')
  [ "$Y" -le 24 ] && break; echo "yük $Y > 24, 60 sn bekle"; sleep 60
done
perl -e 'alarm 900; exec @ARGV' /usr/bin/python3 ortak/yakala.py projeler/$PROJE/sahneler/$KLASOR/sayfa.html$SORGU "$KARE_DIR" | tee "$D/yakala.log"
grep '^\[sayfa\] OLAYLAR ' "$D/yakala.log" | sed 's/^\[sayfa\] OLAYLAR //' > "$D/olaylar.json"
[ -s "$D/olaylar.json" ] || { echo "olaylar.json boş"; exit 1; }
C=$(ls "$KARE_DIR" | grep -c '\.png$'); [ "$C" -eq "$N" ] || { echo "kare sayısı $C ($N olmalı)"; exit 1; }
ffmpeg -y -loglevel error -framerate 30 -i "$KARE_DIR/%04d.png" -frames:v "$N" -c:v libx264 -pix_fmt yuv420p -crf 16 -r 30 "$D/video.mp4"
S=$((N - 13)); SEL="eq(n\,0)+eq(n\,$((N/5)))+eq(n\,$((N*2/5)))+eq(n\,$((N*3/5)))+eq(n\,$((N*4/5)))+eq(n\,$S)"
ffmpeg -y -loglevel error -i "$D/video.mp4" -vf "select='$SEL',scale=640:-1,tile=3x2" -frames:v 1 "$D/kontrol.png"
mkdir -p "$D/k"
for T in $GLOBAL_SN; do F=$(perl -e "printf('%d', ($T-$TBAS)*30+0.5)"); cp "$KARE_DIR/$(printf '%04d' "$F").png" "$D/k/$(printf '%04d' "$F").png"; done
cp "$KARE_DIR/$(printf '%04d' "$S").png" "$D/k/$(printf '%04d' "$S").png"
if [ "${KAREYI_TUT:-0}" != "1" ]; then
  H="$HOME/Silinecekler/2026-11-13-02-02-ydt-ileri"; mkdir -p "$H"; mv "$KARE_DIR" "$H/kareler-$KLASOR-$(date +%H%M%S)"
fi
tema_bitir "$D"
echo "tamam: $(( $(date +%s) - BAS )) sn"
