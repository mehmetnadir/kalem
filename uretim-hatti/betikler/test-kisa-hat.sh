#!/bin/bash
# test-kisa-hat.sh — kisa-hat.sh ve model parametreli sonra/sonra2/zincir2 betiklerini sahte HOME'da sınar.
# Sahte kos.sh (çağrıyı günlüğe yazar, durum dosyasını hemen "bitti <rc>" yapar), sahte setsid/sleep/timeout/node.
# Mac'te de koşar (setsid, timeout yok → sahte kabuk betikleri). Model çağrısı yok.
set -uo pipefail
BU="$(cd "$(dirname "$0")" && pwd)"
ANA="${TMPDIR:-/tmp}"
gecti=0; kaldi=0
sina() { if [ "$2" = "$3" ]; then gecti=$((gecti + 1)); echo "GEÇTİ $1"; else kaldi=$((kaldi + 1)); echo "KALDI $1: beklenen [$3] gelen [$2]"; fi; }

# kur: yeni sahte ortam; T, H, R, K, L (çağrı günlüğü) değişkenlerini ayarlar
kur() {
  T="$(mktemp -d "$ANA/kisa-hat-test.XXXXXX")"; H="$T/home"
  R="$H/is/uretim-0204"; K="$H/01dev/_worktrees/kalem-0204"; L="$T/cagri.log"
  mkdir -p "$R" "$H/.local/bin" "$K/araclar" "$K/projeler/p1-s2/uretim-tutanagi/istem/sahne"
  : > "$L"
  for f in sonra.sh sonra2.sh zincir2.sh sahne-kuyruk2.sh; do cp "$BU/$f" "$R/$f"; done
  for ad in A B-dil B-kural C; do echo "istem" > "$R/P0201T-S2-$ad.md"; done
  for s in 01-a 02-b; do echo "sahne" > "$K/projeler/p1-s2/uretim-tutanagi/istem/sahne/D-$s.md"; done
  printf '#!/bin/bash\nexec "$@"\n' > "$H/.local/bin/setsid"
  printf '#!/bin/bash\nexec /bin/sleep 0.2\n' > "$H/.local/bin/sleep"
  printf '#!/bin/bash\nshift\nexec "$@"\n' > "$H/.local/bin/timeout"
  printf '#!/bin/bash\necho "node $*" >> "%s"\n' "$L" > "$H/.local/bin/node"
  # sahte kos.sh: rc dosyası $R/rc-<ad> varsa o kod, yoksa 0
  cat > "$R/kos.sh" <<E
#!/bin/bash
echo "kos \$1 \$2 \$(basename "\$3")" >> "$L"
rc=0; [ -f "$R/rc-\$1" ] && rc="\$(cat "$R/rc-\$1")"
echo "bitti \$rc" > "$R/\$1.durum"
E
  chmod +x "$H/.local/bin/"* "$R/kos.sh"
}
# kos: kisa-hat.sh'ı sahte ortamda koştur
kos() { HOME="$H" PATH="$H/.local/bin:$PATH" bash "$BU/kisa-hat.sh" "$@"; }
bekle() { for _ in $(seq 1 100); do case "$(cat "$R/$1.durum" 2>/dev/null)" in bitti*) return ;; esac; sleep 0.2; done; }
sira() { grep -n -- "$1" "$L" | head -1 | cut -d: -f1; }
satirlar() { grep -c "$1" "$L"; }

# 1) --kuru: hiçbir şey başlamaz, plan basılır
kur
cikti="$(kos 0201T p1 2 --kuru --model claude-sonnet-5-5 2>&1)"; rc=$?
sina "kuru: çıkış 0" "$rc" "0"
sina "kuru: çağrı yok" "$(wc -l < "$L" | tr -d ' ')" "0"
sina "kuru: durum dosyası yok" "$(ls "$R"/*.durum 2>/dev/null | wc -l | tr -d ' ')" "0"
sina "kuru: plan iş adı" "$(echo "$cikti" | grep -c '^ 3. P0201T-S2-B-kural')" "1"
sina "kuru: sahne öneki" "$(echo "$cikti" | grep -c 'K0201TS2')" "1"
sina "kuru: sonnet üretici → jüri opus" "$(echo "$cikti" | head -1)" "plan: 0201T p1 S2 · üretici claude-sonnet-5-5 · jüri claude-opus-5-5 · sahne eşzamanlı 3"

