# SPEC — 02-04 dikey · sahne 05-canvas-ornek3 (düz canvas, 1080×1920)

Şef tasarımı (15.11). Uygulayan agy yalnız şu dosyayı yazar:

**`/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-dikey/sahneler/05-canvas-ornek3/sahne.js`**

Başka dosyaya dokunma. Silme yok. Test, render, git yok. `sahne-ortak.js`, `sayfa.html`, `calistir.sh` hazır; değiştirme.

## 1. Okunacak kaynaklar (kalıp)

| Dosya | Ne alınır |
|---|---|
| `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-dikey/sahneler/04-canvas-ornek2/sahne.js` | DİKEY iskelet (aynı kit): `import` satırları, `new Sahne`, `FF`/`FC`/`t`/`eyGen` yardımcıları, `nowNokta()` ve `grupKucul()` işlevleri (aynen al), A evresi `ogelerA` dizisi + `S.koy(grupKucul(...))`, şerit kalıbı, son satır `surucu(kur, (f) => S.kare(f), KARE)` |
| `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel/sahneler/05-canvas-ornek3/sahne.js` | İÇERİK ve çizimler (yatay): `EKRAN` sözlüğü + `goster()`, `uzunluk()`, `elCizim()`, `nokta()`, `yayOk()`, `trenParcalari()`, `saatParcalari()`, `biletParcalari()`. YERLEŞİM ve `u()` ALINMAZ (§3'teki dönüşüm) |
| `./sahne-ortak.js` (bu dizin) | API: `Sahne`, `S.kur`, `S.fr`, `S.zm`, `S.koy`, `S.bas`, `S.olay`, `S.darbe`, `S.darbeler`, `S.elYazisi`, `S.metinPop`, `S.cumleYaz` (`satirSay`), `S.kart`, `S.nabiz`; dışa aktarım `RT`, `renkCoz`, `elips`, `ok`, `kutu`, `altCizgi`, `lerp`, `yavasla`, `geriTasma`, `olc`, `altY` |
| `/home/sef/01dev/_worktrees/kalem-0204/projeler/present-continuous-dikey/sahneler/05-canvas-ornek3/sahne.js` | yalnız bakmak için (eski dikey 05); kalıp 04 dikeyden alınır |

İçe aktarım (04 dikeyle aynı): `surucu` ← `/ortak/surucu.js`; `Sahne` ve yardımcılar ← `./sahne-ortak.js`;
`yaziNoktalari` ← `/projeler/02-04-ydt-temel-dikey/ortak/kalem-canvas.js` (`eyGen` için). SVG dosyası kullanılmaz.

## 2. Sabitler

`KARE = 747`, `TBAS = 68.84`, `ICERIK = 735`.
`new Sahne({ tbas: TBAS, kare: KARE, icerik: ICERIK, klasor: "05-canvas-ornek3", cumle: 5 })` — `bolum` VERME
(çip `KUNYE.cipler`'den gelir: `Example 3 / 3`). `FF(b) = "700 ${b}px Fredoka"`, `FC(b) = "700 ${b}px Caveat"`.
Renk yalnız `RT.*` (`murekkep`, `ikincil`, `vurgu`, `vurguDolgu`, `zemin`). Hex renk, kırmızı, yeşil, emoji, `Math.random`,
`Date`, try/catch YOK.

`kur()` başında: `await S.kur()`; `S.sozc.length !== 49` ise `throw new Error(...)`. `t = (i) => S.sozc[i].t0`.
`EKRAN = { Izmir: "İzmir", seven: "7", "p.m.": "pm" }` ve `goster(d)` yataydan aynen (ses metni → ekran metni).

Zaman çizgisi sabitleri: `TY = 1310` (eksen y) · `AX0 = 96`, `AX1 = 984` · `NX = 250` (now) · `X7 = 580` (7 pm) ·
`XT = 850` (tonight) · etiket tabanı `ETY = 1376`, etiket boyu 64.

## 3. Yatay çizim işlevlerinin dikey dönüşümü

Yataydaki `u(n)` dikeyde YOK. Her çizim işlevi ölçek parametresi `s` alır; nokta = `ox + s*x`, `oy + s*y`.
Kalem kalınlığı `s` ile ÇARPILMAZ; aşağıdaki sabit px değerleri kullanılır (BRIEF-DIKEY: nesne 4,0–4,8, belirteç 9–12).

| İşlev (yeni imza) | Değişiklik |
|---|---|
| `elCizim(ad, parcalar, tb, sure, olayEnCok = 3)` | `u(6)` → `6`, `u(1800)` → `1800`; geri kalan aynen (kapı kutusu "cizim") |
| `nokta(cx, cy, r, tb, renk)` | aynen (r px) |
| `yayOk(a, b, h)` | ok ucu boyu `u(24)` → `24` |
| `trenParcalari(ox, oy, s, k)` | `P`/`K`/`elips` içinde `u(n)` → `s*n`. `k` kalınlık nesnesi `{ govde, ince, ray, duman }`: gövde/lokomotif/vagon/tekerlek/burun `k.govde`; baca, bağlantı, camlar `k.ince`; ray `k.ray` (`RT.ikincil`); iki duman elipsi `k.duman` ve `k.duman - 0.2` (`RT.ikincil`) |
| `saatParcalari(cx, cy, r)` | kalınlıklar: kadran `4.8`, 4 çentik `4.4`, yelkovan `4.8` (`RT.murekkep`), akrep `10` (`RT.vurgu`); geometri aynen (akrep 7'de, yelkovan 12'de) |
| `biletParcalari(cx, cy, egim, s)` | `R()` içinde `u(x)` → `s*x`; kenar `4.6` (`RT.murekkep`), delik çizgisi `3.6`, baskı satırları `4.0` (`RT.ikincil`); çentik yayı aynen |

Ana tren kalınlığı `{ govde: 4.6, ince: 4.0, ray: 4.0, duman: 3.6 }`; şerit simgesi `{ govde: 3.4, ince: 3.0, ray: 3.0, duman: 2.8 }`.

## 4. Sözcük dizini (cümle 5, küresel sn, `S.sozc` dizini)

```
0 Üçüncü 69.39 · 5 geleceği 71.55 · 6 anlatıyor. 72.03 · 7 The 73.00 · 8 train 73.16 · 10 Izmir 73.64
11 leaves 74.12 · 13 seven 74.76 · 14 p.m. 75.00 · 15 today. 75.84–76.44 · 19 akşam 77.81 · 20 yedide 78.17
21 kalkıyor. 78.53 · 24 tarifede 80.37 · 26 Tarifeli 81.93 · 28 geniş 83.17 · 29 zaman. 83.49–84.69
30 I 84.94 · 31 am 85.10 · 32 going 85.30 · 35 movie 85.82 · 37 tonight. 86.50–87.42 · 39 akşam 87.75
41 gidiyorum. 88.63 · 42 Planı 89.63 · 45 Planlanmış 91.07 · 47 şimdiki 92.43 · 48 zaman. 92.83–93.43
```

## 5. Yerleşim (px, 1080×1920; içerik bandı 352–1392, kenar 48)

```
 352 ┌ (B) şerit 352–472: leaves → TIMETABLE                     [tren simgesi 237×100] ┐
 380 │ (A) Kart A 380–620: The train to İzmir / leaves at 7 pm today.  (taban 476 / 568) │
 490 │ (B) Kart B 490–730: I am going to the / movie theater tonight.  (taban 580 / 680) │
 700 │ (A) Tren x 48–736, y 710–1000 (s 1,6)   ·   Saat merkez (874, 850), r 150          │
 758 │ (B) Bilet merkez (540, 935), s 2,2, eğim −0,06 (≈ 136–944 × 758–1112)              │
1085 │ (A) TIMETABLE Caveat 72, taban 1150, x 88  ·  (B) ARRANGEMENT taban 1200, x 88      │
1310 │ zaman çizgisi (sahne boyunca): eksen 96→984 · now 250 · 7 pm 580 · tonight 850      │
1376 │ etiketler now / 7 pm / tonight (Caveat 64 el yazısı, taban 1376, x'e ortalı)        │
1392 └──────────────────────────────────────────────────────────────────────────────────┘
1400–1536 altyazı (kit çizer) · 1536–1920 boş
```

## 6. Olay listesi (sırayla; zaman = küresel sn)

### Z — zaman çizgisi (doğrudan `S.koy`; grup A'ya GİRMEZ, sahne sonuna kadar kalır)

Ekleme sırası: önce Z1 (bant eksenin altında kalsın), sonra Z2…

| # | Zaman | Sözcük | Öğe |
|---|---|---|---|
| Z1 | `t(6)` 72,03 | anlatıyor. | gelecek bandı: `S.darbe([[NX + 18, TY], [AX1 - 30, TY]], { duz: true, w: 26, renk: RT.vurguDolgu, alfa: 0.45, uc0: 4, uc1: 8, tohum: 201 }, t(6), 0.5, 0.45)`; uç çentiği YOK (gelecek açık uçlu) |
| Z2 | `t(5)` 71,55 | geleceği | eksen: `ok([AX0, TY], [AX1, TY], 21)` → `S.darbeler([[[AX0, TY], [AX1, TY]], uc1, uc2], { duz: true, w: 4, renk: RT.ikincil, uc0: 6, uc1: 12 }, t(5), 0.4, 0.15, 0.4)` (04 dikey A8 kalıbı) |
| Z3 | `t(5)+0.25` 71,80 | geleceği | `nowNokta(NX, TY, t(5) + 0.25)` + `S.nabiz(NX, TY, 14, t(5) + 0.60)` |
| Z4 | `t(5)+0.40` 71,95 | geleceği | `S.elYazisi({ metin: "now", x: NX - eyGen("now", 64) / 2, y: ETY, boy: 64, renk: RT.murekkep, tb, sure: 0.4 })` |
| Z5 | `t(19)` 77,81 | akşam | 7 pm çentiği: `S.darbe([[X7, TY - 16], [X7, TY + 16]], { duz: true, w: 5, renk: RT.murekkep, uc0: 3, uc1: 3, tohum: 211 }, t(19), 0.15, 0.45)` + `nokta(X7, TY, 10, t(19) + 0.1, RT.murekkep)` |
| Z6 | 77,81–78,53 | akşam yedide | `7 pm` el yazısı: `x = X7 - eyGen("7 pm", 64) / 2`, `y: ETY`, `boy: 64`, `RT.murekkep`, `sozcukler: [{ t0: t(19), t1: t(20) }, { t0: t(20), t1: t(21) }]` |
| Z7 | `t(21)` 78,53 | kalkıyor. | now → 7 pm yayı: `yayOk([NX + 14, TY - 20], [X7 - 8, TY - 22], 26)` → 3 parça; parça 0 gövde `{ w: 4.6, renk: RT.ikincil, uc0: 6, uc1: 8, tohum: 220 }`, `tb`, `sure 0.55`, `ses 0.5`; parça 1–2 ok ucu `{ ..., duz: true, tohum: 221 / 222 }`, `tb + 0.50`, `sure 0.12`, `ses false` (yatay `yay()` kalıbı) |
| Z8 | `t(39)` 87,75 | akşam | tonight çentiği (Z5 gibi, `XT`, `tohum 231`) + `nokta(XT, TY, 10, t(39) + 0.1, RT.murekkep)` |
| Z9 | 87,75–88,58 | akşam sinemaya | `tonight` el yazısı: `x = XT - eyGen("tonight", 64) / 2`, `y: ETY`, `boy: 64`, `sozcukler: [{ t0: t(39), t1: t(41) - 0.05 }]` |
| Z10 | `t(41)` 88,63 | gidiyorum. | now → tonight yayı: Z7 gibi, bitiş `[XT - 8, TY - 22]`, `h 38`, `sure 0.65`, `tohum 240 / 241 / 242`, ok uçları `tb + 0.60` |

### A evresi (hepsi `ogelerA` dizisine; `S.koy` ile DEĞİL)

| # | Zaman | Sözcük | Öğe |
|---|---|---|---|
| A1 | 72,60 | — | Kart A çerçevesi `S.kart({ x: 48, y: 380, w: 984, h: 240, tb: 72.60, ad: "kartA", tohum: 4, kutuSure: 0.14, kutuAralik: 0.08, satirlar: [] })` (ilk sözcükten 0,40 sn önce) |
| A2 | 73,00–76,44 | The … today. | `cumA = S.cumleYaz({ sozcukler: goster(S.sozc.slice(7, 16)), x: 88, y: 476, font: FF(boyA), satirH: hA, satirSay: [4, 5], bosluk: 6 })` → `The train to İzmir` / `leaves at 7 pm today.`. KURAL: iki satırdan biri `olc(FF(72), satır) + 6 × (sözcük − 1) > 904` ise `boyA = 64`, `hA = 84`; değilse `boyA = 72`, `hA = 92` |
| A3 | `t(8)` 73,16 | train | `elCizim("tren", trenParcalari(64, 747, 1.6, anaTren), t(8), 1.1)` → x 48–736, y ≈ 710–1000 (ray y 1000) |
| A4 | `t(13)` 74,76 | seven | `elCizim("saat", saatParcalari(874, 850, 150), t(13), 0.6)` → trenin sağında, x 724–1024 |
| A5 | 80,37–81,83 | tarifede yazılı. | `eTT = S.elYazisi({ metin: "TIMETABLE", x: 88, y: 1150, boy: 72, renk: RT.murekkep, sozcukler: [{ t0: t(24), t1: t(26) - 0.1 }] })` |
| A6 | `t(26)` 81,93 | Tarifeli | TIMETABLE altı: `S.darbe(altCizgi(84, 92 + eTT.w, altY(1150, 72, "TIMETABLE"), 61), { w: 9, renk: RT.vurgu, alfa: 0.9, uc0: 8, uc1: 14, tohum: 561 }, t(26), 0.4, 0.5)` |
| A7 | `t(28)` 83,17 | geniş | odak *leaves*: `K = cumA.kel[4]`; `S.darbe(altCizgi(K.x - 6, K.x + K.w + 6, altY(K.y, boyA, K.m), 11), { w: 9, renk: RT.vurgu, alfa: 0.9, uc0: 8, uc1: 14, tohum: 501 }, t(28), 0.4, 0.55)` |

### Geçiş — çift kart kuralı (BRIEF-DIKEY §2.5; sağ kart boş beklemez)

| # | Zaman | Öğe |
|---|---|---|
| G1 | 84,24–84,60 | `S.koy(grupKucul(ogelerA, 84.24, 0.36))` (04 dikey işlevi aynen; odak `(540, 380)`, ölçek 1 → 0,12, alfa 1 → 0; sonra çizilmez) |
| G2 | 84,54 | şerit çerçevesi `S.kart({ x: 48, y: 352, w: 984, h: 120, tb: 84.54, ad: "serit", tohum: 8, kutuSure: 0.1, kutuAralik: 0.05, satirlar: [] })` |
| G3 | 84,58 | `S.metinPop({ parca: [["leaves", RT.murekkep]], x: 88, y: 434, font: FF(64), tb: 84.58, sure: 0.3, ses: 0.4 })` |
| G4 | 84,64 | ok: `xL = 88 + olc(FF(64), "leaves")`; `okBoy = 110`; `xTT = xL + 24 + okBoy + 24`; `wTT = olc(FC(64), "TIMETABLE")`. Simge solu `SX = 779`. `xTT + wTT > SX - 20` ise `okBoy = 70` ve `xTT` yeniden. `S.darbeler(ok([xL + 24, 412], [xL + 24 + okBoy, 412], 23), { w: 6, renk: RT.ikincil, uc0: 6, uc1: 10 }, 84.64, 0.16, 0.06, false)` |
| G5 | 84,72 | `S.metinPop({ parca: [["TIMETABLE", RT.murekkep]], x: xTT, y: 434, font: FC(64), tb: 84.72, sure: 0.3, ses: false })` |
| G6 | 84,66 | tren simgesi `elCizim("tren-simge", trenParcalari(785, 375, 0.55, simgeTren), 84.66, 0.35, 1)` → x ≈ 779–1016, y ≈ 362–462 (≥ 96 px) |

### B evresi (doğrudan `S.koy`)

| # | Zaman | Sözcük | Öğe |
|---|---|---|---|
| B1 | `t(30)-0.34` 84,60 | I | Kart B çerçevesi `S.kart({ x: 48, y: 490, w: 984, h: 240, tb, ad: "kartB", tohum: 6, kutuSure: 0.14, kutuAralik: 0.08, satirlar: [] })` |
| B2 | 84,94–87,42 | I … tonight. | `cumB = S.cumleYaz({ sozcukler: S.sozc.slice(30, 38), x: 88, y: 580, font: FF(boyB), satirH: hB, satirSay: [5, 3], bosluk: 6 })` → `I am going to the` / `movie theater tonight.`. KURAL A2 ile aynı ölçüm; 72 ise `hB = 100`, 64 ise `hB = 92` (1. satırdaki kalıcı altçizgi 2. satıra değmesin) |
| B3 | `t(35)` 85,82 | movie | `elCizim("bilet", biletParcalari(540, 935, -0.06, 2.2), t(35), 1.0)` |
| B4 | 89,63–90,97 | Planı ben yaptım. | `eAR = S.elYazisi({ metin: "ARRANGEMENT", x: 88, y: 1200, boy: 72, renk: RT.murekkep, sozcukler: [{ t0: t(42), t1: t(45) - 0.1 }] })` |
| B5 | `t(45)` 91,07 | Planlanmış | ARRANGEMENT altı: A6 gibi, `altY(1200, 72, "ARRANGEMENT")`, `eAR.w`, `tohum 562`, altCizgi tohumu `62` |
| B6 | `t(47)` 92,43 | şimdiki | odak *am going*: `A = cumB.kel[1]`, `B = cumB.kel[2]`; y = `B.y + 0.48 * boyB` (`going` kuyruklu; sözleşme 14.11 s11: 0,36 kuyruğa değer); `S.darbe(altCizgi(A.x - 6, B.x + B.w + 6, y, 12), { w: 9, renk: RT.vurgu, alfa: 0.9, uc0: 8, uc1: 14, tohum: 502 }, t(47), 0.4, 0.55)` |

Türkçe çeviri YOK (yatayda yok). Altyazıyı kit çizer; sahne.js altyazıya dokunmaz.

## 7. Kurallar

1. Zaman yalnız kareden (`S.fr`, `S.zm`, `t(i)`); sabit saniye yalnız bu SPEC'teki değerler.
2. Aynı anda en çok 3 sarı (`RT.vurgu`) altçizgi. Karaoke altı kitten gelir (`vurguDolgu`).
3. Boş çerçeve ≤ 0,6 sn bekler (kart A 0,40 · şerit 0,04 · kart B 0,34).
4. İlk 12 kare boş (ilk öğe 71,55 = kare 81); son 12 kare durgun (son hareket 92,83'te biter; `nabiz` `ICERIK`'te durur).
5. Hiçbir öğe y < 352 ya da y > 1398'e taşmaz; x 48–1032 dışına çıkmaz. Yazı kutusu çizim kutusuna değmez.
6. Satır kodu ≤ 100 karakter, 2 boşluk girinti, dosya sonu boş satır. Her öğe bloğunun üstünde tek satır yorum:
   `// 73,16 train: tren çizimi` (zaman + tetik sözcüğü). Dosya başında 2 satır açıklama (04 dikey gibi).

## 8. Kabul ölçütü (şef doğrular)

- `node --check sahne.js` geçer.
- `cd /home/sef/01dev/_worktrees/kalem-0204 && bash araclar/qa-yerel.sh 02-04-ydt-temel-dikey 05-canvas-ornek3 79.4,84.0,93.3 93.3 --hazirla`
  → `kapı çıkış kodu: 0`.
- 79,4: kart A + tren + saat (akrep 7) + 7 pm yayı · 84,0: TIMETABLE + altı + *leaves* altı · 93,3: şerit + kart B + bilet +
  ARRANGEMENT + *am going* altı + iki yay; taşma, kesik yazı, üst üste binme, altyazıyla çakışma yok; bant ≥ %85 dolu.
