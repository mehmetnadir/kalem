# SPEC — 02-04-ydt-temel · sahne 02-paperjs-kanca (Paper.js) · 14.11

Şef tasarımı. Uygulayıcı (agy) YALNIZ şu dosyayı yazar:
`/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel/sahneler/02-paperjs-kanca/sahne-02.js`

Başka dosyaya dokunma. Silme yok. Test, render, git yok. Aynı dizindeki `kalem-paper.js`, `sayfa.html`, `calistir.sh`
HAZIR (şef yazdı); değiştirme.

## 1. Örnek ve kalıp

- Örnek sahne (aynı motor, önceki ders): `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-03-ydt-temel/sahneler/02-paperjs-kanca/sahne-02.js`.
  Kalıbı al (import, `export const KARE, T_BAS`, `export async function kur(P)`, `sahneKur` → içerik → `return S`, `not()` kayıtları).
  İçeriği alma.
- `sayfa.html` şunu çağırır: `import { kur, KARE } from ".../02-paperjs-kanca/sahne-02.js"; surucu(async () => { S = await kur(paper); }, (f) => S.kare(f), KARE);`
- Import yolu (mutlak, sunucu kökü): `/projeler/02-04-ydt-temel/sahneler/02-paperjs-kanca/kalem-paper.js`
  → `import { sahneKur, RT, KUNYE } from "…/kalem-paper.js";`
- Değerler: `KARE = 529`, `T_BAS = 3.0` (zaman.json sahne 2: t_bas 3,00 · t_son 20,22 · içerik 517 kare + 12 geçiş).

## 2. kalem-paper.js API (bu dizindeki kopya; 02-03'e göre şef eklemeleri işaretli)

`const S = await sahneKur(P, { KARE, tBas: T_BAS, bolum: "Hook", etkin: 0, kayma: 0, dersGoster })`
- **dersGoster(f) → bool (şef eki):** false iken künye sol üst ders yazısı ("SIMPLE PRESENT vs PRESENT CONTINUOUS") çizilmez
  ve kapıya girmez. `kur` içinde `let F_IN = Infinity;` tanımla, `dersGoster: (f) => f >= F_IN` ver, F_IN'i aşağıda ata.
- S'ten kullanılacaklar: `fr(t)` (yerel kare = round((t − 3) × 30)), `sozcukler(n)` → `[{s, t, f, t1, f1}]`, `genislik(str, font)`,
  `yazi(str, o)`, `cumle(kel, o)`, `altCizgi(kel, o)`, `kutu(x, y, w, h, o)`, `ciz(pts, o)`, `ok(a, b, o)`, `olay(kare, tur, guc)`,
  `not(ad, kare)`, `lerp`, `yumus`.
- **yazi(str, o) ek alanlar (şef eki):** `o.matris(f) → P.Matrix` kareye bağlı dönüşüm; `o.son` = bu kareden sonra yazı gizli.
  matris uçuştan ÖNCE `new P.Matrix()` (birim) döndürmeli, `null` DEĞİL (geri sarmada eski matris kalır).
- `ciz` varsayılan türü "cizim"dir; bu sahnede bütün süs çizgileri `tur: "isaret"` ile verilir (kapı yazı × çizim çakışmasını
  sayar, isaret saymaz). `ok`/`kutu` türünü kendisi verir.
- Renk yalnız belirteçle: `RT.murekkep`, `RT.ikincil`, `RT.vurgu` (SARI), `RT.vurguDolgu` (DOLGU). Ham renk kodu yazma.

## 3. Ölçü kuralı

- `const W = 1920, H = 1080, u = (n) => n * W / 1920;` Bütün uzunluklar `u()` ya da `W`/`H` oranı. Çıplak px sayısı yok.
- Yazı tabanı `TABAN = u(30)`: hiçbir yazı bunun altına inmez.
- `sigdir(metinler, azami, gen)`: `max(TABAN, min(azami, ...metinler.map(m => azami * gen / genislik(m, font(azami)))))`;
  `font = (b) => \`700 ${b}px Fredoka\``. Bütün yazılar Fredoka 700 (Türkçe harf latin-ext ile yüklü).
