#!/bin/bash
# kuyruk-yonet.sh <liste dosyası> — satır: <ad> <model> [zincir-model zincir-ad…]
# En çok ESZ (varsayılan 5) iş aynı anda; yeni iş yalnız yük1 < 14 ve MemAvailable > 14 GB iken başlar (16.11 OOM dersi).
# Her iş için istem = [ön not, ONNOT=0 ile kapanır] + makine notu + uretim-hatti/istemler/<ad>.md → ~/is/uretim-0204/istem-<ad>.md
R="$HOME/is/uretim-0204"; K="$HOME/01dev/_worktrees/kalem-0204"; I="$K/uretim-hatti/istemler"; ESZ="${ESZ:-5}"
LISTE="$1"; GUNLUK="$R/kuyruk-yonet.log"
calisan() { local n=0; while read -r ad _; do case "$(cat "$R/$ad.durum" 2>/dev/null)" in calisiyor*) n=$((n+1)) ;; esac; done < "$LISTE"; echo $n; }
while read -r ad model zincir <&3; do
  [ -n "$ad" ] || continue
  while :; do
    yuk=$(cut -d' ' -f1 /proc/loadavg | cut -d. -f1); bos=$(awk '/MemAvailable/ {print int($2/1048576)}' /proc/meminfo)
    [ "$(calisan)" -lt "$ESZ" ] && [ "$yuk" -lt 14 ] && [ "$bos" -gt 14 ] && break
    sleep 30
  done
  {
    if [ "${ONNOT:-1}" = 1 ]; then
      printf 'ÖN NOT (16.11): bu iş daha önce başladı ve makine bellek arızasıyla yarıda kesildi. Paketlerde yarım değişiklik olabilir: önce `git -C %s status --short -- <paket>` ve `git diff --stat` ile paketin durumunu, varsa rapor taslağını (`uretim-tutanagi/DUZ*-RAPOR.md`) oku. Yapılmış işi yineleme; eksik kalanı tamamla ve her şeyi yeniden doğrula.\n\n' "$K"
    fi
    printf 'MAKİNE NOTU: `el.py` makinede aynı anda en çok 2 koşar: "yuva bekleniyor" satırı olağandır; ses komutunu ön planda `timeout 1500` ile koştur, aynı anda ikinci bir `el.py` başlatma. Kare çekimini sahne sahne yap; aynı anda birden çok başsız tarayıcı açma. `surumler.json` revizyon notu (`degisiklik`) en çok 500 karakter, `no` alanı `r<sayı>` (panel şeması); ayrıntı rapora yazılır. Düzeltme raporunun ilk satırına `uretici_model: <model>` yaz.\n\n'
    cat "$I/$ad.md"
  } > "$R/istem-$ad.md"
  bash "$R/kos.sh" "$ad" "$model" "$R/istem-$ad.md" >> "$GUNLUK" 2>&1
  if [ -n "$zincir" ]; then set -- $zincir; zm="$1"; shift; bash "$K/uretim-hatti/betikler/sonra-m.sh" "$ad" "$zm" "$I" "$@" >> "$GUNLUK" 2>&1; fi
  echo "$(date +%H:%M:%S) başlatıldı $ad (yük $yuk, boş $bos G)" >> "$GUNLUK"
  sleep 45
done 3< "$LISTE"
echo "$(date +%H:%M:%S) liste bitti" >> "$GUNLUK"
