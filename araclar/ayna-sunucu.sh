#!/bin/bash
# Sunucuda üretilen paketi kayit aynasına yükler (srv21, kullanıcı sef). Mac'teki ayna-gonder.sh'in karşılığı:
# rsync yok, paket zaten sunucuda; eşitleme betiği /var/www/videokayit'ten koşar, jeton işçi ortam dosyasından gelir.
#   araclar/ayna-sunucu.sh [--kok <kalem dizini>] [--ortak] [--kuru] <paket>…
# --kok verilmezse bu betiğin bulunduğu kalem kökü kullanılır (worktree de olur).
set -euo pipefail
KOK="$(cd "$(dirname "$0")/.." && pwd)"
ORTAM="${KONTROL_ORTAM:-$HOME/.config/sef/kontrol.env}"
KAYIT="${KAYIT_KOK:-/var/www/videokayit}"
ADRES="${KONTROL_ADRES:-http://127.0.0.1:3810}"
arg=() paketler=()
while [ $# -gt 0 ]; do
  case "$1" in
    --kok) KOK="$(cd "$2" && pwd)"; shift 2 ;;
    --ortak|--kuru) arg+=("$1"); shift ;;
    -*) echo "HATA: bilinmeyen seçenek $1" >&2; exit 1 ;;
    *)
      [[ "$1" =~ ^[a-z0-9]+(-[a-z0-9]+)*$ ]] || { echo "HATA: paket adı kural dışı: $1" >&2; exit 1; }
      [ -d "$KOK/projeler/$1" ] || { echo "HATA: paket yok: $KOK/projeler/$1" >&2; exit 1; }
      paketler+=("$1"); shift ;;
  esac
done
[ "${#paketler[@]}" -gt 0 ] || [ "${#arg[@]}" -gt 0 ] || { echo "kullanım: ayna-sunucu.sh [--kok D] [--ortak] [--kuru] <paket>…" >&2; exit 1; }
[ -r "$ORTAM" ] || { echo "HATA: işçi ortam dosyası okunamıyor: $ORTAM" >&2; exit 1; }
KONTROL_ISCI_JETON="$(sed -n 's/^KONTROL_ISCI_JETON=//p' "$ORTAM" | tail -1)"
[ -n "$KONTROL_ISCI_JETON" ] || { echo "HATA: $ORTAM içinde KONTROL_ISCI_JETON yok" >&2; exit 1; }
export KONTROL_ISCI_JETON
[ "${#paketler[@]}" -gt 0 ] && arg+=(--paket "$(IFS=,; echo "${paketler[*]}")")
cd "$KAYIT"
echo "→ ayna eşitleme: kök $KOK ${arg[*]}"
exec timeout 900 node --import tsx scripts/kontrol-ayna-esitle.ts --kalem "$KOK" --adres "$ADRES" "${arg[@]}"
