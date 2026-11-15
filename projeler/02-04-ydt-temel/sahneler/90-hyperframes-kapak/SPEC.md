# SPEC — sahne 90-hyperframes-kapak · ana ders kapağı (02-04-ydt-temel ve -dikey, durağan tek kare)

> **16.11 DUZ3:** kapak yazısı «HER ZAMAN mı / ŞİMDİ mi?» → «KALICI mı / GEÇİCİ mi?» (KS-4 + EK-5c, 4 sözcük); dikey yazı tavanı 140 px; nesne sığmayan aday reddedilir. Bu belgedeki saniye ve metinler önceki sürümündür; geçerli olan kod + `zaman.json`.

Standart: `dijital-anlatim/.claude/docs/kapak-standardi.md` v1. İstem KAPAK-0204 (15.11.2026). `zaman.json` `sahneler[]` dışı; ses ve mp4 yok.
Kalıp: `02-04-ydt-temel-s1/sahneler/05-hyperframes-kapak-b/` (yazı tipi yükleme, `hf_tema.py`, `tema_bitir`, snapshot).

| Dosya | İş |
|---|---|
| `uret.py` | iki pakette birebir aynı; biçim paket adından (`-dikey` → 1080×1920, öteki 1920×1080). `proje/index.html`, `proje/assets/` (logo-acik/koyu.svg, temizlenmiş karakter/nesne PNG), `nesneler.json` yazar |
| `calistir.sh` | iki pakette aynı; `--tema acik|koyu` → paket kökü `kapak.png` / `kapak-koyu.png`; eski kök PNG `~/Silinecekler/<tarih>-kapak/` altına |
| `yardim.py` | kalıp kopyası; yalnız `genislik`, `font_css`, `font_kopyala`, `LOGO_EN_BOY` kullanılır |

- Metin (şef kararı): `HER ZAMAN mı` · vurgu kutusu `ŞİMDİ mi?` (S1 × 1,35 yatay, × 1,2 dikey) · Lexend `I live · I am living` · çizgi rozet `YDT · TEMEL`.
- Renk: koyu `#141414` zemin, krem yazı, sarı kutu; açık (`#root.tema-acik`) sarı `#fece00` zemin, siyah yazı, siyah kutu + krem yazı, karakter arkasında krem daire.
  Açık temada logo `yds-publishing-seffaf.svg`'nin tek renk `#141414` türevi (sarı zeminde "yds" kaybolur).
- Çıkartma kenarı: 10 px krem, 4 yönlü CSS drop-shadow, 3 geçiş × 3,33 px (tek 10 px adım ok uçlarında basamak bırakır).
- Görsel kopyası: alfa ≤ 64 ve 3×3 açılışta düşen kırıntı sıfırlanır (kaynak `ortak/kapak/` değişmez).
- Yerleşim araması: karakter ölçeği 1,00'dan aşağı; yatayda yazı bloğu ortadan yukarı, dikeyde karakter ortadan sağa kayar; ilk kuralsız düzen seçilir.
  Yatay: yazı sol %55, karakter bel üstü alt kenarda sağa yaslı, tabela başın sağında. Dikey: yazı 408'den, karakter alt %20 sınırında, tabela başın solunda.
- Kurallar (`dogrula`): yazı kutusu ile görsel arası ≥ 34 px; nesne–karakter arası ≥ 24 px; daire yazıdan ≥ 24 px; yatay sağ alt %15×%8 ve dikey üst/alt %20
  görselsiz ve yazısız; yüz üst yarıda (yatay); görseller kenar payı içinde; ana yazı ≥ 120 px (dikey ≥ 110).
- Kullanım: `bash calistir.sh --tema acik` ve `--tema koyu`. `ONIZLE_YALNIZ=1 bash calistir.sh` yalnız `proje/index.html`.
