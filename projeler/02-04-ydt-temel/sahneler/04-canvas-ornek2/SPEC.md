# SPEC — 02-04-ydt-temel sahne 04-canvas-ornek2 (düz canvas) · 14.11

## 1. Görev

- YAZILACAK TEK DOSYA: `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel/sahneler/04-canvas-ornek2/sahne.js`
- Başka dosyaya dokunma. `sahne-ortak.js`, `sayfa.html`, `calistir.sh` hazır, değiştirme. `ortak/` altına yazma.
- Silme yok. Test, render, git, tarayıcı yok. Arka planda süreç yok.
- MAKİNE: Linux x86_64 (srv21). Node `~/.nvm/versions/node/v24.22.2/bin`. Sözdizimi kontrolü: `node --check sahne.js`
  (ES modülü; `--input-type=module` gerekirse onu kullan).

## 2. Örnek (kalıp buradan, içerik buradan DEĞİL)

- `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-03-ydt-temel/sahneler/04-canvas-ornek2/sahne.js` — 88 satır. Dosya
  yapısını birebir izle: başlık yorumu → `import { surucu } from "/ortak/surucu.js"` → `import { Sahne, RT, elips, ok,
  altCizgi, olc } from "./sahne-ortak.js"` → sabitler → `const S = new Sahne({...})` → `async function kur()` → son satır
  `surucu(kur, (f) => S.kare(f), KARE);`.
- Ortak API (bu sahnenin dizinindeki `sahne-ortak.js`, oku): `S.kur()`, `S.sozc` (cümle 4 sözcükleri, `{sozcuk,t0,t1}`,
  küresel sn), `S.koy(e)`, `S.daireSayi(n, cx, cy, tb)`, `S.kart({x,y,w,h,tb,tohum,kutuSure,kutuAralik,satirlar:[]})`,
  `S.cumleYaz({sozcukler,x,y,maxGen,font,satirH,satirSay,bosluk})` → `.kel[i]` (`x,y,w`), `S.cizim({svg,ad,kutu,enCok,
  esik,w,tb,sure,olayEnCok})`, `S.elYazisi({metin,x,y,boy,renk,sozcukler:[{t0,t1}]})`, `S.metinPop({parca,x,y,font,hiza,
  tb,sure,olcek0,ses,turu})`, `S.darbe(pts, o, tb, sure, ses)`, `S.darbeler(liste, o, tb, sure, aralik, ses)`;
  `elips(cx,cy,rx,ry,egim,tohum)`, `ok(a,b,tohum)` → `[govde, uc1, uc2]`, `altCizgi(x0,x1,y,tohum)`, `olc(font, metin)`.
- Renk belirteçleri `RT.murekkep`, `RT.ikincil`, `RT.vurgu` (sarı), `RT.vurguDolgu` (fosfor sarı). Tema (açık/koyu) ve
  künye `ortak/kunye.js` üzerinden `sahne-ortak.js` içinde çözülür; sahne.js hex renk YAZMAZ.

## 3. Sabitler

- `KARE = 762`, `TBAS = 43.85`, `ICERIK = 750`; `new Sahne({ tbas: TBAS, kare: KARE, icerik: ICERIK,
  bolum: "Example 2 / 3", cumle: 4 })`.
- Çizim kökü `/projeler/02-04-ydt-temel/ortak/cizim`; ev = `tabler/home.svg` (fetch ile metin).
- Oran: `const u = (n) => n * S.cv.width / 1920;` Bütün konum, boyut, çizgi kalınlığı ve font px'i `u()` ile yazılır.
  Font yardımcıları: Fredoka 700 (`700 ${u(b)}px Fredoka`), Lexend 500 (`500 ${u(b)}px Lexend`).
- Zaman yalnız sözcükten: `const t = (i) => S.sozc[i].t0;` Elle saniye yazılmaz (yalnız `t(i) ± küçük ofset`).
- `kur()` başında `S.sozc.length !== 49` ise `throw new Error(...)` (sessiz geçiş yok). try/catch yazma.
- Ekran metninde "İstanbul": sol cümle sözcüklerinde `sozcuk === "Istanbul"` olanı `"İstanbul"` yap (kopya nesne).

## 4. Sözcük dizini (cümle 4, 49 sözcük)

0 İkinci · 1 örnek. · 2 Kancadaki · 3 fiil: · 4 live. · 5–11 I live in Istanbul with my family. · 12–14 Ailemle
İstanbul'da yaşıyorum. · 15–17 Orada hep yaşıyorum. · 18 Kalıcı · 19 durum: · 20 geniş · 21 zaman. · 22–34 My parents are
out of town, so I am living with my uncle. (22 My … 30 am, 31 living … 34 uncle.) · 35–41 Ailem şehir dışında, bu yüzden
amcamla yaşıyorum. (37 dışında,) · 42 Bu · 43 yalnız · 44 şimdilik. · 45 Geçici · 46 durum: · 47 şimdiki · 48 zaman.

