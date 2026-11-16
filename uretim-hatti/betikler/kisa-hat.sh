#!/bin/bash
# kisa-hat.sh <kod> <paket> <N> [--model M] [--juri-model J] [--esz 3] [--kuru]
#   Huni kısası zinciri (srv21, sef). Varsayılan M=claude-opus-5-5 (A, C, sahneler), J=claude-sonnet-5-5 (B jürileri).
#   Sıra (P0202 emsali): A (M) → B-dil + B-kural (J, paralel; A "bitti 0" olunca) → C (M; iki B "bitti 0" olunca)
#   → sahne istemleri kuyruğu (M, --esz eşzamanlı; C "bitti 0" olunca) → çakışma kapısı.
#   Bir adım hatayla biterse sonrakiler başlamaz (sonra.sh/sonra2.sh/zincir2.sh "bitti 90").
#   Jüri modeli üretici modelinden farklı olmalı (README kural 5): --model claude-sonnet-5-5 verilip --juri-model
#   verilmezse jüri claude-opus-5-5 olur; ikisi aynı verilirse çıkış 2.
#   İstemler ~/is/uretim-0204/P<kod>-S<N>-{A,B-dil,B-kural,C}.md olarak sunucuda hazır olmalı
#   (kisa-istem-uret.py üretir; şef kopyalar). --kuru hiçbir şey başlatmaz, planı basar.
#   İş adı P<kod>-S<N>-<adım>; sahne kuyruğu öneki K<kod>S<N>.
set -uo pipefail
BU="$(cd "$(dirname "$0")" && pwd)"
D="$HOME/is/uretim-0204"; K="$HOME/01dev/_worktrees/kalem-0204"
KURU=0; M="claude-opus-5-5"; J=""; ESZ=3; POS=()
while [ $# -gt 0 ]; do
  case "$1" in
    --model) M="${2:?--model değer ister}"; shift 2 ;;
    --juri-model) J="${2:?--juri-model değer ister}"; shift 2 ;;
    --esz) ESZ="${2:?--esz değer ister}"; shift 2 ;;
    --kuru) KURU=1; shift ;;
    -*) echo "bilinmeyen bayrak: $1" >&2; exit 2 ;;
    *) POS+=("$1"); shift ;;
  esac
done
[ "${#POS[@]}" -eq 3 ] || { echo "kullanım: kisa-hat.sh <kod> <paket> <N> [--model M] [--juri-model J] [--esz 3] [--kuru]" >&2; exit 2; }
KOD="${POS[0]}"; PAKET="${POS[1]}"; N="${POS[2]}"
case "$N" in ''|*[!0-9]*) echo "N sayı olmalı: $N" >&2; exit 2 ;; esac
if [ -z "$J" ]; then
  J="claude-sonnet-5-5"; [ "$M" = "$J" ] && J="claude-opus-5-5"
elif [ "$J" = "$M" ]; then
  echo "jüri modeli üretici modelle aynı olamaz: $J" >&2; exit 2
fi
A="P$KOD-S$N-A"; BD="P$KOD-S$N-B-dil"; BK="P$KOD-S$N-B-kural"; C="P$KOD-S$N-C"; ON="K${KOD}S$N"
SAHNE="$K/projeler/$PAKET-s$N/uretim-tutanagi/istem/sahne"
# Yardımcı betikler (sonra/sonra2/zincir2) git kopyasından koşar: sunucu dizinindeki eski kopyalar KISA_MODEL'i
# tanımaz (16.11 ölçüm: ~/is/uretim-0204/sonra.sh içinde KISA_MODEL 0) ve C ile sahneleri sessizce opus'ta koşturur.
S="$BU"

echo "plan: $KOD $PAKET S$N · üretici $M · jüri $J · sahne eşzamanlı $ESZ"
printf ' 1. %-22s %-18s istem %s/%s.md  bekler: -\n' "$A" "$M" "$D" "$A"
printf ' 2. %-22s %-18s istem %s/%s.md  bekler: %s bitti 0\n' "$BD" "$J" "$D" "$BD" "$A"
printf ' 3. %-22s %-18s istem %s/%s.md  bekler: %s bitti 0\n' "$BK" "$J" "$D" "$BK" "$A"
printf ' 4. %-22s %-18s istem %s/%s.md  bekler: %s + %s bitti 0\n' "$C" "$M" "$D" "$C" "$BD" "$BK"
printf ' 5. sahne kuyruğu %-9s %-18s istem %s/D-*.md  bekler: %s bitti 0 (en çok %s eşzamanlı)\n' "$ON" "$M" "$SAHNE" "$C" "$ESZ"
printf ' 6. çakışma kapısı %s-s%s  bekler: sahne kuyruğu bitti\n' "$PAKET" "$N"
[ "$KURU" -eq 1 ] && { echo "kuru: hiçbir şey başlatılmadı"; exit 0; }

for ad in "$A" "$BD" "$BK" "$C"; do
  [ -r "$D/$ad.md" ] || { echo "istem yok: $D/$ad.md (kisa-istem-uret.py ile üret, sunucuya kopyala)" >&2; exit 2; }
done
# önceki koşudan kalan bitmiş durum dosyaları zinciri yanıltır (B/C eski sonucu "bitti" görür): eski/ altına taşı
EZ="$D/eski/$(date +%Y%m%d-%H%M%S)-kisa-hat-$KOD-S$N"
for ad in "$BD" "$BK" "$C" "sonra-$A" "sonra2-$C" "zincir2-$ON" "kuyruk-$ON"; do
  [ -f "$D/$ad.durum" ] || continue
  case "$(cat "$D/$ad.durum")" in calisiyor*) echo "zaten çalışıyor: $ad" >&2; exit 1 ;; esac
  mkdir -p "$EZ"; mv "$D/$ad.durum" "$EZ/"
done
bash "$D/kos.sh" "$A" "$M" "$D/$A.md" || { echo "A başlamadı: zincir kurulmadı" >&2; exit 1; }
KISA_MODEL="$J" bash "$S/sonra.sh" "$A" "$BD" "$BK" || exit 1
KISA_MODEL="$M" bash "$S/sonra2.sh" "$BD" "$BK" "$C" || exit 1
KISA_MODEL="$M" bash "$S/zincir2.sh" "$C" "$ON" "$PAKET-s$N" sahne "$ESZ" || exit 1
echo "zincir kuruldu: $A → ($BD, $BK) → $C → $ON → kapı"
