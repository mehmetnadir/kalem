# SPEC — 02-04-ydt-temel-dikey · sahne 02-paperjs-kanca (Paper.js, 1080×1920, 529 kare, t_bas 3,00)

Kök: `K = /home/sef/01dev/_worktrees/kalem-0204`. Sahne dizini: `K/projeler/02-04-ydt-temel-dikey/sahneler/02-paperjs-kanca/`.
Bu sahnede iki kod dosyası var. Her agy koşusu YALNIZ kendisine verilen dosyayı yazar:

| Dosya | Bölüm |
|---|---|
| `…/02-paperjs-kanca/kalem-paper.js` | §A |
| `…/02-paperjs-kanca/sahne-02.js` | §B |

`calistir.sh` ve `sayfa.html` şef yazar. Test, render, git yok. Silme yok. `ortak/`a ve başka sahneye dokunma.

Genel kurallar: 2 boşluk girinti, satır ≤ 120 karakter, Türkçe yorum, `Math.random` / `Date` yok (zaman yalnız kareden).
Zaman: yerel kare `fr(t) = round((t − 3,00) × 30)`; ilk 12 kare (0–11) geçiş altında DURGUN → hiçbir olay 12'den önce
başlamaz (`f0 = (t) => Math.max(12, fr(t))`). Son 12 kare durgun (`SON = KARE − 13 = 516`; kalem-paper zaten dondurur).

---

## §A — `kalem-paper.js` (sahneye özel ortak kalem modülü)

**Taban:** yatay modül `K/projeler/02-04-ydt-temel/sahneler/02-paperjs-kanca/kalem-paper.js` (419 satır). Onu baştan sona
kopyala, aşağıdaki DEĞİŞİKLİKLERİ uygula; geri kalan her işlev (ciz, daire, egri, kutu, tik, svgCiz, yazi `matris`/`son`,
elYazisi, cumle, dinamik, parilti, sozcukler, `__kalemKutu.paperTopla`, `gunluk`) aynen kalır.
Dikey karşılık için ikinci örnek: `K/projeler/present-continuous-dikey/sahneler/02-paperjs-kanca/kalem-paper.js`
(`kucul` ve altyazı satırı oradan alınır).

1. **İçe aktarma ve sabitler**
   - `import { kunyeHazirla, zeminCiz, kunyeCiz, altyaziMetin, altyaziCiz, RENK, RT, renkCoz, temaSurum, KOK, KUNYE }
     from "/projeler/02-04-ydt-temel-dikey/ortak/kunye.js";`
   - `import { yaziNoktalari } from "/projeler/02-04-ydt-temel-dikey/ortak/kalem-canvas.js";`
   - `PK = "/projeler/02-04-ydt-temel-dikey/ortak"`, `W = 1080, H = 1920`. Dışa aktarım `{ RENK, RT, renkCoz, KUNYE }` kalır.
2. **`sahneKur` imzası:** `sahneKur(P, { KARE, tBas, bolum, etkin, kayma = 0, hud = null })`. `dersGoster` KALKAR, yerine `hud`.
   `hud(fe) → { ders: boolean, rozet: number 0..1 }` (fe = dondurulmuş kare).
