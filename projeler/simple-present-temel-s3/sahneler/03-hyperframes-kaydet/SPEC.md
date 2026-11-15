# SPEC — simple-present-temel-s3 sahne 03 Kaydet (HyperFrames, DİKEY 1080×1920, huni v2) · 15.11.2026

Kök: K = `/home/sef/01dev/_worktrees/kalem-0204`. Paket: P = `K/projeler/simple-present-temel-s3`.
Sahne dizini: S = `P/sahneler/03-hyperframes-kaydet`.
Bağlayıcı standart: `/home/sef/01dev/dijital-anlatim/.claude/docs/huni-v2-standart.md` (§1, §2, §3 "3 Kaydet").
Paket brief: `P/BRIEF-S3.md` ("Sahne içeriği" 12,84–18,10 satırları).

**Yazılacak tek dosya:** `S/uret.py` (yeni). Başka dosyaya dokunma. Silme yok. Test, render, git yok.
`S/yardim.py`, `S/olay.py`, `S/calistir.sh` hazır (emsalden kopya; dokunma).

Genel kurallar: Python 3, type hint zorunlu, 4 boşluk girinti, satır ≤ 120. Sabit saniye YAZMA: bütün zamanlar
`sozcukler.json` çapasından türer. Renkler HER ZAMAN koyu taban değerleriyle yazılır (`Y.RENK`); açık temaya `P/ortak/hf_tema.py`
CSS öznitelik seçicileriyle çevirir. Eşleme: `fill="#f3efe6"` / `stroke="#f3efe6"` → murekkep · `stroke="#f2a93b"` → vurgu ·
`rect fill="#f2a93b"` → vurguDolgu (`#ffe066` açık) · `text fill="#1b1a17"` → pilMetin (`#1b2440` açık).
Ekranda yasak: "Tam ders", "dakika", "izle", QR, emoji (bu iki yasak söz kodda yorum olarak da geçmez). Çip YOK. Kırmızı YOK. Yeşil YOK.

---

## 1. Kalıp kaynakları (yalnız okunur)

| Ne | Dosya · satır | Alınacak kalıp |
|---|---|---|
| Dosya iskeleti | `K/projeler/02-04-ydt-temel-s1/sahneler/03-hyperframes-cta/uret.py` 1–23 | docstring, `from __future__`, `AD`, `sys.path`, `import yardim as Y`, `PAKET`, `SAH` (zaman.json `sahneler[]`, `klasor == AD.name`), `T_BAS`, `KARE`, `SURE = round(KARE / 30, 4)` |
| Kapak kontrolü | aynı dosya 25–31 | ALINMAZ (bu sahnede kapak yok) |
| Sözcük ve altyazı | aynı dosya 33–41 | `SOZ`, `ALT`, `R = Y.RENK`; filtre `cumle == 3` |
| `yerel()`, `T()`, `E()` | aynı dosya 44–64 | aynen (cümle numarası metinde 3) |
| Sözcük doğrulaması | aynı dosya 67–81 | `BEKLENEN_SOZLER` + `assert` deseni |
| HTML iskeleti | aynı dosya 193–203, 230–236 | `<style>` içinde `Y.font_css()` + `Y.ZEMIN_CSS` + `#sahne{position:absolute;left:0;top:0;}`, `#root` öznitelikleri, `Y.zemin_html()`, tek `<svg id="sahne">`, `{kunye_svg}`, `<g id="altyazi">` |
| Kapak href betiği | aynı dosya 237–253 | ALINMAZ |
| GSAP iskeleti + altyazı + karaoke | aynı dosya 254–280, 300–303 | `gsap.timeline({paused:true})`, `ac()`, altyazı aç/kapa döngüsü, karaoke çizgisi döngüsü (aynen), `window.__timelines["main"] = tl` |
| Kalem darbesi (dashoffset) | `K/projeler/02-04-ydt-temel-s1/sahneler/01-hyperframes-kapak/uret.py` 454–464 | `getTotalLength()`, `strokeDasharray = L + " " + (L + 2)`, `strokeDashoffset = L`, `tl.set(opacity 1)`, dashoffset → 0, `ease: "sine.inOut"`. FARK: `tl.to` yerine `tl.fromTo({strokeDashoffset: L}, {strokeDashoffset: 0, …, immediateRender: false})` (sırasız aramada da doğru kare) |
| `__main__` | `03-hyperframes-cta/uret.py` 307–314 | aynen (`proje/` aç, `Y.font_kopyala`, `index.html` + `zamanlar.json` yaz, iki `print`) |

