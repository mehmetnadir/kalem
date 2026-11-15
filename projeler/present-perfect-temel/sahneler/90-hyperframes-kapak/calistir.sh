#!/bin/bash
# Ana ders kapağı (kapak standardı v1): HyperFrames durağan kare, ses yok, zaman.json sahneler[] DIŞINDA.
#   bash calistir.sh [--tema acik|koyu] [--duzen yatay|dikey]   (varsayılan: acik, yatay)
# acik -> paket kökü kapak.png · koyu -> paket kökü kapak-koyu.png. mp4 yok. Kalıp: 02-04-ydt-temel-s1/sahneler/05-hyperframes-kapak-b.
# -dikey paketi bu betiği kendi sahne dizininden çağırır (SAHNE=<dikey sahne dizini> ... --duzen dikey).
# Önizleme hazırlığı: ONIZLE_YALNIZ=1 bash calistir.sh [--tema koyu]
set -e
for N in /opt/homebrew/bin "$HOME/.nvm/versions/node/v24.22.2/bin"; do [ -d "$N" ] && export PATH="$N:$PATH"; done   # node >= 22
URET="$(cd "$(dirname "$0")" && pwd)"            # uret.py'nin dizini (ana paket sahnesi)
AD="${SAHNE:-$URET}"                              # çıktı sahnesi (ana ya da dikey)
. "$AD/../../ortak/tema.sh" "$@"                  # TEMA, yuk1, tema_bitir
DUZEN=yatay; _a=("$@"); for ((i = 0; i < ${#_a[@]}; i++)); do [ "${_a[i]}" = --duzen ] && DUZEN="${_a[i + 1]}"; done
KOK="$URET/../../../.."                           # kalem kökü
PAKET="$(cd "$AD/../.." && pwd)"
M="$KOK/motorlar/hyperframes"; BIN="$M/node_modules/.bin"
SN=0.5
mkdir -p "$AD/proje/lib" "$AD/k/koyu"
cp "$M/node_modules/gsap/dist/gsap.min.js" "$AD/proje/lib/" 2>/dev/null || cp "$M/lib/gsap.min.js" "$AD/proje/lib/"
/usr/bin/python3 "$URET/uret.py" --tema "$TEMA" --duzen "$DUZEN" --cikti "$AD/proje" >&2
[ -n "$ONIZLE_YALNIZ" ] && { echo "önizleme hazır"; exit 0; }
for i in 1 2 3 4 5; do Y=$(yuk1); [ "$Y" -le 24 ] && break; sleep 60; done   # yük bekçisi
KD="$AD/k"; [ "$TEMA" = koyu ] && KD="$AD/k/koyu"
cd "$AD/proje"
perl -e 'alarm 170; exec @ARGV' "$BIN/hyperframes" snapshot . --at "$SN" --no-end --keep -o "$KD" >&2
HEDEF="$PAKET/kapak.png"; [ "$TEMA" = koyu ] && HEDEF="$PAKET/kapak-koyu.png"
if [ -f "$HEDEF" ]; then                  # silme yok: eski kök kapak ~/Silinecekler/<tarih>-kapak/ altına (02-04 emsali)
  S="$HOME/Silinecekler/$(date +%F)-kapak"; mkdir -p "$S"
  mv "$HEDEF" "$S/$(basename "$PAKET")-$(basename "$HEDEF" .png)-$(date +%H%M%S).png"
fi
cp "$KD/at-${SN}s.png" "$HEDEF"; chmod 644 "$HEDEF"   # snapshot 0600 yazar
file "$HEDEF"
tema_bitir "$AD"
