#!/bin/bash
# Sunucu worktree'sinde kapak sahneleri ve 02-04 huni v2 üretimini iki commit olarak yazar (kullanıcı sef).
set -euo pipefail
K="$HOME/01dev/_worktrees/kalem-0204"
cd "$K"
G=(git -c user.name="sef (srv21)" -c user.email="sef@srv21.local")
dersler="simple-present-temel 02-04-ydt-temel present-continuous present-continuous-ileri simple-present-ileri 02-03-ydt-temel present-perfect-temel present-perfect-ileri present-perfect-cont-temel present-perfect-cont-ileri simple-past-temel simple-past-ileri"

if [ "${1:-}" = "kapak" ]; then
  for d in $dersler; do
    for p in "$d" "$d-dikey"; do
      [ -d "projeler/$p/sahneler/90-hyperframes-kapak" ] && git add "projeler/$p/sahneler/90-hyperframes-kapak"
      [ -e "projeler/$p/ortak/kapak" ] && git add "projeler/$p/ortak/kapak"
      for f in KAPAK-RAPOR.md kapak-168.png; do
        [ -f "projeler/$p/uretim-tutanagi/$f" ] && git add "projeler/$p/uretim-tutanagi/$f"
      done
    done
  done
  git diff --cached --stat | tail -1
  "${G[@]}" commit -q -F - <<'MSG'
feat(kapak): 12 dersin tasarlanmış kapak sahneleri (yatay + dikey, açık + koyu)

Kapak standardı v1: sahneler/90-hyperframes-kapak (durağan kare, zaman.json dışında),
HTML ile dizilen yazı (Fredoka 700), imagen karakter + nesne, çıkartma kenarı.
Kök kapak.png / kapak-koyu.png git dışı; ayna ile panele gider.

Co-Authored-By: Claude Fable 5.2 <noreply@anthropic.com>
MSG
fi

if [ "${1:-}" = "huni" ]; then
  shift
  for p in "$@"; do git add -A "projeler/$p"; done
  git diff --cached --stat | tail -1
  "${G[@]}" commit -q -F - <<MSG
feat(huni): $* huni v2 (kanal katmanı, kaydet sahnesi, öğrenci sesiyle çağrı)

Huni v2 standardı: kısa boyunca ydspublishing + @ydspublishing katmanı, 4 sahne
(kanca, değer, kaydet, çağrı), son sahnede ana dersin kapağı, çekirdek cümle
"Dersin tamamı YDS Publishing YouTube kanalında." Çakışma kapısı 0 uyarı.

Co-Authored-By: Claude Fable 5.2 <noreply@anthropic.com>
MSG
fi
git log --oneline -3
git status --porcelain | wc -l
