# Sahne 08 Kaydet · huni v2 (02-04-ydt-temel-s2, HyperFrames DİKEY 1080×1920, 172 kare, t_bas 17,41; cümle 3, öğretmen) · 15.11.2026

| Ölçüm | Sonuç |
|---|---|
| Hazırlık | `ONIZLE_YALNIZ=1 calistir.sh --tema acik` (qa-yerel `--hazirla`): `önizleme hazır`, 4 ses olayı; render yok |
| qa-yerel | `qa-yerel.sh 02-04-ydt-temel-s2 08-hyperframes-kaydet 17.41,20.1,22.7 22.7 --hazirla` → `kapı çıkış kodu: 0` |
| Çakışma kapısı | `08-hyperframes-kaydet \| çakışma yok (23 örnek, 3439 kutu)` · rc 0 · 0 uyarı |
| Metin taraması | `grep -rniE "tam ders\|dakika" … --exclude-dir=k` → boş (rc 1) |
| Kanal katmanı | 17,41 · 20,1 · 22,7 karelerinde aynı konumda (logo `#logoimg` x 53,2 y 291 h 48 w 193,5; `@ydspublishing` Lexend 700 42 x 263 taban 330) |
| Yedek | yeni sahne, v1 yok; silinen/taşınan dosya yok |

## Olay listesi (sahne içi sn = küresel − 17,41; çapa `sozcukler.json` cümle 3)

| Olay | Çapa | Küresel | Sahne içi | Kare | Hareket | Ses |
|---|---|---|---|---|---|---|
| kare 0 | — | 17,41 | 0,00 | 0 | kanal katmanı + künye; içerik boş | — |
| `kart_giris` | T(0) `Bu,` | 17,96 | 0,55 | 16 | kural kartı opaklık + ölçek 0,96 → 1, 0,40 sn `power3.out` | vurus 0,5 |
| `nokta_giris` | T(1) `üç` | 18,52 | 1,11 | 33 | 3 nokta (1 dolu, 2 halka), 0,30 sn, aralık 0,08 | tik 0,4 |
| `imi_ciz` | T(6) `kuralı` | 20,47 | 3,06 | 92 | yer imi kalemle çizilir (`strokeDashoffset`), 0,50 sn `sine.inOut` | cizgi 0,6 |
| `kaydet_giris` | T(8) `Kaydet.` | 22,15 | 4,74 | 142 | `Kaydet` (Fredoka 96) gelir · yer imi sarı dolgu · Today hapı → mürekkep çerçeve; 0,30 sn | tik 0,6 |
| kuyruk | — | 22,74 | 5,33 → 5,73 | 160 → 172 | durgun (geçiş payı 12 kare) | — |

