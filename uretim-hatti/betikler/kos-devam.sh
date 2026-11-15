#!/bin/bash
# Biten başsız oturumu sürdür (srv21, sef): kos-devam.sh <ad> <mesaj-dosyası>
# Oturum kimliği ve model <ad>.json'dan okunur; eski koşu dosyaları eski/<zaman>-<ad>/ altına taşınır (silme yok).
set -euo pipefail
AD="$1" MESAJ="$2"
DIZIN="$HOME/is/uretim-0204"
K="$HOME/01dev/_worktrees/kalem-0204"
[ -r "$MESAJ" ] || { echo "mesaj yok: $MESAJ" >&2; exit 1; }
case "$(cat "$DIZIN/$AD.durum" 2>/dev/null)" in calisiyor*) echo "zaten çalışıyor: $AD" >&2; exit 1 ;; esac
read -r SID MODEL < <(/usr/bin/python3 -I -c '
import json, sys
d = json.load(open(sys.argv[1]))
print(d["session_id"], next(iter(d.get("modelUsage") or {"opus": 0})))
' "$DIZIN/$AD.json")
ESKI="$DIZIN/eski/$(date +%Y%m%d-%H%M%S)-$AD"; mkdir -p "$ESKI"
for f in "$DIZIN/$AD".{bitti,json,err,durum}; do [ -e "$f" ] && mv "$f" "$ESKI/"; done
export PATH="$HOME/.local/bin:$HOME/.venvs/ses/bin:$HOME/.nvm/versions/node/v24.22.2/bin:/usr/local/bin:/usr/bin:/bin"
setsid bash -c "
  cd '$K'
  echo \"calisiyor \$\$\" > '$DIZIN/$AD.durum'
  claude -p \"\$(cat '$MESAJ')\" --resume '$SID' --model '$MODEL' --dangerously-skip-permissions \
    --add-dir '$HOME/01dev/dijital-anlatim' --add-dir '$HOME/.claude/skills' \
    --output-format json > '$DIZIN/$AD.json' 2> '$DIZIN/$AD.err'
  rc=\$?
  echo \"bitti \$rc\" > '$DIZIN/$AD.durum'
  echo \$rc > '$DIZIN/$AD.bitti'
" < /dev/null > /dev/null 2>&1 &
echo "sürdürüldü: $AD ($SID, $MODEL)"
