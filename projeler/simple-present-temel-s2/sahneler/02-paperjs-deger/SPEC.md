# SPEC — simple-present-temel-s2 · sahne 02-paperjs-deger · huni v2 (15.11)

Şef tasarımı. Tek dosya, tek agy koşusu:
- YAZILACAK: `/home/sef/01dev/_worktrees/kalem-0204/projeler/simple-present-temel-s2/sahneler/02-paperjs-deger/sahne-02.js` (yeni dosya)

Başka dosyaya dokunma. Silme yok. Test, render, git yok. `kalem-paper.js`, `sayfa.html`, `calistir.sh`, `nesneler.json` hazır, DEĞİŞMEZ.
Bağlayıcı: `/home/sef/01dev/dijital-anlatim/.claude/docs/huni-v2-standart.md` §1–§2 · `../../BRIEF-S2.md` "Sahne içeriği" 3,00–11,87.

## Var olan kod (oku, kalıbı al)

| Dosya (mutlak yol) | Ne alınır |
|---|---|
| `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s1/sahneler/02-paperjs-ornek/sahne-02.js` | dosya iskeleti: baş yorum, 2 import, `export const KARE, T_BAS`, `export async function kur(P)`, `sahneKur(P, { KARE, tBas: T_BAS })`, `eyM/eyG` + `eyGen`, `pen`, `satir`, `noktasiz` + `al()` bekçisi (AYNEN), `cumle`, `yazi`, `elYazisi`, `kutu`, `ciz`, `daire`, `svgCiz`, `not()` kullanımı, `throw new Error` bekçileri, `return S` |
| `/home/sef/01dev/_worktrees/kalem-0204/projeler/simple-present-temel-s2/sahneler/02-paperjs-deger/kalem-paper.js` | API imzaları (S2 kopyası): `ciz(pts,{bas,sure,w,renk,alfa,duz,uc0,uc1,amp,oge,ses,tur,ad})`, `daire(cx,cy,rx,ry,o)`, `kutu(x,y,w,h,{bas,sure,w,renk,ad})`, `yazi`, `cumle`, `elYazisi` (dönüş `{x0,x1,bas,bit}`), `svgCiz(dosya,{kutu,bas,sure,azami,kisaAtla,w,sesAralik,oge})` (dönüş `{sinir}`), `oge({alfa})` (`alfa(f)` grup saydamlığı), `S.kis`, `S.genislik`, `S.sozcukler(n)` |
| `/home/sef/01dev/_worktrees/kalem-0204/projeler/simple-present-temel/sahneler/04-canvas-ornek2/sahne.js` | çizim dizisi (canvas → Paper.js): oturan figür + otobüs + zemin çizgisi, 5 gün kutusu + tik (`TIK` noktaları). Gün adı yazısı (Lexend 28) ALINMAZ |

İçe aktarma (birebir):
```
import { sahneKur, RT, KUNYE } from "/projeler/simple-present-temel-s2/sahneler/02-paperjs-deger/kalem-paper.js";
import { yaziNoktalari } from "/projeler/simple-present-temel-s2/ortak/kalem-canvas.js";
export const KARE = 278, T_BAS = 3.0;
```
Baş yorum 3 satır: sahne adı (simple-present-temel-s2 Shorts, Değer, Paper.js 1080x1920, 278 kare, t_bas 3.00) · cümle 2 içeriği ·
`// huni v2 (15.11): içerik x 60–960, y 460–1380; çip yok; kanal katmanı ve künye kunye.js'te.`
`S`'ten alınacak adlara `kis` eklenir (emsal listesi + `kis`; `ok`, `altCizgi` KULLANILMAZ, alınmaz).

## Bantlar (1080×1920)

```
   0–280   boş (çip YOK)          291–339 kanal (kunye.js)     360–450 künye (kunye.js)
 460–1380  içerik, x 60–960       1400–1550 altyazı (kunye.js)  1570–1920 boş · sağ 960–1080 boş
```

## Sözcükler (`const s2 = S.sozcukler(2)`; her biri `al(s2, i, "…")` ile)

