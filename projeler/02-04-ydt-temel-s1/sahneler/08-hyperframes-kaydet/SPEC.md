# SPEC — sahne 08 Kaydet (02-04-ydt-temel-s1, huni v2, HyperFrames DİKEY 1080×1920) · 15.11.2026

Yazan: şef (istem `uretim-tutanagi/istem/sahne-v2/D-08-hyperframes-kaydet.md`). Uygulayan: `agy-filo tek --rol kod`.
Bağlayıcı: `/home/sef/01dev/dijital-anlatim/.claude/docs/huni-v2-standart.md` §1–§3, paket `BRIEF-S1.md`.

## 1. Yazılacak dosya
- YAZ: `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s1/sahneler/08-hyperframes-kaydet/uret.py`
- Başka dosyaya dokunma. `yardim.py`, `olay.py`, `calistir.sh` hazır (şef yazdı).

## 2. Kalıp (oku, yapıyı al; kodu birebir kopyalama)
Kaynak: `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s1/sahneler/03-hyperframes-cta/uret.py`.
Alınacak yapı:
- `AD`, `sys.path.insert`, `import yardim as Y`, `PAKET`, `SAH` (`zaman.json` → `sahneler[]` içinde `klasor == AD.name`),
  `T_BAS = SAH["t_bas"]` (19,99), `KARE = SAH["kare"]` (177), `SURE = round(KARE / 30, 4)` (5,9).
- `SOZ` = `ortak/anlatim/sozcukler.json` içinde `cumle == 3`; `ALT` = `ortak/anlatim/altyazi.json` içinde `cumle == 3`.
- `yerel(t)`, `T(i, bas)`, `E(i, bas)` işlevleri ve `BEKLENEN_SOZLER` denetimi (assert) aynı biçimde.
- `uret() -> tuple[str, dict]`: HTML + zamanlar sözlüğü. `__main__`: `proje/` aç, `Y.font_kopyala(proje/assets/fonts)`,
  `proje/index.html` ve `zamanlar.json` yaz, iki satır özet bas.
- HTML iskeleti: `Y.font_css()`, `Y.ZEMIN_CSS`, `#root` öznitelikleri (`data-composition-id="main"`, `data-duration=SURE`,
  `data-fps="30"`, 1080×1920), `Y.zemin_html()`, tek `<svg id="sahne">`, `lib/gsap.min.js`, `window.__timelines["main"]`.
- Altyazı + karaoke: `Y.altyazi_svg(T_BAS, SURE, ALT)` ve 03'teki `V.alt` / `V.karaoke` döngüleri aynen.
- Künye: `Y.kunye_svg()` (argümansız; kanal katmanı `#kanal` + `#logoimg` + konu + rozet içinde gelir). Değiştirme.
- ALINMAYACAK: kapak kartı, `ana-kapak` dosya denetimi, `MutationObserver` betiği, `Gerisi`/`hap`/`YouTube` öğeleri.

## 3. Sözcük çapaları (cümle 3; `sozcukler.json`)
| i | sözcük | t0 (küresel) | yerel | kare |
|---|---|---|---|---|
| 0 | `Bu,` | 20,54 | 0,55 | 16 |
| 1 | `üç` | 21,02 | 1,03 | 31 |
| 4 | `biri.` | 22,14 | 2,15 | 64 |
| 5 | `Sınavdan` | 22,77 | 2,78 | 83 |
| 8 | `olacak.` | 23,97 | 3,98 | 119 |
| 9 | `Kaydet.` | 24,89 (t1 25,57) | 4,90 | 147 |

`BEKLENEN_SOZLER = [(0,"Bu"), (1,"üç"), (2,"farktan"), (3,"yalnız"), (4,"biri"), (5,"Sınavdan"), (6,"önce"), (7,"lazım"),
(8,"olacak"), (9,"Kaydet")]`; `assert len(SOZ) == 10`; `assert len(ALT) == 2`. Zaman her yerde `T(i, bas)`'tan okunur; sabit saniye yazma.

