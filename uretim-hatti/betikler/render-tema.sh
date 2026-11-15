#!/bin/bash
# Paket mp4 render (srv21, sef; Nadir 14–15.11 açık mp4 isteği ve "hepsini istiyorum"): sahne render (4 eşzamanlı) -> birlestir.py.
#   TEMA=acik|koyu PAKET=<paket> render-tema.sh            bütün sahneler + birleştirme
#   TEMA=… PAKET=… render-tema.sh <sahne>…                yalnız verilen sahneler (BIRLES=1 ile birleştirme de)
# ES=<n> sahne eşzamanlılığı (varsayılan 4). Varsayılan: TEMA=acik, PAKET=02-04-ydt-temel, KOK=~/01dev/_worktrees/kalem-0204.
# Günlük ~/is/uretim-0204/render/<paket>-<tema>/<sahne>.log + _ana.log; durum ~/is/uretim-0204/render-<paket>-<tema>.durum.
TEMA="${TEMA:-acik}"; P="${PAKET:-02-04-ydt-temel}"; K="${KOK:-$HOME/01dev/_worktrees/kalem-0204}"
D="$HOME/is/uretim-0204"; R="$D/render/$P-$TEMA"; DURUM="$D/render-$P-$TEMA.durum"
mkdir -p "$R"
case "$(cat "$DURUM" 2>/dev/null)" in calisiyor*) echo "zaten çalışıyor: $P $TEMA"; exit 1 ;; esac
export PATH="$HOME/.nvm/versions/node/v24.22.2/bin:/usr/local/bin:/usr/bin:/bin" K P R TEMA
sahne() { s="$1"; ( cd "$K/projeler/$P/sahneler/$s" && bash calistir.sh --tema "$TEMA" ) > "$R/$s.log" 2>&1 \
  && echo "tamam $s" || { echo "HATA $s (bkz. $R/$s.log)"; return 1; }; }
export -f sahne
if [ $# -gt 0 ]; then LISTE=("$@"); BIRLESTIR="${BIRLES:-0}"; else
  LISTE=($(cd "$K/projeler/$P/sahneler" && ls -d [0-9][0-9]-*)); BIRLESTIR=1; fi
setsid bash -c "
  echo \"calisiyor \$\$\" > '$DURUM'
  {
    date +%T; printf '%s\n' ${LISTE[*]} | xargs -P ${ES:-4} -I{} bash -c 'sahne \"\$@\"' _ {}; rc=\$?
    if [ \$rc -eq 0 ] && [ $BIRLESTIR -eq 1 ]; then
      cd '$K' && /usr/bin/python3 birlestir.py projeler/$P --tema $TEMA --gecis BookFlip --efekt hisirti; rc=\$?
    fi
    if [ \$rc -eq 0 ] && [ $BIRLESTIR -eq 1 ]; then
      # panel kapağı + önizleme (15.11): betik önbelleği çalışma dizinine yazar, /var/www sef'e kapalı
      set -a; . \$HOME/.config/sef/kontrol.env; set +a; export KONTROL_URL=http://127.0.0.1:3810
      mkdir -p \$HOME/is/onizleme && cd \$HOME/is/onizleme && timeout 600 /var/www/videokayit/node_modules/.bin/tsx \
        /var/www/videokayit/scripts/kontrol-onizleme.ts '$K/projeler' --paketler $P | tail -4 || echo 'UYARI: önizleme yüklenemedi'
    fi
    date +%T; echo \"rc=\$rc\"
  } > '$R/_ana.log' 2>&1
  echo \"bitti \$rc\" > '$DURUM'
" < /dev/null > /dev/null 2>&1 &
echo "render başladı: $P $TEMA — ${LISTE[*]}"
