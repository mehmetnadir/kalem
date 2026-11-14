#!/bin/bash
# Sunucuda (srv21, sef) ders sesi sentezi: dijital-anlatim el.py'yi kayit vekiliyle koşar.
# Anahtar kayit sürecinden çıkmaz (ELEVEN_VEKIL_URL + işçi jetonu); Whisper kapısı yerel faster-whisper.
#   araclar/ses-sunucu.sh [--kok <kalem dizini>] <paket> [ses_id] [model]
# Mac'te kullanılmaz (Mac yolu: uv run … el.py, Keychain).
set -euo pipefail
KOK="$(cd "$(dirname "$0")/.." && pwd)"
if [ "${1:-}" = "--kok" ]; then KOK="$(cd "$2" && pwd)"; shift 2; fi
PAKET="${1:-}"
[ -n "$PAKET" ] || { echo "kullanım: ses-sunucu.sh [--kok D] <paket> [ses_id] [model]" >&2; exit 1; }
[[ "$PAKET" =~ ^[a-z0-9]+(-[a-z0-9]+)*$ ]] || { echo "HATA: paket adı kural dışı: $PAKET" >&2; exit 1; }
A="$KOK/projeler/$PAKET/ortak/anlatim"
[ -f "$A/senaryo.json" ] || { echo "HATA: senaryo yok: $A/senaryo.json" >&2; exit 1; }
DA="${DA_KOK:-$HOME/01dev/dijital-anlatim}"
EL="$DA/araclar/iki-dilli/el.py"
[ -f "$EL" ] || { echo "HATA: el.py yok: $EL" >&2; exit 1; }
PY="${SES_PY:-$HOME/.venvs/ses/bin/python}"
[ -x "$PY" ] || { echo "HATA: ses python'u yok: $PY" >&2; exit 1; }
ORTAM="${KONTROL_ORTAM:-$HOME/.config/sef/kontrol.env}"
[ -r "$ORTAM" ] || { echo "HATA: işçi ortam dosyası okunamıyor: $ORTAM" >&2; exit 1; }
KONTROL_ISCI_JETON="$(sed -n 's/^KONTROL_ISCI_JETON=//p' "$ORTAM" | tail -1)"
[ -n "$KONTROL_ISCI_JETON" ] || { echo "HATA: $ORTAM içinde KONTROL_ISCI_JETON yok" >&2; exit 1; }
export KONTROL_ISCI_JETON
export ELEVEN_VEKIL_URL="${ELEVEN_VEKIL_URL:-http://127.0.0.1:3810/api/kontrol/saglayici/elevenlabs}"
export HIZ_EN="${HIZ_EN:-0.9}"
export ASR_IPLIK="${ASR_IPLIK:-12}"
# Model önbellekteyse ağa çıkma (HF yeniden doğrulaması yok); yoksa el.py açık hata verir.
export HF_HUB_OFFLINE="${HF_HUB_OFFLINE:-1}"
SES="${2:-gsJ9nrlXYbPztJxC4fwc}"
MODEL="${3:-eleven_v4}"
KILIT="${TMPDIR:-/tmp}/ses-sunucu-$PAKET.kilit"
exec 9>"$KILIT"
flock -n 9 || { echo "HATA: $PAKET için sentez zaten koşuyor ($KILIT)" >&2; exit 1; }
echo "→ sentez: $PAKET · ses $SES · model $MODEL · vekil $ELEVEN_VEKIL_URL"
"$PY" -I "$EL" "$A/senaryo.json" "$A/sentez.wav" "$A" "$SES" "$MODEL"