| i | sözcük | t (sn) | kare `fr(t)` | i | sözcük | t | kare |
|---|---|---|---|---|---|---|---|
| 0 | My | 3,95 | 29 | 9 | işareti. | 7,52 (t1 8,52) | 136 |
| 1 | brother | 4,19 | 36 | 10 | Şu | 8,67 | 170 |
| 2 | usually | 4,59 | 48 | 11 | an | 8,91 | 177 |
| 3 | goes | 4,99 | 60 | 12 | değil, | 9,07 | 182 |
| 4 | to | 5,23 | 67 | 13 | her | 9,79 | 204 |
| 5 | school | 5,39 | 72 | 14 | sabah | 9,95 (t1 10,27 → `f1` 218) | 209 |
| 6 | by | 5,71 | 81 | 15 | yedide | 10,31 | 219 |
| 7 | bus. | 5,95 (t1 6,59 → `f1` 108) | 89 | 16 | kalkarım | 10,67 (t1 11,15) | 230 |
| 8 | Alışkanlık | 6,84 | 115 | 17 | gibi. | 11,39 | (kullanılmaz) |

Kare sayıları beklenen değerdir; kod her zamanı `fr(w.t)` / `w.f` / `w.f1` ile okur, çıplak kare sayısı yazmaz. `SON` = 265 (11,83).

## Sabitler (çıplak sayı yalnız bu blokta; türetilenler formülle)

| Ad | Değer | Not |
|---|---|---|
| `KENAR`, `SAG`, `SOL` | `KUNYE.kenar` (60), `KUNYE.sag` (960), `KENAR + 24` (84) | |
| `KUTU_PAY`, `KX`, `KW` | 10, `KENAR + KUTU_PAY` (70), `SAG − KENAR − 2 * KUTU_PAY` (880) | sözleşme: el çizimi köşe taşması |
| `IC` | `KX + 40` (110) | kart iç sol |
| `KY`, `KH` | 480, 190 | kart 480–670 |
| `BEN`, `BTR` | 64, 64 | Fredoka 700 / Caveat 700; boy DEĞİŞMEZ |
| `F_EN`, `F_TR` | `` `700 ${BEN}px Fredoka` ``, `` `700 ${BTR}px Caveat` `` | `genislik` ölçümü |
| `yb1`, `yb2` | `KY + 76` (556), `yb1 + 84` (640) | kart satır tabanları |
| `EK` | 24 | `usually` önüne ek boşluk (halka `brother`a değmesin) |
| `yTR1`, `yTR2` | `KY + KH + 76` (746), `yTR1 + 80` (826) | soluk TR tabanları |
| `FIG_Y` | 900 | alt bölge üstü |
| `ZEMIN_Y` | `FIG_Y + 458` (1358) | zemin çizgisi |
| `ySU` | 1015 | `şu an` tabanı |
| `yHS1`, `yHS2` | `ySU + 97` (1112), `yHS1 + 76` (1188) | `Her sabah yedide` / `kalkarım.` |
| `GW`, `GH`, `GA` | 104, 76, 28 | gün kutusu eni, boyu, arası |
| `GY` | `yHS2 + 74` (1262) | gün kutuları 1262–1338 |

## Yardımcı: `okYol(pts, o)` (sahne içinde, ~12 satır)

