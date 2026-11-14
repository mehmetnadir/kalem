# Ortak tema çözücü (K19: render varsayılanı AÇIK). Her sahnenin calistir.sh'ı başta çağırır:
#   . "$(dirname "$0")/../../ortak/tema.sh" "$@"
# Sonuç değişkenleri: TEMA (acik|koyu), SORGU ("?tema=acik"), LOGO_DOSYA; işlevler tema_hf, tema_bitir.
# Seçim sırası: --tema X  >  ortam KALEM_TEMA  >  acik.
_TEMA_DIZIN="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TEMA="${KALEM_TEMA:-acik}"
_ta=("$@")
for ((_ti = 0; _ti < ${#_ta[@]}; _ti++)); do
  case "${_ta[_ti]}" in
    --tema) TEMA="${_ta[_ti + 1]:-}" ;;
    --tema=*) TEMA="${_ta[_ti]#--tema=}" ;;
  esac
done
case "$TEMA" in acik | koyu) ;; *) echo "tema acik ya da koyu olmalı: '$TEMA'" >&2; exit 2 ;; esac
SORGU="?tema=$TEMA"
LOGO_DOSYA="yds-publishing-seffaf.svg"; [ "$TEMA" = acik ] && LOGO_DOSYA="yds-publishing-lacivert.svg"
# HyperFrames sahnesinin index.html'ini temaya çevirir (render sorgu almaz, tema dosyaya gömülür).
tema_hf() { /usr/bin/python3 -I "$_TEMA_DIZIN/hf_tema.py" "$1" "$TEMA"; }
# kontrol.png'ye tema damgası, RAPOR.md'ye "Tema:" satırı (PIL kullanıcı site-packages'ta: -I yok).
# 05.11: tema başına sahne videosu saklanır (video-acik.mp4 / video-koyu.mp4); birlestir.py --tema ile seçer,
# iki tema art arda yakalanınca biri diğerini ezmez.
tema_bitir() { /usr/bin/python3 "$_TEMA_DIZIN/tema_damga.py" "$1" "$TEMA"; [ -f "$1/video.mp4" ] && cp "$1/video.mp4" "$1/video-$TEMA.mp4"; true; }
echo "tema: $TEMA" >&2
# 1 dk yük ortalaması (tam sayı): Linux /proc/loadavg, yoksa uptime (macOS "averages: 3.1 3.4" ve Linux "average: 3.10, ..." biçimleri).
yuk1() {
  if [ -r /proc/loadavg ]; then awk '{print int($1)}' /proc/loadavg
  else uptime | sed 's/.*averages*: *//' | awk '{gsub(",","",$1); print int($1)}'; fi
}
