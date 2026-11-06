#!/bin/bash
# Sahne 02 (Paper.js, 451 kare): yakala -> olaylar.json -> video.mp4 -> kontrol.png -> k/*.png Tema: --tema acik|koyu (varsayılan acik, K19).
# Geçici kareler bitince ~/Silinecekler/<tarih>-kalem/ altına taşınır (silme yok).
set -eo pipefail
D="$(cd "$(dirname "$0")" && pwd)"; K="$(cd "$D/../../../.." && pwd)"; KARE_DIR="$D/kareler"; N=${KARE_SAYISI:-451}
. "$D/../../ortak/tema.sh" "$@"
cd "$K"
BAS=$(date +%s)
perl -e 'alarm 1200; exec @ARGV' /usr/bin/python3 ortak/yakala.py projeler/deneme-doku/sahneler/02-paperjs-kanca/sayfa.html$SORGU "$KARE_DIR" | tee "$D/yakala.log"
grep '^\[sayfa\] OLAYLAR ' "$D/yakala.log" | sed 's/^\[sayfa\] OLAYLAR //' > "$D/olaylar.json"
grep '^\[sayfa\] ZAMANLAR ' "$D/yakala.log" | sed 's/^\[sayfa\] ZAMANLAR //' > "$D/zamanlar.json" || true
[ -s "$D/olaylar.json" ] || { echo "olaylar.json boş"; exit 1; }
C=$(ls "$KARE_DIR" | grep -c '\.png$'); [ "$C" -eq "$N" ] || { echo "kare sayısı $C ($N olmalı)"; exit 1; }
ffmpeg -y -loglevel error -framerate 30 -i "$KARE_DIR/%04d.png" -frames:v "$N" -c:v libx264 -pix_fmt yuv420p -crf 16 -r 30 "$D/video.mp4"
S=$((N - 13)); SEL="eq(n\,0)+eq(n\,$((N/5)))+eq(n\,$((N*2/5)))+eq(n\,$((N*3/5)))+eq(n\,$((N*4/5)))+eq(n\,$S)"
ffmpeg -y -loglevel error -i "$D/video.mp4" -vf "select='$SEL',scale=640:-1,tile=3x2" -frames:v 1 "$D/kontrol.png"
mkdir -p "$D/k"
# denetim kareleri: küresel 4,5 / 8,5 / 12,5 sn -> yerel kare = round((t - 3,00) x 30)
for T in 5.0 9.6 15.6; do F=$(perl -e "printf('%d', ($T-3.0)*30+0.5)"); cp "$KARE_DIR/$(printf '%04d' "$F").png" "$D/k/$(printf '%04d' "$F").png"; done
cp "$KARE_DIR/$(printf '%04d' "$S").png" "$D/k/$(printf '%04d' "$S").png"
if [ "${KAREYI_TUT:-0}" != "1" ]; then
  H="$HOME/Silinecekler/2026-11-05-kalem-spi"; mkdir -p "$H"; mv "$KARE_DIR" "$H/kareler-02-$(date +%H%M%S)"
fi
tema_bitir "$D"
echo "tamam: $(( $(date +%s) - BAS )) sn"
