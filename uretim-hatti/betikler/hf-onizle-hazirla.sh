#!/bin/bash
# hf-onizle-hazirla.sh — eksik gsap.min.js içeren HyperFrames sahnelerini hazırlar.
# Kullanım: hf-onizle-hazirla.sh [--kuru] [paket...]
# Ortam: KALEM_KOK (varsayılan betiğin iki üst dizini)

set -uo pipefail

BETIK_DIZIN="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VARSAYILAN_KOK="$(cd "$BETIK_DIZIN/../.." && pwd)"
KOK="${KALEM_KOK:-$VARSAYILAN_KOK}"

KURU=0
PAKETLER=()

for arg in "$@"; do
  if [ "$arg" = "--kuru" ]; then
    KURU=1
  else
    PAKETLER+=("$arg")
  fi
done

PAKET_DIZINLERI=()

if [ ${#PAKETLER[@]} -gt 0 ]; then
  for p in "${PAKETLER[@]}"; do
    if [ -d "$p" ]; then
      PAKET_DIZINLERI+=("$p")
    elif [ -d "$KOK/projeler/$p" ]; then
      PAKET_DIZINLERI+=("$KOK/projeler/$p")
    elif [ -d "$KOK/$p" ]; then
      PAKET_DIZINLERI+=("$KOK/$p")
    fi
  done
else
  if [ -d "$KOK/projeler" ]; then
    for d in "$KOK/projeler"/*; do
      if [ -d "$d" ]; then
        PAKET_DIZINLERI+=("$d")
      fi
    done
  fi
fi

EKSIK_SAHNELER=()

if [ ${#PAKET_DIZINLERI[@]} -gt 0 ]; then
  for pd in "${PAKET_DIZINLERI[@]}"; do
    [ -d "$pd" ] || continue
    p_ad="$(basename "$pd")"
    sahneler_dir="$pd/sahneler"
    [ -d "$sahneler_dir" ] || continue

    for sd in "$sahneler_dir"/*; do
      [ -d "$sd" ] || continue
      s_ad="$(basename "$sd")"
      case "$s_ad" in
        *hyperframes*)
          if [ -f "$sd/calistir.sh" ] && [ ! -f "$sd/proje/lib/gsap.min.js" ]; then
            EKSIK_SAHNELER+=("$p_ad/$s_ad|$sd")
          fi
          ;;
      esac
    done
  done
fi

toplam_eksik=${#EKSIK_SAHNELER[@]}

if [ "$KURU" -eq 1 ]; then
  if [ "$toplam_eksik" -gt 0 ]; then
    for kayit in "${EKSIK_SAHNELER[@]}"; do
      etiket="${kayit%%|*}"
      echo "$etiket"
    done
  fi
  echo "SONUÇ eksik $toplam_eksik"
  exit 0
fi

hazirlanan=0
hatali=0
HATALI_LISTE=()

if [ "$toplam_eksik" -gt 0 ]; then
  for kayit in "${EKSIK_SAHNELER[@]}"; do
    etiket="${kayit%%|*}"
    sd="${kayit##*|}"
    if (cd "$sd" && ONIZLE_YALNIZ=1 bash calistir.sh); then
      hazirlanan=$((hazirlanan + 1))
    else
      hatali=$((hatali + 1))
      HATALI_LISTE+=("$etiket")
    fi
  done
fi

echo "SONUÇ hazırlanan $hazirlanan · hatalı $hatali"

if [ "$hatali" -gt 0 ]; then
  for h in "${HATALI_LISTE[@]}"; do
    echo "Hatalı sahne: $h"
  done
  exit 1
fi

exit 0
