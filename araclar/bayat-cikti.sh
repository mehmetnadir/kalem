#!/bin/bash
# Birleşik çıktısı sahne videolarından eski olan projeleri listeler (yeniden birleştirme gerekir).
#   araclar/bayat-cikti.sh [projeler/<proje>...]
K="$(cd "$(dirname "$0")/.." && pwd)"; cd "$K"
P=${*:-projeler/*}
for p in $P; do
  for c in cikti.mp4 cikti-koyu.mp4; do
    [ -f "$p/$c" ] || continue
    tema=acik; [ "$c" = cikti-koyu.mp4 ] && tema=koyu
    for v in "$p"/sahneler/*/video-$tema.mp4; do
      [ -f "$v" ] && [ "$v" -nt "$p/$c" ] && echo "BAYAT: $p/$c < $v"
    done
  done
done
echo "kontrol bitti"
