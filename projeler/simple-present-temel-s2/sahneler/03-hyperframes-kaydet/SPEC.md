# SPEC — sahne 03 Kaydet (simple-present-temel-s2, huni v2, HyperFrames DİKEY 1080×1920) · 15.11.2026

> DUZ2 (16.11): kart 2. satırı `every day:` + `çoğunlukla` (`#s4`, T(4) `çoğunlukla`); hap T(5) `Simple`; kart sabit = max(T(6) `Present`, hap + 0,30); yer imi T(10) `Kaydet`. Aşağıdaki zaman tablosu 15.11 sesine aittir; güncel değer `zamanlar.json`.

Yazan: şef (istem D-V2 `03-hyperframes-kaydet`). Uygulayan: `agy-filo tek --rol kod`.
Bağlayıcı: `/home/sef/01dev/dijital-anlatim/.claude/docs/huni-v2-standart.md` §1–§3, paket `BRIEF-S2.md` ("Sahne içeriği" 11,87–19,07).

## 1. Yazılacak dosya
- YAZ: `/home/sef/01dev/_worktrees/kalem-0204/projeler/simple-present-temel-s2/sahneler/03-hyperframes-kaydet/uret.py`
- Başka dosyaya dokunma. `yardim.py` (KONU `Simple Present`), `olay.py`, `calistir.sh` hazır (şef kurdu). Test, render, git yok.

## 2. Kalıp (oku, yapıyı al; kodu birebir kopyalama)
Kaynak: `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s1/sahneler/03-hyperframes-cta/uret.py`.
Alınacak yapı:
- `AD`, `sys.path.insert`, `import yardim as Y`, `PAKET = AD.parent.parent`, `SAH` (`zaman.json` → `sahneler[]` içinde
  `klasor == AD.name`), `T_BAS = SAH["t_bas"]` (11,87), `KARE = SAH["kare"]` (228), `SURE = round(KARE / 30, 4)` (7,6).
- `SOZ` = `ortak/anlatim/sozcukler.json` içinde `cumle == 3`.
- `ALT` = `ortak/anlatim/altyazi.json` içinde (`cumle == 3`) VEYA (`cumle == 2` ve `t1 > T_BAS`), dosya sırasıyla.
  (Cümle 2'nin son parçası `gibi.` 11,95'te biter; sahne başında altyazı devam eder.) `assert`: cümle 3'ten 2 parça, cümle 2'den 1 parça.
- `yerel(t)`, `T(i, bas)`, `E(i, bas)` işlevleri ve `BEKLENEN_SOZLER` denetimi (assert) aynı biçimde.
- `uret() -> tuple[str, dict[str, Any]]`: HTML + zamanlar sözlüğü. `__main__`: `proje/` aç, `Y.font_kopyala(proje/assets/fonts)`,
  `proje/index.html` ve `zamanlar.json` yaz, iki satır özet bas (03 ile aynı).
- HTML iskeleti: `Y.font_css()`, `Y.ZEMIN_CSS`, `#sahne` CSS, `#root` öznitelikleri (`data-composition-id="main"`, `data-start="0"`,
  `data-duration=SURE`, `data-fps="30"`, 1080×1920), `Y.zemin_html()`, tek `<svg id="sahne">`, `lib/gsap.min.js`,
  `window.__timelines["main"] = tl`, `gsap.timeline({paused: true})`, `ac()` yardımcısı.
- Altyazı + karaoke: `Y.altyazi_svg(T_BAS, SURE, ALT)` ve 03'teki `V.alt` / `V.karaoke` döngüleri aynen.
  Tek ek: `altyazi_svg`'den dönen karaoke listesinde kapanışı (`k[2]`) ≤ 0 olan satırları AT; açılışı (`k[1]`) < 0 olanı `0.0` yap
  (cümle 2 kuyruğu: yalnız `gibi.` çizgisi kalır). SVG dizgesine dokunma (atılan `<line>` saydam kalır).
- Künye: `Y.kunye_svg()` (argümansız; kanal katmanı `#kanal` + `#logoimg` + konu + rozet içinde gelir). Değiştirme, tween verme.
- ALINMAYACAK: kapak kartı, `ana-kapak` dosya denetimi, `MutationObserver` betiği, `Gerisi`/`bizde`/`hap`/`yt` öğeleri, `clipPath`.

## 3. Sözcük çapaları (cümle 3; `sozcukler.json`)
| i | sözcük | t0 (küresel) | yerel | kare |
|---|---|---|---|---|
| 0 | `Usually,` | 12,42 | 0,55 | 16 |
| 1 | `always,` | 13,70 | 1,83 | 55 |
| 2 | `every` | 14,50 | 2,63 | 79 |
| 4 | `Simple` | 15,54 | 3,67 | 110 |
| 5 | `Present.` | 15,86 | 3,99 | 120 |
| 9 | `Kaydet.` | 18,47 (t1 19,15) | 6,60 | 198 |

