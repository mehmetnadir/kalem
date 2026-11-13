#!/usr/bin/env bash
# Sahne QA'sı (çakışma kapısı + açık/koyu kare) srv21'de sef ile koşar — Mac yükünden bağımsız (13.11, K-0063).
#   araclar/sunucu-qa.sh <paket> <sahne> <acik_t1,t2,…> <koyu_t> [--hazirla] [--kapisiz]
#   1. rsync: projeler/<paket>/ → /home/sef/01dev/kalem/projeler/<paket>/ (artımlı; ayna-gonder hariç listesi + k/)
#   2. sunucuda önizleme sunucusu (41012) + başsız Chrome (41333) açık değilse açılır (araclar/sunucu-onizle.sh)
#   3. --hazirla: sunucuda ONIZLE_YALNIZ=1 calistir.sh --tema acik; sonra sahne dizini Mac'e geri çekilir (k/ hariç)
#   4. çakışma kapısı (--kapisiz atlar) + sahne-kare açık zamanlar, koyu zaman
#   5. kareler Mac'e: sahneler/<sahne>/k/<sahne>-<t>.png ve k/koyu/<sahne>-<t>.png
# Sunucuda en çok 3 koşu aynı anda (flock yuvası); fazlası 30 dk'ya kadar bekler.
# Ortak dizinler (present-continuous/ortak, araclar/, motorlar/) sunucuda hazır olmalı (13.11 kuruldu).
set -euo pipefail
export PATH="/opt/homebrew/bin:$PATH"
KALEM="$(cd "$(dirname "$0")/.." && pwd)"
HEDEF="${QA_HEDEF:-root@100.117.187.26}"
PORT="${QA_PORT:-2222}"
UZAK="/home/sef/01dev/kalem"
# ControlPath=none: ortak ssh çoklama soketi asılı kalınca bütün koşular asılıyordu (13.11); her çağrı kendi bağlantısı.
SSH_SEC="-p $PORT -o ConnectTimeout=12 -o BatchMode=yes -o ServerAliveInterval=20 -o ControlPath=none"
HARIC=(--exclude 'k/' --exclude 'renders/' --exclude '_is/' --exclude 'manifest/' --exclude 'kareler/'
  --exclude 'node_modules/' --exclude '*.mp4' --exclude 'cumle-*.wav' --exclude 'sentez.wav'
  --exclude '.DS_Store' --exclude '__pycache__/')

hazirla=0 kapi=1 konum=()
for a in "$@"; do
  case "$a" in
    --hazirla) hazirla=1 ;;
    --kapisiz) kapi=0 ;;
    -*) echo "HATA: bilinmeyen seçenek $a" >&2; exit 1 ;;
    *) konum+=("$a") ;;
  esac
done
[ "${#konum[@]}" -eq 4 ] || {
  echo "kullanım: sunucu-qa.sh <paket> <sahne> <acik_t1,t2,…> <koyu_t> [--hazirla] [--kapisiz]" >&2; exit 1; }
P="${konum[0]}" S="${konum[1]}" ACIK="${konum[2]}" KOYU="${konum[3]}"
[[ "$P" =~ ^[a-z0-9]+(-[a-z0-9]+)*$ ]] || { echo "HATA: paket adı kural dışı: $P" >&2; exit 1; }
[[ "$S" =~ ^[0-9]{2}-[a-z0-9]+(-[a-z0-9]+)*$ ]] || { echo "HATA: sahne adı kural dışı: $S" >&2; exit 1; }
[[ "$ACIK" =~ ^[0-9]+(\.[0-9]+)?(,[0-9]+(\.[0-9]+)?)*$ ]] || { echo "HATA: açık zamanlar: $ACIK" >&2; exit 1; }
[[ "$KOYU" =~ ^[0-9]+(\.[0-9]+)?$ ]] || { echo "HATA: koyu zaman: $KOYU" >&2; exit 1; }
[ -d "$KALEM/projeler/$P/sahneler/$S" ] || { echo "HATA: sahne yok: $P/$S" >&2; exit 1; }

