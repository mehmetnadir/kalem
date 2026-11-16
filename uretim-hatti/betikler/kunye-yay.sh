#!/bin/bash
# kunye-yay.sh [--kuru] [paket…] — D-0392 künye 30 px düzeltmesini yatay ders paketlerine yayar (srv21, sef; 16.11).
#   D-0391 (soluk yanlış işareti) D-0415 ile geri alındı: renk satırlarına dokunulmaz.
#   D-0392 (yalnız yatay ders şablonu): künye yazısı 30 px — kunye.js seviye/bölüm/ajanda 30, ajanda noktası yazı boyuna göre;
#     HyperFrames yardim.py ajanda/seviye/bölüm 30 px, ajanda genişliği 30 px ile ölçülür, nokta cy 1019,5.
# Dikey ve kısa paketlerde künye ölçüsü ayrıdır (taban 50 / huni-v2): eşleşmeyen satıra dokunulmaz.
# Paket verilmezse K/projeler altındaki bütün paketler. Ders zincirinin boş olduğunu ÇAĞIRAN denetler (durum adları paket değil kod taşır).
# Kaynak değişir; k/ kareleri ve mp4 bayatlar ("render sonrası" etiketi). Render bu betiğin işi değildir.
# --renksiz: geriye uyum için kabul edilir, etkisizdir (renk kısmı D-0415 ile kalktı).
set -uo pipefail
KURU=0
while [ $# -gt 0 ]; do
  case "$1" in --kuru) KURU=1; shift ;; --renksiz) shift ;; *) break ;; esac
done
K="${KALEM_KOK:-$HOME/01dev/_worktrees/kalem-0204}"
if [ $# -gt 0 ]; then PAKETLER=("$@"); else PAKETLER=(); for d in "$K"/projeler/*/; do PAKETLER+=("$(basename "$d")"); done; fi
degisen=0
for pa in "${PAKETLER[@]}"; do
  P="$K/projeler/$pa"; [ -d "$P" ] || continue
  dosyalar=(); [ -f "$P/ortak/kunye.js" ] && dosyalar+=("$P/ortak/kunye.js")
  for y in "$P"/sahneler/*/yardim.py; do [ -f "$y" ] && dosyalar+=("$y"); done
  [ ${#dosyalar[@]} -gt 0 ] || continue
  once=$(cat "${dosyalar[@]}" | md5sum | cut -c1-8)
  if [ "$KURU" -eq 1 ]; then
    desen='bolumYazi: 24, ajandaYazi: 20|seviyeYazi: 22,|genislik\("Lexend", 500, ad, 20\)|cy="1023" r="4"'
    n=$(grep -cE "$desen" "${dosyalar[@]}" | awk -F: '{s+=$NF} END {print s+0}')
    echo "$pa: değişecek satır $n"; continue
  fi
  if [ -f "$P/ortak/kunye.js" ] && grep -q 'bolumYazi: 24, ajandaYazi: 20' "$P/ortak/kunye.js"; then
    sed -i -e 's/bolumYazi: 24, ajandaYazi: 20/bolumYazi: 30, ajandaYazi: 30/' -e 's/seviyeYazi: 22,/seviyeYazi: 30,/' \
      -e 's/ctx.arc(x - w - 12, k.altTaban - 7, 4,/ctx.arc(x - w - 12, k.altTaban - Math.round(k.ajandaYazi * 0.35), 4,/' "$P/ortak/kunye.js"
  fi
  for y in "$P"/sahneler/*/yardim.py; do
    [ -f "$y" ] && grep -q 'genislik("Lexend", 500, ad, 20)' "$y" || continue
    sed -i -e 's/genislik("Lexend", 500, ad, 20)/genislik("Lexend", 500, ad, 30)/; s/(Lexend 500 20)/(Lexend 500 30)/' \
      -e 's/font-size="20">%s<\/text><circle/font-size="30">%s<\/text><circle/' \
      -e "s/font-size=\"20\">%s<\/text>'/font-size=\"30\">%s<\/text>'/" \
      -e 's/font-weight="500" font-size="22" /font-weight="500" font-size="30" /' \
      -e "s/font-size=\"24\" fill=\"%s\">%s<\/text>'/font-size=\"30\" fill=\"%s\">%s<\/text>'/" \
      -e 's/font-size="24" fill="%s" style="opacity:0"/font-size="30" fill="%s" style="opacity:0"/' \
      -e 's/cy="1023" r="4"/cy="1019.5" r="4"/' "$y"
  done
  sonra=$(cat "${dosyalar[@]}" | md5sum | cut -c1-8)
  [ "$once" != "$sonra" ] && { degisen=$((degisen + 1)); echo "$pa: değişti ($once → $sonra)"; }
done
echo "SONUÇ değişen paket $degisen"
