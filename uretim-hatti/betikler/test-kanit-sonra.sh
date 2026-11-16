#!/bin/bash
# test-kanit-sonra.sh — kanit-sonra.sh'ı sahte HOME'da sınar (sahte node, sahte kos.sh; model yok). Linux (setsid) ister: sunucuda koş.
set -uo pipefail
BU="$(cd "$(dirname "$0")" && pwd)"
T="$(mktemp -d "${TMPDIR:-/tmp}/kanit-sonra-test.XXXXXX")"; H="$T/home"
R="$H/is/uretim-0204"; K="$H/01dev/_worktrees/kalem-0204"
mkdir -p "$R" "$K/projeler/p1" "$K/projeler/p1-dikey" "$K/uretim-hatti/istemler" "$H/01dev/dijital-anlatim/araclar" "$H/.local/bin"
printf '#!/bin/bash\necho "node $*" >> "%s/cagri.log"\n' "$T" > "$H/.local/bin/node"; chmod +x "$H/.local/bin/node"
printf '#!/bin/bash\necho "kos $1 $2 $(basename "$3")" >> "%s/cagri.log"\n' "$T" > "$R/kos.sh"
gecti=0; kaldi=0
sina() { if [ "$2" = "$3" ]; then gecti=$((gecti + 1)); echo "GEÇTİ $1"; else kaldi=$((kaldi + 1)); echo "KALDI $1: beklenen [$3] gelen [$2]"; fi; }
bekle() { for _ in $(seq 1 60); do case "$(cat "$R/kanit-$1.durum" 2>/dev/null)" in bitti*) return ;; esac; sleep 0.25; done; }
# 1) "-": hemen; var olan iki paket için kanıt, yok olan atlanır; sonra jüri
: > "$T/cagri.log"
HOME="$H" bash "$BU/kanit-sonra.sh" - "p1,p1-dikey,yok" DJ-X1 >/dev/null; bekle DJ-X1
sina "hemen: durum" "$(cut -d' ' -f1-2 "$R/kanit-DJ-X1.durum")" "bitti 0"
sina "hemen: kanıt 2 paket" "$(grep -c '^node .*kanit-topla.mjs' "$T/cagri.log")" "2"
sina "hemen: yok paket atlandı" "$(grep -c 'projeler/yok' "$T/cagri.log")" "0"
sina "hemen: jüri sonnet ile" "$(grep '^kos' "$T/cagri.log")" "kos DJ-X1 claude-sonnet-5-5 DJ-X1.md"
sina "hemen: önce kanıt sonra jüri" "$(grep -n . "$T/cagri.log" | tail -1 | cut -d: -f2 | cut -c1-3)" "kos"
# 2) beklenen iş hatalı: hiçbir şey başlamaz
: > "$T/cagri.log"; echo "bitti 1" > "$R/DUZ3B-X2.durum"
HOME="$H" bash "$BU/kanit-sonra.sh" DUZ3B-X2 p1 DJ-X2 >/dev/null; bekle DJ-X2
sina "hatalı: durum 90" "$(cut -d' ' -f1-2 "$R/kanit-DJ-X2.durum")" "bitti 90"
sina "hatalı: çağrı yok" "$(wc -l < "$T/cagri.log" | tr -d ' ')" "0"
# 3) beklenen iş sürüyor → bitince başlar
: > "$T/cagri.log"; echo "calisiyor 1" > "$R/DUZ3B-X3.durum"
HOME="$H" bash "$BU/kanit-sonra.sh" DUZ3B-X3 p1 DJ-X3 >/dev/null; sleep 1
sina "sürüyor: henüz çağrı yok" "$(wc -l < "$T/cagri.log" | tr -d ' ')" "0"
echo "bitti 0" > "$R/DUZ3B-X3.durum"
for _ in $(seq 1 120); do case "$(cat "$R/kanit-DJ-X3.durum" 2>/dev/null)" in bitti*) break ;; esac; sleep 0.5; done
sina "sürüyor: bitince kanıt + jüri" "$(grep -c . "$T/cagri.log")" "2"
echo "SONUÇ geçti $gecti kaldı $kaldi"
[ "$kaldi" -eq 0 ]
