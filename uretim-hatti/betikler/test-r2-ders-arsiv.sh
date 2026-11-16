#!/bin/bash
# test-r2-ders-arsiv.sh — r2-ders-arsiv.sh sınaması. Sahte araçlı testler Mac/Linux; uçtan uca test gerçek r2-arsiv.sh ister.
# R2_DERS_BETIK ile sınanan betik ezilebilir (mutasyon kanıtı için).
set -uo pipefail
BU="$(cd "$(dirname "$0")" && pwd)"
B="${R2_DERS_BETIK:-$BU/r2-ders-arsiv.sh}"
T="$(mktemp -d "${TMPDIR:-/tmp}/r2-ders-test.XXXXXX")"
export R2_ARSIV_KAYIT="$T/kayit.jsonl" R2_DERS_BUDAMA_DIZIN="$T/manifest"
gecti=0; kaldi=0; atlandi=""
sina() { if [ "$2" = "$3" ]; then gecti=$((gecti + 1)); echo "GEÇTİ $1"; else kaldi=$((kaldi + 1)); echo "KALDI $1: beklenen [$3] gelen [$2]"; fi; }
var() { if test -e "$1"; then echo var; else echo yok; fi; }
sha() { if command -v sha256sum >/dev/null 2>&1; then sha256sum "$1" | cut -d' ' -f1; else shasum -a 256 "$1" | cut -d' ' -f1; fi; }

paket_kur() {  # paket_kur <kök> → <kök>/paket
  local k="$1" p="$1/paket"
  mkdir -p "$p/k" "$p/ortak/anlatim" "$p/_is"
  git -C "$k" init -q . 2>/dev/null; git -C "$k" config user.email t@t; git -C "$k" config user.name t
  printf 'bir\n' > "$p/a.txt"; head -c 3000 /dev/urandom > "$p/k/izli.png"
  printf 'cikti.mp4\nortak/anlatim/ses.wav\nnotlar.log\n_is/\n' > "$p/.gitignore"
  head -c 5000 /dev/urandom > "$p/cikti.mp4"; head -c 7000 /dev/urandom > "$p/ortak/anlatim/ses.wav"
  printf 'log\n' > "$p/notlar.log"; head -c 900 /dev/urandom > "$p/_is/x.png"
  git -C "$k" add -A . >/dev/null 2>&1; git -C "$k" commit -qm t >/dev/null 2>&1
}
durum() { echo "$(var "$1/cikti.mp4")$(var "$1/ortak/anlatim/ses.wav")$(var "$1/_is/x.png")"; }

# sahte araç: günlük tutar; yukle 0, denetle $SAHTE_DENETLE
cat > "$T/sahte.sh" <<'S'
#!/bin/bash
echo "$1" >> "$SAHTE_GUNLUK"
case "$1" in yukle) exit 0 ;; denetle) exit "${SAHTE_DENETLE:-0}" ;; esac
S
chmod +x "$T/sahte.sh"
export R2_DERS_ARSIV_ARAC="$T/sahte.sh" SAHTE_GUNLUK="$T/gunluk"

# 1) --kuru
mkdir -p "$T/k1"; paket_kur "$T/k1"; : > "$SAHTE_GUNLUK"
bash "$B" --kuru --budama "$T/k1/paket" > "$T/o1" 2>&1; sina "kuru çıkış" "$?" "0"
sina "kuru: hiçbir şey silinmedi" "$(durum "$T/k1/paket")" "varvarvar"
sina "kuru: 3 dosya listelendi" "$(grep -c '^KURU budanacak' "$T/o1")" "3"
sina "kuru: toplam bayt" "$(grep -o 'dosya [0-9]*$' "$T/o1")" "dosya 12900"
sina "kuru: araç çağrılmadı" "$(wc -c < "$SAHTE_GUNLUK" | tr -d ' ')" "0"
sina "kuru: işaret yok" "$(var "$T/k1/paket/R2-BUDANDI.txt")" "yok"

