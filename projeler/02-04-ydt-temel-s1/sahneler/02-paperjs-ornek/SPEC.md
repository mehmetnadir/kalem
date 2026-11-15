# SPEC v2 — 02-04-ydt-temel-s1 · sahne 02-paperjs-ornek · huni v2 (15.11)

Şef tasarımı. İki dosya, iki ayrı agy koşusu; her koşu YALNIZ kendi dosyasını yazar:
- A: `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s1/ortak/kunye.js` (§A)
- B: `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s1/sahneler/02-paperjs-ornek/sahne-02.js` (§B)

Başka dosyaya dokunma. Silme yok. Test, render, git yok. `kalem-paper.js`, `sayfa.html`, `calistir.sh`, `bavul.svg` DEĞİŞMEZ.
Bağlayıcı kaynak: `/home/sef/01dev/dijital-anlatim/.claude/docs/huni-v2-standart.md` §2 ve `../../BRIEF-S1.md` "Kanal katmanı" tablosu.
v1 tasarım (olay sırası, API): `/home/sef/Silinecekler/2026-11-15-huni-v2/02-04-ydt-temel-s1/sahneler/02-paperjs-ornek/SPEC.md`.
Değişen yalnız yerleşim + kanal katmanı. İçerik, olay sırası, zamanlama v1 ile aynı.

## Bantlar (1080×1920, huni v2 §2)

```
   0–280   boş (zemin; çip YOK)
 291–339   kanal: logo x 53,2 (görünür 60) + @ydspublishing x 263, taban 330
 360–450   künye: konu (Fredoka 700, x 60, taban 420) + rozet hapı 386–434
 460–1380  içerik, x 60–960
1400–1550  altyazı, en çok 2 satır, x 60–960 (orta 510)
1570–1920  boş
sağ 960–1080 boş (platform düğmeleri)
```

---

## §A — `ortak/kunye.js` v2 (var olan dosya düzenlenir; mutlak yol yukarıda)

Var olan kod: aynı dosya. Korunan (DEĞİŞMEZ): `KOK`, `TEMALAR`, `RENK`, `__kalemKutu` kancası (satır 14–41), `RT`, `renkCoz`,
`temaAdi`, `temaSurum`, `temaSec`, tema `try` satırı, `GEN`, `YUK`, `FONTLAR`, `kunyeHazirla`, `grenUret`, `zeminCiz`,
`zeminKaroAl`, `vinyetAl`, `altyaziMetin`, `altyaziSar`. Dışa aktarılan adlar korunur (`kalem-paper.js` şunları içe aktarır:
`kunyeHazirla, zeminCiz, kunyeCiz, altyaziMetin, altyaziCiz, RENK, RT, renkCoz, temaSurum, KOK, KUNYE`).

1. **Baş yorum.** İlk satır tam olarak: `// huni v2 (15.11): kanal katmanı + v2 bantları`. Altındaki eski "DİKEY sürüm 2",
   "02-04 (15.11) ders adı 2 satır", "çip" anlatan satırlar v2'ye göre kısaltılır (kullanım satırı:
   `kunyeCiz(ctx, { logo: K.logo })` → kanal + künye; `altyaziCiz(ctx, altyaziMetin(K.altyazi, t))`). S1-C kopya notu kalır.
2. **Bant yorumu** (eski "HUD 0–320 · içerik 352–1392 …" satırları) → yukarıdaki bant çizimi tek satır özetle.
3. **`KANAL` sabiti** (yeni, `export const`), BRIEF-S1 tablosundan birebir:
   `logoX 53.2 · logoY 291 · logoH 48 · logoW 193.5 · yazi "@ydspublishing" · yaziFont "700 42px Lexend" · yaziX 263 ·
   yaziTaban 330 · gorunurX 60 · kutuY 291 · kutuH 50`. Başka değer yazma.
