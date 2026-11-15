#!/bin/bash
# Sahne 04 Çağrı (simple-present-temel-s3, huni v2, HyperFrames DİKEY 1080x1920, 239 kare, t_bas 18,10, cümle 4 öğrenci):
# üret -> olaylar -> [önizleme burada biter]
# -> render -> video.mp4 + kontrol.png + k/*.png. Tema: --tema acik|koyu (varsayılan acik, K19).
# Önizleme hazırlığı: ONIZLE_YALNIZ=1 bash calistir.sh [--tema koyu]
set -e
[ -d /opt/homebrew/bin ] && export PATH="/opt/homebrew/bin:$PATH"   # arm64 node >= 22 (hyperframes şartı)
AD="$(cd "$(dirname "$0")" && pwd)"
. "$AD/../../ortak/tema.sh" "$@"
KOK="$AD/../../../.."                       # paket kökü (kalem)
M="$KOK/motorlar/hyperframes"; BIN="$M/node_modules/.bin"
ORTAK="$AD/../../ortak"
KARE=239
mkdir -p "$AD/proje/lib" "$AD/proje/assets/fonts" "$AD/k" "$AD/proje/renders"
cp "$M/node_modules/gsap/dist/gsap.min.js" "$AD/proje/lib/" 2>/dev/null || cp "$M/lib/gsap.min.js" "$AD/proje/lib/"
cp "$ORTAK/logo/$LOGO_DOSYA" "$AD/proje/assets/logo.svg"
# ana dersin kapağı (huni v2 §1 kural 7): iki tema da kopyalanır, uret.py href'i temaya göre seçer
cp "$ORTAK/kapak/ana-kapak.png" "$ORTAK/kapak/ana-kapak-koyu.png" "$AD/proje/assets/"
/usr/bin/python3 "$AD/uret.py" >&2   # ayrı satır: `a && b` zincirinde set -e uret.py hatasını yutar
/usr/bin/python3 "$AD/olay.py" >&2
tema_hf "$AD/proje/index.html"
[ -n "$ONIZLE_YALNIZ" ] && { echo "önizleme hazır"; exit 0; }
# yük bekçisi: 1 dk yük > 24 ise 60 sn bekle (en çok 5 dk)
for i in 1 2 3 4 5; do
  Y=$(yuk1)
  [ "$Y" -le 24 ] && break; sleep 60
done
cd "$AD/proje"
OUT="renders/cikti-$(date +%H%M%S).mp4"
perl -e 'alarm 480; exec @ARGV' "$BIN/hyperframes" render . -o "$OUT" --fps 30 --workers 1 >&2
ffmpeg -loglevel error -y -i "$OUT" -c:v libx264 -crf 16 -pix_fmt yuv420p -r 30 -an \
  -vf "tpad=stop_mode=clone:stop_duration=2" -frames:v $KARE "$AD/video.mp4"
SEL="eq(n,0)+eq(n,$((KARE/5)))+eq(n,$((KARE*2/5)))+eq(n,$((KARE*3/5)))+eq(n,$((KARE*4/5)))+eq(n,$((KARE-13)))"
ffmpeg -loglevel error -y -i "$AD/video.mp4" -vf "select='$SEL',scale=240:-1,tile=6x1" -frames:v 1 "$AD/kontrol.png"
# denetim kareleri (yerel): 0,05 / 3,50 / 6,90 sn (küresel 18,15 / 21,60 / 25,00)
for sn in 0.05 3.50 6.90; do
  n=$(awk "BEGIN{printf \"%d\", $sn*30+0.5}")
  ffmpeg -loglevel error -y -i "$AD/video.mp4" -vf "select=eq(n\,$n)" -frames:v 1 "$AD/k/$n.png"
done
ffprobe -v error -count_frames -select_streams v:0 -show_entries stream=codec_name,pix_fmt,width,height,nb_read_frames,r_frame_rate -of csv=p=0 "$AD/video.mp4"
tema_bitir "$AD"
