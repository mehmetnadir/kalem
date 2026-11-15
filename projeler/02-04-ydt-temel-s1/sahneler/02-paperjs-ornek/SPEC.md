# SPEC — 02-04-ydt-temel-s1 · sahne 02-paperjs-ornek (Paper.js, dikey 1080×1920) · 15.11

Şef tasarımı. Uygulayıcı (agy) YALNIZ şu dosyayı yazar:
`/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s1/sahneler/02-paperjs-ornek/sahne-02.js`

Başka dosyaya dokunma. Silme yok. Test, render, git yok. Aynı dizindeki `kalem-paper.js`, `sayfa.html`, `calistir.sh`,
`bavul.svg`, `nesneler.json` HAZIR (şef yazdı); değiştirme.

## 1. Örnek ve kalıp

- Dikey örnek (aynı motor, aynı modül ailesi):
  `/home/sef/01dev/_worktrees/kalem-0204/projeler/present-continuous-ileri-s1/sahneler/02-paperjs-ornek/sahne-02.js`.
  Al: import satırları, `export const KARE, T_BAS`, `export async function kur(P)`, `sahneKur` → içerik → `return S`;
  tegaki ölçümü (`EY`, `eyGen`), `pen(ws)` sözcük penceresi ve `satir(soz, pn, o)` el yazısı yardımcısı; `not()` kayıtları.
  İçeriği ALMA (o sahne başka ders).
- Sözcük doğrulama kalıbı: `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel/sahneler/02-paperjs-kanca/sahne-02.js`
  satır 28–40 (`noktasiz`, `al(dizi, i, beklenen)` → uyuşmazlıkta `throw new Error`). Aynısını kur.
- İçerik kaynağı (yatay; yerleşim ALINMAZ): aynı dizindeki `RAPOR.md` / `SPEC.md` (02-paperjs-kanca), `../04-canvas-ornek2/RAPOR.md`
  (live kalıcı / am living geçici, ev, bavul, zaman çizgisi), `../11-canvas-tuzak-cevap/sahne.js` satır 110–130 (zaman çizgisi:
  eksen + sağ ok, now noktası, `now` etiketi, bant, bant uç çentikleri).
- Import (mutlak, sunucu kökü):
  `import { sahneKur, RT, KUNYE } from "/projeler/02-04-ydt-temel-s1/sahneler/02-paperjs-ornek/kalem-paper.js";`
  `import { yaziNoktalari } from "/projeler/02-04-ydt-temel-s1/ortak/kalem-canvas.js";`
- Değerler: `KARE = 522`, `T_BAS = 3.0` (zaman.json sahne 2: t_bas 3,00 · t_son 19,99 · içerik 510 + geçiş 12).

## 2. kalem-paper.js API (bu dizindeki kopya)

`const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: KUNYE.cipler["02-paperjs-ornek"] })`
Kullanılacaklar: `fr(t)` (yerel kare = round((t − 3) × 30)), `sozcukler(n)` → `[{s, t, f, t1, f1}]`, `genislik(str, font)`,
`yazi(str, o)`, `cumle(kel, o)`, `altCizgi(kel, o)`, `elYazisi(str, o)`, `ciz(pts, o)`, `daire(cx, cy, rx, ry, o)`, `ok(a, b, o)`,
`kutu(x, y, w, h, o)`, `svgCiz(dosya, o)`, `oge(o)`, `olay(kare, tur, guc)`, `not(ad, kare)`, `bitis(c)`.
Bu kopyaya özgü (şef ekledi; kullan):
- `yazi(str, {..., oge})`: `oge` verilirse yazının grubu o öğenin grubuna girer; öğe `kay` ile kayınca yazı da kayar.
  `yazi(str, {..., son: [k0, k1]})`: k0–k1 arasında 36 px yukarı kayıp söner, sonra gizlenir.
- `oge({kay: {f0, f1, dx, dy}})`: grup f0–f1 arasında (yumus) dx, dy kadar kayar; ondan önce yerinde, sonra hedefte durur.
  Öğe grupları oluşturulma sırasıyla üst üste biner: SONRA oluşturulan öğe ÜSTTE çizilir.
- `altCizgi(kel, {tut, alt})`: `alt` = çizginin taban altı payı (boy oranı, varsayılan 0,16). `kel` elemanı `{x0, x1, y, boyut, bas}`
  taşıyan herhangi bir nesne olabilir (yalnız `yazi`/`cumle` dönüşü değil).
