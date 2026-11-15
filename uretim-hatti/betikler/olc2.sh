export PATH=$HOME/.nvm/versions/node/v24.22.2/bin:$HOME/.local/bin:$PATH
K=/home/sef/01dev/kalem
echo "== paperjs"; ls $K/motorlar/paperjs/node_modules; ls $K/motorlar/paperjs/node_modules/paper/dist 2>&1 | head -4
echo "== yardimci/ses nm"; ls $K/motorlar/yardimci/node_modules | head; ls $K/ses/node_modules | head -30 | tr '\n' ' '; echo
echo "== tone"; ls $K/ses/node_modules/tone/build 2>&1 | head -2
echo "== hyperframes chrome"; ls ~/.cache/hyperframes ~/.cache/puppeteer 2>&1 | head; ls ~/.cache/hyperframes/chrome 2>&1 | head
echo "== kalem ortak"; ls $K/ortak $K/ortak/editor | head -30 | tr '\n' ' '; echo
echo "== arac sunucu"; ls $K/araclar | tr '\n' ' '; echo
echo "== birlestir"; ls $K/birlestir.py $K/ses/render.mjs 2>&1
echo "== gl-transitions"; ls $K/ortak/gecis-ozel 2>&1 | head -3; grep -c . $K/ortak/gecis-tr.js 2>&1
echo "== 02-03 sahne ornek"; ls $K/projeler/02-03-ydt-temel/sahneler/01-hyperframes-giris $K/projeler/02-03-ydt-temel/sahneler/02-paperjs-kanca
echo "== 02-03 sunucuda uretilmis mi"; ls $K/projeler/02-03-ydt-temel/sahneler/04-canvas-ornek2/ 2>&1 | tr '\n' ' '; echo
ls -d /home/sef/qa-kare/* 2>&1 | head -5; ls /home/sef/qa-kare/02-02-ydt-temel 2>&1 | head -5
echo "== kayit uygulamasi (vekil)"; ls /home/sef 2>&1 | head -30 | tr '\n' ' '; echo
(ss -ltn 2>/dev/null | awk '{print $4}' | grep -E ':(3810|3816|3015|3016|41012|41333)$')
echo "== Claude Code auth"; ls ~/.claude/.credentials.json -la; ls ~/.claude/settings.json 2>&1; ls ~/.claude/projects 2>&1 | head -3
echo "== sozcuk: whisper alternatifleri"; command -v whisper whisper-cpp main whisper-cli 2>&1 | head; ls /usr/local/bin | head -20 | tr '\n' ' '; echo
ls ~/.venv* ~/venv ~/.local/share/uv 2>&1 | head -5
/usr/bin/python3 -m pip --version 2>&1 | head -1
/usr/bin/python3 -m venv --help >/dev/null 2>&1 && echo venv-ok
echo "== font kurulu mu (fc-list)"; fc-list 2>&1 | wc -l
echo "== dijital-anlatim node_modules/hyperframes"; ls /home/sef/01dev/dijital-anlatim/node_modules 2>&1 | head -3
echo "== kontrol"; ls $K/projeler/02-03-ydt-temel/uretim-tutanagi
echo "== kalem testler"; ls $K/testler | head -20 | tr '\n' ' '; echo
echo "== test-tutanak / agir / TT"; command -v test-tutanak agir.sh yuk-dengeleyici agy-filo kovan 2>&1 | head
echo "== dijital-anlatim araclar sema"; ls /home/sef/01dev/dijital-anlatim/araclar/sema | tr '\n' ' '; echo