# 2) varsayılan modeller ve sıra
kur
kos 0201T p1 2 > "$T/cikti.txt" 2>&1; sina "varsayılan: çıkış 0" "$?" "0"
bekle zincir2-K0201TS2
sina "varsayılan: zincir bitti 0" "$(cat "$R/zincir2-K0201TS2.durum")" "bitti 0"
sina "varsayılan: A opus" "$(grep -c '^kos P0201T-S2-A claude-opus-5-5 P0201T-S2-A.md$' "$L")" "1"
sina "varsayılan: B-dil sonnet" "$(grep -c '^kos P0201T-S2-B-dil claude-sonnet-5-5 P0201T-S2-B-dil.md$' "$L")" "1"
sina "varsayılan: B-kural sonnet" "$(grep -c '^kos P0201T-S2-B-kural claude-sonnet-5-5 P0201T-S2-B-kural.md$' "$L")" "1"
sina "varsayılan: C opus" "$(grep -c '^kos P0201T-S2-C claude-opus-5-5 P0201T-S2-C.md$' "$L")" "1"
sina "varsayılan: sahneler opus (2)" "$(grep -c '^kos K0201TS2-.* claude-opus-5-5 D-' "$L")" "2"
a=$(sira 'kos P0201T-S2-A '); bd=$(sira 'kos P0201T-S2-B-dil'); bk=$(sira 'kos P0201T-S2-B-kural')
c=$(sira 'kos P0201T-S2-C '); sh=$(sira 'kos K0201TS2-'); nd=$(sira '^node')
sina "sıra: A < B-dil ve B-kural" "$([ "$a" -lt "$bd" ] && [ "$a" -lt "$bk" ] && echo evet)" "evet"
sina "sıra: B'ler < C" "$([ "$bd" -lt "$c" ] && [ "$bk" -lt "$c" ] && echo evet)" "evet"
sina "sıra: C < sahne < kapı" "$([ "$c" -lt "$sh" ] && [ "$sh" -lt "$nd" ] && echo evet)" "evet"
sina "kapı: çakışma kapısı p1-s2 ile" "$(grep -c 'cakisma-kapisi.mjs p1-s2' "$L")" "1"

# 3) --model sonnet: üretici sonnet, jüri otomatik opus; sahne sonnet
kur
kos 0201T p1 2 --model claude-sonnet-5-5 --esz 1 > /dev/null 2>&1
bekle zincir2-K0201TS2
sina "sonnet: A sonnet" "$(grep -c '^kos P0201T-S2-A claude-sonnet-5-5 ' "$L")" "1"
sina "sonnet: jüriler opus" "$(grep -c '^kos P0201T-S2-B-.* claude-opus-5-5 ' "$L")" "2"
sina "sonnet: C sonnet" "$(grep -c '^kos P0201T-S2-C claude-sonnet-5-5 ' "$L")" "1"
sina "sonnet: sahneler sonnet (2)" "$(grep -c '^kos K0201TS2-.* claude-sonnet-5-5 ' "$L")" "2"
# jüri = üretici → çıkış 2, çağrı yok
kur
kos 0201T p1 2 --model claude-sonnet-5-5 --juri-model claude-sonnet-5-5 > /dev/null 2>&1; rc=$?
sina "aynı model: çıkış 2" "$rc" "2"
sina "aynı model: çağrı yok" "$(wc -l < "$L" | tr -d ' ')" "0"
# açık jüri modeli
kur
kos 0201T p1 2 --juri-model modelx > /dev/null 2>&1; bekle zincir2-K0201TS2
sina "açık jüri: modelx (2)" "$(grep -c '^kos P0201T-S2-B-.* modelx ' "$L")" "2"

