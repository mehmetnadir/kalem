#!/bin/bash
# zincir.sh — "biten yerine yenisi" (srv21, sef; Nadir 15.11). Şef beklemeden sıradaki işi başlatır; ayrık oturumda koşar.
#   zincir.sh kisa <N> <önek>        S<N>-C "bitti 0" olunca 02-04-ydt-temel-s<N> sahne istemlerini kuyruğa verir
#                                    (8 eşzamanlı, opus), kuyruk bitince paket çakışma kapısını koşar
#   zincir.sh kapi <durum-adı> <paket> [port] [sunucu]   <durum-adı>.durum "bitti…" olunca paket çakışma kapısını koşar
# Kapı kapıları var olan ortak tarayıcıya (CDP 41333) ve önizleme sunucusuna (41022) bağlanır; başka port ECONNREFUSED.
# Durum ~/is/uretim-0204/zincir-<ad>.durum (calisiyor | bitti <rc>); kapı çıktısı kapi-<paket>.sonuc (son satır "rc=<n>").
D="$HOME/is/uretim-0204"; K="$HOME/01dev/_worktrees/kalem-0204"
export PATH="$HOME/.local/bin:$HOME/.nvm/versions/node/v24.22.2/bin:/usr/local/bin:/usr/bin:/bin"
KIP="$1"; shift
bekle() { until case "$(cat "$D/$1.durum" 2>/dev/null)" in bitti*) true ;; *) false ;; esac; do sleep 20; done; }
kapi() { # <paket> <port> <sunucu>
  ( cd "$K" && timeout 1800 node araclar/cakisma-kapisi.mjs "$1" --port "$2" --sunucu "$3" ) > "$D/kapi-$1.sonuc" 2>&1
  rc=$?; echo "rc=$rc" >> "$D/kapi-$1.sonuc"; return $rc
}
export -f bekle kapi; export D K
case "$KIP" in
  kisa)
    N="$1"; ON="$2"; AD="kisa-s$N"; P="02-04-ydt-temel-s$N"
    setsid bash -c '
      N="$1"; ON="$2"; AD="$3"; P="$4"
      echo "calisiyor $$" > "$D/zincir-$AD.durum"
      bekle "S$N-C"
      if [ "$(cat "$D/S$N-C.durum")" != "bitti 0" ]; then echo "bitti 90 (S$N-C başarısız)" > "$D/zincir-$AD.durum"; exit; fi
      I="$K/projeler/$P/uretim-tutanagi/istem/sahne"
      S=$(cd "$I" && ls D-[0-9][0-9]-*.md 2>/dev/null | sed "s/^D-//; s/\.md$//")
      if [ -z "$S" ]; then echo "bitti 91 (sahne istemi yok)" > "$D/zincir-$AD.durum"; exit; fi
      bash "$D/sahne-kuyruk2.sh" "$ON" "$I" 8 claude-opus-5-5 $S >> "$D/zincir-$AD.log" 2>&1
      sleep 30; bekle "kuyruk-$ON"
      kapi "$P" 41333 41022; echo "bitti $?" > "$D/zincir-$AD.durum"
    ' _ "$N" "$ON" "$AD" "$P" < /dev/null > /dev/null 2>&1 &
    echo "zincir başladı: $AD (S$N-C → kuyruk $ON → kapı)" ;;
  kapi)
    BEK="$1"; P="$2"; PORT="${3:-41333}"; SUN="${4:-41022}"; AD="kapi-$P"
    setsid bash -c '
      echo "calisiyor $$" > "$D/zincir-$3.durum"
      bekle "$1"; kapi "$2" "$4" "$5"; echo "bitti $?" > "$D/zincir-$3.durum"
    ' _ "$BEK" "$P" "$AD" "$PORT" "$SUN" < /dev/null > /dev/null 2>&1 &
    echo "zincir başladı: $AD ($BEK → kapı)" ;;
  *) echo "kip: kisa | kapi"; exit 1 ;;
esac
