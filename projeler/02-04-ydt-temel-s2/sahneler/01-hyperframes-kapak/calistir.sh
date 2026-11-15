#!/bin/bash
# Sahne 01 kapak, huni v2 (02-04 YDT temel S2 Shorts, HyperFrames DİKEY 1080x1920, 97 kare = içerik 85 + geçiş 12):
# üret -> olaylar -> tema -> [önizleme burada biter] -> render -> video.mp4 + kontrol.png + k/*.png
# (+ tema acik ise paket kökü kapak-a.png ve kopyası kapak.png). mp4 bugün üretilmez (huni v2 §1 kural 9).
# Tema: --tema acik|koyu (varsayılan acik, K19). Önizleme hazırlığı: ONIZLE_YALNIZ=1 bash calistir.sh [--tema koyu]
set -e
[ -d /opt/homebrew/bin ] && export PATH="/opt/homebrew/bin:$PATH"   # arm64 node >= 22 (hyperframes şartı)
AD="$(cd "$(dirname "$0")" && pwd)"
. "$AD/../../ortak/tema.sh" "$@"
KOK="$AD/../../../.."                       # paket kökü (kalem)
M="$KOK/motorlar/hyperframes"; BIN="$M/node_modules/.bin"
ORTAK="$AD/../../ortak"
KARE=97
GEN=1080; YUK=1920                          # yakalama 1080 1920 (index.html data-width/height; aşağıda ffprobe ile denetlenir)
mkdir -p "$AD/proje/lib" "$AD/proje/assets/fonts" "$AD/k" "$AD/proje/renders"
cp "$M/node_modules/gsap/dist/gsap.min.js" "$AD/proje/lib/" 2>/dev/null || cp "$M/lib/gsap.min.js" "$AD/proje/lib/"
cp "$ORTAK/logo/$LOGO_DOSYA" "$AD/proje/assets/logo.svg"
/usr/bin/python3 "$AD/uret.py" >&2 && /usr/bin/python3 "$AD/olay.py" >&2
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
# denetim kareleri: 0,0 (ilk kare) / 0,9 (kapak karesi) / 1,5 (orta) / 2,5 (uçuş) / 2,8 (son hal)
for sn in 0.0 0.9 1.5 2.5 2.8; do
  n=$(awk "BEGIN{printf \"%d\", $sn*30+0.5}")
  ffmpeg -loglevel error -y -i "$AD/video.mp4" -vf "select=eq(n\,$n)" -frames:v 1 "$AD/k/$n.png"
done
# kapak karesi (t = 0,90 sn; ≠ bitmiş, konu yok): tam boy PNG paket köküne (yalnız tema acik). Altyazısız: ilk
# altyazı sözcüğü 0,95'te açılır (uret.py denetim 8 bunu assert eder); önizleme kapağı proje kopyasında #altyazi gizli çekilir.
if [ "$TEMA" = acik ]; then
  ffmpeg -loglevel error -y -i "$AD/video.mp4" -vf "select=eq(n\,27)" -frames:v 1 "$AD/../../kapak-a.png"
  cp "$AD/../../kapak-a.png" "$AD/../../kapak.png"
fi
ffprobe -v error -count_frames -select_streams v:0 -show_entries stream=codec_name,pix_fmt,width,height,nb_read_frames,r_frame_rate -of csv=p=0 "$AD/video.mp4"
BOY=$(ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=p=0 "$AD/video.mp4")
[ "$BOY" = "$GEN,$YUK" ] || { echo "HATA boyut $BOY != $GEN,$YUK" >&2; exit 1; }
tema_bitir "$AD"
