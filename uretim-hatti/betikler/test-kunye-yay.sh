#!/bin/bash
# test-kunye-yay.sh — kunye-yay.sh fikstür testi (geçici kök; gerçek paketlere dokunmaz).
B="$(cd "$(dirname "$0")" && pwd)"; T="$(mktemp -d)"; gecti=0; kaldi=0
sina() { if [ "$2" = "$3" ]; then gecti=$((gecti + 1)); else kaldi=$((kaldi + 1)); echo "KALDI: $1 (beklenen $3, gelen $2)"; fi; }
mkdir -p "$T/projeler/ders/ortak" "$T/projeler/ders/sahneler/06-hf" "$T/projeler/ders/sahneler/01-hf" "$T/projeler/ders-dikey/ortak"
cat > "$T/projeler/ders/ortak/kunye.js" <<'EOF'
const TEMALAR = { koyu: { kirmizi: "#e0473b", ikincil: "#c9c2b3" }, acik: { kirmizi: "#d6453a", ikincil: "#5a6275" } };
export const KUNYE = { kenar: 56, ustTaban: 72, altTaban: 1030, logoYuk: 34, dersYazi: 30, seviyeYazi: 22,
  bolumYazi: 24, ajandaYazi: 20, ders: "X" };
    if (i === etkin) { ctx.beginPath(); ctx.arc(x - w - 12, k.altTaban - 7, 4, 0, Math.PI * 2); ctx.fill(); }
EOF
cat > "$T/projeler/ders/sahneler/06-hf/yardim.py" <<'EOF'
RENK = {"kirmizi": "#e0473b"}
        w = genislik("Lexend", 500, ad, 20)
            'font-size="20">%s</text><circle cx="%.2f" cy="1023" r="4" fill="%s"/></g>'
            'SIMPLE PRESENT<tspan id="ku-sev" dx="14" font-family="Lexend" font-weight="500" font-size="22" '
            'font-size="24" fill="%s">%s</text>'
            'font-size="24" fill="%s" style="opacity:0">%s</text>'
EOF
cat > "$T/projeler/ders/sahneler/01-hf/yardim.py" <<'EOF'
        w = genislik("Lexend", 500, ad, 20)
         'font-size="20">%s</text>'
         '<circle id="ku-nokta" cx="%.2f" cy="1023" r="4" fill="%s"/></g>'
