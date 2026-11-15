# SPEC — sahne 08 Kaydet (02-04-ydt-temel-s2, huni v2, HyperFrames DİKEY 1080×1920) · 15.11.2026

Yazan: şef (istem D-S2-V2, `uretim-tutanagi/istem/sahne-v2/D-08-hyperframes-kaydet.md` ile aynı içerik). Uygulayan: `agy-filo tek --rol kod`.
Bağlayıcı: `/home/sef/01dev/dijital-anlatim/.claude/docs/huni-v2-standart.md` §1–§3; paket `BRIEF-S2.md` ("Yerleşim", "Sahne içeriği" 17,41–22,75).
Ses (öğretmen, cümle 3): "Bu, üç farktan yalnız biri. Bu kuralı kaybetme. Kaydet."

## 1. Yazılacak dosya
- YAZ: `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s2/sahneler/08-hyperframes-kaydet/uret.py`
- Başka dosyaya dokunma. `yardim.py`, `olay.py`, `calistir.sh`, `cizim/bookmark.svg` hazır (şef yazdı). Test, render, git yok.

## 2. Kalıp (oku, yapıyı al; içeriği bu SPEC'ten al)
Örnek: `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s1/sahneler/08-hyperframes-kaydet/uret.py` (aynı motor, aynı tür sahne).
Alınacak yapı (aynen):
- `AD`, `sys.path.insert`, `import yardim as Y`, `PAKET`, `SAH` (`zaman.json` → `sahneler[]` içinde `klasor == AD.name`),
  `T_BAS = float(SAH["t_bas"])` (17,41), `KARE = int(SAH["kare"])` (172), `SURE = round(KARE / 30, 4)` (5,7333).
- `SOZ` = `ortak/anlatim/sozcukler.json` içinde `cumle == 3`; `ALT` = `ortak/anlatim/altyazi.json` içinde `cumle == 3`.
- `yerel(t)`, `T(i, bas)`, `E(i, bas)` işlevleri; `BEKLENEN_SOZLER` denetimi (assert).
- `uret() -> tuple[str, dict[str, Any]]` ve `__main__` bloğu (proje/ aç, `Y.font_kopyala`, `index.html` + `zamanlar.json` yaz, 2 satır özet).
- HTML iskeleti: `Y.font_css()`, `Y.ZEMIN_CSS`, `#root` (`data-composition-id="main"`, `data-start="0"`, `data-duration=SURE`,
  `data-fps="30"`, `data-width="1080"`, `data-height="1920"`), `Y.zemin_html()`, tek `<svg id="sahne" ...>`, `lib/gsap.min.js`,
  `window.__timelines["main"] = tl`.
- Altyazı + karaoke: `alt_svg, alt_zaman, karaoke_zaman = Y.altyazi_svg(T_BAS, SURE, ALT)`; JS'te örnekteki `V.alt` ve
  `V.karaoke` döngüleri AYNEN. Künye: `Y.kunye_svg()` (argümansız; `#kunye` içinde `#kanal` + `#logoimg` + konu + rozet). Değiştirme.
- ALINMAYACAK (örnekte var, burada yok): `#uc` üst yazısı, `#kagit` dolgulu kâğıt, `kart_kenar_yolu()`, `Kaydet` hapı (`#kaydet-hap`).

## 3. Sözcük çapaları (cümle 3; `sozcukler.json`)
`BEKLENEN_SOZLER = [(0,"Bu"), (1,"üç"), (2,"farktan"), (3,"yalnız"), (4,"biri"), (5,"Bu"), (6,"kuralı"), (7,"kaybetme"), (8,"Kaydet")]`;
`assert len(SOZ) == 9`; `assert len(ALT) == 2`. Zaman her yerde `T(i, bas)`'tan okunur; sabit saniye yazma.

| i | sözcük | t0 küresel | yerel | kare |
|---|---|---|---|---|
| 0 | `Bu,` | 17,96 | 0,55 | 16 |
| 1 | `üç` | 18,52 | 1,11 | 33 |
| 6 | `kuralı` | 20,47 | 3,06 | 92 |
| 8 | `Kaydet.` | 22,15 | 4,74 | 142 |