`BEKLENEN_SOZLER = [(0,"Usually"), (1,"always"), (2,"every"), (3,"day"), (4,"Simple"), (5,"Present"), (6,"Bu"), (7,"kuralı"),
(8,"kaybetme"), (9,"Kaydet")]`; `assert len(SOZ) == 10`. Zaman her yerde `T(i, bas)`'tan okunur; sabit saniye yazma
(tek istisna: süreler ve `+ 0.10` ofseti).

## 4. Olay listesi
| olay | yerel sn | kare | küresel | sözcük | hareket |
|---|---|---|---|---|---|
| `kart_giris` | yerel(T(0,"Usually")) = 0,55 | 16 | 12,42 | `Usually,` | `#kart` ölçek 0,96 → 1 + opaklık 0 → 1, 0,45 sn, `power3.out`, `svgOrigin "510 730"` |
| `s1_giris` | yerel(T(0)) = 0,55 | 16 | 12,42 | `Usually,` | `#s1` opaklık 0 → 1, y 16 → 0, 0,25 sn, `power3.out` |
| `s2_giris` | yerel(T(1,"always")) = 1,83 | 55 | 13,70 | `always,` | `#s2` aynı (0,25 sn) |
| `s3_giris` | yerel(T(2,"every")) = 2,63 | 79 | 14,50 | `every day:` | `#s3` aynı (0,25 sn) |
| `hap_giris` | yerel(T(4,"Simple")) = 3,67 | 110 | 15,54 | `Simple Present.` | `#satir3` opaklık 0 → 1, ölçek 0,9 → 1, 0,30 sn, `back.out(1.6)`, `svgOrigin` = hap ortası |
| `kart_sabit` | yerel(T(5,"Present")) = 3,99 | 120 | 15,86 | `Present.` | hareket yok; süre = 7,20 − 3,99 = 3,21 |
| `imi_ciz` | yerel(T(9,"Kaydet")) = 6,60 | 198 | 18,47 | `Kaydet.` | `#kaydet-imi` opaklık 1 (set) + `strokeDashoffset` L → 0, 0,30 sn, `sine.inOut` |
| `yazi_giris` | yerel(T(9)) + 0,10 = 6,70 | 201 | 18,57 | `Kaydet.` | `#kaydet-yazi` opaklık 0 → 1, y 12 → 0, 0,25 sn, `power3.out` |
| `kuyruk_durgun` | (KARE − 12) / 30 = 7,20 | 216 | 19,07 | sahne sonu | hareket yok (son 12 kare, geçiş payı) |

Ses olayları (`zamanlar["olaylar"]`, `[yerel_sn, tur, guc]`): `[0,55, "vurus", 0.5]`, `[3,67, "tik", 0.5]`, `[6,60, "cizgi", 0.6]`,
`[6,70, "tik", 0.4]`. Değerler `yerel(T(...))` ile hesaplanır. `olay.py` hepsinin 12 ≤ kare < 216 olduğunu denetler.
`zamanlar` sözlüğü 03 ile aynı şemadır: `fps`, `kare`, `sure`, `t_bas`, her olay için `[yerel_bas, süre]`, `olaylar`, `olay_listesi`
(her satır `olay`, `kare` = round(yerel × 30), `yerel`, `kuresel`, `sozcuk`). JS'e giden `V.Z` yalnız tween'li olayları taşır.

Kart 12,87'den 19,07'ye sabittir: `#kart` grubunda 0,55 + 0,45 sn sonrasında hiçbir tween yok. Kart içindeki son tween (`#satir3`)
3,97'de biter (≤ 3,99 `kart_sabit`; assert). Sahnede çıkış hareketi yok; bütün öğeler sahne sonuna kadar görünür kalır.