EOF
cat > "$T/projeler/ders-dikey/ortak/kunye.js" <<'EOF'
const TEMALAR = { koyu: { kirmizi: "#e0473b" }, acik: { kirmizi: "#d6453a" } };
export const KUNYE = { kenar: 48, dersYazi: 56, seviyeYazi: 22, bolumYazi: 44 };
EOF
dk_once=$(grep -c "dersYazi: 56, seviyeYazi: 22, bolumYazi: 44" "$T/projeler/ders-dikey/ortak/kunye.js")
kuru=$(KALEM_KOK="$T" bash "$B/kunye-yay.sh" --kuru ders | grep -o "satır [0-9]*")
sina "kuru kip yazmaz" "$(grep -c 'ajandaYazi: 20' "$T/projeler/ders/ortak/kunye.js")" "1"
# Kuru sayım hesabı (yalnız künye desenleri, renk satırları sayılmaz):
#   ders/ortak/kunye.js: seviyeYazi: 22, (1 satır) + bolumYazi: 24, ajandaYazi: 20 (1 satır) = 2
#   ders/sahneler/06-hf/yardim.py: genislik(Lexend, 500, ad, 20) (1 satır) + cy="1023" r="4" (1 satır) = 2
#   ders/sahneler/01-hf/yardim.py: genislik(Lexend, 500, ad, 20) (1 satır) + cy="1023" r="4" (1 satır) = 2
#   Toplam: 2 + 2 + 2 = 6 satır
sina "kuru kip satır sayar" "$kuru" "satır 6"
KALEM_KOK="$T" bash "$B/kunye-yay.sh" ders ders-dikey > "$T/cikti.txt"
J="$T/projeler/ders/ortak/kunye.js"; Y="$T/projeler/ders/sahneler/06-hf/yardim.py"; G="$T/projeler/ders/sahneler/01-hf/yardim.py"
sina "kunye 30" "$(grep -c 'bolumYazi: 30, ajandaYazi: 30' "$J")" "1"
sina "seviye 30" "$(grep -c 'seviyeYazi: 30,' "$J")" "1"
sina "nokta yazıya göre" "$(grep -c 'k.ajandaYazi \* 0.35' "$J")" "1"
sina "kirmizi koyu aynen" "$(grep -c 'kirmizi: "#e0473b"' "$J")" "1"
sina "kirmizi açık aynen" "$(grep -c 'kirmizi: "#d6453a"' "$J")" "1"
sina "HF kirmizi aynen" "$(grep -c '"kirmizi": "#e0473b"' "$Y")" "1"
sina "HF genişlik 30" "$(grep -c 'ad, 30)' "$Y")" "1"
sina "HF 20/22/24 kalmadı" "$(grep -cE 'font-size="(20|22|24)"' "$Y")" "0"
sina "HF nokta cy" "$(grep -c 'cy="1019.5"' "$Y")" "1"
sina "01 ajanda 30" "$(grep -c 'font-size="30">%s</text>' "$G")" "1"
sina "01 nokta cy" "$(grep -c 'cy="1019.5"' "$G")" "1"
sina "dikey ölçü aynı" "$(grep -c 'dersYazi: 56, seviyeYazi: 22, bolumYazi: 44' "$T/projeler/ders-dikey/ortak/kunye.js")" "$dk_once"
sina "dikey kirmizi aynen" "$(grep -c '#e0473b\|#d6453a' "$T/projeler/ders-dikey/ortak/kunye.js")" "1"
sina "yalnız yatay paket değişti" "$(grep -o 'değişen paket [0-9]*' "$T/cikti.txt")" "değişen paket 1"
KALEM_KOK="$T" bash "$B/kunye-yay.sh" ders ders-dikey > "$T/cikti2.txt"
sina "ikinci koşu değiştirmez" "$(grep -o 'değişen paket [0-9]*' "$T/cikti2.txt")" "değişen paket 0"
# --renksiz: künye 30 olur, kirmizi aynen kalır (G-8 açıkken)
R="$T/renksiz"; mkdir -p "$R/projeler/ders/ortak"
printf '%s\n' 'const TEMALAR = { koyu: { kirmizi: "#e0473b" }, acik: { kirmizi: "#d6453a" } };' \
  'export const KUNYE = { seviyeYazi: 22, bolumYazi: 24, ajandaYazi: 20 };' > "$R/projeler/ders/ortak/kunye.js"
rk=$(KALEM_KOK="$R" bash "$B/kunye-yay.sh" --kuru --renksiz ders | grep -o "satır [0-9]*")
sina "renksiz kuru yalnız künye satırı sayar (renk satırı sayılmaz)" "$rk" "satır 1"
KALEM_KOK="$R" bash "$B/kunye-yay.sh" --renksiz ders > /dev/null
sina "renksiz künye 30" "$(grep -c 'bolumYazi: 30, ajandaYazi: 30' "$R/projeler/ders/ortak/kunye.js")" "1"
sina "renksiz kirmizi aynen" "$(grep -c '#e0473b\|#d6453a' "$R/projeler/ders/ortak/kunye.js")" "1"
mkdir -p "$HOME/Silinecekler/$(date +%F)-test-kunye-yay"; mv "$T" "$HOME/Silinecekler/$(date +%F)-test-kunye-yay/"
echo "SONUÇ geçti $gecti kaldı $kaldi"
[ "$kaldi" -eq 0 ]
