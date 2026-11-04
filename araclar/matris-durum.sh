#!/bin/bash
# Üretim matrisi durumu: proje başına sahne videoları (A = açık, K = koyu) ve birleşik çıktılar.
#   araclar/matris-durum.sh [proje...]   (boşsa projeler/ altındaki zaman.json'lu bütün projeler)
export PATH=/opt/homebrew/bin:$PATH
K="$(cd "$(dirname "$0")/.." && pwd)"; cd "$K"
kare() { ffprobe -v error -select_streams v:0 -show_entries stream=nb_frames -of csv=p=0 "$1" 2>/dev/null; }
if [ $# -gt 0 ]; then P="$*"; else P=$(ls -d projeler/*/ | sed 's#/$##' | while read -r d; do [ -f "$d/zaman.json" ] && echo "$d"; done); fi
printf '%-34s %-42s %-12s %-12s\n' PROJE SAHNELER "CIKTI(acik)" "CIKTI(koyu)"
for p in $P; do
  s=""
  for d in "$p"/sahneler/*/; do
    [ -d "$d" ] || continue
    n=$(basename "$d" | cut -c1-2)
    a=$([ -f "$d/video-acik.mp4" ] && echo A || echo -); k=$([ -f "$d/video-koyu.mp4" ] && echo K || echo -)
    s="$s$n$a$k "
  done
  [ -n "$s" ] || s="(sahne yok)"
  ca=$([ -f "$p/cikti.mp4" ] && kare "$p/cikti.mp4" || echo -)
  ck=$([ -f "$p/cikti-koyu.mp4" ] && kare "$p/cikti-koyu.mp4" || echo -)
  printf '%-34s %-42s %-12s %-12s\n' "$(basename "$p")" "$s" "$ca" "$ck"
done