## 5. Yerleşim (1920 tabanlı mantıksal değerler; hepsi `u()` içinde)

| Öğe | Değer |
|---|---|
| Sol kart | x 110, y 250, w 820, h 410 |
| Sağ kart | x 110+820+60 = 990, y 250, w 820, h 410 |
| Kart iç payı | 40 |
| Cümle | x = kart.x + 40, ilk taban y = 250 + 84, satır aralığı 76, Fredoka 56, maxGen = 820 − 80, bosluk 4 |
| Sol satırlar | `satirSay: [4, 3]` → "I live in İstanbul" / "with my family." |
| Sağ satırlar | `satirSay: [6, 7]` → "My parents are out of town," / "so I am living with my uncle." |
| İkon kutusu | 180×180, kartın sağ alt köşesi: x = kart.x + 820 − 40 − 180, y = 250 + 410 − 40 − 180 |
| Etiket (PERMANENT / TEMPORARY) | `elYazisi`, x = kart.x + 40, taban y = 250 + 410 − 56, boy 64, renk murekkep |
| Daire 2 | `daireSayi(2, u(196), u(176), t(0))` |
| "live" başlık | `metinPop`, x 290, taban y 202, Fredoka 72, murekkep; altında sarı el altçizgisi y + 18 |
| Zaman ekseni y | 800 (iki kartın altında, ayrı ayrı) |
| Sol eksen | x 110+30 → 110+820−20 |
| Sağ eksen | x 990+30 → 990+820−20 |
| now noktası | kartın ortası (sol 520, sağ 1400), elips r 15, çizgi 6, renk murekkep |
| "now" etiketi | `metinPop` Lexend 30, ikincil, `hiza: "orta"`, taban y = 800 + 58 |
| Uzun bant (sol) | 110+60 → 110+820−70, y 800 |
| Kısa bant (sağ) | 1400 − 80 → 1400 + 80, y 800; iki ucunda dikey çizgi y 774 → 826, sarı, kalınlık 6 |

## 6. Çizim kuralları

- Eksen: `ok(a, b, tohum)` yalnız ok başları için; gövde yerine düz `[a, b]`; `S.darbeler([[a,b], uc1, uc2], { duz: true,
  w: u(4), renk: RT.ikincil, uc0: 6, uc1: 12 }, tb, 0.4, 0.15, 0.4)`.
- Bant (fosfor): `S.darbe([[x0,800],[x1,800]], { duz: true, w: u(30), renk: RT.vurguDolgu, alfa: 0.8, uc0: 4, uc1: 8,
  tohum }, tb, sure, 0.5)`. Bant now noktasının ALTINDA kalır: `S.koy` sırası bant → eksen → now noktası → "now" etiketi.
- Odak (sarı el altçizgisi, kalıcı): `S.darbe(altCizgi(A.x − 4, B.x + B.w + 4, A.y + 16, tohum), { w: u(8),
  renk: RT.vurgu, alfa: 0.9, uc0: 8, uc1: 14 }, tb, 0.4, 0.55)`. Halka (elips) KULLANMA (13.11 QA kuralı).
- Bavul: kendi SVG'miz, dosya içinde sabit metin (viewBox 0 0 24 24, fill none, stroke currentColor, stroke-width 2,
  round uç). Yollar: gövde `M6 8a2 2 0 0 1 2 -2h8a2 2 0 0 1 2 2v11a2 2 0 0 1 -2 2h-8a2 2 0 0 1 -2 -2z` · tutamak
  `M10 6v-3h4v3` · kayışlar `M10 9v9`, `M14 9v9` · tekerlekler `M8.5 21v1.8`, `M15.5 21v1.8`. `cizim` çağrısında
  `esik: 0.01` (kısa yollar düşmesin).
- Ev ve bavul: `enCok: 10, w: 4, sure: 1.0, olayEnCok: 4`; `ad: "ev"` / `ad: "bavul"`.

## 7. Olay listesi (yerel kare = round((t − 43,85) × 30); hepsi kare 750'den önce biter)

