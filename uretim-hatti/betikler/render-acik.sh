#!/bin/bash
# 02-04-ydt-temel açık tema mp4 (srv21, sef; Nadir 14.11 açık mp4 isteği): sahne render (4 eşzamanlı) -> birlestir.py.
#   render-acik.sh            bütün sahneler + birleştirme
#   render-acik.sh <sahne>…   yalnız verilen sahneler, birleştirme yok (BIRLES=1 ile var: önceden render edilmişler yeniden koşmaz)
# Günlük ~/is/uretim-0204/render/<sahne>.log, durum ~/is/uretim-0204/render.durum ("calisiyor <pid>" -> "bitti <rc>").
D="$HOME/is/uretim-0204"; K="$HOME/01dev/_worktrees/kalem-0204"; P=02-04-ydt-temel; R="$D/render"
mkdir -p "$R"
case "$(cat "$D/render.durum" 2>/dev/null)" in calisiyor*) echo "zaten çalışıyor"; exit 1 ;; esac
export PATH="$HOME/.nvm/versions/node/v24.22.2/bin:/usr/local/bin:/usr/bin:/bin" K P R
sahne() { s="$1"; ( cd "$K/projeler/$P/sahneler/$s" && bash calistir.sh --tema acik ) > "$R/$s.log" 2>&1 \
  && echo "tamam $s" || { echo "HATA $s (bkz. $R/$s.log)"; return 1; }; }
export -f sahne
if [ $# -gt 0 ]; then LISTE=("$@"); BIRLESTIR="${BIRLES:-0}"; else
  LISTE=($(cd "$K/projeler/$P/sahneler" && ls -d [0-9][0-9]-*)); BIRLESTIR=1; fi
setsid bash -c "
  echo \"calisiyor \$\$\" > '$D/render.durum'
  {
    date +%T; printf '%s\n' ${LISTE[*]} | xargs -P 4 -I{} bash -c 'sahne \"\$@\"' _ {}; rc=\$?
    if [ \$rc -eq 0 ] && [ $BIRLESTIR -eq 1 ]; then
      cd '$K' && /usr/bin/python3 birlestir.py projeler/$P --tema acik --gecis BookFlip --efekt hisirti; rc=\$?
    fi
    date +%T; echo \"rc=\$rc\"
  } > '$R/_ana.log' 2>&1
  echo \"bitti \$rc\" > '$D/render.durum'
" < /dev/null > /dev/null 2>&1 &
echo "render başladı: ${LISTE[*]}"
