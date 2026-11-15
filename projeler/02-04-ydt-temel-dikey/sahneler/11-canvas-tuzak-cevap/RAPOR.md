# 11-canvas-tuzak-cevap DİKEY — RAPOR (15.11, D-dikey; render yok)

Tema: koyu

Motor: düz canvas · 1080×1920 · 30 fps · 657 kare (içerik 645) · t_bas 183,79 · t_son 205,30 · cümle 13 · çip `Trap · answer`
(`KUNYE.cipler`). BRIEF-DIKEY §3 satır 11 uygulandı: tek satırlık karşıt çift (§2.5 istisnası), büyük çizim yok.

## Durum

| Dosya | Kim yazdı | Durum |
|---|---|---|
| `SPEC.md` | şef | yerleşim, 19 olay, 4 yardımcı (`esitDegil`, `notOk`, `zamanCizgisi`, `donenAlti`) + baş sallama, kurallar, kabul ölçütü |
| `sahne.js` | agy-filo (rol kod, gemini-3.8-flash-high, 126 sn, 1 tur) | şef baştan sona okudu, SPEC'e uyuyor; QA tur 1'de 2 satır Edit (öğrenci başı y 1228 → 1222) |
| `sahne-ortak.js` | `04-canvas-ornek2` dikey kopyası (`cmp` ile 05'le aynı) | değişmedi |
| `sayfa.html` | 04 dikey kopyası | değişmedi (1080×1920) |
| `calistir.sh` | şef (04 dikey kalıbı) | N 657, KLASOR, TBAS 183.79, GLOBAL_SN; homebrew PATH koşullu, `Y=$(yuk1)`, yakala `1080 1920`; `ONIZLE_YALNIZ=1` → "önizleme hazır", rc 0 |

agy koşu özeti: `/home/sef/.claude/canavar/agy-filo/20261115-122431/ozet.md` (1/1 başarılı). Özetin "değişen 41" listesi paralel
oturumların dosyalarıdır (06, 07, sözleşme); bu dizinde agy yalnız `sahne.js` yazdı (mtime 12:26, öteki dosyalar 12:22).

## Yerleşim (px)

| Öğe | y | Not |
|---|---|---|
| Kart 1 `I am living in İstanbul.` | 380–520, taban 460 | Fredoka 72, x 88 |
| Not 1 `→ for now (temporary)` | taban 592 | ok kalemle (x 88–152), Caveat 64 x 172 |
| Zaman çizgisi 1 | eksen 670 | kısa bant x 690–830, now x 760, `now` taban 730 |
| `≠ meaning` | taban 840 | ≠ sarı kalem 72 px, Caveat 88, grup ortalı x 540 |
| Kart 2 `I live in İstanbul.` | 910–1050, taban 990 | Fredoka 72 |
| Not 2 `→ always (permanent)` | taban 1120 | not sütunu kart 1 ile aynı x |
| Zaman çizgisi 2 | eksen 1196 | uzun bant x 150–880, now x 760 (iki çizgide aynı), `now` taban 1256 |
| Öğrenci başı | x 892–1009, y 1222–1382 | `peeps-kit/ogrenci-bas.svg`, 160 px |

BRIEF y değerleri 0–30 px aşağı kaydı: sözleşme kuralı (kalıcı sarı altçizgi Fredoka taban + 0,48 × boy, Caveat + 0,52 × boy;
yatay 11'de 0,36 kuyruğa değdi) kartlara ve notlara pay istedi.

## Olay listesi (yerel kare = round((t − 183,79) × 30))

| Sözcük | t (sn) | Kare | Olay |
|---|---|---|---|
| (cevap öncesi) | 184,20 | 12 | öğrenci başı kalemle, alt sağ |
| 0 Olur, | 184,54 | 23 | kart 1 çerçevesi |
| 2 anlam | 185,90 | 63 | `≠` üç sarı darbe (0,1 sn arayla); çarpı yok |
| 3 değişir. | 186,22–186,82 | 73–91 | `meaning` el yazısı |
| 4–8 I … Istanbul. | 187,11–188,95 | 100–155 | kart 1 cümlesi sözcük sözcük, karaoke altı (kit) |
| 9 Şimdilik | 189,12 / 189,30 | 160 / 166 | not oku + `for now` |
| 10 İstanbul'da | 189,68 | 177 | eksen 1 |
| — | 190,00 / 190,08 | 186 / 189 | now 1 + nabız + `now` |
| 11 yaşıyorum | 190,24 | 194 | kısa bant + çentikler (mürekkep) |
| 13 Geçici. | 191,55–192,30 | 233–255 | `(temporary)` |
| 14 Ailenle | 192,48 | 261 | kart 2 çerçevesi + eksen 2 (185,42'de çizilmez) |
| — | 192,90 | 273 | now 2 + nabız + `now` |
| 15 hep | 193,12 / 193,28 | 280 / 285 | not oku + `always` |
| 16 orada | 193,36–194,21 | 287–313 | uzun bant + çentikler |
| 17 yaşıyorsan: | 193,95–194,65 | 305–326 | `(permanent)` |
| 18–21 I … Istanbul. | 194,89–196,65 | 333–386 | kart 2 cümlesi sözcük sözcük |
| 23 yor | 197,70 / 197,78 | 417 / 420 | çoklu odak: *am living* + *live* sarı altı |
| 31 ayrılır. | 201,30 | 525 | *meaning* sarı altı; fiil altları 0,3 sn'de `ikincil`e döner (kaybolmaz) |
| (cevap bitimi) | 202,30–203,30 | 555–585 | öğrenci 1 sn baş sallar (2 vuruş) |
| 32 Kalıcı | 202,74 | 569 | *(permanent)* sarı altı |
| 34 geçici | 203,46 | 590 | *(temporary)* sarı altı (203,86'da biter, kare 602) |

İlk öğe kare 12; son hareket kare 602; nabız içerik sonunda (645) durur; son 12 kare durgun. En uzun olaysız aralık
197,78 → 201,30 (3,5 sn; nabız sürer). Son durumda sarı belirteç 3 (*meaning*, *(permanent)*, *(temporary)*).

## Kapı

`cd K && bash araclar/qa-yerel.sh 02-04-ydt-temel-dikey 11-canvas-tuzak-cevap 192.4,199.5,202.55,204.5 204.5 --hazirla` (son koşu):

```
== KAPI
11-canvas-tuzak-cevap | çakışma yok (87 örnek, 1508 kutu)
...
kapı çıkış kodu: 0
```

İlk koşu (`192.4,199.5,204.5 204.5`) da 0 verdi. Ara kareler `187.6,193.7,201.45,202.55 193.7 --kapisiz` ile alındı.
`node --check sahne.js` geçti; satır ≤ 100 karakter.

## Bakılan kareler ve bulgu

| Kare | Bulgu |
|---|---|
| `k/…-192.4.png` | kart 1 + not 1 + zaman çizgisi 1 (kısa bant, now) + `≠ meaning` + öğrenci başı; alt yarı boş (kart 2 192,48'de gelir) |
| `k/…-187.6.png` | kart 1 yazılıyor; karaoke altı *living* `g` kuyruğunun altında; kart 2 yok |
| `k/…-193.7.png` + `k/koyu/…-193.7.png` | kart 2 çerçevesi boş (cümle 194,89'da), `always` yazılıyor, uzun bant çiziliyor |
| `k/…-199.5.png` | iki kart dolu; *am living* ve *live* sarı altı; altçizgi kuyruğa ve kart kenarına değmez |
| `k/…-201.45.png` | geçiş: fiil altları sarıdan ikincile dönüyor, *meaning* altı çiziliyor |
| `k/…-202.55.png` | baş sallama tepesi: baş altyazıya değmez, eksen okuyla arası ≈ 20 px |
| `k/…-204.5.png` + `k/koyu/…-204.5.png` | son düzen: bant 380–1382 dolu; 3 sarı altçizgi; fiil altları ikincil (koyu temada açık gri, okunur); now noktası zemin halkasıyla bantta seçilir |

Düzeltme turu 1/4: baş sallama (genlik 9,6 px) başın kapı kutusunu 1397,6'ya indiriyordu (sınır 1392). Baş kutusu
y 1228 → 1222 alındı. Kapı 0, kareler temiz.

## Açık noktalar

- Boş çerçeve: kart 1 184,54 → cümle 187,11 (2,6 sn), kart 2 192,48 → cümle 194,89 (2,4 sn). BRIEF satır 11 bu zamanları açıkça
  verir; §0'daki "≤ 0,6 sn" kuralından sapar, "≤ 4 sn" kuralına uyar. Arada `≠ meaning` ve not/zaman çizgisi çizilir.
- 184,2–192,48 arası bandın alt yarısında yalnız öğrenci başı var (≈ 6 sn). Kart 2 erken çizilirse boş çerçeve uzar; BRIEF zamanı tutuldu.
- Bant uç çentikleri `murekkep` (yatay 11 gibi); 04 dikeyde `vurgu`. Sarı sayısını düşürmek için seçildi; BRIEF renk vermiyor.
- Açık temada bant (vurguDolgu %45, BRIEF §2.7) soluk; değer BRIEF'ten, değişmedi (04 raporuyla aynı not).
- Öğrenci başının sahne 10 dikeydeki konumu ile sürekliliği ölçülmedi (10 dikey bu koşuda yok). BRIEF: 10'da baş balonla y 860–1380.
- `k/` içinde istemdeki 3 + 1 kareden fazla kare var (ara kareler); hepsi bakıldı.
- Render (mp4, olaylar.json) koşulmadı (istem gereği).
