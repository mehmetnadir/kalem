echo "== vekil rotasi (kayit)"
ls /var/www/videokayit 2>&1 | head -3
grep -rIl -i 'ELEVEN_VEKIL\|elevenlabs' /var/www/videokayit/scripts /var/www/videokayit/src 2>/dev/null | head -8
echo "== env (anahtar adlari, deger yok)"
systemctl --user list-units 2>/dev/null | grep -i -E 'kontrol|kayit' | head -3
ls /home/sef/.config 2>/dev/null | head
echo "== HF cache / whisper"
find /home/sef /root /opt /usr/local/share -maxdepth 4 \( -iname '*whisper*' -o -iname 'models--*' \) 2>/dev/null | head -8
echo "== disk (modeller ~1.5GB)"; df -h /home | tail -1
echo "== dijital-anlatim docs"
ls /home/sef/01dev/dijital-anlatim/.claude/docs | grep -E 'sozlesme|grammar-defter'
echo "== sunucu 02-03 tema.sh vs Mac"
md5sum /home/sef/01dev/kalem/projeler/02-03-ydt-temel/ortak/tema.sh /home/sef/01dev/kalem/projeler/02-03-ydt-temel/ortak/anlatim/senaryo.json
echo "== claude oturum: skill + istek"
ls /home/sef/.claude/skills | grep -E 'motion-grafik|gorev-haritasi'; ls /home/sef/.claude/skills/motion-grafik-ders 2>&1 | head
md5sum /home/sef/.claude/skills/motion-grafik-ders/SKILL.md 2>&1
echo "== kalem git origin/izlenen"
git -C /home/sef/01dev/kalem ls-files projeler/02-03-ydt-temel | wc -l
git -C /home/sef/01dev/kalem ls-files _is | wc -l
echo "== uv/pip kurulabilirlik (yalniz bakis)"
/usr/bin/python3 -m pip config list 2>&1 | head -3
ls /home/sef/.local/bin | head -30 | tr '\n' ' '