# 2) --budama başarılı
mkdir -p "$T/k2"; paket_kur "$T/k2"; : > "$SAHTE_GUNLUK"; export SAHTE_DENETLE=0
sha_m=$(sha "$T/k2/paket/cikti.mp4")
bash "$B" --budama --kume deneme "$T/k2/paket" > "$T/o2" 2>&1; sina "budama çıkış" "$?" "0"
sina "budama: 3 dosya silindi" "$(durum "$T/k2/paket")" "yokyokyok"
sina "budama: izlenenler ve .log kaldı" "$(var "$T/k2/paket/a.txt")$(var "$T/k2/paket/k/izli.png")$(var "$T/k2/paket/notlar.log")$(var "$T/k2/paket/.gitignore")" "varvarvarvar"
sina "budama: sonuç satırı" "$(grep -c '^ARŞİV+BUDAMA .*/paket 3 dosya 12900$' "$T/o2")" "1"
m=$(ls "$T/manifest"/paket-*.tsv 2>/dev/null | head -1)
sina "manifest 3 satır" "$(wc -l < "$m" | tr -d ' ')" "3"
sina "manifest sha doğru" "$(grep "cikti.mp4" "$m" | cut -f3)" "$sha_m"
sina "manifest bayt doğru" "$(grep "cikti.mp4" "$m" | cut -f2)" "5000"
sina "jsonl budama satırı" "$(grep -c '"islem":"budama".*"dosya":3,"bayt":12900' "$R2_ARSIV_KAYIT")" "1"
sina "araç sırası yukle,denetle" "$(tr '\n' ',' < "$SAHTE_GUNLUK")" "yukle,denetle,"
sina "budama: işaret dosyası (ayna bekçisi için)" "$(grep -c '^küme=deneme$' "$T/k2/paket/R2-BUDANDI.txt" 2>/dev/null)" "1"

# 3) denetim kalırsa silinmez
mkdir -p "$T/k3"; paket_kur "$T/k3"; export SAHTE_DENETLE=5
bash "$B" --budama "$T/k3/paket" > "$T/o3" 2>&1; sina "denetim kaldı: çıkış ≠ 0" "$([ $? -ne 0 ] && echo evet)" "evet"
sina "denetim kaldı: hiçbir şey silinmedi" "$(durum "$T/k3/paket")" "varvarvar"
sina "denetim kaldı: HATA satırı" "$(grep -c '^HATA .*denetim KALDI' "$T/o3")" "1"
sina "denetim kaldı: işaret yok" "$(var "$T/k3/paket/R2-BUDANDI.txt")" "yok"

# 4) --budama yoksa silinmez
mkdir -p "$T/k4"; paket_kur "$T/k4"; export SAHTE_DENETLE=0
bash "$B" "$T/k4/paket" > "$T/o4" 2>&1; sina "budamasız çıkış" "$?" "0"
sina "budamasız: silinmedi" "$(durum "$T/k4/paket")" "varvarvar"
sina "budamasız: ARŞİV satırı" "$(grep -c '^ARŞİV .*/paket$' "$T/o4")" "1"

# 5) kötü paket sonrakini engellemez
mkdir -p "$T/k5"; paket_kur "$T/k5"
bash "$B" --budama "$T/yok-dizin" "$T/k5/paket" > "$T/o5" 2>&1; sina "kötü+iyi: çıkış ≠ 0" "$([ $? -ne 0 ] && echo evet)" "evet"
sina "kötü+iyi: ikinci paket budandı" "$(durum "$T/k5/paket")" "yokyokyok"

# 6) uçtan uca: gerçek r2-arsiv.sh, yerel rclone hedefi
unset R2_DERS_ARSIV_ARAC
RC=$(command -v rclone || true); ZS=$(command -v zstd || true)
if [ -z "$RC" ] || [ -z "$ZS" ] || ! du -sb "$T" >/dev/null 2>&1 || ! openssl enc -aes-256-ctr -pbkdf2 -iter 10 -pass pass:x </dev/null >/dev/null 2>&1; then
  atlandi="uçtan uca (rclone/zstd yok, GNU du -sb yok (r2-arsiv.sh Linux'a özgü) ya da openssl -pbkdf2 desteklemiyor; Linux'ta koş)"; echo "ATLANDI $atlandi"
else
  export R2_ARSIV_HEDEF="$T/uzak" R2_ARSIV_ANAHTAR="$T/anahtar" R2_ARSIV_KIMLIKSIZ=1
  head -c 48 /dev/urandom | base64 > "$R2_ARSIV_ANAHTAR"; mkdir -p "$T/uzak" "$T/k6"; paket_kur "$T/k6"
  bash "$B" --budama --kume deneme "$T/k6/paket" > "$T/o6" 2>&1; sina "e2e çıkış" "$?" "0"
  sina "e2e: nesne R2 hedefinde" "$(test -s "$T/uzak/deneme/paket.tar.zst.enc" && echo var)" "var"
  sina "e2e: budandı" "$(durum "$T/k6/paket")" "yokyokyok"
  sina "e2e: izlenenler kaldı" "$(var "$T/k6/paket/a.txt")$(var "$T/k6/paket/k/izli.png")" "varvar"
fi
echo "SONUÇ geçti $gecti kaldı $kaldi${atlandi:+ atlandı: $atlandi}"
[ "$kaldi" -eq 0 ]
