# SPEC — 02-04 dikey · sahne 09-canvas-karsit2 (düz canvas, 1080×1920)

Şef tasarımı (15.11). Uygulayan agy yalnız şu dosyayı yazar:

**`/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-dikey/sahneler/09-canvas-karsit2/sahne.js`**

Başka dosyaya dokunma. Silme yok. Test, render, git yok. `sahne-ortak.js`, `sayfa.html`, `calistir.sh` hazır; değiştirme.

## 1. Okunacak kaynaklar (kalıp)

| Dosya | Ne alınır |
|---|---|
| `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-dikey/sahneler/04-canvas-ornek2/sahne.js` | DİKEY iskelet: `import` satırları, `new Sahne`, `FF`/`FC`/`t`/`eyGen`, `nowNokta()` (§3 değişikliği ile), `grupKucul()` + `gizli` tuvali (aynen), şerit kalıbı, son satır `surucu(kur, (f) => S.kare(f), KARE)` |
| `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-dikey/sahneler/05-canvas-ornek3/sahne.js` | dikeye çevrilmiş yardımcılar (aynen al): `EKRAN` + `goster()`, `uzunluk()`, `elCizim()`, `nokta()`, `yayOk()`, `trenParcalari(ox, oy, s, k)` |
| `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel/sahneler/09-canvas-karsit2/sahne.js` | YATAY karşılık: olay sırası, `TISORT` ızgarası + `tisortParcalari()`, `esitDegil()`, not satırı el yazısının `sozcukler` pencereleri. YERLEŞİM ve `u()` ALINMAZ |
| `./sahne-ortak.js` (bu dizin) | API: `S.kur`, `S.fr`, `S.zm`, `S.koy`, `S.bas`, `S.olay`, `S.darbe`, `S.darbeler`, `S.elYazisi`, `S.metinPop`, `S.cumleYaz` (`satirSay`), `S.kart`, `S.nabiz`; dışa aktarım `RT`, `renkCoz`, `elips`, `ok`, `kutu`, `altCizgi`, `lerp`, `yavasla`, `olc`, `altY` |

İçe aktarım 04 dikeyle aynı: `surucu` ← `/ortak/surucu.js`; `Sahne` ve yardımcılar ← `./sahne-ortak.js`;
`yaziNoktalari` ← `/projeler/02-04-ydt-temel-dikey/ortak/kalem-canvas.js` (`eyGen` için). SVG dosyası kullanılmaz.

## 2. Sabitler