## 4. Olay listesi
| olay | yerel sn | kare | küresel | sözcük | hareket |
|---|---|---|---|---|---|
| `kart_giris` | yerel(T(0,"Bu")) = 0,55 | 16 | 17,96 | `Bu,` | `#kart` opaklık 0 → 1 ve ölçek 0,96 → 1, 0,40 sn, `power3.out`, `svgOrigin "510 780"` (örnekteki gibi iki ayrı `fromTo`) |
| `nokta_giris` | yerel(T(1,"üç")) = 1,11 | 33 | 18,52 | `üç` | `#nokta0`, `#nokta1`, `#nokta2` opaklık 0 → 1, y 12 → 0, 0,30 sn, `power3.out`, aralık 0,08 sn (0,1,2 sırası) |
| `imi_ciz` | yerel(T(6,"kuralı")) = 3,06 | 92 | 20,47 | `kuralı` | `#imi-cizgi` opaklık 1 (set) + `strokeDashoffset` L → 0, 0,50 sn, `sine.inOut` |
| `kaydet_giris` | yerel(T(8,"Kaydet")) = 4,74 | 142 | 22,15 | `Kaydet.` | aynı anda, hepsi 0,30 sn: `#kaydet-yazi` opaklık 0 → 1 + y 24 → 0 (`power3.out`); `#imi-dolgu` opaklık 0 → 1 (`power2.out`); `#today-kutu` ve `#today-yazi` opaklık 1 → 0; `#today-cerceve` ve `#today-yazi2` opaklık 0 → 1 (`power2.out`) |
| `kuyruk_durgun` | 5,3333 (= (KARE − 12) / 30) | 160 | 22,74 | geçiş | hareket yok (son 12 kare geçiş payı) |

Ses olayları (`zamanlar["olaylar"]`, `[yerel_sn, tur, guc]`): `[0,55,"vurus",0.5]`, `[1,11,"tik",0.4]`, `[3,06,"cizgi",0.6]`,
`[4,74,"tik",0.6]`. Değerler `yerel(T(...))` ile hesaplanır. `olay.py` hepsinin 12 ≤ kare < 160 olduğunu denetler.
`zamanlar` sözlüğü örnekle aynı şemadır: `fps`, `kare`, `sure`, `t_bas`, her olay için `[yerel_bas, süre]` (`nokta_giris` süresi
0,46 = 0,30 + 2 × 0,08), `olaylar`, `olay_listesi` (satır başına `olay`, `kare` = round(yerel × 30), `yerel`, `kuresel`, `sozcuk`).
JS'e giden `V.Z` yalnız olay zamanlarını taşır (örnekteki gibi).

Kart 18,36'dan (0,55 + 0,40 sonrası) sahne sonuna SABİTTİR: `#kart`, `#kart-crv`, `#s1`, `#s2`, `#s3` üzerinde 0,95 sn sonrasında tween yok.
Tek istisna `kaydet_giris` anındaki Today hapı dönüşümü (istem gereği). Sahnede çıkış hareketi yok; bütün öğeler sahne sonuna kadar kalır.

## 5. Yerleşim (px; bütün içerik x 60–960, y 460–1380 içinde)
Kart tasarımı paketteki Hikâye A kartıyla aynı dildir (dolgusuz, mürekkep çerçeve, köşe 32; bkz.
`/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s2/sahneler/04-hyperframes-hikaye/uret.py` `kart_svg()`).

