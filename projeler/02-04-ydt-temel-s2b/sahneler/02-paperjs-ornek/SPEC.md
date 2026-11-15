# SPEC v2 (huni v2) — 02-04-ydt-temel-s2 · sahne 02-paperjs-ornek (Paper.js, dikey 1080×1920) · 15.11

Şef tasarımı. Uygulayıcı (agy) YALNIZ şu dosyayı yazar:
`/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s2/sahneler/02-paperjs-ornek/sahne-02.js`

Başka dosyaya dokunma. Silme yok. Test, render, git yok. Aynı dizindeki `kalem-paper.js`, `sayfa.html`, `calistir.sh`,
`nesneler.json` HAZIR (şef yazdı); değiştirme. Bağlayıcı standart: `/home/sef/01dev/dijital-anlatim/.claude/docs/huni-v2-standart.md` §1–§2.

## 0. Yöntem: v1 dosyasını yerinde uyarla

Hedef dosya şu an v1 sürümüdür (yedek: `/home/sef/Silinecekler/2026-11-15-huni-v2/02-04-ydt-temel-s2/sahneler/02-paperjs-ornek/sahne-02.js`).
İçerik ve olaylar AYNI kalır; değişen yalnız yerleşim, kanal katmanı + künye ve aşağıdaki maddeler.

KORU (aynen): `EN2` dizisi ve üstündeki 4 satırlık kaynak yorumu · `MONT`, `TISORT` · `noktasiz`, `al` bekçisi ·
`eyGen` · `elCizim`, `kar`, `nokta`, `nabiz` · `yalin`, `kapat` · `kel1`/`kel2` + `altCizgi` · today halkası (süper elips,
`halkaNoktalari`, sarı + mürekkep ikizi, tohum 4242) · `MEANING` hapı (`dinamik` dolgu + yazı) · bütün olay blokları, sıraları,
çapaları, süreleri ve `not()` çağrıları · `f0` geçiş payı.

DEĞİŞTİR:
1. Dosya başı yorumu (3–4 satır): sahne, 449 kare, t_bas 2.84, huni v2 yerleşimi (kanal katmanı + künye sahnede çizilir).
2. Import: `import { sahneKur, RT, renkCoz } from "/projeler/02-04-ydt-temel-s2/sahneler/02-paperjs-ornek/kalem-paper.js";`
   (KUNYE kullanılmaz). `yaziNoktalari` importu kalır.
3. `sahneKur` çağrısı: `sahneKur(P, { KARE, tBas: T_BAS, kunye: (ctx, K) => kanalCiz(ctx, K) })`. `bolum` YOK (çip yok).
   `kanalCiz` aynı `kur` içinde `function` bildirimi olarak tanımlanır (§5); her karede `kalem-paper.js` çağırır.
4. Ölçü sabitleri bloğu §3 tablosuyla DEĞİŞİR (`KENAR`, `KUNYE.kenar`, `KUNYE.icerikSon` kullanımı kalkar).
5. `RIGHT NOW` artık `Present Continuous`'un ALTINDA, sağda, zaman çizgisi 2'nin hemen üstünde (§4, §6 olay 18).
6. today halkası → `RIGHT NOW` okunun hedefi ve bükümü (§6 olay 20).
7. Bekçiler §8 ile değişir.

## 1. kalem-paper.js API (bu dizindeki kopya)

