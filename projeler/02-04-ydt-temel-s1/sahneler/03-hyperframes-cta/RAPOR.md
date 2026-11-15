# Sahne 03 CTA (02-04-ydt-temel-s1, HyperFrames DİKEY 1080×1920, 347 kare, t_bas 19,99; cümle 3)

Durum: yazıldı. `ONIZLE_YALNIZ=1` hazırlığı koşuldu, son koşu AÇIK tema. Render yok. Kapı GEÇTİ (çıkış kodu 0, çakışma yok).
Tema: acik
Dosyalar: `SPEC.md` (şef) · `uret.py` (agy) · `olay.py` (şef, 11 satır) · `yardim.py` (örnek kopyası + künye düzeltmesi) ·
`calistir.sh` (örnek kopyası + `ONIZLE_YALNIZ`) · `nesneler.json` · üretilen: `proje/index.html`, `zamanlar.json`, `olaylar.json` (11 ses olayı).

## İçerik ve yerleşim

| Satır | Öğe | Yazı · boy | Konum (y) |
|---|---|---|---|
| A | `üç farktan biri` → `üç farkın hepsi` (`üç` yerinde kalır, sarı altçizgi) | Lexend 700 · 72 | taban 452 |
| B | `Tam ders:` (soldan yazılır) | Caveat 700 · 96 | taban 620 |
| Bant | `Simple Present` / `vs Present Continuous`, dolgu `vurgu` | Fredoka 700 · 74 | 660–896 (x 132–948) |
| İkon | ev (sol, x 48–120) · bavul (sağ, x 960–1032), 72 px | çizgi 4,4 | merkez 778 |
| E | saat + `dört buçuk dakikada` | Lexend 700 · 72 | taban 1066 |
| F | `@ydspublishing` hapı (açık: `#ffe066` / `#1b2440`) | Fredoka 700 · 64 | 1200–1312 |

İçerik bandı 383–1312 (bandın %89'u). Altyazı 1400–1536 (`yardim.altyazi_svg`). 1536 altı boş.
Künye: logo, ders adı 2 satır `SIMPLE PRESENT vs` / `PRESENT CONTINUOUS`, rozet `YDT · BASIC` 2. satırın sağında (x 670–952),
çip `Full lesson` (`KUNYE.cipler["03-hyperframes-cta"]`). Ölçüler `ortak/kunye.js` ile aynı.
Renk: tek vurgu (bant, hap, `üç` altçizgisi). Vurgu renginde yazı yok. Yeşil, kırmızı, emoji yok. "kanal", QR, "6 dk" yok.

## Olay listesi (yerel sn = küresel − 19,99; zaman `sozcukler.json` çapasından, `T(i, bas)` assert'li)

| Olay | Kare · yerel (küresel) | Cümle 3 sözcüğü (sıra) |
|---|---|---|
| `üç` kinetik | 31 · 1,03 (21,02) | üç (1) |
| `farktan` kinetik | 36 · 1,19 (21,18) | farktan (2) |
| `üç` sarı altçizgi | 38 · 1,25 (21,24) | üç + 0,22 |
| `biri` kinetik | 67 · 2,23 (22,22) | biri. (4) |
| `Tam ders:` yazımı (1,04 sn) | 83 · 2,78 (22,77) | Tam (5) → ders: t1 (6) |
| bant girişi + `Simple` | 119 · 3,98 (23,97) | Simple (7) |
| `Present` (satır 1) | 127 · 4,22 (24,21) | Present (8) |
| `vs` | 143 · 4,78 (24,77) | ve (9) |
| `Present` (satır 2) | 158 · 5,26 (25,25) | Present (10) |
| `Continuous` | 178 · 5,94 (25,93) | Continuous. (11) |
| `farktan biri` çıkışı | 210 · 7,01 (27,00) | Üç (12) |
| `farkın` kinetik | 218 · 7,25 (27,24) | farkın (13) |
| `hepsi` kinetik | 232 · 7,73 (27,72) | hepsi (14) |
| saat darbesi + `dört` | 251 · 8,37 (28,36) | dört (15) |
| `buçuk` | 258 · 8,61 (28,60) | buçuk (16) |
| `dakikada` + hap girişi | 266 · 8,85 (28,84) | dakikada. (17) |
| `@ydspublishing` yazımı (0,70 sn) | 268 · 8,95 (28,94) | dakikada. → t1 29,64 |
| ev darbesi | 290 · 9,65 (29,64) | dakikada. t1 |
| bavul darbesi | 292 · 9,75 (29,74) | dakikada. t1 + 0,10 |

Hareket 10,20 yerel'de (kare 306) biter. İlk 12 kare ve son 41 kare durgun. En uzun durgunluk 1,1 sn; boş çerçeve yok.
Son kare: ev ve bavul bandın iki yanında → kapak karesine döngü (kalıp §1 kural 5).

## Kapı

Komut: `bash araclar/qa-yerel.sh 02-04-ydt-temel-s1 03-hyperframes-cta 22.7,27.0,30.4 29.8 --hazirla`

```
== KAPI
03-hyperframes-cta | çakışma yok (44 örnek, 1140 kutu)
...
kapı çıkış kodu: 0
```

Düzeltme turu: 0 (ilk koşu geçti).

## Bakılan kareler ve bulgu

| Kare | Ne görünür | Bulgu |
|---|---|---|
| `k/03-hyperframes-cta-22.7.png` | künye, `üç farktan biri` + altçizgi, altyazı cümle 3/1 | sorun yok; `Tam ders:` 22,77'de başlar, bant henüz yok |
| `k/03-hyperframes-cta-27.png` | satır A (çıkış başlıyor), `Tam ders:`, bant 2 satır | sorun yok |
| `k/03-hyperframes-cta-30.4.png` | son düzen: satır A, `Tam ders:`, bant + ev + bavul, saat satırı, hap | taşma, kesik yazı, üst üste binme yok; altyazı kapanmış; 1536 altı boş |
| `k/koyu/03-hyperframes-cta-29.8.png` | koyu son düzen, ikonlar çizim ortasında | kontrast yeterli; ikonlar 29,64'ten çizilir (beklenen) |

## agy koşusu

`agy-filo tek --rol kod` · gemini-3.8-flash-high · 312 sn · başarılı. Özet: `~/.claude/canavar/agy-filo/20261115-120259`.
Şef okuması: `uret.py` SPEC'e uyuyor (çapa assert'leri, `BANT_BOY` 74, yerleşim, renk kuralı, 11 ses olayı). Düzeltme gerekmedi.
agy özetindeki "değişen" listesi worktree'nin tamamıdır. Listedeki `02-04-ydt-temel-dikey/…` ve `.claude/docs/sozlesme.md`
yolları aynı worktree'de koşan eş oturumların işidir. agy yalnız `uret.py` yazdı (ve kendi denemesinde `uret.py` + `olay.py`'yi koştu).

