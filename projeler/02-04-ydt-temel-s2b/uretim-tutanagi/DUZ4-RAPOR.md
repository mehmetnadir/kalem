uretici_model: Claude Opus 5.5 (claude-opus-5-5, şef oturumu) + ajan yok

# DUZ4-0204S2 raporu — `02-04-ydt-temel-s2b` (A/B kol b, değişken `kapanis`) · J3 A sınıfı düzeltmeleri ve üretilebilir kanıtlar · 16.11.2026

| Ölçüm | Değer |
|---|---|
| Düzeltilen kusur | A1 (DK-1, sahne 02 + 03), A2 (başlık B; kol a ile eş), A9 (E6, altyazı sağ sınırı); ek: **AB-8** `02-paperjs-ornek/calistir.sh:8` kol a yolu (kapının K5 düzeltmesiyle görünür oldu) |
| Üretilen kanıt | C2 (EK-8, kontak), C3 (ST-2, `hyperframes check`), C5 (EK-12, zaman kapısı). C1 uygulanmaz (değişken `kapanis`, kol b kapak taşımaz); C4 kol a işi |
| Ses | değişmedi: 8/8 dosya sha256 önce = sonra; AB-9: `cumle-1.wav`, `cumle-2.wav` iki kolda eşit |
| Karaoke (sahne 02) | 19 kare, 19'unda çizgi doğru sözcükte; kareler kol a ile bayt aynı |
| Karaoke (sahne 03) | `karaoke` dizisi 0 → 9 öğe (= altyazı sözcük sayısı 9); 10 altyazılı karenin 10'unda çizgi doğru sözcükte |
| Altyazı en büyük x | sahne 02: 1015 → 910 · sahne 03: 963 → 936 (çizgi dahil 944) |
| AB-8 taraması | kod başvurusu 1 → 0; kalan 25 satır yorum / belge dizgisi / `kimlik` / kol eşleme kaydı |
| `diff -rq` | 161 satır; beklenmeyen **0** (§7) |
| Çakışma kapısı | çıkış 0 (01: 13 örnek, 02: 60, 08: 23, 03: 28; çakışma yok) |
| Huni kapısı | çıkış 1: 23 GEÇTİ, 2 KALDI (JR-1b beklenen, KR-1 kapı hatası), 5 ÖLÇÜLEMEDİ, 3 UYGULANMAZ; AB-1/2/3/6/8/9 ve KS-6f GEÇTİ |
| mp4 | yok |

Girdi: `uretim-hatti/raporlar/J3-OZET-1611.md` §3A, §3C.1, §3D, §5; `juri/KBJ-hukum-1611-0003.md` (E6 dahil); `DUZ2-RAPOR.md`;
`D/.claude/docs/huni-ab-sozlesme.md` §4 (tek değişken), `huni-v2-standart.md`, `juri-olcutleri.md`.
Kol a raporu (ayrıntılı yöntem, ortak kod açıklaması): `../../02-04-ydt-temel-s2/uretim-tutanagi/DUZ4-RAPOR.md`.

## 1. Düzeltmeler

