#!/bin/bash
# test-ders-sonraki-hayir.sh — ders-sonraki.sh'ın "hayır" sayımı (DUZ3B mi KNT mi kararı) regresyon testi.
# 16.11 hatası: jüri hücreyi kalın yazınca ("| **hayır** |") sayım 0 çıktı, 6 ders düzeltmesiz yeniden jüriye gitti.
set -uo pipefail
BU="$(cd "$(dirname "$0")" && pwd)"
T="$(mktemp -d "${TMPDIR:-/tmp}/ders-sonraki-test.XXXXXX")"
satir=$(grep -m1 '^ *hayir=\$(grep' "$BU/ders-sonraki.sh") || { echo "KALDI: sayım satırı bulunamadı"; exit 1; }
gecti=0; kaldi=0
sina() { if [ "$2" = "$3" ]; then gecti=$((gecti + 1)); echo "GEÇTİ $1"; else kaldi=$((kaldi + 1)); echo "KALDI $1: beklenen [$3] gelen [$2]"; fi; }
say() { local h="$1"; eval "$satir"; echo "$hayir"; }
cat > "$T/karma.md" <<'EOF'
| Bölüm | evet | hayır | kanıt yok |
|---|---|---|---|
| DK-1 | **hayır** | `06/yardim.py:170` | Düzeltme: dolgu |
| EK-3 | hayır | kare yok | Düzeltme: koyu kare |
| EK-5b | hayır (kısmi) | tablo | Düzeltme: ekle |
| EK-6 | evet | — | — |
| EK-7 | **evet** | — | — |
| EK-8 | kanıt yok | — | — |
EOF
sina "karma: kalın + düz + parantezli = 3" "$(say "$T/karma.md")" "3"
printf '| Bölüm | evet | hayır | kanıt yok |\n| A | evet | x |\n| B | **evet** | y |\n' > "$T/temiz.md"
sina "temiz: başlık ve evet satırları sayılmaz" "$(say "$T/temiz.md")" "0"
printf '| DK-1 | **hayır** | a |\n| DK-2 | **hayır** | b |\n' > "$T/kalin.md"
sina "yalnız kalın: 2" "$(say "$T/kalin.md")" "2"
echo "SONUÇ geçti $gecti kaldı $kaldi"
[ "$kaldi" -eq 0 ]
