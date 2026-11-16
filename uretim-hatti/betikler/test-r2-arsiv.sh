#!/bin/bash
# test-r2-arsiv.sh — r2-arsiv.sh'ı yerel rclone hedefiyle sınar (R2 yok, DB yok, geçici anahtar). Linux'ta koş (srv21).
set -uo pipefail
BU="$(cd "$(dirname "$0")" && pwd)"
T="$(mktemp -d "${TMPDIR:-/tmp}/r2-arsiv-test.XXXXXX")"
export R2_ARSIV_HEDEF="$T/uzak" R2_ARSIV_ANAHTAR="$T/anahtar" R2_ARSIV_KAYIT="$T/kayit.jsonl" R2_ARSIV_KIMLIKSIZ=1
head -c 48 /dev/urandom | base64 > "$R2_ARSIV_ANAHTAR"; mkdir -p "$T/uzak" "$T/yerel/paket-a/alt"
printf 'bir\n' > "$T/yerel/paket-a/a.txt"; head -c 200000 /dev/urandom > "$T/yerel/paket-a/alt/b.png"
ln -s a.txt "$T/yerel/paket-a/bag"
gecti=0; kaldi=0
sina() { if [ "$2" = "$3" ]; then gecti=$((gecti + 1)); echo "GEÇTİ $1"; else kaldi=$((kaldi + 1)); echo "KALDI $1: beklenen [$3] gelen [$2]"; fi; }
A="bash $BU/r2-arsiv.sh"
# 1) yükleme: şifreli nesne + .sha256 + kayıt; yerel dizin yerinde
$A yukle --kume deneme "$T/yerel/paket-a" > "$T/o1" 2>&1; sina "yükle çıkış" "$?" "0"
sina "nesne var" "$(test -s "$T/uzak/deneme/paket-a.tar.zst.enc" && echo var)" "var"
sina "sha yan dosyası" "$(test -s "$T/uzak/deneme/paket-a.tar.zst.enc.sha256" && echo var)" "var"
sina "kayıt dosya sayısı (2 dosya + 1 bağ)" "$(grep -o '"dosya":[0-9]*' "$R2_ARSIV_KAYIT")" '"dosya":3'
sina "yerel silinmedi" "$(test -f "$T/yerel/paket-a/a.txt" && echo var)" "var"
sina "içerik şifreli (düz metin yok)" "$(zstd -q -d -c "$T/uzak/deneme/paket-a.tar.zst.enc" 2>/dev/null | grep -c bir)" "0"
# 2) denetim geçer
$A denetle --kume deneme "$T/yerel/paket-a" > "$T/o2" 2>&1; sina "denetle çıkış" "$?" "0"
sina "denetle GEÇTİ" "$(grep -c '^GEÇTİ deneme/paket-a' "$T/o2")" "1"
# 3) geri açma birebir
$A geri --kume deneme paket-a "$T/geri" > /dev/null 2>&1; sina "geri çıkış" "$?" "0"
sina "geri birebir" "$(diff -r --no-dereference "$T/yerel/paket-a" "$T/geri/paket-a" > /dev/null && echo ayni)" "ayni"
# 4) bozulmuş nesne: denetim kalır
printf 'X' | dd of="$T/uzak/deneme/paket-a.tar.zst.enc" bs=1 seek=5000 conv=notrunc 2>/dev/null
$A denetle --kume deneme "$T/yerel/paket-a" > "$T/o4" 2>&1; sina "bozuk: çıkış 5" "$?" "5"
sina "bozuk: KALDI" "$(grep -c '^KALDI deneme/paket-a' "$T/o4")" "1"
# 5) kayıtta olmayan yükleme denetlenemez; geçersiz küme adı reddedilir
$A denetle --kume deneme "$T/yerel/yok" > /dev/null 2>&1; sina "kayıtsız: çıkış 5" "$?" "5"
$A yukle --kume "../x" "$T/yerel/paket-a" > /dev/null 2>&1; sina "küme adı: çıkış 2" "$?" "2"
# 6) parçalı okuma: küçük parça boyutuyla denetim geçer (4. test nesneyi bozdu → önce yeniden yükle)
$A yukle --kume deneme "$T/yerel/paket-a" > /dev/null 2>&1; sina "yeniden yükle çıkış" "$?" "0"
R2_ARSIV_PARCA=50000 $A denetle --kume deneme "$T/yerel/paket-a" > "$T/o6" 2>&1; sina "parçalı denetle çıkış" "$?" "0"
sina "parçalı denetle GEÇTİ" "$(grep -c '^GEÇTİ deneme/paket-a' "$T/o6")" "1"
# 7) kesintili rclone taklidi: ilk çağrıda kesilir, yeniden denemede geçer
GERCEK_RCLONE="$(command -v rclone)"
mkdir -p "$T/sahte-bin"
printf '0' > "$T/sayac"
cat << EOF > "$T/sahte-bin/rclone"
#!/bin/bash
is_cat=0
has_offset=0
for a in "\$@"; do
  [ "\$a" = "cat" ] && is_cat=1
  [ "\$a" = "--offset" ] && has_offset=1
done
if [ "\$is_cat" = 1 ] && [ "\$has_offset" = 1 ]; then
  n=\$(cat "$T/sayac" 2>/dev/null || echo 0)
  n=\$((n + 1))
  echo "\$n" > "$T/sayac"
  if [ "\$n" -eq 1 ]; then
    "$GERCEK_RCLONE" "\$@" | head -c 1000
    exit 1
  fi
fi
exec "$GERCEK_RCLONE" "\$@"
EOF
chmod +x "$T/sahte-bin/rclone"
PATH="$T/sahte-bin:$PATH" R2_ARSIV_PARCA=50000 R2_ARSIV_DENEME=3 \
  $A denetle --kume deneme "$T/yerel/paket-a" > "$T/o7" 2>&1; sina "kesintili denetle çıkış" "$?" "0"
sina "kesintili denetle GEÇTİ" "$(grep -c '^GEÇTİ deneme/paket-a' "$T/o7")" "1"
sina "kesintili sayaç >= 2" "$(( $(cat "$T/sayac") >= 2 ))" "1"
# 8) hep kesen rclone taklidi: her denemede kesilir, denetim kalır
cat << EOF > "$T/sahte-bin/rclone"
#!/bin/bash
is_cat=0
has_offset=0
for a in "\$@"; do
  [ "\$a" = "cat" ] && is_cat=1
  [ "\$a" = "--offset" ] && has_offset=1
done
if [ "\$is_cat" = 1 ] && [ "\$has_offset" = 1 ]; then
  "$GERCEK_RCLONE" "\$@" | head -c 1000
  exit 1
fi
exec "$GERCEK_RCLONE" "\$@"
EOF
chmod +x "$T/sahte-bin/rclone"
PATH="$T/sahte-bin:$PATH" R2_ARSIV_PARCA=50000 R2_ARSIV_DENEME=2 R2_ARSIV_BEKLE_TAVAN=0 \
  $A denetle --kume deneme "$T/yerel/paket-a" > "$T/o8" 2>&1; sina "hep kesen: çıkış 5" "$?" "5"
sina "hep kesen: KALDI" "$(grep -c '^KALDI deneme/paket-a' "$T/o8")" "1"
sina "hep kesen: stderr okunamadı" "$(( $(grep -c 'okunamadı' "$T/o8") >= 1 ))" "1"
echo "SONUÇ geçti $gecti kaldı $kaldi"
[ "$kaldi" -eq 0 ]
