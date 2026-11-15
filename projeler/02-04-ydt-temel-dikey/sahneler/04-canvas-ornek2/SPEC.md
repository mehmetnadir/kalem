# SPEC — 02-04 dikey · sahne 04-canvas-ornek2 (düz canvas, 1080×1920)

Şef tasarımı (15.11). Uygulayan agy yalnız şu dosyayı yazar:

**`/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-dikey/sahneler/04-canvas-ornek2/sahne.js`**

Başka dosyaya dokunma. Silme yok. Test, render, git yok. `sahne-ortak.js`, `sayfa.html`, `calistir.sh` hazır; değiştirme.

## 1. Okunacak kaynaklar (kalıp)

| Dosya | Ne alınır |
|---|---|
| `/home/sef/01dev/_worktrees/kalem-0204/projeler/present-continuous-dikey/sahneler/04-canvas-ornek2/sahne.js` | dikey dosya iskeleti: `import`, `new Sahne`, `svgOku`, `pen`/`eyGen` yardımcıları, `kur()` içinde `S.koy(...)`, son satır `surucu(kur, (f) => S.kare(f), KARE)` |
| `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel/sahneler/04-canvas-ornek2/sahne.js` | İÇERİK ve olay sırası (yatay): `t(i) = S.sozc[i].t0`, 49 sözcük denetimi (`throw`), `Istanbul → İstanbul` düzeltmesi, `BAVUL_SVG` dizesi, zaman çizgisi kalıbı (`ok()` → `[[a,b], uc1, uc2]` + `duz: true`). YERLEŞİM ALINMAZ |
| `./sahne-ortak.js` (bu dizin) | API: `Sahne`, `S.kur`, `S.fr`, `S.zm`, `S.koy`, `S.olay`, `S.darbe`, `S.darbeler`, `S.elYazisi`, `S.cizim`, `S.metinPop`, `S.cumleYaz` (yeni: `satirSay`), `S.kart`, `S.daireSayi(sayi, cx, cy, tb, r)`, `S.nabiz`, `olc`, `altY`, `RT`, `RENK`, `renkCoz`, `elips`, `ok`, `altCizgi`, `lerp`, `yavasla`, `kis` |

İçe aktarım:
- `surucu` → `/ortak/surucu.js`
- `Sahne` ve yardımcılar → `./sahne-ortak.js`
- `yaziNoktalari` → `/projeler/02-04-ydt-temel-dikey/ortak/kalem-canvas.js` (el yazısı genişliği; örnekteki `eyGen`)
- SVG kökü: `/projeler/02-04-ydt-temel-dikey/ortak/cizim`

## 2. Sabitler

