#!/bin/bash
# DUZ-1 sonrası: 3 paketi aynaya yükle, içe al, yalnız DUZ-1 dosyalarını commit et.
set -euo pipefail
K=/home/sef/01dev/_worktrees/kalem-0204
cd "$K"
[ "${YALNIZ_COMMIT:-0}" = 1 ] || bash araclar/ayna-sunucu.sh --kok "$K" 02-04-ydt-temel-s1 simple-present-temel-s1 simple-present-temel-s2 2>&1 | tail -6
[ "${YALNIZ_COMMIT:-0}" = 1 ] || bash /home/sef/is/uretim-0204/ice-al.sh 2>&1 | tail -6
DOSYALAR=(
  projeler/02-04-ydt-temel-s1/aciklama-a.md
  projeler/02-04-ydt-temel-s1/aciklama-b.md
  projeler/02-04-ydt-temel-s1/aciklama.md
  projeler/02-04-ydt-temel-s1/sahneler/07-hyperframes-hikaye-b/SPEC.md
  projeler/02-04-ydt-temel-s1/sahneler/07-hyperframes-hikaye-b/nesneler.json
  projeler/02-04-ydt-temel-s1/sahneler/07-hyperframes-hikaye-b/proje/index.html
  projeler/02-04-ydt-temel-s1/sahneler/07-hyperframes-hikaye-b/uret.py
  projeler/02-04-ydt-temel-s1/uretim-tutanagi/DUZ-1-RAPOR.md
  projeler/simple-present-temel-s1/aciklama-a.md
  projeler/simple-present-temel-s1/aciklama-b.md
  projeler/simple-present-temel-s1/aciklama.md
  projeler/simple-present-temel-s1/ortak/anlatim/senaryo.json
  projeler/simple-present-temel-s1/surumler.json
  projeler/simple-present-temel-s2/aciklama-a.md
  projeler/simple-present-temel-s2/aciklama-b.md
  projeler/simple-present-temel-s2/aciklama.md
)
git add -- "${DOSYALAR[@]}"
git -c user.name="sef (srv21)" -c user.email="sef@srv21.local" commit -q -F - --only -- "${DOSYALAR[@]}" <<'MESAJ'
fix(huni): bağımsız inceleme düzeltmeleri (hikâye B, yanlış denklik, utm, mutlak kural)

- 02-04-ydt-temel-s1: hikâye B doğru cümlenin üstünü çizmiyor; iki şık yan yana, etiketli
- simple-present-temel-s1: "Türkçe geniş zaman eki = İngilizce s" denkliği açıklama ve künyeden çıktı
- 02-04-ydt-temel-s1: utm_campaign ve utm_content standarda çekildi; yazım hatası düzeltildi
- simple-present-temel-s2: always için mutlak kural cümlesi yumuşatıldı

Co-Authored-By: Claude Fable 5.2 <noreply@anthropic.com>
MESAJ
git log --oneline -1
