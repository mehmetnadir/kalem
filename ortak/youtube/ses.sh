#!/bin/bash
# YouTube ortak parçaları: giriş ve çıkış sözünü ders ses zinciriyle sentezler (araclar/ses-sunucu.sh → dijital-anlatim el.py).
# Öğrenci sesi; önbellek anahtarı el.py'nin (ses metni + bağlam + ses kimliği + model + tohum + hız), Whisper kapısı el.py içinde.
#   bash ortak/youtube/ses.sh        → giris/ses/ ve cikis/ses/: sentez.wav, cumle-1.wav, sureler.json, sentez.wav.rapor.json
# ses-sunucu.sh paket dizini ister: _kok/projeler/youtube-<ad>/ortak/anlatim → <ad>/ses (simge bağı); anahtar ortamını araç kendisi okur.
set -euo pipefail
Y="$(cd "$(dirname "$0")" && pwd)"
K="$(cd "$Y/../.." && pwd)"
ANA="$K/projeler/02-04-ydt-temel/ortak/anlatim/senaryo.json"
oku() { /usr/bin/python3 -I -c 'import json,sys; print(json.load(open(sys.argv[1]))["sesler"]["ogrenci"])' "$1"; }
OGR="$(oku "$ANA")"
for ad in giris cikis; do
  [ "$(oku "$Y/$ad/ses/senaryo.json")" = "$OGR" ] || { echo "HATA: $ad öğrenci sesi ana dersle aynı değil" >&2; exit 1; }
  mkdir -p "$Y/_kok/projeler/youtube-$ad/ortak"
  ln -sfn "../../../../$ad/ses" "$Y/_kok/projeler/youtube-$ad/ortak/anlatim"
  echo "== $ad $(date +%H:%M:%S)"
  bash "$K/araclar/ses-sunucu.sh" --kok "$Y/_kok" "youtube-$ad" "$OGR"
done