## 4. Olay listesi
| olay | yerel sn | kare | küresel | sözcük | hareket |
|---|---|---|---|---|---|
| `kart_giris` | yerel(T(0,"Bu")) = 0,55 | 16 | 20,54 | `Bu,` | `#kart` ölçek 0,96 → 1 + opaklık 0 → 1, 0,45 sn, `power3.out`, `svgOrigin "510 790"` |
| `uc_giris` | yerel(T(1,"üç")) = 1,03 | 31 | 21,02 | `üç` | `#uc` opaklık 0 → 1, y 16 → 0, 0,30 sn, `power3.out` |
| `imi_ciz` | yerel(T(9,"Kaydet")) = 4,90 | 147 | 24,89 | `Kaydet.` | `#kaydet-imi` opaklık 1 (set) + `strokeDashoffset` L → 0, 0,30 sn, `sine.inOut` |
| `hap_giris` | yerel(T(9)) + 0,10 = 5,00 | 150 | 24,99 | `Kaydet.` | `#kaydet-hap` opaklık 0 → 1, ölçek 0,9 → 1, 0,30 sn, `back.out(1.6)`, `svgOrigin` = hap ortası |
| `kuyruk_durgun` | 5,50 | 165 | 25,49 | sahne sonu | hareket yok (son 12 kare durgun) |

Ses olayları (`zamanlar["olaylar"]`, `[yerel_sn, tur, guc]`): `[0,55, "vurus", 0.5]`, `[4,90, "cizgi", 0.6]`, `[5,00, "tik", 0.5]`.
Değerler `yerel(T(...))` ile hesaplanır. `olay.py` hepsinin 12 ≤ kare < 165 olduğunu denetler.
`zamanlar` sözlüğü 03 ile aynı şemadır: `fps`, `kare`, `sure`, `t_bas`, her olay için `[yerel_bas, süre]`, `olaylar`, `olay_listesi`
(her satır `olay`, `kare` = round(yerel × 30), `yerel`, `kuresel`, `sozcuk`).

Kart 21,00'den 25,49'a sabittir: `#kart` üzerinde 0,55 + 0,45 sn sonrasında hiçbir tween yok. Sahnede çıkış hareketi yok.
`#uc` sahne sonuna kadar görünür kalır.

## 5. Yerleşim (px; bütün öğeler x 60–960 içinde)
| Öğe | Kimlik | Değer |
|---|---|---|
| Künye + kanal | `#kunye` | `Y.kunye_svg()`; y 291–434; dokunma |
| Üst yazı | `#uc` (`<text>`) | `üç farktan biri`, Lexend 700, 48 px, x 60, taban y 528, `fill="#f3efe6"` + `fill-opacity="0.7"`, `style="opacity:0"` |
| Kart grubu | `#kart` (`<g>`, `style="opacity:0"`) | aşağıdaki 3 öğe bu sırayla, DOĞRUDAN `#kart` çocuğu (ara `<g>` yok) |
| — kâğıt | `#kagit` (`<rect>`) | x 61, y 601, w 898, h 378, rx 22, `fill="#fff9e6"`, `stroke="#c9c2b3"`, `stroke-width="2"` (dış kenar 60–960 × 600–980) |
| — kalem kenarı | `#kart-kenar` (`<path>`) | elle çizilmiş dikdörtgen, §6; `fill="none"`, `stroke="#1b1a17"`, `stroke-width="4.5"`, round cap/join |
| — kural satırı 0 (DUZ2 15.11) | `#kural0` (`<text>`) | `Live, work fiillerinde:` Fredoka 700, boy B (76 → 64; 3 satır), x 110, taban T0 = T1 − A |
| — kural satırı 1 | `#kural1` (`<text>`) | `kalıcıysa geniş zaman,` Fredoka 700, boy B, x 110, taban T1, `fill="#1b1a17"` |
| — kural satırı 2 | `#kural2` (`<text>`) | `geçiciyse şimdiki zaman.` Fredoka 700, boy B, x 110, taban T2, `fill="#1b1a17"` |
| Kaydet grubu | `#kaydet` (`<g>`) | yer imi + sarı hap, yatayda 510'a ortalı, y 1020–1140; §7 |
| Altyazı | `#altyazi` | `Y.altyazi_svg(...)` çıktısı, y 1400–1550 |