3. **Künye çizimi (`kare()` içinde, yatayın `dersGoster` dalının yerine):**
   - `hud` yoksa ya da `h.ders && h.rozet >= 1` ise: `kunyeCiz(oc, { bolum, etkin, logo: K.logo })` (tam künye).
   - Değilse kırpma ile çiz: `oc.save(); oc.beginPath();` `oc.rect(0, 0, W, 150)` (logo y 48–144 + çip y 48–128 her zaman);
     `h.ders` ise `oc.rect(0, 150, RX − 6, 170)`; `h.rozet > 0` ise `oc.rect(RX − 6, 150, (W − KUNYE.kenar − RX + 12) * h.rozet, 170)`;
     `oc.clip(); kunyeCiz(…); oc.restore();`
   - `RX` (rozet hapının sol x'i) `sahneKur` içinde bir kez, fontlar yüklendikten sonra hesaplanır:
     `olc.font = "700 " + KUNYE.dersYazi + "px Fredoka"; RX = KUNYE.kenar + olc.measureText(KUNYE.ders[1]).width + KUNYE.rozetAra`
     (≈ 670). `KUNYE.ders` bir dizidir (2 satır).
   - Kırpılan kare sonrası kanca kutuları: `window.__kalemKutu.kare`'den `!h.ders` ise `ad === "kunye:ders"`, `h.rozet <= 0` ise
     `ad === "kunye:rozet"` olanlar çıkarılır (yatay kalıbı).
4. **Altyazı:** künyeden sonra `altyaziCiz(oc, altyaziMetin(K.altyazi, tBas + fe / 30));` (dikey örnekteki satır).
5. **`kucul` (öğe küçülmesi):** `matrisUygula` dikey örnekteki gövdeyle değiştirilir: `e.kucul = {f0, f1, s, px, py, dx, dy}` →
   `u = yumus((f − f0)/(f1 − f0))`, `k = lerp(1, s, u)`, `m.translate(dx*u, dy*u).translate(px, py).scale(k).translate(−px, −py)`,
   sonra mevcut kay/nefes dönüşümü eklenir; `e.alfa` aynen.
6. **Karaoke altçizgisi (`altCizgi`):** çizgi tabanı `z.y + z.boyut * 0.16` yerine
   `z.y + z.boyut * (/[gjpqyşçğ]/.test(z.str) ? 0.48 : 0.28)` (BRIEF-DIKEY §0 + sözleşme 14.11 s11: kuyruklu sözcükte
   kuyruğun altından geçer). Başka değişiklik yok.
7. **Renk dönüşü (`donus`) — "eski belirteç söner, ikincil çizgiye döner" (BRIEF-DIKEY §0, en çok 3 sarı):**
   - `ciz(pts, o)`: `o.donus` (kare, isteğe bağlı) darbeye yazılır: `c.renk0 = c.renk; c.donus = o.donus ?? null`.
   - `kare()` darbe döngüsünde, `ilerle`den önce: `const istenen = c.donus != null && fe >= c.donus ? RT.ikincil : c.renk0;`
     `if (c.renk !== istenen) { c.renk = istenen; c.alfa = istenen === RT.ikincil ? 0.75 : c.alfa0; c.tam = false; }`
     (`c.alfa0` kalemGeo sonrası saklanır). Tema değişimi dalı aynen çalışır.
   - `ok(a, b, o)`: `o.donus` gövdeye ve iki uç çizgisine geçer.
8. **`ok` için yol noktaları:** `o.ara` (nokta dizisi, isteğe bağlı) verilirse gövde noktaları `egri()` yerine `[a, ...o.ara, b]`
   olur (ciz `duz` olmadan çağrılır → catmull-rom yumuşatma zaten var). Uç yönü: `uc(b, o.ara[o.ara.length − 1])` (son ara
   noktadan uca). `o.ara` yoksa davranış aynen.
9. Dosya başı yorumu: "DİKEY 1080×1920, 02-04 sahne 02; taban yatay 02-04 kalem-paper.js; değişiklikler SPEC §A" (≤ 4 satır).

---

## §B — `sahne-02.js` (içerik)

**Kalıp:** yatay `K/projeler/02-04-ydt-temel/sahneler/02-paperjs-kanca/sahne-02.js` — `al()` sözcük doğrulama, `cumleGenislik`,
`ucusMatris`, `f0`, `not()` kayıtları, olay sırası. Yerleşim yataydan DEĞİL, aşağıdaki tablodan. Dikey dosya yapısı örneği:
`K/projeler/present-continuous-dikey/sahneler/02-paperjs-kanca/sahne-02.js`.

İskelet:
```
import { sahneKur, RT, KUNYE } from "/projeler/02-04-ydt-temel-dikey/sahneler/02-paperjs-kanca/kalem-paper.js";
export const KARE = 529, T_BAS = 3.0;
export async function kur(P) { … sahneKur(P, { KARE, tBas: T_BAS, bolum: KUNYE.cipler["02-paperjs-kanca"], etkin: 0,
  hud: (f) => ({ ders: f >= FL1, rozet: kis((f − FL1) / 9) }) }) … return S; }
```
`FL1` `let` ile önce `Infinity` tanımlanır, zaman hesaplanınca atanır (yatay kalıbı). Ölçüler `genislik(metin, font)` ile
ölçülür (sabit px genişlik yazma). Fontlar: `F(b) = "700 " + b + "px Fredoka"`. Renkler: `MUR = RT.murekkep`,
`SARI = RT.vurgu`, `DOLGU = RT.vurguDolgu`, `PIL = RT.pilMetin`, `IKI = RT.ikincil`. Sözcükler: `s1 = S.sozcukler(1)`,
`s2 = S.sozcukler(2)`; her zaman `al(dizi, i, "beklenen")` ile alınır.

### B1. Sözcük → kare tablosu (küresel sn; `al` indeksleri doğrulanmış)

| Olay | Sözcük (`al`) | sn | kare |
|---|---|---|---|
| 4. satır `yaşı-yor-um.` | s1[3] `yaşıyorum` | 3,08 | 12 (`f0`) |
| `=` üst çizgi | s1[5] `ikisi` | 4,84 | 55 |
| `=` alt çizgi | s1[6] `de` | 5,24 | 67 |
| şeride toplanma | s1[7] `yaşıyorum` t1 + 0,06 | 6,50 | CF0 = 105, CF1 = CF0 + 12 |
| kart A + sözcükler | s2[0..3] `I live in Istanbul` (ekran `İstanbul.`) | 6,91–7,55 | 117–137 |
| bağ oku 1 | s2[4] `Biri` | 8,60 | 168 |
| `SIMPLE` / `PRESENT` | s2[5] `geniş` / s2[6] `zaman` | 9,08 / 9,40 | 182 / 192 |
| kart B + sözcükler | s2[7..12] `I am living with my uncle` | 10,69–11,73 | 231–262 |
| bağ oku 2 | s2[13] `Öteki` | 12,86 | 296 |
| `PRESENT` / `CONTINUOUS` | s2[14] `şimdiki` / s2[15] `zaman` | 13,50 / 13,94 | 315 / 328 |
| `vs` | s2[18] `iki` | 15,82 | 385 |
| künyeye uçuş | s2[19] `zamanın` | 15,98 | FL0 = fr + 3 = 392, FL1 = FL0 + 18 = 410 |
| rozet açılır | — | ≈ 16,70 | FL1 … FL1 + 9 (kalem-paper kırpması) |
| fark oku | s2[22] `farkını` | 17,26 | 428 |
| `MEANING` + belirteç | s2[25] `anlam` / s2[26] `belirler` | 19,26 / 19,58 | 488 / 497 |

### B2. Kare 0 = sahne 01 son düzeni (Fredoka 700 128, sola hizalı x 96)

| Satır | Metin | Taban y | bas |
|---|---|---|---|
| L1 | `İstanbul'da` | 560 | −10 (hazır) |
| L2 | `yaşı-` · `yor` · `-um.` (3 ayrı `yazi`) | 740 | −10 (hazır) |
| L3 | `Amcamla` | 960 | −10 (hazır) |
| L4 | `yaşı-` · `yor` · `-um.` | 1140 | 12 / 14 / 16, sure 4, ilki `ses: true` |

- Parça x'leri: `yaşı-` x 96; `yor` x `96 + genislik("yaşı-", F(128))`; `-um.` x `96 + genislik("yaşı-yor", F(128))`.
  `yor` rengi `PIL` (iki temada koyu, sarı dolgu üstünde okunur); diğerleri `MUR`.
- **yor kutusu** (L2 ve L4): kalın sarı kalem bandı, `ciz([[yx0 − 0.05·B, y − 0.17·B], [yx1 + 0.05·B, y − 0.17·B]],
  { duz: true, w: 1.0·B, renk: DOLGU, alfa: 0.95, uc0: 8, uc1: 12, amp: 0.6, tur: "isaret", ad: "yor kutu L2|L4", oge })`,
  B = 128, yx0/yx1 = `yor` parçasının x aralığı. L2: bas −30, sure 10, ses false. L4: bas 18, sure 8, ses "tik".
- **z-sırası:** her satırın kutu öğesi (`S.oge({ kucul })`) ve `ciz`'i, o satırın `yazi` parçalarından ÖNCE oluşturulur
  (Paper yeni öğeyi üste koyar; yazı kutunun üstünde kalır).

### B3. `=` (4,84 / 5,24)

İki kısa sarı yatay çizgi, sağ koridorda, iki yor satırının arasında: x 872 → 972, y_orta = (L2 kutu merkezi + L4 kutu merkezi)/2
(≈ 918); üst çizgi y_orta − 18 (bas 55), alt çizgi y_orta + 18 (bas 67). `ciz(…, { duz: true, w: 9, renk: SARI, alfa: 0.9,
sure: 8, uc0: 5, uc1: 8, amp: 0.4, ses: "tik", tur: "isaret", ad: "esittir ust|alt", oge: OEQ })`.
`OEQ = S.oge({ alfa: (f) => f < CF0 ? 1 : Math.max(0, 1 − (f − CF0) / 6) })` → şeride toplanırken söner.

### B4. Şeride toplanma (CF0 105 → CF1 117)

Dört satır Fredoka 64'e (ölçek 0,5) iner, üst şeritte iki satır olur. **Zikzak yerleşim** (bağ okları yazının üstünden geçmesin):
şerit satırı 1 SAĞA hizalı (sağ kenar 1032), şerit satırı 2 SOLA hizalı (x 48).

| Kaynak (çapa x, taban y) | Hedef (x, taban y) |
|---|---|
| L1 (96, 560) | `S1X = 1032 − genislik("İstanbul'da yaşı-yor-um.", F(64))` (≈ 328), 420 |
| L2 (96, 740) | `S1X + genislik("İstanbul'da ", F(64))` (≈ 662), 420 |
| L3 (96, 960) | 48, 520 |
| L4 (96, 1140) | `48 + genislik("Amcamla ", F(64))` (≈ 333), 520 |

- Yazı parçaları: `matris: topla(x0, y0, tx, ty)` →
  `(f) => { const q = yumus((f − CF0) / (CF1 − CF0)); return new P.Matrix().translate(lerp(x0, tx, q), lerp(y0, ty, q))
  .scale(lerp(1, 0.5, q)).translate(−x0, −y0); }`. L2/L4'ün üç parçası AYNI çapayı (96, y0) kullanır.
- yor kutusu öğesi: `kucul: { f0: CF0, f1: CF1, s: 0.5, px: 96, py: y0, dx: tx − 96, dy: ty − y0 }` (yazı ile aynı dönüşüm).
- Toplanma sonrası şerit: satır 1 ≈ x 328–1032, yor ≈ 805–905; satır 2 ≈ x 48–703, yor ≈ 476–576. Şerit y 366–535.

### B5. Kart A (sağa hizalı) ve kart B (sola hizalı)

| Öğe | Değer |
|---|---|
| Kart A çerçevesi | `kutu(48, 600, 984, 140, { bas: CF1 − 1, sure: 14, w: 4, ad: "kart A" })` |
| Kart A cümlesi | `I` `live` `in` `İstanbul.` Fredoka 72, taban 695, sağa hizalı: x0 = `992 − cumleGenislik` (≈ 464); `cumle()` sözcük zamanlı |
| Kart A karaoke | `altCizgi(kelA, { tut: 12 })` (8,50'de söner; bağ oku 1'den önce) |
| Kart B çerçevesi | `kutu(48, 880, 984, 140, { bas: fr(10,69) − 4, sure: 14, w: 4, ad: "kart B" })` |
| Kart B cümlesi | `I am living with my uncle.` Fredoka 72, taban 975, x 88 (≈ 88–903; BRIEF §3: tek satır, 812 px) |
| Kart B karaoke | `altCizgi(kelB, { tut: 14 })` (12,73'te söner; bağ oku 2'den önce) |

### B6. Etiketler (Fredoka 64, `MUR`, sure 6, `ses: true`, `son: FL1`, `matris: ucus(...)`)

| Satır | Parçalar | Taban y | x |
|---|---|---|---|
| A (kart A altı) | `SIMPLE` (182) · `PRESENT` (192) · `vs` (385) | 825 | sağa hizalı: `EX = 992 − genislik("SIMPLE PRESENT vs", F(64))` (≈ 408); `PRESENT` `EX + genislik("SIMPLE ", F(64))`; `vs` `EX + genislik("SIMPLE PRESENT ", F(64))` |
| B (kart B altı) | `PRESENT` (315) · `CONTINUOUS` (328) | 1105 | `PRESENT` 88; `CONTINUOUS` `88 + genislik("PRESENT ", F(64))` |

`vs` A satırının sonundadır: okuma sırası `SIMPLE PRESENT vs` / `PRESENT CONTINUOUS` = künyenin iki satırı.

### B7. Künyeye uçuş (FL0 392 → FL1 410) ve rozet

- Hedefler (künye dersi Fredoka 700 56, `FK = F(KUNYE.dersYazi)`): satır 1 taban `KUNYE.dersTaban` (212), satır 2 taban
  `KUNYE.dersTaban + KUNYE.dersSatir` (276). x: `SIMPLE` 48; `PRESENT` (A) `48 + genislik("SIMPLE ", FK)`; `vs`
  `48 + genislik("SIMPLE PRESENT ", FK)`; `PRESENT` (B) 48; `CONTINUOUS` `48 + genislik("PRESENT ", FK)`. 48 = `KUNYE.kenar`.
- `ucus(x0, y0, tx, ty) = (f) => f < FL0 ? new P.Matrix() : (q = yumus((f − FL0)/(FL1 − FL0)), new P.Matrix().translate(lerp(x0, tx, q),
  lerp(y0, ty, q)).scale(lerp(1, KUNYE.dersYazi / 64, q)).translate(−x0, −y0))`.
- `son: FL1` → uçan yazı FL1'de gizlenir; aynı karede `hud.ders` true olur, künye aynı yazıyı çizer (kesintisiz geçiş).
- Rozet `hud.rozet = kis((f − FL1)/9)` → kalem-paper soldan sağa açar. `olay(FL1, "tik", 0.4)`.

### B8. Bağ okları (`ok(a, b, { ara, bas, sure: 18, w: 6, uzun: 20, ad, donus })`, `tur` "isaret" ok'ta hazır)

Oklar yazının üstünden GEÇMEZ. Noktalar ölçülen konumdan türetilir (≈ değerler kontrol için):

| Ok | a (başlangıç) | ara | b (uç) | bas | donus |
|---|---|---|---|---|---|
| 1: şerit 1. *yor* → *live* | (yor1 orta x, 420 + 22) ≈ (855, 442) | `[[S2 sağ uç + 34, 566], [live orta x + 14, 598]]` ≈ (737, 566), (572, 598) | (live orta x, 695 − 0.72·72 − 10) ≈ (558, 633) | 168 | fr(10,69) = 231 |
| 2: şerit 2. *yor* → *am living* | (yor2 orta x, 520 + 22) ≈ (526, 542) | `[[330, 700], [amLiving orta x + 6, 880]]` ≈ (330, 700), (275, 880) | (amLiving orta x, 975 − 0.72·72 − 10) ≈ (269, 913) | 296 | fr(17,26) = 428 |

- S2 sağ uç = şerit satırı 2'nin son x'i (≈ 703). live / amLiving orta x: kart sözcüklerinin `(x0 + x1)/2` (`am living` için
  `kelB[1].x0` ile `kelB[2].x1`).
- Kontrol: ok 1 y 466–535 aralığında x ≥ 715 (şerit 2 bitişi 703); ok 2 y 643–715 aralığında x ≤ 420 (kart A yazısı ≈ 464'ten
  başlar), y 780–825'te x ≤ 400 (etiket A ≈ 408'den başlar).

