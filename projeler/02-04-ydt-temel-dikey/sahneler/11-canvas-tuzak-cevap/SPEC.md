# SPEC — 02-04 dikey · sahne 11-canvas-tuzak-cevap (düz canvas, 1080×1920)

> **16.11 DUZ3:** cümle 13 «Ailenle hep orada yaşıyorsan» → «Ailenle kalıcı olarak yaşıyorsan»; not «always» → «long-term» (EK-5c); 643 kare; TBAS 183,79 eski çerçeve + KAYMA −1,68; cümle içi sabit zamanlar sözcüğe bağlı. Bu belgedeki saniye ve metinler önceki sürümündür; geçerli olan kod + `zaman.json`.

Şef tasarımı (15.11). Uygulayan agy yalnız şu dosyayı yazar:

**`/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-dikey/sahneler/11-canvas-tuzak-cevap/sahne.js`**

Başka dosyaya dokunma. Silme yok. Test, render, git yok. `sahne-ortak.js`, `sayfa.html`, `calistir.sh` hazır; değiştirme.

## 1. Okunacak kaynaklar (kalıp)

| Dosya | Ne alınır |
|---|---|
| `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-dikey/sahneler/04-canvas-ornek2/sahne.js` | DİKEY İSKELET (birebir kalıp): `import` satırları, `new Sahne({... klasor ...})`, `svgOku`, `FF`/`FC`, `eyGen`, `nowNokta(cx, cy, tb)` yardımcısı (AYNEN al), zaman çizgisi kalıbı (bant → eksen `ok()` + `S.darbeler` → now noktası + `S.nabiz` → `now` el yazısı), odak altçizgisi `altCizgi(...)` + `S.darbe` (y bu SPEC §5 ve §7.3'ten, `altY` DEĞİL), son satır `surucu(kur, (f) => S.kare(f), KARE)`. `grupKucul` bu sahnede YOK |
| `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel/sahneler/11-canvas-tuzak-cevap/sahne.js` | İÇERİK ve olay sırası (yatay): `S.dizi("I", 187.11, 5)` / `S.dizi("I", 194.89, 4)`, `Istanbul → İstanbul`, `≠` üç darbe kalıbı, not oku `notOk`, öğrenci başı `S.cizim` + `og.donusum` baş sallama. YERLEŞİM ve `u()` ALINMAZ (dikey tuval 1080 sabit; px bu SPEC'ten) |
| `./sahne-ortak.js` (bu dizin) | API: `Sahne`, `S.kur`, `S.fr`, `S.zm`, `S.t0`, `S.dizi`, `S.koy`, `S.olay`, `S.bas`, `S.darbe`, `S.darbeler`, `S.elYazisi` (döner `{x, w}`), `S.cizim`, `S.cumleYaz` (`satirSay`, döner `{kel}`), `S.kart`, `S.nabiz`, `olc`, `altY`, `RT`, `renkCoz`, `ok`, `altCizgi`, `lerp`, `yavasla`, `kis` |

İçe aktarım (04 dikeyle aynı):
- `surucu` → `/ortak/surucu.js`
- `Sahne` ve yardımcılar → `./sahne-ortak.js`
- `yaziNoktalari` → `/projeler/02-04-ydt-temel-dikey/ortak/kalem-canvas.js` (`eyGen` el yazısı genişliği)
- SVG kökü: `/projeler/02-04-ydt-temel-dikey/ortak/cizim`; öğrenci başı `peeps-kit/ogrenci-bas.svg`

## 2. Sabitler

`KARE = 657`, `TBAS = 183.79`, `ICERIK = 645`.
`new Sahne({ tbas: TBAS, kare: KARE, icerik: ICERIK, klasor: "11-canvas-tuzak-cevap", cumle: 13 })` — `bolum` VERME
(çip `KUNYE.cipler`'den gelir: `Trap · answer`). `KUNYE` import etme, ajanda/`etkin` yok.
Fontlar: `FF(b) = "700 ${b}px Fredoka"`, `FC(b) = "700 ${b}px Caveat"`. Tuval 1080 sabit; `u()` YOK; px bu SPEC'ten.
Renk yalnız `RT.*` (`murekkep`, `ikincil`, `vurgu`, `vurguDolgu`, `zemin`). Hex renk, kırmızı, yeşil, emoji, `Math.random`,
`Date`, try/catch YOK.

`kur()` başında: `await S.kur()`; `S.sozc.length !== 39` ise `throw new Error(...)`. `t = (i) => S.sozc[i].t0`.

## 3. Sözcük dizini (cümle 13, küresel sn; `t(i)`)

```
0 Olur, 184.54 · 1 ama 185.42 · 2 anlam 185.90 · 3 değişir. 186.22–186.86
4 I 187.11 · 5 am 187.27 · 6 living 187.47 · 7 in 187.67 · 8 Istanbul. 187.83–188.95
9 Şimdilik 189.12 · 10 İstanbul'da 189.68 · 11 yaşıyorum 190.24 · 13 Geçici. 191.55–192.44
14 Ailenle 192.48 · 15 hep 193.12 · 16 orada 193.36 · 17 yaşıyorsan: 193.60–194.72
18 I 194.89 · 19 live 195.13 · 20 in 195.45 · 21 Istanbul. 195.61–196.65
22 Türkçede 196.90 · 23 yor 197.70 · 31 ayrılır. 201.30 · 32 Kalıcı 202.74 · 34 geçici 203.46 · 38 sor. 204.86–205.38
```

Cümleler: `a = S.sozc.slice(4, 9)` → `I am living in İstanbul.` · `b = S.sozc.slice(18, 22)` → `I live in İstanbul.`
(ikisinde de `sozcuk` içindeki `Istanbul` → `İstanbul`, 04 dikeydeki `map` kalıbı).

## 4. Yerleşim (px, 1080×1920; içerik bandı 352–1392, kenar 48)

```
 380 ┌ Kart 1 (x 48, w 984, h 140) 380–520: I am living in İstanbul.  (Fredoka 72, taban 460, x 88)   ┐
 592 │ → for now (temporary)        (ok x 88–152 · Caveat 64 x 172, taban 592)                       │
 670 │ ──────────────────[kısa bant 690–830]──●now(760)──────────────► eksen 1, now taban 730        │
 840 │            ≠  meaning        (≠ sarı kalem + Caveat 88, ortalı x 540, taban 840)              │
 910 │ Kart 2 910–1050: I live in İstanbul.  (Fredoka 72, taban 990, x 88)                            │
1120 │ → long-term (permanent)         (ok x 88–152 · Caveat 64 x 172, taban 1120)                      │
1196 │ ──[uzun bant 150–880]────────────────●now(760)─────────────────► eksen 2, now taban 1256      │
1228 │                                                       [öğrenci başı x 892–1009, y 1228–1388]  │
1392 └──────────────────────────────────────────────────────────────────────────────────────────────┘
1400–1536 altyazı (kit çizer) · 1536–1920 boş
```

Not sütunu iki kartta aynı x (ok 88 → 152, yazı 172). now x iki çizgide aynı (760).

## 5. Olay listesi (sırayla; zaman = küresel sn; hepsi `S.koy`)

| # | Zaman | Sözcük | Öğe | Yerleşim ve ölçü |
|---|---|---|---|---|
| 1 | 184,20 | (cevap öncesi) | Öğrenci başı: `og = S.cizim({ svg: basSvg, ad: "ogrenci", kutu: { x: 892, y: 1228, w: 117, h: 160 }, esik: 0.004, enCok: 60, w: 4, tb: 184.2, sure: 0.55, olayEnCok: 3, nefes: false })` | alt sağ; ilk öğe kare 12 |
| 2 | `t(0)` 184,54 | Olur, | Kart 1 çerçevesi `S.kart({ x: 48, y: 380, w: 984, h: 140, tb: t(0), ad: "kart-1", tohum: 11, kutuSure: 0.2, kutuAralik: 0.12, satirlar: [] })` | 380–520 |
| 3 | `t(2)` 185,90 (+0,1 arayla) | anlam | `≠` üç sarı darbe (§6 `esitDegil`) | ≠ kutusu x `nx0`…`nx0+72`, merkez y 814 |
| 4 | `t(3)` 186,22 | değişir. | `nM = S.elYazisi({ metin: "meaning", x: nx0 + 72 + 26, y: 840, boy: 88, renk: RT.murekkep, tb: t(3), sure: 0.6 })` | `wM = eyGen("meaning", 88)`, `nx0 = 540 − (72 + 26 + wM) / 2` (grup ortalı) |
| 5 | 187,11–188,95 | I … Istanbul. | `c1 = S.cumleYaz({ sozcukler: a, x: 88, y: 460, font: FF(72), satirH: 92, satirSay: [5], bosluk: 6 })` | tek satır; karaoke altını kit çizer |
| 6 | `t(9)` 189,12 | Şimdilik | not oku (§6 `notOk(592, t(9), 231)`), sonra `S.elYazisi({ metin: "for now", x: 172, y: 592, boy: 64, renk: RT.murekkep, tb: t(9) + 0.18, sure: 0.5 })` | taban 592 |
| 7 | `t(10)` 189,68 · 190,00 · `t(11)` 190,24 | İstanbul'da · — · yaşıyorum | Zaman çizgisi 1: `zamanCizgisi({ TY: 670, bant: [690, 830], tEksen: t(10), tNokta: 190.0, tBant: t(11), bantSure: 0.4, tohum: 600, nowY: 730 })` (§6) | eksen y 670 |
| 8 | `t(13)` 191,55 | Geçici. | `nTmp = S.elYazisi({ metin: "(temporary)", x: 172 + eyGen("for now", 64) + 20, y: 592, boy: 64, renk: RT.murekkep, tb: t(13), sure: 0.75 })` | 191,55–192,30 |
| 9 | `t(14)` 192,48 | Ailenle | Kart 2 çerçevesi `S.kart({ x: 48, y: 910, w: 984, h: 140, tb: t(14), ad: "kart-2", tohum: 12, kutuSure: 0.2, kutuAralik: 0.12, satirlar: [] })` | 910–1050; 185,42'de ÇİZİLMEZ |
| 10 | `t(14)` 192,48 · 192,90 · `t(16)` 193,36 | Ailenle · — · orada | Zaman çizgisi 2: `zamanCizgisi({ TY: 1196, bant: [150, 880], tEksen: t(14), tNokta: 192.9, tBant: t(16), bantSure: 0.85, tohum: 620, nowY: 1256 })` | uzun bant 193,36–194,21 |
| 11 | `t(15)` 193,12 | hep | `notOk(1120, t(15), 241)`, sonra `S.elYazisi({ metin: "long-term", x: 172, y: 1120, boy: 64, renk: RT.murekkep, tb: t(15) + 0.16, sure: 0.45 })` | taban 1120 |
| 12 | 193,95 | yaşıyorsan: | `nPer = S.elYazisi({ metin: "(permanent)", x: 172 + eyGen("long-term", 64) + 20, y: 1120, boy: 64, renk: RT.murekkep, tb: 193.95, sure: 0.7 })` | |
| 13 | 194,89–196,65 | I … Istanbul. | `c2 = S.cumleYaz({ sozcukler: b, x: 88, y: 990, font: FF(72), satirH: 92, satirSay: [4], bosluk: 6 })` | tek satır |
| 14 | `t(23)` 197,70 | yor | odak *am living*: `A = c1.kel[1]`, `B = c1.kel[2]`; `altCizgi(A.x − 6, B.x + B.w + 6, B.y + 0.48 × 72, 11)`; `{ w: 9, renk: RT.vurgu, alfa: 0.9, uc0: 8, uc1: 14, tohum: 501 }`, `sure 0.4`, `ses 0.55`. §6 `donenAlti` ile (201,30'da ikincile döner) | `g` kuyruğunun altından (sözleşme: Fredoka taban + 0,48 × boy) |
| 15 | `t(23)+0.08` 197,78 | yor | odak *live*: `L = c2.kel[1]`; `altCizgi(L.x − 6, L.x + L.w + 6, L.y + 0.48 × 72, 12)`; tohum 502, `ses false`; `donenAlti` | |
| 16 | `t(31)` 201,30 | ayrılır. | *meaning* sarı altı: `altCizgi(nM.x − 6, nM.x + nM.w + 10, 840 + 0.52 × 88, 13)`; `{ w: 10, renk: RT.vurgu, alfa: 0.9, uc0: 8, uc1: 14, tohum: 503 }`, `sure 0.4`, `ses 0.55`. Aynı anda 14 ve 15 `ikincil`e döner | sağda +10 (tegaki genişlik payı) |
| 17 | 202,30–203,30 | (cevap bitimi) | öğrenci 1 sn baş sallar (§6 `og.donusum`) | |
| 18 | `t(32)` 202,74 | Kalıcı | *(permanent)* sarı altı: `altCizgi(nPer.x − 6, nPer.x + nPer.w + 10, 1120 + 0.52 × 64, 14)`; `{ w: 9, renk: RT.vurgu, alfa: 0.9, uc0: 8, uc1: 14, tohum: 504 }`, `sure 0.4`, `ses 0.5` | |
| 19 | `t(34)` 203,46 | geçici | *(temporary)* sarı altı: `altCizgi(nTmp.x − 6, nTmp.x + nTmp.w + 10, 592 + 0.52 × 64, 15)`; tohum 505, aynı stil | son hareket 203,86 |

Son durumda sarı belirteç 3: *meaning*, *(permanent)*, *(temporary)*. Fiil altları `ikincil` (kaybolmaz).
Türkçe çeviri yok (yatayda yok). Altyazıyı kit çizer; sahne.js altyazıya dokunmaz.

## 6. sahne.js içinde yazılacak yardımcılar (yalnız davranış tarifi)

**`nowNokta(cx, cy, tb)`** — 04 dikey `sahne.js`'teki işlevin AYNISI (kopyala).

**`esitDegil(tb)`** — `≠` üç darbe, sarı kalem: `NE = 72` genişlik, merkez `ncy = 814`, sol uç `nx0` (§5 satır 4).
Darbe 1: `[[nx0, ncy − 15], [nx0 + NE, ncy − 15]]` · darbe 2: `[[nx0, ncy + 15], [nx0 + NE, ncy + 15]]` · darbe 3 (eğik):
`[[nx0 + NE × 0.68, ncy − 38], [nx0 + NE × 0.32, ncy + 38]]`. Her biri `S.darbe(p, { duz: true, w: 9, renk: RT.vurgu, alfa: 0.9,
uc0: 4, uc1: 6, tohum: 300 + i }, tb + i × 0.1, 0.16, i ? false : 0.5)`. Çarpı YOK.

**`notOk(yb, tb, tohum)`** — not oku: `S.darbeler(ok([88, yb − 18], [152, yb − 18], tohum), { w: 6, renk: RT.murekkep, uc0: 6,
uc1: 10 }, tb, 0.16, 0.06, 0.4)` → `S.koy`.

**`zamanCizgisi({ TY, bant, tEksen, tNokta, tBant, bantSure, tohum, nowY })`** — ekleme SIRASI önemli (bant eksenin altında kalır):
1. Bant: `S.darbe([[bant[0], TY], [bant[1], TY]], { duz: true, w: 30, renk: RT.vurguDolgu, alfa: 0.45, uc0: 4, uc1: 8, tohum },
   tBant, bantSure, 0.5)`.
2. Eksen + sağ ok: `const [, u1, u2] = ok([96, TY], [984, TY], tohum + 1)`; `S.darbeler([[[96, TY], [984, TY]], u1, u2],
   { duz: true, w: 4, renk: RT.ikincil, uc0: 6, uc1: 12 }, tEksen, 0.4, 0.15, 0.4)`.
3. Uç çentikleri (her bant ucu, `murekkep`, sarı DEĞİL): `[[x, TY − 24], [x, TY + 24]]`, `{ duz: true, w: 6, renk: RT.murekkep,
   uc0: 3, uc1: 3, tohum: tohum + 4 + i }`, `tb = tBant + bantSure × 0.5 + i × 0.12`, `sure 0.18`, `ses i ? false : 0.4`.
4. now noktası: `nowNokta(760, TY, tNokta)` + `S.nabiz(760, TY, 14, tNokta + 0.35)`.
5. `now` el yazısı: `S.elYazisi({ metin: "now", x: 760 − gNow / 2, y: nowY, boy: 64, renk: RT.murekkep, tb: tNokta + 0.08,
   sure: 0.4, ses: false })`, `gNow = eyGen("now", 64)`.
Zaman çizgisi için elle kapı kutusu (`__kalemKutu.ekle`) YAZMA (04 dikeyde de yok).

**`donenAlti(pts, o, tb, tDon)`** — 201,30'da sarıdan `ikincil`e dönen altçizgi. İki darbe aynı `pts` ve aynı `tohum` ile kurulur:
`dS = S.darbe(pts, { ...o, renk: RT.vurgu }, tb, 0.4, ses)` ve `dI = S.darbe(pts, { ...o, renk: RT.ikincil }, tb, 0.4, false)`.
Döner öğe `{ ciz(ctx, f) }`: `u = yavasla((f − S.fr(tDon)) / 9)` (0,3 sn geçiş, `u` 0–1 arasına kırp).
`u ≤ 0` → yalnız `dS.ciz(ctx, f)`. Aksi hâlde `dS.carpan = 1 − u`, `dI.carpan = u`; önce `dI.ciz`, sonra `u < 1` ise `dS.ciz`.
`tDon = t(31)` (201,30).

**Öğrenci baş sallama** — `og.donusum = (f) => { ... }`: `p = (f − S.fr(202.3)) / 30`; `0 < p < 1` iken
`ty = 160 × 0.06 × sin(2πp)²`, değilse 0; döner `{ cx: 892 + 58.5, cy: 1228 + 160, tx: 0, ty, dondur: 0, olcek: 1 }`
(yatay sahnedeki kalıp; 2 vuruş, 1 sn).

## 7. Kurallar

1. Zaman yalnız kareden (`S.fr`, `S.zm`, `t(i)`); sabit saniye yalnız bu SPEC'teki değerler (184.2, 190.0, 192.9, 193.95,
   202.3).
2. Aynı anda en çok 3 sarı (`RT.vurgu`) belirteç (altçizgi). `≠` ve now noktası işarettir, sayılmaz. Karaoke altı kitten gelir.
3. Kalıcı sarı altçizgi (odak, *meaning*, parantezli not) y'si sözleşme kuralıyla: Fredoka cümlede taban + 0,48 × boy,
   Caveat notta taban + 0,52 × boy (yatay 11 QA: 0,36 g/y/p ve parantez kuyruğuna değdi). `altY` yalnız kitin karaoke altında.
4. İlk 12 kare boş (ilk öğe 184,20 = kare 12). Son 12 kare durgun (son hareket 203,86; `nabiz` içerik sonunda durur).
5. Hiçbir öğe y < 352 ya da y > 1392'ye taşmaz; x 48–1032 dışına çıkmaz.
6. Satır kodu ≤ 100 karakter, 2 boşluk girinti, dosya sonu boş satır. Her öğe bloğunun üstünde tek satır yorum:
   `// 189,12 Şimdilik: …` (zaman + tetik sözcüğü). Dosya başında 3–4 satır sahne özeti yorumu.

## 8. Kabul ölçütü (şef doğrular)

- `node --check sahne.js` geçer.
- `cd /home/sef/01dev/_worktrees/kalem-0204 && bash araclar/qa-yerel.sh 02-04-ydt-temel-dikey 11-canvas-tuzak-cevap
  192.4,199.5,204.5 204.5 --hazirla` → `kapı çıkış kodu: 0`.
- Karelerde: taşma, kesik yazı, üst üste binme, okunmaz kontrast, boş kare, altyazıyla çakışma yok; 204,5'te iki kart + iki not +
  iki zaman çizgisi + `≠ meaning` + öğrenci başı (bant 380–1388 dolu); 3 sarı altçizgi, fiil altları ikincil.