`KARE = 523`, `TBAS = 145.29`, `ICERIK = 511`.
`new Sahne({ tbas: TBAS, kare: KARE, icerik: ICERIK, klasor: "09-canvas-karsit2", cumle: 10 })` — `bolum` VERME
(çip `KUNYE.cipler`'den: `Contrast 2 / 2`). `FF(b) = "700 ${b}px Fredoka"`, `FC(b) = "700 ${b}px Caveat"`.
Renk yalnız `RT.*` (`murekkep`, `ikincil`, `vurgu`, `vurguDolgu`, `zemin`). Hex renk, kırmızı, yeşil, emoji, `Math.random`,
`Date`, try/catch YOK.

`kur()` başında: `await S.kur()`; `S.sozc.length !== 37` ise `throw new Error(...)`. `t = (i) => S.sozc[i].t0`,
`t1 = (i) => S.sozc[i].t1`. `gizli` tuvalini 04 dikey gibi kur.

`HZ = 144.0` — "hazır" zamanı: sahne 08'den süren öğeler bu zamanda başlar, kare 0'da TAM görünür (kare 0 = 08 son düzeni).
HZ öğelerinin HEPSİ sessiz: `ses: false` (olay yazılmaz; kare 0 geçiş altındadır).

Ölçü sabitleri (BRIEF-DIKEY §3 satır 8 ortak ölçüler):
kart `x 48, y 490, w 984, h 270`, satır tabanı `600` / `700` (`satirH 100`), metin `x 88` · not satırı tabanı `NY = 860`, boy 72 ·
zaman ekseni `TY = 1180`, `AX0 = 96`, `AX1 = 984` · today bandı `x 200–880, y 1040–1180` · `NX = 360` (now) · `X7 = 780` (7 pm) ·
etiket tabanı `ETY = 1240`, boy 64 · alt satır tabanı `EY = 1370`, boy 64 · şerit `y 352, h 120`, şerit yazı tabanı `430`.

## 3. Yeni / değişen yardımcılar (sahne.js içinde; tam kodu agy yazar)

| İşlev | Tarif |
|---|---|
| `nowNokta(cx, cy, tb)` | 04 dikeydeki işlev, YALNIZ `S.olay(...)` satırı yok (now 08'den hazır; ses yazılmaz) |
| `tisortParcalari(x, y, w, h, kal)` | yatay 09 `TISORT` ızgarası (100×90), kutuya ortalı; `u()` yok; her parça `o: { w: kal, renk: RT.murekkep, duz: d.duz }` |
| `bantDolgu(x0, y0, x1, y1, tb, alfa)` | öğe `{ciz}`: `f < S.fr(tb)` ise çizmez; değilse `ctx.globalAlpha = alfa`, `fillStyle = renkCoz(RT.vurguDolgu)`, `fillRect`. Kapı kutusu yok, olay yok; başta `S.bas(S.fr(tb))` |
| `sonenOdak(x0, x1, y, tohum, tb, tSon, ses)` | aynı `altCizgi(x0, x1, y, tohum)` noktalarından iki `S.darbe`: sarı `{ w: 9, renk: RT.vurgu, alfa: 0.9, uc0: 8, uc1: 14, tohum: 500 + tohum }` (`ses`) ve aynı ayarla `RT.ikincil` (`false`); ikisi de `tb`, `0.4` sn. Öğe `f < S.fr(tSon)` iken sarıyı, sonra ikincili çizer (BRIEF §0: eski belirteç söner, kaybolmaz) |
| `esitDegil(cx, cy)` | `≠` üç kalem darbesi: `[[cx-24, cy-13], [cx+24, cy-13]]`, `[[cx-24, cy+13], [cx+24, cy+13]]`, `[[cx+13, cy-36], [cx-13, cy+36]]` |

Kalıcı (sönmeyen) odak altçizgisi 05 dikey A7 kalıbı: `S.darbe(altCizgi(x0, x1, y, tohum), { w: 9, renk: RT.vurgu, alfa: 0.9,
uc0: 8, uc1: 14, tohum: 500 + tohum }, tb, 0.4, ses)`.

## 4. Sözcük dizini (cümle 10, küresel sn, `S.sozc` dizini; 37 sözcük)

```
0 The 145.84 · 1 train 146.00 · 2 to 146.32 · 3 Izmir 146.48 · 4 leaves 147.04 · 5 at 147.40 · 6 seven 147.64
7 p.m. 147.92 · 8 today. 148.24–148.80 · 9 Burada 149.05 · 10 today 149.69–150.17 · 12 saatle 150.57
13 geliyor: 151.05–151.77 · 14 akşam 151.85 · 15 yedi. 152.25–152.97 · 16 Kalkış 153.01 · 17 henüz 153.45
20 tarifede 154.93 · 21 yazılı. 155.33–156.01 · 22 Geniş 156.09 · 24 Today 157.21–157.61 · 28 var. 158.61–158.89
29 Farkı 159.05 · 32 konuşma 160.57–160.89 · 33 anı 160.97–161.21 · 35 tarife 161.61–162.01 · 36 mi? 162.09–162.41
```

## 5. Yerleşim (px, 1080×1920; içerik bandı 352–1392, kenar 48)

```
 352 ┌ (Ş) şerit 352–472: is wearing … today → this day only           [tişört simgesi 96] ┐
 380 │ (H) 08 üst notu "today" Caveat 80, taban 450 (yalnız kare 0–21; şeride küçülür)     │
 490 │ Kart 490–760 · satır tabanı 600 / 700 · metin x 88                                   │
     │   (H) She is wearing her / pink T-shirt today.      tişört 220 px x 772–992 + halka   │
     │   (B) The train to İzmir / leaves at 7 pm today.    tren x ≈ 726–992, y ≈ 507–619    │
 860 │ not satırı (taban 860, Caveat 72): (H) today → this day only · (N) today + 7 pm → timetable │
1040 │ today bandı x 200–880, y 1040–1180 (vurguDolgu dolgu) + uç çentikleri                │
1180 │ eksen 96 → 984 (ok ucu) · now ● x 360 (nabız) · 7 pm ● x 780 · yay now → 7 pm (bant içi) │
1240 │ etiketler now (x 360) · 7 pm (x 780), Caveat 64 el yazısı, x'e ortalı                │
1370 │ RIGHT NOW (x 360'a ortalı)      ≠ (x 570)      TIMETABLE (x 780'e ortalı), Caveat 64  │
1392 └──────────────────────────────────────────────────────────────────────────────────────┘
1400–1536 altyazı (kit çizer) · 1536–1920 boş
```

Ölçülen genişlikler (başsız Chrome, 15.11): FF(72) `The train to İzmir` 568, `leaves at 7 pm today.` 690, `She is wearing her` 589,
`pink T-shirt today.` 604 · FF(56) `is wearing … today` ≈ 474 · FC(56) `this day only` ≈ 244 · FC(64) `RIGHT NOW` 292, `TIMETABLE` 293.
Bu yüzden kart 72 px'te kalır; şerit 56 px'tir (64 px'te şerit + simge 1032'yi aşar; BRIEF §2.10 küçülünce ≥ 48).

## 6. Olay listesi (sırayla; zaman = küresel sn)

### Z — zaman çizgisi (doğrudan `S.koy`; grup H'ye GİRMEZ, sahne sonuna kadar kalır). Ekleme sırası Z1 → Z5.

| # | Zaman | Öğe |
|---|---|---|
| Z1 | HZ | `bantDolgu(200, 1040, 880, 1180, HZ, 0.32)` |
| Z2 | HZ | bant uç çentikleri: x 200 ve x 880 için `S.darbe([[x, 1040], [x, 1196]], { duz: true, w: 4.5, renk: RT.murekkep, uc0: 3, uc1: 3, tohum: 212 / 213 }, HZ, 0.15, false)` |
| Z3 | HZ | eksen: `ok([AX0, TY], [AX1, TY], 21)` → `S.darbeler([[[AX0, TY], [AX1, TY]], uc1, uc2], { duz: true, w: 4, renk: RT.ikincil, uc0: 6, uc1: 12 }, HZ, 0.3, 0.1, false)` (04 dikey kalıbı) |
| Z4 | HZ | `nowNokta(NX, TY, HZ)` + `S.nabiz(NX, TY, 14, HZ)` |
| Z5 | HZ | `S.elYazisi({ metin: "now", x: NX - eyGen("now", 64) / 2, y: ETY, boy: 64, renk: RT.murekkep, tb: HZ, sure: 0.3, ses: false })` |

### H — sahne 08'in son düzeni (hepsi `ogelerH` dizisine; `S.koy` ile DEĞİL; hepsi `HZ`, sessiz)

| # | Öğe |
|---|---|
| H1 | üst not `eH1 = S.elYazisi({ metin: "today", x: 88, y: 450, boy: 80, renk: RT.murekkep, tb: HZ, sure: 0.3, ses: false })` |
| H2 | H1 altı (söndü): `S.darbe(altCizgi(84, 92 + eH1.w, 479, 2), { w: 7, renk: RT.ikincil, alfa: 0.9, uc0: 8, uc1: 14, tohum: 562 }, HZ, 0.3, false)` |
| H3 | kart çerçevesi (sessiz): `S.darbeler(kutu(48, 490, 984, 270, 91), { w: 4, renk: RT.ikincil, uc0: 10, uc1: 18 }, HZ, 0.1, 0.05, false)` (`S.kart` DEĞİL: o olay yazar) |
| H4 | cümle iki satır: `S.metinPop({ parca: [["She is wearing her", RT.murekkep]], x: 88, y: 600, font: FF(72), tb: HZ, sure: 0.3 })`; aynısı `"pink T-shirt today."`, `y: 700` (`ses` verme) |
| H5 | `elCizim("tisort", tisortParcalari(772, 526, 220, 198, 4.6), HZ, 0.3, 0)` |
| H6 | tişört halkası (08 141,77): `S.darbe(elips(882, 625, 128, 116, -0.05, 31), { w: 6, renk: RT.vurgu, alfa: 0.85, uc0: 14, uc1: 30 }, HZ, 0.3, false)` |
| H7 | *is wearing* altı (08 son odağı, sarı): `x0 = 88 + olc(FF(72), "She ") - 6`, `x1 = 88 + olc(FF(72), "She is wearing") + 6`, `y = altY(600, 72, "wearing")`; kalıcı odak kalıbı, `tohum 3`, `HZ`, `ses false` |
| H8 | kart *today* altı (söndü): `x0 = 88 + olc(FF(72), "pink T-shirt ") - 6`, `x1 = x0 + olc(FF(72), "today") + 12`, `y = altY(700, 72, "today")`; kalıcı odak kalıbı ama `renk: RT.ikincil`, `tohum 1`, `HZ`, `ses false` |
| H9 | not satırı `today → this day only`: `eH9 = S.elYazisi({ metin: "today", x: 88, y: NY, boy: 72, … HZ, sure 0.3, ses false })`; ok `ox = 88 + eH9.w + 18`: `ok([ox, NY - 20], [ox + 56, NY - 20], 7)` → `S.darbeler(…, { duz: true, w: 4.5, renk: RT.murekkep, uc0: 4, uc1: 6 }, HZ, 0.1, 0.03, false)`; `S.elYazisi({ metin: "this day only", x: ox + 74, y: NY, boy: 72, … HZ, sure 0.3, ses false })` |

### G — küçülme (BRIEF §3 satır 9: 145,72'de 08 kartı + notu üst şeride küçülür)

| # | Zaman | Öğe |
|---|---|---|
| G1 | 145,72–145,96 | `S.koy(grupKucul(ogelerH, 145.72, 0.24))` (04 dikey işlevi aynen; süre 0,24: yeni kartın ilk sözcüğü 145,84) |

### B — yeni kart (doğrudan `S.koy`)

| # | Zaman | Sözcük | Öğe |
|---|---|---|---|
| B1 | 145,80 | — | `S.kart({ x: 48, y: 490, w: 984, h: 270, tb: 145.80, ad: "kart", tohum: 2, kutuSure: 0.12, kutuAralik: 0.06, satirlar: [] })` (ilk sözcükten 0,04 sn önce) |
| B2 | 145,84–148,80 | The … today. | `cum = S.cumleYaz({ sozcukler: goster(S.sozc.slice(0, 9)), x: 88, y: 600, font: FF(72), satirH: 100, satirSay: [4, 5], bosluk: 6 })` → `The train to İzmir` / `leaves at 7 pm today.` |
| B3 | `t(1)` 146,00 | train | `elCizim("tren", trenParcalari(732, 521, 0.62, { govde: 4.2, ince: 3.6, ray: 3.6, duman: 3.2 }), t(1), 0.9)` → kartın sağ üst iç köşesi, x ≈ 726–992, y ≈ 507–619 (1. satır 674'te biter; 2. satır yazı kutusu 635'te başlar) |

### Ş — şerit (doğrudan `S.koy`; BRIEF §2.5)

| # | Zaman | Öğe |
|---|---|---|
| Ş1 | 145,92 | `S.kart({ x: 48, y: 352, w: 984, h: 120, tb: 145.92, ad: "serit", tohum: 8, kutuSure: 0.1, kutuAralik: 0.05, satirlar: [] })` |
| Ş2 | 145,96 | `S.metinPop({ parca: [["is wearing … today", RT.murekkep]], x: 88, y: 430, font: FF(56), tb: 145.96, sure: 0.3, ses: 0.4 })` |
| Ş3 | 146,02 | `xL = 88 + olc(FF(56), "is wearing … today")`; `S.darbeler(ok([xL + 20, 410], [xL + 80, 410], 23), { w: 5, renk: RT.ikincil, uc0: 6, uc1: 10 }, 146.02, 0.16, 0.06, false)` |
| Ş4 | 146,08 | `S.metinPop({ parca: [["this day only", RT.murekkep]], x: xL + 100, y: 430, font: FC(56), tb: 146.08, sure: 0.3, ses: false })`. KURAL: `xL + 100 + olc(FC(56), "this day only") > 910` ise Ş2–Ş4'te 56 yerine 52 |
| Ş5 | 146,04 | `elCizim("tisort-simge", tisortParcalari(922, 368, 96, 86, 3.4), 146.04, 0.35, 1)` |

### N — not satırı ve 7 pm (doğrudan `S.koy`)

| # | Zaman | Sözcük | Öğe |
|---|---|---|---|
| N1 | 149,69 / 151,05 | today · geliyor: | `eN1 = S.elYazisi({ metin: "today + 7 pm", x: 88, y: NY, boy: 72, renk: RT.murekkep, sozcukler: [{ t0: t(10), t1: t1(10) }, { t0: t(13), t1: t(13) + 0.22 }, { t0: t(13) + 0.26, t1: t(13) + 0.42 }, { t0: t(13) + 0.44, t1: t1(13) }] })` (yatay kalıbı) |
| N2 | `t(12)` 150,57 | saatle | *7 pm* altı (dar öbek → halka değil `alti`): `A = cum.kel[6]`, `B = cum.kel[7]`; `sonenOdak(A.x - 6, B.x + B.w + 6, altY(B.y, 72, "7 pm"), 11, t(12), t(24), 0.55)` — 157,21'de ikincile döner |
| N3 | `t(14)` 151,85 | akşam | 7 pm çentiği: `S.darbe([[X7, TY - 16], [X7, TY + 16]], { duz: true, w: 5, renk: RT.murekkep, uc0: 3, uc1: 3, tohum: 211 }, t(14), 0.15, 0.45)` + `nokta(X7, TY, 10, t(14) + 0.1, RT.murekkep)` |
| N4 | 152,25–152,96 | yedi. | `S.elYazisi({ metin: "7 pm", x: X7 - eyGen("7 pm", 64) / 2, y: ETY, boy: 64, renk: RT.murekkep, sozcukler: [{ t0: t(15), t1: t(15) + 0.3 }, { t0: t(15) + 0.32, t1: t(16) - 0.05 }] })` |
| N5 | `t(17)` 153,45 | henüz | now → 7 pm yayı: `yayOk([NX + 14, TY - 20], [X7 - 8, TY - 22], 50)` → 3 parça; parça 0 gövde `{ w: 4.6, renk: RT.ikincil, uc0: 6, uc1: 8, tohum: 220 }`, `t(17)`, `sure 0.8`, `ses 0.5`; parça 1–2 ok ucu `{ …, duz: true, tohum: 221 / 222 }`, `t(17) + 0.75`, `0.12`, `false`. Tepe ≈ y 1108 (bandın içinde) |
| N6 | `t(20)` 154,93 | tarifede | not oku: `ox = 88 + eN1.w + 18`; gövde `S.darbe([[ox, NY - 20], [ox + 56, NY - 20]], { duz: true, w: 4.5, renk: RT.murekkep, uc0: 4, uc1: 6, tohum: 240 }, t(20), 0.2, 0.45)`; iki uç (`ok()` uçları) `t(20) + 0.18`, `0.08`, `false` |
| N7 | 155,23–155,96 | yazılı. | `S.elYazisi({ metin: "timetable", x: ox + 74, y: NY, boy: 72, renk: RT.murekkep, sozcukler: [{ t0: t(20) + 0.3, t1: t1(21) - 0.05 }] })` |

### O — odak (doğrudan `S.koy`)

| # | Zaman | Sözcük | Öğe |
|---|---|---|---|
| O1 | `t(22)` 156,09 | Geniş | *leaves* (kalıcı): `K = cum.kel[4]`; `altCizgi(K.x - 6, K.x + K.w + 6, altY(K.y, 72, K.m), 12)`, `tohum 2`, `ses 0.55` |
| O2 | `t(24)` 157,21 | Today | iki *today* aynı anda (kalıcı): şerit `xs = 88 + olc(FF(56), "is wearing … ")`, `ws = olc(FF(56), "today")`, `y = altY(430, 56, "today")`, `w: 8`, `tohum 3`, `ses 0.55`; kart `K = cum.kel[8]`, genişlik `olc(FF(72), "today")` (noktasız), `y = altY(K.y, 72, "today")`, `tohum 4`, `ses false`. Ş2–Ş4 52'ye düştüyse şerit ölçüsü 52 ile |

Sarı sayımı: 150,57 → 1 (7 pm) · 156,09 → 2 · 157,21 → 3 (leaves + iki today; 7 pm ikincile döner). Hiçbir anda 3'ten çok sarı yok.

### E — alt satır (doğrudan `S.koy`)

| # | Zaman | Sözcük | Öğe |
|---|---|---|---|
| E1 | `t(29)` 159,05 | Farkı | `esitDegil(570, 1346)` her parça `S.darbe(p, { duz: true, w: 7, renk: RT.murekkep, alfa: 0.9, uc0: 4, uc1: 8, tohum: 700 + i }, t(29) + i * 0.12, 0.14, i ? false : 0.5)` |
| E2 | 160,57–161,21 | konuşma anı | `S.elYazisi({ metin: "RIGHT NOW", x: NX - eyGen("RIGHT NOW", 64) / 2, y: EY, boy: 64, renk: RT.murekkep, sozcukler: [{ t0: t(32), t1: t1(32) }, { t0: t(33), t1: t1(33) }] })` |
| E3 | 161,61–162,11 | tarife | `S.elYazisi({ metin: "TIMETABLE", x: X7 - eyGen("TIMETABLE", 64) / 2, y: EY, boy: 64, renk: RT.murekkep, sozcukler: [{ t0: t(35), t1: t(35) + 0.5 }] })` |

Türkçe çeviri YOK (yatayda yok). Altyazıyı kit çizer; sahne.js altyazıya dokunmaz.

## 7. Kurallar

1. Zaman yalnız kareden (`S.fr`, `S.zm`, `t(i)`, `t1(i)`); sabit saniye yalnız bu SPEC'teki değerler (`HZ`, 145.72, 145.80, 145.92 …).
2. Aynı anda en çok 3 sarı (`RT.vurgu`) belirteç (§6 sayımı). Karaoke altı kitten gelir (`vurguDolgu`).
3. Boş çerçeve ≤ 0,6 sn (kart 0,04 · şerit 0,04).
4. Kare 0–12 durgun 08 düzeni (ilk hareket 145,72 = kare 13); son hareket 162,11 (kare 505); `nabiz` `ICERIK`'te durur.
5. Hiçbir öğe y < 352 ya da y > 1392'ye taşmaz; x 48–1032 dışına çıkmaz. Yazı kutusu çizim kutusuna değmez.
6. Satır kodu ≤ 100 karakter, 2 boşluk girinti, dosya sonu boş satır. Her öğe bloğunun üstünde tek satır yorum:
   `// 146,00 train: tren simgesi` (zaman + tetik sözcüğü). Dosya başında 2 satır açıklama (04 dikey gibi).

## 8. Kabul ölçütü (şef doğrular)

- `node --check sahne.js` geçer.
- `cd /home/sef/01dev/_worktrees/kalem-0204 && bash araclar/qa-yerel.sh 02-04-ydt-temel-dikey 09-canvas-karsit2 149.0,156.6,162.2 162.2 --hazirla`
  → `kapı çıkış kodu: 0`.
- 149,0: şerit + tişört simgesi + kart cümlesi tam + tren + bant/now · 156,6: not satırı tam (`today + 7 pm → timetable`),
  7 pm çentik + etiket + yay, *7 pm* ve *leaves* altı · 162,2: iki *today* altı, `RIGHT NOW ≠ TIMETABLE`; taşma, kesik yazı,
  üst üste binme, altyazıyla çakışma yok.
