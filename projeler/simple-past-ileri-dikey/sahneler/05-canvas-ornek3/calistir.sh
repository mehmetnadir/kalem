#!/bin/bash
# Sahne 05 SIMPLE PAST İLERİ DİKEY (düz canvas, 1080x1920, 528 kare): yakala -> olaylar.json -> video.mp4 -> kontrol.png -> k/*.png
# Tema: --tema acik|koyu (varsayılan acik). Geçici kareler ~/Silinecekler/2026-11-05-kalem-spasti/ altına taşınır (silme yok).
set -eo pipefail
[ -d /opt/homebrew/bin ] && export PATH="/opt/homebrew/bin:$PATH"
D="$(cd "$(dirname "$0")" && pwd)"; K="$(cd "$D/../../../.." && pwd)"; KARE_DIR="$D/kareler"; N=528
KLASOR=05-canvas-ornek3; PROJE=simple-past-ileri-dikey; TBAS=48.99; GLOBAL_SN="52.5 59.0 64.8"
. "$D/../../ortak/tema.sh" "$@"
cd "$K"
BAS=$(date +%s)
for i in 1 2 3 4 5; do
  Y=$(yuk1)
  [ "$Y" -le 24 ] && break; echo "yük $Y > 24, 60 sn bekle"; sleep 60
done
perl -e 'alarm 1500; exec @ARGV' /usr/bin/python3 ortak/yakala.py projeler/$PROJE/sahneler/$KLASOR/sayfa.html$SORGU "$KARE_DIR" 1080 1920 | tee "$D/yakala.log"
grep '^\[sayfa\] OLAYLAR ' "$D/yakala.log" | sed 's/^\[sayfa\] OLAYLAR //' > "$D/olaylar.json"
grep '^\[sayfa\] ZAMANLAR ' "$D/yakala.log" | sed 's/^\[sayfa\] ZAMANLAR //' > "$D/zamanlar.json" || true
[ -s "$D/olaylar.json" ] || { echo "olaylar.json boş"; exit 1; }
C=$(ls "$KARE_DIR" | grep -c '\.png$'); [ "$C" -eq "$N" ] || { echo "kare sayısı $C ($N olmalı)"; exit 1; }
ffmpeg -y -loglevel error -framerate 30 -i "$KARE_DIR/%04d.png" -frames:v "$N" -c:v libx264 -pix_fmt yuv420p -crf 16 -r 30 "$D/video.mp4"
S=$((N - 13)); SEL="eq(n\,0)+eq(n\,$((N/5)))+eq(n\,$((N*2/5)))+eq(n\,$((N*3/5)))+eq(n\,$((N*4/5)))+eq(n\,$S)"
ffmpeg -y -loglevel error -i "$D/video.mp4" -vf "select='$SEL',scale=360:-1,tile=6x1" -frames:v 1 "$D/kontrol.png"
mkdir -p "$D/k"
ffmpeg -y -loglevel error -i "$D/video.mp4" -vf "fps=1,scale=360:640,tile=3x2" "$D/k/telefon-%02d.png"
for T in $GLOBAL_SN; do F=$(perl -e "printf('%d', ($T-$TBAS)*30+0.5)"); cp "$KARE_DIR/$(printf '%04d' "$F").png" "$D/k/$(printf '%04d' "$F").png"; done
cp "$KARE_DIR/$(printf '%04d' "$S").png" "$D/k/$(printf '%04d' "$S").png"
if [ "${KAREYI_TUT:-0}" != "1" ]; then
  H="$HOME/Silinecekler/2026-11-05-kalem-spasti"; mkdir -p "$H"; mv "$KARE_DIR" "$H/kareler-$KLASOR-$(date +%H%M%S)"
fi
tema_bitir "$D"
echo "tamam: $(( $(date +%s) - BAS )) sn"
