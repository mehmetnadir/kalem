#!/bin/bash
# Sahne 11 kapanış (HyperFrames, 599 kare): üret -> olaylar -> (önizleme hazır | render -> video.mp4 + kontrol.png)
# Tema: --tema acik|koyu (varsayılan acik, K19). Önizleme: ONIZLE_YALNIZ=1 bash calistir.sh [--tema koyu]
set -e
[ -d /opt/homebrew/bin ] && export PATH="/opt/homebrew/bin:$PATH"   # arm64 node >= 22 (hyperframes şartı)
AD="$(cd "$(dirname "$0")" && pwd)"
. "$AD/../../ortak/tema.sh" "$@"
KOK="$AD/../../../.."                       # paket kökü (kalem)
M="$KOK/motorlar/hyperframes"; BIN="$M/node_modules/.bin"
ORTAK="$AD/../../ortak"
KARE=599
mkdir -p "$AD/proje/lib" "$AD/proje/assets/fonts" "$AD/k" "$AD/proje/renders"
cp "$M/node_modules/gsap/dist/gsap.min.js" "$AD/proje/lib/" 2>/dev/null || cp "$M/lib/gsap.min.js" "$AD/proje/lib/"
cp "$ORTAK/logo/$LOGO_DOSYA" "$AD/proje/assets/logo.svg"
/usr/bin/python3 "$AD/uret.py" >&2 && /usr/bin/python3 "$AD/olay.py" >&2
tema_hf "$AD/proje/index.html"
/usr/bin/python3 -c "import sys;sys.path.insert(0,'$AD');import yardim;yardim.font_kopyala('$AD/proje/assets/fonts')"
[ -n "$ONIZLE_YALNIZ" ] && { echo "önizleme hazır"; exit 0; }
# yük bekçisi: 1 dk yük > 24 ise 60 sn bekle (en çok 5 dk)
for i in 1 2 3 4 5; do
  Y=$(yuk1)
  [ "$Y" -le 24 ] && break; sleep 60
done
cd "$AD/proje"
OUT="renders/cikti.mp4"
perl -e 'alarm 480; exec @ARGV' "$BIN/hyperframes" render . -o "$OUT" --fps 30 --workers 1 >&2
ffmpeg -loglevel error -y -i "$OUT" -c:v libx264 -crf 16 -pix_fmt yuv420p -r 30 -an \
  -vf "tpad=stop_mode=clone:stop_duration=2" -frames:v $KARE "$AD/video.mp4"
SEL="eq(n,0)+eq(n,$((KARE/5)))+eq(n,$((KARE*2/5)))+eq(n,$((KARE*3/5)))+eq(n,$((KARE*4/5)))+eq(n,$((KARE-13)))"
ffmpeg -loglevel error -y -i "$AD/video.mp4" -vf "select='$SEL',scale=640:-1,tile=3x2" -frames:v 1 "$AD/kontrol.png"
tema_bitir "$AD"
