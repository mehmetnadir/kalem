# SPEC — 02-04-ydt-temel-dikey · sahne 03-paperjs-ornek1 (Paper.js, 1080×1920, 721 kare, t_bas 20,22)

Kök: `K = /home/sef/01dev/_worktrees/kalem-0204`. Sahne dizini: `K/projeler/02-04-ydt-temel-dikey/sahneler/03-paperjs-ornek1/`.
İki kod dosyası var. Her agy koşusu YALNIZ kendisine verilen dosyayı yazar:

| Dosya (mutlak yol) | Bölüm |
|---|---|
| `K/projeler/02-04-ydt-temel-dikey/sahneler/03-paperjs-ornek1/kalem-paper.js` | §A |
| `K/projeler/02-04-ydt-temel-dikey/sahneler/03-paperjs-ornek1/sahne-03.js` | §B |

`calistir.sh` ve `sayfa.html` şef yazar. Test, render, git yok. Silme yok. `ortak/`a, başka sahneye, yatay pakete dokunma.
Genel: 2 boşluk girinti, satır ≤ 120 karakter, Türkçe yorum, `Math.random` / `Date` yok (zaman yalnız kareden).
Renkler yalnız `RT.*` belirteçleri (`RT.murekkep`, `RT.ikincil`, `RT.vurgu`, `RT.vurguDolgu`): tema çifti (açık + koyu) böyle çalışır.
Ham renk kodu, kırmızı, yeşil, emoji YOK.

---

## §A — `kalem-paper.js` (sahneye özel kalem modülü)

**Taban:** yatay modül `K/projeler/02-04-ydt-temel/sahneler/03-paperjs-ornek1/kalem-paper.js` (403 satır). Onu baştan sona
kopyala; aşağıdaki DEĞİŞİKLİKLERİ uygula; geri kalan her işlev (ciz, daire, egri, ok, kutu, tik, svgCiz, yazi, elYazisi,
cumle, altCizgi, dinamik, parilti, sozcukler, `__kalemKutu.paperTopla`, `gunluk`, OLAYLAR/ZAMANLAR günlüğü) aynen kalır.
Dikey karşılık örneği: `K/projeler/present-continuous-dikey/sahneler/02-paperjs-kanca/kalem-paper.js` (`kucul` gövdesi ve
`altyaziMetin` satırı oradan).

1. **Dosya başı yorumu** (≤ 3 satır): "DİKEY 1080×1920, 02-04 sahne 03; taban yatay 02-04 sahne 03 kalem-paper.js;
   değişiklikler SPEC §A".
2. **İçe aktarma ve sabitler:**
   - `import { kunyeHazirla, zeminCiz, kunyeCiz, altyaziMetin, altyaziCiz, RENK, RT, renkCoz, temaSurum, KOK }
     from "/projeler/02-04-ydt-temel-dikey/ortak/kunye.js";`
   - `import { yaziNoktalari } from "/projeler/02-04-ydt-temel-dikey/ortak/kalem-canvas.js";`
   - `PK = "/projeler/02-04-ydt-temel-dikey/ortak"`, `W = 1080, H = 1920`. Dışa aktarım `{ RENK, RT, renkCoz }` ve
     `kis`, `yumus`, `cikis` aynen.
3. **`sahneKur` imzası aynen:** `sahneKur(P, { KARE, tBas, bolum, etkin, kayma = 0 })`.
4. **Künye + altyazı (`kare()` içinde):** `kunyeCiz(oc, { bolum, logo: K.logo });` satırından hemen sonra
   `altyaziCiz(oc, altyaziMetin(K.altyazi, tBas + fe / 30));` (fe = dondurulmuş kare; altyazı her karede `K.altyazi`dan
   OKUNUR — sahne listeyi değiştirebilsin diye kopya alınmaz). `etkin` künyeye geçmez (dikey künye ajanda çizmez).
5. **`kucul` (öğe küçülmesi)** — `matrisUygula(e, f)` gövdesi dikey örnekteki (`present-continuous-dikey/…/02-paperjs-kanca/
   kalem-paper.js`) gövdeyle değiştirilir: `e.kucul = { f0, f1, s, px, py, dx, dy }` →
   `u = yumus((f − f0) / (f1 − f0))`, `k = lerp(1, s, u)`;
   `m = new P.Matrix(); m.translate(dx·u, dy·u).translate(px, py).scale(k).translate(−px, −py)`; sonra mevcut kay/nefes
   dönüşümü aynı matrise eklenir; `if (e.alfa) e.g.opacity = e.alfa(f)` aynen.
