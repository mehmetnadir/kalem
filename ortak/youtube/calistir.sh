#!/bin/bash
# YouTube ortak parçaları (istem YT-1): üret → kareler (açık + koyu) → bildirim PNG → ölçümler. mp4 RENDER YOK.
#   bash ortak/youtube/ses.sh        (bir kez; ses zinciri, önbellekli)
#   bash ortak/youtube/calistir.sh   (sunucuda: önizleme 41022 bu kökü sunar, ortak Chrome CDP 41333)
# Kareler: giris/k/{,koyu/}giris-{0.0,1.0,2.97}.png · cikis/k/{,koyu/}cikis-{0.5,4.0,19.9}.png
# Ölçüm: olcum/ses.json, olcum/sag.json, bildirim/yer.json, bildirim/olcum/yer-tablo.json, bildirim/ornek-*.png
set -euo pipefail
Y="$(cd "$(dirname "$0")" && pwd)"
cd "$Y"
export PATH="/home/sef/.nvm/versions/node/v24.22.2/bin:$PATH"
PORT="${ONIZLE_PORT:-41022}"
U="http://127.0.0.1:$PORT/ortak/youtube"
curl -sf -o /dev/null --max-time 3 "$U/uret.py" || { echo "HATA: önizleme $PORT bu kökü sunmuyor ($U)" >&2; exit 4; }
OLC='JSON.stringify([...document.querySelectorAll("#marka > *, #icerik > :not(#marka), #kart-svg > :not(#kart)")]
  .map(e=>{const b=e.getBoundingClientRect();return [e.id,+b.left.toFixed(1),+b.top.toFixed(1),+b.right.toFixed(1),+b.bottom.toFixed(1)]}))'
/usr/bin/python3 -I uret.py
mkdir -p olcum
for TEMA in acik koyu; do
  D=""; [ "$TEMA" = koyu ] && D="koyu/"
  timeout 120 node kare.mjs "$U/giris/proje/index.html?tema=$TEMA" 0=giris/k/${D}giris-0.0.png \
    1.0=giris/k/${D}giris-1.0.png 2.9667=giris/k/${D}giris-2.97.png --olc "$OLC" > olcum/giris-kutu-$TEMA.jsonl
  timeout 120 node kare.mjs "$U/cikis/proje/index.html?tema=$TEMA" 0.5=cikis/k/${D}cikis-0.5.png \
    4.0=cikis/k/${D}cikis-4.0.png 19.9=cikis/k/${D}cikis-19.9.png --olc "$OLC" > olcum/cikis-kutu-$TEMA.jsonl
  timeout 60 node kare.mjs "$U/cikis/proje/index.html?tema=$TEMA&zemin=1" 19.9=olcum/zemin-$TEMA.png > /dev/null
  timeout 60 node kare.mjs "$U/bildirim/kart.html?tema=$TEMA" -=bildirim/bildirim-$TEMA.png --boyut 520x140 --seffaf \
    --olc "$OLC" > olcum/kart-kutu-$TEMA.jsonl
done
echo "== ses";  /usr/bin/python3 -I olc.py ses
echo "== sağ yarı"; /usr/bin/python3 -I olc.py sag
echo "== bildirim yeri"; timeout 1200 /usr/bin/python3 -I olc.py yer
echo "== önizleme"; /usr/bin/python3 -I uret.py --onizle
