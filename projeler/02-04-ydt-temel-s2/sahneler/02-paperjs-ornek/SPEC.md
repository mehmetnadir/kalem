# SPEC — 02-04-ydt-temel-s2 · sahne 02-paperjs-ornek (Paper.js, dikey 1080×1920) · 15.11

Şef tasarımı. Uygulayıcı (agy) YALNIZ şu dosyayı yazar:
`/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s2/sahneler/02-paperjs-ornek/sahne-02.js`

Başka dosyaya dokunma. Silme yok. Test, render, git yok. Aynı dizindeki `kalem-paper.js`, `sayfa.html`, `calistir.sh`,
`nesneler.json` HAZIR (şef yazdı); değiştirme.

## 1. Örnek ve kalıp

- Dikey örnek (aynı ders, aynı motor, aynı modül kopyası):
  `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s1/sahneler/02-paperjs-ornek/sahne-02.js`.
  Al: dosya başı yorum biçimi, import satırları, `export const KARE, T_BAS`, `export async function kur(P)`, `sahneKur` →
  içerik → `return S`; tegaki ölçümü (`EY`, `eyGen`); sözcük bekçisi `noktasiz` + `al(dizi, i, beklenen)` (uyuşmazlıkta
  `throw new Error`); adlı ölçü sabitleri bloğu; bekçi bloğu (`throw new Error`); her olaya `not("<ad> (<sözcük>)", kare)`.
  İçeriği ALMA (o sahne başka cümle).
- Giysi çizimi kaynağı (yatay ana ders; yerleşim ALINMAZ):
  `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel/sahneler/03-paperjs-ornek1/sahne-03.js`
  - satır 16–32: `MONT` ve `TISORT` dizilerini AYNEN al (birim ızgara; mont 100×120, tişört 100×90).
  - satır 58–82: `elCizim(darbeler, [bx, by, bw, bh], [UW, UH], o)` işlevini al; tek fark: `u()` yok (bu sahne 1080 px gerçek
    ölçüde), `MUR` yerine `RT.murekkep`. `tur: "cizim"` ve `ad: o.ad` aynen kalır.
  - satır 84: `yalin(z)` (sözcüğün sondaki `.`/`,`/`:` hariç sağ ucu) kalıbını al: `z.x0 + genislik(z.str.replace(/[.,:]$/, ""), F_EN)`.
- İçerik kaynağı (yalnız fikir): ana ders `08-canvas-karsit1/sahne.js` (today gün bandı + iki uç çentiği, now noktası nabız).
- Import (mutlak, sunucu kökü):
  `import { sahneKur, RT, KUNYE, renkCoz } from "/projeler/02-04-ydt-temel-s2/sahneler/02-paperjs-ornek/kalem-paper.js";`
  `import { yaziNoktalari } from "/projeler/02-04-ydt-temel-s2/ortak/kalem-canvas.js";`
- Değerler: `KARE = 449`, `T_BAS = 2.84` (zaman.json sahne 2: t_bas 2,84 · t_son 17,41 · içerik 437 + geçiş 12).
  Yerel kare `fr(t) = round((t − 2,84) × 30)`. Modül `SON = KARE − 13 = 436`'da zamanı dondurur: bütün olaylar kare 436'dan
  önce biter.

## 2. kalem-paper.js API (bu dizindeki kopya = S1 kopyası, yalnız import yolları değişti)

