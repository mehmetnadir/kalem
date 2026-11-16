#!/bin/bash
# ders-sonraki.sh <kod> <paket> — DUZ3-<kod> ve ardından gelen DJ-<kod> hükmünü bekler; hükme göre sıradaki turu başlatır (srv21, sef):
#   hükümde "hayır" satırı varsa  DUZ3B-<kod> (sonnet; DUZ_MODEL ile ezilir) → kanıt betiği (model yok) → DJ-<kod> (sonnet)
#   yalnız "kanıt yok" varsa       kanıt betiği (model yok) → DJ-<kod> (sonnet)   [KNT oturumu 16.11 kalktı]
# Ders başına BİR kez karar verir (ikinci DJ hükmünden sonra yeni tur başlatmaz; şef okur).
# Kapasite: düzeltme / kanıt oturumu sayısı < ESZ (varsayılan 8), yük1 < 14, MemAvailable > 14 GB (16.11 OOM dersi).
# Ayrık oturumda koşar; durum ~/is/uretim-0204/sonraki-<kod>.durum.
R="$HOME/is/uretim-0204"; K="$HOME/01dev/_worktrees/kalem-0204"; I="$K/uretim-hatti/istemler"
KOD="$1"; PA="$2"; ESZ="${ESZ:-8}"
setsid bash -c '
  R="$1"; K="$2"; I="$3"; KOD="$4"; PA="$5"; ESZ="$6"
  S="$R/sonraki-$KOD.durum"; echo "bekliyor DUZ3 $$" > "$S"
  # Yalnız "bitti 0" beklenir: arızadan kalan eski "bitti 137" yeniden başlatılacak işin durumudur, karar değildir.
  until [ "$(cat "$R/DUZ3-$KOD.durum" 2>/dev/null)" = "bitti 0" ]; do sleep 30; done
  echo "bekliyor DJ $$" > "$S"
  J="$K/projeler/$PA/uretim-tutanagi/juri"
  while :; do
    h=$(ls -t "$J"/DJ-hukum-*.md 2>/dev/null | head -1)
    if [ -n "$h" ] && [ "$h" -nt "$R/DUZ3-$KOD.durum" ]; then
      case "$(cat "$R/DJ-$KOD.durum" 2>/dev/null)" in bitti*) break ;; esac
    fi
    sleep 30
  done
  # Sayım tablosunun başlık satırı ("| Bölüm | evet | hayır | kanıt yok |") hüküm satırı değildir.
  # Jüri hücreyi kalın da yazar ("| **hayır** |"; 16.11 ölçüm: son 12 DJ hükmünden 9 tanesi kalın) — ikisi de sayılır.
  hayir=$(grep -E "^\|.*\| *(\*\*)?hayır(\*\*)?( |\||\()" "$h" | grep -c -v -E "\| *(\*\*)?evet(\*\*)? *\|")
  # DUZ_MODEL (16.11): varsayılan sonnet (analiz §4: Opus DUZ3 ort. 17,23 $, Sonnet DUZ3B 1,64 $; API kredisi tek org kaldı). Opus için DUZ_MODEL=claude-opus-5-5.
  if [ "$hayir" -gt 0 ]; then ILK="DUZ3B-$KOD"; MODEL="${DUZ_MODEL:-claude-sonnet-5-5}"; else ILK="KNT-$KOD"; MODEL=claude-sonnet-5-5; fi
  GOVDE="$I/$ILK.md"
  # Elle yazılmış DUZ3B dosyası kazanır; yoksa şablon üreteci hükümden gövdeyi üretir (16.11, git dizinine yazılmaz).
  if [ ! -s "$GOVDE" ] && [ "${ILK#DUZ3B-}" != "$ILK" ]; then
    GOVDE="$R/govde-$ILK.md"
    /usr/bin/python3 -I "$K/uretim-hatti/betikler/duz-istem-uret.py" "$KOD" "$PA" --hukum "$h" > "$GOVDE" 2>> "$R/sonraki.log" || : > "$GOVDE"
  fi
  [ -s "$GOVDE" ] || { echo "bitti 91 (istem yok: $ILK)" > "$S"; exit; }
  echo "kapasite bekliyor ($ILK, hayır $hayir) $$" > "$S"
  while :; do
    sleep $((RANDOM % 25))
    n=$(grep -l "^calisiyor" "$R"/DUZ[0-9]*-*.durum "$R"/KNT-*.durum 2>/dev/null | wc -l)
    yuk=$(cut -d" " -f1 /proc/loadavg | cut -d. -f1); bos=$(awk "/MemAvailable/ {print int(\$2/1048576)}" /proc/meminfo)
    [ "$n" -lt "$ESZ" ] && [ "$yuk" -lt 14 ] && [ "$bos" -gt 14 ] && break
    sleep 30
  done
  if [ "$ILK" = "KNT-$KOD" ]; then
    bash "$K/uretim-hatti/betikler/kanit-sonra.sh" - "$PA,$PA-dikey" "DJ-$KOD" >> "$R/sonraki.log" 2>&1
    echo "bitti 0 (kanıt betiği → DJ, hayır 0)" > "$S"; exit
  fi
  {
    printf "MAKİNE NOTU: \`el.py\` makinede aynı anda en çok 2 koşar: \"yuva bekleniyor\" satırı olağandır; ses komutunu ön planda \`timeout 1500\` ile koştur, aynı anda ikinci bir \`el.py\` başlatma. Kare çekimini sahne sahne yap; aynı anda birden çok başsız tarayıcı açma. \`surumler.json\` revizyon notu (\`degisiklik\`) en çok 500 karakter, \`no\` alanı \`r<sayı>\` (panel şeması); ayrıntı rapora yazılır. Düzeltme raporunun ilk satırına \`uretici_model: <model>\` yaz.\n\n"
    cat "$GOVDE"
  } > "$R/istem-$ILK.md"
  bash "$R/kos.sh" "$ILK" "$MODEL" "$R/istem-$ILK.md" >> "$R/sonraki.log" 2>&1
  # KNT oturumu yerine kanıt betiği (16.11, K-0266): DUZ3B bitince kanıt, sonra DJ.
  bash "$K/uretim-hatti/betikler/kanit-sonra.sh" "DUZ3B-$KOD" "$PA,$PA-dikey" "DJ-$KOD" >> "$R/sonraki.log" 2>&1
  echo "$(date +%H:%M:%S) $KOD: $ILK başladı (hayır $hayir, yük $yuk, boş $bos G, çalışan $n)" >> "$R/sonraki.log"
  echo "bitti 0 ($ILK, hayır $hayir)" > "$S"
' _ "$R" "$K" "$I" "$KOD" "$PA" "$ESZ" < /dev/null > /dev/null 2>&1 &
echo "ders-sonraki: $KOD ($PA) izleniyor"