| # | Olay | Zaman | Kare | Cümle sözcüğü |
|---|---|---|---|---|
| 1 | daire içinde 2 | t(0) = 44,40 | 17 | 0 İkinci |
| 2 | sol kart çerçevesi (`kutuSure 0.2, kutuAralik 0.2`, tohum 4) | t(2) = 45,76 | 57 | 2 Kancadaki |
| 3 | "live" başlık pop (`sure 0.3, olcek0 0.85, ses 0.5, turu "tik"`) | t(4) = 47,20 | 101 | 4 live. |
| 4 | "live" altında sarı altçizgi (0,35 sn) | t(4) + 0,35 | 111 | 4 live. |
| 5 | sol cümle sözcük sözcük (`cumleYaz`, karaoke kendiliğinden) | t(5)…t(11) = 48,09–49,61 | 127–173 | 5–11 |
| 6 | ev çizimi, sol ikon kutusu | t(12) = 50,82 | 209 | 12 Ailemle |
| 7 | sol eksen | t(15) = 52,90 | 272 | 15 Orada |
| 8 | sol now noktası + etiket (+0,15) | t(15) + 0,25 | 279 | 15 Orada |
| 9 | uzun bant (sure 1,0) | t(16) = 53,30 | 284 | 16 hep |
| 10 | PERMANENT (kalem yazar) `sozcukler: [{t0: t(18), t1: t(20)}]` | 54,58–55,54 | 322 | 18 Kalıcı |
| 11 | odak *live* (sol `kel[1]`) | t(20) = 55,54 | 351 | 20 geniş |
| 12 | sağ kart çerçevesi (`kutuSure 0.14, kutuAralik 0.08`, tohum 6) | t(22) − 0,35 = 56,64 | 384 | 22 My |
| 13 | sağ cümle sözcük sözcük | t(22)…t(34) = 56,99–59,95 | 394–483 | 22–34 |
| 14 | bavul çizimi, sağ ikon kutusu | t(37) = 62,28 | 553 | 37 dışında, |
| 15 | sağ eksen | t(42) = 65,00 | 635 | 42 Bu |
| 16 | sağ now noktası + etiket | t(42) + 0,25 | 642 | 42 Bu |
| 17 | kısa bant (sure 0,4) | t(44) = 65,60 | 653 | 44 şimdilik. |
| 18 | kısa bant uç çizgileri (0,18 sn, ikincisi +0,12) | t(44) + 0,4 | 665 | 44 şimdilik. |
| 19 | TEMPORARY `sozcukler: [{t0: t(45), t1: t(47)}]` | 66,84–67,88 | 690 | 45 Geçici |
| 20 | odak *am living* (sağ `kel[8]` → `kel[9]`) | t(47) = 67,88 | 721 | 47 şimdiki |

Sağ cümle `kel` dizini: 0 My 1 parents 2 are 3 out 4 of 5 town, 6 so 7 I 8 am 9 living 10 with 11 my 12 uncle.

## 8. Ekran metni (senaryo-taslak satır 4; bunun dışında yazı yok)

"I live in İstanbul with my family." · "My parents are out of town, so I am living with my uncle." · "PERMANENT" ·
"TEMPORARY" · "live" · "now" (eksen etiketi) · daire içinde "2". Türkçe çeviri YOK. Künye ve "Example 2 / 3" çipini
`sahne-ortak.js` çizer.

## 9. Kurallar

- Tek vurgu rengi sarı (`RT.vurgu` / `RT.vurguDolgu`); kırmızı yok (`RT.kirmizi` kullanma); yeşil yok (doğru şık yok).
- Emoji yok. Hex renk yok. Yazı tabanı en az 30 mantıksal px (en küçük yazı "now" Lexend 30).
- Sabit px yok: her sayısal konum/boyut `u()` içinde (yalnız `uc0/uc1` uç incelme değerleri, `alfa`, `tohum`, süreler hariç).
- Sessiz catch yok; `.catch(() => {})` yazma; hata fırlat.
- `Math.random` ve `Date` yok (zaman yalnız kare numarasından).
- Satır en çok 120 karakter, 2 boşluk girinti, dosya sonunda boş satır.
- Her olayın yanında örnekteki gibi tek satır yorum: `// 50,82 Ailemle: ev`.

## 10. Kabul ölçütü

1. `node --check` geçer; dosya yalnız `sahne.js`; `git status --short` yalnız bu sahne dizinini gösterir.
2. Şef koşar: `cd /home/sef/01dev/_worktrees/kalem-0204 && bash araclar/qa-yerel.sh 02-04-ydt-temel 04-canvas-ornek2
   56.2,63.5,68.6 68.6 --hazirla` → çıkış 0 (çakışma yok, ölçüm hatası yok).
3. Şef PNG'lere bakar: taşma, kesilen yazı, üst üste binme, okunmaz kontrast, boş kare yok.