### B9. Fark oku ve MEANING

- **Fark oku** (17,26): `ok([960, 748], [960, 872], { cift: true, bas: 428, sure: 16, w: 7, uzun: 22, bukum: 0.05,
  ad: "fark oku", donus: fr(19,26) })` — kart A altı ↔ kart B üstü, sağ kenarda (etiket satırı bu anda boş).
- **MEANING belirteci** (önce oluşturulur; yazının altında kalır): `ciz([[MX0 − 14, 1310 − 0.18·140], [MX1 + 16, 1310 − 0.18·140]],
  { duz: true, w: 0.36·140, renk: DOLGU, alfa: 0.8, uc0: 6, uc1: 14, amp: 1.2, bas: 488, sure: 497 − 488, tur: "isaret",
  ses: false, ad: "MEANING belirtec" })` → 19,58'de biter, yazının alt yarısını (taban 1310, büyük harf üstü ≈ 1212) örter.
- **MEANING** (19,26): `yazi("MEANING", { x: 540, y: 1310, hizala: "orta", boyut: 140, aile: "Fredoka", agirlik: 700, renk: MUR,
  bas: 488, sure: 8, olcek: true, ses: true })`. MX0/MX1 = `540 ∓ genislik("MEANING", F(140))/2` (≈ 231–849).