## 5. Yerleşim (px; bütün içerik x 60–960, y 460–1380 içinde)
| Öğe | Kimlik | Değer |
|---|---|---|
| Künye + kanal | `#kunye` | `Y.kunye_svg()`; y 291–434; dokunma |
| Kart grubu | `#kart` (`<g>`, `style="opacity:0"`) | aşağıdaki öğeler bu sırayla, DOĞRUDAN `#kart` çocuğu |
| — kâğıt | `#kagit` (`<rect>`) | x 61, y 549, w 898, h 362, rx 22, `fill="#fff9e6"`, `stroke="#c9c2b3"`, `stroke-width="2"` (dış kenar 60–960 × 548–912) |
| — kalem kenarı | `#kart-kenar` (`<path>`) | elle çizilmiş dikdörtgen, §6; `fill="none"`, `stroke="#1b1a17"`, `stroke-width="4.5"`, round cap/join |
| — satır 1a | `#s1` (`<text>`, `style="opacity:0"`) | `Usually,` x BX, taban T1 |
| — satır 1b | `#s2` (`<text>`, `style="opacity:0"`) | `always,` x BX + `Y.genislik("Fredoka", 700, "Usually, ", 72)` (≈ 281,7), taban T1 |
| — satır 2 | `#s3` (`<text>`, `style="opacity:0"`) | `every day:` x BX, taban T2 |
| — satır 3 | `#satir3` (`<g>`, `style="opacity:0"`) | hap `<rect>` x BX, y T3 − 64, w HAP_W, h 92, rx 46, `fill="#f2a93b"` + `<text>` `Simple Present.` x BX + HAP_W/2, `text-anchor="middle"`, taban T3 (şef QA 15.11: hap dışındaki nokta kopuk göründü → nokta hapın içinde) |
| Kaydet grubu | `#kaydet` (`<g>`) | yer imi + `Kaydet` yazısı, yatayda 510'a ortalı, y 960–1060; §7 |
| Altyazı | `#altyazi` | `<g id="altyazi">` + `Y.altyazi_svg(...)` çıktısı, y 1400–1550 |

