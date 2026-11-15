#!/bin/bash
# Dikey ana ders kapağı 1080x1920 (kapak standardı v1). Üretici ve yerleşim ana pakette (tek kaynak, iki ayrı düzen):
#   ../../../present-perfect-cont-temel/sahneler/90-hyperframes-kapak/uret.py --duzen dikey
# Görseller bu paketin ortak/kapak/ bağından (-> ana paket ortak/kapak) proje/assets/ altına kopyalanır.
#   bash calistir.sh [--tema acik|koyu]   -> paket kökü kapak.png (açık) · kapak-koyu.png (koyu)
set -e
AD="$(cd "$(dirname "$0")" && pwd)"
SAHNE="$AD" exec bash "$AD/../../../present-perfect-cont-temel/sahneler/90-hyperframes-kapak/calistir.sh" "$@" --duzen dikey
