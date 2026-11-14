#!/bin/bash
# Sahne 05 (düz canvas, İLERİ dikey): yakala -> OLAYLAR -> olaylar.json -> video.mp4 -> kontrol.png -> k/*.png.
# Paket kökünden bağımsız. Tema: --tema acik|koyu (varsayılan acik, K19).
set -eo pipefail
[ -d /opt/homebrew/bin ] && export PATH="/opt/homebrew/bin:$PATH"
D="$(cd "$(dirname "$0")" && pwd)"; K="$(cd "$D/../../../.." && pwd)"; KAREDIR="$D/kareler"
. "$D/../../ortak/tema.sh" "$@"
N=406; TBAS=48.29; KLASOR=05-canvas-ornek3; GLOBAL_SN="52.0 56.0 60.0"
cd "$K"
BAS=$(date +%s)
for i in 1 2 3 4 5; do
  Y=$(yuk1)
  [ "$Y" -le 24 ] && break; echo "yük $Y > 24, 60 sn bekle"; sleep 60
done
perl -e 'alarm 900; exec @ARGV' /usr/bin/python3 ortak/yakala.py \
  projeler/simple-present-ileri-dikey/sahneler/$KLASOR/sayfa.html$SORGU "$KAREDIR" 1080 1920 | tee "$D/yakala.log"
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
# kareler/ geçici klasörü: KAREYI_TUT=1 ise yerinde kalır, değilse Silinecekler'e taşınır (silme yok kuralı)
if [ "${KAREYI_TUT:-0}" != "1" ]; then
  H=~/Silinecekler/2026-11-05-kalem-ileri/$KLASOR-kareler-$(date +%H%M%S); mkdir -p "$(dirname "$H")"; mv "$KAREDIR" "$H"
  echo "$H — ileri-dikey $KLASOR geçici kareler ($TEMA), video.mp4 üretildi, 05.11" >> ~/Silinecekler/2026-11-05-kalem-ileri/LISTE.md
fi
tema_bitir "$D"
echo "tamam: $(( $(date +%s) - BAS )) sn"
