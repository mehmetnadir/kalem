#!/usr/bin/python3 -I
"""ayna-sunucu.sh içine eksilme bekçisini ekler (bir kez; ikinci koşuda değişiklik yapmaz)."""
from pathlib import Path

yol = Path.home() / "01dev/_worktrees/kalem-0204/araclar/ayna-sunucu.sh"
s = yol.read_text(encoding="utf-8")
iz = 'cd "$KAYIT"\n'
bekci = '''# Eksilme bekçisi (15.11): yükleme aynadaki paket ağacını bütünüyle değiştirir. Kaynakta git dışı kalan dosya
# (ses, gsap, yazı tipi) yoksa aynadan da kaybolur ve editör kararır. Aynada olup kaynakta olmayan böyle dosya
# varsa yükleme durur. Bilerek eksiltmek için: AYNA_EKSILT=1.
AYNA_DEPO="${AYNA_DEPO:-$KAYIT/storage/kontrol-ayna/projeler}"
if [ "${AYNA_EKSILT:-0}" != 1 ]; then
  for p in "${paketler[@]}"; do
    [ -d "$AYNA_DEPO/$p" ] || continue
    kayip="$(cd "$AYNA_DEPO/$p" && find . -type f \\( -name '*.wav' -o -name '*.m4a' -o -name '*.mp3' -o -name '*.min.js' \\
      -o -path './ortak/font/*' \\) | while read -r f; do [ -f "$KOK/projeler/$p/$f" ] || echo "$f"; done)"
    if [ -n "$kayip" ]; then
      echo "HATA: $p — aynada olup kaynakta olmayan $(echo "$kayip" | wc -l) dosya var; yükleme bunları düşürür:" >&2
      echo "$kayip" | head -8 >&2
      echo "Kaynağı tamamla (ör. ayna-kayip.py --kopyala) ya da AYNA_EKSILT=1 ile bilerek eksilt." >&2
      exit 1
    fi
  done
fi
'''
if "Eksilme bekçisi" in s:
    print("zaten var")
else:
    assert s.count(iz) == 1
    yol.write_text(s.replace(iz, bekci + iz), encoding="utf-8")
    print("eklendi")
