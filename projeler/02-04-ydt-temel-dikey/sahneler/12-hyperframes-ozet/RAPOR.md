# Sahne 12 · ara özet DİKEY (HyperFrames 1080×1920, 463 kare, 205,30–220,33 sn; cümle 14)

Durum: istem D-dikey (15.11.2026, srv21). Önizleme hazırlığı `ONIZLE_YALNIZ=1` ile koştu (qa `--hazirla`). Render yok, commit yok.
Tema: koyu

| Kapı | Sonuç |
|---|---|
| `qa-yerel.sh` çıkış kodu | 0 |
| Çakışma kapısı | çakışma yok (61 örnek, 27482 kutu) |
| Kare bakışı (açık 3 + koyu 1 + ara 4 açık + 1 koyu) | taşma, kesik yazı, binme, okunmaz kontrast, boş kare, platform bandında öğe YOK |
| Düzeltme turu | 1 (kuyruk ↔ belirteç payı, ikon satırı, satır sonu `·`) |

## Olay listesi (cümle 14; yerel = küresel − 205,30)

| # | Olay | Küresel sn | Kare | Sözcük (i) |
|---|---|---|---|---|
| 1 | cümle 13 son altyazı dilimi ("Önce bunu sor.") kare 0'dan | 205,30–205,73 | 0–13 | — |
| 2 | çip `Recap` nabzı (ölçek 1 → 1,08 → 1) | 205,85 | 16 | Özet. (0) |
| 3 | blok 1 çerçevesi (el kutusu, x 48–1032, y 360–690) | 206,59 | 39 | Genel (1) |
| 4 | `general` + sarı belirteç | 206,89 | 48 | Genel (1) |
| 5 | mont ikonu | 207,29 | 60 | durum, (2) |
| 6 | `· permanent ·` + belirteç; ev ikonu (+0,2) | 207,85 | 76 | kalıcı (3) |
| 7 | `timetable` + belirteç; tren ikonu (+0,2) | 208,89 | 108 | tarifeli (6) |
| 8 | kalem oku + hap `V1 / V-s` | 210,17 | 146 | geniş (8) |
| 9 | blok 2 çerçevesi (y 702–1032) | 210,99 | 171 | Konuşma (10) |
| 10 | `right now` + belirteç | 211,29 | 180 | Konuşma (10) |
| 11 | blok 1 belirteçleri `ikincil`e döner (en çok 3 sarı) | 211,39 | 183 | — |
| 12 | tişört ikonu | 211,77 | 194 | anı, (11) |
| 13 | `· temporary ·` + belirteç; bavul ikonu (+0,2) | 212,41 | 213 | geçici (12) |
| 14 | `arrangement` + belirteç; bilet ikonu (+0,2) | 213,37 | 242 | planlanmış (15) |
| 15 | kalem oku + hap `am / is / are + V-ing` | 214,77 | 284 | şimdiki (17) |
| 16 | blok 3 çerçevesi (y 1044–1254) | 215,71 | 312 | Zaman (19) |
| 17 | `time word` + belirteç | 216,01 | 321 | Zaman (19) |
| 18 | blok 2 belirteçleri `ikincil`e döner | 216,11 | 324 | — |
| 19 | `· Turkish -yor` + belirteç | 217,21 | 357 | Türkçe (22) |
| 20 | kalem oku + hap `clue` | 217,93 | 379 | ipucu (24) |
| 21 | `MEANING FIRST` Fredoka 96 (x 88, taban 1340) | 218,97 | 410 | Kararı (26) |
| 22 | MEANING FIRST sarı belirteci (biter 219,45) | 219,07 | 413 | anlam (27) |
| 23 | `MEANING` (blok 3 satır b) | 219,45 | 424 | anlam (27) |
| 24 | kalem oku + hap `decision` (biter 220,25) | 219,85 | 436 | verir. (28) |
| 25 | geçiş çizgisi (y 1390, x 88–992) | 219,87–220,29 | 437 | verir. (28) |

`olaylar.json`: 44 ses olayı (29 `cizgi`), hepsi kare < 451. `Y.kontrol`: hareket yerel 0,55–14,99 sn (ilk/son 12 kare durgun).
Altyazı: `alt0` = cümle 13 son dilimi, `alt1–alt3` = cümle 14 dilimleri; aynı anda tek dilim (sözleşme satır 49 kuralı).

## Kapı sonucu (son koşu, düzeltme turu 1 sonrası)
```
== KAPI
12-hyperframes-ozet | çakışma yok (61 örnek, 27482 kutu)
== KARE (açık)  210.7 · 215.45 · 220.32
== KARE (koyu)  220.32
kapı çıkış kodu: 0
```
Komut: `cd K && bash araclar/qa-yerel.sh 02-04-ydt-temel-dikey 12-hyperframes-ozet 210.70,215.45,220.32 220.32 --hazirla`
(210,70 = blok 1 bitti · 215,45 = blok 2 bitti · 220,32 = son düzen). Ara kareler: aynı betik `--kapisiz`, 205.40,206.95,213.00,219.30 / koyu 216.50.

## Bakılan kareler ve bulgu

