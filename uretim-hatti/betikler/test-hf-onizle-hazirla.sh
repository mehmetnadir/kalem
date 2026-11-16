#!/bin/bash
# test-hf-onizle-hazirla.sh — hf-onizle-hazirla.sh fikstür testi (geçici kök; gerçek paketlere dokunmaz).

set -uo pipefail

B="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
T="$(mktemp -d)"
gecti=0
kaldi=0

sina() {
  if [ "$2" = "$3" ]; then
    gecti=$((gecti + 1))
  else
    kaldi=$((kaldi + 1))
    echo "KALDI: $1 (beklenen $3, gelen $2)"
  fi
}

# Fikstür oluşturma:
# 2 paket:
# Paket 1 (p1):
#   - 01-hyperframes-var: gsap'lı HF sahnesi (zaten var)
#   - 02-canvas-sahne: gsap'sız canvas sahnesi (adı hyperframes içermeyen)
# Paket 2 (p2):
#   - 01-hyperframes-eksik: gsap'sız HF sahnesi (calistir.sh var)
#   - 02-hyperframes-hatali: gsap'sız HF sahnesi (calistir.sh exit 3 verir)
#   - 03-hyperframes-nosh: calistir.sh'sız HF sahnesi

mkdir -p "$T/projeler/p1/sahneler/01-hyperframes-var/proje/lib"
echo "var" > "$T/projeler/p1/sahneler/01-hyperframes-var/proje/lib/gsap.min.js"
cat > "$T/projeler/p1/sahneler/01-hyperframes-var/calistir.sh" <<'EOF'
#!/bin/bash
echo "KOSMAMALI" > kosmamali.log
exit 0
EOF
chmod +x "$T/projeler/p1/sahneler/01-hyperframes-var/calistir.sh"

mkdir -p "$T/projeler/p1/sahneler/02-canvas-sahne"
cat > "$T/projeler/p1/sahneler/02-canvas-sahne/calistir.sh" <<'EOF'
#!/bin/bash
echo "CANVAS" > canvas.log
exit 0
EOF
chmod +x "$T/projeler/p1/sahneler/02-canvas-sahne/calistir.sh"

mkdir -p "$T/projeler/p2/sahneler/01-hyperframes-eksik"
cat > "$T/projeler/p2/sahneler/01-hyperframes-eksik/calistir.sh" <<'EOF'
#!/bin/bash
mkdir -p proje/lib
echo x > proje/lib/gsap.min.js
echo "${ONIZLE_YALNIZ:-}" > onizle_yalniz.val
exit 0
EOF
chmod +x "$T/projeler/p2/sahneler/01-hyperframes-eksik/calistir.sh"

mkdir -p "$T/projeler/p2/sahneler/02-hyperframes-hatali"
cat > "$T/projeler/p2/sahneler/02-hyperframes-hatali/calistir.sh" <<'EOF'
#!/bin/bash
exit 3
EOF
chmod +x "$T/projeler/p2/sahneler/02-hyperframes-hatali/calistir.sh"

mkdir -p "$T/projeler/p2/sahneler/03-hyperframes-nosh"

# 1. Test: --kuru sayısı ve listesi doğru
kuru_cikti=$(KALEM_KOK="$T" bash "$B/hf-onizle-hazirla.sh" --kuru)
sina "kuru sayısı 2 eksik" "$(echo "$kuru_cikti" | grep -c '^SONUÇ eksik 2$')" "1"
sina "kuru p2/01 listelendi" "$(echo "$kuru_cikti" | grep -c '^p2/01-hyperframes-eksik$')" "1"
sina "kuru p2/02 listelendi" "$(echo "$kuru_cikti" | grep -c '^p2/02-hyperframes-hatali$')" "1"
sina "kuru p1/01 listelenmedi" "$(echo "$kuru_cikti" | grep -c '01-hyperframes-var')" "0"
sina "kuru canvas listelenmedi" "$(echo "$kuru_cikti" | grep -c '02-canvas-sahne')" "0"
sina "kuru nosh listelenmedi" "$(echo "$kuru_cikti" | grep -c '03-hyperframes-nosh')" "0"

