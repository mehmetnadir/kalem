# SPEC — 02-04 dikey · sahne 08-canvas-karsit1 (düz canvas, 1080×1920)

Şef tasarımı (15.11). Uygulayan agy yalnız şu dosyayı yazar:

**`/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-dikey/sahneler/08-canvas-karsit1/sahne.js`**

Başka dosyaya dokunma. Silme yok. Test, render, git yok. `sahne-ortak.js`, `sayfa.html`, `calistir.sh` hazır; değiştirme.

## 1. Okunacak kaynaklar (kalıp)

| Dosya | Ne alınır |
|---|---|
| `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-dikey/sahneler/04-canvas-ornek2/sahne.js` | DİKEY iskelet (aynı paket, aynı `sahne-ortak.js`): `import` satırları, `new Sahne({... klasor ...})`, `FF`/`FC`/`t`/`eyGen` yardımcıları, `nowNokta()` işlevi (aynen al), `kur()` içinde `S.koy(...)`, son satır `surucu(kur, (f) => S.kare(f), KARE)`. Yorum biçimi `// 47,20 live.: …` |
| `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel/sahneler/08-canvas-karsit1/sahne.js` | İÇERİK ve olay sırası (yatay): `EN` sözcük zamanı dizisi (aynen al), `uzunluk()`, `elCizim()` (kalem çizimi grubu, `cizim` kutusu yazar), `tisortParcalari()` (100×90 ızgara). YERLEŞİM ve `u()` ALINMAZ: dikey tuval 1080 sabit, bu SPEC'teki px değerleri doğrudan kullanılır |
| `./sahne-ortak.js` (bu dizin) | API: `Sahne`, `S.kur`, `S.fr`, `S.zm`, `S.bas`, `S.koy`, `S.olay`, `S.darbe`, `S.darbeler`, `S.elYazisi`, `S.cumleYaz` (`satirSay`), `S.kart`, `S.nabiz`, `S.K.altyazi`, `olc`, `altY`, `RT`, `renkCoz`, `elips`, `ok`, `altCizgi`, `lerp`, `yavasla`, `kis` |

İçe aktarım: `surucu` → `/ortak/surucu.js` · `Sahne` ve yardımcılar → `./sahne-ortak.js` ·
`yaziNoktalari` → `/projeler/02-04-ydt-temel-dikey/ortak/kalem-canvas.js` (el yazısı genişliği, `eyGen`).

## 2. Sabitler

`KARE = 459`, `TBAS = 130.4`, `ICERIK = 447`.
`new Sahne({ tbas: TBAS, kare: KARE, icerik: ICERIK, klasor: "08-canvas-karsit1", cumle: 9 })` — `bolum` VERME (çip
`KUNYE.cipler` → `Contrast 1 / 2`). `FF(b) = "700 ${b}px Fredoka"`, `FC(b) = "700 ${b}px Caveat"`.
Renk yalnız `RT.*` (`murekkep`, `ikincil`, `vurgu`, `vurguDolgu`, `zemin`). Hex renk, kırmızı, yeşil, emoji, `Math.random`,
`Date`, try/catch YOK.

`kur()` başında: `await S.kur()`; `S.sozc.length !== 20` ise `throw new Error(...)`. `t = (i) => S.sozc[i].t0`.
`EN` (yatay dizi, 7 sözcük, küresel sn) aynen; `sozcukler.json`'da cümle 9 EN parçası YOK, bu yüzden sabit.

## 3. Sözcük dizini (cümle 9, `S.sozc`, küresel sn)

```
0 Karşıt 130.95 · 1 çift. 131.51 · 2 İki 132.55 · 6 var: 134.11 · 7 today. 134.95–135.35
8 Burada 138.57 · 9 today 139.21–139.69 · 10 bugünü 139.93 · 11 gösterir. 140.29–140.89 · 12 Bugünkü 141.29
13 kıyafet: 141.77 · 14 konuşma 142.57 · 15 anında 143.05 · 16 olan 143.57 · 17 durum, 143.77 · 18 şimdiki 144.37
19 zaman. 144.77–145.37
EN: She 135.61 · is 135.89 · wearing 135.97 · her 136.33 · pink 136.51 · T-shirt 136.87 · today. 137.29–137.69
```

## 4. Yerleşim (px, 1080×1920; içerik bandı 352–1392, kenar 48) — 08–09 ORTAK ÖLÇÜLER