Yardımcı API (`S/yardim.py`, hazır): `Y.RENK`, `Y.HUD`, `Y.genislik(aile, agirlik, metin, boy)`, `Y.font_css()`, `Y.ZEMIN_CSS`,
`Y.zemin_html()`, `Y.font_kopyala(dizin)`, `Y.kunye_svg()` (kanal katmanı + künye `Simple Present` + rozet `YDT · TEMEL`; dokunma),
`Y.altyazi_svg(t_bas, sure, liste) -> (svg, zaman, karaoke)`. `Y.yol_uzunluk` KULLANILMAZ (simge yolları göreli komut ve yay içerir).

---

## 2. Zaman (tek kaynak)

- `SAH`: no 3, `t_bas` 12.84, `kare` 170 → `SURE` 5.6667. `yerel(t) = round(t - T_BAS, 3)`; kare = `round(yerel * 30)`.
- `SOZ` = `P/ortak/anlatim/sozcukler.json` içinde `cumle == 3`. `assert len(SOZ) == 10`. Doğrulama (`T(i, bas)` ile):
  `[(0,"Does"), (1,"varsa"), (2,"fiil"), (3,"yalın"), (4,"Bir"), (5,"arkadaşına"), (6,"gönder"), (7,"o"), (8,"da"), (9,"karıştırıyor")]`.
- `ALT` = `P/ortak/anlatim/altyazi.json` içinde `cumle == 3`. `assert len(ALT) == 2`
  (`Does varsa fiil yalın.` 13,39–15,31 · `Bir arkadaşına gönder; o da karıştırıyor.` 15,46–18,18).

## 3. Olay listesi (zamanlar.json anahtarı = `[yerel_bas, sure]`)

| Olay | Başlangıç (küresel) | Yerel sn (kare) | Süre · ease | Ne olur |
|---|---|---|---|---|
| `kart_cerceve` | `T_BAS` 12,84 | 0.00 (0) | 0.40 · `sine.inOut` | `#kart-cerceve` kalem darbesi (dashoffset L → 0); aynı anda `#kart-zemin` opaklık 0 → 1 (0.40, `power2.out`) |
| `soz_does` | `T(0,"Does")` 13,39 | 0.55 (17) | 0.18 · `power2.out` | `#ks0` `Does` opaklık 0 → 1 |
| `soz_varsa` | `T(1,"varsa")` 13,71 | 0.87 (26) | 0.18 · `power2.out` | `#ks1` `varsa` |
| `soz_fiil` | `T(2,"fiil")` 14,35 | 1.51 (45) | 0.18 · `power2.out` | `#ks2` `fiil` |
| `soz_yalin` | `T(3,"yalın")` 14,75 | 1.91 (57) | 0.18 · `power2.out` | `#ks3` `yalın.` |
| `kart_tam` | `E(3,"yalın")` 15,31 | 2.47 (74) | tween yok (işaret) | kart tam; buradan sahne sonuna (2,79 sn+) kart hareketsiz |
| `yerimi_ciz` | `T(4,"Bir")` 15,46 | 2.62 (79) | 0.30 · `sine.inOut` | `#yerimi` grubu görünür, yol kalemle çizilir |
| `kaydet_hap` | `T(4,"Bir")` + 0.10 | 2.72 (82) | 0.30 · `back.out(1.6)` | `#kaydet` hap: ölçek 0.9 → 1 (`svgOrigin` = hapın sol-orta noktası), opaklık 0 → 1 |
| `ucak_ciz` | `T(6,"gönder")` 16,26 | 3.42 (103) | 0.30 · `sine.inOut` | `#ucak` grubu görünür, 2 yol sırayla çizilir (önce dış gövde, sonra iç kıvrım) |
| `gonder_yazi` | `T(6,"gönder")` + 0.08 | 3.50 (105) | 0.20 · `power3.out` | `#gonder` x −12 → 0, opaklık 0 → 1 |
| `kuyruk_durgun` | `E(9,"karıştırıyor")` 18,18 | 5.34 → sahne sonu | tween yok | — |

