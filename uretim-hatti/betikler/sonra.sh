#!/bin/bash
# sonra.sh <beklenen-ad> <iş-adı>…  — <beklenen-ad>.durum "bitti 0" olunca her <iş-adı> için kos.sh <iş-adı> $KISA_MODEL <iş-adı>.md başlatır (KISA_MODEL yoksa claude-opus-5-5).
# Beklenen iş hatayla biterse hiçbir şey başlatmaz; başlamayacak her işin <iş-adı>.durum dosyasına "bitti 90" yazar (zincir takılı kalmasın). Durum: ~/is/uretim-0204/sonra-<beklenen-ad>.durum (calisiyor | bitti <rc>). Ayrık oturumda koşar.
D="$HOME/is/uretim-0204"; BEK="$1"; shift; MODEL="${KISA_MODEL:-claude-opus-5-5}"
setsid bash -c '
  D="$1"; BEK="$2"; MODEL="$3"; shift 3
  echo "calisiyor $$" > "$D/sonra-$BEK.durum"
  until case "$(cat "$D/$BEK.durum" 2>/dev/null)" in bitti*) true ;; *) false ;; esac; do sleep 20; done
  if [ "$(cat "$D/$BEK.durum")" != "bitti 0" ]; then
    echo "bitti 90" > "$D/sonra-$BEK.durum"
    # zincirin sonraki halkaları sonsuz beklemesin: başlamayacak işlere "bitti 90" yaz
    for a in "$@"; do case "$(cat "$D/$a.durum" 2>/dev/null)" in calisiyor*|bitti*) ;; *) echo "bitti 90" > "$D/$a.durum" ;; esac; done
    exit
  fi
  for a in "$@"; do bash "$D/kos.sh" "$a" "$MODEL" "$D/$a.md" >> "$D/sonra-$BEK.log" 2>&1; done
  echo "bitti 0" > "$D/sonra-$BEK.durum"
' _ "$D" "$BEK" "$MODEL" "$@" < /dev/null > /dev/null 2>&1 &
echo "sonra: $BEK → $*"