### B10. Sarı sayımı (aynı anda en çok 3 belirteç; künye çipi ve rozeti sayılmaz)

| Aralık | Sarı belirteçler |
|---|---|
| 3,47–4,84 | yor kutu L2, L4 |
| 4,84–6,70 | + `=` (toplanmada söner) |
| 6,91–8,50 | yor ×2 + karaoke A |
| 8,60–10,69 | yor ×2 + ok 1 |
| 10,69–12,73 | yor ×2 + karaoke B (ok 1 `ikincil`) |
| 12,86–17,26 | yor ×2 + ok 2 |
| 17,26–19,26 | yor ×2 + fark oku (ok 2 `ikincil`) |
| 19,26– | yor ×2 + MEANING belirteci (fark oku `ikincil`) |

### B11. Kayıt ve kurallar

- Her olay için `not("<ad>", kare)` (yatay kalıbı). Ses olayları: L4 ilk parça `ses: true`, kutular "tik", çerçeve ilk kenar,
  etiketler `ses: true`, `olay(FL1, "tik", 0.4)`.
- Bütün içerik y 352–1392 bandında; x 48–1032. Altyazı bandına (1400–1536) ve platform bandına öğe girmez.
- Emoji yok, kırmızı yok, yeşil yok. Yazı tabanı ≥ 50 px (en küçük 56/64).
- Eski çizim/çerçeve 4 sn'den uzun boş beklemez (kart çerçevesi ilk sözcükle başlar).

### Kabul ölçütü

1. `node --check` iki dosyada hatasız (şef koşar).
2. `cd K && bash araclar/qa-yerel.sh 02-04-ydt-temel-dikey 02-paperjs-kanca 5.6,14.6,20.1 17.8 --hazirla` çıkış 0 (şef koşar).
3. Kareler: 5,6 sn dört satır + iki yor kutusu + `=`; 14,6 sn şerit + iki kart + dört etiket + iki ok (yazıya değmez);
   20,1 sn künyede ders 2 satır + rozet, fark oku, MEANING + belirteç, oklar `ikincil`; koyu 17,8 sn yor yazısı okunur.
