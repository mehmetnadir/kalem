#!/bin/bash
# 02-04-ydt-temel ses zinciri (srv21, sef): el.py (vekil) → sözcük → zaman → kur → m4a → altyazı → METIN.
# Ayrık koşar; günlük ~/is/uretim-0204/ses.log, durum ~/is/uretim-0204/ses.durum ("calisiyor <pid>" → "bitti <rc>").
D="$HOME/is/uretim-0204"; K="$HOME/01dev/_worktrees/kalem-0204"; P=02-04-ydt-temel; A="$K/projeler/$P/ortak/anlatim"
mkdir -p "$D"
case "$(cat "$D/ses.durum" 2>/dev/null)" in calisiyor*) echo "zaten çalışıyor"; exit 1 ;; esac
setsid bash -c "
  set -o pipefail
  echo \"calisiyor \$\$\" > '$D/ses.durum'
  export PATH=\"$HOME/.nvm/versions/node/v24.22.2/bin:/usr/local/bin:/usr/bin:/bin\"
  adim() { echo \"== \$(date +%T) \$*\"; }
  ( set -e
    adim el.py; bash '$K/araclar/ses-sunucu.sh' --kok '$K' $P
    adim sozcuk_uret; /usr/bin/python3 -I '$A/sozcuk_uret.py'
    adim zaman_uret; /usr/bin/python3 -I '$A/zaman_uret.py'
    adim kur; /usr/bin/python3 -I '$A/kur.py'
    adim ses-paketle; /usr/bin/python3 '$K/araclar/ses-paketle.py' --yaz --paket $P --kok '$K'
    adim altyazi; cd '$K' && /usr/bin/python3 -I araclar/altyazi_uret.py projeler/$P
    adim metin; /usr/bin/python3 -I '$A/metin_uret.py'
    adim TAMAM
  ) > '$D/ses.log' 2>&1
  echo \"bitti \$?\" > '$D/ses.durum'
" < /dev/null > /dev/null 2>&1 &
echo "ses zinciri başladı"
