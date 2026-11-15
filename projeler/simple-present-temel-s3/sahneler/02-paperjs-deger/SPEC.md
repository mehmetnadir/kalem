# SPEC — simple-present-temel-s3 · sahne 02-paperjs-deger · huni v2 (15.11)

Şef tasarımı (istem `uretim-tutanagi/istem/sahne/D-02-paperjs-deger.md`). Tek dosya, tek agy koşusu:

- YAZILACAK: `/home/sef/01dev/_worktrees/kalem-0204/projeler/simple-present-temel-s3/sahneler/02-paperjs-deger/sahne-02.js` (yeni dosya)
- KALIP (yalnız okunur): `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s1/sahneler/02-paperjs-ornek/sahne-02.js`
- API (yalnız okunur): `/home/sef/01dev/_worktrees/kalem-0204/projeler/simple-present-temel-s3/sahneler/02-paperjs-deger/kalem-paper.js`

Başka dosyaya dokunma. Silme yok. Test, render, git yok. `kalem-paper.js`, `sayfa.html`, `calistir.sh`, `nesneler.json` DEĞİŞMEZ.
Bağlayıcı: `/home/sef/01dev/dijital-anlatim/.claude/docs/huni-v2-standart.md` §1–§2, `../../BRIEF-S3.md` "Sahne içeriği" 3,89–12,84.

## 1. Kalıptan alınan (aynen)

- Baş yorum 3 satır: sahne adı + kare + t_bas; içerik özeti; `// huni v2 (15.11): yerleşim x 60–960, y 460–1380; çip yok; kanal katmanı kunye.js'te.`
- İçe aktarma: `import { sahneKur, RT, KUNYE } from "/projeler/simple-present-temel-s3/sahneler/02-paperjs-deger/kalem-paper.js";`
  (`yaziNoktalari` ve tegaki `fetch` bloğu GEREKMEZ; `eyGen`, `pen`, `satir` yardımcıları YOK.)
- `export const KARE = 281, T_BAS = 3.89;` · `export async function kur(P)` · `const S = await sahneKur(P, { KARE, tBas: T_BAS });`
  (`bolum` YOK) · API'den kullanılanlar: `fr, ciz, daire, ok, kutu, yazi, elYazisi, cumle, altCizgi, oge, not, genislik, kis`.
- `noktasiz` + `al(dizi, i, beklenen)` sözcük bekçisi kalıptaki gibi (satır 37–47). Sözcükler `const s2 = S.sozcukler(2);`.
- `not(ad, kare)` her olayda (kalıp gibi). Sonda `return S;`.

## 2. Sözcükler (`al(s2, i, …)`; küresel sn → yerel kare = `fr(t)` = round((t − 3,89) × 30))

| Değişken | i | beklenen | t | kare |
|---|---|---|---|---|
| `wDoes` | 3 | `does` | 6,28 | 72 |
| `wS1` | 5 | `s` | 7,24 | 101 |
| `wOna` | 6 | `ona` | 7,56 | 110 |
| `wS2` | 9 | `s` | 8,99 | 153 |
| `wGelmez` | 10 | `gelmez.` | 9,23 | 160 |
| `wHe` | 11 | `He` | 10,36 | 194 |
| `wDoesnt` | 12 | `doesn't` | 10,60 | 201 |
| `wGo1` | 13 | `go.` | 11,16 | 218 |
| `wDoes2` | 14 | `Does` | 11,96 | 242 |
| `wShe` | 15 | `she` | 12,20 | 249 |
| `wGo2` | 16 | `go?` | 12,36 | 254 |

Kısaltmalar: `F_HE = fr(wHe.t)`, `F_S2 = fr(wS2.t)`, `F_GEL = fr(wGelmez.t)`. Yardımcı: `const sonma = (f0, n) => (f) => 1 - kis((f - f0) / n);`.

## 3. Ölçü sabitleri (çıplak sayı yalnız bu blokta; türetilen formülle)