echo "→ rsync $P"
rsync -az --delete "${HARIC[@]}" -e "ssh $SSH_SEC" "$KALEM/projeler/$P/" "$HEDEF:$UZAK/projeler/$P/"
# shellcheck disable=SC2086
ssh $SSH_SEC "$HEDEF" "chown -R sef:sef $UZAK/projeler/$P"

echo "→ sunucuda QA: $S"
# shellcheck disable=SC2086
ssh $SSH_SEC "$HEDEF" "runuser -u sef -- bash -s -- $P $S $ACIK $KOYU $hazirla $kapi" <<'UZAK_BETIK'
set -u
export PATH=/home/sef/.nvm/versions/node/v24.22.2/bin:$PATH
P=$1 S=$2 ACIK=$3 KOYU=$4 HAZ=$5 KAPI=$6
K=/home/sef/01dev/kalem; C=/home/sef/.cache; O=/home/sef/qa-kare/$P/$S
mkdir -p "$O/koyu" "$C"
YUVA=""
for i in 1 2 3; do
  exec 9>"$C/qa-yuva-$i.lock"
  if flock -n 9; then YUVA=$i; break; fi
done
if [ -z "$YUVA" ]; then
  exec 9>"$C/qa-yuva-1.lock"
  flock -w 1800 9 || { echo "HATA: yuva 30 dk boşalmadı"; exit 3; }
  YUVA=1
fi
echo "yuva $YUVA"
cd "$K" || exit 4
# -o ve 9>&-: başlatılan uzun ömürlü önizleme/Chrome süreçleri kilit dosyalarını devralmasın (13.11: devraldı,
# yuva 1 ve başlatma kilidi kalıcı tutuldu, bütün koşular kilitlendi).
flock -o "$C/qa-baslat.lock" bash araclar/sunucu-onizle.sh baslat > /dev/null 9>&- \
  || { echo "HATA: önizleme/Chrome açılamadı"; bash araclar/sunucu-onizle.sh durum; exit 4; }
if [ "$HAZ" = 1 ]; then
  echo "== HAZIRLA"
  (cd "projeler/$P/sahneler/$S" && ONIZLE_YALNIZ=1 timeout 600 bash calistir.sh --tema acik 2>&1 | tail -5)
fi
rc=0
if [ "$KAPI" = 1 ]; then
  echo "== KAPI"
  timeout 600 node araclar/cakisma-kapisi.mjs "$P" --sahne "$S" --port 41333 --sunucu 41012 2>&1 | tail -25
  rc=${PIPESTATUS[0]}
fi
echo "== KARE (açık)"
timeout 300 node araclar/sahne-kare.mjs "$P" "$S" "$ACIK" "$O" --tema acik --port 41333 --sunucu 41012 2>&1 \
  | grep -o '"png":"[^"]*"\|[Hh]ata.*\|HATA.*'
echo "== KARE (koyu)"
timeout 300 node araclar/sahne-kare.mjs "$P" "$S" "$KOYU" "$O/koyu" --tema koyu --port 41333 --sunucu 41012 2>&1 \
  | grep -o '"png":"[^"]*"\|[Hh]ata.*\|HATA.*'
echo "kapı çıkış kodu: $rc"
UZAK_BETIK

if [ "$hazirla" = 1 ]; then
  echo "→ hazırlanan sahne Mac'e"
  rsync -az --exclude 'k/' --exclude 'kareler/' -e "ssh $SSH_SEC" \
    "$HEDEF:$UZAK/projeler/$P/sahneler/$S/" "$KALEM/projeler/$P/sahneler/$S/"
fi
echo "→ kareler Mac'e"
mkdir -p "$KALEM/projeler/$P/sahneler/$S/k"
rsync -az -e "ssh $SSH_SEC" "$HEDEF:/home/sef/qa-kare/$P/$S/" "$KALEM/projeler/$P/sahneler/$S/k/"
ls "$KALEM/projeler/$P/sahneler/$S/k/" "$KALEM/projeler/$P/sahneler/$S/k/koyu/" 2>/dev/null | grep -F "$S-" || true
