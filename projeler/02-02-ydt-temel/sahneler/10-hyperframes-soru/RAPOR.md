# Sahne 10 — Mini soru (HyperFrames, 1574 kare, t_bas 316,41, cümle 54–59)

Durum: P2 yazıldı. `ONIZLE_YALNIZ=1 bash calistir.sh --tema koyu` ve ardından açık tema (son koşu AÇIK) tamam; uret.py geometri doğrulamaları (satır taşması, şık/pil/balon sığması) geçti. Kapı ve sahne-kare koşulmadı (EK 13.11 12:40).
Künye: SIMPLE PRESENT · YDT BASIC, bölüm "Mini question", ajanda Hook Examples Rule Trap, etkin Trap (kunye.js ile aynı).

## İçerik (taslak 7.1–7.6)
Soru kartı (Every morning, my brother ____ the dog for a walk before school.) + 5 şık (A take · B takes · C taking · D is taking · E to take) · sayaç halkası 3-2-1 ·
öğrenci balonu «Bence A şıkkı: take.» (ogrenci-bas.svg, kadın) · B yeşil `#167A4A` + takes boşluğa yazılır · üç adım yöntemi · çeldirici notları D, C, E.
Kırmızı yok: yanlış işareti ikincil renkli çarpı (BRIEF: kırmızı yalnız tuzak sahnesinde).

## Olay ↔ sözcük t0
| Olay | Küresel sn | Sözcük (t0) |
|---|---|---|
| Kart + MINI QUESTION etiketi | 316,96 | Mini (316,96) |
| İlk sözcük (Every) | 318,01 | Every (318,01) |
| Boşluk çizgisi | 319,86 | boşluk (319,86) |
| Şık satırları gelir | 323,46 | Şıklara (323,46) |
| Sayaç halkası + 3 (2: 325,50 · 1: 326,50; söner 327,54) | 324,50 | Üç (324,50) |
| Öğrenci başı çizilir (−0,18 sn lead-in) / balon sözcükleri | 327,75 / 327,93 | Bence (327,93) |
| A çerçevesi (soluk sarı) | 328,65 | A (328,65) |
| Balon + çerçeve söner | 331,36 | Yaklaştın, (331,36) |
| Özne belirteci (my brother) | 333,93 | My (333,93) |
| A imleci | 335,79 | he. (335,79) |
| A pili «he için s yok» | 337,40 | se (337,40) |
| B satırı yeşil + onay | 339,08 | B (339,08) |
| «takes» boşluğa | 340,61 | takes. (340,61) |
| Panel söner; adım 1 | 342,12 / 343,80 | Yöntem / Önce |
| every morning belirteci | 345,81 | every (345,81) |
| Adım 2; my brother halkası | 348,94 / 350,87 | Sonra / my |
| Adım 3; «yok»; boşluk sarı | 353,62 / 356,50 / 357,18 | Sonra / yok, / takı |
| Panel geri gelir (adımlar 358,59'da söner) | 358,85 | Çeldiricilere (358,89) |
| D imleci / pili | 361,45 / 362,41 | D / rutin |
| C imleci / pili | 366,57 / 366,81 | C / şıkkı |
| E imleci / pili (çarpı 368,08–368,33) | 367,69 / 367,93 | E / şıkkı. |

Son değişiklik 368,33; içerik sonu 368,48 (son 12 kare durgun).

## Kontroller (kapı yerine)
- İd çakışması 0, GSAP komut hedeflerinin hepsi var; index.html tema-acik sınıfı var.
- Satır sayısı 2 (boşluk ilk satırda); balon, pil, şık metni sığma assert'leri geçti.

## Açık notlar
- Panel (şıklar) 342,12–358,85 arasında %8'e söner, üç adım üstüne biner; kapı yanlış alarm verirse bu bölüm bakılacak yer.
- 3-2-1 sayaç: «Üç saniye» + 2,0 sn sessizlik (324,50–327,50). Sayaç anlatımın «Üç» sözcüğünden başlar.

## QA 13.11
- Düzeltme (uret.py): YESIL `#167A4A` → `SAR` (vurgu token'ı; B şık dolgusu, boşluk çizgisi, tik). Önizleme YENİDEN KOŞULMADI (`ONIZLE_YALNIZ=1 bash calistir.sh` gerekir).
- Panel %8 sönüm (342–359 sn) binme: görülmedi, kare alınamadı; binme varsa `s.to("#panel", …opacity 0.08)` → 0.
- Kapı/kare: yok.
- 2. tur (sunucu, --hazirla): panel 342–359 sn arasında 0,08 değil 0'a iniyor (adım kartlarıyla binme kalktı, k/…-345 doğrulandı). Doğru şık sarı + mürekkep tik; B satırının metin/çip rengi tween'i kaldırıldı (açık temada beyaz-sarı okunmuyordu, k/…-340 doğrulandı). Kareler k/10-…-330, -340, -345, -365, k/koyu -340.
- Kalan (küçük): koyu temada B satırı krem yazı + turuncu dolgu, kontrast orta; okunur ama zayıf.
- 3. tur (sunucu, --hazirla): B satırı metin, çip ve tik rengi `var(--pilMetin)` (koyu temada zemin koyusu, açıkta lacivert); yeni token yok (uret.py, rowB/ck tween). Kareler k/10-…-340 (açık) ve k/koyu/10-…-340: iki temada koyu yazı + dolgu okunur, kontrast iyi.

- Halka kuralı: DEĞİŞTİ: `my brother` halkası (cevre) → belirteç altçizgisi (z2, my brother 352,63 sonrası). BIRAKILDI: 1/2/3 adım rakam daireleri ve sayaç halkası (metne değmiyor). Kare k/…-355 temiz.

- zaman eşitleme 13.11: KARE 1574 aynı; --hazirla ile yeniden kuruldu; doğru şık B ve takes sözcükten sonra (k/…-342.1 doğrulandı); kareler -341.3…365.