İnce kalem oku, çok noktalı eğri (emsalin `ok()`'u tek büküm verir; burada yol koridordan geçer). Gövde:
`ciz(pts, { w: 4, renk: RT.ikincil, alfa: 0.85, uc0: 10, uc1: 14, amp: 0.7, bas: o.bas, sure: o.sure, tur: "isaret", ad: o.ad })`
(`duz` YOK → catmull-rom yumuşatma). Uç: son iki nokta `a = pts[n−2]`, `b = pts[n−1]`; `u = (b − a) / |b − a|`, `k = 20`;
`rot(r) = [−(ux·cos r − uy·sin r)·k + bx, −(ux·sin r + uy·cos r)·k + by]`;
`ciz([rot(0.5), b, rot(−0.5)], { duz: true, w: 3.6, renk: RT.ikincil, alfa: 0.85, bas: o.bas + o.sure − 2, sure: 6, uc0: 6, uc1: 6,
amp: 0.4, ses: false, tur: "isaret", ad: o.ad + ":uc" })`.

## Olaylar (sıra bu; her olaydan sonra `not("<ad> (<sözcük>)", kare)`)

| # | Olay | Kare (beklenen) | Kod |
|---|---|---|---|
| 1 | Boş kart çerçevesi (yazısız, tek hareket) | 0–12 (3,00–3,40) | `kutu(KX, KY, KW, KH, { bas: 0, sure: 12, w: 4, renk: RT.ikincil, ad: "kart kutusu" })`. Kare 0'da içerik bandı boş |
| 2 | Alt öğe grubu | — | `const altOge = oge({ alfa: (f) => 1 - kis((f - F_SU) / 4) })`, `F_SU = fr(wSu.t)` |
| 3 | Kart satır 1 `My brother` | 29 / 36 | `kel1 = cumle([{s: wMy.s, f: fr(wMy.t)}, {s: wBrother.s, f: fr(wBrother.t)}], { x: IC, y: yb1, boyut: BEN, aile: "Fredoka", agirlik: 700, renk: RT.murekkep })` |
| 4 | `usually` | 48 | `wU = yazi(wUsually.s, { x: kel1[1].x1 + genislik(" ", F_EN) + EK, y: yb1, boyut: BEN, aile: "Fredoka", agirlik: 700, renk: RT.murekkep, bas: fr(wUsually.t), sure: 4 })` |
| 5 | Kart satır 2 `goes to school by bus.` | 60 / 67 / 72 / 81 / 89 | `kel2 = cumle([...5 sözcük, ekranda `bus.`], { x: IC, y: yb2, …aynı })`. `altCizgi` YOK (sahnenin tek sarısı halka) |
| 6 | Oturan figür (kalem) | 29–80 | `fig = await svgCiz("open-peeps/sitting-4.svg", { kutu: [KX, FIG_Y, 340, 450], bas: fr(wMy.t), sure: 51, azami: 60, kisaAtla: 0.004, w: 3.2, sesAralik: 8, oge: altOge })` |
| 7 | Halka `usually` (sarı, tek vurgu) | 52–64 | `cx = (wU.x0 + wU.x1) / 2`, `cy = yb1 − BEN * 0.27`, `rx = (wU.x1 − wU.x0) / 2 + 16`, `ry = BEN * 0.62`; `daire(cx, cy, rx, ry, { bas: fr(wUsually.t) + 4, sure: 12, ses: "tik", ad: "usually halka" })` (renk varsayılan `RT.vurgu`) |
| 8 | Otobüs (kalem) | 60–93 | `bus = await svgCiz("coco/bus.svg", { kutu: [KX + 380, FIG_Y + 250, 480, 200], bas: fr(wGoes.t), sure: 33, azami: 25, w: 3.8, sesAralik: 5, oge: altOge })` |
| 9 | Zemin çizgisi | 89–104 | `ciz([[KX, ZEMIN_Y], [KX + 300, ZEMIN_Y − 3], [KX + 560, ZEMIN_Y + 2], [SAG − 30, ZEMIN_Y]], { duz: true, w: 3.4, renk: RT.ikincil, alfa: 0.75, uc0: 10, uc1: 30, bas: fr(wBus.t), sure: 15, oge: altOge, ad: "zemin" })` |
| 10 | Soluk TR (seslendirilmez) | 108 / 112 | `TR1 = "Kardeşim genellikle"`, `TR2 = "okula otobüsle gider."`; `yazi(TR1, { x: SOL, y: yTR1, boyut: BTR, aile: "Caveat", agirlik: 700, renk: RT.ikincil, bas: wBus.f1, sure: 8 })`; TR2 aynı, `y: yTR2`, `bas: wBus.f1 + 4` |
| 11 | Ok 1: halka → `alışkanlık` | 115–125 | `alW = eyGen("alışkanlık", BTR)`, `alX = SAG − 24 − alW`; `okYol([[cx + rx + 2, cy − 12], [SAG − 40, KY + 36], [SAG − 34, yTR2 − 130], [alX + alW * 0.6, yTR2 − BTR * 0.85 − 6]], { bas: fr(wAliskanlik.t), sure: 10, ad: "ok alışkanlık" })` |
| 12 | `alışkanlık` (Caveat 64, kartın sağ altı) | 121–135 | `elYazisi("alışkanlık", { x: alX, y: yTR2, boyut: BTR, renk: RT.murekkep, bas: fr(wAliskanlik.t) + 6, sure: 14 })` |
| 13 | Ok 2 (köprü): halka → TR `genellikle` | 136–150 | `genX1 = SOL + genislik(TR1, F_TR)`, `L2X1 = kel2[4].x1`; `okYol([[cx + rx + 2, cy + 12], [L2X1 + 40, cy + 30], [L2X1 + 48, yTR1 − 52], [genX1 + 18, yTR1 − 22]], { bas: fr(wIsareti.t), sure: 14, ad: "ok köprü" })` — yol kart satır 2'nin sağından geçer, yazıya değmez |
| 14 | Figür + otobüs + zemin solar | 170–174 | `altOge.alfa` (2. olay); ayrı kod yok, yalnız `not("alt bölge solar (Şu)", F_SU)` |
| 15 | `şu an` (ikincil) | 174–184 | `suAn = elYazisi("şu an", { x: SOL, y: ySU, boyut: BTR, renk: RT.ikincil, bas: F_SU + 4, sure: 10 })` (solma bitmeden yazı başlamaz: kapı figürle çakışma saymasın) |
| 16 | `şu an` üstüne kalem çizgisi | ≈ 184–191 | `ciz([[suAn.x0 − 8, ySU − BTR * 0.26 + 3], [suAn.x1 + 10, ySU − BTR * 0.30]], { duz: true, w: 5, renk: RT.murekkep, alfa: 0.9, uc0: 4, uc1: 6, amp: 0.4, bas: Math.max(fr(wDegil.t), suAn.bit), sure: 7, ses: "tik", tur: "isaret", ad: "şu an çizgi" })` |
| 17 | `Her sabah yedide` (sözcük zamanlı) | 204–228 | `hs = satir(["Her", "sabah", "yedide"], pen(s2.slice(13, 16)), { x: SOL, y: yHS1, boyut: BTR, renk: RT.murekkep })` |
| 18 | 5 gün kutusu (el çizimi, yazısız) | 204–225 | `i = 0..4`: `kutu(SOL + i * (GW + GA), GY, GW, GH, { bas: fr(wHer.t) + 3 * i, sure: 9, w: 3.4, renk: RT.ikincil, ad: \`gün ${i + 1}\` })` |
| 19 | `her sabah` altçizgi (mürekkep, sarı DEĞİL) | 218–226 | `ciz([[hs[0].x0 − 4, yHS1 + 12], [hs[1].x1 + 6, yHS1 + 10]], { duz: true, w: 5, renk: RT.murekkep, alfa: 0.85, uc0: 6, uc1: 8, amp: 0.8, bas: wSabah.f1, sure: 8, ses: "tik", tur: "isaret", ad: "her sabah altçizgi" })` |
| 20 | `kalkarım.` | 230–245 | `satir(["kalkarım."], pen(s2.slice(16, 17)), { x: SOL, y: yHS2, boyut: BTR, renk: RT.murekkep })` |
| 21 | 5 tik (mürekkep), 5/5 | 219 / 225 / 231 / 237 / 243 | `cx = SOL + i * (GW + GA) + GW / 2`, `cy = GY + GH / 2 + 2`; `ciz([[cx − 18, cy + 1], [cx − 5, cy + 16], [cx + 22, cy − 19]], { w: 6, renk: RT.murekkep, alfa: 0.9, uc0: 5, uc1: 8, amp: 0.3, bas: fr(wYedide.t) + 6 * i, sure: 7, ses: "tik", tur: "isaret", ad: \`tik ${i + 1}\` })` |

`ok()`, `tik()` (sarı), `altCizgi()` (sarı) KULLANILMAZ. Sarı yalnız 7. olayın halkası.

## Bekçiler (`throw new Error("Bekçi: …" + değerler)`; çizimden önce, ölçümler hazır olunca)

1. `wU.x1 + 16 > KX + KW − 30` ya da `kel2[4].x1 > KX + KW − 30` → kart yazısı taşar.
2. `cx + rx + 2 > SAG − 120` → oklar için sağ koridor yok.
3. `L2X1 + 48 > SAG − 34 − 60` → iki ok koridoru arası < 60.
4. `genX1 + 18 + 40 > L2X1 + 48` → köprü okunun sola giden kolu yok.
5. `SOL + genislik(TR2, F_TR) + 40 > alX` → TR satır 2 `alışkanlık`a değer.
6. `Math.max(genX1, SOL + genislik(TR2, F_TR)) > SAG`.
7. `yb2 − yb1 < BEN * 1.22` ya da `yTR2 − yTR1 < BTR * 1.22` (Paper yazı kutusu: taban − 0,9 boy … taban + 0,3 boy; üst üste binmesin).
8. `KY − 10 < KUNYE.icerikBas` · `GY + GH + 10 > KUNYE.icerikSon` · `ZEMIN_Y + 6 > KUNYE.icerikSon`.
9. `FIG_Y < yTR2 + BTR * 0.3 + 30` (alt bölge soluk TR'nin altında başlar).
10. svgCiz sonrası: `fig.sinir.bottom > KUNYE.icerikSon` · `bus.sinir.right > SAG` · `bus.sinir.left < fig.sinir.right + 10`.

## Beklenen konumlar (yaklaşık; ölçüm koşuda)

Kart 70–950 × 480–670 · satır 1 110–≈ 640 (halka ≈ 420–660 × 497–581) · satır 2 110–≈ 730 · TR 84–≈ 550 × 700–845 ·
`alışkanlık` ≈ 715–936 × 778–842 · figür 70–400 × 900–1350 · otobüs ≈ 450–930 × 1157–1343 · `şu an` 84–≈ 210 × 965–1031 ·
`Her sabah yedide` 84–≈ 440 × 1064–1128 · `kalkarım.` 84–≈ 290 × 1140–1204 · gün kutuları 84–716 × 1262–1338.

## Kurallar

Tek vurgu sarı (halka), yeşil ve kırmızı yok, emoji yok, içerik yazısı ≥ 64 px, satır ≤ 24 karakter, tema kodu yok, `try/catch` yok,
`Math.random`/`Date` yok, 2 boşluk girinti, satır ≤ 120 karakter. Ekran metni sesten önce gelmez (TR satırı ve `alışkanlık` EN cümleden sonra).
Dosyada "tam ders", "dakika" sözü, QR, süre metni, "izle" düğmesi yok. Türkçe karakterler tam (ş, ı, ğ, ü, ç, ö).

## Şef düzeltmeleri (kare turları 1–3, Edit; agy koşusu 1 tur)

| Değer | Spec | Son | Gerekçe (karede ölçüm) |
|---|---|---|---|
| `KH` | 190 | 196 | satır aralığı açılınca kart alt payı |
| `yb2` | `yb1 + 84` | `yb1 + 92` | halka altı ile satır 2 üst uzantıları (`h`, `l`, `b`) arası |
| `EK` | 24 | 40 | büyüyen halka `brother`a değmesin |
| halka `cy`, `rx`, `ry`, `egim` | `yb1 − 0,27 boy`, `w/2 + 16`, 0,62 boy, varsayılan −0,07 | `yb1 − 0,21 boy`, `w/2 + 36`, 0,72 boy, 0 | tur 1–2: halka 2. `l` tepesine ve `y` koluna değdi (1 px); tur 3: en yakın 4 px |
| ok 1 ara noktaları | `SAG − 40`, `SAG − 34` | `SAG − 70`, `SAG − 64` (bekçi 3 aynı sayıyla) | ok 1 kart sağ kenarına 10 px yaklaşıp çift çizgi gibi görünüyordu |

## Kabul (şef koşturur)

`node --check` (`.mjs` kopyasıyla) · `bash araclar/qa-yerel.sh simple-present-temel-s2 02-paperjs-deger 3.05,7.45,11.80 7.45 --hazirla`
çıkış 0 · `node araclar/cakisma-kapisi.mjs simple-present-temel-s2 --sahne 02-paperjs-deger --port 41333 --sunucu 41022` çıkış 0,
0 uyarı · karelerde 0–280, 1570–1920, x 960–1080 boş; kanal katmanı her karede.