| Sabit | Değer | Formül / not |
|---|---|---|
| `KENAR`, `SAG` | 60, 960 | `KUNYE.kenar`, `KUNYE.sag` |
| `KUTU_PAY` | 10 | kutu() köşesi 8 px + kalem taşar; görünür kenar 60'ta kalır (emsal ile aynı) |
| `KX` | 70 | `KENAR + KUTU_PAY` |
| `KW` | 680 | sabit; görünür kart x 62–758 (sahne 01 kartı ≈ 700 px) |
| `IC` | 110 | `KX + 40` (bütün kart yazıları sola hizalı) |
| `KY0`, `KH0` | 490, 140 | `KUNYE.icerikBas + 20 + KUTU_PAY`; görünür kart 0: y 480–639 (sahne 01 son karesi: x 60, y 480–640) |
| `Y0`, `B0` | 582, 80 | kart 0 yazı tabanı, Fredoka 700 80 |
| `KY1`, `KH` | 490, 200 | `KY0`; görünür kart 1: y 480–699 |
| `KY2` | 770 | `KY1 + 280`; görünür kart 2: y 760–979 |
| `Y1`, `Y2` | 566, 846 | `KY1 + 76`, `KY2 + 76` (EN taban) |
| `T1`, `T2` | 644, 924 | `KY1 + 154`, `KY2 + 154` (soluk TR taban) |
| `B1`, `BTR`, `ALT` | 72, 52, 0.30 | kart 1–2 EN Fredoka 700 72 · TR Caveat 700 52 · altçizgi tabandan pay |
| `XX`, `XS` | 790, 64 | `KX + KW + 40` · ✗ kenarı (✗ x 790–854) |

Kart 0 parça konumları (`const F80 = "700 80px Fredoka"`, `g = (s) => genislik(s, F80)`), soldan sağa, boşluk `g(" ")`:
`xHe = IC` · `xDo = xHe + g("He") + g(" ")` · `xEs1 = xDo + g("do")` · `xNt = xEs1 + g("es")` · `xGo = xNt + g("n't") + g(" ")` ·
`xEs2 = xGo + g("go")` · `xNokta = xEs2 + g("es")` · `gEs = g("es")`. Beklenen (fontkit): 110 · 223,6 · 312,6 · 392,0 · 501,8 · 590,1 · 669,5; son 687,1.

Türetilen: daire `DCX = (xDo + xNt) / 2 − 4` (≈ 303,8), `DCY = Y0 − 26`, `DRX = (xNt − xDo) / 2 + 8` (≈ 92,2), `DRY = 70` (şef kare turu 1; 50 `s`yi kesiyordu) ·
ok `OA = [xEs2 + gEs / 2, Y0 − 50]` (≈ 629,8; 532), `OB = [xEs1 + gEs / 2, Y0 − 50]` (≈ 352,3; 532), `OBUK = 0.2` ·
bant `BY = Y0 − B0 * 0.22`, kalınlık `B0 * 0.70`.

## 4. Katman sırası (Paper'da sonra kurulan üstte; oge'leri BU SIRAYLA, yazılardan ÖNCE kur)

| # | Öğe | Kurulum | İçerik |
|---|---|---|---|
| 1 | `BANT1` | `oge({ alfa: sonma(F_S2, 6) })` | `es` (goes) arkası sarı bant |
| 2 | `SARI` | `oge({ alfa: sonma(F_GEL, 6) })` | `does` sarı dairesi + `es` (does) arkası sarı bant |
| 3 | `ESKI` | `oge({ alfa: sonma(F_HE, 4) })` | kart 0 kutusu, kart 0 yazıları (`es` goes HARİÇ), mürekkep daire |
| 4 | `DUSEN` | `oge({ kay: { f0: F_HE, f1: F_HE + 10, dx: 0, dy: 120 }, alfa: sonma(F_HE, 5) })` (şef kare turu 1: 70 → 120) | `es` (goes) yazısı + kırmızı üstü çizgi |
| 5 | `OK1` | `oge({ alfa: sonma(F_S2, 6) })` | `es` → `does` oku |
| 6 | `CARPI` | `oge({ alfa: sonma(F_HE, 4) })` | kırmızı ✗ |

`DUSEN.g.data` YAZMA (kapı yazı kutusunu grup içinden okur; çizgi `isaret` türünde muaf). Kart 1–2 öğeleri oge'siz (kök/üst katman).

## 5. Olaylar (kare = yerel; hepsi `not()` ile kayıt)