| Öğe | Kimlik | Değer |
|---|---|---|
| Künye + kanal | `#kunye` | `Y.kunye_svg()`; dokunma |
| Kart grubu | `#kart` (`<g style="opacity:0">`) | aşağıdaki öğeler bu sırayla |
| — çerçeve | `#kart-crv` (`<rect>`) | x 62, y 562, w 896, h 436, rx 32, `fill="none"`, `stroke="#f3efe6"`, `stroke-width="4"` (dış kenar 60–960 × 560–1000) |
| — Today hapı | `#today-hap` (`<g>`) | içinde sırayla `#today-kutu`, `#today-cerceve`, `#today-yazi`, `#today-yazi2` |
| —— kutu | `#today-kutu` (`<rect>`) | x 102, y B1 − 64, w HW, h 88, rx 44, `fill="#f2a93b"` |
| —— çerçeve | `#today-cerceve` (`<rect>`) | kutu ile aynı geometri, `fill="none"`, `stroke="#f3efe6"`, `stroke-width="3"`, `style="opacity:0"` |
| —— yazı | `#today-yazi` (`<text>`) | `Today`, Fredoka 700 72, x 124, taban B1, `fill="#1b1a17"` |
| —— yazı 2 | `#today-yazi2` (`<text>`) | `Today`, aynı konum ve boy, `fill="#f3efe6"`, `style="opacity:0"` |
| — satır 1 devamı | `#s1` | `iki zamanda`, Fredoka 700 72, x S1X, taban B1, `fill="#f3efe6"` |
| — satır 2 | `#s2` | `da geçebilir;`, Fredoka 700 72, x 124, taban B2, `fill="#f3efe6"` |
| — satır 3 | `#s3` | `farkı anlam yapar.`, Fredoka 700 72, x 124, taban B3, `fill="#f3efe6"` |
| Noktalar | `#noktalar` (`<g>`) | `#nokta0` dolu daire cx 115, cy 1040, r 13, `fill="#f3efe6"`; `#nokta1` cx 159 ve `#nokta2` cx 203: halka, cy 1040, r 11, `fill="none"`, `stroke="#f3efe6"`, `stroke-width="4"`; üçü `style="opacity:0"` |
| Yer imi grubu | `#yerimi` (`<g transform="translate(IX IY) scale(S)">`) | içinde sırayla `#imi-dolgu`, `#imi-cizgi` (dolgu altta, çizgi üstte) |
| — dolgu | `#imi-dolgu` (`<path>`) | d = YERIMI_D, `fill="#f2a93b"`, `stroke="none"`, `style="opacity:0"` |
| — çizgi | `#imi-cizgi` (`<path>`) | d = YERIMI_D, `fill="none"`, `stroke="#f3efe6"`, `stroke-width` = round(6 / S, 4), `stroke-linecap="round"`, `stroke-linejoin="round"`, `style="opacity:0"` |
| Kaydet yazısı | `#kaydet-yazi` (`<text>`) | `Kaydet`, Fredoka 700 96, x KX, taban 1224, `fill="#f3efe6"`, `style="opacity:0"` |
| Altyazı | `#altyazi` | `<g id="altyazi">` + `Y.altyazi_svg(...)` çıktısı (y 1400–1550) |

