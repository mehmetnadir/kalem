#!/bin/bash
# Sunucuda (srv21, sef) yerel sahne QA'sı: sunucu-qa.sh'in Mac'siz karşılığı. rsync/ssh yok; kalem kökü bu betiğin
# deposu (worktree de olur). Ana depo dışındaki kök için ayrı önizleme sunucusu açar (varsayılan 41022), Chrome'u
# (CDP 41333) ana önizlemeyle paylaşır. Kareler ~/qa-kare/<paket>/<sahne>/ ve sahne dizinindeki k/ altına yazılır.
#   araclar/qa-yerel.sh <paket> <sahne> <acik_t1,t2,…> <koyu_t> [--hazirla] [--kapisiz]
set -u
if [ "$(uname -s)" != "Linux" ] || [ "$(id -un)" != "sef" ]; then
  echo "yalnız Linux/sef: bu betik sunucuda sef kullanıcısı ile koşar" >&2; exit 1
fi
export PATH="/home/sef/.nvm/versions/node/v24.22.2/bin:$PATH"
K="$(cd "$(dirname "$0")/.." && pwd)"
ANA="${QA_ANA_KOK:-/home/sef/01dev/kalem}"
CDP="${CDP_PORT:-41333}"
if [ "$K" = "$ANA" ]; then PORT="${ONIZLE_PORT:-41012}"; else PORT="${ONIZLE_PORT:-41022}"; fi
C=/home/sef/.cache
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
  echo "kullanım: qa-yerel.sh <paket> <sahne> <acik_t1,t2,…> <koyu_t> [--hazirla] [--kapisiz]" >&2; exit 1; }
P="${konum[0]}" S="${konum[1]}" ACIK="${konum[2]}" KOYU="${konum[3]}"
[[ "$P" =~ ^[a-z0-9]+(-[a-z0-9]+)*$ ]] || { echo "HATA: paket adı kural dışı: $P" >&2; exit 1; }
[[ "$S" =~ ^[0-9]{2}-[a-z0-9]+(-[a-z0-9]+)*$ ]] || { echo "HATA: sahne adı kural dışı: $S" >&2; exit 1; }
[[ "$ACIK" =~ ^[0-9]+(\.[0-9]+)?(,[0-9]+(\.[0-9]+)?)*$ ]] || { echo "HATA: açık zamanlar: $ACIK" >&2; exit 1; }
[[ "$KOYU" =~ ^[0-9]+(\.[0-9]+)?$ ]] || { echo "HATA: koyu zaman: $KOYU" >&2; exit 1; }
[ -d "$K/projeler/$P/sahneler/$S" ] || { echo "HATA: sahne yok: $P/$S" >&2; exit 1; }
O="/home/sef/qa-kare/$P/$S"
mkdir -p "$O/koyu" "$C"

# QA yuvası (sunucu-qa.sh ile aynı 3 yuva: ikisi birlikte de taşmaz).
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
echo "yuva $YUVA · kök $K · önizleme $PORT · cdp $CDP"

# Chrome + ana önizleme (paylaşılan); -o ve 9>&-: uzun ömürlü süreç kilidi devralmasın.
flock -o "$C/qa-baslat.lock" bash "$ANA/araclar/sunucu-onizle.sh" baslat > /dev/null 9>&- \
  || { echo "HATA: ana önizleme/Chrome açılamadı"; exit 4; }
if [ "$PORT" != 41012 ] && ! curl -s -o /dev/null --max-time 3 "http://127.0.0.1:$PORT/"; then
  PIDF="$C/kalem-onizle-$PORT.pid"
  setsid node "$K/ortak/onizle-sunucu.mjs" --port "$PORT" --kok "$K" \
    > "$C/kalem-onizle-$PORT.log" 2>&1 < /dev/null 3>&- 4>&- 5>&- 6>&- 7>&- 8>&- 9>&- &
  echo "onizle $!" > "$PIDF"
  for _ in $(seq 1 15); do curl -s -o /dev/null --max-time 2 "http://127.0.0.1:$PORT/" && break; sleep 1; done
  curl -s -o /dev/null --max-time 3 "http://127.0.0.1:$PORT/" || { echo "HATA: önizleme $PORT açılamadı"; exit 4; }
fi

cd "$K" || exit 4
if [ "$hazirla" = 1 ]; then
  echo "== HAZIRLA"
  (cd "projeler/$P/sahneler/$S" && ONIZLE_YALNIZ=1 timeout 600 bash calistir.sh --tema acik 2>&1 | tail -5)
fi
rc=0
if [ "$kapi" = 1 ]; then
  echo "== KAPI"
  timeout 600 node araclar/cakisma-kapisi.mjs "$P" --sahne "$S" --port "$CDP" --sunucu "$PORT" 2>&1 | tail -25
  rc=${PIPESTATUS[0]}
fi
echo "== KARE (açık)"
timeout 300 node araclar/sahne-kare.mjs "$P" "$S" "$ACIK" "$O" --tema acik --port "$CDP" --sunucu "$PORT" 2>&1 \
  | grep -o '"png":"[^"]*"\|[Hh]ata.*\|HATA.*'
echo "== KARE (koyu)"
timeout 300 node araclar/sahne-kare.mjs "$P" "$S" "$KOYU" "$O/koyu" --tema koyu --port "$CDP" --sunucu "$PORT" 2>&1 \
  | grep -o '"png":"[^"]*"\|[Hh]ata.*\|HATA.*'
mkdir -p "projeler/$P/sahneler/$S/k"
cp -r "$O/." "projeler/$P/sahneler/$S/k/"
echo "kapı çıkış kodu: $rc"
exit "$rc"
