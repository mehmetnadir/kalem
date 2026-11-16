#!/bin/bash
# Sunucuda başsız Claude Code işi (srv21, sef): kos.sh <ad> <model> <istem-dosyası>
# Ayrık oturumda başlar (ssh kopsa da sürer). Çıktı: ~/is/uretim-0204/<ad>.json, <ad>.err, durum <ad>.durum,
# bitince <ad>.bitti (çıkış kodu). Silme yok: eski koşunun dosyaları eski/<zaman>/ altına taşınır.
set -euo pipefail
AD="$1" MODEL="$2" ISTEM="$3"
DIZIN="$HOME/is/uretim-0204"
K="$HOME/01dev/_worktrees/kalem-0204"
mkdir -p "$DIZIN"
[ -r "$ISTEM" ] || { echo "istem yok: $ISTEM" >&2; exit 1; }
case "$(cat "$DIZIN/$AD.durum" 2>/dev/null)" in calisiyor*) echo "zaten çalışıyor: $AD" >&2; exit 1 ;; esac
if ls "$DIZIN/$AD".{bitti,json,err,durum} >/dev/null 2>&1; then
  ESKI="$DIZIN/eski/$(date +%Y%m%d-%H%M%S)-$AD"; mkdir -p "$ESKI"
  for f in "$DIZIN/$AD".{bitti,json,err,durum}; do [ -e "$f" ] && mv "$f" "$ESKI/"; done
fi
export PATH="$HOME/.local/bin:$HOME/.venvs/ses/bin:$HOME/.nvm/versions/node/v24.22.2/bin:/usr/local/bin:/usr/bin:/bin"
# Kredi kipi (16.11): KREDI_ORG=<N|auto> verilirse oturum API kredisiyle koşar (kredi-sec.sh tavanı, kos-calis.sh gövdesi).
if [ -n "${KREDI_ORG:-}" ]; then
  if ! SECIM=$(bash "$DIZIN/kredi-sec.sh" "$KREDI_ORG"); then
    echo "bitti 91" > "$DIZIN/$AD.durum"; echo 91 > "$DIZIN/$AD.bitti"; echo "kredi yok: $AD" >&2; exit 1
  fi
  setsid bash "$DIZIN/kos-calis.sh" "$AD" "$MODEL" "$ISTEM" "${SECIM%% *}" "${SECIM#* }" < /dev/null > /dev/null 2>&1 &
  echo "başladı: $AD ($MODEL, kredi org ${SECIM%% *})"; exit 0
fi
setsid bash -c "
  cd '$K'
  echo \"calisiyor \$\$\" > '$DIZIN/$AD.durum'
  claude -p \"\$(cat '$ISTEM')\" --model '$MODEL' --dangerously-skip-permissions \
    --add-dir '$HOME/01dev/dijital-anlatim' --add-dir '$HOME/.claude/skills' \
    --output-format json > '$DIZIN/$AD.json' 2> '$DIZIN/$AD.err'
  rc=\$?
  echo \"bitti \$rc\" > '$DIZIN/$AD.durum'
  echo \$rc > '$DIZIN/$AD.bitti'
" < /dev/null > /dev/null 2>&1 &
echo "başladı: $AD ($MODEL)"
