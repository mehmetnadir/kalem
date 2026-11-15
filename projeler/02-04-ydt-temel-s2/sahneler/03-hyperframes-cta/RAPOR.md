# Sahne 03 CTA (02-04-ydt-temel-s2, HyperFrames DİKEY 1080×1920, 347 kare, t_bas 17,41; cümle 3)

Durum: yazıldı. `ONIZLE_YALNIZ=1` hazırlığı koşuldu, son koşu AÇIK tema. Render yok. Kapı GEÇTİ (çıkış kodu 0, çakışma yok).
Tema: acik
Dosyalar: `SPEC.md` (şef) · `uret.py` (S1 sahne 03 kopyası; şef 2 satır, agy ikon değişimi) · `olay.py`, `yardim.py`,
`nesneler.json` (S1 kopyası, değişmedi) · `calistir.sh` (S1 kopyası; başlık yorumu ve denetim kareleri S2'ye göre) ·
üretilen: `proje/index.html`, `zamanlar.json`, `olaylar.json` (11 ses olayı), `k/*.png`.

## Yöntem
S1 `uret.py` tam parametriktir: `T_BAS`/`KARE` `zaman.json`'dan, çapalar `sozcukler.json` cümle 3'ten (`T(i, bas)` assert'li) okunur.
S2 cümle 3 metni S1 ile birebir (aynı önbellek wav), sözcükler 2,58 sn önde. Kopya S2 verisiyle koştu, 18 assert geçti; zaman kaydırma yok.
Tek içerik farkı ikonlar: S1 ev + bavul → S2 mont (sol) + tişört (sağ). Veri ana ders `12-hyperframes-ozet/uret.py` `MONT`/`TISORT`
(Catmull-Rom `egri` dalı dahil). Değişim `SPEC.md` §3 ile agy'ye verildi.

## İçerik ve yerleşim (S1 ile aynı)

| Satır | Öğe | Yazı · boy | Konum (y) |
|---|---|---|---|
| A | `üç farktan biri` → `üç farkın hepsi` (`üç` yerinde, sarı altçizgi) | Lexend 700 · 72 | taban 452 |
| B | `Tam ders:` (soldan yazılır) | Caveat 700 · 96 | taban 620 |
| Bant | `Simple Present` / `vs Present Continuous`, dolgu vurgu | Fredoka 700 · 74 | 660–896 (x 132–948) |
| İkon | mont (sol, merkez 84/778, ≈ 56×72) · tişört (sağ, merkez 996/778, ≈ 72×60) | çizgi 4,4 / ince 3,0 | bant dışı, 12 px boşluk |
| E | saat + `dört buçuk dakikada` | Lexend 700 · 72 | taban 1066 |
| F | `@ydspublishing` hapı (açık `#ffe066` / `#1b2440`) | Fredoka 700 · 64 | 1200–1312 |

İçerik bandı 383–1312 (%89). Altyazı 1400–1536. 1536 altı boş. Künye: logo, 2 satır ders adı, `YDT · BASIC`, çip `Full lesson`
(`KUNYE.cipler["03-hyperframes-cta"]`). Tek vurgu (bant, hap, `üç` altçizgisi); vurgu renginde yazı, yeşil, kırmızı, emoji yok.
"kanal", QR, "6 dk" yok.

## Olay listesi (kare = yerel; küresel = 17,41 + yerel; zaman `sozcukler.json` cümle 3 çapasından)

| Olay | Kare · yerel (küresel) | Cümle 3 sözcüğü (sıra) |
|---|---|---|
| `üç` kinetik | 31 · 1,03 (18,44) | üç (1) |
| `farktan` kinetik | 36 · 1,19 (18,60) | farktan (2) |
| `üç` sarı altçizgi | 38 · 1,25 (18,66) | üç + 0,22 |
| `biri` kinetik | 67 · 2,23 (19,64) | biri. (4) |
| `Tam ders:` yazımı (1,04 sn) | 83 · 2,78 (20,19) | Tam (5) → ders: t1 (6) |
| bant girişi + `Simple` | 119 · 3,98 (21,39) | Simple (7) |
| `Present` (satır 1) | 127 · 4,22 (21,63) | Present (8) |
| `vs` | 143 · 4,78 (22,19) | ve (9) |
| `Present` (satır 2) | 158 · 5,26 (22,67) | Present (10) |
| `Continuous` | 178 · 5,94 (23,35) | Continuous. (11) |
| `farktan biri` çıkışı | 210 · 7,01 (24,42) | Üç (12) |
| `farkın` kinetik | 218 · 7,25 (24,66) | farkın (13) |
| `hepsi` kinetik | 232 · 7,73 (25,14) | hepsi (14) |
| saat darbesi + `dört` | 251 · 8,37 (25,78) | dört (15) |
| `buçuk` | 258 · 8,61 (26,02) | buçuk (16) |
| `dakikada` + hap girişi | 266 · 8,85 (26,26) | dakikada. (17) |
| `@ydspublishing` yazımı (0,70 sn) | 268 · 8,95 (26,36) | dakikada. → t1 27,06 |
| mont darbesi | 290 · 9,65 (27,06) | dakikada. t1 |
| tişört darbesi | 292 · 9,75 (27,16) | dakikada. t1 + 0,10 |

Hareket kare 306'da biter; ilk 12 kare ve son 41 kare durgun. En uzun boş alt bant 21,39–25,78 (4,4 sn; 9 sn sınırının altında).
Son kare: mont ve tişört bandın iki yanında → kapak karesine döngü (kalıp §1 kural 5).

## Kapı

Komut: `bash araclar/qa-yerel.sh 02-04-ydt-temel-s2 03-hyperframes-cta 20.0,24.2,27.9 27.0 --hazirla`

```
== KAPI
03-hyperframes-cta | çakışma yok (44 örnek, 1156 kutu)
== KARE (açık)  20 · 24.2 · 27.9
== KARE (koyu)  27
kapı çıkış kodu: 0
```

Düzeltme turu: 0 (ilk koşu geçti).

## Bakılan kareler ve bulgu

| Kare | Ne görünür | Bulgu |
|---|---|---|
| `k/03-hyperframes-cta-20.png` | künye, `üç farktan biri` + altçizgi, altyazı `Bu, üç farktan yalnız biri.` | sorun yok; `Tam ders:` 20,19'da başlar |
| `k/03-hyperframes-cta-24.2.png` | satır A, `Tam ders:`, bant 2 satır, altyazı 2 satır | sorun yok; altyazı 1400–1536 içinde |
| `k/03-hyperframes-cta-27.9.png` | son düzen: `üç farkın hepsi`, `Tam ders:`, bant + mont + tişört, saat satırı, hap | taşma, kesik yazı, üst üste binme yok; ikonlar okunur; altyazı kapanmış; 1536 altı boş |
| `k/koyu/03-hyperframes-cta-27.png` | koyu son düzen, hap yazısı clip ile açılıyor (`@ydspublishin`), ikonlar henüz yok | beklenen: yazım 27,06'da biter, ikonlar 27,06'dan çizilir; kontrast yeterli |

## agy koşusu

`agy-filo tek --rol kod` · gemini-3.8-flash-high · 126 sn · başarılı. Özet: `~/.claude/canavar/agy-filo/20261115-124648`.
Şef okuması: S1 dosyasıyla `diff` yalnız SPEC §3 değişimini gösterir (MONT/TISORT verisi, `egri` dalı, sabitler, SVG grupları,
`mont_darbe`/`tisort_darbe`, JS çağrıları). Düzeltme gerekmedi. Özetteki "değişen" listesi worktree geneli; listedeki S2 04/06/07 ve
S3 yolları eş oturumların işidir. Bu sahne dizininde agy yalnız `uret.py` yazdı.

## Açık noktalar

1. **İkonlar kuyrukta çizilir** (27,06–27,61). BRIEF "26,98–27,98 durgun kuyruk" der; ikonlar son sözden sonra 0,55 sn çizilir, sonra durur (S1 ile aynı).
2. **Mont ikonu dar** (≈ 56×72; ızgara oranı 88:113). Bant ile ekran kenarı arası 72 px olduğu için büyütülemez.
3. Bant yazısı 74 px (S1 açık noktası 1 ile aynı: bant 816 px, yanlarda ikon payı).
4. Birim testi yok (HF sahneleri test taşımıyor); doğrulama kapı + kare. Render yapılmadı (`video.mp4`, `kontrol.png` yok).
