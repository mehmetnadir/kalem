export PATH=$HOME/.nvm/versions/node/v24.22.2/bin:$HOME/.local/bin:$PATH
echo "== host"; uname -srm; nproc; free -g | sed -n 2p; df -h /home | tail -1; cat /proc/loadavg
echo "== araclar"
for c in node npm ffmpeg ffprobe claude uv git rsync perl google-chrome; do printf '%s: ' $c; (command -v $c && $c --version 2>&1 | head -1) | tr '\n' ' '; echo; done
echo "== python"
/usr/bin/python3 --version
for m in numpy soundfile pyloudnorm faster_whisper PIL pytest av ctranslate2 requests; do /usr/bin/python3 -I -c "import $m; print('$m OK', getattr($m,'__version__',''))" 2>&1 | tail -1; done
echo "== env/anahtar"
env | grep -E '^(ELEVEN|KONTROL|CHROME|ASR)' | sed 's/=.*/=<var>/'
ls ~/.config 2>/dev/null | head; ls ~/.cache | head -20
echo "== whisper model"
ls ~/.cache/huggingface/hub 2>/dev/null | head; ls /home/sef/models /opt/models 2>/dev/null | head
echo "== depolar"
for d in kalem dijital-anlatim conductor; do echo "-- $d"; git -C /home/sef/01dev/$d log -1 --format='%h %ad %s' --date=iso | cut -c1-120; git -C /home/sef/01dev/$d status --short | head -3; done
echo "== kalem node_modules"
K=/home/sef/01dev/kalem
for d in motorlar/paperjs motorlar/hyperframes motorlar/pixijs motorlar/threejs motorlar/yardimci ses; do printf '%s: ' $d; ls $K/$d/node_modules 2>/dev/null | wc -l; done
ls $K/motorlar/hyperframes/node_modules/.bin 2>/dev/null | grep -c hyperframes
$K/motorlar/hyperframes/node_modules/.bin/hyperframes --version 2>&1 | head -2
ls $K/motorlar/hyperframes/node_modules/gsap/dist/gsap.min.js $K/ortak/paper-core.js 2>&1
echo "== kalem projeler"
ls $K/projeler | head -80 | tr '\n' ' '; echo
ls $K/projeler/02-03-ydt-temel $K/projeler/02-03-ydt-temel/ortak $K/projeler/02-03-ydt-temel/ortak/anlatim 2>&1 | head -50
ls -la $K/projeler/02-03-ydt-temel/ortak/ | head -20
ls $K/projeler/02-04-ydt-temel 2>&1 | head -3
ls $K/projeler/present-continuous/ortak 2>&1 | head -30
ls $K/projeler/present-continuous/ortak/cizim 2>&1 | head -5
echo "== font"
ls $K/projeler/present-continuous/ortak/font 2>&1 | head -5
fc-list 2>/dev/null | grep -ciE 'lexend|fredoka|caveat'
echo "== chrome"
ls -la /usr/bin/google-chrome* 2>&1 | head -3
echo "== dijital-anlatim"
D=/home/sef/01dev/dijital-anlatim
ls $D/araclar | head -40 | tr '\n' ' '; echo
ls $D/araclar/iki-dilli | tr '\n' ' '; echo
ls $D/varlik/grammar | tr '\n' ' '; echo
ls $D/varlik/grammar/transkript-whisper/863572960* $D/varlik/grammar/transkript-whisper/863572892* 2>&1
ls "$D/varlik/grammar/kaynak-pptx" 2>&1 | head -3
ls $D/.claude/docs 2>&1 | head -5
echo "== sabit yol taramasi (sunucu kopyasında)"
grep -rIl '/Users/nadir' $K/araclar $K/ortak $K/birlestir.py $K/projeler/02-03-ydt-temel/ortak $K/projeler/02-03-ydt-temel/sahneler --include='*.py' --include='*.sh' --include='*.mjs' --include='*.js' 2>/dev/null | head -20
echo "== claude"
ls ~/.claude 2>&1 | head; ls ~/.claude/skills 2>&1 | head; ls ~/.claude/.credentials.json 2>&1
ls /home/sef/01dev/conductor/claude/skills 2>&1 | grep -E 'motion|gorev'
echo "== kuyruk / kilit araclari"
for c in flock runuser setsid timeout; do printf '%s: ' $c; command -v $c; done
