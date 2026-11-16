#!/bin/bash
# kos-calis.sh <ad> <model> <istem> <org> <env dosyası>  [ortam KOS_DEVAM=<oturum>] — kos.sh kredi kipinin ayrık gövdesi. (srv21, sef)
# Abonelik kimliği çocuğa geçmez; API anahtarı yalnız ortam dosyasından yüklenir, basılmaz. Bitince maliyet deftere yazılır.
AD="$1" MODEL="$2" ISTEM="$3" ORG="$4" ENVF="$5"
DIZIN="$HOME/is/uretim-0204"; K="$HOME/01dev/_worktrees/kalem-0204"
cd "$K" || exit 1
echo "calisiyor $$" > "$DIZIN/$AD.durum"
unset CLAUDE_CODE_OAUTH_TOKEN ANTHROPIC_AUTH_TOKEN CLAUDECODE CLAUDE_PID CLAUDE_EFFORT CLAUDE_AGENT_SDK_VERSION
for v in $(env | grep -o '^CLAUDE_CODE_[A-Z_]*'); do unset "$v"; done
set -a; . "$ENVF"; set +a
# KOS_DEVAM=<oturum kimliği>: yarıda kesilen oturumu aynı dökümle sürdür (istem = devam mesajı).
DEVAM=(); [ -n "${KOS_DEVAM:-}" ] && DEVAM=(--resume "$KOS_DEVAM")
# KOS_PROFIL=yalin (16.11, ölçüm): oturum ~/.claude-uretim yapılandırma dizininde koşar. Etkileşimli conductor
# kuralları, 212 skill listesi ve 55 kanca yüklenmez; taban bağlam 72 K → 24 K token ve özdeş önek oturumlar arasında
# önbellekten okunur. Kanca: kanca-bash, tarayıcı havuzu, Playwright, görüntü küçültme, Türkçe karakter
# (settings.json → uretim-hatti/profil/yalin-ayar.json); kurallar CLAUDE.md → yalin-kurallar.md. --bare kullanılmaz:
# o kipte --settings kancaları da koşmaz (16.11 ölçüm). Sürdürme (KOS_DEVAM) aynı profille yapılır (döküm o dizinde).
PROFIL=(); PD="$HOME/.claude-uretim"
if [ "${KOS_PROFIL:-}" = yalin ] && [ -r "$PD/settings.json" ] && [ -r "$PD/CLAUDE.md" ]; then
  export CLAUDE_CONFIG_DIR="$PD"
  PROFIL=(--disable-slash-commands --strict-mcp-config --tools "Bash,Read,Edit,Write,Grep,Glob,Monitor")
fi
claude -p "$(cat "$ISTEM")" "${DEVAM[@]}" --model "$MODEL" --dangerously-skip-permissions "${PROFIL[@]}" \
  --add-dir "$HOME/01dev/dijital-anlatim" --add-dir "$HOME/.claude/skills" \
  --output-format json > "$DIZIN/$AD.json" 2> "$DIZIN/$AD.err"
rc=$?
m=$(grep -a -o '"total_cost_usd":[0-9.]*' "$DIZIN/$AD.json" | tail -1 | cut -d: -f2)
# Kredi bitti işareti (16.11 ölçüm: org 3 Mac + sunucu harcamasıyla 200 $'ı aştı, 7 oturum "Credit balance is too low"
# ile öldü; sunucu defteri Mac harcamasını görmez). İşaretli org'u kredi-sec.sh o ay seçmez.
grep -aq "Credit balance is too low" "$DIZIN/$AD.json" "$DIZIN/$AD.err" 2>/dev/null \
  && echo "$(date -Is) $AD" >> "$DIZIN/kredi-bitti-$ORG-$(date -u +%Y-%m)"
pr="${PROFIL[0]:+yalin}"
printf '{"zaman":"%s","ay":"%s","ad":"%s","org":"%s","model":"%s","maliyet":%s,"rc":%s,"profil":"%s"}\n' \
  "$(date -Is)" "$(date -u +%Y-%m)" "$AD" "$ORG" "$MODEL" "${m:-0}" "$rc" "${pr:-tam}" >> "$DIZIN/kredi-defter.jsonl"
echo "bitti $rc" > "$DIZIN/$AD.durum"
echo "$rc" > "$DIZIN/$AD.bitti"
