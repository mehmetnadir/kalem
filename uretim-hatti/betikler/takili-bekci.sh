#!/bin/bash
# takili-bekci.sh — başsız oturumların kendi komut satırını eşleyen "until … pgrep -f" beklemelerini çözer (srv21, sef; 15.11).
# Kural: bekleyen bash 60 sn'den yaşlıysa ve KENDİ üst oturumunun (aynı claude süreci) agy-filo süreci yoksa bekleyeni kapatır;
# kendi agy'si sürüyorsa 1500 sn'ye kadar bekler. Yalnız sef'in bash süreçleri, PID ile. Günlük takili-bekci.log. En çok 6 saat koşar.
D="$HOME/is/uretim-0204"; L="$D/takili-bekci.log"
setsid bash -c '
  L="$1"; son=$(( $(date +%s) + 21600 )); KALIP="until .*pgr""ep -f"
  echo "$(date +%H:%M:%S) bekçi başladı $$" >> "$L"
  while [ "$(date +%s)" -lt "$son" ]; do
    for p in $(pgrep -u "$(id -u)" -f "$KALIP"); do
      [ "$p" = "$$" ] && continue
      [ "$(ps -o comm= -p "$p" 2>/dev/null)" = bash ] || continue
      yas=$(ps -o etimes= -p "$p" 2>/dev/null | tr -d " "); [ -n "$yas" ] || continue
      ust=$(ps -o ppid= -p "$p" 2>/dev/null | tr -d " "); [ -n "$ust" ] || continue
      gercek=0
      for q in $(pgrep -u "$(id -u)" -x agy-filo); do
        a1=$(ps -o ppid= -p "$q" 2>/dev/null | tr -d " "); a2=$(ps -o ppid= -p "${a1:-0}" 2>/dev/null | tr -d " ")
        { [ "$a1" = "$ust" ] || [ "$a2" = "$ust" ]; } && gercek=$((gercek+1))
      done
      if { [ "$gercek" -eq 0 ] && [ "$yas" -gt 60 ]; } || [ "$yas" -gt 1500 ]; then
        kill "$p" 2>/dev/null && echo "$(date +%H:%M:%S) kapatıldı pid $p yaş $yas üst $ust agy $gercek" >> "$L"
      fi
    done
    sleep 45
  done
' _ "$L" < /dev/null > /dev/null 2>&1 &
echo "bekçi başlatıldı"
