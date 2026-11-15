# SPEC — simple-present-temel-s1 · sahne 02-paperjs-deger (Değer) · huni v2 · 15.11

Şef tasarımı (istem D-S1). Tek dosya, tek agy koşusu:
**Yazılacak dosya:** `/home/sef/01dev/_worktrees/kalem-0204/projeler/simple-present-temel-s1/sahneler/02-paperjs-deger/sahne-02.js` (yeni).
Başka dosyaya dokunma. Silme yok. Test, render, git yok. `kalem-paper.js`, `sayfa.html`, `calistir.sh`, `nesneler.json` HAZIR, DEĞİŞMEZ.

Bağlayıcı kaynak: `/home/sef/01dev/dijital-anlatim/.claude/docs/huni-v2-standart.md` §1–§2 ve
`/home/sef/01dev/_worktrees/kalem-0204/projeler/simple-present-temel-s1/BRIEF-S1.md` ("Sahne içeriği" 3,40–14,63).

## 0. Emsal kod ve alınacak kalıp

| Emsal (mutlak yol) | Alınacak kalıp |
|---|---|
| `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s1/sahneler/02-paperjs-ornek/sahne-02.js` | dosya iskeleti: import satırları (yol `simple-present-temel-s1/sahneler/02-paperjs-deger`), `export const KARE, T_BAS`, `export async function kur(P)`, `sahneKur(P, { KARE, tBas: T_BAS })` (bolum YOK), `eyGen` (tegaki genişlik), `al()` sözcük bekçisi (aynen), `not()` kayıtları, bekçi `throw new Error` biçimi, `oge()`, `kutu()`, `ok()`, `daire()`, `cumle()` + `altCizgi(kel, { tut: 24, alt: ALT })`, `svgCiz`, odak alt çizgisi (`ciz` duz, `RT.vurguDolgu`, w 9), `metinOge1.g.data = { kalemTur, kalemAd }` (kayan grubun kapı kutusu) |
| `/home/sef/01dev/_worktrees/kalem-0204/projeler/simple-present-temel-s1/sahneler/02-paperjs-deger/kalem-paper.js` | API (okunur, değişmez): `sahneKur` dönüşü `{ fr, not, olay, ciz, daire, ok, kutu, yazi, elYazisi, cumle, altCizgi, dinamik, svgCiz, sozcukler, oge, genislik, kis, yumus, cikis, lerp }`; `kutu()` köşe taşması (satır 137–145); `yazi()` kutusu taban − 0,9 × boy … taban + 0,3 × boy; `oge({ kay, alfa })` her karede `matrisUygula` ile matrisi SIFIRLAR |
| `/home/sef/Silinecekler/2026-11-15-huni-v2/simple-present-temel-s1-eski/sahneler/02-paperjs-ornek/sahne-02.js` | içerik kaynağı (aynı örnek cümle, `go + es` formülü); yerleşimi ALINMAZ |

## 1. Bantlar ve sabitler (1080×1920; içerik x 60–960, y 460–1380)

```
   0–280  boş · 291–339 kanal (kunye.js) · 360–450 künye (kunye.js) · 460–1380 içerik · 1400–1550 altyazı · 1570–1920 boş
   sağ 960–1080 boş. Kanal, künye, altyazı kalem-paper.js kare() içinde çizilir; sahne-02.js bunlara dokunmaz.
```

