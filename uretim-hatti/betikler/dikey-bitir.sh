#!/bin/bash
# dikey-bitir.sh (srv21, sef): izlenen yatay dosyaları geri al → dikey + s1 commit → ön tutanak → sahne 02 render + birleştirme (açık, koyu).
set -u
K="$HOME/01dev/_worktrees/kalem-0204"; D="$HOME/is/uretim-0204"; P=02-04-ydt-temel-dikey
cd "$K" || exit 1
for f in $(git status --short | awk '$1=="M"{print $2}'); do git show "HEAD:$f" > "$f" && echo "geri alındı: $f"; done
git add projeler/02-04-ydt-temel-dikey projeler/02-04-ydt-temel-s1
git commit -q -F "$D/commit-dikey.txt" && git log --oneline -1
/usr/bin/python3 -I "$HOME/01dev/dijital-anlatim/araclar/sema/tutanak_on.py" uret "projeler/$P" --yaz 2>&1 | tail -2
for T in acik koyu; do
  BIRLES=1 ES=4 TEMA=$T PAKET=$P bash "$D/render-tema.sh" 02-paperjs-kanca | cut -c1-70
  sleep 5
  until case "$(cat "$D/render-$P-$T.durum")" in bitti*) true ;; *) false ;; esac; do sleep 10; done
  echo "$T: $(cat "$D/render-$P-$T.durum")"; tail -6 "$D/render/$P-$T/_ana.log"
done
ls -la --time-style=+%H:%M "projeler/$P"/cikti*.mp4 | cut -c24-
git status --short | grep -v '^??' | head
