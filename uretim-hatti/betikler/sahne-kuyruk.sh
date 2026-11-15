#!/bin/bash
# Sahne yazarlarını kuyruktan en çok N eşzamanlı koşturur (srv21, sef): sahne-kuyruk.sh <N> <model> <sahne>…
D="$HOME/is/uretim-0204"; I="$HOME/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel/uretim-tutanagi/istem/sahne"
N="$1"; MODEL="$2"; shift 2
setsid bash -c '
  D="$1"; I="$2"; N="$3"; MODEL="$4"; shift 4
  echo "calisiyor $$" > "$D/kuyruk.durum"
  for s in "$@"; do
    while :; do
      n=0; for f in "$D"/D-*.durum; do [ -e "$f" ] || continue; case "$(cat "$f")" in calisiyor*) n=$((n+1));; esac; done
      [ "$n" -lt "$N" ] && break; sleep 20
    done
    bash "$D/kos.sh" "D-$s" "$MODEL" "$I/D-$s.md" >> "$D/kuyruk.log" 2>&1
    sleep 5
  done
  while :; do
    n=0; for f in "$D"/D-*.durum; do case "$(cat "$f")" in calisiyor*) n=$((n+1));; esac; done
    [ "$n" -eq 0 ] && break; sleep 20
  done
  echo "bitti" > "$D/kuyruk.durum"
' _ "$D" "$I" "$N" "$MODEL" "$@" < /dev/null > /dev/null 2>&1 &
echo "kuyruk başladı: $# sahne, $N eşzamanlı, $MODEL"
