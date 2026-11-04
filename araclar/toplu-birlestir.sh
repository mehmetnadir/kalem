#!/bin/bash
# Birden çok projeyi iki temada birleştirir; aynı anda en çok 3 proje. Günlük: <proje>/_birlestir.log
#   araclar/toplu-birlestir.sh projeler/a projeler/b ...
export PATH=/opt/homebrew/bin:$PATH
K="$(cd "$(dirname "$0")/.." && pwd)"; cd "$K"
tek() {
  p="$1"; L="$p/_birlestir.log"; : > "$L"
  for tema in acik koyu; do
    /usr/bin/python3 birlestir.py "$p" --tema "$tema" --gecis BookFlip --efekt hisirti >> "$L" 2>&1 \
      || { echo "HATA: $p $tema (bkz. $L)"; return 1; }
  done
  echo "tamam: $p $(tail -1 "$L" | sed 's/.*mp4 *//')"
}
export -f tek
printf '%s\n' "$@" | xargs -P 3 -I{} bash -c 'tek "$@"' _ {}