Kart yazıları: hepsi Fredoka 700 72, `fill="#1b1a17"`, `style` içinde `font-kerning:none` yok (yardim ölçüsü ±1 px yeter).
Ölçüler (Python'da hesapla, sabit yazma):
- `HAP_W = Y.genislik("Fredoka", 700, "Simple Present.", 72) + 56` (≈ 558,2; iç boşluk 28 + 28).
- Satır enleri: `G1 = genislik("Usually, always,")` (≈ 527,8), `G2 = genislik("every day:")` (≈ 345,5),
  `G3 = HAP_W`. `GMAX = max(G1, G2, G3)`.
- Blok sola hizalı satırlar, blok yatayda ortalı: `BX = round(510 - GMAX / 2, 1)` (≈ 230,9).
- Taban: `T1 = 646`, `T2 = T1 + 96` (742), `T3 = T2 + 96` (838); hap y 774–866. Yazı üstü T1 − 52 = 594.
- `assert`: `BX >= 110` ve `BX + GMAX <= 910`; `T1 - 52 >= 564 + 24`; `T3 + 28 <= 896 - 24`; hap üstü (T3 − 64) − (T2 + 17) ≥ 12.
- Hap ölçek ortası: `svgOrigin = f"{BX + HAP_W / 2:.1f} {T3 - 18}"`.

## 6. Kalem kenarı yolu (`#kart-kenar`)
Emsal yöntem (`02-04-ydt-temel-s1/sahneler/08-hyperframes-kaydet/SPEC.md` §6) bu kartın ölçüsüyle:
- Taban dikdörtgen: x 76–944, y 564–896 (kâğıdın 16 px içi).
- Tek alt yol (tek `M`; Chrome kesik desenini her `M`'de baştan başlatır). Biçim: `M` + kenar başına 3 ara noktalı `Q` ya da `L`
  dizisi. Her ara noktaya sabit dizi kaydırması uygula: `KAY = [1.6, -1.2, 2.2, -0.8, 1.0, -2.0, 0.6, 1.8, -1.4, 0.4, -2.2, 1.2]`
  (sırayla, dik yönde, ±2,5 px'i geçmez). Rastgele sayı yok (deterministik).
- Başlangıç sol üst köşeden 10 px sağda (86, 564); saat yönünde dolaşır; bitiş başlangıcı 14 px geçer (sol üstte hafif
  bindirme, el çizimi izi). `Z` yok.
- `assert`: bütün noktalar 74 ≤ x ≤ 946 ve 562 ≤ y ≤ 898.

## 7. Kaydet grubu (`#kaydet`)
- Yer imi yolu (Tabler `bookmark`, MIT; yolu literal yaz, dosyadan okuma; yerel `ortak/cizim/tabler/` içinde yok):
  `M18 7v14l-6 -4l-6 4v-14a4 4 0 0 1 4 -4h4a4 4 0 0 1 4 4z` (24 birimlik kutu; yol x 6–18, y 3–21).
- Ölçü: `YAZI_W = Y.genislik("Fredoka", 700, "Kaydet", 72)` (≈ 233,9); `IKON_EN = 67` (60 + çizgi 7); `ARA = 28`;
  `GRUP_EN = IKON_EN + ARA + YAZI_W`; `GX = 510 - GRUP_EN / 2`; `TX = GX + 3.5 - 30`; `YAZI_X = GX + IKON_EN + ARA`.
- `<g id="kaydet-ikon" transform="translate(TX 951) scale(5)" fill="none" stroke="#f3efe6" stroke-width="1.4"
  stroke-linecap="round" stroke-linejoin="round"><path id="kaydet-imi" d="…" style="opacity:0"/></g>`
  (çizgi 7 px; yol y 966–1056, ortası 1011).
- `<text id="kaydet-yazi" x=YAZI_X y="1036" font-family="Fredoka" font-weight="700" font-size="72" fill="#f3efe6"
  style="opacity:0">Kaydet</text>` (hapsız, mürekkep; büyük harf ortası 1011, ikonla aynı).
- `assert GX >= 60 and GX + GRUP_EN <= 960`.
- JS: `var el = $("#kaydet-imi"), L = el.getTotalLength(); el.style.strokeDasharray = L + " " + (L + 2);
  el.style.strokeDashoffset = L;` sonra `tl.set(el, ac({opacity:1}), Z.imi_ciz[0])` +
  `tl.fromTo(el, {strokeDashoffset: L}, {strokeDashoffset: 0, duration: 0.30, ease: "sine.inOut", immediateRender: false}, Z.imi_ciz[0])`.

## 8. Tema (renk yalnız hex eşlemesiyle; `ortak/hf_tema.py`)
| Yazılan değer | Koyu | Açık |
|---|---|---|
| `fill="#f3efe6"` / `stroke="#f3efe6"` (Kaydet ikon + yazı) | mürekkep `#f3efe6` | `#1b2440` |
| `rect fill="#f2a93b"` (hap) | `#f2a93b` | vurguDolgu `#ffe066` |
| `text fill="#1b1a17"` (kart yazıları, hap yazısı) | `#1b1a17` | pilMetin `#1b2440` |
| `stroke="#c9c2b3"` (kâğıt) | `#c9c2b3` | ikincil `#5a6275` |
| `#kagit` `fill="#fff9e6"` (eşlemesiz) | `#fff9e6` | CSS `.tema-acik #kagit{fill:#fffdf8}` |
| `#kart-kenar` `stroke="#1b1a17"` | CSS `#root #kart-kenar{stroke:var(--pilMetin)}` → `#1b1a17` | `#1b2440` |

CSS'i `<style>` içine `Y.ZEMIN_CSS`'ten sonra yaz. `hf_tema` `[stroke="#1b1a17"]`'yi zemine boyar; `#root #kart-kenar` kuralı
bunu ezer (özgüllük 2,0,0). Sahnenin tek sarısı `Simple Present` hapı (+ ortak karaoke çizgisi); `Kaydet` hapsız.

## 9. Kurallar
1. `uret.py` metninde `#root.tema-acik` dizgesi OLMAZ (hf_tema onu "çevrildi" sayar, açık tema koyu çıkar). `.tema-acik #id` yaz.
2. Yasak söz listesini koda literal yazma (dış `grep` taramasını kirletir). Ekranda yalnız §5 ve §7 metinleri var.
3. `rz1` kimliği kullanma. Emoji, QR, düğme taklidi, gradyan, gölge yok.
4. 0. sn'de açık öğe yok (GSAP `seek(0)` 0'daki `set`'i uygulamaz): bütün içerik öğeleri `style="opacity:0"` ile başlar.
5. Bütün tween'lerde `immediateRender: false` (03'teki `ac()` yardımcısı).
6. Son 12 karede (yerel ≥ 7,20) tween yok: `assert` yazı girişi bitişi `6.70 + 0.25 <= 7.20` (değerler hesaptan).
7. Satır ≤ 24 karakter (`assert len(satır) <= 24`); yazı tabanı ≥ 64 (künye, kanal, altyazı hariç).
8. Bütün içerik öğeleri y 460–1380 ve x 60–960 içinde (assert: kart 548–912, kaydet 960–1060).
9. Python: tip ipuçları zorunlu; girinti 4 boşluk (03 ile aynı); satır ≤ 120.

## 10. Kabul ölçütü (agy koşmaz; şef koşar)
- `ONIZLE_YALNIZ=1 bash calistir.sh --tema acik` → `önizleme hazır`, `zamanlar.json` 4 ses olayı, `olaylar.json` 4 satır.
- `araclar/qa-yerel.sh simple-present-temel-s2 03-hyperframes-kaydet 11.95,15.45,19.00 19.00 --hazirla` → çıkış 0.
- `araclar/cakisma-kapisi.mjs … --sahne 03-hyperframes-kaydet` → çıkış 0, 0 uyarı.
- Karede: 11,95 kanal + künye + cümle 2 kuyruk altyazısı (kart 12,42'de girer); 15,45 kart + `Usually, always,` / `every day:` + altyazı;
  19,00 + `Simple Present.` hapı + yer imi + `Kaydet`.
