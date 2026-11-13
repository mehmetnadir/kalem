#!/bin/bash
# Sunucu önizleme başlatıcı (yalnız Linux/sef): önizleme sunucusu + başsız Chrome.
#   bash araclar/sunucu-onizle.sh [baslat|durdur|durum]
# Ortam: ONIZLE_PORT (varsayılan 41012), CDP_PORT (varsayılan 41333). Portlar 32768–60999 aralığında kalmalı
# (sef loopback çıkış kuralı). PID dosyası: ~/.cache/kalem-onizle.pid
set -u
if [ "$(uname -s)" != "Linux" ] || [ "$(id -un)" != "sef" ]; then
  echo "yalnız Linux/sef: bu betik sunucuda sef kullanıcısı ile koşar" >&2; exit 1
fi
export PATH="/home/sef/.nvm/versions/node/v24.22.2/bin:$PATH"
KOK="$(cd "$(dirname "$0")/.." && pwd)"
ONIZLE_PORT="${ONIZLE_PORT:-41012}"
CDP_PORT="${CDP_PORT:-41333}"
PIDF="/home/sef/.cache/kalem-onizle.pid"
LOGD="/home/sef/.cache"
mkdir -p "$LOGD"

saglik() {
  local ok=0
  # statik sunucu: kökte 404 normal; yanıt gelmesi (000 değil) yeter
  local kod
  kod="$(curl -s -o /dev/null -w '%{http_code}' --max-time 5 "http://127.0.0.1:$ONIZLE_PORT/")"
  [ "$kod" != "000" ] && echo "onizle:$ONIZLE_PORT TAMAM ($kod)" || { echo "onizle:$ONIZLE_PORT YOK"; ok=1; }
  curl -fsS -o /dev/null --max-time 5 "http://127.0.0.1:$CDP_PORT/json/version" \
    && echo "chrome-cdp:$CDP_PORT TAMAM" || { echo "chrome-cdp:$CDP_PORT YOK"; ok=1; }
  return $ok
}

# yalnız PID dosyasındaki süreç grupları (setsid ile başlatıldı: pid = grup kimliği)
durdur() {
  [ -f "$PIDF" ] || { echo "pid dosyası yok"; return 0; }
  while read -r ad pid; do
    [ -n "${pid:-}" ] || continue
    if kill -0 "$pid" 2>/dev/null; then
      kill -- "-$pid" 2>/dev/null || kill "$pid" 2>/dev/null
      echo "durdu: $ad $pid"
    fi
  done < "$PIDF"
  sleep 1
  while read -r ad pid; do
    [ -n "${pid:-}" ] && kill -0 "$pid" 2>/dev/null \
      && { kill -9 -- "-$pid" 2>/dev/null || kill -9 "$pid" 2>/dev/null; }
  done < "$PIDF"
  mkdir -p /home/sef/Silinecekler
  mv "$PIDF" "/home/sef/Silinecekler/kalem-onizle.pid.$(date +%s)"
}

baslat() {
  if [ -f "$PIDF" ] && saglik >/dev/null 2>&1; then echo "zaten açık"; saglik; return 0; fi
  [ -f "$PIDF" ] && durdur
  for p in "$ONIZLE_PORT" "$CDP_PORT"; do
    if (echo > "/dev/tcp/127.0.0.1/$p") 2>/dev/null; then echo "HATA port dolu: $p" >&2; return 1; fi
  done
  # Çağıranın açık dosya tanıtıcıları (flock kilitleri, 3–9) uzun ömürlü süreçlere geçmesin (13.11).
  setsid node "$KOK/ortak/onizle-sunucu.mjs" --port "$ONIZLE_PORT" --kok "$KOK" \
    > "$LOGD/kalem-onizle.log" 2>&1 < /dev/null 3>&- 4>&- 5>&- 6>&- 7>&- 8>&- 9>&- &
  echo "onizle $!" > "$PIDF"
  setsid google-chrome --headless=new --no-sandbox --disable-gpu \
    --remote-debugging-address=127.0.0.1 --remote-debugging-port="$CDP_PORT" \
    --user-data-dir=/home/sef/.cache/kalem-chrome about:blank \
    > "$LOGD/kalem-chrome.log" 2>&1 < /dev/null 3>&- 4>&- 5>&- 6>&- 7>&- 8>&- 9>&- &
  echo "chrome $!" >> "$PIDF"
  for _ in $(seq 1 20); do saglik >/dev/null 2>&1 && break; sleep 1; done
  saglik
}

case "${1:-baslat}" in
  baslat) baslat ;;
  durdur) durdur ;;
  durum) saglik ;;
  *) echo "kullanım: $0 [baslat|durdur|durum]" >&2; exit 2 ;;
esac