| # | J3 · jüri | Dosya | Önce → sonra | Kanıt |
|---|---|---|---|---|
| 1 | A1 + A9 · DK-1, E6 (sahne 02) | `ortak/kunye.js` (kol a kopyası) | karaokesiz altyazı, en 984 / merkez 540 → `altyaziCiz { sozcukler, t }` karaoke seçeneği, en 900 / merkez 510 | §3, §4; normalleştirilmiş `diff` boş |
| 2 | A1 · DK-1 (sahne 02) | `sahneler/02-paperjs-ornek/kalem-paper.js`, `sahne-02.js` (kol a kopyası) | altyazıya sözcük zamanı geçmiyordu → `altyaziSozcuk(p)` (`sozcukler.json` + EN2 çapası) | aynı |
| 3 | A1 + A9 · DK-1, E6 (sahne 03) | `sahneler/03-hyperframes-cta/yardim.py` (kol a kopyası; iki kolda bayt aynı) | `altyazi_svg` iki değer, `x="540"` orta → üç değer + `<line id="ak…">`, x 60–960 | `proje/index.html` 9 `<line>` |
| 4 | A1 · DK-1 (sahne 03, değişken sahne) | `sahneler/03-hyperframes-cta/uret.py` (kol b kendi metni `Konu burada bitmiyor.`) | `:98` iki değer → `alt_svg, alt_zaman, karaoke_zaman`; `veri["karaoke"]`; `V.karaoke.forEach` (kol a ile aynı üç değişiklik + belge satırı) | `"karaoke"` 9 öğe |
| 5 | A2 · HV-20b / KS-4 (kol a kusuru; başlık iki kolda ortak) | `aciklama-b.md` satır 19, 72 | `Today varsa hangi zaman?` → `Today görünce hangi zamanı seçersin?` | gövde kol a ile aynı (`utm_content` dışında) |
| 6 | **AB-8** (gerçek; J3 K5 kalıbı, P2b A8 ile aynı sınıf) | `sahneler/02-paperjs-ornek/calistir.sh:8` | `PROJE=02-04-ydt-temel-s2` → `PROJE=02-04-ydt-temel-s2b` | huni kapısı AB-8 KALDI → GEÇTİ (§8); `bash -n` geçti |
| 7 | C3 · ST-2 | `uretim-tutanagi/hf-check-duz4.txt` (yeni) | yok → 7 HTML sahnesi | §9 |
| 8 | C2 · EK-8 | `uretim-tutanagi/kontak/02-04-ydt-temel-s2b-duz4-kontak.png`, `…-koyu.png` (yeni) | yok → açık 24 kare, koyu 14 kare; türev yok | §10 |
| 9 | C5 · EK-12 | `uretim-tutanagi/zaman-kapisi.md` (yeni) | yok → 57 satır | §11 |
| 10 | kayıt | `surumler.json` `revizyonlar` | r1 → r1 + r2 (404 karakter) | dosya |

`calistir.sh` notu: `PROJE` yalnız mp4 yakalama yolunda (`ONIZLE_YALNIZ` çıkışından sonra) okunur. Bu oturumun kareleri
`sahne-kare.mjs 02-04-ydt-temel-s2b …` ile kol b'den çekildi; düzeltme kareyi değiştirmez. Önceki kol b jürisi bu satırı görmedi
(eski kapı yalnız `/` önekli yolu arıyordu; K5).

## 2. Ses sha256 (önce = sonra) ve AB-9

| Dosya | Kol b sha256 (ilk 16) | Kol a | Not |
|---|---|---|---|
| `cumle-1.wav` | `0b0dafd59a9813b1` | `0b0dafd59a9813b1` | AB-9: metni aynı cümle, eşit |
| `cumle-2.wav` | `1d805b981216fb41` | `1d805b981216fb41` | AB-9: eşit |
| `cumle-3.wav` | `597582d3ddfd71be` | `720b3d7cc5524ca8` | değişken cümlesi |
| `cumle-4.wav` | `8f69da650730544d` | `b192db36b66bd3a2` | değişken cümlesi |
| `sentez.wav` | `907ff38ad004b731` | `5cc72c39c21b786a` | türev |
| `anlatim.m4a` | `7cd8cb1029989e9b` | `8945bfafa6043897` | türev |
| `anlatim.m4a.imza` | `d951f8e6788ec275` | `5574c4b12cb60933` | türev |
| `anlatim.wav` | `cc999a3bbdb2a8d1` | `33ae53946c6fd609` | türev |

İş başı ve iş sonu ölçümü `diff` boş: 8/8 kol b dosyası değişmedi.

## 3. Karaoke tablosu

Ölçüm yöntemi kol a raporu §3 ile aynı (y 1400–1550; r > 200, 130 < g < 200, b < 120).

Sahne 02 (19 kare; `diff -rq` bu kareleri listelemez: kol a ile bayt aynı):