## Açık noktalar

1. **Bant yazısı 74 px.** Bant tam genişlikte (984) olsaydı `vs Present Continuous` 84 px'e sığardı. Son karede ev ve bavul bandın
   iki yanında durmalı; bant bu yüzden 816 px (yanlarda 72 px ikon + 12 px boşluk). İstenirse 3 satır (`Simple Present` / `vs` /
   `Present Continuous`) ile yazı 78 px olur; BRIEF satır kırılımı değişir.
2. **İkonlar kuyrukta çizilir** (29,64–30,19). BRIEF "29,56–30,56 durgun kuyruk" der; ikonlar son sözden sonra 0,55 sn çizilir, sonra durur.
3. **Bant girişi öncesi boşluk.** 20,39–23,97 arasında içerik bandının alt kısmı (500–1392) boş; en uzun boş süre 3,6 sn (9 sn sınırının altında).
4. `yardim.py` künyesi bu pakete göre değişti (ders adı 2 satır, rozet konumu, çip dolgusu 64). Sahne 01 ve 04 HF sahneleri aynı
   düzeltmeyi taşımalı; kare 0 künyesi Paper.js sahne 02 (`kunye.js`) ile aynı px.
6. **Sözleşme adayı (yazma kapsamı dışı, şef ekler):** "Dikey HF sahnesinin `yardim.py` künyesi `ortak/kunye.js` KUNYE ile aynı
   olmalı (ders 2 satır `dersSatir` 64, rozet x = kenar + 2. satır genişliği + `rozetAra` 24, çip dolgusu 64); örnek paket kopyası tek
   satır ders taşır (15.11, 02-04-s1 s03)." · "`agy-filo tek` özetindeki 'değişen' listesi worktree geneli; eş oturum varken sahiplik
   `git status` + mtime ile ayrılır."
5. Birim testi yok (HF sahneleri test taşımıyor); doğrulama kapı + kare. Render yapılmadı (`video.mp4`, `kontrol.png` yok).