Ölçüler (uret.py içinde hesapla, sabit yazma):
- `HW = Y.genislik("Fredoka", 700, "Today", 72) + 44` (≈ 251,7). `S1X = 102 + HW + 20` (≈ 373,7).
- `B1 = 703`, `B2 = 803`, `B3 = 903` (satır aralığı 100; blok kartın ortası y 780'e ortalı).
- `YERIMI_D` = `cizim/bookmark.svg` dosyasından oku: `re.findall(r'<path d="([^"]+)"', metin)` ilk eleman
  (dosyadaki `M0 0h24v24H0z` yolu `stroke` özniteliğiyle başlar, eşleşmez). `assert YERIMI_D.startswith("M18 7v14")`.
  Yol 24 birimlik kutuda x 6–18, y 3–21.
- `S = 140 / 18` (yer imi yüksekliği 140). `IX = 102 - 6 * S` (görünür sol kenar x 102), `IY = 1120 - 3 * S` (üst y 1120, alt 1260).
- Yer imi sağ kenarı `IR = 102 + 12 * S` (≈ 195,3). `KX = round(IR + 3 + 36, 1)` (≈ 234,3). Kaydet sağ ucu
  `KX + Y.genislik("Fredoka", 700, "Kaydet", 96)` ≈ 546.

JS (yer imi çizgisi, örnekteki `#kaydet-imi` kalıbı): `var el = $("#imi-cizgi"), L = el.getTotalLength();
el.style.strokeDasharray = L + " " + (L + 2); el.style.strokeDashoffset = L;` sonra
`tl.set(el, ac({opacity:1}), Z.imi_ciz[0])` + `tl.fromTo(el, {strokeDashoffset: L}, {strokeDashoffset: 0, duration: 0.50,
ease: "sine.inOut", immediateRender: false}, Z.imi_ciz[0])`.

## 6. Tema (renk yalnız hex eşlemesiyle; `ortak/hf_tema.py` CSS'i sonradan ekler)
| Yazılan değer | Koyu | Açık |
|---|---|---|
| `fill="#f3efe6"` / `stroke="#f3efe6"` | mürekkep `#f3efe6` | `#1b2440` |
| `rect fill="#f2a93b"` (`#today-kutu`) | `#f2a93b` | vurguDolgu `#ffe066` |
| `text fill="#1b1a17"` (`#today-yazi`) | `#1b1a17` | pilMetin `#1b2440` |
| `#imi-dolgu` `fill="#f2a93b"` (path) | CSS `#root #imi-dolgu{fill:var(--vurguDolgu,#f2a93b)}` → `#f2a93b` | `#ffe066` |

CSS'i `<style>` içine `Y.ZEMIN_CSS`'ten sonra yaz: `#sahne{position:absolute;left:0;top:0;}` ve yukarıdaki `#imi-dolgu` kuralı.
(hf_tema'nın `#root [fill="#f2a93b"]` kuralı path'i `--vurgu`'ya (`#d9900f`) boyar; `#root #imi-dolgu` özgüllüğü onu ezer.)
Tek sarı kuralı: `kaydet_giris`'ten önce tek sarı `#today-kutu`; sonra tek sarı `#imi-dolgu`. Karaoke çizgisi ortak altyazı öğesidir.
`stroke="#1b1a17"` YAZMA (hf_tema onu zemine boyar).

## 7. Kurallar
1. `uret.py` metninde `#root.tema-acik` dizgesi OLMAZ (hf_tema onu "çevrildi" sayar, açık tema koyu çıkar).
2. Ekranda yalnız §5 metinleri var. Yasaklı söz listesini koda literal YAZMA (dış grep taramasını kirletir).
3. `rz1` kimliği kullanma. Emoji, QR, oynat/izle düğmesi taklidi, gradyan, gölge, kırmızı yok.
4. 0. sn'de içerik öğesi görünmez: içerik grupları `style="opacity:0"` ile başlar (GSAP `seek(0)` 0'daki `set`'i uygulamaz).
5. Bütün tween'lerde `immediateRender: false` (örnekteki `ac()` yardımcısı).
6. Son 12 karede (yerel ≥ 5,3333) tween yok: `assert yerel(T(8)) + 0.30 <= (KARE - 12) / 30`.
7. Satır ≤ 24 karakter (`assert len(satır) <= 24`: `Today iki zamanda`, `da geçebilir;`, `farkı anlam yapar.`, `Kaydet`).
   İçerik yazı boyu ≥ 64 (72 ve 96; künye, kanal, altyazı istisna).
8. Sınır denetimi (assert): `102 + HW + 20 + Y.genislik("Fredoka",700,"iki zamanda",72) <= 920`;
   `124 + Y.genislik("Fredoka",700,"farkı anlam yapar.",72) <= 920`; `KX + genişlik(Kaydet 96) <= 960`; `B1 - 64 >= 562 + 16`;
   `B3 + 20 <= 998 - 16`; yer imi 1120–1260 ve Kaydet tabanı 1224 < 1380.
9. Python: tip ipuçları zorunlu; girinti 4 boşluk; satır ≤ 120; `from __future__ import annotations`.
10. Ekran metni sesten önce gelmez: `Kaydet` yazısı `kaydet_giris`'ten önce görünmez.

## 8. Kabul ölçütü (agy koşmaz; şef koşar)
- `ONIZLE_YALNIZ=1 bash calistir.sh --tema acik` → `önizleme hazır`; `zamanlar.json` 4 ses olayı; `olaylar.json` 4 satır.
- `araclar/qa-yerel.sh 02-04-ydt-temel-s2 08-hyperframes-kaydet 17.41,20.1,22.7 22.7 --hazirla` → çıkış 0.
- `node araclar/cakisma-kapisi.mjs 02-04-ydt-temel-s2 --sahne 08-hyperframes-kaydet --port 41333 --sunucu 41022` → 0 uyarı.
- Karede: 17,41 yalnız kanal + künye; 20,1 kart + 3 nokta + altyazı (yer imi yok); 22,7 + yer imi sarı dolgulu + `Kaydet`,
  Today hapı mürekkep çerçeveli.