| # | Olay | Kare | Çapa | Çağrı (öz) |
|---|---|---|---|---|
| 1 | Kart 0 kutusu hazır | 0 | — | `kutu(KX, KY0, KW, KH0, { bas: -40, sure: 14, w: 4, renk: RT.ikincil, oge: ESKI, ad: "kart 0 kutusu" })` |
| 2 | Kart 0 yazısı hazır: `He` `do` `es` `n't` `go` `.` (ESKI) + `es` (DUSEN) | 0 | — | her parça `yazi(str, { x, y: Y0, boyut: B0, aile: "Fredoka", agirlik: 700, renk: RT.murekkep, bas: -30, sure: 4, ses: false, oge })` |
| 3 | `does` sarı dairesi | 72 | 2:3 does (6,28) | `daire(DCX, DCY, DRX, DRY, { bas: fr(wDoes.t), sure: 12, oge: SARI, ad: "does dairesi" })` (renk varsayılan `RT.vurgu`) |
| 4 | `es` (goes) arkası bant (ek_ayir) | 101 | 2:5 s (7,24) | `ciz([[xEs2 − 5, BY], [xEs2 + gEs + 6, BY]], { duz: true, w: B0 * 0.70, renk: RT.vurguDolgu, alfa: 0.6, uc0: 5, uc1: 9, amp: 1.0, bas: fr(wS1.t), sure: 8, tur: "isaret", ses: "tik", oge: BANT1, ad: "es bandı goes" })` |
| 5 | Kavisli ok `es` → `does` | 101 | 2:5 s (7,24) | `ok(OA, OB, { bas: fr(wS1.t), sure: 12, w: 6, uzun: 18, bukum: OBUK, yon: [0, -1], oge: OK1, ad: "es oku" })` (renk varsayılan; yay kartın üstünden, tepe ≈ 476) |
| 6 | `es` (does) arkası bant: `do-es` | 110 | 2:6 ona (7,56) | olay 4 ile aynı, x `xEs1`, `bas: fr(wOna.t)`, `oge: SARI`, `ad: "es bandı does"` |
| 7 | Kırmızı üstü çizgi `es` (goes) | 153 | 2:9 s (8,99) | `ciz([[xEs2 − 4, Y0 − 18], [xEs2 + gEs + 4, Y0 − 26]], { duz: true, w: 7, renk: RT.kirmizi, alfa: 0.95, uc0: 4, uc1: 6, amp: 0.5, bas: F_S2, sure: 8, tur: "isaret", oge: DUSEN, ad: "üstü çizili es" })` |
| 8 | Ok + bant 1 söner | 153–159 | 2:9 s | `OK1`, `BANT1` alfa (§4); kod gerekmez, `not` yaz |
| 9 | Kırmızı ✗ | 160 / 165 | 2:10 gelmez. (9,23) | iki darbe: `[[XX, Y0 − 56], [XX + XS, Y0 + 8]]` `bas: F_GEL` ve `[[XX + XS, Y0 − 56], [XX, Y0 + 8]]` `bas: F_GEL + 5`; ikisi `duz: true, w: 8, renk: RT.kirmizi, alfa: 0.95, uc0: 5, uc1: 8, amp: 0.4, sure: 7, tur: "isaret", oge: CARPI, ad: "carpi"`; ikinci `ses: false` |
| 10 | `does` dairesi mürekkebe döner | 160 | 2:10 gelmez. | `daire(DCX, DCY, DRX, DRY, { renk: RT.murekkep, bas: F_GEL, sure: 6, ses: false, oge: ESKI, ad: "does dairesi mürekkep" })`; sarı `SARI` 6 karede söner |
| 11 | `es` düşer ve solar; ✗ silinir; kart 0 söner | 194–204 | 2:11 He (10,36) | `DUSEN` kay + alfa, `CARPI`, `ESKI` alfa (§4) |
| 12 | Kart 1 kutusu | 194 | 2:11 He | `kutu(KX, KY1, KW, KH, { bas: F_HE, sure: 12, w: 4, renk: RT.ikincil, ad: "kart 1 kutusu" })` |
| 13 | Kart 1 EN `He doesn't go.` | 198 / 201 / 218 | 2:11–13 | `kel1 = cumle([{ s: "He", f: F_HE + 4 }, { s: "doesn't", f: fr(wDoesnt.t) }, { s: "go", f: fr(wGo1.t) }], { x: IC, y: Y1, boyut: B1, aile: "Fredoka", agirlik: 700, renk: RT.murekkep })` + `yazi(".", { x: kel1[2].x1, y: Y1, boyut: B1, aile: "Fredoka", agirlik: 700, renk: RT.murekkep, bas: fr(wGo1.t), sure: 4 })`. `He` F_HE + 4: kart 0 sönmeden yeni yazı gelmez (kapı yazı × yazı) |
| 14 | Soluk TR `O gitmez.` | 226–240 | 2:13 go. + 8 | `elYazisi("O gitmez.", { x: IC, y: T1, boyut: BTR, renk: RT.ikincil, bas: fr(wGo1.t) + 8, sure: 14 })` |
| 15 | Kart 2 kutusu | 234 | 2:14 Does − 8 | `kutu(KX, KY2, KW, KH, { bas: fr(wDoes2.t) - 8, sure: 12, w: 4, renk: RT.ikincil, ad: "kart 2 kutusu" })` |
| 16 | Kart 2 EN `Does she go?` | 242 / 249 / 254 | 2:14–16 | `kel2 = cumle([Does, she, go], { x: IC, y: Y2, … })` (f = `fr(wDoes2.t)`, `fr(wShe.t)`, `fr(wGo2.t)`) + `yazi("?", { x: kel2[2].x1, y: Y2, …, bas: fr(wGo2.t), sure: 4 })` |
| 17 | Soluk TR `O gider mi?` | 249–259 | 2:15 she | `elYazisi("O gider mi?", { x: IC, y: T2, boyut: BTR, renk: RT.ikincil, bas: fr(wShe.t), sure: 10 })` (şef kare turu 1: `go?` 254 donma 268 öncesi bitmiyordu) |
| 18 | Kart karaoke (tek sarı altçizgi kayar; 218'de kart 1 `go`, 254'te kart 2 `go`) | 198–268 | 2:11–16 | `altCizgi([...kel1, ...kel2], { tut: 40, alt: ALT })` (6 sözcük; `.` ve `?` dizide YOK; altçizgi `go` genişliğinde) |