`const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: KUNYE.cipler["02-paperjs-ornek"] })`
Kullanılacaklar (S'den): `fr, not, olay, ciz, daire, ok, kutu, yazi, elYazisi, cumle, altCizgi, dinamik, oge, sozcukler, genislik,
kis, cikis, P` (Paper nesnesi `S.P`).
- `yazi(str, {x, y, boyut, aile, agirlik, renk, bas, sure, hizala, ses})` → `{x0, x1, y, boyut, bas, str}`; kapıya "yazi" girer.
  `hizala: "orta"` → `x` ortadır.
- `cumle([{s, f, satir}], {x, y, boyut, aile, agirlik, renk, aralik})` → sözcük dizisi (`x0, x1, y, boyut, bas, str`).
- `altCizgi(kel, {tut, alt})` → karaoke sarı çizgisi; son sözcükten sonra `tut` kare durur, 16 karede söner.
- `elYazisi(str, {x, y, boyut, renk, sozcukler: [{f0, f1}] | bas, sure, ses})` → `{x0, x1, w, bas, bit}`; tegaki Caveat.
  `sozcukler` verilirse her sözcük kendi penceresinde yazılır (pencere sayısı = sözcük sayısı). `oge` VERME.
- `ciz(pts, {duz, w, renk, alfa, uc0, uc1, amp, bas, sure, tur, ad, ses, oge, tohum})`: `tur` varsayılan "cizim"; süs/belirteç
  `tur: "isaret"`. Kapı yalnız yazı × "cizim" çakışmasını sayar.
- `daire(cx, cy, rx, ry, o)`: **DİKKAT:** `o.tur` dönüş sayısıdır; `tur` VERME. Renk varsayılanı `RT.vurgu` (sarı).
  `o.tohum` verilirse kalem biçimi o tohumdan gelir.
- `ok(a, b, {bas, sure, w, renk, alfa, uzun, bukum, ad})`: renk varsayılanı sarıdır; bu sahnede `renk: RT.murekkep` ver.
- `kutu(x, y, w, h, {bas, sure, w, renk, ad})` → kart çerçevesi (kapıda sayılmaz).
- `oge({alfa: (f) => 0..1})` → grup; `ciz(..., {oge})` ile içine konan darbelerin opaklığını o kare için ayarlar.
  Öğe grupları oluşturulma sırasıyla üst üste biner (SONRA oluşturulan ÜSTTE). `kok` grubu en alttadır (öğesiz darbeler oraya girer).
- `dinamik((f, g) => {...})` → her karede boşaltılan grup; içine `new S.P.Path.Circle(...)` / `new S.P.Path.Rectangle(...)`
  `{insert: false}` ile kurulup `g.addChild` ile eklenir. Renk `renkCoz(RT.x)` ile HER karede çözülür (tema değişimi).
- Renk yalnız belirteçle: `RT.murekkep`, `RT.ikincil`, `RT.vurgu` (sarı çizgi), `RT.vurguDolgu` (sarı dolgu), `RT.pilMetin`
  (hap yazısı). Ham renk kodu YOK. `RT.kirmizi` YOK.

## 3. Zaman çapaları (zaman sözcükten okunur; sayı elle YAZILMAZ — tek istisna EN2)

`s2 = S.sozcukler(2)`. `al()` ile adlı al (beklenen metinle):
0 She · 3 coat · 4 in · 6 winter. · 7 Genel · 8 durum: · 9 geniş · 10 zaman. · 11 Today · 17 anlam · 19 Konuşma · 20 anı: ·
21 şimdiki · 22 zaman. — kart 1 sözcükleri `s2.slice(0, 7)` (She wears her coat in the winter.).

**EN2 (kart 2) sabit dizi** — `sozcukler.json`'da YOK. Koda bu yorumla yaz:
`// Cümle 2 parça 3 (EN "She is wearing her pink T-shirt today.") sozcukler.json'da YOK: el.py T-shirt'ü sese "T shirt"`
`// gönderir, sözcük sayısı tutmaz. Çapa: ElevenLabs önbellek hizalaması ~/.local/share/elevenlabs-onbellek/`
`// 3e7a9af33838d05cd9a8083c218a882a935c6edf.hiz.json (T + shirt birleşik) + parça başı 8,37 (sureler.json cümle 2`
`// parcalar[2][0] 4,98 + cümle başı 3,39). BRIEF-S2 DİKKAT notu ile aynı. Küresel sn.`
`const EN2 = [["She", 8.37], ["is", 8.61], ["wearing", 8.77], ["her", 9.21], ["pink", 9.45], ["T-shirt", 9.65], ["today.", 10.13]];`
Ekranda `T-shirt` tireli.

## 4. Ölçü (BRIEF-DIKEY §2–§3; her sayı adlı sabit)

| Sabit | Değer | Not |
|---|---|---|
| `W` | 1080 | |
| `KENAR` | `KUNYE.kenar` (48) | sağ sınır `SAG = W − KENAR` (1032) |
| `SOL` | `KENAR + 24` (72) | soru satırı, `Simple Present`, `Present Continuous`, eksen başı |
| `KX, KW` | `KENAR`, `W − 2·KENAR` (984) | kart x, en |
| `IC` | `KX + 40` (88) | kart iç yazı x |
| `F_EN`, `BEN` | `"700 64px Fredoka"`, 64 | kart cümleleri |
| `ARA` | 84 | kart satır aralığı (`cumle` `aralik`) |
| `ALT` | 0.32 | karaoke ve odak altçizgisi taban altı payı (boy oranı) |
| `BSORU`, `Y_SORU` | 80, 430 | soru satırı Caveat 700 80, taban 430 (kare 0 devri, §5) |
| `KY1, KH1` | 478, 200 | kart 1 (alt 678) |
| `KY2, KH2` | 912, 210 | kart 2 (alt 1122) |
| `yb1` | `KY1 + 84` (562) | kart 1 satır 1 tabanı; satır 2 `yb1 + ARA` (646) |
| `yb2` | `KY2 + 96` (1008) | kart 2 satır 1 tabanı (üstte hap payı); satır 2 `yb2 + ARA` (1092) |
| `BET` | 64 | `GENERAL`, `RIGHT NOW` Caveat el yazısı, `RT.murekkep` (şef QA tur 1: 72'de satır B 28 px çakıştı) |
| `F_INCE`, `BINCE` | `"500 64px Lexend"`, 64 | `Simple Present`, `Present Continuous` (ince yazı; yüklü Lexend ağırlıkları 500/700) |
| `Y_ETA` | `KY1 + KH1 + 78` (756) | satır A tabanı (kart 1 altı) |
| `Y_ETB` | `KY2 + KH2 + 78` (1200) | satır B tabanı (kart 2 altı) |
| `AXY1` | 820 | zaman çizgisi 1 (kış) |
| `AXY2` | 1252 | zaman çizgisi 2 (today) |
| `BNOW`, `NOW_DY` | 64, 66 | `now` etiketi Caveat el yazısı 64, taban `AXY + NOW_DY` |
| `AX0, AX1` | `SOL`, `SAG − 24` (1008) | eksen uçları; sağda ok ucu |
| `NX` | `round(AX0 + 0.45 · (AX1 − AX0))` (≈ 493) | iki çizgide aynı now x'i |
| `BW`, `BP` | 110, 230 | kış bandı eni, bant adımı |
| `TB` | 120 | today bandı yarı eni (`[NX − TB, NX + TB]`) |
| `BANT_W`, `BANT_A` | 28, 0.35 | bant kalınlığı ve alfası (renk `RT.ikincil`, §7 neden) |
| `IKON` | 100 | giysi kutusu; x `IKX = KX + KW − 32 − IKON` (900) |
| `HAP_H`, `HAP_P` | 80, 34 | hap yüksekliği, yatay iç pay |

Türetilen:
- Mont kutusu `[IKX, KY1 + KH1 − 14 − IKON, IKON, IKON]` (kart 1 sağ alt köşe); tişört kutusu `[IKX, KY2 + KH2 − 14 − IKON, IKON, IKON]`
  (kart 2 sağ alt köşe). `elCizim` oranı korur (mont ≈ 83×100, tişört 100×90).
- Kış bandı merkezleri: `k = −3 … 2` için `c = NX + BP · (k + 0.5)`; yalnız `c − BW/2 ≥ AX0 + 8` ve `c + BW/2 ≤ AX1 − 40` olanlar
  (NX ≈ 493 → 148, 378, 608, 838: 4 bant). now noktası iki bant arasında kalır (bantların dışında).
- `GENERAL` ve `RIGHT NOW` SAĞA hizalı: `x = SAG − 12 − eyGen(metin, BET)` (tegaki `gen` kuyruklu son harfi ≈ 10 px eksik ölçer).
- Hap: `HAP_W = genislik("MEANING", F_EN) + 2 · HAP_P`; sağ kenar `SAG − 24`, `hx0 = SAG − 24 − HAP_W`; dikey merkez `KY2`
  (kart 2 üst çizgisinin üstüne oturur, çizgiyi örter); yazı `yazi("MEANING", {x: hx0 + HAP_W / 2, y: KY2 + 22, hizala: "orta",
  boyut: BEN, aile: "Fredoka", agirlik: 700, renk: RT.pilMetin})`.
- today halkası (şef QA tur 2 düzeltmesi; ilk sürüm `daire()` elipsiydi ve `T-shirt`'ün son `t`'sini kesti): süper elips
  (n = 6) kutusu `HL = z.x0 − 11`, `HR = yalin(z) + 22`, `HT = z.y − BEN · 0.8`, `HB = z.y + BEN · 0.36`; 73 nokta, açı −2,3'ten
  1,08 tur; `ciz(..., {duz: true, w: 7.5, alfa: 0.85, amp: 0.4, uc0: 14, uc1: 40, tohum: 4242, tur: "isaret"})`, sarı ve mürekkep
  ikizi aynı noktalarla. Ok halkanın sağından (`[HR + 2, (HT + HB) / 2]`) çıkar, `bukum: 0.25, yon: [0.3, -1]` ile yukarı bombe
  yapar, `[RN.x0 + RN.w · 0.45, Y_ETB − BET · 0.84]`'e iner (ilk sürümde ok başı `RIGHT`'ın `I`'sına düştü).

## 5. Yerleşim (tek sütun, üstten alta)

```
 352 ─ HUD altı
 ~360–455  Genel mi, şu an mı?   (Caveat 700 80, x 72, taban 430; kare 0'dan hazır; 14,14'te mürekkep altçizgi y 454)
 478–678   KART 1: She wears her coat / in the winter.  (Fredoka 64; mont sağ alt köşe, 100 px)
 700–770   Simple Present (Lexend 500 64, sol)  ……………  GENERAL (Caveat 72, sağa hizalı)
 806–834   zaman çizgisi 1: eksen + ok · 4 kış bandı (gri) + bant içinde kar tanesi · now noktası bantlar arasında
 ~850–886  now (Caveat 64, NX'te ortalı)
 872–952   [MEANING] sarı hap — kart 2 üst çizgisinin sağ ucunda
 912–1122  KART 2: She is wearing her / pink T-shirt today.  (tişört sağ alt köşe; today dairesi)
 1146–1200 Present Continuous (sol)  ……………  RIGHT NOW (sağa hizalı) · today dairesinden RIGHT NOW'a ince mürekkep oku
 1224–1280 zaman çizgisi 2: eksen + ok · today bandı (gri) + iki uç çentiği · now noktası bandın içinde, nabız
 ~1290–1318 now (Caveat 64)
1392 ─ içerik sonu · 1400–1536 altyazı (modül çizer) · 1536–1920 BOŞ
```

**Kare 0 devri:** soru satırı `yazi("Genel mi, şu an mı?", {x: SOL, y: Y_SORU, boyut: BSORU, aile: "Caveat", agirlik: 700,
renk: RT.murekkep, bas: -30, sure: 4, ses: false})` → kare 0'da tam. Sahne 01'in son karesi bu konumla eşleşmeli
(Caveat 700 80, x 72, taban 430, `RENK.murekkep`, altçizgi yok).

## 6. Olay listesi (kare = `fr(t)`, t küresel sn; ilk 12 kare geçiş: hareket yok → `f0 = (f) => Math.max(12, f)`)

| # | Olay | t (sn) ≈ kare | Çapa | Uygulama |
|---|---|---|---|---|
| 1 | Soru satırı hazır | — · 0 | — | §5 |
| 2 | Kart 1 kutusu | 12 | She (3,39) − 10 → f0 | `kutu(KX, KY1, KW, KH1, {bas: f0(fr(She) − 10), sure: 10, w: 4, renk: RT.ikincil, ad: "kart 1"})` |
| 3 | Kart 1 sözcükleri + karaoke | 3,39–4,67 · 17–55 | s2[0..6] | `cumle(s2.slice(0, 7).map((k, i) => ({s: k.s, f: k.f, satir: i < 4 ? 0 : 1})), {x: IC, y: yb1, boyut: BEN, aile: "Fredoka", agirlik: 700, renk: RT.murekkep, aralik: ARA})`; `altCizgi(kel1, {tut: 0, alt: ALT})` |
| 4 | Mont kalemle (sağ alt köşe) | 4,27 · 43 | coat | `elCizim(MONT, montKutu, [100, 120], {bas: fr(coat), sure: 30, w: 4, ad: "mont"})` |
| 5 | `odak` *in the winter* (sarı) | 4,47 · 49 | in | `ciz([[kel1[4].x0 − 4, yU1], [yalin(kel1[6]) + 4, yU1 − 2]], {duz: true, w: 9, renk: RT.vurguDolgu, alfa: 0.9, uc0: 6, uc1: 8, amp: 0.8, bas: fr(in), sure: 12, tur: "isaret", ses: "tik", ad: "odak in the winter", oge: odak1})`; `yU1 = kel1[4].y + BEN · ALT`; `odak1 = oge({alfa: kapat(fr(EN2 She))})` |
| 6 | `GENERAL` | 5,56 · 82 | Genel → durum: | `elYazisi("GENERAL", {x: sağa hizalı (§4), y: Y_ETA, boyut: BET, renk: RT.murekkep, sozcukler: [{f0: fr(Genel), f1: fr(durum:)}]})` |
| 7 | Zaman çizgisi 1: eksen + ok ucu | 6,04 · 96 | durum: | eksen `ciz([[AX0, AXY1], [AX1, AXY1]], {duz: true, w: 4.5, renk: RT.ikincil, uc0: 8, uc1: 6, bas: fr(durum:), sure: 12, ad: "zaman-1"})`; ok ucu iki kısa `ciz([[AX1 − 26, AXY1 ∓ 16], [AX1, AXY1]], {duz: true, w: 4.5, renk: RT.ikincil, uc0: 4, uc1: 4, bas: +11, sure: 4, ses: false, ad: "zaman-1"})` |
| 8 | now noktası 1 + `now` | 6,31 / 6,44 · 104 / 108 | durum: + 8 / + 12 | `nokta(NX, AXY1, fr(durum:) + 8)` (§7); `elYazisi("now", {x: NX − eyGen("now", BNOW) / 2, y: AXY1 + NOW_DY, boyut: BNOW, renk: RT.murekkep, bas: +12, sure: 12, ses: false})` |
| 9 | `Simple Present` (ince yazı) | 6,68 · 115 | geniş | `yazi("Simple Present", {x: SOL, y: Y_ETA, boyut: BINCE, aile: "Lexend", agirlik: 500, renk: RT.murekkep, bas: fr(geniş), sure: 12, ses: "tik"})` |
| 10 | Kış bantları + kar taneleri | 7,00 · 125–145 | zaman. (s2[10]) | bant k (soldan sağa i = 0…): `ciz([[c − BW/2, AXY1], [c + BW/2, AXY1]], {duz: true, w: BANT_W, renk: RT.ikincil, alfa: BANT_A, uc0: 4, uc1: 4, amp: 0.6, bas: fr(zaman.) + 4i, sure: 8, tur: "isaret", ses: i ? false : undefined, ad: "kış bandı"})`; kar tanesi `kar(c, AXY1, 11, fr(zaman.) + 4i + 6)` (§7) |
| 11 | odak 1 kapanır | 8,37 · 166–174 | EN2 She | `odak1` alfası (§7 `kapat`) |
| 12 | Kart 2 kutusu | 8,04 · 156 | EN2 She − 10 | `kutu(KX, KY2, KW, KH2, {bas: fr(8.37) − 10, sure: 14, w: 4, renk: RT.ikincil, ad: "kart 2"})` |
| 13 | Kart 2 sözcükleri + karaoke | 8,37–10,13 · 166–219 | EN2 | `cumle(EN2.map(([s, t], i) => ({s, f: fr(t), satir: i < 4 ? 0 : 1})), {x: IC, y: yb2, …kart 1 ile aynı})`; `altCizgi(kel2, {tut: 12, alt: ALT})` (11,07'de söner; daireden önce) |
| 14 | Tişört kalemle (sağ alt köşe) | 9,65 · 204 | EN2 T-shirt | `elCizim(TISORT, tisortKutu, [100, 90], {bas: fr(9.65), sure: 30, w: 4, ad: "tisort"})` |
| 15 | `odak` *today* (sarı) | 10,13 · 219 | EN2 today. | 5. olay gibi, x `kel2[6].x0 − 4` … `yalin(kel2[6]) + 4`, `yU2 = kel2[6].y + BEN · ALT`, `sure: 10`, `ad: "odak today"`, `oge: odak2`, `odak2 = oge({alfa: kapat(fr(Today))})` |
| 16 | today sarı daire (`isaret`) | 11,42 · 257 | Today | §7 `cift daire`: sarı (`RT.vurgu`, `ses: "tik"`) ve mürekkep ikizi aynı bas/sure (`sure: 14`) |
| 17 | `MEANING` sarı hap + soru satırı mürekkep altçizgi + daire mürekkebe döner | 14,14 · 339 | anlam | hap §7; altçizgi `ciz([[SOL − 4, Y_SORU + 24], [SOL + genislik("Genel mi, şu an mı?", "700 80px Caveat") + 4, Y_SORU + 22]], {duz: true, w: 6, renk: RT.murekkep, alfa: 0.9, uc0: 6, uc1: 10, amp: 0.8, bas: fr(anlam) + 2, sure: 12, tur: "isaret", ses: false, ad: "soru altçizgi"})`; daire geçişi §7 (8 kare) |
| 18 | `RIGHT NOW` | 15,25 · 372–395 | Konuşma → anı: | `elYazisi("RIGHT NOW", {x: sağa hizalı (§4), y: Y_ETB, boyut: BET, renk: RT.murekkep, sozcukler: [{f0: fr(Konuşma), f1: fr(Konuşma.t1)}, {f0: fr(Konuşma.t1), f1: fr(anı:) + 6}]})` |
| 19 | Zaman çizgisi 2: eksen + ok ucu | 15,38 · 376 | Konuşma + 4 | 7. olay gibi, `AXY2`, `bas: fr(Konuşma) + 4, sure: 10`, ok ucu `+ 9`, ad "zaman-2" |
| 20 | today dairesi → `RIGHT NOW` ince oku | 15,73 · 387 | Konuşma.t1 | `ok([cx + rx · 0.45, cy + ry · 0.92], [RN.x0 + RN.w · 0.25, Y_ETB − BET · 0.78], {bas: fr(Konuşma.t1), sure: 10, w: 4.5, renk: RT.murekkep, alfa: 0.9, uzun: 16, bukum: 0.12, ad: "bag today"})`; `RN` = 18. olayın dönüşü |
| 21 | now noktası 2 + nabız + `now` | 15,81 · 389 / 392 / 395 | anı: | `nabiz(NX, AXY2, fr(anı:) + 3)` önce, sonra `nokta(NX, AXY2, fr(anı:))` (nokta üstte); `now` 8. olay gibi, `y: AXY2 + NOW_DY`, `bas: fr(anı:) + 6, sure: 10` |
| 22 | `Present Continuous` (ince yazı) | 16,49 · 410 | şimdiki | 9. olay gibi, `y: Y_ETB`, `bas: fr(şimdiki)` |
| 23 | today bandı + iki uç çentiği (now bandın içinde) | 16,62 · 414 / 418 / 421 | şimdiki + 4 | bant `ciz([[NX − TB, AXY2], [NX + TB, AXY2]], {duz: true, w: BANT_W, renk: RT.ikincil, alfa: BANT_A, uc0: 4, uc1: 4, amp: 0.6, bas: fr(şimdiki) + 4, sure: 8, tur: "isaret", ad: "today bandı"})`; çentik `ciz([[x, AXY2 − 26], [x, AXY2 + 26]], {duz: true, w: 4.5, renk: RT.murekkep, alfa: 0.9, uc0: 3, uc1: 3, amp: 0.3, bas: fr(şimdiki) + 8 + 3i, sure: 5, ses: false, tur: "isaret", ad: "today çentik"})` |

Son olay ≈ kare 426'da biter (< 436). Her olaya `not()`. Sözcükler `al()` ile alınır; `fr(...)` yalnız EN2 için sayıyla çağrılır.

## 7. Yardımcılar (sahne dosyasında, kısa)

- `kapat(fk) = (f) => 1 - kis((f - fk) / 8)` — sarı belirteci fk'dan sonra 8 karede söndürür (tek sarı kuralı).
- `kar(cx, cy, r, bas)` — kar tanesi: 3 çizgi, açılar −90°, −30°, 30° (merkezden geçen çaplar, 60° arayla); her biri
  `ciz([[cx − r·cos a, cy − r·sin a], [cx + r·cos a, cy + r·sin a]], {duz: true, w: 3, renk: RT.murekkep, alfa: 0.9, uc0: 2, uc1: 2,
  amp: 0.2, bas: bas + 2j, sure: 4, ses: false, tur: "isaret", ad: "kar"})`.
- `nokta(cx, cy, bas)` — dolu now noktası: `dinamik` grubu; `f < bas` boş; `k = cikis(kis((f − bas) / 6))`;
  `new S.P.Path.Circle({center: [cx, cy], radius: Math.max(0.5, 11 · k), fillColor: renkCoz(RT.murekkep), opacity: 0.95, insert: false})`;
  `olay(bas, "tik", 0.45)`.
- `nabiz(cx, cy, bas)` — `dinamik`; `f < bas` boş; `ph = ((f − bas) % 24) / 24`; halka `new S.P.Path.Circle({center, radius:
  12 + 12 · cikis(ph), strokeColor: renkCoz(RT.murekkep), strokeWidth: 3, opacity: 0.6 · (1 − ph), insert: false})`.
  `nabiz` `nokta`dan ÖNCE kurulur (nokta üstte kalsın).
- `cift daire` (16 + 17. olay): iki öğe ÖNCE kurulur: `sariOge = oge({alfa: (f) => 1 − kis((f − FM) / 8)})`,
  `murOge = oge({alfa: (f) => kis((f − FM) / 8)})`, `FM = fr(anlam)`. Sonra ARDIŞIK iki çağrı (aralarında başka çizim yok):
  `daire(cx, cy, rx, ry, {bas: fr(Today), sure: 14, tohum: 4242, ses: "tik", ad: "today daire", oge: sariOge})` ve
  `daire(cx, cy, rx, ry, {bas: fr(Today), sure: 14, tohum: 4242, renk: RT.murekkep, ses: false, ad: "today daire mürekkep", oge: murOge})`.
  Aynı tohum + ardışık çağrı = aynı kalem biçimi; 14,14'te sarı söner, mürekkep ikizi belirir.
- `hap` (17. olay): ÖNCE `dinamik` dolgu grubu, SONRA yazı (yazı üstte). Dolgu: `f < FM` boş; `u = kis((f − FM) / 8)`,
  `s = 0.7 + 0.3 · cikis(u)`; `new S.P.Path.Rectangle({rectangle: new S.P.Rectangle(hcx − HAP_W·s/2, KY2 − HAP_H·s/2, HAP_W·s,
  HAP_H·s), radius: HAP_H·s/2, fillColor: renkCoz(RT.vurguDolgu), opacity: cikis(u), insert: false})`, `hcx = hx0 + HAP_W / 2`.
  Yazı `yazi("MEANING", {..., bas: FM + 3, sure: 6, ses: false})` (§4). `olay(FM, "parilti", 0.5)`.
  Hap kart 2 kutusundan SONRA kurulur (kart çizgisinin üstünde kalsın; kutu darbeleri `kok`ta, en altta).

## 8. Tek sarı kuralı (S2-duzeltme madde 2; BRIEF-S2 "o anda tek sarı MEANING")

Aynı anda en çok bir sarı öğe. Sarı zinciri: karaoke 1 (3,39–5,8; odak 1 ile aynı yerde birleşir) → odak *in the winter*
(4,47–8,6) → karaoke 2 (8,37–11,07) → odak *today* (10,13–11,7) → today dairesi (11,42–14,4) → `MEANING` hapı (14,14–son).
Bantlar, eksenler, kar, now noktası, oklar, soru altçizgisi SARI DEĞİL (`RT.ikincil` / `RT.murekkep`). Bu yüzden kış bantları
ve today bandı gri (ana ders sahne 08'de sarıydı; burada sarı olsaydı 16,62'de hapla ikinci sarı olurdu).
YASAK: `Simple Present` etiketine ok, kart 1'e herhangi bir bağ, ikinci ok.

## 9. Bekçiler (sessiz geçiş yok, `throw new Error(...)`)

- Kart satırlarının sağ ucu: satır 1'ler `x1 > SAG − 40`; satır 2'ler `x1 > IKX − 16` (giysi sağ alt köşede); today dairesi
  `cx + rx > IKX − 12`.
- Satır A: `Simple Present` sağ ucu + 32 > `GENERAL` x; satır B: `Present Continuous` sağ ucu + 32 > `RIGHT NOW` x.
- Hap: alt kenarı (`KY2 + HAP_H / 2`) > kart 2 satır 1 yazı üstü (`yb2 − BEN · 0.72`) VE x aralıkları kesişiyorsa.
- Kış bandı sayısı < 3; `NX` bir kış bandının içinde; today bandı `[NX − TB, NX + TB]` eksen dışında.
- `AXY2 + NOW_DY + 4 > KUNYE.icerikSon` (1392); soru satırı sağ ucu > `SAG`.

## 10. Kurallar

Tek vurgu sarı (§8) · yeşil yok · kırmızı yok · emoji yok · içerik yazısı ≥ 64 px · satır ≤ 24 karakter · künye, çip, altyazı,
açık/koyu tema modülde (`kalem-paper.js` + `ortak/kunye.js`); sahnede tema kodu yok · sessiz catch yok, try/catch yok ·
`Math.random` / `Date` yok · 2 boşluk girinti, satır ≤ 120 karakter · "kanal" sözü, QR, süre metni yok · dosya başında 3–4 satır
yorum (sahne, kare, t_bas, içerik özeti) · her bölüm `// --- <t> <sözcük>: <olay>` yorumuyla.

## 11. Kabul

`node --check` geçer (şef `.mjs` kopyasıyla dener). Şef koşar:
`cd /home/sef/01dev/_worktrees/kalem-0204 && bash araclar/qa-yerel.sh 02-04-ydt-temel-s2 02-paperjs-ornek 7.9,14.9,17.3 14.9 --hazirla`
→ çıkış 0 (yazı × çizim / yazı × künye çakışması yok, ölçüm hatası yok). Kare PNG'lerinde taşma, kesik yazı, üst üste binme yok;
1536 altı boş; altyazı bandına (1400–1536) içerik girmez; aynı anda en çok bir sarı öğe.
