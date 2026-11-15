#!/bin/bash
# ice-al.sh [--kuru] [--buda] — worktree paketlerini kayit paneline içe alır (srv21, sef). Jeton işçi ortam dosyasından.
set -a; . "$HOME/.config/sef/kontrol.env"; set +a
export KONTROL_URL=http://127.0.0.1:3810
DA="$HOME/01dev/dijital-anlatim"; K="$HOME/01dev/_worktrees/kalem-0204"
cd /var/www/videokayit || exit 1   # "@/…" yol takma adı tsconfig'ten çözülür; betik çalışma dizinine yazmaz
timeout 600 node_modules/.bin/tsx scripts/kontrol-ice-al.ts \
  --katalog "$DA/varlik/grammar/katalog.json" --durum "$DA/varlik/grammar/katalog-durum.json" --paketler "$K/projeler" "$@"