| Sabit | Değer | Not |
|---|---|---|
| `KENAR`, `SAG`, `SOL` | `KUNYE.kenar` (60), `KUNYE.sag` (960), `KENAR + 24` (84) | |
| `KUTU_PAY` | 10 | `kutu()` köşe taşması 8 + kalem 2 (sözleşme satır 76) |
| `TR_X`, `TR_Y`, `B_TR` | 60, 560, 72 | Caveat 700 `Kardeşim gider:` (sahne 01 son karesi; D-01 istemiyle ortak) |
| `KANCA_Y`, `KANCA_H` | 620, 200 | kanca kart satırı görünür 620–820 |
| kart kutusu | `kutu(x0 + KUTU_PAY, KANCA_Y + KUTU_PAY, 360, 180)` | `go` x0 = 60 (kutu x 70), `goes` x0 = 580 (kutu x 590) |
| `B_KART`, `Y_KART` | 120, 750 | Fredoka 700; `go` orta x 250, `goes` orta x 770 (`hizala: "orta"`) |
| `KART_MX`, `KART_MY` | 250, 720 | `go` kartının yerel merkezi (ölçek ekseni) |
| `KART_YARIM` | 188 | kart görünür yarım genişliği (360 + 2 × 8) / 2 |
| `SORU_X`, `SORU_Y`, `B_SORU` | 510, 760, 140 | kalem `?` (Caveat el yazısı), x 450–570 ortası |
| küçük figür | `svgCiz("open-peeps/standing-2.svg", { kutu: [700, 460, 60, 140] })` | ayna YOK (doğal yön sola bakar) |
| küçük otobüs | `svgCiz("coco/bus.svg", { kutu: [770, 530, 190, 70], ayna: true })` | SVG doğal yönü sağa; `ayna` → sola gider |
| `KAY_DY` | 260 | kanca satırı 4,20'de aşağı kayar: 620–820 → 880–1080 (EN karta yer açar) |
| `KX`, `KW`, `KY`, `KH` | `KENAR + KUTU_PAY` (70), `SAG − KENAR − 2·KUTU_PAY` (880), `KANCA_Y + KUTU_PAY` (630), 220 | EN kart kutusu, görünür 62–958 × 620–859 |
| `IC`, `BEN`, `ALT` | `KX + 40` (110), 72, 0.30 | EN kart yazısı Fredoka 700 72 |
| `yb1`, `yb2` | `KY + 82` (712), `yb1 + 92` (804) | satır tabanları (`cumle` `aralik: 92`) |
| `OTOBUS` | `[726, 730, 220, 85]`, `ayna: true` | büyük otobüs, EN kartın sağında, `bus.` satırının yanında |
| `DX_ES` | `genislik("-", F_EN) + 20` (≈ 49) | `es` sağa kayma payı (`go-es`); kare turu 1: + 12 iken daire tireye değdi |
| `Y_ESIT` | 950 | Caveat 72 `= he` tabanı, x `IC + 8` (118) |
| `YA`, `YB`, `BSAT` | 1100, 1250, 72 | alt satır tabanları, Fredoka 700 72 |
| `OK_ARA`, `OK_BOY` | 20, 64 | satır oku: zamir sonu + 20 → + 64 |
| `KUCUK` | 0.6 | küçük `go` kartı (yazı 120 × 0,6 = 72) |
| `BEKLE_X`, `BEKLE_Y` | 842, 949 | `go` kartı bekleme merkezi (görünür 729–955 × 889–1009) |
| `DON_X`, `DON_Y` | `xB1 + 2·OK_ARA + OK_BOY + KART_YARIM·KUCUK` (≈ 833), `YB − (Y_KART − KART_MY)·KUCUK` (1232) | `go` kartının satır B sonundaki yeri; kart yazı tabanı = `YB` |

`F_EN = "700 72px Fredoka"`. Renkler yalnız `RT.*` belirteci: `murekkep`, `ikincil`, `vurgu`, `vurguDolgu`, `kirmizi`. Ham renk kodu YOK.

## 2. Zaman (yerel kare = round((t − 3,00) × 30); hepsi `al()` ile sözcükten)

`s1 = S.sozcukler(1)`, `s2 = S.sozcukler(2)`. `al()` çağrıları (dizin, beklenen): s1: 4 `goes` · 5 `mu?`. s2: 0 `My` · 1 `brother`
· 2 `goes` · 3 `to` · 4 `school` · 5 `by` · 6 `bus.` · 7 `He,` · 8 `she,` · 9 `it` · 12 `s` · 13 `gelir.` · 14 `I,` · 15 `you,` · 16 `we,`
· 17 `they` · 19 `gelmez.`