6. **`yazi()` öğeye bağlanır:** `o.oge` verilirse yazının grubu (`g`) `o.oge.g.addChild(g)` ile öğe grubunun ÇOCUĞU olur
   (öğe küçülünce ve solunca yazı da küçülür, solar). `g.data = { kalemTur: "yazi", kalemAd: str }` aynen kalır.
   Ayrıca yazı nesnesine `desc` alanı eklenir: aynı font ile `olc.measureText(str).actualBoundingBoxDescent` (px).
7. **`cumle(kel, o)`:** `o.oge` her `yazi()` çağrısına geçer.
8. **`altCizgi(kel, o)` (karaoke):**
   - Çizgi tabanı `z.y + z.boyut * 0.16` yerine `z.y + Math.max(z.boyut * 0.28, (z.desc || 0) + 8)` (BRIEF-DIKEY §0:
     altçizgi taban + 0,28 em; kuyruklu sözcükte kuyruğun altından geçer).
   - `o.oge` verilirse karaoke grubu `o.oge.g.addChild(g)` ile öğeye bağlanır.
   - Başka değişiklik yok (renk `RT.vurguDolgu`, tut/solma aynen).
9. **`elYazisi()`:** `if (o.oge) { o.oge.g.addChild(g); o.oge.g.data = …; }` satırındaki `o.oge.g.data = …` ATAMASI KALKAR
   (öğe grubuna `kalemTur` yazılırsa çakışma kapısı bütün kartı tek "yazi" kutusu sayar, içindeki çizimi görmez).
   `o.oge.g.addChild(g)` ve `g.data` kalır.
10. **Renk dönüşü (`donus`)** — "eski belirteç söner, `ikincil` çizgiye döner" (BRIEF-DIKEY §0, aynı anda en çok 3 sarı):
    - `ciz(pts, o)`: `c.renk0 = c.renk; c.alfa0 = c.alfa; c.donus = o.donus == null ? null : o.donus;` (kalemGeo sonrası).
    - `kare()` darbe döngüsünde `ilerle`den ÖNCE: `const istenen = c.donus != null && fe >= c.donus ? RT.ikincil : c.renk0;`
      `if (c.renk !== istenen) { c.renk = istenen; c.alfa = istenen === RT.ikincil ? 0.75 : c.alfa0; c.tam = false; }`
    - Tema değişimi dalı (`temaSurum`) aynen çalışır.

Kabul §A: `node --check` geçer (ES modül); dışa aktarılan `sahneKur` dönüş nesnesi değişmez (aynı anahtarlar).

---

## §B — `sahne-03.js` (içerik)

**Kalıp:** yatay `K/projeler/02-04-ydt-temel/sahneler/03-paperjs-ornek1/sahne-03.js` — `EN2` sabiti (AYNEN kopyala),
`MONT` ve `TISORT` birim ızgara darbeleri (AYNEN kopyala), `elCizim()`, `alti()`, `yalin()`, `s3` sözcük dizini, `not()`
kayıtları, olay sırası. Ölçüler yataydan DEĞİL, aşağıdaki tablodan (dikey px, `u()` YOK — 1080 genişlik tabanı).
Dikey dosya yapısı örneği: `K/projeler/present-continuous-dikey/sahneler/03-paperjs-ornek1/sahne-03.js` (`eyGen` ile ortalı
el yazısı, `pen()` sözcük penceresi, `kutu`/`cumle`/`altCizgi` çağrı biçimi).

İskelet:
```
import { sahneKur, RT } from "/projeler/02-04-ydt-temel-dikey/sahneler/03-paperjs-ornek1/kalem-paper.js";
import { KUNYE } from "/projeler/02-04-ydt-temel-dikey/ortak/kunye.js";
import { yaziNoktalari } from "/projeler/02-04-ydt-temel-dikey/ortak/kalem-canvas.js";
export const KARE = 721, T_BAS = 20.22;
export async function kur(P) { const S = await sahneKur(P, { KARE, tBas: T_BAS,
  bolum: KUNYE.cipler["03-paperjs-ornek1"], etkin: 1, kayma: 0 }); … return S; }
```
Zaman: yerel kare `fr(t) = round((t − 20,22) × 30)`. İlk 12 kare (0–11) geçiş altında DURGUN: hiçbir olay 12'den önce
başlamaz. Son 12 kare durgun (`SON = 708`): bütün olaylar 708'den önce BİTER (kalem-paper zaten dondurur).
Sözcük zamanı: `s3 = S.sozcukler(3)`; dizin tablosu yataydaki yorumla aynı (0 Birinci … 36 wearing.). `f(i) = s3[i].f`.
Kart B cümlesi `EN2`'den (`fr(t)`); `sozcukler.json`'da yok, yeniden ölçme YOK.
El yazısı genişliği: dikey örnekteki `eyGen(str, boyut)` (tegaki `metrik.json` + `glyphData-700.json`, `yaziNoktalari`).