4. **`kanalCiz(ctx, K)`** (yeni, `export function`). `K` = `logo` alanı olan nesne (`kunyeHazirla` dönüşü ya da `{ logo }`).
   - `ctx.save()`; `globalAlpha = 1` (kanal hep tam opak; alfa parametresi YOK); `textAlign "left"`, `textBaseline "alphabetic"`.
   - `K.logo` varsa `ctx.drawImage(K.logo, logoX, logoY, logoW, logoH)`.
   - Yazı: `ctx.font = yaziFont`, `fillStyle = RENK.murekkep`, `fillText(yazi, yaziX, yaziTaban)`. Genişliği `measureText` ile al.
   - `ctx.restore()`.
   - Kanca: `window.__kalemKutu` varsa tek kutu `ekle("kunye", "kunye:kanal", gorunurX, kutuY, yaziX + yaziGen − gorunurX, kutuH)`.
5. **`KUNYE` sabiti** (eskisinin yerine; çip, ders, ajanda, cipler, hud alanları KALKAR):
   `kenar 60 · sag 960 · icerikBas 460 · icerikSon 1380 · altyaziBas 1400 · altyaziSon 1550 · altyaziYazi 44 · altyaziSatir 56 ·
   konu "Simple Present vs Present Continuous" · konuX 60 · konuTaban 420 · konuAzami 34 · konuAsgari 28 ·
   rozet "YDT · BASIC" · rozetY 386 · rozetH 48 · rozetYazi 26 · rozetAra 20 · rozetPay 20`.
