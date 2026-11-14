#!/bin/bash
# Sahne 06 soru + form (HyperFrames İLERİ dikey SPI, 901 kare): üret -> olaylar -> render -> video.mp4 + kontrol.png + k/*.png
# Tema: --tema acik|koyu (varsayılan acik, K19).
set -e
[ -d /opt/homebrew/bin ] && export PATH="/opt/homebrew/bin:$PATH"   # arm64 node >= 22 (hyperframes şartı)
AD="$(cd "$(dirname "$0")" && pwd)"
. "$AD/../../ortak/tema.sh" "$@"
KOK="$AD/../../../.."                       # paket kökü (kalem)
M="$KOK/motorlar/hyperframes"; BIN="$M/node_modules/.bin"
ORTAK="$AD/../../ortak"
KARE=901; TBAS=61.41
mkdir -p "$AD/proje/lib" "$AD/proje/assets/fonts" "$AD/proje/assets/cizim" "$AD/k" "$AD/proje/renders"
cp "$M/node_modules/gsap/dist/gsap.min.js" "$AD/proje/lib/" 2>/dev/null || cp "$M/lib/gsap.min.js" "$AD/proje/lib/"
cp "$ORTAK/logo/$LOGO_DOSYA" "$AD/proje/assets/logo.svg"
/usr/bin/python3 "$AD/uret.py" >&2 && /usr/bin/python3 "$AD/olay.py" >&2
tema_hf "$AD/proje/index.html"
/usr/bin/python3 -c "import sys;sys.path.insert(0,'$AD');import yardim;yardim.font_kopyala('$AD/proje/assets/fonts')"
# yük bekçisi: 1 dk yük > 24 ise 60 sn bekle (en çok 5 dk)
for i in 1 2 3 4 5; do
  Y=$(yuk1)
  [ "$Y" -le 24 ] && break; sleep 60
done
cd "$AD/proje"
OUT="renders/cikti.mp4"
perl -e 'alarm 1200; exec @ARGV' "$BIN/hyperframes" render . -o "$OUT" --fps 30 --workers 1 >&2
ffmpeg -loglevel error -y -i "$OUT" -c:v libx264 -crf 16 -pix_fmt yuv420p -r 30 -an \
  -vf "tpad=stop_mode=clone:stop_duration=2" -frames:v $KARE "$AD/video.mp4"
SEL="eq(n,0)+eq(n,$((KARE/5)))+eq(n,$((KARE*2/5)))+eq(n,$((KARE*3/5)))+eq(n,$((KARE*4/5)))+eq(n,$((KARE-13)))"
ffmpeg -loglevel error -y -i "$AD/video.mp4" -vf "select='$SEL',scale=360:-1,tile=6x1" -frames:v 1 "$AD/kontrol.png"
for sn in 64.0 66.8 70.0 73.5 78.0 82.5 86.5 89.5; do   # küresel sn -> yerel kare = (t - 61,41) x 30
  n=$(awk "BEGIN{printf \"%d\", ($sn-$TBAS)*30+0.5}")
  ffmpeg -loglevel error -y -i "$AD/video.mp4" -vf "select=eq(n\,$n)" -frames:v 1 "$AD/k/$n.png"
done
# telefon ölçeği: 1 sn aralıklı kontak (360x640, 6 karelik sayfalar)
ffmpeg -loglevel error -y -i "$AD/video.mp4" -vf "fps=1,scale=360:640,tile=3x2" "$AD/k/telefon-%02d.png"
ffprobe -v error -count_frames -select_streams v:0 -show_entries stream=codec_name,pix_fmt,width,height,nb_read_frames,r_frame_rate -of csv=p=0 "$AD/video.mp4"
tema_bitir "$AD"