# 2. Test: --kuru hiçbir dosya yazmaz
sina "kuru dosya yazmadı gsap" "$([ -f "$T/projeler/p2/sahneler/01-hyperframes-eksik/proje/lib/gsap.min.js" ] && echo 1 || echo 0)" "0"
sina "kuru dosya yazmadı val" "$([ -f "$T/projeler/p2/sahneler/01-hyperframes-eksik/onizle_yalniz.val" ] && echo 1 || echo 0)" "0"

# 3. Test: Tekil paket argümanı ile kuru kip (p1'de eksik yok -> 0)
kuru_p1=$(KALEM_KOK="$T" bash "$B/hf-onizle-hazirla.sh" --kuru p1)
sina "kuru p1 eksik 0" "$(echo "$kuru_p1" | grep -c '^SONUÇ eksik 0$')" "1"

# 4. Test: p2 tekil paket koşusu (hatalı sahne var -> çıkış 1, hazırlanan 1 · hatalı 1)
set +e
p2_cikti=$(KALEM_KOK="$T" bash "$B/hf-onizle-hazirla.sh" p2 2>&1)
p2_kod=$?
set -e
sina "hatalı sahne çıkış 1" "$p2_kod" "1"
sina "hatalı sahne sonuç satırı" "$(echo "$p2_cikti" | grep -c '^SONUÇ hazırlanan 1 · hatalı 1$')" "1"
sina "hatalı sahne listelendi" "$(echo "$p2_cikti" | grep -c 'Hatalı sahne: p2/02-hyperframes-hatali')" "1"

# 5. Test: normal kipte gsap oluşur
sina "normal kipte gsap oluşur" "$([ -f "$T/projeler/p2/sahneler/01-hyperframes-eksik/proje/lib/gsap.min.js" ] && echo 1 || echo 0)" "1"

# 6. Test: ONIZLE_YALNIZ=1 geçer
onizle_val=$(cat "$T/projeler/p2/sahneler/01-hyperframes-eksik/onizle_yalniz.val" 2>/dev/null || echo "")
sina "ONIZLE_YALNIZ=1 geçer" "$onizle_val" "1"

# 7. Test: gsap'lı sahne koşmaz
sina "gsap'lı sahne koşmaz" "$([ -f "$T/projeler/p1/sahneler/01-hyperframes-var/kosmamali.log" ] && echo 1 || echo 0)" "0"

# 8. Test: İkinci koşu: 01 hazır olduğundan p2'de yalnız hatalı sahne koşar (hazırlanan 0)
# Hatalı sahneyi düzeltelim, ikinci koşu hazırlanan 1, sonrakinde hazırlanan 0 olsun
cat > "$T/projeler/p2/sahneler/02-hyperframes-hatali/calistir.sh" <<'EOF'
#!/bin/bash
mkdir -p proje/lib
echo x > proje/lib/gsap.min.js
exit 0
EOF
p2_duzelt_cikti=$(KALEM_KOK="$T" bash "$B/hf-onizle-hazirla.sh" p2)
sina "düzelen sahne hazırlandı" "$(echo "$p2_duzelt_cikti" | grep -c '^SONUÇ hazırlanan 1 · hatalı 0$')" "1"

# 9. Test: ikinci koşu 'hazırlanan 0'
ikinci_cikti=$(KALEM_KOK="$T" bash "$B/hf-onizle-hazirla.sh" p1 p2)
sina "ikinci koşu hazırlanan 0" "$(echo "$ikinci_cikti" | grep -c '^SONUÇ hazırlanan 0 · hatalı 0$')" "1"

# Geçici kökü temizleme: rm ile SİLME, ~/Silinecekler/ altına mv et
mkdir -p "$HOME/Silinecekler/$(date +%F)-test-hf-onizle-hazirla"
mv "$T" "$HOME/Silinecekler/$(date +%F)-test-hf-onizle-hazirla/"

echo "SONUÇ geçti $gecti kaldı $kaldi"
[ "$kaldi" -eq 0 ]
