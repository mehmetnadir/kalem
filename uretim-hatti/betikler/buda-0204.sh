#!/bin/bash
# buda-0204.sh — YALNIZ 02-04-ydt-temel öğesinde kaynakta olmayan, revizyonsuz sürüm satırlarını budar (srv21, sef).
# Gövde ~/is/uretim-0204/buda-0204.json (huni-tasi.py yazar). Jeton işçi ortam dosyasından; ekrana basılmaz.
set -a; . "$HOME/.config/sef/kontrol.env"; set +a
curl -sS -m 60 -X POST http://127.0.0.1:3810/api/kontrol/ice-al/buda \
  -H 'Content-Type: application/json' -H "x-kontrol-jeton: $KONTROL_ISCI_JETON" -H 'x-kontrol-isci: ice-al-betik' \
  --data-binary @"$HOME/is/uretim-0204/buda-0204.json" -w '\nhttp %{http_code}\n'
