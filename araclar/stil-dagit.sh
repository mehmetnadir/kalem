#!/usr/bin/env bash
# Stil modüllerini tek kaynaktan (ortak/stil) paketlere dağıtır ve denetler.
# Kullanım: stil-dagit.sh <paket>... | --hepsi | --denetle [paket... | --hepsi]
set -euo pipefail

KOK="$(cd "$(dirname "$0")/.." && pwd)"
KAYNAK="$KOK/ortak/stil"
ALT="sahneler/02-paperjs-kanca"

kullanim() {
  echo "Kullanım: stil-dagit.sh <paket>... | --hepsi | --denetle [paket... | --hepsi]" >&2
  exit 2
}

hash_of() { shasum -a 256 "$1" | cut -d' ' -f1; }

paketler_hepsi() {
  local d
  for d in "$KOK"/projeler/*/; do
    [ -d "${d}${ALT}" ] && basename "$d"
  done
  return 0
}

dagit() {
  local p="$1" hedef="$KOK/projeler/$1/$ALT/stil" f ad tarih commit ilk=1
  [ -d "$KOK/projeler/$p/$ALT" ] || { echo "YOK paket: $p" >&2; exit 2; }
  mkdir -p "$hedef"
  for f in "$KAYNAK"/*.js; do cp "$f" "$hedef/$(basename "$f")"; done
  tarih="$(date '+%Y-%m-%dT%H:%M:%S%z')"
  commit="$(git -C "$KOK" rev-parse --short HEAD 2>/dev/null || echo yok)"
  {
    echo "{"
    echo "  \"kaynak\": \"ortak/stil\","
    echo "  \"tarih\": \"$tarih\","
    echo "  \"commit\": \"$commit\","
    echo "  \"dosyalar\": {"
    for f in "$KAYNAK"/*.js; do
      ad="$(basename "$f")"
      [ "$ilk" = 1 ] || echo ","
      ilk=0
      printf '    "%s": "%s"' "$ad" "$(hash_of "$f")"
    done
    echo ""
    echo "  }"
    echo "}"
  } > "$hedef/STIL-SURUM.json"
  echo "DAĞITILDI $p"
}

# stdout: KALDI satırları; dönüş: 0 eşit, 1 ayrışmış, 3 stil/ yok
denetle_bir() {
  local p="$1" hedef="$KOK/projeler/$1/$ALT/stil" f ad kalan=0
  [ -d "$hedef" ] || return 3
  for f in "$KAYNAK"/*.js; do
    ad="$(basename "$f")"
    if [ ! -f "$hedef/$ad" ] || [ "$(hash_of "$f")" != "$(hash_of "$hedef/$ad")" ]; then
      echo "KALDI $p $ad"
      kalan=1
    fi
  done
  return $kalan
}

denetle() {
  local liste="$*" p rc n=0 kotu=0
  [ -n "$liste" ] || kullanim
  if [ "$liste" = "--hepsi" ]; then liste="$(paketler_hepsi)"; fi
  for p in $liste; do
    rc=0
    denetle_bir "$p" || rc=$?
    if [ "$rc" = 3 ]; then
      echo "bilgi: $p stil/ yok, atlandı"
    elif [ "$rc" = 0 ]; then
      n=$((n + 1))
    else
      kotu=1
    fi
  done
  if [ "$kotu" = 1 ]; then exit 1; fi
  echo "GEÇTİ $n paket"
}

[ $# -ge 1 ] || kullanim
case "$1" in
  --denetle)
    shift
    [ $# -ge 1 ] || kullanim
    denetle "$@"
    ;;
  --hepsi)
    for p in $(paketler_hepsi); do dagit "$p"; done
    ;;
  -*) kullanim ;;
  *)
    for p in "$@"; do dagit "$p"; done
    ;;
esac
