#!/bin/bash
# sonra.sh <beklenen-ad> <iş-adı>…  — <beklenen-ad>.durum "bitti 0" olunca her <iş-adı> için kos.sh <iş-adı> claude-opus-5-5 <iş-adı>.md başlatır.
# Beklenen iş hatayla biterse hiçbir şey başlatmaz. Durum: ~/is/uretim-0204/sonra-<beklenen-ad>.durum (calisiyor | bitti <rc>). Ayrık oturumda koşar.
D="$HOME/is/uretim-0204"; BEK="$1"; shift
setsid bash -c '
  D="$1"; BEK="$2"; shift 2
  echo "calisiyor $$" > "$D/sonra-$BEK.durum"
  until case "$(cat "$D/$BEK.durum" 2>/dev/null)" in bitti*) true ;; *) false ;; esac; do sleep 20; done
  if [ "$(cat "$D/$BEK.durum")" != "bitti 0" ]; then echo "bitti 90" > "$D/sonra-$BEK.durum"; exit; fi
  for a in "$@"; do bash "$D/kos.sh" "$a" claude-opus-5-5 "$D/$a.md" >> "$D/sonra-$BEK.log" 2>&1; done
  echo "bitti 0" > "$D/sonra-$BEK.durum"
' _ "$D" "$BEK" "$@" < /dev/null > /dev/null 2>&1 &
echo "sonra: $BEK → $*"
