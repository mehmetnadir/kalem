# SPEC — sahne 03 Kaydet (simple-present-temel-s1, huni v2, HyperFrames DİKEY 1080×1920) · 15.11.2026

Yazan: şef (istem D-S1 03-hyperframes-kaydet). Uygulayan: `agy-filo tek --rol kod`.
Bağlayıcı: `/home/sef/01dev/dijital-anlatim/.claude/docs/huni-v2-standart.md` §1–§3, paket `BRIEF-S1.md` ("Sahne içeriği" 15,18–17,40).

## 1. Yazılacak dosya
- YAZ: `/home/sef/01dev/_worktrees/kalem-0204/projeler/simple-present-temel-s1/sahneler/03-hyperframes-kaydet/uret.py`
- Başka dosyaya dokunma. `yardim.py`, `olay.py`, `calistir.sh` hazır (şef kopyaladı ve kurdu). Silme yok. Test, render, git yok.

## 2. Kalıp (oku, yapıyı al; kodu birebir kopyalama)
Kaynak: `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s1/sahneler/03-hyperframes-cta/uret.py` (huni v2).
Alınacak yapı:
- `AD`, `sys.path.insert`, `import yardim as Y`, `PAKET`, `SAH` (`zaman.json` → `sahneler[]` içinde `klasor == AD.name`),
  `T_BAS = SAH["t_bas"]` (14,63), `KARE = SAH["kare"]` (105), `SURE = round(KARE / 30, 4)` (3,5).
- `SOZ` = `ortak/anlatim/sozcukler.json` içinde `cumle == 3`; `ALT` = `ortak/anlatim/altyazi.json` içinde `cumle == 3`.
- `yerel(t)`, `T(i, bas)`, `E(i, bas)` işlevleri ve `BEKLENEN_SOZLER` denetimi (assert) aynı biçimde.
- `uret() -> tuple[str, dict]`: HTML + zamanlar sözlüğü. `__main__`: `proje/` aç, `Y.font_kopyala(proje/assets/fonts)`,
  `proje/index.html` ve `zamanlar.json` yaz, iki satır özet bas.
- HTML iskeleti: `Y.font_css()`, `Y.ZEMIN_CSS`, `#sahne` CSS'i, `#root` öznitelikleri (`data-composition-id="main"`,
  `data-start="0"`, `data-duration=SURE`, `data-fps="30"`, `data-width="1080"`, `data-height="1920"`), `Y.zemin_html()`,
  tek `<svg id="sahne">`, `lib/gsap.min.js`, `window.__timelines["main"]`.
- Altyazı + karaoke: `Y.altyazi_svg(T_BAS, SURE, ALT)` ve 03'teki `V.alt` / `V.karaoke` döngüleri aynen.
- Künye: `Y.kunye_svg()` (argümansız; kanal katmanı `#kanal` + `#logoimg` + konu + rozet içinde gelir). Değiştirme.
- ALINMAYACAK: kapak kartı, `ana-kapak` dosya denetimi, `MutationObserver` betiği, `Gerisi`/`hap`/`YouTube` öğeleri.

## 3. Sözcük çapaları (cümle 3; `sozcukler.json`)
| i | sözcük | t0 (küresel) | yerel | kare |
|---|---|---|---|---|
| 0 | `Sınavdan` | 15,18 | 0,55 | 16 |
| 1 | `önce` | 15,74 | 1,11 | 33 |
| 2 | `lazım` | 15,94 | 1,31 | 39 |
| 3 | `olacak.` | 16,30 | 1,67 | 50 |
| 4 | `Kaydet.` | 17,10 (t1 17,82) | 2,47 | 74 |

`BEKLENEN_SOZLER = [(0,"Sınavdan"), (1,"önce"), (2,"lazım"), (3,"olacak"), (4,"Kaydet")]`; `assert len(SOZ) == 5`;
`assert len(ALT) == 1` (ham parça 1; `Y.altyazi_svg` onu iki cümleye kendisi böler). Zaman her yerde `T(i, bas)`'tan okunur;
sabit saniye yazma.