- Sözcük doğrulama: `al(dizi, i, beklenen)` — `dizi[i].s` noktalamasız, `toLocaleLowerCase("tr")` ile beklenene eşit değilse
  `throw new Error(...)`. Sessiz geçiş, boş catch YOK.
- `f0 = (t) => Math.max(12, fr(t))`: ilk 12 kare geçiş, hareket başlamaz.

## 4. Yerleşim (iki sütun)

| Ad | Değer |
|---|---|
| Sütun ortası | `CX = [W*0.255, W*0.745]`, sütun eni `CW = W*0.42` |
| Türkçe satır tabanı | `Y_TR = H*0.262`, boy `BTR = sigdir(iki satır, u(64), CW − u(40))` |
| Kart | üst `Y_KART = H*0.352`, yükseklik `CH = H*0.185`, x = `CX[k] − CW/2`, en `CW` |
| Kart yazısı | boy `BEN = sigdir(iki kart metni, u(64), CW − u(70))`, taban `yb = Y_KART + CH/2 + BEN*0.36`, sütunda ortalı |
| Kart altı ad | taban `Y_AD = H*0.63`, boy `BAD = u(44)` |
| Fark oku | `y = H*0.62` (adlar uçtuktan sonra boş yer) |
| MEANING | taban `Y_ANLAM = H*0.80`, boy `u(110)`, yatay ortalı |

## 5. Ekran metni (senaryo ekran metni sütunu; yalnız bunlar)

- Sol sütun Türkçe: `İstanbul'da yaşı-yor-um.` · sağ: `Amcamla yaşı-yor-um.` (tek `yazi`; *yor* x aralığı önek ölçümüyle:
  `yx0 = x0 + genislik("İstanbul'da yaşı-")`, `yx1 = yx0 + genislik("yor")`).
- Sol kart: `I live in İstanbul.` · sağ kart: `I am living with my uncle.` (`cumle` ile sözcük sözcük).
- Adlar: `SIMPLE PRESENT` (sol kart altı), `PRESENT CONTINUOUS` (sağ kart altı), ortada `vs`.
- `MEANING`.

## 6. Olay listesi (yerel kare = round((t − 3,00) × 30); zaman sozcukler.json'dan, `al()` ile; sayı elle yazılmaz)