# 4) B-kural hatalı (rc 1): C başlamaz, sahne başlamaz
kur; echo 1 > "$R/rc-P0201T-S2-B-kural"
kos 0201T p1 2 > /dev/null 2>&1
bekle sonra2-P0201T-S2-C; bekle zincir2-K0201TS2
sina "B hatalı: C başlamadı" "$(satirlar '^kos P0201T-S2-C ')" "0"
sina "B hatalı: sonra2 bitti 90" "$(cat "$R/sonra2-P0201T-S2-C.durum")" "bitti 90"
sina "B hatalı: sahne yok" "$(satirlar '^kos K0201TS2-')" "0"
sina "B hatalı: kapı yok" "$(satirlar '^node')" "0"
sina "B hatalı: zincir2 bitti 90" "$(cut -d' ' -f1-2 "$R/zincir2-K0201TS2.durum")" "bitti 90"
# 5) A hatalı: B başlamaz
kur; echo 1 > "$R/rc-P0201T-S2-A"
kos 0201T p1 2 > /dev/null 2>&1; bekle sonra-P0201T-S2-A; bekle sonra2-P0201T-S2-C
sina "A hatalı: B başlamadı" "$(satirlar '^kos P0201T-S2-B-')" "0"
sina "A hatalı: sonra bitti 90" "$(cat "$R/sonra-P0201T-S2-A.durum")" "bitti 90"
bekle zincir2-K0201TS2
sina "A hatalı: sonra2 bitti 90 (B bitti 90 ile zincirlendi)" "$(cat "$R/sonra2-P0201T-S2-C.durum")" "bitti 90"
sina "A hatalı: zincir2 bitti 90 (takılı kalmaz)" "$(cut -d' ' -f1-2 "$R/zincir2-K0201TS2.durum")" "bitti 90"
sina "A hatalı: C başlamadı" "$(satirlar '^kos P0201T-S2-C ')" "0"
# 5b) önceki koşudan kalan bayat "bitti 0" durumları zinciri yanıltmaz (eski/ altına taşınır), A hatalıysa C yine başlamaz
kur
for ad in P0201T-S2-B-dil P0201T-S2-B-kural P0201T-S2-C; do echo "bitti 0" > "$R/$ad.durum"; done
echo 1 > "$R/rc-P0201T-S2-A"
kos 0201T p1 2 > /dev/null 2>&1; bekle zincir2-K0201TS2
sina "bayat durum: C başlamadı" "$(satirlar '^kos P0201T-S2-C ')" "0"
sina "bayat durum: eski/ altına taşındı" "$(ls "$R"/eski/*/P0201T-S2-B-dil.durum 2>/dev/null | wc -l | tr -d ' ')" "1"
sina "bayat durum: zincir2 bitti 90" "$(cut -d' ' -f1-2 "$R/zincir2-K0201TS2.durum")" "bitti 90"
# 6) eksik istem dosyası: çıkış 2, kos yok
kur; mv "$R/P0201T-S2-C.md" "$T/C.yedek"
kos 0201T p1 2 > /dev/null 2>&1; rc=$?
sina "istem eksik: çıkış 2" "$rc" "2"
sina "istem eksik: çağrı yok" "$(wc -l < "$L" | tr -d ' ')" "0"

# 7) mevcut betikler: KISA_MODEL yoksa claude-opus-5-5 (varsayılan davranış değişmedi), varsa o
kur
HOME="$H" PATH="$H/.local/bin:$PATH" bash "$BU/sonra.sh" BEK1 IS1 > /dev/null; echo "bitti 0" > "$R/BEK1.durum"; bekle sonra-BEK1
sina "sonra.sh varsayılan opus" "$(grep -c '^kos IS1 claude-opus-5-5 IS1.md$' "$L")" "1"
HOME="$H" PATH="$H/.local/bin:$PATH" KISA_MODEL=mx bash "$BU/sonra.sh" BEK2 IS2 > /dev/null; echo "bitti 0" > "$R/BEK2.durum"; bekle sonra-BEK2
sina "sonra.sh KISA_MODEL=mx" "$(grep -c '^kos IS2 mx IS2.md$' "$L")" "1"
echo "bitti 0" > "$R/X1.durum"; echo "bitti 0" > "$R/X2.durum"
HOME="$H" PATH="$H/.local/bin:$PATH" bash "$BU/sonra2.sh" X1 X2 IS3 > /dev/null; bekle sonra2-IS3
sina "sonra2.sh varsayılan opus" "$(grep -c '^kos IS3 claude-opus-5-5 IS3.md$' "$L")" "1"
HOME="$H" PATH="$H/.local/bin:$PATH" KISA_MODEL=mx bash "$BU/sonra2.sh" X1 X2 IS4 > /dev/null; bekle sonra2-IS4
sina "sonra2.sh KISA_MODEL=mx" "$(grep -c '^kos IS4 mx IS4.md$' "$L")" "1"
echo "bitti 0" > "$R/BEK3.durum"
HOME="$H" PATH="$H/.local/bin:$PATH" bash "$BU/zincir2.sh" BEK3 ZO1 p1-s2 > /dev/null; bekle zincir2-ZO1
sina "zincir2.sh varsayılan opus (sahne 2)" "$(grep -c '^kos ZO1-.* claude-opus-5-5 D-' "$L")" "2"
HOME="$H" PATH="$H/.local/bin:$PATH" KISA_MODEL=mx bash "$BU/zincir2.sh" BEK3 ZO2 p1-s2 > /dev/null; bekle zincir2-ZO2
sina "zincir2.sh KISA_MODEL=mx (sahne 2)" "$(grep -c '^kos ZO2-.* mx D-' "$L")" "2"

echo "SONUÇ geçti $gecti kaldı $kaldi"
[ "$kaldi" -eq 0 ]