| Kare | Tema | Okunan sözcük | Beklenen x | Çizgi x | px | Sonuç |
|---|---|---|---|---|---|---|
| `k/…-2.84` | açık | `mı?` | 645–698 | 642–700 | 346 | doğru |
| `k/karaoke/…-3.77` (orta) | açık | `wears` | 247–377 | 247–344 | 582 | doğru (çizilme sürüyor) |
| `k/ara/…-4.9` | açık | `winter.` | 719–855 | 718–859 | 848 | doğru |
| `k/karaoke/…-5.76` (orta) | açık | `Genel` | 216–340 | 213–342 | 772 | doğru |
| `k/karaoke/…-6.32` (orta) | açık | `durum:` | 353–495 | 350–498 | 886 | doğru |
| `k/koyu/…-6.32` (orta) | koyu | `durum:` | 353–495 | 350–497 | 882 | doğru |
| `k/ara/…-7.6` | açık | `zaman.` | 647–794 | 645–796 | 908 | doğru |
| `k/karaoke/…-9.55` (orta) | açık | `pink` (EN2) | 518–611 | 517–601 | 502 | doğru |
| `k/koyu/…-9.55` (orta) | koyu | `pink` (EN2) | 518–611 | 518–601 | 496 | doğru |
| `k/…-10.1` | açık | `T-shirt` (EN2) | 624–766 | 624–767 | 860 | doğru |
| `k/ara/…-12` | açık | `Today` | 103–239 | 103–239 | 818 | doğru |
| `k/karaoke/…-12.62` (orta) | açık | `zamanda` | 317–520 | 312–520 | 1248 | doğru |
| `k/koyu/…-13.38` (orta) | koyu | `geçebilir;` | 603–791 | 598–790 | 1154 | doğru |
| `k/karaoke/…-13.92` (orta) | açık | `farkı` | 816–917 | 811–914 | 616 | doğru |
| `k/ara/…-14.6` | açık | `yapar.` (2. satır) | 515–644 | 514–602 | 528 | doğru (çizilme sürüyor) |
| `k/koyu/…-14.9` | koyu | `yapar.` (2. satır) | 515–644 | 515–648 | 798 | doğru |
| `k/ara/…-16.1` | açık | `anı:` | 411–477 | 407–479 | 428 | doğru |
| `k/karaoke/…-16.13` (orta) | açık | `anı:` | 411–477 | 407–479 | 427 | doğru |
| `k/…-17.35` | açık | `zaman.` | 669–816 | 665–817 | 906 | doğru |

Sahne 03 (değişken sahne, t_bas 22,83; 14 kare):

