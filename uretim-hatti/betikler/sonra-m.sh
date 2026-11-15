#!/bin/bash
# sonra-m.sh <beklenen-ad> <model> <istem-dizini> <iş-adı>…
# <beklenen-ad>.durum "bitti 0" olunca her <iş-adı> için kos.sh <iş-adı> <model> <istem-dizini>/<iş-adı>.md başlatır.
# sonra.sh'tan farkı: model ve istem dizini seçilir (jüri oturumu üreticiden FARKLI modelle koşar; juri-olcutleri.md §1e).
# Beklenen iş hatayla biterse hiçbir şey başlatmaz. Durum: ~/is/uretim-0204/sonra-<beklenen-ad>.durum. Ayrık oturumda koşar.
D="$HOME/is/uretim-0204"; BEK="$1"; MODEL="$2"; ISTEMLER="$3"; shift 3
setsid bash -c '
  D="$1"; BEK="$2"; MODEL="$3"; ISTEMLER="$4"; shift 4
  echo "calisiyor $$" > "$D/sonra-$BEK.durum"
  until case "$(cat "$D/$BEK.durum" 2>/dev/null)" in bitti*) true ;; *) false ;; esac; do sleep 20; done
  if [ "$(cat "$D/$BEK.durum")" != "bitti 0" ]; then echo "bitti 90" > "$D/sonra-$BEK.durum"; exit; fi
  for a in "$@"; do bash "$D/kos.sh" "$a" "$MODEL" "$ISTEMLER/$a.md" >> "$D/sonra-$BEK.log" 2>&1; done
  echo "bitti 0" > "$D/sonra-$BEK.durum"
' _ "$D" "$BEK" "$MODEL" "$ISTEMLER" "$@" < /dev/null > /dev/null 2>&1 &
echo "sonra-m: $BEK → $* ($MODEL)"