| Kare sabiti | Formül | Değer |
|---|---|---|
| `F_GOESK` | `fr(s1[4].t)` | 12 |
| `F_SORU` | `fr(s1[5].t)` | 24 |
| `F_KAY0`, `F_KAY1` | `fr(s1[5].t1)`, `F_KAY0 + 10` | 36, 46 |
| `F_MY` | `fr(My.t)` | 50 |
| `F_UC0`, `F_UC1` | `fr(goes.t) − 6`, `fr(goes.t) + 3` | 61, 70 |
| `F_GO0`, `F_GO1` | `F_UC1`, `F_GO0 + 12` | 70, 82 |
| `F_HE`, `F_SHE`, `F_IT` | `fr(He,.t)` … | 122, 139, 154 |
| `F_S` | `fr(s.t)` | 188 |
| `F_GELIR` | `fr(gelir..t)` | 197 |
| `F_I` … `F_THEY` | `fr(I,.t)` … `fr(they.t)` | 229, 253, 274, 296 |
| `F_DON0`, `F_DON1` | `fr(gelmez..t)`, `F_DON0 + 10` | 318, 328 |

## 3. Öğeler ve olaylar (sırayla yaz)

Hazır öğe (kare 0'da tam görünür, sahne 01'den devralınır): `bas` negatif, ses YOK. `kutu()` ilk kenarda ses olayı yazar ve
ses parametresi almaz → hazır kart kutusu için yerel `kutuHazir(x, y, w, h, o)` yaz: `kutu()` ile AYNI 4 kenar geometrisi
(kalem-paper.js satır 138–143), her `ciz` `ses: false`, `tur: "kart"`, `bas: −40`.