### B.1 Yerleşim (px, 1080×1920; içerik bandı 352–1392, kenar 48, genişlik 984; altyazı 1400–1536 kalem-paper'da)

```
y 352 ┌──────────────── ÜST ŞERİT (32,2'den) ─────────────────┐  wears → GENERAL            [mont 100]
  472 └────────────────────────────────────────────────────────┘
  380 ┌ KART A (20,77–32,3) ──────────┐   490 ┌ KART B (32,1'den) ─────────────┐
      │ She wears her coat     (478)  │       │ She is wearing her      (588)  │
      │ in the winter.         (564)  │       │ pink T-shirt today.     (674)  │
      │ Kışın montunu giyer.   (680)  │       │ Bugün pembe tişörtünü…  (790)  │
  724 └───────────────────────────────┘   830 └────────────────────────────────┘
  750  MONT 367×440 (x 357–723)          871  TİŞÖRT 420×378 (x 330–750)
 1190                                    1249
 1296  GENERAL (Caveat 80, ortalı)       1340  RIGHT NOW (Caveat 80, ortalı)
```

| Öğe | Değer |
|---|---|
| Kart A kutusu | `kutu(48, 380, 984, 344, { w: 4, renk: RT.ikincil, oge: kartA })` |
| Kart A cümle | Fredoka 700 72, x 88, satır 0 taban 478, satır 1 taban 564 (`aralik: 86`); satır 0 = s3[5..8] `She wears her coat`, satır 1 = s3[9..11] `in the winter.` |
| TR 1 | `elYazisi("Kışın montunu giyer.", { x: 88, y: 680, boyut: 64, renk: RT.murekkep, oge: kartA, sozcukler: … })` |
| Mont | `elCizim(MONT, [320, 750, 440, 440], [100, 120], { w: 4.8, oge: kartA })` → çizim ≈ 367×440, x ≈ 357–723 |
| GENERAL | Caveat 80, taban 1296, x = 540 − eyGen("GENERAL", 80)/2, `RT.murekkep`, `oge: kartA` |
| Kart B kutusu | `kutu(48, 490, 984, 340, { w: 4, renk: RT.ikincil })` |
| Kart B cümle | Fredoka 700 72, x 88, satır 0 taban 588 (EN2[0..3] `She is wearing her`), satır 1 taban 674 (EN2[4..6] `pink T-shirt today.`) |
| TR 2 | `elYazisi("Bugün pembe tişörtünü giyiyor.", { x: 88, y: 790, boyut: 64, renk: RT.murekkep, sozcukler: … })` |
| Tişört | `elCizim(TISORT, [330, 860, 420, 400], [100, 90], { w: 4.8 })` → ≈ 420×378, y ≈ 871–1249 |
| RIGHT NOW | Caveat 80, taban 1340, x = 540 − eyGen("RIGHT NOW", 80)/2, `RT.murekkep` |
| Üst şerit kutusu | `kutu(48, 352, 984, 120, { w: 4, renk: RT.ikincil })` |
| Şerit `wears` | `yazi("wears", { x: 88, y: 434, boyut: 64, aile: "Fredoka", agirlik: 700, renk: RT.murekkep })` |
| Şerit ok | `ok([wears.x1 + 24, 414], [wears.x1 + 114, 414], { w: 6, renk: RT.ikincil, bukum: 0.04 })` |
| Şerit GENERAL | `elYazisi("GENERAL", { x: wears.x1 + 134, y: 436, boyut: 64, renk: RT.murekkep, bas, sure: 9 })` |
| Şerit mont simgesi | `elCizim(MONT, [916, 362, 100, 100], [100, 120], { w: 3.2 })` → ≈ 83×100 (≥ 96 px yükseklik) |

- `kartA = S.oge({ kucul: { f0: 350, f1: 360, s: 0.3, px: 48, py: 380, dx: 0, dy: -28 },
  alfa: (f) => 1 - S.kis((f - 350) / 10) })` — kart A + TR 1 + mont + GENERAL + bunların altçizgileri (karaoke dahil)
  bu öğede. 350 → 360 karede kart üst şeride doğru küçülür ve söner; 360'tan sonra opaklık 0 (çakışma kapısı < 0,2 opak
  öğeyi saymaz; kart B yazısı 366'da başlar).
