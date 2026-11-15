#!/bin/bash
# ders-sonraki.sh <kod> <paket> — DUZ3-<kod> ve ardından gelen DJ-<kod> hükmünü bekler; hükme göre sıradaki turu başlatır (srv21, sef):
#   hükümde "hayır" satırı varsa  DUZ3B-<kod> (opus) → KNT-<kod> (sonnet) → DJ-<kod> (sonnet)
#   yalnız "kanıt yok" varsa       KNT-<kod> (sonnet) → DJ-<kod> (sonnet)
# Ders başına BİR kez karar verir (ikinci DJ hükmünden sonra yeni tur başlatmaz; şef okur).
# Kapasite: düzeltme / kanıt oturumu sayısı < ESZ (varsayılan 8), yük1 < 14, MemAvailable > 14 GB (16.11 OOM dersi).
# Ayrık oturumda koşar; durum ~/is/uretim-0204/sonraki-<kod>.durum.
R="$HOME/is/uretim-0204"; K="$HOME/01dev/_worktrees/kalem-0204"; I="$K/uretim-hatti/istemler"
KOD="$1"; PA="$2"; ESZ="${ESZ:-8}"
setsid bash -c '
  R="$1"; K="$2"; I="$3"; KOD="$4"; PA="$5"; ESZ="$6"
  S="$R/sonraki-$KOD.durum"; echo "bekliyor DUZ3 $$" > "$S"
  until case "$(cat "$R/DUZ3-$KOD.durum" 2>/dev/null)" in bitti*) true ;; *) false ;; esac; do sleep 30; done
  if [ "$(cat "$R/DUZ3-$KOD.durum")" != "bitti 0" ]; then echo "bitti 90 (DUZ3 hata)" > "$S"; exit; fi
  echo "bekliyor DJ $$" > "$S"
  J="$K/projeler/$PA/uretim-tutanagi/juri"
  while :; do
    h=$(ls -t "$J"/DJ-hukum-*.md 2>/dev/null | head -1)
    if [ -n "$h" ] && [ "$h" -nt "$R/DUZ3-$KOD.durum" ]; then
      case "$(cat "$R/DJ-$KOD.durum" 2>/dev/null)" in bitti*) break ;; esac
    fi
    sleep 30
  done
  hayir=$(grep -c -E "^\|.*\| *hayır( |\||\()" "$h")
  if [ "$hayir" -gt 0 ]; then ILK="DUZ3B-$KOD"; MODEL=claude-opus-5-5; else ILK="KNT-$KOD"; MODEL=claude-sonnet-5-5; fi
  [ -s "$I/$ILK.md" ] || { echo "bitti 91 (istem yok: $ILK)" > "$S"; exit; }
  echo "kapasite bekliyor ($ILK, hayır $hayir) $$" > "$S"
  while :; do
    sleep $((RANDOM % 25))
    n=$(grep -l "^calisiyor" "$R"/DUZ[0-9]*-*.durum "$R"/KNT-*.durum 2>/dev/null | wc -l)
    yuk=$(cut -d" " -f1 /proc/loadavg | cut -d. -f1); bos=$(awk "/MemAvailable/ {print int(\$2/1048576)}" /proc/meminfo)
    [ "$n" -lt "$ESZ" ] && [ "$yuk" -lt 14 ] && [ "$bos" -gt 14 ] && break
    sleep 30
  done
  {
    printf "MAKİNE NOTU: \`el.py\` makinede aynı anda en çok 2 koşar: \"yuva bekleniyor\" satırı olağandır; ses komutunu ön planda \`timeout 1500\` ile koştur, aynı anda ikinci bir \`el.py\` başlatma. Kare çekimini sahne sahne yap; aynı anda birden çok başsız tarayıcı açma. \`surumler.json\` revizyon notu (\`degisiklik\`) en çok 500 karakter, \`no\` alanı \`r<sayı>\` (panel şeması); ayrıntı rapora yazılır. Düzeltme raporunun ilk satırına \`uretici_model: <model>\` yaz.\n\n"
    cat "$I/$ILK.md"
  } > "$R/istem-$ILK.md"
  bash "$R/kos.sh" "$ILK" "$MODEL" "$R/istem-$ILK.md" >> "$R/sonraki.log" 2>&1
  if [ "$ILK" = "DUZ3B-$KOD" ]; then
    bash "$K/uretim-hatti/betikler/sonra-m.sh" "DUZ3B-$KOD" claude-sonnet-5-5 "$I" "KNT-$KOD" >> "$R/sonraki.log" 2>&1
  fi
  bash "$K/uretim-hatti/betikler/sonra-m.sh" "KNT-$KOD" claude-sonnet-5-5 "$I" "DJ-$KOD" >> "$R/sonraki.log" 2>&1
  echo "$(date +%H:%M:%S) $KOD: $ILK başladı (hayır $hayir, yük $yuk, boş $bos G, çalışan $n)" >> "$R/sonraki.log"
  echo "bitti 0 ($ILK, hayır $hayir)" > "$S"
' _ "$R" "$K" "$I" "$KOD" "$PA" "$ESZ" < /dev/null > /dev/null 2>&1 &
echo "ders-sonraki: $KOD ($PA) izleniyor"
