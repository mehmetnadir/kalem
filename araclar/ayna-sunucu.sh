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
# Eksilme bekçisi (15.11): yükleme aynadaki paket ağacını bütünüyle değiştirir. Kaynakta git dışı kalan dosya
# (ses, gsap, yazı tipi) yoksa aynadan da kaybolur ve editör kararır. Aynada olup kaynakta olmayan böyle dosya
# varsa yükleme durur. Bilerek eksiltmek için: AYNA_EKSILT=1.
AYNA_DEPO="${AYNA_DEPO:-$KAYIT/storage/kontrol-ayna/projeler}"
if [ "${AYNA_EKSILT:-0}" != 1 ]; then
  for p in "${paketler[@]}"; do
    # R2 budaması (16.11, r2-ders-arsiv.sh): git dışı kare/ses/mp4 sunucudan silinmiş paket yüklenmez.
    if [ -f "$KOK/projeler/$p/R2-BUDANDI.txt" ]; then
      echo "HATA: $p R2'ye arşivlenip budandı ($KOK/projeler/$p/R2-BUDANDI.txt); yükleme aynadan kare/ses düşürür." >&2
      echo "Önce geri yükle (r2-arsiv.sh geri …), sonra işaret dosyasını kaldır." >&2
      exit 1
    fi
    [ -d "$AYNA_DEPO/$p" ] || continue
    kayip="$(cd "$AYNA_DEPO/$p" && find . -type f \( -name '*.wav' -o -name '*.m4a' -o -name '*.mp3' -o -name '*.min.js' \
      -o -path './ortak/font/*' \) | while read -r f; do [ -f "$KOK/projeler/$p/$f" ] || echo "$f"; done)"
    if [ -n "$kayip" ]; then
      echo "HATA: $p — aynada olup kaynakta olmayan $(echo "$kayip" | wc -l) dosya var; yükleme bunları düşürür:" >&2
      echo "$kayip" | head -8 >&2
      echo "Kaynağı tamamla (ör. ayna-kayip.py --kopyala) ya da AYNA_EKSILT=1 ile bilerek eksilt." >&2
      exit 1
    fi
  done
fi
cd "$KAYIT"
echo "→ ayna eşitleme: kök $KOK ${arg[*]}"
exec timeout 900 node --import tsx scripts/kontrol-ayna-esitle.ts --kalem "$KOK" --adres "$ADRES" "${arg[@]}"