Kural satırı ölçüsü: B = 80'den 64'e inerek, iki satırın `Y.genislik("Fredoka", 700, satır, B)` en büyüğü ≤ 800 olan ilk boy
(beklenen 73). `assert B >= 64`. Satır aralığı `A = round(1.32 * B)`; `T1 = round(790 - A / 2 + 0.32 * B)`; `T2 = T1 + A`
(B 73 → A 96, T1 765, T2 861). Satır sonu `110 + genişlik ≤ 910` (assert).

## 6. Kalem kenarı yolu (`#kart-kenar`)
- Taban dikdörtgen: x 76–944, y 616–964 (kâğıdın 16 px içi).
- Tek alt yol (tek `M`; Chrome kesik desenini her `M`'de baştan başlatır). Biçim: `M` + kenar başına 3 ara noktalı `Q` ya da `L`
  dizisi. Her ara noktaya sabit dizi kaydırması uygula: `KAY = [1.6, -1.2, 2.2, -0.8, 1.0, -2.0, 0.6, 1.8, -1.4, 0.4, -2.2, 1.2]`
  (sırayla, dik yönde, ±2,5 px'i geçmez). Rastgele sayı yok (deterministik).
- Başlangıç sol üst köşeden 10 px sağda (86, 616); saat yönünde dolaşır; bitiş başlangıcı 14 px geçer (sol üstte hafif
  bindirme, el çizimi izi). `Z` yok.
- `assert`: bütün noktalar 74 ≤ x ≤ 946 ve 614 ≤ y ≤ 966 (kâğıdın içinde, yazıdan uzak).

## 7. Kaydet grubu (`#kaydet`)
- Yer imi yolu (Tabler `bookmark`, MIT; yolu literal yaz, dosyadan okuma):
  `M18 7v14l-6 -4l-6 4v-14a4 4 0 0 1 4 -4h4a4 4 0 0 1 4 4z` (24 birimlik kutu; yol x 6–18, y 3–21).
- `<g id="kaydet-ikon" transform="translate(TX 1020) scale(5)" fill="none" stroke="#f3efe6" stroke-width="1.4"
  stroke-linecap="round" stroke-linejoin="round"><path id="kaydet-imi" d="…" style="opacity:0"/></g>`
  (çizgi 7 px; yol y 1035–1125, ortası 1080).
- Hap: `hap_w = Y.genislik("Fredoka", 700, "Kaydet", 64) + 80`; `ikon_en = 67` (60 + çizgi 7); `ara = 24`;
  `grup_en = ikon_en + ara + hap_w`; `gx = 510 - grup_en / 2`; `TX = gx + 3.5 - 30`; `hap_x = gx + ikon_en + ara`.
- `<g id="kaydet-hap" style="opacity:0"><rect x=hap_x y="1036" width=hap_w height="88" rx="44" fill="#f2a93b"/>
  <text x=hap_x+hap_w/2 y="1102" text-anchor="middle" font-family="Fredoka" font-weight="700" font-size="64"
  fill="#1b1a17">Kaydet</text></g>`; `svgOrigin` = `"{hap_x + hap_w/2} 1080"`.
- `assert gx >= 60 and gx + grup_en <= 960`.
- JS: `var el = $("#kaydet-imi"), L = el.getTotalLength(); el.style.strokeDasharray = L + " " + (L + 2);
  el.style.strokeDashoffset = L;` sonra `tl.set(el, ac({opacity:1}), Z.imi_ciz[0])` +
  `tl.fromTo(el, {strokeDashoffset: L}, {strokeDashoffset: 0, duration: 0.30, ease: "sine.inOut", immediateRender: false}, Z.imi_ciz[0])`.

## 8. Tema (renk yalnız hex eşlemesiyle; `ortak/hf_tema.py`)
| Yazılan değer | Koyu | Açık |
|---|---|---|
| `fill="#f3efe6"` / `stroke="#f3efe6"` | mürekkep `#f3efe6` | `#1b2440` |
| `rect fill="#f2a93b"` | `#f2a93b` | vurguDolgu `#ffe066` |
| `text fill="#1b1a17"` | `#1b1a17` | pilMetin `#1b2440` |
| `stroke="#c9c2b3"` | `#c9c2b3` | ikincil `#5a6275` |
| `#kagit` `fill="#fff9e6"` (eşlemesiz) | `#fff9e6` | CSS `.tema-acik #kagit{fill:#fffdf8}` |
| `#kart-kenar` `stroke="#1b1a17"` | CSS `#root #kart-kenar{stroke:var(--pilMetin)}` → `#1b1a17` | `#1b2440` |

CSS'i `<style>` içine `Y.ZEMIN_CSS`'ten sonra yaz. `hf_tema` `[stroke="#1b1a17"]`'yi zemine boyar; `#root #kart-kenar` kuralı
bunu ezer (özgüllük 2,0,0). Kart içinde sarı yok; tek sarı `Kaydet` hapı (+ ortak karaoke çizgisi).

## 9. Kurallar
1. `uret.py` metninde `#root.tema-acik` dizgesi OLMAZ (hf_tema onu "çevrildi" sayar, açık tema koyu çıkar). `.tema-acik #id` yaz.
2. Yasak söz listesini koda literal yazma (dış `grep` taramasını kirletir). Ekranda yalnız §5 metinleri var.
3. `rz1` kimliği kullanma. Emoji, QR, düğme taklidi, gradyan, gölge yok.
4. 0. sn'de açık öğe yok (GSAP `seek(0)` 0'daki `set`'i uygulamaz): bütün içerik öğeleri `style="opacity:0"` ile başlar.
5. Bütün tween'lerde `immediateRender: false` (03'teki `ac()` yardımcısı).
6. Sahnenin son 12 karesinde (yerel ≥ 5,50) tween yok: `assert` hap girişi bitişi `5.00 + 0.30 <= 5.50`.
7. Satır ≤ 24 karakter (`assert len(satır) <= 24`); yazı tabanı ≥ 64 (künye, kanal, altyazı ve `#uc` 48 istisnası istemde açık).
8. Bütün içerik öğeleri y 460–1380 ve x 60–960 içinde (assert: `#uc` 480–540, kart 600–980, kaydet 1020–1140).
9. Python: tip ipuçları zorunlu; girinti 4 boşluk (03 ile aynı); satır ≤ 120.

## 10. Kabul ölçütü (agy koşmaz; şef koşar)
- `ONIZLE_YALNIZ=1 bash calistir.sh --tema acik` → `önizleme hazır`, `zamanlar.json` 3 ses olayı, `olaylar.json` 3 satır.
- `araclar/qa-yerel.sh 02-04-ydt-temel-s1 08-hyperframes-kaydet 20.05,22.75,25.40 25.40 --hazirla` → çıkış 0.
- `araclar/cakisma-kapisi.mjs … --sahne 08-hyperframes-kaydet` → çıkış 0, 0 uyarı.
- Karede: 20,05 yalnız kanal + künye (kart 20,54'te girer); 22,75 `üç farktan biri` + kart + altyazı; 25,40 + yer imi + `Kaydet` hapı.
