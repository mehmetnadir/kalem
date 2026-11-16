#!/bin/bash
# r2-arsiv.sh — üretim ve deneme artıklarını YDS R2'ye (ydsdigital/uretim-arsiv/) ŞİFRELİ taşır. srv21'de root koşar.
# Neden (Nadir 16.11): "bu denemeler ve üretimlerin tamamına ait veriler hep r2'de tutulmalı, srv21 diskinde minimum
# düzeyde yük bindirmeliyiz." Kova herkese açık alan adına bağlı → içerik şifresiz YÜKLENMEZ.
# Şifre ve kimlik /root/scripts/r2-yds.sh ile aynıdır (aes-256-ctr + pbkdf2 200000, anahtar /root/.interactive-yedek.anahtar,
# kimlik r2_configs "YDS Publishing" satırı; hiçbir çıktıya düşmez). Yerel disk ara dosyası yok: tar | zstd | openssl | rcat.
#
#   r2-arsiv.sh yukle [--kume <ad>] <dizin>...   # her dizin → <kume>/<dizin adı>.tar.zst.enc (+ .sha256), boyut doğrulanır
#   r2-arsiv.sh denetle [--kume <ad>] <dizin>... # R2'den indirir, çözer; tar sha256 + dosya sayısı yüklemeyle aynı mı
#   r2-arsiv.sh geri [--kume <ad>] <ad> <hedef-dizin>   # indirir, çözer, hedef dizine açar
#   r2-arsiv.sh liste                            # öneki listeler
# Yerel dizini SİLMEZ. "denetle" GEÇTİ yazmadan yerel kopyaya dokunulmaz (silme kararı Nadir'de).
# Kayıt: $R2_ARSIV_KAYIT (varsayılan /home/sef/is/r2-arsiv.jsonl): her yükleme ve denetim bir satır.
# Test için: R2_ARSIV_HEDEF (rclone hedefi), R2_ARSIV_ANAHTAR, R2_ARSIV_KIMLIKSIZ=1 (DB okuma atlanır).
set -euo pipefail
ANAHTAR="${R2_ARSIV_ANAHTAR:-/root/.interactive-yedek.anahtar}"
HEDEF="${R2_ARSIV_HEDEF:-r2yds:ydsdigital/uretim-arsiv}"
KAYIT="${R2_ARSIV_KAYIT:-/home/sef/is/r2-arsiv.jsonl}"
R2_ID=2c449b6d-ab28-49d4-ab3f-596618db0018
BANT="${R2_ARSIV_BANT:-30M}"
SIFRE=(-aes-256-ctr -pbkdf2 -iter 200000 -pass "file:$ANAHTAR")

kimlik() {
  [ "${R2_ARSIV_KIMLIKSIZ:-}" = 1 ] && return 0
  local satir
  satir=$(mariadb --defaults-extra-file=/root/.pipeline-db.cnf -N -B -e \
    "SELECT access_key_id, secret_access_key, endpoint FROM r2_configs WHERE id='$R2_ID'" 2>/dev/null) || true
  [ -n "$satir" ] || { echo "HATA: R2 kimliği okunamadı (r2_configs $R2_ID)" >&2; exit 3; }
  export RCLONE_CONFIG_R2YDS_TYPE=s3 RCLONE_CONFIG_R2YDS_PROVIDER=Cloudflare RCLONE_CONFIG_R2YDS_NO_CHECK_BUCKET=true
  RCLONE_CONFIG_R2YDS_ACCESS_KEY_ID=$(cut -f1 <<<"$satir")
  RCLONE_CONFIG_R2YDS_SECRET_ACCESS_KEY=$(cut -f2 <<<"$satir")
  RCLONE_CONFIG_R2YDS_ENDPOINT=$(cut -f3 <<<"$satir")
  export RCLONE_CONFIG_R2YDS_ACCESS_KEY_ID RCLONE_CONFIG_R2YDS_SECRET_ACCESS_KEY RCLONE_CONFIG_R2YDS_ENDPOINT
}

uzak_boyut() {
  rclone lsjson --stat "$HEDEF/$1" 2>/dev/null | sed -n 's/.*"Size": *\([0-9]*\).*/\1/p'
}

kaydet() {  # kaydet <json satırı>
  mkdir -p "$(dirname "$KAYIT")"
  printf '%s\n' "$1" >> "$KAYIT"
  [ "$(id -u)" = 0 ] && [ -d /home/sef ] && chown sef:sef "$KAYIT" 2>/dev/null || true
}

son_kayit() {  # son_kayit <uzak ad> <alan> → son "yukle" satırındaki alan değeri
  [ -s "$KAYIT" ] || return 0
  { grep "\"islem\":\"yukle\"" "$KAYIT" | grep "\"uzak\":\"$1\"" | grep '"sonuc":"ok"' | tail -1 \
    | sed -n "s/.*\"$2\":\"\{0,1\}\([^\",}]*\).*/\1/p"; } || true
}

kume="silinecekler"
komut="${1:-}"; shift || true
if [ "${1:-}" = "--kume" ]; then kume="$2"; shift 2; fi
case "$kume" in *[!a-z0-9._-]*|"") echo "HATA: küme adı yalnız a-z 0-9 . _ - olur: '$kume'" >&2; exit 2 ;; esac
[ -s "$ANAHTAR" ] || { echo "HATA: anahtar yok: $ANAHTAR" >&2; exit 3; }