| Kare | Tema | Okunan sözcük (t0–t1) | Beklenen x (`<line>`) | Çizgi x | Çizgi y | px | Sonuç |
|---|---|---|---|---|---|---|---|
| `k/03-hyperframes-cta-22.83.png` | açık, koyu | — (söz 23,38'de başlar) | — | — | — | 0 | doğru (altyazı yok) |
| `k/karaoke/…-23.52.png` (orta) | açık | `Konu` (23,38–23,66) | 263–377 | 261–378 | 1493–1498 | 704 | doğru |
| `k/karaoke/…-23.86.png` (orta) | açık | `burada` (23,70–24,02) | 390–549 | 387–550 | 1493–1498 | 980 | doğru |
| `k/03-hyperframes-cta-24.png` | açık | `burada` | 390–549 | 387–551 | 1493–1498 | 982 | doğru |
| `k/karaoke/…-24.48.png` (orta) | açık | `bitmiyor.` (24,14–24,82) | 562–746 | 559–748 | 1493–1498 | 1136 | doğru |
| `k/03-hyperframes-cta-24.6.png` | açık | `bitmiyor.` | 562–746 | 559–748 | 1493–1498 | 1136 | doğru |
| `k/koyu/…-24.6.png` | koyu | `bitmiyor.` | 562–746 | 559–748 | 1493–1498 | 1130 | doğru |
| `k/karaoke/…-25.85.png` (orta) | açık | `tamamı` (25,53–26,17) | 229–396 | 226–398 | 1465–1470 | 1034 | doğru |
| `k/koyu/…-25.85.png` (orta) | koyu | `tamamı` | 229–396 | 226–398 | 1465–1470 | 1028 | doğru |
| `k/03-hyperframes-cta-26.8.png` | açık | `Publishing` (26,73–27,29) | 513–738 | 510–701 | 1465–1470 | 1148 | doğru (çizilme sürüyor) |
| `k/karaoke/…-27.53.png` (orta) | açık | `YouTube` (27,37–27,69) | 751–943 | 748–944 | 1465–1470 | 1178 | doğru |
| `k/03-hyperframes-cta-29.48.png` | açık, koyu | — (altyazı 28,84'te kapanır) | — | — | — | 0 | doğru (altyazı yok) |

`proje/index.html`: `"karaoke"` 9 öğe (`ak0_0` `Konu` … `ak1_5` `kanalında.`), `<line id="ak…">` 9; `altyazi.json` cümle 4 sözcük sayısı 9.

## 4. Altyazı x tablosu (y 1400–1550)

| Sahne | Kare | Tema | Önce (DUZ2) | Sonra (DUZ4) |
|---|---|---|---|---|
| 02 | 12 · 14,6 | açık | 63–1015 (kol a ile piksel aynı; jüri E6: 62–1018) | 107–910 |
| 02 | 14,9 | koyu | 63–1015 | 107–910 |
| 03 | 26,8 | açık | 119–963 | 82–935 |
| 03 | 25,85 | koyu | — | 82–936 |
| 03 | 24 · 24,6 | açık | 303–778 | 268–750 |

En büyük x: sahne 02 910, sahne 03 936 (çizgi dahil 944); en küçük x 82. Hepsi x 60–960 içinde; en çok 2 satır.

## 5. AB-8 taraması

Komut: `grep -rnw "02-04-ydt-temel-s2" K/projeler/02-04-ydt-temel-s2b --include=*.js --include=*.html --include=*.json --include=*.py --include=*.sh`

Düzeltmeden önce 26 satır; tek kod başvurusu `sahneler/02-paperjs-ornek/calistir.sh:8` (`PROJE=02-04-ydt-temel-s2;`) → düzeltildi.
Düzeltmeden sonra 25 satır, sınıflama:

| Dosya:satır | İçerik (kısa) | Sınıf |
|---|---|---|
| `sahneler/01-hyperframes-kapak/olay.py:1`, `uret.py:1`, `yardim.py:1` | `"""02-04-ydt-temel-s2 sahne 01 …` | belge dizgisi (yorum) |
| `sahneler/02-paperjs-ornek/sahne-02.js:1` | `// Sahne 02 (02-04-ydt-temel-s2 Shorts) …` | yorum |
| `sahneler/02-paperjs-ornek/kalem-paper.js:8` | `// S2 (15.11): … yalnız iki import yolu 02-04-ydt-temel-s2 oldu` | yorum |
| `sahneler/02-paperjs-ornek/sayfa.html:5` | `// SAHNE 02 — Örnek (02-04-ydt-temel-s2 Shorts) …` | yorum |
| `sahneler/02-paperjs-ornek/calistir.sh:2` | `# Sahne 02 02-04-ydt-temel-s2 Shorts …` | yorum |
| `sahneler/03-hyperframes-cta/uret.py:2`, `yardim.py:1` | `Kol a (02-04-ydt-temel-s2) kopyası …` / `"""02-04-ydt-temel-s2 huni v2 …` | belge dizgisi |
| `sahneler/04-hyperframes-hikaye/uret.py:2`, `yardim.py:1`, `calistir.sh:11` | belge dizgisi; `# paket kökü (02-04-ydt-temel-s2)` | yorum |
| `sahneler/05-hyperframes-kapak-b/uret.py:2`, `yardim.py:1`, `calistir.sh:4`, `calistir.sh:11` | belge dizgisi; `# … (02-04-ydt…`; `# paket kökü (…)` | yorum |
| `sahneler/06-hyperframes-kapak-c/yardim.py:1`, `calistir.sh:11` | belge dizgisi; yorum | yorum |
| `sahneler/07-hyperframes-hikaye-b/uret.py:2`, `yardim.py:1`, `calistir.sh:10` | belge dizgisi; yorum | yorum |
| `sahneler/08-hyperframes-kaydet/uret.py:3`, `yardim.py:1` | `Kol a (02-04-ydt-temel-s2) kopyası …` | belge dizgisi |
| `ortak/anlatim/senaryo.json:135` | `"kimlik": "02-04-ydt-temel-s2"` | `kimlik` alanı (AB-8 "Sayılmaz") |
| `uretim-tutanagi/kol-b.json:3` | `"kol_a": "02-04-ydt-temel-s2"` | kol eşleme kaydı (`varyant` başvurusu sınıfı; tutanak) |

Kod başvurusu (içe aktarma, `KOK`, yol değişkeni) 0. `find -type l`: simge bağı 0. Huni kapısı AB-8: "bilgi: 11 yorum satırı", GEÇTİ.

## 6. Tek değişken (AB-3, AB-9)

| Ölçü | Sonuç |
|---|---|
| Ortak dosyalar (`ortak/kunye.js`, `kalem-paper.js`, `sahne-02.js`, `sayfa.html`, `calistir.sh` sahne 02) | paket adı normalleştirilerek `diff` 5/5 boş |
| `03-hyperframes-cta/yardim.py` | kol a ile bayt aynı |
| Değişmeyen sahnelerin göreli başlangıcı | `zaman.json`: 01 t_bas 0,00 ve 02 t_bas 2,84 iki kolda aynı; 08 (17,41) iki kolda aynı başlar; değişken 08 süresi (kol a 5,34 sn ↔ kol b 5,42 sn) 03'ü 22,75 → 22,83'e kaydırır |
| Değişmeyen sahne kareleri | 01 (11) ve 02 (19) kareleri kol a ile bayt aynı (`diff -rq` listesinde yok) |
| AB-9 | `cumle-1.wav`, `cumle-2.wav` sha256 iki kolda eşit (§2) |

## 7. `diff -rq K/projeler/02-04-ydt-temel-s2 K/projeler/02-04-ydt-temel-s2b` sınıflaması

Ham çıktı: `uretim-tutanagi/DUZ4-diff-rq.txt` (bu rapor ve o dosya yazıldıktan sonra koşuldu).

| Sınıf | Satır | Beklenen mi | İçerik |
|---|---|---|---|
| Değişken `kapanis` | 64 | beklenen | `ortak/anlatim/*` (altyazı, başlar, sözcük, süre, METIN, senaryo, `cumle-3/4.wav`, `sentez.wav`, `anlatim.*`), `zaman.json`, `sahneler/08-*` (uret, html, olay, zaman, `calistir.sh`, `cizim/vizor.svg`, kareler), `sahneler/03-*` (uret, html, olay, zaman, `calistir.sh` yorumu, kareler) |
| Tutanak | 42 | beklenen | paket başına ayrı kayıt (raporlar, jüri hükümleri, kapı çıktıları, kontaklar, taslaklar) |
| Türetilmiş araç çıktısı | 36 | beklenen | `__pycache__/*.pyc` (`co_filename` paket yolu), `proje/.hyperframes/` (`history-id`, `video-state.json`, `artifacts/checks/*.json`; git dışı, kapı dışlar) |
| Kol b türev taşımaz (AB §4) | 10 | beklenen | kök `kapak*.png`, `hikaye*.png`, `kapak-a|b|c-168.png` yalnız kol a'da |
| AB-8 yol | 5 | beklenen | `ortak/kunye.js`, `02-paperjs-ornek/kalem-paper.js`, `sahne-02.js`, `sayfa.html`, `calistir.sh`: yalnız paket adı |
| Paket kimliği | 4 | beklenen | `aciklama.md`, `aciklama-a.md`, `aciklama-b.md` (üst bilgi + `utm_content`; gövde aynı), `surumler.json` (sürüm kimliği, varyant, revizyon) |
| **Beklenmeyen** | **0** | — | — |
| **Toplam** | **161** | | |

## 8. Kapı çıktıları

| Kapı | Komut (çalışma dizini K) | Çıkış | Sonuç |
|---|---|---|---|
| Çakışma | `node araclar/cakisma-kapisi.mjs 02-04-ydt-temel-s2b --port 41333 --sunucu 41022 --json projeler/02-04-ydt-temel-s2b/uretim-tutanagi/cakisma-DUZ4.json` | **0** (47 sn) | 4 sahne çakışma yok |
| Huni, 1. koşu | `node D/araclar/huni-kapi.mjs K/projeler/02-04-ydt-temel-s2b --kol-a K/projeler/02-04-ydt-temel-s2` (kapı `8afc202`) | 1 | 22 GEÇTİ, 3 KALDI (JR-1b, KR-1, **AB-8**) |
| Huni, son koşu (AB-8 düzeltmesinden sonra) | aynı | **1** | 23 GEÇTİ, 2 KALDI, 5 ÖLÇÜLEMEDİ, 3 UYGULANMAZ; `huni-kapi-duz4.txt` |
| `hyperframes check` | §9 | 0 × 7 | hata 0 |

| Madde | Sınıf | Gerekçe |
|---|---|---|
| JR-1b | gerçek, beklenen | jüri `KBJ-hukum-1611-0003.md` 00:06 < son içerik 02:14; 3. tur jüri kapatır |
| KR-1 | **kapı hatası K7** (uygulama) | kol a raporu §11: kunye.js her sahneye uygulanır, HTML sahneleri içe aktarmaz; `yardim.py` kümede yok; `k/` alt dizinleri sayılmaz. Kol b'de 01, 04–08 aynı durum |
| AB-8 (1. koşu) | **gerçek** → düzeltildi | `calistir.sh:8` `PROJE=02-04-ydt-temel-s2` (§1 satır 6); son koşu GEÇTİ |

Son koşuda GEÇTİ: AB-1, AB-2 (29 beklenen, 0 beklenmeyen), AB-3, AB-6, AB-8, AB-9, KS-6f (kol a 168 px; kol b uygulanmaz), HV-1s.

## 9. `hyperframes check` (C3)

Dosya: `uretim-tutanagi/hf-check-duz4.txt`. 7 HTML sahnesi, 7/7 çıkış 0; Lint, Runtime, Motion 0 hata 0 uyarı; Layout 0 sorun;
kontrast 39/39 · 34/34 · 65/65 · 30/30 · 45/45 · 65/65 · 41/41 (01, 03, 04, 05, 06, 07, 08).
Craft uyarıları (düzeltilmedi, B1 bekler): `text_below_floor` 7 (rozet 26 px) · `line_unread` 01 ×6, 04 ×13, 05 ×6, 06 ×9, 07 ×13,
08 ×2 (`sınav günü bak.` 1,40 sn, `al,` 1,83 sn). Sahne 02 boyut sabitleri kol a raporu §7 ile aynı (dosyalar ortak): altyazı 44 (yedek 40/36),
satır 56, en 900, merkez 510; kanal 42; konu 34; rozet 26.

## 10. Kontak (C2) ve 18 klişe ön sayımı

| Sayfa | İçerik |
|---|---|
| `kontak/02-04-ydt-temel-s2b-duz4-kontak.png` (açık) | 01: 0 · 0,9 · 1,5 · 2,4 · 2,8 · 02: 2,84 · 3,77 · 6,32 · 9,55 · 12,62 · 14,6 · 17,35 · 08: 17,41 · 20,5 · 21,2 · 21,7 · 22,4 · 22,82 · 03: 22,83 · 23,52 · 24,48 · 25,85 · 27,53 · 29,48 |
| `kontak/02-04-ydt-temel-s2b-duz4-kontak-koyu.png` (koyu) | 01: 0,9 · 1,5 · 2,6 · 02: 6,32 · 9,55 · 13,38 · 14,9 · 08: 17,41 · 21,7 · 22,82 · 03: 22,83 · 24,6 · 25,85 · 29,48 |

Kol b türev taşımaz (AB §4). Ön sayım (kanıt jürinin sayımıdır): 17 madde 0; **#16 metin duvarı 1 işaret** (sahne 02 son yarısı,
içerik bölgesinde 10 yazı öbeği; kol a ile aynı sahne, aynı kareler). #8 ve #11 kontaktan ölçülmez.

## 11. Zaman kapısı (C5)

Dosya: `uretim-tutanagi/zaman-kapisi.md` (57 satır: kanca 10, gövde 47). Sınıflar kol a ile aynı: kanca istisnası 2, kare yuvarlaması 6,
yazısız kart çerçevesi 2, **gerçek 0**. Bilgi satırları (B2, kod değişmedi):

| Sahne | Öğe | Giriş | İlk sözcük t0 | İkinci sözcük t0 | Not |
|---|---|---|---|---|---|
| 08 | vizör + `Ekran görüntüsü` | 20,27 | `Ekran` 20,27 | `görüntüsü` 20,71 | ifade ilk sözcüğüyle açılır; ikinci sözcük 0,44 sn önce görünür (istem: değişmez, B2 kararı bekler) |
| 03 | `Konu burada` | 23,38 | `Konu` 23,38 | `burada` 23,70 | aynı kalıp; ikinci sözcük 0,32 sn önce görünür. Kol b değişken sahnesi; B2 kararı bu satırı da kapsar |

## 12. Kare tazeliği

Kaynak kümesi kol a raporu §10 ile aynı (`yardim.py` dahil; `ortak/kunye.js` yalnız içe aktaran sahne 02'de; `k/` alt dizinleri dahil).

| Sahne | Kare | En eski kare | En yeni kare | En yeni kaynak | Sonuç |
|---|---|---|---|---|---|
| 01 | 11 | 15.11 23:42:43 | 16.11 02:06:10 | `proje/index.html` 15.11 23:41:45 | taze |
| 02 | 19 | 16.11 02:05:40 | 16.11 02:05:57 | `sahne-02.js` 16.11 01:59:47 (= `kunye.js`) | taze (bütün kareler yeni) |
| 03 | 14 | 16.11 02:05:58 | 16.11 02:06:08 | `proje/index.html` 16.11 02:01:10 | taze (bütün kareler yeni) |
| 04 | 3 | 15.11 23:41:50 | 15.11 23:41:54 | `proje/index.html` 15.11 23:41:50 | taze |
| 05 | 3 | 15.11 23:42:02 | 15.11 23:42:11 | `proje/index.html` 15.11 23:42:03 | taze |
| 06 | 3 | 15.11 23:42:16 | 15.11 23:42:21 | `proje/index.html` 15.11 23:42:17 | taze |
| 07 | 6 | 15.11 23:42:25 | 15.11 23:44:12 | `proje/index.html` 15.11 23:42:26 | taze |
| 08 | 9 | 15.11 23:43:00 | 15.11 23:43:05 | `proje/index.html` 15.11 23:41:45 | taze |

`calistir.sh` (02) 02:15'te değişti; kare kaynağı değildir (§1 notu).

## 13. Düzeltilmeyen maddeler

| Madde | Sebep |
|---|---|
| EK-12 `Ekran görüntüsü` (08) ve `Konu burada` (03) | istem: B2 kararı bekler; bilgi satırı (§11) |
| ST-2 (rozet 26 px) | B1 bekler |
| EK-4, EK-11 | insan kanıtı (`Ekran görüntüsü al, sınav günü bak.`, `Konu burada bitmiyor.` dinlemesi) |
| AB-4, AB-5, AB-7 | yayın sonrası |
| #16 ön sayım işareti (sahne 02) | A listesinde yok; jüri ve şef |
| KR-1 KALDI | kapı hatası (§8) |
| Süre 29,49 sn > hedef | açık nokta; ses değişmez |

## 14. Değişen ve yeni dosyalar

Kaynak: `ortak/kunye.js`, `sahneler/02-paperjs-ornek/kalem-paper.js`, `sahne-02.js`, `calistir.sh`, `sahneler/03-hyperframes-cta/yardim.py`,
`uret.py`, `aciklama-b.md`, `surumler.json`. Türetilmiş: `03/proje/index.html`, `zamanlar.json`, `olaylar.json`; kareler `02/k/**` (19),
`03/k/**` (14), `01/k/koyu/…-1.5.png`, `-2.6.png`. Tutanak: `DUZ4-RAPOR.md`, `DUZ4-diff-rq.txt`, `zaman-kapisi.md`, `hf-check-duz4.txt`,
`cakisma-DUZ4.json`, `cakisma-DUZ4.txt`, `huni-kapi-duz4.txt`, `kontak/` (yeni dizin, 2 sayfa). Kol a paketi dışında başka pakete yazılmadı.

---
Son Güncelleme: 16.11.2026 02:2x — DUZ4-0204S2 (Opus 5.5).