v1 ile aynı; tek fark: `sahneKur(P, {KARE, tBas, kunye})` — `kunye(ctx, K)` ZORUNLU (yoksa `throw`). Modül her karede
`zeminCiz` → Paper tuvali → `kunye(oc, K)` → altyazı sırasıyla çizer; `ortak/kunye.js` `kunyeCiz` (v1 HUD) ÇAĞRILMAZ.
`K.logo` tema logosudur (açık `yds-publishing-lacivert.svg`, koyu `yds-publishing-seffaf.svg`; `Image`, yüklü).
Kare başında `window.__kalemKutu.kare = []` sıfırlanır; `kunye` içindeki `ekle` çağrıları her karede yeniden yazılır.
S'den kullanılanlar v1 ile aynı: `fr, not, olay, ciz, ok, kutu, yazi, elYazisi, cumle, altCizgi, dinamik, oge, genislik, kis,
cikis, sozcukler, P`. Renk yalnız belirteçle (`RT.murekkep`, `RT.ikincil`, `RT.vurgu`, `RT.vurguDolgu`, `RT.pilMetin`) ve
canvas'ta `renkCoz(RT.x)` ile HER karede çözülür (tema değişimi). Ham renk kodu YOK.

## 2. Zaman çapaları (v1 ile aynı)

`s2 = S.sozcukler(2)`, `al()` ile: 0 She (3,39) · 3 coat (4,27) · 4 in (4,47) · 6 winter. (4,67) · 7 Genel (5,56) ·
8 durum: (6,04) · 9 geniş (6,68) · 10 zaman. (7,00) · 11 Today (11,42) · 17 anlam (14,14) · 19 Konuşma (15,25; t1 15,73) ·
20 anı: (15,81) · 21 şimdiki (16,49) · 22 zaman. (16,89). Kart 2 = `EN2` sabit dizisi (8,37 … 10,13; BRIEF-S2 DİKKAT notu).

## 3. Ölçü (huni v2 §2; her sayı adlı sabit)

| Sabit | Değer | Not |
|---|---|---|
| `W` | 1080 | |
| `SOL` | 60 | soru satırı, `Simple Present`, `Present Continuous`, eksen başı, konu, kanal |
| `SAG` | 960 | içerik sağ sınırı (960–1080 platform arayüzü) |
| `ICERIK_UST`, `ICERIK_ALT` | 460, 1380 | içerik bandı |
| `KX`, `KW` | 68, 884 | kart kutusu; `kutu()` köşeleri ±8 taşar → çizgi 60–960 |
| `IC` | `KX + 40` (108) | kart iç yazı x |
| `F_EN`, `BEN`, `ARA`, `ALT` | `"700 64px Fredoka"`, 64, 80, 0.32 | kart cümleleri, satır aralığı, altçizgi payı |
| `BSORU`, `Y_SORU` | 72, 530 | soru satırı Caveat 700 72, taban 530 (sahne 01 son karesi ile aynı) |
| `KY1`, `KH1` | 576, 192 | kart 1 (alt 768); `yb1 = KY1 + 76` (652), satır 2 `yb1 + ARA` (732) |
| `BET` | 64 | `GENERAL`, `RIGHT NOW` Caveat el yazısı |
| `F_INCE`, `BINCE` | `"500 64px Lexend"`, 64 | `Simple Present`, `Present Continuous` |
| `Y_ETA` | `KY1 + KH1 + 68` (836) | satır A tabanı: `Simple Present` (sol) + `GENERAL` (sağ) aynı satırda |
| `AXY1` | `Y_ETA + 54` (890) | zaman çizgisi 1 |
| `BNOW`, `NOW_DY` | 64, 54 | `now` Caveat 64, taban `AXY + NOW_DY` |
| `KY2`, `KH2` | `AXY1 + 70` (960), 210 | kart 2 (alt 1170); `yb2 = KY2 + 96` (1056; üstte hap payı), satır 2 1136 |
| `Y_ETB` | `KY2 + KH2 + 66` (1236) | `Present Continuous` tabanı (sol, tek başına) |
| `Y_RN` | `Y_ETB + 64` (1300) | `RIGHT NOW` tabanı (sağ, ikinci satır) |
| `AXY2` | `Y_RN + 16` (1316) | zaman çizgisi 2; `now` 2 tabanı 1370 |
| `AX0`, `AX1` | `SOL` (60), `SAG − 24` (936) | eksen uçları; sağda ok ucu |
| `NX` | `round(AX0 + 0.45 · (AX1 − AX0))` (454) | iki çizgide aynı now x'i |
| `BW`, `BP` | 100, 200 | kış bandı eni, adımı (v1 110/230; dar bantta 4 bant için) |
| `TB` | 120 | today bandı yarı eni |
| `BANT_W`, `BANT_A` | 28, 0.35 | bant kalınlığı, alfası (`RT.ikincil`) |
| `IKON` | 100 | giysi kutusu; `IKX = KX + KW − 32 − IKON` (820) |
| `HAP_H`, `HAP_P` | 80, 34 | `MEANING` hapı |

Türetilen:
- Mont kutusu `[IKX, KY1 + KH1 − 14 − IKON, IKON, IKON]`; tişört kutusu `[IKX, KY2 + KH2 − 14 − IKON, IKON, IKON]`.
- Kış bandı merkezleri: `k = −3 … 2` için `c = NX + BP · (k + 0.5)`; yalnız `c − BW/2 ≥ AX0 + 8` ve `c + BW/2 ≤ AX1 − 40`
  (→ 154, 354, 554, 754: 4 bant; now 454 iki bant arasında).
- `GENERAL` sağa hizalı: `xGeneral = SAG − 12 − eyGen("GENERAL", BET)`.
- `RIGHT NOW` sağda ama eksen ok ucundan önce biter: `xRightNow = AX1 − 48 − eyGen("RIGHT NOW", BET)` (≈ 602; mürekkep sağ ucu
  ≈ 898, ok ucu 910'da başlar).
- Hap: `HAP_W = genislik("MEANING", F_EN) + 2 · HAP_P`; `hx0 = SAG − 24 − HAP_W`; `hcx = hx0 + HAP_W / 2`; dikey merkez `KY2`.
- `eyKutu(str, boyut)` (yeni, kısa): `yaziNoktalari(str, EY.G, {upm, asc, boy: boyut, x: 0, taban: 0})` darbelerinin `pts`
  noktalarından `{ust: min y − maxGen/2, alt: max y + maxGen/2, sol, sag}` (taban 0'a göre). Yalnız bekçide kullanılır.

## 4. Yerleşim (tek sütun, x 60–960; y 460–1380)

```
 280–350  kanal katmanı: [logo] @ydspublishing            (§5; her karede, alfa 1)
 360–450  künye: Simple Present vs Present Continuous [YDT · BASIC]   (§5)
 ~476–552 Genel mi, şu an mı?   (Caveat 700 72, x 60, taban 530; kare 0'dan hazır; 14,14'te altçizgi)
 576–768  KART 1: She wears her coat / in the winter.      (Fredoka 64; mont sağ alt köşe)
 ~790–855 Simple Present (Lexend 500 64, x 60) ………… GENERAL (Caveat 64, sağa hizalı)
 876–904  zaman çizgisi 1: eksen + ok · 4 kış bandı (gri) + kar tanesi · now noktası bantlar arasında
 ~917–944 now
 920–1000 [MEANING] sarı hap — kart 2 üst çizgisinin sağ ucunda (x 585–936)
 960–1170 KART 2: She is wearing her / pink T-shirt today.  (tişört sağ alt köşe; today halkası)
 ~1190–1236 Present Continuous (Lexend 500 64, x 60)
 ~1256–1300            RIGHT NOW (Caveat 64, x ≈ 602)  ← today halkasından ince mürekkep ok
 1290–1342 zaman çizgisi 2: eksen + ok · today bandı (gri) + 2 uç çentiği · now noktası bandın içinde, nabız
 ~1343–1370 now
 1380 ─ içerik sonu · 1400–1536 altyazı (modül çizer) · 1570–1920 boş
