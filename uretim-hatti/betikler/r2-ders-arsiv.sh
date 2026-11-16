#!/bin/bash
# r2-ders-arsiv.sh — ders paketini R2'ye arşivler, denetim GEÇTİYSE git dışı ağır çıktıyı sunucudan budar.
# Neden (Nadir 16.11): "bu denemeler ve üretimlerin tamamına ait veriler hep r2'de tutulmalı, srv21 diskinde
# minimum düzeyde yük bindirmeliyiz." 600 ders × yüzlerce MB git dışı çıktı diske sığmaz.
#
#   r2-ders-arsiv.sh [--kume <ad>] [--budama] [--kuru] <paket-dizini>...
#
# Her paket: r2-arsiv.sh yukle → r2-arsiv.sh denetle → (--budama ve GEÇTİ ise) budama.
# Budama YALNIZ git'in yok saydığı (status --ignored `!!`) ve uzantısı mp4|wav|m4a|mov|png|webm olan DOSYALARI siler.
# Git'te izlenen dosyaya, .git'e, uzantısı listede olmayan dosyaya, bağa dokunmaz. Silinen her dosya
# `yol<TAB>bayt<TAB>sha256` olarak $R2_DERS_BUDAMA_DIZIN/<paket>-<zaman>.tsv manifestine yazılır
# (varsayılan /home/sef/is/r2-budama). Toplam bayt ekrana ve $R2_ARSIV_KAYIT jsonl'ine ("islem":"budama") düşer.
# --kuru: yüklemez, silmez; yüklenecek paketi + budanacak dosyaları + toplam baytı basar.
# Test: R2_DERS_ARSIV_ARAC (r2-arsiv.sh yerine koşacak araç). bash 3.2 uyumlu (Mac testi).
set -euo pipefail
BU="$(cd "$(dirname "$0")" && pwd)"
ARAC="${R2_DERS_ARSIV_ARAC:-$BU/r2-arsiv.sh}"
KAYIT="${R2_ARSIV_KAYIT:-/home/sef/is/r2-arsiv.jsonl}"
MANIFEST_DIZIN="${R2_DERS_BUDAMA_DIZIN:-/home/sef/is/r2-budama}"
kume="kalem-$(date +%Y%m)"; budama=0; kuru=0; paketler=()

while [ $# -gt 0 ]; do
  case "$1" in
    --kume) [ $# -ge 2 ] || { echo "HATA: --kume değer ister" >&2; exit 2; }; kume="$2"; shift 2 ;;
    --budama) budama=1; shift ;;
    --kuru) kuru=1; shift ;;
    --) shift; while [ $# -gt 0 ]; do paketler+=("$1"); shift; done ;;
    -*) echo "HATA: bilinmeyen seçenek: $1" >&2; exit 2 ;;
    *) paketler+=("$1"); shift ;;
  esac
done
case "$kume" in *[!a-z0-9._-]*|"") echo "HATA: küme adı yalnız a-z 0-9 . _ - olur: '$kume'" >&2; exit 2 ;; esac
[ "${#paketler[@]}" -gt 0 ] || { echo "kullanım: $0 [--kume <ad>] [--budama] [--kuru] <paket-dizini>..." >&2; exit 2; }

sha() { if command -v sha256sum >/dev/null 2>&1; then sha256sum "$1" | cut -d' ' -f1; else shasum -a 256 "$1" | cut -d' ' -f1; fi; }
boyut() { wc -c < "$1" | tr -d ' '; }
kucuk() { printf '%s' "$1" | tr 'A-Z' 'a-z'; }
json() { printf '%s' "$1" | sed 's/\\/\\\\/g; s/"/\\"/g'; }
kaydet() { mkdir -p "$(dirname "$KAYIT")"; printf '%s\n' "$1" >> "$KAYIT"; }
simdi() { date -Is 2>/dev/null || date +%Y-%m-%dT%H:%M:%S; }