```
 352 ┌────────────────────────────────────────────────────────────────┐
 378 │ today  (Caveat 80, x 88, taban 436)                              │  başlık notu
 490 │ ┌ Kart 48–1032 × 490–760 ───────────────────────────┬────────┐ │
 596 │ │ She is wearing her          (Fredoka 72, x 88)     │ tişört │ │  taban 596
 688 │ │ pink T-shirt today.                                │ 220 px │ │  taban 688
 760 │ └────────────────────────────────────────────────────┴────────┘ │
 790 │                       ↳ this day only   (not satırı 790–880)    │  kanca ok kartın today.'si altından
1040 │      ┌ today bandı x 200–880, y 1040–1180 (vurguDolgu %45) ┐     │
1180 │ ─────┼──●now (x 360)───────────────────────────────────────┼───▶ │  eksen x 96–984
1252 │        now  (Caveat 64)                                          │
1392 └────────────────────────────────────────────────────────────────┘
1400–1536 altyazı (kit çizer; §6.3 düzeltmesiyle) · 1536–1920 boş
```

## 5. Olay listesi (sırayla; zaman = küresel sn)

| # | Zaman | Sözcük | Öğe | Yerleşim ve ölçü |
|---|---|---|---|---|
| 1 | `t(7)` 134,95 | today. | başlık notu `nT = S.elYazisi({ metin: "today", x: 88, y: 436, boy: 80, renk: RT.murekkep, sozcukler: [{ t0: t(7), t1: S.sozc[7].t1 }] })` | sol üst, y ≈ 378–470 |
| 2 | `EN[0].t0 − 0.5` 135,11 | today. | Kart çerçevesi `S.kart({ x: 48, y: 490, w: 984, h: 270, tb, ad: "kart", tohum: 8, kutuSure: 0.14, kutuAralik: 0.08, satirlar: [] })` | 490–760; ilk sözcükten 0,5 sn önce (≤ 0,6 kuralı) |
| 3 | 135,61–137,69 | She … today. | `cum = S.cumleYaz({ sozcukler: EN, x: 88, y: 596, font: FF(72), satirH: 92, satirSay: [4, 3], bosluk: 6 })` | `She is wearing her` / `pink T-shirt today.`; taban 596 / 688; sağ uç ≈ 710 (PIL ölçümü 589 + 18 / 604 + 12) |
| 4 | `EN[5].t0` 136,87 | T-shirt | `tis = elCizim("tisort", tisortParcalari(772, 524, 2.2), EN[5].t0, 0.75)` | ≈ x 772–992, y 533–718 (220 × 185); kartın sağ iç köşesi |
| 5 | `t(8)` 138,57 | Burada | eksen: `ok([96, 1180], [984, 1180], 21)` → `S.darbeler([[[96,1180],[984,1180]], uc1, uc2], { duz: true, w: 4.5, renk: RT.ikincil, uc0: 6, uc1: 12 }, t(8), 0.5, 0.15, 0.45)` (04'teki eksen kalıbı) | y 1180, sağ ok ucu |
| 6 | `t(9)` 139,21 | today | odak kartta: `kT = cum.kel[6]`, `wT = olc(FF(72), "today")` (nokta hariç); `donen(altCizgi(kT.x − 6, kT.x + wT + 6, altY(kT.y, 72, "today"), 11), { w: 9, renk: RT.vurgu, alfa: 0.9, uc0: 8, uc1: 14, tohum: 501 }, t(9), 0.4, 0.55, t(18))` | y ≈ 714; 144,37'de `ikincil`e döner |
| 7 | `t(9) + 0.08` 139,29 | today | odak notta: `donen(altCizgi(84, 88 + nT.w + 4, 436 + 0.42 * 80, 12), { w: 8, renk: RT.vurgu, alfa: 0.9, uc0: 8, uc1: 14, tohum: 502 }, t(9) + 0.08, 0.4, false, t(13))` | y ≈ 470 (y kuyruğunun altı); 141,77'de `ikincil`e döner |
| 8 | `t(10)` 139,93 | bugünü | today bandı `bant(200, 880, 1040, 1180, t(10), 0.45)` (§6.2). Çizim sırası §7.4: bant ekseni örtmesin diye eksenden ÖNCE `S.koy` edilir | x 200–880, y 1040–1180 |
| 9 | `t(10) + 0.10` / `+ 0.22` | bugünü | uç çentikleri: `[[200, 1032], [200, 1198]]` ve `[[880, 1032], [880, 1198]]`, `{ duz: true, w: 5, renk: RT.murekkep, uc0: 3, uc1: 3, tohum: 212 / 213 }`, `sure 0.15`, ses `0.45` / `false` | bandın iki ucu, ekseni 18 px keser |
| 10 | `S.sozc[10].t0 + 0.12` 140,05 | bugünü | kanca ok (↳), kartın `today`'sinin altından: `cx = kT.x + wT / 2`; dikey darbe `[[xa, 774], [xa, 830]]` (`xa = cx`), 0,12 sn; sonra `ok([xa, 830], [xb, 830], 23)` → `S.darbeler(..., { duz: true, w: 5, renk: RT.murekkep, uc0: 4, uc1: 8 }, 140.17, 0.12, 0.06, false)`. `xb = xMetin − 18` (aşağı bak) | not satırı 790–880; dikey darbe ses `0.4` |
| 11 | `t(11)` 140,29–140,89 | gösterir. | `this day only`: `wD = eyGen("this day only", 72)`, `xMetin = Math.min(cx + 92, 1000 − wD)`; `S.elYazisi({ metin: "this day only", x: xMetin, y: 852, boy: 72, renk: RT.murekkep, sozcukler: [{ t0: t(11), t1: S.sozc[11].t1 }] })` | taban 852; sağ uç ≤ 1000 (K26 dikey eki: ≤ 1032) |
| 12 | `t(13)` 141,77 | kıyafet: | tişört halkası (sarı): `tc` = `tis.kut` merkezi; `S.darbe(elips(tc.x, tc.y, tis.kut.w / 2 + 14, tis.kut.h / 2 + 10, -0.05, 31), { w: 9, renk: RT.vurgu, alfa: 0.85, uc0: 14, uc1: 30 }, t(13), 0.45, 0.55)` | halka kart çerçevesine ve cümleye değmez (≈ x 750–1014, y 513–738) |
| 13 | `t(14)` 142,57 | konuşma | `nowNokta(360, 1180, t(14))` (04'teki işlev aynen) + `S.nabiz(360, 1180, 14, t(14) + 0.1)` | now x 360, today bandının içinde |
| 14 | `t(15)` 143,05 | anında | `now` etiketi: `gNow = eyGen("now", 64)`; `S.elYazisi({ metin: "now", x: 360 − gNow / 2, y: 1252, boy: 64, renk: RT.murekkep, tb: t(15), sure: 0.4 })` | noktanın altında ortalı; nabız (en çok r 34) etikete değmez |
| 15 | `t(18)` 144,37 | şimdiki | odak *is wearing*: `A = cum.kel[1]`, `B = cum.kel[2]`; `S.darbe(altCizgi(A.x − 6, B.x + B.w + 6, altY(B.y, 72, "wearing"), 13), { w: 9, renk: RT.vurgu, alfa: 0.9, uc0: 8, uc1: 14, tohum: 503 }, t(18), 0.4, 0.55)` | y ≈ 622; `g` kuyruğunun altından |

Türkçe çeviri YOK (yatayda yok). Ekran metni yalnız: `today`, kart cümlesi, `this day only`, `now`.

## 6. sahne.js içinde yazılacak yardımcılar (yalnız davranış tarifi)

### 6.1 `donen(pts, o, tb, sure, ses, tDon)` → öğe `{ ciz(ctx, f) }`
Sarı belirteç sınırı (aynı anda en çok 3 sarı): `tDon` anında sarı çizgi `ikincil`e döner, kaybolmaz.
- Aynı `pts` ve aynı `o` (yalnız `renk` farklı: biri `o.renk`, öbürü `RT.ikincil`) ile iki `S.darbe` kur: `sari` (`ses` ile),
  `gri` (`tb`, `sure` aynı, ses `false`).
- `u = kis((f − S.fr(tDon)) / 9)`. `sari.carpan = 1 − u`, `gri.carpan = u`. Önce `gri.ciz(ctx, f)`, sonra `sari.ciz(ctx, f)`.
  (`darbe` öğesinin `carpan` alanı `darbeCiz` saydamlık çarpanıdır.)

### 6.2 `bant(x0, x1, y0, y1, tb, sure)` → öğe `{ ciz(ctx, f) }`
Today gün bandı (BRIEF-DIKEY §2.7: `vurguDolgu` %45). Kalem darbesi DEĞİL; soldan sağa açılan düz dolgu.
- `fb = S.fr(tb)`; oluşturulurken bir kez `S.bas(fb)` ve `S.olay(fb, "cizgi", 0.5)`.
- `u = yavasla((f − fb) / (sure × 30))`; `u <= 0` ise çizme. `ctx.save()`, `globalAlpha = 0.45`,
  `fillStyle = renkCoz(RT.vurguDolgu)`, `fillRect(x0, y0, (x1 − x0) × u, y1 − y0)`, `ctx.restore()`.
- Çakışma kapısına kutu YAZMAZ (04'teki bant darbesi gibi).

### 6.3 `altyaziDuzelt()` — `kur()` içinde `S.kur()`'dan hemen sonra bir kez çağrılır
Sorun (ölçüldü): `ortak/anlatim/altyazi.json` cümle 9'da EN parçası `t0 138,57 / t1 142,97`, son TR parçası `t0 143,05`
yazılı; ses ise EN'yi 135,61–137,69'da, son TR parçasını 138,57'de başlatıyor. Sonuç: EN söylenirken altyazı boş,
"Burada today…" söylenirken EN görünür. Bu sahne kendi kopyasını düzeltir (`ortak/`a YAZILMAZ):
1. `L = S.K.altyazi`. `i0` = `cumle === 9` olan ilk girdinin sırası; cümle 9 girdileri ardışıktır.
2. Cümle 9 girdilerini ayır: ilk girdi `tr1` (aynen kalır), `dil === "en"` girdisi `en`, kalan `tr` girdilerinin `metin`'i
   `" "` ile birleşir → `tr3Metin` (kit önceden dilimlediyse birleşince özgün metin döner).
3. Yeni girdiler (`{ ...en, ... }` biçiminde, öbür alanlar korunur):
   - `tr1` aynen.
   - `en`: `t0 = EN[0].t0`, `t1 = EN[6].t1`.
   - `tr3`: sözcükler `tr3Metin.split(" ")` (12), sözcük `i`'nin zamanı `S.sozc[8 + i].t0` (12 sözcük, birebir).
     Açgözlü dilim: dilim metni `500 44px Lexend` ile ölçülür; sarma kuralı kunye.js `altyaziSar` ile aynı (sözcük ekle,
     genişlik 984'ü aşarsa yeni satır); bir sözcük eklenince 2 satırı aşacaksa dilim kapanır. Dilim `t0` = ilk sözcük zamanı;
     son olmayan dilimin `t1` = sonraki dilimin `t0` − 0,4; son dilimin `t1` = `S.sozc[19].t1`.
4. `L.splice(i0, <cümle 9 girdi sayısı>, ...yeniGirdiler)`. Cümle 9 girdisi yoksa ya da `en` yoksa hiçbir şey yapma.
Ölçüm tuvali: `document.createElement("canvas").getContext("2d")` (sahne başına bir kez).

## 7. Kurallar

1. Zaman yalnız kareden (`S.fr`, `S.zm`, `t(i)`, `EN[k]`); sabit saniye yalnız bu SPEC'teki değerler (140.17 gibi).
2. Aynı anda en çok 3 sarı (`RT.vurgu`) belirteç: 141,77'den sonra notun today'si, 144,37'den sonra kartın today'si
   `ikincil` (`donen`). Son düzen: halka + *is wearing* + now noktası. Karaoke altı kitten (`vurguDolgu`).
3. Altçizgi y'si Fredoka'da `altY(taban, 72, metin)`; Caveat başlık notunda `436 + 0.42 × 80`.
4. `S.koy` sırası (çizim sırası = katman): bant (8) → çentikler (9) → eksen (5) → diğerleri zaman sırasıyla. Yani bant ve
   çentikler kod içinde eksenden önce eklenir; yorum satırları kendi zamanlarını yazar.
5. Boş çerçeve ≤ 0,6 sn (kart 0,50 sn). İlk öğe 134,95 (kare 137 ≥ 12). Son hareket 144,77'de biter; `nabiz` içerik
   sonunda (kare 447) durur; son 12 kare durgun.
6. Hiçbir öğe y < 352 ya da y > 1392'ye, x 48–1032 dışına taşmaz.
7. Satır kodu ≤ 100 karakter, 2 boşluk girinti, dosya sonu boş satır. Her öğe bloğunun üstünde tek satır yorum:
   `// 139,21 today: …` (zaman + tetik sözcüğü).

## 8. Kabul ölçütü (şef doğrular)

- `node --check sahne.js` geçer.
- `cd /home/sef/01dev/_worktrees/kalem-0204 && bash araclar/qa-yerel.sh 02-04-ydt-temel-dikey 08-canvas-karsit1 138.3,141.2,145.25 143.6 --hazirla` → `kapı çıkış kodu: 0`.
- Karelerde taşma, kesik yazı, üst üste binme, okunmaz kontrast, boş kare, altyazıyla çakışma yok; 145,25'te başlık notu +
  kart + tişört halkası + `↳ this day only` + bant + now + `now` görünür; altyazı söylenen parçayı gösterir.