| Kare | Bulgu |
|---|---|
| `k/12-hyperframes-ozet-210.7.png` | HUD tam (logo, 2 satır ders, rozet, `Recap`); blok 1 dolu; 3 sarı belirteç; alt bant boş (blok 2 sözü gelmedi), boş çerçeve yok |
| `k/12-hyperframes-ozet-215.45.png` | blok 1 belirteçleri gri; blok 2 dolu; hap 182–783 içeride |
| `k/12-hyperframes-ozet-220.32.png` | son düzen: 3 blok + MEANING FIRST + geçiş çizgisi; bant 360–1392 dolu; altyazı 1 satır |
| `k/koyu/12-hyperframes-ozet-220.32.png` | koyu: hap turuncu dolgu üstünde koyu yazı okunur; çizgiler açık renk |
| `k/12-hyperframes-ozet-205.4.png` | kare 0 devri: HUD + "Önce bunu sor." (cümle 13 sonu); içerik bandı boş, 1,3 sn |
| `k/12-hyperframes-ozet-206.95.png` | çerçeve çizilirken `general` açılıyor; binme yok |
| `k/12-hyperframes-ozet-213.png` | blok 2 yarıda (tişört, bavul); 2 sarı belirteç |
| `k/12-hyperframes-ozet-219.3.png` | MEANING FIRST belirteci çiziliyor; blok 3 satır b henüz yok |
| `k/koyu/12-hyperframes-ozet-216.5.png` | koyu ara kare: blok 3 `time word` + belirteç; blok 2 belirteçleri gri |

Düzeltme turu 1 (Edit, şef): ilk koşuda kapı 0 idi, ama yakın kırpmada Caveat *p/y* kuyruğu belirtece ≈ 4 px kaldı. Sözleşme satır 48
kuralına çekildi: belirteç = taban + max(0,28 em, kuyruk + 13) = 28 px (önce 0,36 em ≈ 23 px); ikon satırı 112 → 116 (belirteç ↔ ikon
payı 10 px); BRIEF'teki satır sonu `·` eklendi (`general · permanent ·`, `right now · temporary ·`; belirteç noktayı kapsamaz). SPEC.md eşlendi.

## Kod yolu
- Şef: dikey 01'den `olay.py`, `yardim.py`, `calistir.sh` kopyaladı; `calistir.sh` Edit ile uyarlandı (başlık, KARE=463). `SPEC.md` yazdı.
- agy (`agy-filo tek --rol kod`, gemini-3.8-flash-high, 194 sn, başarılı): `yardim.py` `kunye_svg(bolum)` tam HUD (ku-ders, ku-rz, ku-bolum),
  `uret.py` yeni. Özet: `/home/sef/.claude/canavar/agy-filo/20261115-122605`.
- Şef okuması: SPEC'e uyuyor. Düzeltme turu 1 Edit ile (5 küçük değişiklik, yukarıda).

## Açık noktalar
1. **Yerleşim BRIEF y değerlerinden sapar** (BRIEF §2.10 "y yaklaşık"): blok 1 360–690 (BRIEF 380–680), blok 2 702–1032 (700–1000),
   blok 3 1044–1254 (1020–1240), alt 1274–1373. Gerekçe: blok 1–2'de 3 satır (terim 64, ikon 110, hap 68) ve belirteç payı 300 px'e sığmaz.
2. **İkonlar terimlerin "altında" değil, satır b'de sağa yaslı** (x 502–992). Blok 2 hapı (601 px) ikon satırının yanına sığmaz; iki blok aynı düzende.
3. **Çip nabzı** ("Özet.", 205,85): BRIEF'te yok, şef ekledi; ilk 1,6 sn'de tek görsel değişim. İstenmezse olay 2 silinir.
4. **Altyazı boyu 44.** İstem "yazı tabanı ≥ 50" der; BRIEF §2 ve `ortak/kunye.js` 44 yazar (01 ile aynı karar).
5. **Bantta karaoke yok** (01 ve `kunye.js` ile aynı). Anlatım Türkçe, ekranda İngilizce terim: terim söylendiği anda yazılır. Dilim, kunye.js
   kuralıyla sözcükten önce görünür (ör. 210,7'de "geçici" henüz söylenmedi).
6. "Doğru şık yeşil" bu sahnede uygulanmaz (soru yok).
7. Sönen belirteç `ikincil` + opaklık 0,6: kalın gri çizgi olarak kalır (BRIEF §0 "kaybolmaz"). Daha ince istenirse kalınlık da düşürülür.
8. agy-filo "değişen" listesi 06 ve 07 sahne dosyalarını da gösterdi: paralel oturumların işi; bu sahne o dosyalara dokunmadı.
9. `hyperframes check` ve render koşmadı (istem kapısı `qa-yerel.sh`; render yasak). `uret.py` `-I` olmadan koşar (fontTools kullanıcı site-packages).
10. `nesneler.json` / `zamanlar.json` yok: 01 kalıbı (zaman `zaman.json` + `sozcukler.json` tek kaynak).

Dosyalar: `SPEC.md`, `uret.py`, `yardim.py`, `olay.py`, `calistir.sh`, `proje/index.html`, `olaylar.json`, `k/`, `RAPOR.md`.
