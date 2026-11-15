#!/bin/bash
# Sahne yazarlarını kuyruktan en çok N eşzamanlı koşturur (srv21, sef), paket bağımsız:
#   sahne-kuyruk2.sh <önek> <istem-dizini> <N> <model> <sahne>…
# İş adı <önek>-<sahne> (ör. V-01-hyperframes-giris); istem <istem-dizini>/D-<sahne>.md; durum ~/is/uretim-0204/kuyruk-<önek>.durum.
D="$HOME/is/uretim-0204"
ON="$1"; I="$2"; N="$3"; MODEL="$4"; shift 4
case "$(cat "$D/kuyruk-$ON.durum" 2>/dev/null)" in calisiyor*) echo "kuyruk zaten çalışıyor: $ON"; exit 1 ;; esac
setsid bash -c '
  D="$1"; ON="$2"; I="$3"; N="$4"; MODEL="$5"; shift 5
  say() { n=0; for f in "$D/$ON"-*.durum; do [ -e "$f" ] || continue; case "$(cat "$f")" in calisiyor*) n=$((n+1));; esac; done; echo "$n"; }
  echo "calisiyor $$" > "$D/kuyruk-$ON.durum"
  for s in "$@"; do
    # eşzamanlılık koşarken değişebilir: echo 6 > kuyruk-<önek>.n
    while [ "$(say)" -ge "$(cat "$D/kuyruk-$ON.n" 2>/dev/null || echo "$N")" ]; do sleep 20; done
    bash "$D/kos.sh" "$ON-$s" "$MODEL" "$I/D-$s.md" >> "$D/kuyruk-$ON.log" 2>&1
    sleep 5
  done
  while [ "$(say)" -gt 0 ]; do sleep 20; done
  echo "bitti" > "$D/kuyruk-$ON.durum"
' _ "$D" "$ON" "$I" "$N" "$MODEL" "$@" < /dev/null > /dev/null 2>&1 &
echo "kuyruk başladı: $ON — $# sahne, $N eşzamanlı, $MODEL"
