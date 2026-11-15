#!/bin/bash
# kapasite-izleyici.sh — srv21 şerit kapasitesini 60 sn'de bir ölçer, DEĞİŞİNCE tek satır basar (şefi uyandırır).
# Satır basma koşulu: ilk ölçüm · ek şerit sayısı ≥4 oynadı · ≥3 şerit boşaldı · yeni hata · kapasite 0'a indi.
# İki satır arası en az 120 sn. Ölçüm: sunucuda kapasite.sh (salt okur).
SSH="ssh -p 2222 -o BatchMode=yes -o ControlPath=none -o ConnectTimeout=8 root@10.0.0.21"
SON_EK=-99; SON_A=-99; SON_HATA=0; SON_T=0; DUSTU=0
while true; do
  S=$($SSH 'bash /home/sef/is/uretim-0204/kapasite.sh' 2>/dev/null)
  if [ -z "$S" ]; then
    DUSTU=$((DUSTU+1))
    [ "$DUSTU" -eq 5 ] && echo "KAPASİTE: srv21'e 5 ölçümdür ulaşılamıyor"
  else
    DUSTU=0
    read -r A Y C BOS CPU MEM EK SINIR HATA <<< "$S"
    SIMDI=$(date +%s)
    NEDEN=""
    if [ "$SON_EK" -eq -99 ]; then NEDEN="ilk ölçüm"
    elif [ "$HATA" -gt "$SON_HATA" ]; then NEDEN="yeni hata"
    elif [ "$EK" -eq 0 ] && [ "$SON_EK" -gt 0 ]; then NEDEN="kapasite doldu"
    elif [ "$A" -le $((SON_A-3)) ]; then NEDEN="şerit boşaldı"
    elif [ $((EK-SON_EK)) -ge 4 ] || [ $((SON_EK-EK)) -ge 4 ]; then NEDEN="kapasite değişti"
    fi
    if [ -n "$NEDEN" ] && { [ "$SON_EK" -eq -99 ] || [ $((SIMDI-SON_T)) -ge 120 ]; }; then
      MY=$(sysctl -n vm.loadavg | awk '{print $2}'); MC=$(sysctl -n hw.ncpu)
      echo "KAPASİTE ($NEDEN): srv21 aktif $A şerit · yük $Y/$C · boş bellek ${BOS}G · oturum başı ${CPU} çekirdek ${MEM}G → +$EK şerit açılabilir (sınır: $SINIR) · son 30 dk hata $HATA · Mac yük $MY/$MC"
      SON_EK=$EK; SON_A=$A; SON_HATA=$HATA; SON_T=$SIMDI
    fi
  fi
  sleep 60
done
