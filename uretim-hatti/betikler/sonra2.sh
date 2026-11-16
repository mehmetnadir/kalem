#!/bin/bash
# sonra2.sh <beklenen-1> <beklenen-2> <iş-adı>  — iki iş de "bitti 0" olunca kos.sh <iş-adı> $KISA_MODEL <iş-adı>.md başlatır (KISA_MODEL yoksa claude-opus-5-5).
# Biri hatayla biterse başlatmaz; <iş-adı>.durum dosyasına "bitti 90" yazar (zincir takılı kalmasın). Durum: ~/is/uretim-0204/sonra2-<iş-adı>.durum. Ayrık oturumda koşar.
D="$HOME/is/uretim-0204"; MODEL="${KISA_MODEL:-claude-opus-5-5}"
setsid bash -c '
  D="$1"; A="$2"; B="$3"; IS="$4"; MODEL="$5"
  echo "calisiyor $$" > "$D/sonra2-$IS.durum"
  bitti() { case "$(cat "$D/$1.durum" 2>/dev/null)" in bitti*) return 0 ;; *) return 1 ;; esac; }
  until bitti "$A" && bitti "$B"; do sleep 20; done
  if [ "$(cat "$D/$A.durum")" != "bitti 0" ] || [ "$(cat "$D/$B.durum")" != "bitti 0" ]; then
    echo "bitti 90" > "$D/sonra2-$IS.durum"
    # zincirin sonraki halkaları sonsuz beklemesin
    case "$(cat "$D/$IS.durum" 2>/dev/null)" in calisiyor*|bitti*) ;; *) echo "bitti 90" > "$D/$IS.durum" ;; esac
    exit
  fi
  bash "$D/kos.sh" "$IS" "$MODEL" "$D/$IS.md" >> "$D/sonra2-$IS.log" 2>&1
  echo "bitti 0" > "$D/sonra2-$IS.durum"
' _ "$D" "$1" "$2" "$3" "$MODEL" < /dev/null > /dev/null 2>&1 &
echo "sonra2: $1 + $2 → $3"
