#!/bin/bash
# Ana ders kapağı (kapak standardı v1): durağan tek kare, ses yok, zaman.json sahneler[] dışı, mp4 yok.
# Biçim uret.py'de paket adından: ana paket 1920x1080, -dikey paket 1080x1920 (iki pakette aynı betik).
# Tema: --tema acik|koyu (varsayılan acik). acik -> paket kökü kapak.png · koyu -> paket kökü kapak-koyu.png.
# Kökte eski kapak varsa ~/Silinecekler/<tarih>-kapak/ altına taşınır (silme yok).
# Kalıp: 02-04-ydt-temel-s1/sahneler/05-hyperframes-kapak-b/calistir.sh. Önizleme: ONIZLE_YALNIZ=1 bash calistir.sh
set -e
[ -d /opt/homebrew/bin ] && export PATH="/opt/homebrew/bin:$PATH"                       # Mac arm64 node
[ -d "$HOME/.nvm/versions/node/v24.22.2/bin" ] && export PATH="$HOME/.nvm/versions/node/v24.22.2/bin:$PATH"  # srv21
AD="$(cd "$(dirname "$0")" && pwd)"
. "$AD/../../ortak/tema.sh" "$@"
KOK="$AD/../../../.."                       # kalem kökü
PAKET="$(cd "$AD/../.." && pwd)"
M="$KOK/motorlar/hyperframes"; BIN="$M/node_modules/.bin"
SN=0.5                                      # yakalama anı (kare durağan)
mkdir -p "$AD/proje/lib" "$AD/proje/assets/fonts" "$AD/k/$TEMA"
cp "$M/node_modules/gsap/dist/gsap.min.js" "$AD/proje/lib/" 2>/dev/null || cp "$M/lib/gsap.min.js" "$AD/proje/lib/"
/usr/bin/python3 "$AD/uret.py" >&2
tema_hf "$AD/proje/index.html"
[ -n "$ONIZLE_YALNIZ" ] && { echo "önizleme hazır"; exit 0; }
for i in 1 2 3 4 5; do                      # yük bekçisi: 1 dk yük > 24 ise 60 sn bekle (en çok 5 dk)
  Y=$(yuk1); [ "$Y" -le 24 ] && break; sleep 60
done
KD="$AD/k/$TEMA"
cd "$AD/proje"
perl -e 'alarm 170; exec @ARGV' "$BIN/hyperframes" snapshot . --at "$SN" --no-end --keep -o "$KD" >&2
HEDEF="$PAKET/kapak.png"; [ "$TEMA" = koyu ] && HEDEF="$PAKET/kapak-koyu.png"
if [ -f "$HEDEF" ]; then
  S="$HOME/Silinecekler/$(date +%F)-kapak"; mkdir -p "$S"
  mv "$HEDEF" "$S/$(basename "$PAKET")-$(basename "$HEDEF" .png)-$(date +%H%M%S).png"
fi
cp "$KD/at-${SN}s.png" "$HEDEF"; chmod 644 "$HEDEF"   # snapshot 0600 yazar
ffprobe -v error -select_streams v:0 -show_entries stream=codec_name,width,height -of csv=p=0 "$HEDEF"
echo "$HEDEF"
tema_bitir "$AD"