- `svgCiz(dosya, ...)`: `dosya` "/" ile başlarsa tam yol (bavul için), değilse `ortak/cizim/` altı (ev: `tabler/home.svg`).
- Kapı türleri: `ciz` varsayılanı "cizim"; süs/belirteç çizgilerine `tur: "isaret"` ver. Kapı yazı × çizim çakışmasını sayar,
  isaret ve kart (kutu) saymaz. `yazi`, `elYazisi` kapıya "yazi" olarak girer.
- Renk yalnız belirteçle: `RT.murekkep`, `RT.ikincil`, `RT.vurgu` (sarı çizgi), `RT.vurguDolgu` (sarı dolgu). Ham renk kodu yok.

## 3. Ölçü (BRIEF-DIKEY §2–§3; her sayı adlı sabit, çıplak sayı dağıtma)

| Sabit | Değer | Not |
|---|---|---|
| `KENAR` | `KUNYE.kenar` (48) | sol/sağ güvenli kenar; sağ sınır `W − KENAR` = 1032 |
| `SOL` | `KENAR + 24` (72) | TR satırları, etiketler sol hizası |
| `KX, KW` | `KENAR`, `W − 2·KENAR` (984) | kart kutusu x ve eni |
| `IC` | `KX + 40` (88) | kart iç yazı x (iç boşluk 40) |
| `BTR` | 80 | TR satır boyu, Caveat 700 |
| `Y_L1, Y_L2` | 470, 590 | TR satır tabanları (sahne 01'in uçuş sonrası konumu = kare 0) |
| `BEN` | 64 | kart cümlesi, Fredoka 700 |
| `BTR2` | 72 | soluk TR (`Hep orada.`, `Şimdilik.`), Caveat el yazısı, `RT.ikincil` (ikincil yalnız ≥ 72) |
| `BET` | 72 | `PERMANENT` / `TEMPORARY` etiketi, Caveat el yazısı, `RT.murekkep` |
| `BNOW` | 64 | `now` etiketi, Caveat el yazısı, `RT.murekkep` |
| `KY1, KH1` | 460, 220 | kart 1 kutusu (alt 680) |
| `KY2, KH2` | 935, 300 | kart 2 kutusu (alt 1235) |
| `YC1, YC2` | 430, 905 | *yor* çiplerinin hedef tabanı (kart 1'in / kart 2'nin hemen üstü) |
| `AXY1, AXY2` | 740, 1290 | zaman çizgisi eksenleri |
| `IKON` | 100 | ev / bavul kutusu kenarı; kutu x `KX + KW − 40 − IKON` (892), y `KY + 14` |
| `ALT` | 0.30 | kart altçizgileri taban altı payı (g, y kuyruğunu kesmesin) |

Türetilen:
- Kart 1 cümle tabanı `yb1 = KY1 + 88` (548); TR `Hep orada.` tabanı `KY1 + 182` (642).
- Kart 2 satır 1 tabanı `yb2 = KY2 + 88` (1023), satır 2 `yb2 + 85` (1108); TR `Şimdilik.` tabanı `KY2 + 267` (1202).
- Etiket tabanı `AXY + 24`; `now` tabanı `AXY + 76`; now noktası x `NX = round((AX0 + AX1) / 2)`.
- `AX1 = W − KENAR − 24` (1008); `AX0 = SOL + max(eyGen("PERMANENT", BET), eyGen("TEMPORARY", BET)) + 36` (iki satırda aynı).
- Uzun bant `[AX0 + 24, AX1 − 44]`; kısa bant `[NX − 72, NX + 72]`.

Bekçiler (sessiz geçiş yok, `throw new Error(...)`): TR satırı sağ ucu > 1032 · kart 1 cümlesi sağ ucu > ikon x − 20 ·
kart 2 satırlarının sağ ucu > 1032 − 40 · `AX0 > NX − 120` · `AXY2 + 76 > KUNYE.icerikSon` (1392).

## 4. Yerleşim (tek sütun, üstten alta)

```
352 ─ HUD altı
 ~420–600  FAZ A (kare 0–171): iki TR satır (Caveat 80, x 72, taban 470 / 590)
 378–450   çip 1: yor (sarı kutu) — kart 1'in üstü, `live` ortasının 150 px sağında
 460–680   KART 1: I live in İstanbul. (Fredoka 64) · ev sağ üst · Hep orada. (Caveat 72 soluk)
 700–816   PERMANENT (sol) + zaman çizgisi 1: eksen, uzun bant, now noktası + now
 859–925   çip 2: yor (sarı kutu) — kart 2'nin üstü, `am living` ortasının 150 px sağında
 935–1235  KART 2: I am living / with my uncle. · bavul sağ üst · Şimdilik. (Caveat 72 soluk)
1250–1366  TEMPORARY (sol) + zaman çizgisi 2: eksen, kısa bant + çentikler, now noktası + now
1392 ─ içerik sonu · 1400–1536 altyazı (modül çizer) · 1536–1920 BOŞ
```

## 5. TR satırları ve *yor* çipleri (kare 0 = sahne 01'in son karesi)

Her satır üç `yazi` parçasıdır (Caveat 700 80, `RT.murekkep`, `bas: -30, sure: 4`, ses yok): `pre` · `yor` · `post`.
- Satır 1: `pre = "İstanbul'da yaşı-"`, satır 2: `pre = "Amcamla yaşı-"`; ikisinde `yor = "yor"`, `post = "-um."`.
- x: `pre` `SOL`; `yor` `xYor = SOL + genislik(pre, F)`; `post` `xYor + genislik("yor", F)`; `F = "700 80px Caveat"`.
- `pre` ve `post` `son: [G0, G0 + 8]` alır (yukarı solar). `yor` sönmez.
  (Şef düzeltmesi, 1. kare turu: ilk sürüm `[G0, G0 + 11]` + kayma G0'da başlıyordu; çip 1 sönen `yaşı-` üstünden geçti.
  Kayma artık `GK0 = G0 + 6`'da başlar, `G1 = GK0 + 15`.)

Çip öğeleri (sıra önemli — kutu yazının ALTINDA kalsın): önce `bandOge1`, `bandOge2`, sonra `metinOge1`, `metinOge2`;
her biri `oge({kay: {f0: G0, f1: G1, dx: dx_k, dy: dy_k}})`, aynı çipin iki öğesinde aynı dx/dy.
- `G0 = fr(ayrılır)`, `G1 = G0 + 15`.
- Hedef: çip yazısının x'i `XC_k = hedefOrta_k + 150 − genislik("yor", F) / 2`, tabanı `YC_k`.
  `hedefOrta_1` = kart 1 `live` sözcüğünün ortası; `hedefOrta_2` = kart 2 `am` başı ile `living` sonu ortası.
  `dx_k = XC_k − xYor_k`, `dy_k = YC_k − Y_Lk`. (Kart sözcüklerini önce `cumle` ile kur, konumları buradan oku.)
- `yor` yazısı `oge: metinOge_k`.
- *yor* kutusu (ek_ayir): `ciz([[xYor − 5, by], [xYor + gYor + 6, by]], {duz: true, w: BTR * 0.70, renk: RT.vurguDolgu, alfa: 0.6,
  uc0: 5, uc1: 9, amp: 1.0, sure: 10, tur: "isaret", ses: "tik", oge: bandOge_k, ad: "yor kutusu k"})`, `by = Y_Lk − BTR * 0.22`,
  `gYor = genislik("yor", F)`. Koordinat satırdaki ilk konumdur; kayma öğeden gelir.

## 6. Olay listesi (yerel kare = round((t − 3,00) × 30); zaman `al()` ile sözcükten, sayı elle yazılmaz)

`s1 = S.sozcukler(1)`, `s2 = S.sozcukler(2)`. `f0 = (t) => Math.max(12, fr(t))` (ilk 12 kare geçiş: hareket yok).

| # | Olay | Kare (≈) | Cümle:sözcük (t0 sn) | Uygulama |
|---|---|---|---|---|
| 1 | İki TR satırı hazır (sahne 01'den) | 0 | — | §5, `bas: -30` |
| 2 | Karaoke: satır 2 `yaşı-yor-um.` altı | 12 | 1:3 yaşıyorum. (3,08) | `altCizgi([{x0: xYor2 − genislik("yaşı-", F), x1: xYor2 + gYor + genislik("-um.", F), y: Y_L2, boyut: BTR, bas: f0(t)}], {tut: 20, alt: 0.32})` |
| 3 | ek_ayir: satır 1 *yor* kutusu | 29 | 1:4 Türkçede (3,96) | §5 kutu, `bas: f0(t)` |
| 4 | ek_ayir: satır 2 *yor* kutusu | 86 | 1:7 yaşıyorum. (5,56) + 9 kare (*yor* hecesi ≈ +0,30 sn) | §5 kutu, `bas: fr(t) + 9` |
| 5 | TR satırlar solar, iki çip ayrılır (çip 1 kart 1'in üstüne, çip 2 kart 2'nin üstüne kayar) | 156–171 | 2:2 ayrılır. (8,19) | §5 `son` + `kay` |
| 6 | Kart 1 kutusu | 172 | 2:3 I (9,08) − 10 | `kutu(KX, KY1, KW, KH1, {bas: fr(t) − 10, sure: 14, w: 4, renk: RT.ikincil})` |
| 7 | Kart 1 sözcükleri (sözcük zamanlı) + karaoke altçizgi | 182–199 | 2:3–6 I live in Istanbul. | `cumle` her sözcük `f: fr(t)`, x `IC`, y `yb1`, BEN, Fredoka 700, mürekkep; ekranda `İstanbul.` (noktalı İ); `altCizgi(kel1, {tut: 24, alt: ALT})` |
| 8 | `odak` *live* (kalıcı sarı altçizgi) | 190 | 2:4 live (9,32) | `ciz([[x0 − 4, yU], [x1 + 4, yU − 2]], {duz: true, w: 9, renk: RT.vurguDolgu, alfa: 0.9, uc0: 6, uc1: 8, amp: 0.8, bas: fr(t), sure: 6, tur: "isaret", ses: "tik", ad: "odak live"})`, `yU = yb1 + BEN * ALT` |
| 9 | `bag` çip 1 → *live* | 194 | 2:5 in (9,48) | `ok([XC1 − 8, YC1 + 10], [hedefOrta_1 + 10, yb1 − BEN * 0.95], {bas: fr(t), sure: 12, w: 6, uzun: 18, bukum: 0.12, ad: "bag 1"})` |
| 10 | Ev ikonu (kart 1 sağ üst, küçük) | 199 | 2:6 Istanbul. (9,64) | `svgCiz("tabler/home.svg", {kutu: [892, KY1 + 14, IKON, IKON], bas: fr(t), sure: 20, azami: 25, w: 4, sesAralik: 3})` |
| 11 | Soluk TR `Hep orada.` (kalemle, sözcük penceresi) | 245–279 | 2:7–8 Hep orada: (11,17–12,29) | `satir(["Hep", "orada."], pen(s2.slice(7, 9)), {x: IC, y: KY1 + 182, boyut: BTR2, renk: RT.ikincil})` |
| 12 | `PERMANENT` etiketi | 281 | 2:9 kalıcı (12,37) | `elYazisi("PERMANENT", {x: SOL, y: AXY1 + 24, boyut: BET, renk: RT.murekkep, bas: fr(t), sure: 18})` |
| 13 | Zaman çizgisi 1: eksen + sağ ok | 293 | 2:10 durum, (12,77) | eksen `ciz([[AX0, AXY1], [AX1, AXY1]], {duz: true, w: 4.5, renk: RT.ikincil, uc0: 8, uc1: 6, bas: fr(t), sure: 12, tur: "cizim", ad: "zaman-1"})`; ok ucu iki kısa `ciz` (`[[AX1 − 26, AXY1 ∓ 16], [AX1, AXY1]]`, `bas: fr(t) + 11, sure: 4, ses: false`, aynı ad) |
| 14 | now noktası + `now` | 301 / 305 | durum, + 8 / + 12 kare | `daire(NX, AXY1, 12, 12, {renk: RT.murekkep, w: 4.5, alfa: 0.95, a0: -1.6, ad: "now 1", bas, sure: 8, ses: "tik", oge: UST})` (DİKKAT: `daire`'de `o.tur` dönüş sayısıdır; `tur` VERME); `now`: `elYazisi("now", {x: NX − eyGen("now", BNOW) / 2, y: AXY1 + 76, boyut: BNOW, renk: RT.murekkep, bas, sure: 12, ses: false})` |
| 15 | Uzun bant (kalıcı), now bandın içinde | 308 | 2:11 geniş (13,25) | `ciz([[AX0 + 24, AXY1], [AX1 − 44, AXY1]], {duz: true, w: 28, renk: RT.vurguDolgu, alfa: 0.55, uc0: 4, uc1: 4, amp: 0.6, bas: fr(t), sure: 16, tur: "isaret", ad: "uzun bant"})` |
| 16 | Kart 2 kutusu | 341 | 2:13 I (14,70) − 10 | `kutu(KX, KY2, KW, KH2, {bas: fr(t) − 10, sure: 14, w: 4, renk: RT.ikincil})` |
| 17 | Kart 2 sözcükleri (2 satır) + karaoke | 351–382 | 2:13–18 I am living with my uncle. | `cumle` (`I am living` satır 0, `with my uncle.` satır 1), x `IC`, y `yb2`, `aralik: 85`, BEN; `altCizgi(kel2, {tut: 24, alt: ALT})` |
| 18 | `odak` *am living* | 361 | 2:15 living (15,02) | 8. olay gibi, x `am.x0 − 4` … `living.x1 + 4`, `yU = yb2 + BEN * ALT`, `sure: 8`, ad "odak am living" |
| 19 | `bag` çip 2 → *am living* | 370 | 2:16 with (15,34) | 9. olay gibi: `ok([XC2 − 8, YC2 + 10], [hedefOrta_2 + 10, yb2 − BEN * 0.95], …, ad: "bag 2")` |
| 20 | Bavul ikonu (kart 2 sağ üst, küçük) | 382 | 2:18 uncle. (15,74) | `svgCiz("/projeler/02-04-ydt-temel-s1/sahneler/02-paperjs-ornek/bavul.svg", {kutu: [892, KY2 + 14, IKON, IKON], bas: fr(t), sure: 20, azami: 12, w: 4, sesAralik: 3})` |
| 21 | Soluk TR `Şimdilik.` | 391–420 | 2:19 Şimdilik: (17,03–17,99) | `satir(["Şimdilik."], pen(s2.slice(19, 20)), {x: IC, y: KY2 + 267, boyut: BTR2, renk: RT.ikincil})` |
| 22 | `TEMPORARY` etiketi | 422 | 2:20 geçici (18,07) | 12. olay gibi, y `AXY2 + 24` |
| 23 | Zaman çizgisi 2: eksen + ok, now + `now` | 434 / 442 / 446 | 2:21 durum, (18,47) | 13–14. olay gibi, `AXY2`, ad "zaman-2" |
| 24 | Kısa bant (geçici) + iki uç çentiği, now bandın içinde | 451 / 457 | 2:22 şimdiki (19,03) | bant `ciz([[NX − 72, AXY2], [NX + 72, AXY2]], {…15. olay gibi, sure: 10, ad: "kısa bant"})`; çentikler `ciz([[x, AXY2 − 26], [x, AXY2 + 26]], {duz: true, w: 5, renk: RT.vurgu, alfa: 0.9, uc0: 3, uc1: 3, amp: 0.3, bas: fr(t) + 6 + 3·i, sure: 5, ses: false, tur: "isaret"})` |

`UST = oge({})` — çip öğelerinden SONRA, içerik çizimlerinden önce kur (now noktaları bandın üstünde kalsın).
Kart sözcük metinleri `s2` sözcüğünden gelir; tek fark ekranda `Istanbul.` → `İstanbul.`. Soluk TR'de ses `orada:` /
`Şimdilik:`, ekran `orada.` / `Şimdilik.`. Her olaya `not("<ad> (<sözcük>)", kare)`. Son olay ≈ kare 470; kare 509–521 durgun
(modül zamanı kendisi dondurur).

## 7. Kurallar

Tek vurgu sarı (`RT.vurgu` / `RT.vurguDolgu`) · yeşil yok · kırmızı yok (`RT.kirmizi` kullanma) · emoji yok · içerik yazısı ≥ 64 px
(`now` 64, diğerleri 72–80) · satır ≤ 24 karakter · künye, çip, altyazı, açık/koyu tema modülde (`kalem-paper.js` + `ortak/kunye.js`);
sahnede tema kodu yok · sessiz catch yok, try/catch yok · `Math.random` / `Date` yok · 2 boşluk girinti, satır ≤ 120 karakter ·
"kanal" sözü, QR, süre metni yok.

## 8. Kabul

`node --check` geçer (şef `.mjs` kopyasıyla dener). Şef koşar:
`cd /home/sef/01dev/_worktrees/kalem-0204 && bash araclar/qa-yerel.sh 02-04-ydt-temel-s1 02-paperjs-ornek 6.0,13.8,19.6 16.0 --hazirla`
→ çıkış 0 (yazı × çizim / yazı × künye çakışması yok, ölçüm hatası yok). Kare PNG'lerinde taşma, kesik yazı, üst üste binme yok;
1536 altı boş; altyazı bandına (1400–1536) içerik girmez.
