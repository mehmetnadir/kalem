#!/bin/bash
# Render öncesi canlı önizleme sunucusu: onizle.sh <proje> [port]  (proje örn. projeler/present-continuous)
# Paket kökünden statik sunucu açar; ön planda çalışır, Ctrl-C ile kapanır. Port 3000 yasak, varsayılan 3012.
set -eo pipefail
K="$(cd "$(dirname "$0")/.." && pwd)"
P="${1:?kullanım: ortak/onizle.sh <proje> [port]}"; PORT="${2:-3012}"
[ "$PORT" = "3000" ] && { echo "port 3000 yasak"; exit 1; }
[ -f "$K/$P/onizle.html" ] || { echo "$P/onizle.html yok"; exit 1; }
if lsof -i ":$PORT" >/dev/null 2>&1; then echo "port $PORT dolu (lsof -i :$PORT); başka port ver"; exit 1; fi
echo "Önizleme: http://127.0.0.1:$PORT/$P/onizle.html   (Ctrl-C ile kapat)"
cd "$K" && exec /usr/bin/python3 -m http.server "$PORT" --bind 127.0.0.1