Kart 18,36'dan sahne sonuna sabittir (çerçeve ve 3 satır). Tek istisna 22,15'teki Today hapı dönüşümü (istem gereği).
Altyazı cümle 3: `Bu, üç farktan yalnız biri.` (17,91–20,22) · `Bu kuralı kaybetme.` (20,22–22,10) · `Kaydet.` (22,10–23,10; sahne 172 kare = 23,14'e kadar);
`altyazi_cumleleri` 2. parçayı iki cümleye böler. Karaoke 9 sözcükte (altçizgi, ortak altyazı öğesi).

## Yerleşim (px)

| Öğe | Değer |
|---|---|
| Kanal + künye | `Y.kunye_svg()` (S1 sahne 08 `yardim.py` kopyası; BRIEF-S2 değerleri ile aynı); konu Fredoka 700 34, rozet `YDT · BASIC` x 664,6 w 203,6 y 386–434 |
| Kural kartı | `rect` x 62 y 562 w 896 h 436 rx 32, mürekkep çizgi 4 (dış 60–960 × 560–1000); dolgu yok (Hikâye A kartıyla aynı dil) |
| Kart metni | Fredoka 700 72, x 124, taban 703 / 803 / 903: `Today` (hap x 102 w 251,7 y 639–727 rx 44) + `iki zamanda` (x 373,7, sağ uç 760,8) · `da geçebilir;` · `farkı anlam yapar.` (sağ uç 721) |
| Noktalar | y 1040: dolu r 13 x 115 · halka r 11 çizgi 4 x 159, 203 |
| Yer imi | Tabler `bookmark`, ölçek 140/18, x 102–195,3, y 1120–1260, çizgi 6 px; dolgu `#imi-dolgu` |
| Kaydet | Fredoka 700 96, x 234,3, taban 1224 (sağ uç ≈ 546) |
| Altyazı | 1400–1550 bandı, `Y.altyazi_svg` (orta 510, genişlik ≤ 900, x 60–960) |

Tema: `#today-kutu` açıkta `#ffe066`, koyuda `#f2a93b`; Today yazısı açıkta/koyuda pilMetin. `#imi-dolgu` path olduğu için
`#root #imi-dolgu{fill:var(--vurguDolgu,#f2a93b)}` (hf_tema path dolgusunu `--vurgu` `#d9900f`'a boyardı).

## Bakılan kareler ve bulgu

| Kare | Bulgu |
|---|---|
| `k/08-hyperframes-kaydet-17.41.png` (açık) | yalnız kanal katmanı + künye; içerik ve altyazı boş |
| `k/08-hyperframes-kaydet-20.1.png` (açık) | kart + 3 nokta + altyazı `Bu, üç farktan yalnız biri.` (karaoke `biri`); yer imi yok; tek sarı Today hapı |
| `k/ara/08-hyperframes-kaydet-20.72.png` (açık) | yer imi yarı çizili (kalem ilerliyor), altyazı `Bu kuralı kaybetme.` |
| `k/ara/08-hyperframes-kaydet-22.27.png` (açık) · `k/ara/koyu/…22.27.png` | hap geçişi: açıkta Today tam okunur; koyuda renk geçişi okunur |
| `k/08-hyperframes-kaydet-22.7.png` (açık) | yer imi sarı dolgulu + `Kaydet`; Today hapı mürekkep çerçeveli; altyazı `Kaydet.` |
| `k/koyu/08-hyperframes-kaydet-22.7.png` (koyu) | aynı düzen; şeffaf logo, sarı `#f2a93b`, krem mürekkep; okunur |

Taşma, kesik yazı, üst üste binme yok. İçerik x 960 sağına geçmez. 0–280 ve 1570–1920 boş. 9 sn'den uzun boş çerçeve yok.
`Kaydet` yazısı 22,15'ten önce yok. Emoji, QR, düğme taklidi, kırmızı yok.

Düzeltme turları:
1. Hap geçişinin ortasında (22,27) açık temada `Today` soluyordu: iki yazı karşılıklı solunca kaplama %75'e iniyor.
   Asimetrik geçiş (alttaki tam kalır) görüntüyü onardı ama kapı 22,41'de `today-hap:text0 × text1` uyarısı verdi.
   Son çözüm: açık temada iki renk aynı (`#1b2440`) → CSS `.tema-acik #today-yazi{opacity:1 !important}` +
   `.tema-acik #today-yazi2{display:none}`; koyu temada simetrik geçiş kalır. Kapı yeniden 0 uyarı.

## Şef düzeltmeleri (agy dışı, Edit)

- `yardim.py` (S1 sahne 08 kopyası): karaoke sözcük süzgecinin üst sınırı `t1 + 0,05` → `t1`. Bölünen parçada t1 = sonraki cümlenin
  ilk sözcüğü (`Kaydet.` 22,15); pay onu pencereye alıyor, sayı tutmuyor, `Bu kuralı kaybetme.` karaokesiz kalıyordu. S1 sahne 08'de
  aynı kusur var (`… olacak.` parçası) — S1'e dokunulmadı, açık nokta.
- `calistir.sh`: `uret.py && olay.py` zinciri iki satıra ayrıldı (sözleşme: `set -e` uret.py hatasını yutar, eski index.html yakalanır).
- `uret.py`: `"#root.tema-acik" not in html` assert'i; Today geçişi için 2 CSS kuralı (yukarıda).

## agy koşu özeti

| Koşu | Model | Süre | Sonuç | Özet |
|---|---|---|---|---|
| `tek` (uret.py, SPEC §1–§8) | gemini-3.8-flash-high | 148 sn | başarılı, tek tur | `/home/sef/.claude/canavar/agy-filo/20261115-192641` |

agy özetinin "değişen" listesinde başka paketlerin dosyaları görünür: worktree'deki paralel oturumların değişikliği; agy yalnız `uret.py` yazdı.

## Kaynak

- Yer imi: Tabler Icons `bookmark` (outline), MIT Lisansı, https://tabler.io/icons — `cizim/bookmark.svg` (paket kataloğunda yok).
- `yardim.py`: `02-04-ydt-temel-s1/sahneler/08-hyperframes-kaydet/yardim.py` kopyası (künye değerleri BRIEF-S2 ile aynı; karaoke içerir).
- `olay.py`: `03-hyperframes-cta/olay.py` kopyası. `calistir.sh`: S1 sahne 08 kopyası (KARE 172, boyut denetimi, denetim kareleri).

## Açık noktalar

1. Karaoke altçizgisi ortak altyazı öğesidir, açık temada `#d9900f`: 22,15 sonrası ekranda yer imi sarısı + karaoke turuncusu birlikte.
2. Koyu tema geçiş karesinde (22,27) iki yazı yarı opak (renk geçişi); kapı yalnız açık temayı ölçer.
3. S1 sahne 08 `yardim.py` aynı karaoke süzgeci kusurunu taşır (bu oturumun kapsamı dışında).
4. `Kaydet.` sözcüğü 22,83'te biter: içerik sonu (t_son 22,75) sonrasına, 12 karelik geçiş payına sarkar; birleştirmede
   sahne 03'e geçiş bu kareleri örter (`birlestir.py` geçiş seçimi şefte; V2-C açık nokta 4).
