#!/bin/bash
# kanit-sonra.sh <beklenen-ad|-> <paket>[,<paket>…] <iş-adı>… — KNT oturumunun yerini alır (16.11, K-0266).
# <beklenen-ad>.durum "bitti 0" olunca (ya da "-" ise hemen) her paket için kanit-topla.mjs koşar (model yok),
# sonra her <iş-adı> için kos.sh <iş-adı> claude-sonnet-5-5 istemler/<iş-adı>.md başlatır (jüri).
# Beklenen iş hatayla biterse hiçbir şey başlatmaz. Durum: ~/is/uretim-0204/kanit-<ilk iş>.durum. Ayrık oturumda koşar.
# Kanıt betiği hata verirse jüri yine başlar: eksik kanıt KANIT.md'de "olculemedi" yazar, jüri "kanıt yok" der (§1h).
R="$HOME/is/uretim-0204"; K="$HOME/01dev/_worktrees/kalem-0204"; D="$HOME/01dev/dijital-anlatim"
I="$K/uretim-hatti/istemler"; MODEL="${JURI_MODEL:-claude-sonnet-5-5}"
BEK="$1"; PAKETLER="$2"; shift 2
[ $# -gt 0 ] || { echo "kullanım: kanit-sonra.sh <beklenen-ad|-> <paket,…> <iş-adı>…" >&2; exit 1; }
setsid bash -c '
  R="$1"; K="$2"; D="$3"; I="$4"; MODEL="$5"; BEK="$6"; PAKETLER="$7"; shift 7
  S="$R/kanit-$1.durum"; echo "calisiyor $$" > "$S"
  if [ "$BEK" != "-" ]; then
    until case "$(cat "$R/$BEK.durum" 2>/dev/null)" in bitti*) true ;; *) false ;; esac; do sleep 20; done
    if [ "$(cat "$R/$BEK.durum")" != "bitti 0" ]; then echo "bitti 90 ($BEK hatalı)" > "$S"; exit; fi
  fi
  export PATH="$HOME/.local/bin:$HOME/.nvm/versions/node/v24.22.2/bin:/usr/local/bin:/usr/bin:/bin"
  hata=0
  for p in ${PAKETLER//,/ }; do
    [ -d "$K/projeler/$p" ] || { echo "$(date +%H:%M:%S) kanıt: $p yok, atlandı" >> "$R/kanit.log"; continue; }
    timeout 1500 node "$D/araclar/kanit-topla.mjs" "$K/projeler/$p" >> "$R/kanit.log" 2>&1 || hata=$((hata + 1))
  done
  for a in "$@"; do bash "$R/kos.sh" "$a" "$MODEL" "$I/$a.md" >> "$R/kanit.log" 2>&1; done
  echo "bitti 0 (kanıt hatası $hata)" > "$S"
' _ "$R" "$K" "$D" "$I" "$MODEL" "$BEK" "$PAKETLER" "$@" < /dev/null > /dev/null 2>&1 &
echo "kanit-sonra: $BEK → kanıt ($PAKETLER) → $* ($MODEL)"