| # | Olay | Kare (≈) | Cümle:sözcük (t0) | Uygulama |
|---|---|---|---|---|
| 1 | İki Türkçe satır hazır (sahne 01'den) | 0 | — | `yazi(..., {bas: -10, sure: 4})`, renk mürekkep |
| 2 | 1. satır *yor* kutusu hazır | 0 | — | `ciz` düz bant yx0−u(5)…yx1+u(6), y ≈ Y_TR − BTR*0.28, `w: BTR*0.74`, DOLGU, alfa 0.6, `bas: -30, sure: 10`, tur isaret, ses false |
| 3 | 2. satır *yor* kutusu | 12 | 1:3 yaşıyorum (3,08) | aynı bant, `bas: f0(t)`, sure 8, ses "tik" |
| 4 | Satırlar arasında sarı "=" 1. çizgi | 55 | 1:5 ikisi (4,84) | iki kısa yatay `ciz` (SARI, `w: u(7)`, yarım en u(26), aralık ±u(10)); x = iki satırın arası ortası, y = Y_TR − BTR*0.3 |
| 5 | "=" 2. çizgi | 67 | 1:6 de (5,24) | aynı, alttaki çizgi |
| 6 | Sol kart kutusu | 103 | 2:0 I (6,91) − 14 kare | `kutu(x, Y_KART, CW, CH, {bas: fr(t)−14, sure: 16, w: u(4)})` |
| 7 | Sol kart sözcükleri + karaoke | 117–137 | 2:0–3 I live in Istanbul | `cumle` her sözcük `f: fr(t)`; `altCizgi(kel, {tut: 30})` |
| 8 | bag: sol *yor* → *live* | 168 | 2:4 Biri (8,60) | `ok([yc, Y_TR + BTR*0.2 + u(10)], [live ortası, yb − BEN*0.86 − u(8)], {sure: 16, w: u(6), uzun: u(20), bukum: 0.05})` |
| 9 | SIMPLE | 182 | 2:5 geniş (9,08) | `yazi` BAD, mürekkep, sure 6, ses true, `matris` + `son` (madde 15) |
| 10 | PRESENT (sol) | 192 | 2:6 zaman (9,40) | aynı satırda SIMPLE'ın sağında; iki sözcük birlikte sol sütunda ortalı |
| 11 | Sağ kart kutusu | 217 | 2:7 I (10,69) − 14 | madde 6 gibi |
| 12 | Sağ kart sözcükleri + karaoke | 231–262 | 2:7–12 I am living with my uncle | madde 7 gibi |
| 13 | bag: sağ *yor* → *am living* | 296 | 2:13 Öteki (12,86) | madde 8; hedef x = am.x0 ile living.x1 ortası |
| 14 | PRESENT / CONTINUOUS (sağ) | 315 / 328 | 2:14 şimdiki (13,50) · 2:15 zaman (13,94) | madde 9–10 gibi, sağ sütunda ortalı |
| 15 | `vs` ortada | 385 | 2:18 iki (15,82) | `yazi("vs")` BAD, MÜREKKEP (sarı değil: künyeye geçişte renk aynı kalmalı), x ortası W/2 |
| 16 | Başlık künyeye uçar | 392–410 | 2:19 zamanın (15,98) | `FL0 = fr(t) + 3`, `FL1 = FL0 + 18`, `F_IN = FL1`. Her parça (SIMPLE, PRESENT, vs, PRESENT, CONTINUOUS) kendi künye yerine: hedef x = `KUNYE.kenar + genislik(önek, font(KUNYE.dersYazi))`, önekler `""`, `"SIMPLE "`, `"SIMPLE PRESENT "`, `"SIMPLE PRESENT vs "`, `"SIMPLE PRESENT vs PRESENT "`; hedef taban `KUNYE.ustTaban`. `q = yumus((f−FL0)/(FL1−FL0))`, `sc = lerp(1, KUNYE.dersYazi/BAD, q)`, matris `translate(lerp(x0,tx,q), lerp(Y_AD,ustTaban,q)).scale(sc).translate(−x0, −Y_AD)`. `son: FL1` → FL1'de parçalar gizlenir, künye ders yazısı aynı yerde açılır. `olay(FL1, "tik", 0.4)` |
| 17 | İki uçlu sarı fark oku | 428 | 2:22 farkını (17,26) | `ok([CX[0], H*0.62], [CX[1], H*0.62], {cift: true, sure: 20, w: u(7), uzun: u(24), bukum: 0.03})` |
| 18 | MEANING + sarı belirteç | 483 / 488 | 2:25 anlam (19,26) · 2:26 belirler (19,58) | belirteç: `ciz` düz bant x0−u(14)…x1+u(16), y ≈ Y_ANLAM − B*0.18, `w: B*0.4` (yazının ALT yarısı; iki temada okunur), DOLGU alfa 0.7, `bas: fr(anlam)−5`, `sure: fr(belirler) − fr(anlam) + 5`, tur isaret, ses false; yazı `yazi("MEANING", {bas: fr(anlam), sure: 8, olcek: true, ses: true})` |

Her olaya `not("<ad> (<sözcük>)", kare)` yaz (örnekteki gibi). Kalan 12 kare (517–528) durgun; modül zamanı kendisi dondurur.

## 7. Kurallar

Tek vurgu sarı (RT.vurgu / RT.vurguDolgu) · doğru şık yeşili bu sahnede yok · kırmızı yok (`RT.kirmizi` kullanma) · emoji yok ·
yazı tabanı yatay 30 mantıksal px · sabit px yok (u() / oran) · künye ve açık/koyu tema `ortak/kunye.js` üzerinden (modül yapar;
sahnede tema kodu yok) · sessiz catch yok · `Math.random`/`Date` yok · 2 boşluk girinti, satır ≤ 120 karakter.

## 8. Kabul

`node --check` geçer (şef `.mjs` kopyasıyla dener). Şef koşar:
`cd /home/sef/01dev/_worktrees/kalem-0204 && bash araclar/qa-yerel.sh 02-04-ydt-temel 02-paperjs-kanca 5.8,9.9,14.6,16.9,20.1 14.6 --hazirla`
→ çıkış 0 (yazı × çizim / yazı × künye çakışması yok, ölçüm hatası yok). Kare PNG'lerinde taşma, kesik yazı, üst üste binme yok.