Son 13 kare (268–280) donar (`kalem-paper.js` `SON`); bütün olaylar 266'da biter.

## 6. Bekçiler (`throw new Error("Bekçi: …")`; sessiz geçiş yok)

1. `xNokta + g(".") > KX + KW − 20` (kart 0 yazısı kutuya sığmalı; beklenen 687 ≤ 730).
2. `IC + genislik("He doesn't go.", "700 72px Fredoka") > KX + KW − 20` ve aynısı `"Does she go?"`.
3. `XX + XS > SAG` (✗ sağ sınır 960).
4. `KY0 − 10 < KUNYE.icerikBas` (kart üst kenarı 460'ın altında kalmalı).
5. `KY2 + KH + 10 > KUNYE.icerikSon` (kart 2 alt kenarı ≤ 1380).
6. `OA[1] − OBUK * (OA[0] − OB[0]) < KUNYE.icerikBas` (ok tepesi ≥ 460).
7. `DRX < (xNt − xDo) / 2` (daire `does`'u kapsamalı).
8. `Y1 + B1 * 0.3 > T1 − BTR * 0.9` (kart 1 EN yazı kutusu altı TR yazı kutusu üstüne değmemeli; beklenen 587,6 ≤ 597,2).

## 7. Kurallar

- Renk yalnız `RT.*` belirteci: mürekkep, ikincil, vurgu (daire), vurguDolgu (bant), kirmizi (YALNIZ üstü çizgi ve ✗). Ham renk kodu yok.
- Tek vurgu sarı; kart 1–2'de aynı anda tek sarı (altCizgi). Yeşil yok. Emoji yok (✗ iki kalem darbesidir).
- İçerik yazısı ≥ 64 (80 / 72), soluk TR 52. Satır ≤ 24 karakter. Ekran metni sesten önce gelmez (kart 0 sahne 01'den hazır gelir).
- Kart 0 `goes` iki parçadır: `go` (ESKI) + `es` (DUSEN). Kartta asla `goe` görünmez.
- Ev, bavul, ikon, küçük üstü çizili `goes` notu YOK. `svgCiz` çağrısı yok.
- `try/catch` yok, `Math.random` / `Date` yok, tema kodu yok, 2 boşluk girinti, satır ≤ 120 karakter. "kanal", "dakika", "tam ders" sözü yok.

## 8. Kabul

`node --check` (şef `.mjs` kopyasıyla) · `bash araclar/qa-yerel.sh simple-present-temel-s3 02-paperjs-deger 3.95,8.40,12.75 8.40 --hazirla`
çıkış 0 · `node araclar/cakisma-kapisi.mjs simple-present-temel-s3 --sahne 02-paperjs-deger --port 41333 --sunucu 41022` çıkış 0,
0 uyarı · karelerde kanal katmanı (logo 53,2–246,7 × 291–339, yazı x 263, taban 330); 0–280, 1570–1920 ve x 960–1080 boş.
Kare 2 (3,95): yalnız kart 0. Kare 135 (8,40): daire, iki bant, ok. Kare 266 (12,75): kart 1 + kart 2, altçizgi kart 2 `go` altında.