- `elCizim()` yataydaki işlev; dikeyde sabit px alır. `o.oge` verilirse her `ciz()` çağrısına `oge: o.oge` geçer; düğme
  dairesi dahil. Darbe türü `tur: "cizim"`, `ad` öğe adı ("mont", "tisort", "mont-simge").
- `alti(x0, x1, y, bas, ad, ek)`: yataydaki işlev; `w: 10`, `renk: RT.vurgu`, `tur: "isaret"`, `sure: 14`; `ek` nesnesi
  `oge` ve `donus` alanlarını `ciz()`e geçirir. `bitis(d)`'de `olay(…, "tik", 0.5)` ve `not(ad, d.bas)` aynen.
- `altY(z) = z.y + Math.max(72 * 0.28, z.desc + 8)` (odak altçizgisi karaoke ile aynı kural; `z.desc` §A.6).
- `yalin(z)`: sondaki noktalama hariç sözcük sonu (yatay kalıp; font `"700 72px Fredoka"`).
- Karaoke: `altCizgi(czA, { tut: 40, w: 9, oge: kartA })`, `altCizgi(czB, { tut: 40, w: 9 })`.

### B.2 Olay listesi (bu sırayla; kare = fr(t); her satıra `not("<ad>", kare)`)

| # | Olay | Küresel sn / kare | Cümle sözcüğü | Ayrıntı |
|---|---|---|---|---|
| 1 | kart A kutusu | 20,77 / 17 | s3[0] Birinci | `bas: f(0), sure: 28` |
| 2 | kart A cümle sözcük sözcük + karaoke | 24,22–25,78 / 120–167 | s3[5..11] | `cumle(…, { oge: kartA })` |
| 3 | mont çizimi | 25,02 / 144 | s3[8] coat | `bas: f(8), sure: 42` |
| 4 | TR 1 el yazısı | 26,79 / 197 | s3[12..14] | pencereler `[12,13,14].map(i => ({ f0: f(i), f1: i < 14 ? f(i+1) : s3[i].f1 }))` |
| 5 | odak *in the winter* | 28,55 / 250 | s3[15] Her | `alti(czA[4].x0, yalin(czA[6]), altY(czA[4]), f(15), "odak in the winter", { oge: kartA })` |
| 6 | GENERAL el yazısı | 30,31 / 303 | s3[18] Genel | `sozcukler: [{ f0: f(18), f1: f(20) }]` |
| 7 | GENERAL altçizgisi | 31,35 / 334 | s3[20] geniş | `alti(g1.x0, g1.x1, 1296 + 18, f(20), "GENERAL altçizgi", { oge: kartA })`; biter 348 |
| 8 | kart A küçülür + söner (çift kart kuralı) | 31,89–32,22 / 350–360 | s3[21] zaman. bitişi | `kartA.kucul` + `alfa` (yukarıda) |
| 9 | şerit kutusu | 32,02 / 354 | — | `bas: 354, sure: 10` |
| 10 | şerit mont simgesi | 32,09 / 356 | — | `bas: 356, sure: 12` |
| 11 | kart B kutusu | 32,15 / 358 | EN2 She (32,41) öncesi ≤ 0,6 sn | `bas: 358, sure: 8` (366'da biter) |
| 12 | şerit `wears` | 32,25 / 361 | — | `bas: 361, sure: 5` |
| 13 | şerit ok | 32,32 / 363 | — | `bas: 363, sure: 6`; `olay` sesi ok'un kendi `cizgi` olayı |
| 14 | şerit GENERAL | 32,35 / 364 | — | `bas: 364, sure: 9` (≈ 373'te biter) |
| 15 | kart B cümle sözcük sözcük + karaoke | 32,41–34,13 / 366–417 | EN2 | `cumle(EN2.map(([s, t], i) => ({ s, f: fr(t), satir: i < 4 ? 0 : 1 })), …)` |
| 16 | tişört çizimi | 33,63 / 402 | EN2 T-shirt | `bas: fr(33.63), sure: 36` |
| 17 | TR 2 el yazısı | 35,37 / 454 | s3[22..25] | pencereler `[22..25]`, son `s3[25].f1` |
| 18 | odak *today* | 38,17 / 539 | s3[28] bugüne | `alti(czB[6].x0, yalin(czB[6]), altY(czB[6]), f(28), "odak today", { donus: f(35) })` |
| 19 | RIGHT NOW el yazısı | 39,05 / 565 | s3[30] konuşma | `sozcukler: [{ f0: f(30), f1: f(31) }, { f0: f(31), f1: f(32) + 8 }]` |
| 20 | RIGHT NOW altçizgisi | 41,45 / 637 | s3[33] Şimdiki | `alti(g2.x0, g2.x1, 1340 + 18, f(33), "RIGHT NOW altçizgi")` |
| 21 | *is* altçizgisi + *today* ikincile döner | 42,81 / 678 | s3[35] is | `alti(czB[1].x0, yalin(czB[1]), altY(czB[1]), f(35), "is altçizgi")` |
| 22 | *-ing* altçizgisi | 43,05 / 685 (biter 699) | s3[36] wearing. | `x0 = czB[2].x0 + genislik("wear", "700 72px Fredoka")`, `x1 = czB[2].x1` |

Sarı sayımı: kart A evresinde en çok 2 (odak + GENERAL altı) + karaoke; son karede 3 (RIGHT NOW altı, *is*, *-ing*);
*today* odağı 678'de `ikincil`e döner (§A.10). Şerit, ok ve kart kutuları sarı DEĞİL.

### B.3 Altyazı düzeltmesi (sahne içi; `ortak/` yazılmaz)

`ortak/anlatim/altyazi.json` cümle 3'ün ikinci yarısında kaymış: EN `She is wearing her pink T-shirt today.` 35,37–38,49
yazılı (gerçekte 32,41–34,55 söyleniyor) ve TR parçası 38,65'te başlıyor (gerçekte `Bugün` 35,37). Sahne, `sahneKur`dan
hemen sonra `S.K.altyazi` listesini düzeltir:
1. `cumle === 3 && t0 >= 32` olan bütün girdileri çıkar.
2. Yerlerine (zaman sırasıyla, kalan cümle 3 girdilerinden hemen sonra) şu 4 girdiyi ekle; her biri
   `{ cumle: 3, konusan: "ogretmen", dil, t0, t1, metin }`:

| dil | t0 | t1 | metin |
|---|---|---|---|
| en | 32.41 | 34.55 | `She is wearing her pink T-shirt today.` |
| tr | 35.37 | 37.13 | `Bugün pembe tişörtünü giyiyor.` |
| tr | 37.53 | 40.81 | `Bu yalnız bugüne ait, konuşma anında oluyor.` |
| tr | 41.45 | 43.93 | `Şimdiki zaman: is wearing.` |

Kaynak: `EN2` (EN), `s3[22]`, `s3[25]`, `s3[26]`, `s3[32]`, `s3[33]`, `s3[36]` (TR). Yeni dizi `S.K.altyazi`ya atanır
(kalem-paper her karede oradan okur). Yorumla gerekçe 2 satır.

### B.4 Kurallar

- Yazı tabanı ≥ 50 px (en küçük yazı 64). Satır ≤ 24 karakter (en uzun satır `pink T-shirt today.` 19).
- Çakışma: yazı ↔ çizim kutusu kesişmez (mont 750–1190 ↔ TR 1 ≤ 700 ve GENERAL ≥ 1240; tişört 871–1249 ↔ TR 2 ≤ 808 ve
  RIGHT NOW ≥ 1285). Şerit yazısı kart A sönmeden (361 öncesi) başlamaz.
- İçerik 1392'nin altına inmez (en alt RIGHT NOW altçizgisi ≈ 1365).
- Boş çerçeve: kart A kutusu 20,77'de (BRIEF §3), ilk sözcük 24,22 (3,45 sn < 4 sn); kart B kutusu ilk sözcükten 0,2 sn önce.
- Durağanlık ≤ 4 sn (en uzun boşluk 21,7 → 24,22).
- `Math.random`, `Date` yok; `await` yalnız `sahneKur` ve tegaki `fetch` için.

### B.5 Kabul ölçütü (şef doğrular)

1. `node --check` geçer; `qa-yerel.sh 02-04-ydt-temel-dikey 03-paperjs-ornek1 31.85,38.9,43.6 43.6 --hazirla` çıkış 0.
2. Karelerde: 31,85 kart A + mont + GENERAL (+ altı) tam; 38,9 şerit (`wears → GENERAL` + mont simgesi) + kart B + tişört +
   TR 2 + *today* altı; 43,6 son düzen, 3 sarı belirteç, RIGHT NOW altında altçizgi.
3. Taşma, kesik yazı, üst üste binme, boş kare yok; altyazı bandında konuşulan dilim; 1536 altı boş.