case "$komut" in
  yukle)
    [ $# -gt 0 ] || { echo "kullanım: $0 yukle [--kume <ad>] <dizin>..." >&2; exit 2; }
    kimlik
    hata=0
    for dizin in "$@"; do
      dizin="${dizin%/}"
      [ -d "$dizin" ] || { echo "HATA: dizin yok: $dizin" >&2; hata=$((hata + 1)); continue; }
      ad="$(basename "$dizin")"; uzak="$kume/$ad.tar.zst.enc"
      g=$(mktemp -d "${TMPDIR:-/var/tmp}/r2-arsiv.XXXXXX")
      dosya=$(find "$dizin" -mindepth 1 ! -type d | wc -l | tr -d ' ')  # tar -t'deki dizin dışı satır sayısı
      yerel=$(du -sb "$dizin" | cut -f1)
      bas=$(date +%s)
      # tar akışının ve şifreli akışın sha256 + boyutu yüklemeyle AYNI geçişte ölçülür (ikinci okuma yok).
      tar -C "$(dirname "$dizin")" -cf - "$ad" \
        | tee >(sha256sum | cut -d' ' -f1 > "$g/tar-sha") \
        | nice -n 10 zstd -q -3 -T2 \
        | openssl enc "${SIFRE[@]}" \
        | tee >(sha256sum | cut -d' ' -f1 > "$g/enc-sha") >(wc -c > "$g/enc-boyut") \
        | rclone rcat "$HEDEF/$uzak" --s3-chunk-size 64M --s3-upload-concurrency 4 \
            --bwlimit "$BANT" --retries 5 --low-level-retries 20
      sleep 2  # tee alt süreçleri dosyaları kapatsın
      beklenen=$(tr -d ' ' < "$g/enc-boyut"); gelen=$(uzak_boyut "$uzak")
      if [ -z "$gelen" ] || [ "$gelen" != "$beklenen" ]; then
        echo "HATA: boyut tutmadı — şifreli $beklenen, R2 ${gelen:-yok} ($uzak)" >&2
        kaydet "{\"zaman\":\"$(date -Is)\",\"islem\":\"yukle\",\"uzak\":\"$uzak\",\"sonuc\":\"boyut-hatasi\"}"
        hata=$((hata + 1)); continue
      fi
      printf '%s  %s\n' "$(cat "$g/enc-sha")" "$ad.tar.zst.enc" | rclone rcat "$HEDEF/$uzak.sha256"
      kaydet "{\"zaman\":\"$(date -Is)\",\"islem\":\"yukle\",\"uzak\":\"$uzak\",\"yerel\":\"$dizin\",\"dosya\":$dosya,\"yerel_bayt\":$yerel,\"enc_bayt\":$gelen,\"tar_sha\":\"$(cat "$g/tar-sha")\",\"enc_sha\":\"$(cat "$g/enc-sha")\",\"sure_sn\":$(( $(date +%s) - bas )),\"sonuc\":\"ok\"}"
      echo "OK $uzak dosya=$dosya yerel=$yerel şifreli=$gelen"
    done
    exit $((hata > 0 ? 4 : 0))
    ;;
  denetle)
    [ $# -gt 0 ] || { echo "kullanım: $0 denetle [--kume <ad>] <dizin>..." >&2; exit 2; }
    kimlik
    hata=0
    for dizin in "$@"; do
      dizin="${dizin%/}"; ad="$(basename "$dizin")"; uzak="$kume/$ad.tar.zst.enc"
      bek_sha=$(son_kayit "$uzak" tar_sha); bek_dosya=$(son_kayit "$uzak" dosya)
      [ -n "$bek_sha" ] || { echo "HATA: kayıtta yükleme yok: $uzak" >&2; hata=$((hata + 1)); continue; }
      g=$(mktemp -d "${TMPDIR:-/var/tmp}/r2-arsiv.XXXXXX")
      rclone cat "$HEDEF/$uzak" --bwlimit "$BANT" | openssl enc -d "${SIFRE[@]}" | zstd -q -d \
        | tee >(sha256sum | cut -d' ' -f1 > "$g/sha") | tar -tf - | grep -vc '/$' > "$g/n" || true
      sleep 2
      sha=$(cat "$g/sha"); n=$(tr -d ' ' < "$g/n")
      if [ "$sha" = "$bek_sha" ] && [ "$n" = "$bek_dosya" ]; then sonuc=gecti; else sonuc=kaldi; hata=$((hata + 1)); fi
      kaydet "{\"zaman\":\"$(date -Is)\",\"islem\":\"denetle\",\"uzak\":\"$uzak\",\"tar_sha\":\"$sha\",\"dosya\":${n:-0},\"sonuc\":\"$sonuc\"}"
      echo "$( [ "$sonuc" = gecti ] && echo GEÇTİ || echo KALDI ) $uzak dosya=$n/$bek_dosya sha=${sha:0:12}/${bek_sha:0:12}"
    done
    exit $((hata > 0 ? 5 : 0))
    ;;
  geri)
    [ $# -eq 2 ] || { echo "kullanım: $0 geri [--kume <ad>] <ad> <hedef-dizin>" >&2; exit 2; }
    kimlik
    mkdir -p "$2"
    rclone cat "$HEDEF/$kume/$1.tar.zst.enc" | openssl enc -d "${SIFRE[@]}" | zstd -q -d | tar -C "$2" -xf -
    echo "OK $2/$1"
    ;;
  liste)
    kimlik; rclone lsl "$HEDEF/"
    ;;
  *) echo "kullanım: $0 yukle|denetle [--kume <ad>] <dizin>... | geri [--kume <ad>] <ad> <hedef> | liste" >&2; exit 2 ;;
esac