## 4. Olay listesi
| olay | yerel sn | kare | küresel | sözcük | hareket |
|---|---|---|---|---|---|
| `kart_giris` | yerel(T(0,"Sınavdan")) = 0,55 | 16 | 15,18 | `Sınavdan` | `#kart` ölçek 0,96 → 1 + opaklık 0 → 1, 0,45 sn, `power3.out`, `svgOrigin "510 790"` |
| `kart_sabit` | 0,55 + 0,45 = 1,00 | 30 | 15,63 | — | hareket yok; kart sahne sonuna kadar sabit (17,74'e 2,11 sn) |
| `imi_ciz` | yerel(T(4,"Kaydet")) = 2,47 | 74 | 17,10 | `Kaydet.` | `#kaydet-imi` opaklık 1 (set) + `strokeDashoffset` L → 0, 0,30 sn, `sine.inOut` |
| `hap_giris` | yerel(T(4)) + 0,10 = 2,57 | 77 | 17,20 | `Kaydet.` | `#kaydet-hap` opaklık 0 → 1, ölçek 0,9 → 1, 0,20 sn (17,40'ta biter), `back.out(1.6)`, `svgOrigin` = hap ortası |
| `kuyruk_durgun` | 2,77 → 3,50 | 83 → 105 | 17,40 → | — | hareket yok |

Ses olayları (`zamanlar["olaylar"]`, `[yerel_sn, tur, guc]`): `[0,55, "vurus", 0.5]`, `[2,47, "cizgi", 0.6]`, `[2,57, "tik", 0.5]`.
Değerler `yerel(T(...))` ile hesaplanır. `olay.py` hepsinin 12 ≤ kare < 93 olduğunu denetler.
`zamanlar` sözlüğü 03 ile aynı şemadır: `fps`, `kare`, `sure`, `t_bas`, her olay için `[yerel_bas, süre]` (`kart_giris`,
`imi_ciz`, `hap_giris`, `kuyruk_durgun`), `olaylar`, `olay_listesi` (her satır `olay`, `kare` = round(yerel × 30), `yerel`,
`kuresel`, `sozcuk`; 5 satır, tablo sırasıyla).

`#kart` üzerinde 0,55 + 0,45 sn sonrasında hiçbir tween yok. Sahnede çıkış hareketi yok. 0–0,55 arası yalnız kanal + künye görünür.

## 5. Yerleşim (px; bütün öğeler x 60–960 içinde)
| Öğe | Kimlik | Değer |
|---|---|---|
| Künye + kanal | `#kunye` | `Y.kunye_svg()`; y 291–434; dokunma |
| Kart grubu | `#kart` (`<g>`, `style="opacity:0"`) | aşağıdaki 4 öğe bu sırayla, DOĞRUDAN `#kart` çocuğu (ara `<g>` yok) |
| — kâğıt | `#kagit` (`<rect>`) | x 61, y 601, w 898, h 378, rx 22, `fill="#fff9e6"`, `stroke="#c9c2b3"`, `stroke-width="2"` (dış kenar 60–960 × 600–980) |
| — kalem kenarı | `#kart-kenar` (`<path>`) | elle çizilmiş dikdörtgen, §6; `fill="none"`, `stroke="#1b1a17"`, `stroke-width="4.5"`, round cap/join |
| — kural satırı 1 | `#kural1` (`<text>`) | `He, she, it: s gelir;` Fredoka 700, boy B, x 110, taban T1, `fill="#1b1a17"` |
| — kural satırı 2 | `#kural2` (`<text>`) | `I, you, we, they: s yok.` Fredoka 700, boy B, x 110, taban T2, `fill="#1b1a17"` |
| Kaydet grubu | `#kaydet` (`<g>`) | yer imi + sarı hap, yatayda 510'a ortalı, y 1020–1140; §7 |
| Altyazı | `#altyazi` | `Y.altyazi_svg(...)` çıktısı, y 1400–1550 |

Kural satırı ölçüsü: B = 80'den 64'e inerek, iki satırın `Y.genislik("Fredoka", 700, satır, B)` en büyüğü ≤ 800 olan ilk boy
(beklenen 80; satır 2 ≈ 776 px). `assert B >= 64`. Satır aralığı `A = round(1.32 * B)`; `T1 = round(790 - A / 2 + 0.32 * B)`;
`T2 = T1 + A` (B 80 → A 106, T1 763, T2 869). Satır sonu `110 + genişlik ≤ 910` (assert). Kart içinde vurgu yok (sarı yok,
alt çizgi yok); iki satır tek renk.

## 6. Kalem kenarı yolu (`#kart-kenar`)
- Taban dikdörtgen: x 76–944, y 616–964 (kâğıdın 16 px içi).
- Tek alt yol (tek `M`; Chrome kesik desenini her `M`'de baştan başlatır). Biçim: `M` + kenar başına 3 ara noktalı `Q` ya da `L`
  dizisi. Her ara noktaya sabit dizi kaydırması uygula: `KAY = [1.6, -1.2, 2.2, -0.8, 1.0, -2.0, 0.6, 1.8, -1.4, 0.4, -2.2, 1.2]`
  (sırayla, dik yönde, ±2,5 px'i geçmez). Rastgele sayı yok (deterministik).
- Başlangıç sol üst köşeden 10 px sağda (86, 616); saat yönünde dolaşır; bitiş başlangıcı 14 px geçer (sol üstte hafif
  bindirme, el çizimi izi). `Z` yok.
- `assert`: bütün noktalar 74 ≤ x ≤ 946 ve 614 ≤ y ≤ 966 (kâğıdın içinde, yazıdan uzak).
- Kenar kartla birlikte girer (kartın bir parçası); ayrı çizim hareketi yok.

## 7. Kaydet grubu (`#kaydet`)
- Yer imi yolu (Tabler `bookmark`, MIT; yolu literal yaz, dosyadan okuma):
  `M18 7v14l-6 -4l-6 4v-14a4 4 0 0 1 4 -4h4a4 4 0 0 1 4 4z` (24 birimlik kutu; yol x 6–18, y 3–21).
- `<g id="kaydet-ikon" transform="translate(TX 1020) scale(5)" fill="none" stroke="#f3efe6" stroke-width="1.4"
  stroke-linecap="round" stroke-linejoin="round"><path id="kaydet-imi" d="…" style="opacity:0"/></g>`
  (çizgi 7 px; yol y 1035–1125, ortası 1080).
- Hap: `hap_w = Y.genislik("Fredoka", 700, "Kaydet", 64) + 80` (≈ 288); `ikon_en = 67` (60 + çizgi 7); `ara = 24`;
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
| `stroke="#f3efe6"` (yer imi) | mürekkep `#f3efe6` | `#1b2440` |
| `rect fill="#f2a93b"` (hap) | `#f2a93b` | vurguDolgu `#ffe066` |
| `text fill="#1b1a17"` (kural, hap yazısı) | `#1b1a17` | pilMetin `#1b2440` |
| `stroke="#c9c2b3"` (kâğıt kenarı) | `#c9c2b3` | ikincil `#5a6275` |
| `#kagit` `fill="#fff9e6"` (eşlemesiz) | `#fff9e6` | CSS `.tema-acik #kagit{fill:#fffdf8}` |
| `#kart-kenar` `stroke="#1b1a17"` | CSS `#root #kart-kenar{stroke:var(--pilMetin,#1b1a17)}` → `#1b1a17` | `#1b2440` |

CSS'i `<style>` içine `Y.ZEMIN_CSS`'ten sonra yaz. `hf_tema` `[stroke="#1b1a17"]`'yi zemine boyar; `#root #kart-kenar` kuralı
bunu ezer (özgüllük 2,0,0). Kart içinde sarı yok; tek sarı `Kaydet` hapı (+ ortak karaoke çizgisi ve künye rozeti, kanal katmanı).

## 9. Kurallar
1. `uret.py` metninde `#root.tema-acik` dizgesi OLMAZ (hf_tema onu "çevrildi" sayar, açık tema koyu çıkar). `.tema-acik #id` yaz.
2. Yasak söz listesini koda literal yazma (dış `grep` taramasını kirletir). Ekranda yalnız §5 ve §7 metinleri var.
3. `rz1` kimliği kullanma. Emoji, QR, düğme taklidi, gradyan, gölge yok.
4. 0. sn'de açık öğe yok (GSAP `seek(0)` 0'daki `set`'i uygulamaz): bütün içerik öğeleri `style="opacity:0"` ile başlar.
5. Bütün tween'lerde `immediateRender: false` (03'teki `ac()` yardımcısı).
6. Sahnenin son 12 karesinde (yerel ≥ 3,10) tween yok: `assert` hap girişi bitişi `yerel(T(4)) + 0.10 + 0.20 <= (KARE - 12) / 30`.
   İlk 12 kare (yerel < 0,40) geçiş payıdır: kart girişi 0,55'te başlar.
7. Satır ≤ 24 karakter (`assert len(satır) <= 24`); yazı tabanı ≥ 64 (künye, kanal ve altyazı hariç).
8. Bütün içerik öğeleri y 460–1380 ve x 60–960 içinde (assert: kart 600–980, kaydet 1020–1140).
9. Python: tip ipuçları zorunlu; girinti 4 boşluk (03 ile aynı); satır ≤ 120.

## 10. Kabul ölçütü (agy koşmaz; şef koşar)
- `ONIZLE_YALNIZ=1 bash calistir.sh --tema acik` → `önizleme hazır`, `zamanlar.json` 3 ses olayı, `olaylar.json` 3 satır.
- `araclar/qa-yerel.sh simple-present-temel-s1 03-hyperframes-kaydet 14.70,16.20,17.65 17.65 --hazirla` → çıkış 0.
- `araclar/cakisma-kapisi.mjs … --sahne 03-hyperframes-kaydet` → çıkış 0, 0 uyarı.
- Karede: 14,70 yalnız kanal + künye (kart 15,18'de girer); 16,20 kart tam + altyazı; 17,65 + yer imi + `Kaydet` hapı.
