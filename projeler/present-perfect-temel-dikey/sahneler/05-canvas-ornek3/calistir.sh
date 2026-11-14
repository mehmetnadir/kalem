#!/bin/bash
# Sahne 05 DİKEY PRESENT PERFECT (düz canvas, 494 kare): yakala -> OLAYLAR -> olaylar.json -> video.mp4 -> kontrol.png -> k/*.png.
# Tema: --tema acik|koyu (varsayılan acik, K19). Paket kökünden bağımsız.
set -eo pipefail
[ -d /opt/homebrew/bin ] && export PATH="/opt/homebrew/bin:$PATH"
D="$(cd "$(dirname "$0")" && pwd)"; K="$(cd "$D/../../../.." && pwd)"; KAREDIR="$D/kareler"
. "$D/../../ortak/tema.sh" "$@"
N=494; TBAS=51.12; KLASOR=05-canvas-ornek3; GLOBAL_SN="55.5 59.2 66.6"
cd "$K"
BAS=$(date +%s)
for i in 1 2 3 4 5; do
  Y=$(yuk1)
  [ "$Y" -le 24 ] && break; echo "yük $Y > 24, 60 sn bekle"; sleep 60
done
perl -e 'alarm 1500; exec @ARGV' /usr/bin/python3 ortak/yakala.py \
  projeler/present-perfect-temel-dikey/sahneler/$KLASOR/sayfa.html$SORGU "$KAREDIR" 1080 1920 | tee "$D/yakala.log"
grep '^\[sayfa\] OLAYLAR ' "$D/yakala.log" | sed 's/^\[sayfa\] OLAYLAR //' > "$D/olaylar.json"
[ -s "$D/olaylar.json" ] || { echo "olaylar.json boş"; exit 1; }
SAY=$(ls "$KAREDIR" | grep -c '\.png$'); [ "$SAY" -eq "$N" ] || { echo "kare sayısı $SAY ($N olmalı)"; exit 1; }
ffmpeg -y -loglevel error -framerate 30 -i "$KAREDIR/%04d.png" -frames:v $N -c:v libx264 -pix_fmt yuv420p -crf 16 -r 30 "$D/video.mp4"
SEL=$(awk -v n=$N 'BEGIN{printf "eq(n\\,0)+eq(n\\,%d)+eq(n\\,%d)+eq(n\\,%d)+eq(n\\,%d)+eq(n\\,%d)", int(n*0.2), int(n*0.4), int(n*0.6), int(n*0.8), n-13}')
ffmpeg -y -loglevel error -i "$D/video.mp4" -vf "select='$SEL',scale=360:-1,tile=6x1" -frames:v 1 "$D/kontrol.png"
mkdir -p "$D/k"
for T in $GLOBAL_SN; do
  F=$(awk -v t=$T -v b=$TBAS 'BEGIN{printf "%04d", int((t-b)*30+0.5)}')
  cp "$KAREDIR/$F.png" "$D/k/$F.png"
done
ffmpeg -y -loglevel error -i "$D/video.mp4" -vf "fps=1,scale=360:640,tile=3x2" -frames:v 1 "$D/k/telefon-01.png"
ffmpeg -y -loglevel error -ss 6 -i "$D/video.mp4" -vf "fps=1,scale=360:640,tile=3x2" -frames:v 1 "$D/k/telefon-02.png"
ffmpeg -y -loglevel error -ss 12 -i "$D/video.mp4" -vf "fps=1,scale=360:640,tile=3x2" -frames:v 1 "$D/k/telefon-03.png"
# kareler/ geçici klasörü: KAREYI_TUT=1 ise yerinde kalır, değilse Silinecekler'e taşınır (silme yok kuralı)
if [ "${KAREYI_TUT:-0}" != "1" ]; then
  H=~/Silinecekler/2026-11-05-kalem-pp/$KLASOR-kareler-$(date +%H%M%S); mkdir -p "$(dirname "$H")"; mv "$KAREDIR" "$H"
  echo "$H : $KLASOR kareler (geçici yakalama)" >> ~/Silinecekler/2026-11-05-kalem-pp/LISTE.md
fi
tema_bitir "$D"
echo "tamam: $(( $(date +%s) - BAS )) sn"