uygun() {  # uygun <dosya> → uzantı listede mi
  case "$(kucuk "${1##*.}")" in mp4|wav|m4a|mov|png|webm) return 0 ;; esac
  return 1
}

# Budanacak dosyaları NUL ayraçlı yazar: budanacak <paket> <çıktı dosyası>
budanacak() {
  local paket="$1" cikti="$2" kok kayit yol tam f
  kok=$(git -C "$paket" rev-parse --show-toplevel) || return 1
  : > "$cikti"
  git -C "$paket" status --ignored --porcelain -z -- . > "$cikti.st" || return 1
  while IFS= read -r -d '' kayit; do
    [ "${kayit:0:2}" = '!!' ] || continue
    yol="${kayit:3}"; tam="$kok/${yol%/}"
    if [ -d "$tam" ] && [ ! -L "$tam" ]; then
      while IFS= read -r -d '' f; do
        uygun "$f" || continue
        if git -C "$kok" ls-files --error-unmatch -- "$f" >/dev/null 2>&1; then continue; fi  # izlenen: dokunma
        printf '%s\0' "$f" >> "$cikti"
      done < <(find "$tam" -name .git -prune -o -type f -print0)
    elif [ -f "$tam" ] && [ ! -L "$tam" ] && uygun "$tam"; then
      printf '%s\0' "$tam" >> "$cikti"
    fi
  done < "$cikti.st"
  rm -f "$cikti.st"
}

hata=0
for paket in "${paketler[@]}"; do
  paket="${paket%/}"; ad="$(basename "$paket")"
  if [ ! -d "$paket" ]; then echo "HATA $paket dizin yok"; hata=$((hata + 1)); continue; fi
  if ! git -C "$paket" rev-parse --show-toplevel >/dev/null 2>&1; then
    echo "HATA $paket git çalışma ağacında değil"; hata=$((hata + 1)); continue
  fi
  g=$(mktemp -d "${TMPDIR:-/var/tmp}/r2-ders-arsiv.XXXXXX")
  if [ "$kuru" = 1 ]; then
    echo "KURU yüklenecek: $paket → $kume/$ad.tar.zst.enc"
    if [ "$budama" = 1 ]; then
      if ! budanacak "$paket" "$g/liste"; then
        echo "HATA $paket git durumu okunamadı"; hata=$((hata + 1)); rm -rf "$g"; continue
      fi
      n=0; toplam=0
      while IFS= read -r -d '' f; do
        b=$(boyut "$f"); n=$((n + 1)); toplam=$((toplam + b)); printf 'KURU budanacak: %s\t%s\n' "$f" "$b"
      done < "$g/liste"
      echo "KURU ARŞİV+BUDAMA $paket $n dosya $toplam"
    else
      echo "KURU ARŞİV $paket"
    fi
    rm -rf "$g"; continue
  fi

  if ! bash "$ARAC" yukle --kume "$kume" "$paket" > "$g/yukle.log" 2>&1; then
    cat "$g/yukle.log" >&2; echo "HATA $paket yükleme başarısız"; hata=$((hata + 1)); rm -rf "$g"; continue
  fi
  if ! bash "$ARAC" denetle --kume "$kume" "$paket" > "$g/denetle.log" 2>&1; then
    cat "$g/denetle.log" >&2; echo "HATA $paket denetim KALDI (budama yok)"; hata=$((hata + 1)); rm -rf "$g"; continue
  fi
  if [ "$budama" != 1 ]; then echo "ARŞİV $paket"; rm -rf "$g"; continue; fi

  if ! budanacak "$paket" "$g/liste"; then
    echo "HATA $paket git durumu okunamadı (budama yok)"; hata=$((hata + 1)); rm -rf "$g"; continue
  fi
  zaman=$(date +%Y%m%dT%H%M%S)
  mkdir -p "$MANIFEST_DIZIN"; manifest="$MANIFEST_DIZIN/$ad-$zaman.tsv"; : > "$manifest"
  # İşaret: ayna yüklemesi (araclar/ayna-sunucu.sh) paket ağacını bütünüyle değiştirir; budanmış paket yüklenirse
  # aynadan da kare/ses düşer. Bekçi bu dosyayı görünce durur; geri yüklemeden sonra işaret kaldırılır.
  printf 'küme=%s\nmanifest=%s\nzaman=%s\ngeri: r2-arsiv.sh geri --kume %s %s <hedef>\n' \
    "$kume" "$manifest" "$zaman" "$kume" "$ad" > "$paket/R2-BUDANDI.txt"
  n=0; toplam=0; sil_hata=0
  while IFS= read -r -d '' f; do
    b=$(boyut "$f"); s=$(sha "$f")
    printf '%s\t%s\t%s\n' "$f" "$b" "$s" >> "$manifest"   # önce manifest, sonra silme
    if rm -f -- "$f"; then n=$((n + 1)); toplam=$((toplam + b)); else sil_hata=$((sil_hata + 1)); fi
  done < "$g/liste"
  if [ "$sil_hata" = 0 ]; then sonuc=ok; else sonuc=silme-hatasi; fi
  kaydet "{\"zaman\":\"$(simdi)\",\"islem\":\"budama\",\"yerel\":\"$(json "$paket")\",\"kume\":\"$kume\",\"dosya\":$n,\"bayt\":$toplam,\"manifest\":\"$(json "$manifest")\",\"sonuc\":\"$sonuc\"}"
  if [ "$sil_hata" != 0 ]; then echo "HATA $paket $sil_hata dosya silinemedi"; hata=$((hata + 1)); rm -rf "$g"; continue; fi
  echo "ARŞİV+BUDAMA $paket $n dosya $toplam"
  rm -rf "$g"
done
[ "$hata" -eq 0 ] || exit 1