6. **`konuDuzen(ctx)`** (yeni, iç işlev; eski `dersDuzen`'in yerine). `boy` 34'ten 28'e 1'er azalır:
   `kw` = `700 ${boy}px Fredoka` ile konu genişliği; `rw` = `700 26px Lexend` ile rozet genişliği + 2 × `rozetPay`;
   `konuX + kw + rozetAra + rw <= sag` ilk sağlanan boyda dur. Dönüş `{ boy, kw, rx: konuX + kw + rozetAra, rw }`.
   28'de de sığmazsa `throw new Error("künye: konu + rozet 960'a sığmıyor")` (sessiz geçiş yok). Ölçülen değer: 34 px'te
   konu ≈ 581 px, rozet ≈ 162 + 40 → sağ uç ≈ 863; beklenen boy 34.
7. **`kunyeCiz(ctx, { logo, alfa = 1 })`** yeniden yazılır. `bolum` gelirse YOK SAYILIR (çip v2'de kapalı; çizim ve kutu yok).
   - Önce `kanalCiz(ctx, { logo })` (alfadan bağımsız, her karede).
   - Sonra `save`, `globalAlpha = alfa`; `D = konuDuzen(ctx)`; konu: `700 ${D.boy}px Fredoka`, `RENK.murekkep`, sol hiza,
     `fillText(konu, konuX, konuTaban)`.
   - Rozet hapı: `fillStyle RENK.vurguDolgu`, `roundRect(D.rx, rozetY, D.rw, rozetH, rozetH / 2)` dolgu; yazı `700 26px Lexend`,
     `RENK.pilMetin`, `textAlign "center"`, `fillText(rozet, D.rx + D.rw / 2, rozetY + rozetH / 2 + 9)`. `restore`.
   - Kanca (alfa ≥ 0,2 ve `__kalemKutu` varsa): `ekle("kunye", "kunye:konu", konuX, konuTaban − D.boy, D.kw, D.boy + 8)`,
     `ekle("kunye", "kunye:rozet", D.rx, rozetY, D.rw, rozetH)`. Eski `kunye:logo`, `kunye:ders`, `kunye:sag-ust` kutuları KALKAR.
8. **`altyaziCiz`**: genişlik `KUNYE.sag − KUNYE.kenar` (900), yatay orta `(KUNYE.kenar + KUNYE.sag) / 2` (510; eski `W / 2`).
   Boy döngüsü 44 → 40 → 36 kalır. En çok 2 satır: 3 satır dalı (`satirlar.length > 3` birleştirme, `adim 44`, `y0 … 40`) KALKAR;
   36 px'te de 2 satırı aşarsa `throw new Error("altyazı 2 satıra sığmıyor: " + metin)`. `y0` = `altyaziBas + 84` (1 satır) ya da
   `altyaziBas + 56` (2 satır); satır adımı `altyaziSatir`.
9. **`altyaziDilimle`**: `genislik` = `KUNYE.sag − KUNYE.kenar` (eski `W − 2 * KUNYE.kenar`). Başka değişiklik yok.
10. `const W = 1080, H = 1920` kalır (zemin ve vinyet tam tuval).

Kurallar: 2 boşluk girinti, satır ≤ 120 karakter, `try/catch` ekleme (var olan iki `fetch` catch'i ve tema `try` satırı kalır),
`Math.random`/`Date` yok, ham renk kodu yalnız `TEMALAR` içinde.

---

## §B — `sahneler/02-paperjs-ornek/sahne-02.js` v2 (var olan dosya düzenlenir)

Var olan kod: aynı dosya (v1, 578 satır). Yapı, import, `al()` bekçisi, `pen`, `satir`, 24 olay, `not()` kayıtları, `UST`
öğesi ve çip öğe sırası AYNEN kalır. Değişen yalnız aşağıdakiler.

1. **Baş yorum** 3. satıra ek: `// huni v2 (15.11): yerleşim x 60–960, y 460–1380; çip yok; kanal katmanı kunye.js'te.`
2. **`sahneKur` çağrısı**: `bolum` alanı kalkar → `sahneKur(P, { KARE, tBas: T_BAS })` (`KUNYE.cipler` v2'de yok; kalırsa hata).
3. **Ölçü sabitleri** (satır 78–102 bloğu) şu değerlere geçer; türetilenler formülle yazılır (çıplak sayı dağıtma):

| Sabit | v1 | v2 | Formül / not |
|---|---|---|---|
| `KENAR` | 48 | 60 | `KUNYE.kenar` |
| `SAG` | `W − KENAR` | 960 | `KUNYE.sag` (yeni kaynak) |
| `SOL` | 72 | 84 | `KENAR + 24` |
| `KX`, `KW` | 48, 984 | 70, 880 | `KENAR + KUTU_PAY`, `SAG − KENAR − 2 · KUTU_PAY`; `KUTU_PAY` 10 (şef düzeltmesi, kare turu 1: kutu köşe taşması x 52–967 → 60–960) |
| `IC` | 88 | 110 | `KX + 40` |
| `Y_L1`, `Y_L2` | 470, 590 | 560, 680 | sahne 01 uçuş sonu (D-01 istemi); sabit sayı |
| `YC1` | 430 | 540 | sabit sayı; çip 1 hedef tabanı |
| `KY1` | 460 | 570 | `YC1 + 30` |
| `KH1` | 220 | 196 | sabit; iç pay küçüldü |
| `AXY1` | 740 | 816 | `KY1 + KH1 + 50` |
| `YC2` | 905 | 936 | `AXY1 + 120` |
| `KY2` | 935 | 966 | `YC2 + 30` |
| `KH2` | 300 | 272 | sabit; iç pay küçüldü |
| `AXY2` | 1290 | 1288 | `KY2 + KH2 + 50` |
| `BTR, BEN, BTR2, BET, BNOW, IKON, ALT` | — | aynı | 80, 64, 72, 72, 64, 100, 0.30 (yazı boyu DEĞİŞMEZ) |

   Türetilen konumlar:
   - `yb1 = KY1 + 80` (650; v1 +88) · `yTr1 = KY1 + 166` (736; v1 +182).
   - `yb2 = KY2 + 78` (1044; v1 +88) · kart 2 `cumle` `aralik: 80` (v1 85; satır 2 = 1124) · `yTr2 = KY2 + 242` (1208; v1 +267).
   - `yEtiket = AXY + 24`, `yNow = AXY + 76` (aynı formül). `AX1 = SAG − 24` (936; v1 `W − KENAR − 24`).
   - `AX0`, `NX`, `ikonX = KX + KW − 40 − IKON` (810) formülleri aynı (yeni değerlerle).
   Beklenen değerler (fontkit ölçümü): kart 1 cümlesi 110–577 · kart 2 satır 1 110–402, satır 2 110–525 · TR satır 1 84–754 ·
   `AX0` ≈ 481, `NX` ≈ 708 · çip 1 hedef x ≈ 290, çip 2 ≈ 368 · içerik dikey 468–1366.
4. **Bekçiler** (v1 beşi kalır, `SAG` artık 960; `throw new Error`):
   - TR satırı sağ ucu > `SAG` · kart 1 cümlesi sağ ucu > `ikonX − 20` · kart 2 satır sağ uçları > `SAG − 40` · `AX0 > NX − 120` ·
     `AXY2 + 76 > KUNYE.icerikSon` (1380).
   - YENİ: `Math.min(YC1, Y_L1) − BTR * 0.9 < KUNYE.icerikBas` (çip / TR satırı yazı kutusu üstü 460'ın altında kalmalı;
     Paper yazı kutusu üstü = taban − 0,9 × boy).
   - YENİ: `SAG > KUNYE.sag` ya da `KX + KW > KUNYE.sag` (içerik sağ sınırı 960).
5. Olaylar, zamanlar, renk belirteçleri, `oge`/`kay`, `metinOge*.g.data`, `GK0 = G0 + 6`, `G1 = GK0 + 15`, `son: [G0, G0 + 8]`
   v1 ile aynı. Olay kodu yalnız yukarıdaki sabitler üzerinden yeni konuma gider.

Kurallar (v1 §7 aynen): tek vurgu sarı, yeşil ve kırmızı yok, emoji yok, içerik yazısı ≥ 64 px, satır ≤ 24 karakter, tema kodu
yok, `try/catch` yok, `Math.random`/`Date` yok, 2 boşluk girinti, satır ≤ 120 karakter, "kanal"/"dakika"/"tam ders" sözü,
QR, süre metni yok. Ekranda `İstanbul.` (noktalı İ).

## Olay listesi (v1 ile aynı; yerel kare = round((t − 3,00) × 30), sözcük `ortak/anlatim/sozcukler.json`)

| # | Olay | Kare | Cümle:sözcük (küresel sn) | v2 konum |
|---|---|---|---|---|
| 1 | İki TR satırı hazır (sahne 01'den) | 0 | — | x 84, taban 560 / 680 |
| 2 | Karaoke: satır 2 `yaşı-yor-um.` | 12 | 1:3 yaşıyorum. (3,08) | taban 680 |
| 3 | ek_ayir satır 1 *yor* kutusu | 29 | 1:4 Türkçede (3,96) | x ≈ 551–636, y 560 |
| 4 | ek_ayir satır 2 *yor* kutusu | 86 | 1:7 yaşıyorum. (5,56) + 9 | x ≈ 482–567, y 680 |
| 5 | TR parçaları solar · çipler kayar | 156–177 | 2:2 ayrılır. (8,19) | çip 1 → (≈290, 540), çip 2 → (≈368, 936) |
| 6–7 | Kart 1 kutusu + `I live in İstanbul.` | 172 / 182–199 | 2:3–6 (9,08–9,64) | kutu 70–950 × 570–766, taban 650 |
| 8–10 | odak *live* · bag 1 · ev | 190 / 194 / 199 | 2:4–6 | ev 810–910 × 584–684 |
| 11 | `Hep orada.` (soluk) | 245–279 | 2:7–8 (11,17–12,29) | taban 736 |
| 12–15 | `PERMANENT` · eksen 1 · now · uzun bant | 281 / 293 / 301–305 / 308 | 2:9–11 (12,37–13,25) | eksen y 816, x 481–936 |
| 16–17 | Kart 2 kutusu + `I am living` / `with my uncle.` | 341 / 351–382 | 2:13–18 (14,70–15,74) | kutu 70–950 × 966–1238, taban 1044 / 1124 |
| 18–20 | odak *am living* · bag 2 · bavul | 361 / 370 / 382 | 2:15–18 | bavul 810–910 × 980–1080 |
| 21 | `Şimdilik.` (soluk) | 391–420 | 2:19 (17,03–17,99) | taban 1208 |
| 22–24 | `TEMPORARY` · eksen 2 · now · kısa bant + çentik | 422 / 434–446 / 451–460 | 2:20–22 (18,07–19,03) | eksen y 1288, now taban 1364 |

## Kabul

`node --check` (şef `.mjs` kopyasıyla) · `bash araclar/qa-yerel.sh 02-04-ydt-temel-s1 02-paperjs-ornek 3.05,11.50,19.90 11.50 --hazirla`
çıkış 0 · `node araclar/cakisma-kapisi.mjs 02-04-ydt-temel-s1 --sahne 02-paperjs-ornek --port 41333 --sunucu 41022` çıkış 0, 0 uyarı ·
karelerde kanal katmanı (logo 53,2–246,7 × 291–339, yazı x 263, taban 330) her karede; 0–280, 1570–1920 ve x 960–1080 boş.
