#!/bin/bash
# Sahne 04 hikâye karesi (HyperFrames DİKEY 1080x1920, tek kare, ses yok): üret -> [önizleme burada biter] -> tek kare PNG.
# Tema: --tema acik|koyu (varsayılan acik, K19). acik -> paket kökü hikaye-a.png + kopyası hikaye.png ·
# koyu -> k/hikaye-a-koyu.png. mp4 yok, birleştirme yok. Kalıp: 02-04-ydt-temel-s1/sahneler/04-hyperframes-hikaye.
# Önizleme hazırlığı: ONIZLE_YALNIZ=1 bash calistir.sh [--tema koyu]
set -e
[ -d /opt/homebrew/bin ] && export PATH="/opt/homebrew/bin:$PATH"   # arm64 node >= 22 (hyperframes şartı)
AD="$(cd "$(dirname "$0")" && pwd)"
. "$AD/../../ortak/tema.sh" "$@"
KOK="$AD/../../../.."                       # kalem kökü
PAKET="$(cd "$AD/../.." && pwd)"            # paket kökü (02-04-ydt-temel-s2)
M="$KOK/motorlar/hyperframes"; BIN="$M/node_modules/.bin"
ORTAK="$AD/../../ortak"
SN=0.5                                      # yakalama anı: zamanlar.json yakala_sn (kare durağan)
GEN=1080; YUK=1920                          # yakalama 1080 1920 (index.html data-width/height; aşağıda ffprobe ile denetlenir)
mkdir -p "$AD/proje/lib" "$AD/proje/assets/fonts" "$AD/k/koyu"
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
KD="$AD/k"; [ "$TEMA" = koyu ] && KD="$AD/k/koyu"
cd "$AD/proje"
# tek kare: --keep çıktı klasörünü silmez (k/ altında k/koyu/ durur), ad at-<sn>s.png
perl -e 'alarm 170; exec @ARGV' "$BIN/hyperframes" snapshot . --at "$SN" --no-end --keep -o "$KD" >&2
HEDEF="$AD/k/hikaye-a-koyu.png"; [ "$TEMA" = acik ] && HEDEF="$PAKET/hikaye-a.png"
cp "$KD/at-${SN}s.png" "$HEDEF"; chmod 644 "$HEDEF"   # snapshot 0600 yazar
BOY=$(ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=p=0 "$HEDEF")
echo "png,$BOY"
[ "$BOY" = "$GEN,$YUK" ] || { echo "HATA boyut $BOY != $GEN,$YUK" >&2; exit 1; }
echo "$HEDEF"
if [ "$TEMA" = acik ]; then cp "$HEDEF" "$PAKET/hikaye.png"; chmod 644 "$PAKET/hikaye.png"; echo "$PAKET/hikaye.png"; fi
tema_bitir "$AD"
