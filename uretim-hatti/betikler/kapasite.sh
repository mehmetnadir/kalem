#!/bin/bash
# kapasite.sh — srv21 anlık şerit kapasitesi (salt okur; Nadir 15.11: "kaç ajan çalıştırabilir bulsun").
# Çıktı tek satır: aktif yuk cekirdek bosG oturumCpu oturumG ek sinir hata takili
#   aktif     = ~sef/is/uretim-0204/*.durum içinde "calisiyor <pid>" ve pid canlı (kuyruk-* ve render-* sayılmaz)
#   oturumCpu = yük / aktif (0,3–2 arası), oturumG = sef süreçlerinin toplam RSS'i / aktif (0,5–4 arası)
#   ek        = açılabilecek ek şerit = min((çekirdek×0,8 − yük)/oturumCpu, (boş bellek − 8 G)/oturumG), 0–40
#   hata      = son 30 dk içinde hatayla biten oturum sayısı (is_error true)
D=/home/sef/is/uretim-0204
A=0
for f in "$D"/*.durum; do
  [ -e "$f" ] || continue
  case "$(basename "$f")" in kuyruk-*|render-*) continue ;; esac
  read -r durum pid < "$f"
  [ "$durum" = calisiyor ] && [ -n "$pid" ] && [ -d "/proc/$pid" ] && A=$((A+1))
done
C=$(nproc)
Y=$(cut -d' ' -f1 /proc/loadavg)
BOS=$(awk '/MemAvailable/{printf "%.1f", $2/1048576}' /proc/meminfo)
RSS=$(ps -u sef -o rss= | awk '{s+=$1} END{printf "%.1f", s/1048576}')
HATA=$(find "$D" -maxdepth 1 -name '*.json' -mmin -30 -exec grep -l '"is_error":true' {} + 2>/dev/null | wc -l)
# takılı = kendi komut satırını eşleyen "until … pgrep -f" beklemesi 5 dk'yı geçmiş oturum (15.11: W-06 21 dk bekledi)
TAKILI=0
for p in $(pgrep -u sef -f 'until .*pgrep -f'); do
  [ "$(ps -o comm= -p "$p" 2>/dev/null)" = bash ] || continue   # istem metninde geçen kalıp (claude süreci) sayılmaz
  [ "$(ps -o etimes= -p "$p" 2>/dev/null | tr -d ' ')" -gt 300 ] 2>/dev/null && TAKILI=$((TAKILI+1))
done
awk -v takili="$TAKILI" -v a="$A" -v y="$Y" -v c="$C" -v bos="$BOS" -v rss="$RSS" -v hata="$HATA" 'BEGIN{
  # az şeritte bölme yanıltır (sabit süreçler tek oturuma yazılır): 4 şeridin altında ölçülmüş sabitler (15.11: 0,6 çekirdek, 1 G)
  cpu = (a>=4) ? y/a : 0.6; if (cpu<0.3) cpu=0.3; if (cpu>2) cpu=2
  mem = (a>=4) ? rss/a : 1.0; if (mem<0.5) mem=0.5; if (mem>4) mem=4
  ec = (c*0.8 - y)/cpu; em = (bos - 8)/mem
  ek = (ec<em) ? ec : em; sinir = (ec<em) ? "cpu" : "bellek"
  if (ek<0) ek=0; if (ek>40) ek=40
  printf "%d %s %d %s %.2f %.2f %d %s %d %d\n", a, y, c, bos, cpu, mem, int(ek), sinir, hata, takili
}'