`KARE = 762`, `TBAS = 43.85`, `ICERIK = 750`.
`new Sahne({ tbas: TBAS, kare: KARE, icerik: ICERIK, klasor: "04-canvas-ornek2", cumle: 4 })` — `bolum` VERME (çip `KUNYE.cipler`'den gelir: `Example 2 / 3`).
Fontlar: `FF(b) = "700 ${b}px Fredoka"`, `FC(b) = "700 ${b}px Caveat"`. Sabit px yerine bu SPEC'teki BRIEF-DIKEY ölçüleri kullanılır (tuval 1080 sabit; `u()` gerekmez).
Renk yalnız `RT.*` (`murekkep`, `ikincil`, `vurgu`, `vurguDolgu`, `zemin`). Hex renk, kırmızı, yeşil, emoji, `Math.random`, `Date`, try/catch YOK.

`kur()` başında: `await S.kur()`; `S.sozc.length !== 49` ise `throw new Error(...)`. `t = (i) => S.sozc[i].t0`.

## 3. Sözcük dizini (cümle 4, küresel sn)

```
0 İkinci 44.40 · 2 Kancadaki 45.76 · 4 live. 47.20 · 5 I 48.09 … 11 family. 49.61 · 12 Ailemle 50.82
15 Orada 52.90 · 16 hep 53.30 · 18 Kalıcı 54.58 · 20 geniş 55.54 · 21 zaman. 55.86–56.82
22 My 56.99 … 34 uncle. 59.95 · 37 dışında, 62.28 · 42 Bu 65.00 · 44 şimdilik. 65.60–66.76
45 Geçici 66.84 · 47 şimdiki 67.88 · 48 zaman. 68.28–68.92
```

## 4. Yerleşim (px, 1080×1920; içerik bandı 352–1392, kenar 48)

```
 352 ┌ şerit (56,50'den sonra) 352–472: [live] → [PERMANENT]          [ev 96] ┐
 380 │ (2) live            ← A evresi: daire + live 140 + sarı altı (360–525)  │
 490 │                     ← B: Kart B 490–818 (3 satır, 72)                   │
 540 │ Kart A 540–776 (2 satır, 72)                                           │
 792 │ Ev 792–1212 (420)   ← B: Bavul 845–1265 (420)                          │
1230 │ PERMANENT / zaman çizgisi A (eksen y 1330)  ← B: zaman çizgisi B (y 1330) │
1392 └────────────────────────────────────────────────────────────────────────┘
1400–1536 altyazı (kit çizer) · 1536–1920 boş
```

## 5. Olay listesi (sırayla; zaman = küresel sn)

### A evresi (grup A; hepsi tek dizide toplanır, `S.koy` ile DEĞİL, §6 grup öğesiyle eklenir)

| # | Zaman | Sözcük | Öğe | Yerleşim ve ölçü |
|---|---|---|---|---|
| A1 | `t(0)` 44,40 | İkinci | `S.daireSayi(2, 96, 428, t(0), 48)` | 96 px daire, sol üst (x 48–144, y 380–476) |
| A2 | `t(4)` 47,20 | live. | `S.metinPop` `[["live", RT.murekkep]]`, `FF(140)`, `x 184`, `y 486` (taban), `sure 0.3`, `olcek0 0.85`, `ses 0.5`, `turu "tik"` | daire sağında, sola hizalı |
| A3 | `t(4)+0.35` 47,55 | live. | sarı altı: `S.darbe(altCizgi(184-6, 184+wLive+6, 520, 401), { w: 10, renk: RT.vurgu, alfa: 0.9, uc0: 8, uc1: 14, tohum: 401 }, t, 0.35, 0.55)`; `wLive = olc(FF(140), "live")` | y 520 |
| A4 | 47,70 | — | Kart A çerçevesi `S.kart({ x: 48, y: 540, w: 984, h: 236, tb: 47.70, ad: "kartA", tohum: 4, kutuSure: 0.14, kutuAralik: 0.08, satirlar: [] })` | 540–776; ilk sözcükten 0,39 sn önce |
| A5 | 48,09–49,61 | I … family. | `S.cumleYaz({ sozcukler: S.sozc.slice(5, 12)` (Istanbul → İstanbul) `, x: 88, y: 636, font: FF(72), satirH: 92, satirSay: [4, 3], bosluk: 6 })` → `cumA` | taban 636 / 728; `I live in İstanbul` / `with my family.` |
| A6 | `t(12)` 50,82 | Ailemle | Ev: `S.cizim({ svg: evSvg, ad: "ev", kutu: { x: 330, y: 792, w: 420, h: 420 }, enCok: 10, esik: 0.01, w: 4.4, tb: t(12), sure: 1.0, olayEnCok: 4, nefes: false })`. `evSvg` = `tabler/home.svg` metni, `viewBox="0 0 24 24"` → `viewBox="2.5 2.5 19 19"` ile değiştirilmiş (çizim kutuyu doldursun, ≈ 400 px) | bant ortası |
| A7 | `t(16)` 53,30 | hep | uzun bant (eksenin ALTINDA kalsın diye önce eklenir): `S.darbe([[150, 1330], [930, 1330]], { duz: true, w: 30, renk: RT.vurguDolgu, alfa: 0.45, uc0: 4, uc1: 8, tohum: 101 }, t(16), 1.0, 0.5)` | uç çentiği YOK (kalıcı = açık uçlu; B'de var) |
| A8 | `t(15)` 52,90 | Orada | eksen: `ok([96, 1330], [984, 1330], 21)` → `S.darbeler([[[96,1330],[984,1330]], uc1, uc2], { duz: true, w: 4, renk: RT.ikincil, uc0: 6, uc1: 12 }, t(15), 0.4, 0.15, 0.4)` | y 1330, sağ ok |
| A9 | `t(15)+0.25` 53,15 | Orada | now noktası `nowNokta(540, 1330, t)` (§6) + `S.nabiz(540, 1330, 14, t + 0.35)` | |
| A10 | `t(15)+0.40` 53,30 | Orada | `now` el yazısı: `S.elYazisi({ metin: "now", x: 540 - g/2, y: 1390, boy: 64, renk: RT.murekkep, tb, sure: 0.4 })`, `g = eyGen("now", 64)` | noktanın altında, ortalı |
| A11 | `t(18)` 54,58 | Kalıcı | `PERMANENT`: `S.elYazisi({ metin: "PERMANENT", x: 150, y: 1298, boy: 72, renk: RT.murekkep, sozcukler: [{ t0: t(18), t1: t(20) }] })` | bandın üstünde, solda; 54,58–55,54 yazılır |
| A12 | `t(20)` 55,54 | geniş | odak *live*: `K = cumA.kel[1]`; `S.darbe(altCizgi(K.x-6, K.x+K.w+6, altY(K.y, 72, K.m), 11), { w: 9, renk: RT.vurgu, alfa: 0.9, uc0: 8, uc1: 14, tohum: 501 }, t(20), 0.4, 0.55)` | kuyruğa değmez (`altY`) |

### Geçiş — çift kart kuralı (BRIEF-DIKEY §2.5)

| # | Zaman | Öğe |
|---|---|---|
| G1 | 56,20–56,56 | Grup A küçülür ve söner (§6 `grupKucul(ogelerA, 56.20, 0.36)`): ölçek 1 → 0,12, odak `(540, 380)`, alfa 1 → 0; 56,56'dan sonra grup ÇİZİLMEZ |
| G2 | 56,50 | şerit çerçevesi `S.kart({ x: 48, y: 352, w: 984, h: 120, tb: 56.50, ad: "serit", tohum: 8, kutuSure: 0.1, kutuAralik: 0.05, satirlar: [] })` |
| G3 | 56,54 | `live` `S.metinPop([["live", RT.murekkep]], FF(64), x 88, y 434, sure 0.3, ses 0.4)` |
| G4 | 56,60 | ok: `ok([xL + 24, 412], [xL + 134, 412], 23)` (`xL = 88 + olc(FF(64), "live")`) → `S.darbeler(..., { w: 6, renk: RT.ikincil, uc0: 6, uc1: 10 }, 56.60, 0.16, 0.06, false)` |
| G5 | 56,68 | `PERMANENT` `S.metinPop([["PERMANENT", RT.murekkep]], FC(64), x xL + 158, y 434, sure 0.3, ses false)` |
| G6 | 56,62 | ev simgesi `S.cizim({ svg: evSvg, ad: "ev-simge", kutu: { x: 912, y: 364, w: 96, h: 96 }, enCok: 10, esik: 0.01, w: 4, tb: 56.62, sure: 0.35, olayEnCok: 1, nefes: false })` |

### B evresi (doğrudan `S.koy`)

| # | Zaman | Sözcük | Öğe | Yerleşim |
|---|---|---|---|---|
| B1 | `t(22)-0.35` 56,64 | My | Kart B çerçevesi `S.kart({ x: 48, y: 490, w: 984, h: 328, tb, ad: "kartB", tohum: 6, kutuSure: 0.14, kutuAralik: 0.08, satirlar: [] })` | 490–818 |
| B2 | 56,99–59,95 | My … uncle. | `S.cumleYaz({ sozcukler: S.sozc.slice(22, 35), x: 88, y: 586, font: FF(72), satirH: 92, satirSay: [5, 5, 3], bosluk: 6 })` → `cumB` | `My parents are out of` / `town, so I am living` / `with my uncle.`; taban 586 / 678 / 770. KURAL: en uzun satır `olc` ile > 904 px ise font `FF(64)`, `satirH 84` |
| B3 | `t(37)` 62,28 | dışında, | Bavul: `S.cizim({ svg: BAVUL_SVG_DIKEY, ad: "bavul", kutu: { x: 356, y: 845, w: 268, h: 420 }, enCok: 10, esik: 0.01, w: 4.4, tb: t(37), sure: 1.0, olayEnCok: 4, nefes: false })`. `BAVUL_SVG_DIKEY` = yatay `BAVUL_SVG` dizesi, yalnız `viewBox="0 0 24 24"` → `viewBox="5 2 14 22"` | ≈ 267×420; QA tur 1: x 406 → 356 (sağda TEMPORARY'ye yer) |
| B4 | `t(44)` 65,60 | şimdilik. | kısa bant (önce eklenir): `S.darbe([[470, 1330], [610, 1330]], { duz: true, w: 30, renk: RT.vurguDolgu, alfa: 0.45, uc0: 4, uc1: 8, tohum: 102 }, t(44), 0.4, 0.5)` | now (540) bandın içinde |
| B5 | `t(42)` 65,00 | Bu | eksen: A8 ile aynı, `tohum 22` | y 1330 |
| B6 | `t(44)+0.40` / `+0.52` | şimdilik. | uç çentikleri: `[[470, 1304], [470, 1356]]` ve `[[610, 1304], [610, 1356]]`, `{ duz: true, w: 6, renk: RT.vurgu, uc0: 3, uc1: 3, tohum: 103 / 104 }`, `sure 0.18`, `ses 0.4` | 66,00 / 66,12 |
| B7 | `t(42)+0.25` 65,25 | Bu | `nowNokta(540, 1330, t)` + `S.nabiz(540, 1330, 14, t + 0.35)` | |
| B8 | `t(42)+0.40` 65,40 | Bu | `now` el yazısı, A10 ile aynı ölçü | |
| B9 | `t(45)` 66,84 | Geçici | `TEMPORARY`: `S.elYazisi({ metin: "TEMPORARY", x: 632, y: 1300, boy: 64, renk: RT.murekkep, sozcukler: [{ t0: t(45), t1: t(47) }] })`. QA tur 1: 72 px / x 690'da Y ucu x 1043'e taştı ve kuyruğu ok ucuna değdi | kısa bandın SAĞINDA (uç 610), ok ucundan (≈ 952) önce; bavul kutusuna (x ≤ 624) değmez |
| B10 | `t(47)` 67,88 | şimdiki | odak *am living*: `A = cumB.kel[8]`, `B = cumB.kel[9]`; `S.darbe(altCizgi(A.x-6, B.x+B.w+6, altY(B.y, boyB, "living"), 12), { w: 9, renk: RT.vurgu, alfa: 0.9, uc0: 8, uc1: 14, tohum: 502 }, t(47), 0.4, 0.55)` (`boyB` = B2'de seçilen font boyu) | `g` kuyruğunun altından |

Türkçe çeviri YOK (yatayda yok). Altyazıyı kit çizer; sahne.js altyazıya dokunmaz.

## 6. sahne.js içinde yazılacak iki yardımcı (yalnız davranış tarifi)

**`nowNokta(cx, cy, tb)`** → öğe `{ ciz(ctx, f) }`. `fb = S.fr(tb)`; `u = yavasla((f - fb) / 7.5)`; `u <= 0` ise çizme.
Dolu daire: yarıçap `13 × lerp(0.6, 1, u)`, dolgu `renkCoz(RT.vurgu)`, çevresi `renkCoz(RT.zemin)` 5 px çizgi (bant üstünde iki temada seçilsin), `globalAlpha = u`; `ctx.save/restore`.
Oluşturulurken bir kez `S.olay(fb, "tik", 0.4)`.

**`grupKucul(ogeler, t0, sure)`** → öğe `{ ciz(ctx, f) }`. `ogeler` düz dizi (iç diziler `flat()` ile açılır).
- `f < S.fr(t0)`: her öğeyi doğrudan `ctx` üstüne çiz (kutu kaydı normal).
- `S.fr(t0) ≤ f < S.fr(t0 + sure)`: `u = yavasla((f - S.fr(t0)) / (sure × 30))`. Öğeleri `kur()` içinde BİR KEZ oluşturulan 1080×1920 gizli tuvale çiz (her karede `clearRect`). Bu çizim sırasında `window.__kalemKutu.ekle` geçici olarak boş işlevle değiştirilir, sonra eski hâline döner (sönen grup çakışma kapısına kutu yazmaz). Sonra ana `ctx`: `save` → `globalAlpha = 1 - u` → odak `(540, 380)` çevresinde `scale(lerp(1, 0.12, u))` → `drawImage(gizli, 0, 0)` → `restore`.
- `f ≥ S.fr(t0 + sure)`: hiçbir şey çizme.

## 7. Kurallar

1. Zaman yalnız kareden (`S.fr`, `S.zm`, `t(i)`); sabit saniye yalnız bu SPEC'teki değerler.
2. Aynı anda en çok 3 sarı (`RT.vurgu`) belirteç. Karaoke altı kitten gelir (`vurguDolgu`).
3. Altçizgi y'si her yerde `altY(taban, boy, metin)` (kuyruklu sözcükte kuyruğun altı).
4. Boş çerçeve ≤ 0,6 sn bekler (kart A 0,39 sn, kart B 0,35 sn, şerit 0,04 sn).
5. İlk 12 kare boş (ilk öğe 44,40 = kare 17); son 12 kare durgun (son hareket 68,28 biter; `nabiz` içerik sonunda durur).
6. Hiçbir öğe y < 352 ya da y > 1398'e taşmaz; x 48–1032 dışına çıkmaz.
7. Satır kodu ≤ 100 karakter, 2 boşluk girinti, dosya sonu boş satır. Her öğe bloğunun üstünde tek satır yorum: `// 47,20 live.: …` (zaman + tetik sözcüğü).

## 8. Kabul ölçütü (şef doğrular)

- `node --check sahne.js` geçer.
- `cd /home/sef/01dev/_worktrees/kalem-0204 && bash araclar/qa-yerel.sh 02-04-ydt-temel-dikey 04-canvas-ornek2 56.2,63.5,68.6 68.6 --hazirla` → `kapı çıkış kodu: 0`.
- Karelerde: taşma, kesik yazı, üst üste binme, okunmaz kontrast, boş kare, altyazıyla çakışma yok; 68,6'da şerit + kart B + bavul + zaman çizgisi B bandı dolu (≥ %85).
