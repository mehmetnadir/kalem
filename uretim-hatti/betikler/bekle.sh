#!/bin/bash
# bekle.sh <durum-dosyası>… : sunucuda verilen durum dosyalarından biri "bitti" olunca çıkar ve hepsini basar (en çok 90 dk).
for i in $(seq 1 270); do
  s=$(ssh -p 2222 -o BatchMode=yes -o ControlPath=none -o ConnectTimeout=15 root@10.0.0.21 "cd /home/sef/is/uretim-0204 && for f in $*; do echo \"\$f: \$(cat \$f 2>/dev/null)\"; done" < /dev/null 2>/dev/null)
  echo "$s" | grep -q ': bitti' && { echo "$s"; exit 0; }
  sleep 20
done
echo "zaman aşımı"; echo "$s"
