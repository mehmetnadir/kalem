#!/usr/bin/env bash
# Paket(ler)i editör paneline (kayit.ndr.ist /ai-video) yansıtır — Mac'te jeton YOK, eşitleme sunucuda koşar.
#   1. rsync: kalem/projeler/<paket>/ (+ --ortak: ortak/, katalog.json, paper-core.js) → srv21 /home/sef/kalem-ayna/
#   2. chown sef (yazılan dizin sef'in)
#   3. sunucuda kayit uygulamasının env'iyle scripts/kontrol-ayna-esitle.ts (iç adres 127.0.0.1:3810, işçi jetonu)
# rsync artımlıdır (değişmeyen dosya gitmez); eşitleme sha256 aynıysa sunucuda yeni sürüm yazmaz.
# Kullanım: araclar/ayna-gonder.sh [--ortak] [--kuru] <paket> [<paket> …]
#           araclar/ayna-gonder.sh --ortak            (yalnız ortak + katalog)
set -euo pipefail
export PATH="/opt/homebrew/bin:$PATH"
KALEM="$(cd "$(dirname "$0")/.." && pwd)"
HEDEF="${AYNA_HEDEF:-root@100.117.187.26}"
PORT="${AYNA_PORT:-2222}"
UZAK_KOK="/home/sef/kalem-ayna"
SSH=(ssh -p "$PORT" -o ConnectTimeout=12 -o BatchMode=yes)
HARIC=(--exclude 'k/' --exclude 'renders/' --exclude '_is/' --exclude 'manifest/' --exclude 'kareler/'
  --exclude 'node_modules/' --exclude '*.mp4' --exclude 'cumle-*.wav' --exclude 'sentez.wav'
  --exclude '.DS_Store' --exclude '__pycache__/')

ortak=0 kuru=0 paketler=()
for a in "$@"; do
  case "$a" in
    --ortak) ortak=1 ;;
    --kuru) kuru=1 ;;
    -*) echo "HATA: bilinmeyen seçenek $a" >&2; exit 1 ;;
    *)
      [[ "$a" =~ ^[a-z0-9]+(-[a-z0-9]+)*$ ]] || { echo "HATA: paket adı kural dışı: $a" >&2; exit 1; }
      [ -d "$KALEM/projeler/$a" ] || { echo "HATA: paket yok: $KALEM/projeler/$a" >&2; exit 1; }
      paketler+=("$a") ;;
  esac
done
[ "${#paketler[@]}" -gt 0 ] || [ "$ortak" = 1 ] || { echo "kullanım: ayna-gonder.sh [--ortak] [--kuru] <paket>…" >&2; exit 1; }

RS=(rsync -az --delete "${HARIC[@]}" -e "ssh -p $PORT -o ConnectTimeout=12 -o BatchMode=yes")
[ "$kuru" = 1 ] && RS+=(-n --itemize-changes)

"${SSH[@]}" "$HEDEF" "install -d -o sef -g sef $UZAK_KOK/projeler $UZAK_KOK/motorlar/paperjs/node_modules/paper/dist"
for p in ${paketler[@]+"${paketler[@]}"}; do
  echo "→ rsync $p"
  "${RS[@]}" "$KALEM/projeler/$p/" "$HEDEF:$UZAK_KOK/projeler/$p/"
done
if [ "$ortak" = 1 ]; then
  echo "→ rsync ortak + katalog"
  "${RS[@]}" "$KALEM/ortak/" "$HEDEF:$UZAK_KOK/ortak/"
  "${RS[@]}" "$KALEM/projeler/katalog.json" "$HEDEF:$UZAK_KOK/projeler/katalog.json"
  "${RS[@]}" "$KALEM/motorlar/paperjs/node_modules/paper/dist/paper-core.js" \
    "$HEDEF:$UZAK_KOK/motorlar/paperjs/node_modules/paper/dist/paper-core.js"
fi
"${SSH[@]}" "$HEDEF" "chown -R sef:sef $UZAK_KOK"

arg=""
[ "${#paketler[@]}" -gt 0 ] && arg="--paket $(IFS=,; echo "${paketler[*]}")"
[ "$ortak" = 1 ] && arg="$arg --ortak"
[ "$kuru" = 1 ] && arg="$arg --kuru"
echo "→ sunucuda eşitleme:$arg"
"${SSH[@]}" "$HEDEF" "cd /var/www/videokayit && timeout 900 node --env-file=.env --import tsx \
  scripts/kontrol-ayna-esitle.ts --kalem $UZAK_KOK --adres http://127.0.0.1:3810 $arg 2>&1 | tail -30"
