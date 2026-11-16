#!/bin/bash
# zincir2.sh <beklenen-ad> <önek> <paket> [istem-altdizin=sahne] [eşzamanlı=3]
#   <beklenen-ad> "bitti 0" olunca <paket>/uretim-tutanagi/istem/<altdizin>/D-*.md sahne istemlerini kuyruğa verir (model: $KISA_MODEL, yoksa claude-opus-5-5),
#   kuyruk bitince paket çakışma kapısını koşar (CDP 41333, önizleme 41022). Durum: zincir2-<önek>.durum; kapı çıktısı kapi-<paket>.sonuc.
D="$HOME/is/uretim-0204"; K="$HOME/01dev/_worktrees/kalem-0204"
MODEL="${KISA_MODEL:-claude-opus-5-5}"
export PATH="$HOME/.local/bin:$HOME/.nvm/versions/node/v24.22.2/bin:/usr/local/bin:/usr/bin:/bin"
setsid bash -c '
  D="$1"; K="$2"; BEK="$3"; ON="$4"; P="$5"; ALT="$6"; N="$7"; MODEL="$8"
  echo "calisiyor $$" > "$D/zincir2-$ON.durum"
  until case "$(cat "$D/$BEK.durum" 2>/dev/null)" in bitti*) true ;; *) false ;; esac; do sleep 20; done
  if [ "$(cat "$D/$BEK.durum")" != "bitti 0" ]; then echo "bitti 90 ($BEK başarısız)" > "$D/zincir2-$ON.durum"; exit; fi
  I="$K/projeler/$P/uretim-tutanagi/istem/$ALT"
  S=$(cd "$I" 2>/dev/null && ls D-[0-9][0-9]-*.md 2>/dev/null | sed "s/^D-//; s/\.md$//")
  if [ -z "$S" ]; then echo "bitti 91 (sahne istemi yok)" > "$D/zincir2-$ON.durum"; exit; fi
  bash "$D/sahne-kuyruk2.sh" "$ON" "$I" "$N" "$MODEL" $S >> "$D/zincir2-$ON.log" 2>&1
  sleep 30
  until case "$(cat "$D/kuyruk-$ON.durum" 2>/dev/null)" in bitti*) true ;; *) false ;; esac; do sleep 20; done
  ( cd "$K" && timeout 1800 node araclar/cakisma-kapisi.mjs "$P" --port 41333 --sunucu 41022 ) > "$D/kapi-$P.sonuc" 2>&1
  rc=$?; echo "rc=$rc" >> "$D/kapi-$P.sonuc"; echo "bitti $rc" > "$D/zincir2-$ON.durum"
' _ "$D" "$K" "$1" "$2" "$3" "${4:-sahne}" "${5:-3}" "$MODEL" < /dev/null > /dev/null 2>&1 &
echo "zincir2: $1 → kuyruk $2 ($3) → kapı"
