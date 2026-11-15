#!/bin/bash
# YouTube dikey parçaları (istem YT-2): üret → kareler (açık + koyu) → ölçümler → önizleme. mp4 RENDER YOK.
#   bash ortak/youtube/dikey/calistir.sh   (önizleme sunucusu 41022 K kökünü sunar, ortak Chrome CDP 41333)
# Kareler: giris/k/{,koyu/}giris-{0.0,1.0,2.97}.png · cikis/k/{,koyu/}cikis-{0.5,4.0,19.9}.png
#          cikis-kisa/k/{,koyu/}cikis-kisa-{0.3,2.97}.png
# Ölçüm: olcum/ses.json, olcum/alt.json, olcum/*-kutu-*.jsonl, bildirim/yer.json, bildirim/olcum/yer-tablo.json
set -euo pipefail
D="$(cd "$(dirname "$0")" && pwd)"
cd "$D"
export PATH="/home/sef/.nvm/versions/node/v24.22.2/bin:$PATH"
PORT="${ONIZLE_PORT:-41022}"
U="http://127.0.0.1:$PORT/ortak/youtube/dikey"
KARE="node ../kare.mjs"
curl -sf -o /dev/null --max-time 3 "$U/uret.py" || { echo "HATA: önizleme $PORT bu kökü sunmuyor ($U)" >&2; exit 4; }
OLC='JSON.stringify([...document.querySelectorAll("#marka > *, #icerik > :not(#marka)")]
  .map(e=>{const b=e.getBoundingClientRect();return [e.id,+b.left.toFixed(1),+b.top.toFixed(1),+b.right.toFixed(1),+b.bottom.toFixed(1)]}))'
B="--boyut 1080x1920"
/usr/bin/python3 -I uret.py
mkdir -p olcum
echo "== ses"; /usr/bin/python3 -I olc.py ses
for TEMA in acik koyu; do
  K=""; [ "$TEMA" = koyu ] && K="koyu/"
  timeout 120 $KARE "$U/giris/proje/index.html?tema=$TEMA" 0=giris/k/${K}giris-0.0.png 1.0=giris/k/${K}giris-1.0.png \
    2.9667=giris/k/${K}giris-2.97.png $B --olc "$OLC" > olcum/giris-kutu-$TEMA.jsonl
  timeout 120 $KARE "$U/cikis/proje/index.html?tema=$TEMA" 0.5=cikis/k/${K}cikis-0.5.png 4.0=cikis/k/${K}cikis-4.0.png \
    19.9=cikis/k/${K}cikis-19.9.png $B --olc "$OLC" > olcum/cikis-kutu-$TEMA.jsonl
  timeout 120 $KARE "$U/cikis-kisa/proje/index.html?tema=$TEMA" 0.3=cikis-kisa/k/${K}cikis-kisa-0.3.png \
    2.9667=cikis-kisa/k/${K}cikis-kisa-2.97.png $B --olc "$OLC" > olcum/cikis-kisa-kutu-$TEMA.jsonl
  timeout 60 $KARE "$U/cikis/proje/index.html?tema=$TEMA&zemin=1" 19.9=olcum/zemin-$TEMA.png $B > /dev/null
done
echo "== alt yarı ve bölge"; /usr/bin/python3 -I olc.py alt
echo "== bildirim yeri"; timeout 1500 /usr/bin/python3 -I olc.py yer
echo "== önizleme"; /usr/bin/python3 -I uret.py --onizle