| # | Olay | Kare / küresel sn | Sözcük | Yapım |
|---|---|---|---|---|
| 1 | `Kardeşim gider:` hazır | 0 | — | `yazi` Caveat 700 `B_TR`, x `TR_X`, taban `TR_Y`, `RT.murekkep`, `bas: −30`, `oge: trA` |
| 2 | kart `go` hazır | 0 | — | özel kap `kartGo` (§4) içinde: `kutuHazir(70, 630, 360, 180, { oge: kartGo, w: 4, renk: RT.ikincil })` + `yazi("go")` Fredoka 700 `B_KART`, `hizala: "orta"`, x 250, taban `Y_KART`, `bas: −30` |
| 3 | küçük figür + küçük otobüs hazır | 0 | — | §1 kutuları, `bas: −200`, `sure: 2`, `sessiz: true`, `w: 3.4`, ikisi de `oge: eskiz` |
| 4 | kart `goes` | 8 (kutu) / 12 (yazı) | 3,40 `goes` | `kartGoes` kabı: kutu alt kabı `kutuGoes` içinde `kutu(590, 630, 360, 180, { bas: F_GOESK − 4, sure: 10, w: 4, renk: RT.ikincil })`; `yazi("goes")` orta x 770, taban `Y_KART`, `bas: F_GOESK`, `sure: 6`, `olcek: true`, `ses: "tik"` |
| 5 | kalem `?` | 24 | 3,80 `mu?` | `elYazisi("?", { x: SORU_X − eyGen("?", B_SORU)/2, y: SORU_Y, boyut: B_SORU, renk: RT.murekkep, bas: F_SORU, sure: 10, oge: soruOge })` |
| 6 | kanca satırı aşağı kayar | 36–46 | 4,20 `mu?` sonu | `kartGo`, `kartGoes` (§4) ve `soruOge` (`kay: { f0: F_KAY0, f1: F_KAY1, dx: 0, dy: KAY_DY }`) |
| 7 | EN kart kutusu | 46–60 | 4,67 `My` | `kutu(KX, KY, KW, KH, { bas: F_KAY1, sure: 14, w: 4, renk: RT.ikincil })` |
| 8 | TR satırı soluk Caveat'e döner | 50–60 | 4,67 | `trA` alfa 1 → 0; aynı metin `trB` (`RT.ikincil`, `bas: −30`) alfa 0 → 1 (`oge({ alfa })`, `kis((f − F_MY) / 10)`); sahne sonuna dek kalır |
| 9 | figür + küçük otobüs solar | 50–62 | 4,67 | `eskiz` alfa `1 − kis((f − F_MY) / 12)` |
| 10 | büyük otobüs kalemle | 50–96 | 4,67 → 6,19 `bus.` | `svgCiz("coco/bus.svg", { kutu: OTOBUS, ayna: true, bas: F_MY, sure: fr(bus..t) − F_MY, azami: 25, w: 4, sesAralik: 3 })` |
| 11 | EN cümle + karaoke | 50–96 | `My` 4,67 · `brother` 4,99 · `to` 5,51 · `school` 5,63 · `by` 6,03 · `bus.` 6,19 | `cumle([My, brother (satir 0), to, school, by, bus. (satir 1)], { x: IC, y: yb1, boyut: BEN, aile: "Fredoka", agirlik: 700, renk: RT.murekkep, aralik: 92 })`; metin `w.s` (sözcük dosyasından). `goes` cümleye GİRMEZ (#13) |
| 12 | `goes` kartı cümledeki yerine uçar | 61–70 | 5,23 `goes` | §4 `kartGoes` uçuşu; `kutuGoes` alfa 1 → 0 (61–70); kap `F_UC1 + 3`'ten sonra `visible = false` |
| 13 | cümledeki `goes` | 70 | 5,23 | `goX = kel[1].x1 + genislik(" ", F_EN)`; `yazi("go", { x: goX, y: yb1, boyut: BEN, aile: "Fredoka", agirlik: 700, bas: F_UC1, sure: 2 })`; `yazi("es", { x: goX + genislik("go", F_EN), …, oge: esOge })`; `esOge.g.data = { kalemTur: "yazi", kalemAd: "es" }` |
| 14 | karaoke | 50–… | 7 sözcük | `altCizgi([My, brother, goesK, to, school, by, bus.], { tut: 24, alt: ALT })`; `goesK = { x0: goX, x1: goX + genislik("goes", F_EN), y: yb1, boyut: BEN, bas: fr(goes.t) }` |
| 15 | `goes` sarı alt çizgi (kalıcı) | 72–78 | 5,23 | `ciz([[goX − 4, yU], [goX + genislik("goes", F_EN) + 4, yU − 2]], { duz: true, w: 9, renk: RT.vurguDolgu, alfa: 0.9, bas: F_UC1 + 2, sure: 6, tur: "isaret", ses: "tik", ad: "odak goes" })`, `yU = yb1 + BEN·ALT` |
| 16 | kart `go` soluk, sağ kenarda bekler | 70–82 | 5,23 | §4 `kartGo` evre 2 (ölçek 0,6, alfa 0,4) |
| 17 | `My brother` → `= he` kalem oku | 122–134 | 7,08 `He,` | `ok([IC − 14, yb1 − 0.3·BEN], [IC − 4, Y_ESIT − 0.3·72], { bas: F_HE, sure: 12, w: 6, uzun: 18, bukum: 0.05, yon: [−1, 0], renk: RT.murekkep, ad: "ok he" })` (kart sol payında, `to` sözcüğünün solundan iner) |
| 18 | Caveat `= he` | 126–140 | 7,08 | `elYazisi("= he", { x: IC + 8, y: Y_ESIT, boyut: 72, renk: RT.murekkep, bas: F_HE + 4, sure: 14 })` |
| 19 | satır A zamirleri | 122 / 139 / 154 | `He,` 7,08 · `she,` 7,64 · `it` 8,12 | `yazi` Fredoka 700 `BSAT`, taban `YA`, x `SOL`'dan yan yana: `he` · `" · "` · `she` · `" · "` · `it`; zamir `RT.murekkep`, ayraç `" · "` (U+00B7) `RT.ikincil`; ayraç sonraki zamirle aynı karede; `sure: 4`, `olcek: true`, zamirde `ses: "tik"`; `xA1` = `it` sonu |
| 20 | `goes` → `go-es` | 188–194 | 9,25 `s` | `esOge.kay = { f0: F_S, f1: F_S + 6, dx: DX_ES, dy: 0 }`; `yazi("-", { x: goX + genislik("go", F_EN) + 4, y: yb1, …, renk: RT.murekkep, bas: F_S + 6, sure: 4 })` (es kaydıktan SONRA; kapı yazı × yazı uyarısı olmasın) |
| 21 | `es` sarı daire | 196–214 | 9,25 | `daire(cx, yb1 − 0.3·BEN, genislik("es", F_EN)/2 + 10, BEN·0.5, { bas: F_S + 8, sure: 18, a0: −2.0, ad: "es daire" })`, `cx` = kaymış `es` ortası (renk varsayılan `RT.vurgu`); sarı belirteç 2: #15 + #21 |
| 22 | satır A oku + `goes` | 197–213 | 9,57 `gelir.` | `ok([xA1 + OK_ARA, YA − 0.3·BSAT], [xA1 + OK_ARA + OK_BOY, YA − 0.3·BSAT], { bas: F_GELIR, sure: 10, w: 6, uzun: 18, bukum: 0.04, renk: RT.murekkep, ad: "ok A" })`; `yazi("goes", { x: xA1 + 2·OK_ARA + OK_BOY, y: YA, Fredoka 700 BSAT, renk: RT.murekkep, bas: F_GELIR + 6, sure: 4, olcek: true, ses: "tik" })` |
| 23 | satır B zamirleri | 229 / 253 / 274 / 296 | `I,` 10,62 · `you,` 11,42 · `we,` 12,14 · `they` 12,86 | #19 ile aynı kalıp, taban `YB`: `I` · `you` · `we` · `they`; `xB1` = `they` sonu |
| 24 | soluk `go` kartı satır B'nin yanına döner | 318–328 | 13,59 `gelmez.` | §4 `kartGo` evre 3 (alfa 0,4 → 1, `DON_X`, `DON_Y`) |
| 25 | satır B oku | 318–328 | 13,59 | #22 oku, `YB` ve `xB1` ile, `bas: F_DON0`, `ad: "ok B"` |
| 26 | `s` yuvası + kırmızı kalem çizgisi | 328–339 | 13,59 | `kartGo` içinde YEREL koordinatla (kartla birlikte ölçeklenir): alt kap `sYuva` (`opacity: 0.5`) içinde `yazi("s", { x: 250 + genislik("go", F_KART)/2 + 6, y: Y_KART, Fredoka 700 B_KART, renk: RT.ikincil, bas: F_DON1, sure: 4 })`; `ciz([[sx0 − 8, Y_KART + 12], [sx1 + 8, Y_KART − 66]], { duz: true, w: 12, renk: RT.kirmizi, alfa: 0.95, bas: F_DON1 + 3, sure: 8, oge: kartGo, tur: "isaret", ad: "s yuvası kırmızı" })`; `F_KART = "700 120px Fredoka"`, `sx0/sx1` = `s` yazısının x0/x1 |
| — | son durum | 328–348 | 13,59–14,63 | iki satır `he · she · it → goes` / `I · you · we · they → go`; hiçbir öğe sahne sonuna dek kaybolmaz (soluyan yalnız: #9 eskiz, #12 `goes` kartı kutusu, #5 `?` evre 2'de) |

`?` (#5) soluşu: `soruOge.alfa = (f) => 1 − kis((f − F_UC0) / 8)` (soru cevaplandı; `goes` kartı uçarken söner).
Her olaya `not("<ad> (<sözcük>)", kare)` yaz (emsal gibi).

## 4. Ölçekli kaplar (`kartGo`, `kartGoes`)

`oge()` matrisi her karede sıfırlar (yalnız `kay` çevirisi + `nefes`), ölçek taşımaz. Bu yüzden iki kart `oge()` DEĞİLDİR:
- `const kartGo = { g: new P.Group({ applyMatrix: false }) }`; `kutu`/`ciz`/`yazi` `oge: kartGo` alır (kalem-paper `c.og.g.addChild`, `o.oge.g.addChild`).
- Alt kaplar aynı biçim: `kutuGoes` → `kartGoes.g.addChild(kutuGoes.g)`; `sYuva` (`opacity: 0.5`) → `kartGo.g.addChild(sYuva.g)`.
- Kapı kutusu: `kartGo.g.data = { kalemTur: "kart", kalemAd: "kart go" }`, `kartGoes.g.data = { kalemTur: "kart", kalemAd: "kart goes" }`
  (paperTopla grup kutusunu matrisle okur, içine inmez; kart kuralı uçuşta yanlış uyarı vermez).
- Her kare: `S.dinamik((f) => { … })` içinde matris ve opaklık atanır (dinamik'in kendi grubu kullanılmaz).
  Matris: `new P.Matrix().translate(cx, cy).scale(s).translate(−px, −py)`; evre içi `u = yumus((f − f0) / (f1 − f0))`, `cx, cy, s, alfa` doğrusal ara değer.

| Kap | Pivot (px, py) | Evre (kare) | (cx, cy, s, alfa) |
|---|---|---|---|
| `kartGo` | (250, 720) | f ≤ `F_KAY0` | (250, 720, 1, 1) |
| | | `F_KAY0`–`F_KAY1` | → (250, 720 + KAY_DY, 1, 1) |
| | | `F_GO0`–`F_GO1` | → (`BEKLE_X`, `BEKLE_Y`, `KUCUK`, 0.4) |
| | | `F_DON0`–`F_DON1` | → (`DON_X`, `DON_Y`, `KUCUK`, 1); sonra sabit |
| `kartGoes` | (xG0, `Y_KART`); `xG0 = 770 − genislik("goes", F_KART)/2` | f ≤ `F_KAY0` | (xG0, `Y_KART`, 1) |
| | | `F_KAY0`–`F_KAY1` | → (xG0, `Y_KART` + KAY_DY, 1) |
| | | `F_UC0`–`F_UC1` | → (`goX`, `yb1`, `BEN / B_KART`); `kutuGoes.g.opacity` 1 → 0 |
| | | f ≥ `F_UC1 + 3` | `kartGoes.g.visible = false` (cümle yazısı #13 `F_UC1`'de açılır; 2 kare aynı yerde üst üste, titreme yok) |

## 5. Bekçiler (`throw new Error`, sessiz geçiş yok)

1. `TR_X + genislik("Kardeşim gider:", "700 72px Caveat") > SAG`.
2. Satır 1 kaymış sonu: `goX + genislik("go", F_EN) + DX_ES + genislik("es", F_EN) + 12 > OTOBUS[0] − 14`.
3. Satır 2 sonu (`kel[5].x1`) `> OTOBUS[0] − 20`.
4. `OTOBUS[0] + OTOBUS[2] > SAG − 8` · `KX + KW > KUNYE.sag − KUTU_PAY` · `BEKLE_X + KART_YARIM·KUCUK > SAG − 4`.
5. Satır A sonu (`goes` x1) `> SAG` · `DON_X + KART_YARIM·KUCUK > SAG − 4`.
6. Dikey: `TR_Y − B_TR·0.9 < KUNYE.icerikBas` · `DON_Y + 100·KUCUK > KUNYE.icerikSon` · `YB + BSAT·0.3 > KUNYE.icerikSon`.
7. `eyGen("?", B_SORU) <= 0` (glif yok).

Beklenen değerler (fontkit ölçümü): `goX` ≈ 496 · satır 1 kaymış sonu ≈ 688 · satır 2 110–655 · daire x ≈ 604–700 · `xA1` ≈ 423,
satır A `goes` ≈ 527–678 · `xB1` ≈ 616 · `DON_X` ≈ 833 (kart görünür 720–945) · içerik dikey ≈ 495–1292.

## 6. Kurallar

Tek vurgu sarı (`vurgu`/`vurguDolgu`: karaoke, #15, #21); yeşil YOK; kırmızı YALNIZ #26. Emoji yok. İçerik yazısı ≥ 64 px
(`?` 140, kart 120, ölçekli kart 72, diğerleri 72). Satır ≤ 24 karakter. Söylenmeyen yeni TR satır YOK (`Kardeşim okula …` yazma).
Ekran metni sesten önce gelmez (hazır öğeler sahne 01'de söylendi). Tema kodu yok (`RT` belirteci yeter). `try/catch` yok.
`Math.random` / `Date` yok. 2 boşluk girinti, satır ≤ 120 karakter. Kanal, dakika, eski kapanış sözü, QR, süre metni YOK.
Dosya başı yorum: `// Sahne 02 (simple-present-temel-s1 Shorts, huni v2) — Değer: Paper.js, 1080x1920, 361 kare, t_bas 3.00.`

## 7. Kabul

`node --check` (şef `.mjs` kopyasıyla) · `bash araclar/qa-yerel.sh simple-present-temel-s1 02-paperjs-deger 3.05,8.80,14.55 8.80 --hazirla`
çıkış 0 · `node araclar/cakisma-kapisi.mjs simple-present-temel-s1 --sahne 02-paperjs-deger --port 41333 --sunucu 41022` çıkış 0, 0 uyarı ·
karelerde kanal katmanı yerinde; 0–280, 1570–1920, x 960–1080 boş; son karede iki satır + EN kart + soluk TR birlikte.