```
Neden iki satır: x 60–960 bandında `Present Continuous` (611 px) + `RIGHT NOW` (≈ 296 px) + 32 aralık sığmaz (999 > 960).
`Simple Present` (469) + `GENERAL` (≈ 239) sığar; satır A v1 gibi tek satır kalır.

**Kare 0 devri:** soru satırı `yazi("Genel mi, şu an mı?", {x: SOL, y: Y_SORU, boyut: BSORU, aile: "Caveat", agirlik: 700,
renk: RT.murekkep, bas: -30, sure: 4, ses: false})` → kare 0'da tam (sahne 01 son karesi: Caveat 72, x 60, taban 530).

## 5. Kanal katmanı + künye — `kanalCiz(ctx, K)` (canvas 2D, her kare, animasyon YOK)

Değerler bütün sahnelerde AYNI piksel (BRIEF-S2 "Yerleşim" tablosu; S1 ile aynı). Sabitler:
`KONU = "Simple Present vs Present Continuous"`, `ROZET = "YDT · BASIC"`, `ROZET_P = 20` (hap yatay iç payı), `ROZET_ARA = 20`.

`kur` içinde bir kez (sahneKur'dan sonra, fontlar yüklü) ölç: `rozetW = genislik(ROZET, "700 26px Lexend") + 2 · ROZET_P`;
`KONU_BOY` = 34'ten 28'e inerek `SOL + genislik(KONU, "700 <boy>px Fredoka") + ROZET_ARA + rozetW ≤ SAG` olan İLK boy
(28'de de sığmazsa `throw`); `konuW` = o boydaki genişlik; `rozetX = SOL + konuW + ROZET_ARA`;
`kanalW = genislik("@ydspublishing", "700 42px Lexend")`.

`function kanalCiz(ctx, K)` sırası (`ctx.save()` … `ctx.restore()`; `globalAlpha = 1`, `textBaseline = "alphabetic"`):
1. Logo: `ctx.drawImage(K.logo, 53.2, 291, 193.5, 48)`.
2. `@ydspublishing`: `font "700 42px Lexend"`, `fillStyle renkCoz(RT.murekkep)`, `textAlign "left"`, `fillText(…, 263, 330)`.
3. Konu: `font "700 <KONU_BOY>px Fredoka"`, mürekkep, `fillText(KONU, SOL, 420)`.
4. Rozet hapı: `fillStyle renkCoz(RT.vurguDolgu)`, `beginPath(); roundRect(rozetX, 386, rozetW, 48, 24); fill()`; yazı
   `font "700 26px Lexend"`, `fillStyle renkCoz(RT.pilMetin)`, `textAlign "center"`, `fillText(ROZET, rozetX + rozetW / 2, 419)`.
5. Kanca (çakışma kapısı; `ortak/kunye.js` satır 166–196 kalıbı), `window.__kalemKutu` varsa:
   `ekle("kunye", "kunye:kanal", 60, 291, 263 + kanalW − 60, 52)` ·
   `ekle("kunye", "kunye:konu", SOL, 420 − round(0.8 · KONU_BOY), konuW, KONU_BOY)` ·
   `ekle("kunye", "kunye:rozet", rozetX, 386, rozetW, 48)`.
Çip (sağ üst `Example`) YOK. v1 HUD değerleri (logo y 48, ders adı y 212, rozet y 216, çip y 48) YOK.

## 6. Olay listesi (kare = `fr(t)` = round((t − 2,84) × 30); t küresel sn; ilk 12 kare geçiş: `f0`)

| # | Olay | t · kare | Çapa | Not (v1'den fark) |
|---|---|---|---|---|
| 1 | Soru satırı hazır | — · 0 | — | §4 kare 0 devri |
| 2 | Kart 1 kutusu | 3,06 → 12 | She − 10, `f0` | `kutu(KX, KY1, KW, KH1, {…v1})` |
| 3 | Kart 1 sözcükleri + karaoke | 3,39–4,67 · 17–55 | s2[0..6] | `cumle(…, {x: IC, y: yb1, …, aralik: ARA})`, `altCizgi(kel1, {tut: 0, alt: ALT})` |
| 4 | Mont kalemle | 4,27 · 43 | coat | mont kutusu §3 |
| 5 | `odak` *in the winter* (sarı) | 4,47 · 49 | in | v1 aynı; `odak1` 8,37'de söner |
| 6 | `GENERAL` | 5,56 · 82 | Genel → durum: | x `xGeneral`, y `Y_ETA` |
| 7 | Zaman çizgisi 1: eksen + ok ucu | 6,04 · 96 / 107 | durum: | `AXY1`, `AX0`–`AX1` |
| 8 | now noktası 1 / `now` | 104 / 108 | durum: + 8 / + 12 | `y: AXY1 + NOW_DY` |
| 9 | `Simple Present` | 6,68 · 115 | geniş | x `SOL`, y `Y_ETA` |
| 10 | 4 kış bandı + kar tanesi | 7,00 · 125–143 | zaman. | yeni `BW`/`BP` |
| 11 | odak 1 söner | 8,37 · 166–174 | EN2 She | v1 aynı |
| 12 | Kart 2 kutusu | 8,04 · 156 | EN2 She − 10 | `kutu(KX, KY2, KW, KH2, …)` |
| 13 | Kart 2 sözcükleri + karaoke | 8,37–10,13 · 166–219 | EN2 | `y: yb2`; `altCizgi(kel2, {tut: 12, alt: ALT})` |
| 14 | Tişört kalemle | 9,65 · 204 | EN2 T-shirt | tişört kutusu §3 |
| 15 | `odak` *today* (sarı) | 10,13 · 219 | EN2 today. | v1 aynı; 11,42'de söner |
| 16 | today halkası (sarı) | 11,42 · 257 | Today | v1 aynı (süper elips, ikiz) |
| 17 | `MEANING` hapı + soru altçizgisi; halka mürekkebe döner | 14,14 · 339 / 341 | anlam | altçizgi `[[SOL − 4, Y_SORU + 22], [SOL + w + 4, Y_SORU + 20]]`, `w = genislik("Genel mi, şu an mı?", "700 72px Caveat")` |
| 18 | `RIGHT NOW` | 15,25–15,94 · 372–395 | Konuşma → anı: | x `xRightNow`, y `Y_RN` (sözcük pencereleri v1 aynı) |
| 19 | Zaman çizgisi 2: eksen + ok ucu | 15,38 · 376 / 385 | Konuşma + 4 | `AXY2` |
| 20 | halka → `RIGHT NOW` oku | 15,73 · 387 | Konuşma.t1 | `ok([HR + 2, (HT + HB) / 2], [RN.x0 + RN.w · 0.4, Y_RN − BET · 0.84], {bas, sure: 10, w: 4.5, renk: RT.murekkep, alfa: 0.9, uzun: 16, bukum: 0.18, yon: [0.3, -1], ad: "bag today"})` |
| 21 | now 2 + nabız / `now` | 15,81 · 389 / 392 / 395 | anı: | `y: AXY2 + NOW_DY` |
| 22 | `Present Continuous` | 16,49 · 410 | şimdiki | x `SOL`, y `Y_ETB` |
| 23 | today bandı + 2 uç çentiği | 16,62 · 414 / 418 / 421 | şimdiki + 4 | `AXY2` |

Son hareket ≈ kare 426 (< 436, modül 436'da zamanı dondurur). Ok yolu: halkanın sağından (≈ 653, 1114) sağ-aşağı,
`Present Continuous` sağ ucunun (671) ≈ 50 px sağından geçer, `RIGHT NOW`'un üstüne ≈ 10 px boşlukla iner; tişörte (x ≥ 820) değmez.

## 7. Tek sarı kuralı (S2-duzeltme madde 2)

Aynı anda en çok bir sarı öğe: karaoke 1 → odak *in the winter* → karaoke 2 → odak *today* → today halkası → `MEANING` hapı.
Bantlar, eksenler, kar, now noktası, ok, soru altçizgisi sarı DEĞİL. Künye rozet hapı künye öğesidir (vurgu sayılmaz).
YASAK: `Simple Present` etiketine ok, kart 1'e herhangi bir bağ, ikinci ok.

## 8. Bekçiler (`throw new Error(...)`, sessiz geçiş yok)

- Kart: `KX − 8 < SOL` ya da `KX + KW + 8 > SAG`; satır 1'ler `x1 > SAG − 40`; satır 2'ler `x1 > IKX − 16`; halka `HR > IKX − 12`.
- Satır A: `SOL + genislik("Simple Present", F_INCE) + 32 > xGeneral`; `xGeneral + eyGen("GENERAL", BET) + 12 > SAG`.
- `RIGHT NOW`: `xRightNow + eyGen("RIGHT NOW", BET) + 12 > AX1 − 26` (ok ucuna değer) · `Y_RN + eyKutu("RIGHT NOW", BET).ust <
  Y_ETB + 0.3 · BINCE − 4` (`Present Continuous` yazı kutusuyla dikey kesişim; kapı Paper metin kutusunu taban + 0,3 boy sayar).
- Hap: alt kenarı (`KY2 + HAP_H / 2`) > kart 2 satır 1 yazı üstü (`yb2 − BEN · 0.72`) VE x aralıkları kesişiyorsa.
- Kış bandı sayısı < 3; `NX` bir kış bandının içinde; today bandı eksen dışında.
- İçerik bandı: `Y_SORU − 0.75 · BSORU < ICERIK_UST`; `AXY2 + NOW_DY + 4 > ICERIK_ALT`; soru satırı sağ ucu > `SAG`.
- Künye: `KONU_BOY` bulunamadı (28'de sığmıyor).

## 9. Kurallar

Tek vurgu sarı (§7) · yeşil yok · kırmızı yok · emoji yok · içerik yazısı ≥ 64 px (kanal katmanı 42 ve künye ≤ 34/26 hariç) ·
satır ≤ 24 karakter · ekranda `T-shirt` tireli · tema kodu yok (renk her karede `renkCoz`) · sessiz catch yok, try/catch yok ·
`Math.random` / `Date` yok · 2 boşluk girinti, satır ≤ 120 karakter · ekranda ve kodda süre sözü, QR, oynat/izle düğmesi YOK ·
her bölüm `// --- <t> <sözcük>: <olay>` yorumuyla · dosya başı 3–4 satır yorum.

## 10. Kabul

`node --check` geçer (şef `.mjs` kopyasıyla dener). Şef koşar:
`cd /home/sef/01dev/_worktrees/kalem-0204 && bash araclar/qa-yerel.sh 02-04-ydt-temel-s2 02-paperjs-ornek 2.84,10.1,17.35 14.9 --hazirla`
→ çıkış 0; `node araclar/cakisma-kapisi.mjs 02-04-ydt-temel-s2 --sahne 02-paperjs-ornek --port 41333 --sunucu 41022` → 0 uyarı.
Karelerde: kanal katmanı üç karede aynı yerde; 0–280 ve 1570–1920 boş; içerik x 960 sağına geçmez; altyazı bandına içerik girmez;
taşma, kesik yazı, üst üste binme yok; aynı anda en çok bir sarı öğe.
