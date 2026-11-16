#!/bin/bash
# kredi-sec.sh <org|auto> — kredi kipinde hangi org'un anahtar dosyası kullanılacak. (srv21, sef)
# Çıktı: "<org> <env dosyası>" ya da çıkış 1. Anahtar değeri okunmaz, basılmaz; yalnız dosya varlığı ve defter toplamı.
# Tavan: KREDI_TAVAN (varsayılan 170 $ / org / ay). 190 $ kredinin 20 $'ı aynı anda koşan oturumlar için pay.
set -uo pipefail
DIZIN="$HOME/is/uretim-0204"; CFG="$HOME/.config/sef"
DEFTER="$DIZIN/kredi-defter.jsonl"; AY=$(date -u +%Y-%m)
TAVAN="${KREDI_TAVAN:-170}"
istek="${1:-auto}"
if [ "$istek" = "auto" ]; then adaylar=$(ls "$CFG"/kredi-*.env 2>/dev/null | sed -E 's/.*kredi-([0-9]+)\.env/\1/' | sort -n)
else adaylar="$istek"; fi
for o in $adaylar; do
  f="$CFG/kredi-$o.env"
  [ -r "$f" ] || continue
  # kos-calis.sh "Credit balance is too low" görünce bu işareti yazar (defter Mac harcamasını görmez).
  if [ -e "$DIZIN/kredi-bitti-$o-$AY" ]; then echo "org $o kredisi bitti (işaret $AY)" >&2; continue; fi
  harc=$(grep -a "\"ay\":\"$AY\"" "$DEFTER" 2>/dev/null | grep -a "\"org\":\"$o\"" \
    | grep -a -o '"maliyet":[0-9.]*' | cut -d: -f2 | awk '{s+=$1} END {printf "%.2f", s+0}')
  if awk -v h="$harc" -v t="$TAVAN" 'BEGIN {exit !(h < t)}'; then echo "$o $f"; exit 0; fi
  echo "org $o tavanda: $harc / $TAVAN \$" >&2
done
echo "kredi yok (anahtar dosyası ya da tavan altı org yok)" >&2
exit 1