Çok yollu simgede süre yolların uzunluğuyla orantılı bölünür (JS'de `getTotalLength()` ile; toplam = olay süresi), yollar sırayla çizilir.
Bütün tween'ler `immediateRender: false` (`ac()` ya da açık yazım). Başlangıç durumları `style="opacity:0"`: `#kart-zemin`, `#ks0`–`#ks3`,
`#yerimi`, `#kaydet`, `#ucak`, `#gonder`. `#kart-cerceve` opaklığı 1; görünmezliği dashoffset = L ile sağlanır (JS hazırlığında).
`#kunye` opaklığı ve konumu hiç değişmez (tween yok, `gsap.set` yok).

Altyazı: `Y.altyazi_svg(T_BAS, SURE, ALT)` → `#al<i>` aç/kapa + karaoke çizgisi (emsal 262–280 döngüleri aynen).

Ses olayları (`zamanlar.json` `"olaylar"`, `[yerel_sn, tur, guc]`; `olay.py` kare 12 ≤ k < 158 ister):
`[0.40, "cizgi", 0.4]` (kart çerçevesi kapanır) · `[yerimi, "cizgi", 0.5]` · `[kaydet_hap, "tik", 0.6]` · `[ucak, "cizgi", 0.5]`.
`zamanlar.json` ayrıca: `fps` 30, `kare`, `sure`, `t_bas`, her olay anahtarı, `olay_listesi`
`[{"olay", "kare", "yerel", "kuresel", "sozcuk"}]` (her olay için bir satır; RAPOR tablosu için).

## 4. Yerleşim (px; içerik 460–1380, x 60–960; sağ 960–1080 boş)

| Öğe | Yazı · boy | Konum | Renk (koyu taban) |
|---|---|---|---|
| `#kart-zemin` | — | `<rect x=60 y=560 width=900 height=340 rx=30>` | `fill="#f3efe6"` + `fill-opacity="0.06"` (kâğıt tonu; iki temada da zeminden ayrışır) |
| `#kart-cerceve` | — | `<rect x=62 y=562 width=896 height=336 rx=28 fill="none" stroke-width=4 stroke-linecap="round" stroke-linejoin="round">` (dış kenar tam 60–960 / 560–900) | `stroke="#f3efe6"` |
| Kart yazısı, satır 1 `Does varsa` | Fredoka 700 · `K_BOY` | taban y 700; satır kart içinde yatay ortalı: `x1 = 510 - genislik(satır1)/2` | `#f3efe6` |
| Kart yazısı, satır 2 `fiil yalın.` | Fredoka 700 · `K_BOY` | taban y = 700 + round(1.18 × K_BOY) (88'de 804); `x2 = 510 - genislik(satır2)/2` | `#f3efe6` |
| ↳ sözcükler | — | her sözcük ayrı `<text>`: `#ks0` `Does` (x1) · `#ks1` `varsa` (x1 + genislik("Does ")) · `#ks2` `fiil` (x2) · `#ks3` `yalın.` (x2 + genislik("fiil ")); `text-anchor="start"`, `style="font-kerning:none;opacity:0"` | `#f3efe6` |
| Kaydet grubu (sol yarı, 60–510, merkez 285) | — | grup eni `G1 = 96 + 16 + hap_en`; `g1x = 285 - G1/2` | — |
| ↳ `#yerimi` yer imi simgesi | 24×24 ızgara, `scale(4)` (96 px) | `<g id="yerimi" transform="translate(g1x 1022) scale(4)" fill="none" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">` + 1 `<path>` | `stroke="#f3efe6"` |
| ↳ `#kaydet` hap | Fredoka 700 · 64 | `<rect>` x = g1x + 96 + 16, y 1022, en `hap_en = genislik(Fredoka 700, "Kaydet", 64) + 2×28`, boy 96, rx 48; `<text>` `Kaydet` ortalı (`text-anchor="middle"`), taban y 1092 | rect `#f2a93b`, yazı `#1b1a17` |
| Gönder grubu (sağ yarı, 510–960, merkez 735) | — | grup eni `G2 = 96 + 16 + genislik(Lexend 700, "Gönder", 56)`; `g2x = 735 - G2/2` | — |
| ↳ `#ucak` kâğıt uçak simgesi | 24×24 ızgara, `scale(4)` | `<g id="ucak" transform="translate(g2x 1022) scale(4)" …aynı öznitelikler…>` + 2 `<path>` | `stroke="#f3efe6"` |
| ↳ `#gonder` `Gönder` | Lexend 700 · 56 | x = g2x + 96 + 16, taban y 1090, hapsız | `#f3efe6` |
| `#kunye` | — | `Y.kunye_svg()` (kanal katmanı + künye; ilk kareden son kareye, animasyonsuz) | — |
| `#altyazi` | — | `<g id="altyazi">` + `Y.altyazi_svg` svg'si (y 1400–1550) | — |

`K_BOY`: 88'den başla; `max(genislik(satır1), genislik(satır2)) <= 900 - 2*56` olana kadar 1'er küçült; `assert K_BOY >= 64`
(ölçüm: 88'de satır 1 441,8 px, satır 2 346,2 px → 88 kalır).
Kontroller (`assert`): `g1x >= 60`, `g1x + G1 <= 510`, `g2x >= 510`, `g2x + G2 <= 960`, kart sözcüklerinin sağ ucu ≤ 960 - 56.

Simge yolları (Tabler Icons biçimi, MIT; 24×24, sahne içinde sabit dize olarak yaz; yerel `ortak/cizim/tabler/` içinde yok):
- `YERIMI = ["M18 7v14l-6 -4l-6 4v-14a4 4 0 0 1 4 -4h4a4 4 0 0 1 4 4z"]` (dikdörtgen gövde + alt V çentik)
- `UCAK = ["M21 3l-6.5 18a.55 .55 0 0 1 -1 0l-3.5 -7l-7 -3.5a.55 .55 0 0 1 0 -1l18 -6.5", "M10 14l11 -11"]`
  (çizim sırası: önce dış gövde, sonra iç kıvrım)

SVG sırası: `<defs>` (boş olabilir) → `#kart-zemin` → `#kart-cerceve` → `#ks0`–`#ks3` → `#yerimi` → `#kaydet` → `#ucak` → `#gonder`
→ `#kunye` → `#altyazi`.

## 5. Ekran metni (tamamı)

`Does varsa` / `fiil yalın.` (kart) · `Kaydet` (sarı hap) · `Gönder` · künye (`Simple Present`, `YDT · TEMEL`, `@ydspublishing`) ·
altyazı (cümle 3'ün 2 parçası). Başka metin yok. Sahne 02'nin örnek satırı (`doesn't go · Does she go?`) YOK.

## 6. Kurallar

- Tek vurgu: yalnız `Kaydet` hapı (+ altyazı karaoke altçizgisi, yardımcı işlevden). Kart içinde sarı YOK.
- Kart durgun: kart zemini, çerçevesi ve sözcükleri yalnız opaklık/dashoffset ile belirir; ölçek, konum, renk tween'i YOK.
  Hareket yalnız simgelerde (çizim) ve `Kaydet`/`Gönder` girişinde.
- Ekran metni sesten önce gelmez: her kart sözcüğü kendi `t0` anında belirir.
- Emoji yok: simgeler yalnız SVG `<path>` kalem çizimi.
- Sahne sonunda (yerel 5.34 → 5.6667) her şey yerinde, tween yok.

## 7. Kabul ölçütü (yazar koşmaz; şef doğrular)

- `/usr/bin/python3 S/uret.py` hatasız; `S/proje/index.html` ve `S/zamanlar.json` yazılır; `olay.py` assert'i geçer (4 olay).
- `grep -niE 'tam ders|dakika'` `S/*.py` ve `S/proje/index.html` içinde boş.
- İçerik x 60–960, y 460–1380; altyazı 1400–1550; 0–280 ve 1570–1920 boş; 960–1080 boş.
- `#kunye` (kanal dahil) her karede opaklık 1; konum değişmez.
- QA kareleri: küresel 12,90 (kare 2: çerçeve çizilmeye başlamış), 16,60 (kare 113: kart tam + yer imi + `Kaydet` + uçak + `Gönder` tam),
  18,00 (kare 155: aynı + altyazı parça 2); koyu 16,60.
