ls -la /opt/etk-whisper | head; ls /opt/etk-whisper/modeller/models--Systran--faster-whisper-small/snapshots/* 2>&1 | head -8
for p in /opt/etk-whisper/venv/bin/python /opt/etk-whisper/.venv/bin/python; do [ -x $p ] && { echo $p; $p -c "import faster_whisper,soundfile,numpy;print('fw',faster_whisper.__version__)" 2>&1 | tail -1; $p -c "import pyloudnorm" 2>&1 | tail -1; $p -c "import soundfile" 2>&1|tail -1; }; done
diff <(sed -n 1,200p /home/sef/.claude/skills/motion-grafik-ders/SKILL.md) /dev/null | wc -l
grep -c 'D-0204' /home/sef/.claude/skills/motion-grafik-ders/SKILL.md
ls -la /home/sef/.claude/skills/motion-grafik-ders/references | head -12
