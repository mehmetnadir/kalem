#!/bin/bash
# ayna-sunucu.sh eksilme bekçisini sunucu worktree'sinde commit eder (kullanıcı sef).
set -euo pipefail
cd "$HOME/01dev/_worktrees/kalem-0204"
git -c user.name="sef (srv21)" -c user.email="sef@srv21.local" commit -q --only araclar/ayna-sunucu.sh -F - <<'MSG'
fix(ayna): eksilme bekçisi, aynada olup kaynakta olmayan ses/gsap/yazı tipi varsa yükleme durur

15.11: kapak yüklemesi 21 paketin anlatim.wav ve gsap.min.js dosyalarını düşürdü (git dışı dosyalar
worktree'de yoktu), editör karardı. Dosyalar .eski ağacından geri kondu; bekçi tekrarını önler.
Bilerek eksiltme: AYNA_EKSILT=1.

Co-Authored-By: Claude Fable 5.2 <noreply@anthropic.com>
MSG
git log --oneline -1
git status --porcelain | head -3
