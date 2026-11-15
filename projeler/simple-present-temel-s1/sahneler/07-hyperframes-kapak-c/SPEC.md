# SPEC — simple-present-temel-s1 · sahne 07-hyperframes-kapak-c (huni v2; HyperFrames, 1080×1920, tek kare, ses yok)

Yazan: şef (15.11.2026, istem D-S1). Kod yazmaz; tasarım verir. K = `/home/sef/01dev/_worktrees/kalem-0204`.
Sahne dizini D = `K/projeler/simple-present-temel-s1/sahneler/07-hyperframes-kapak-c/`. Paket P = `K/projeler/simple-present-temel-s1/`.
Bağlayıcı: `/home/sef/01dev/dijital-anlatim/.claude/docs/huni-v2-standart.md` §1–§2, `P/BRIEF-S1.md` "Yerleşim" + "Kanal katmanı" + "Kapak",
`P/uretim-tutanagi/kapak-taslak.md` §2 ve §5. Paket yeni: bu sahnenin eski sürümü yok.

İçerik: başlık `HE GOES` / `I GO` (`ES` sarı hap; satır 2 mürekkep, vurgusuz) + otobüs kalem çizimi (sağa gider) + zemin çizgisi.
Figür yok, etiket yok, altyazı yok, çip yok. Künye satırında yalnız rozet `YDT · TEMEL` (x 60'tan).

## 1. Dosyalar

| Dosya | Durum | İş |
|---|---|---|
| `D/uret.py` | YOK | **YAZILACAK** (mutlak yol `/home/sef/01dev/_worktrees/kalem-0204/projeler/simple-present-temel-s1/sahneler/07-hyperframes-kapak-c/uret.py`) |
| `D/yardim.py` | VAR (sahne 01-hyperframes-kanca v2 kopyası) | DOKUNMA; yalnız `import yardim as Y` |
| `D/calistir.sh`, `D/olay.py`, `D/zamanlar.json` | VAR | DOKUNMA |
| `D/nesneler.json`, `D/proje/index.html` | uret.py yazar | §6 madde 4 |

Başka dosyaya dokunma. Silme yok. Test, render, snapshot, `calistir.sh`, git YOK.

## 2. Kalıp kaynakları (salt oku)

| Kalıp | Mutlak yol | Ne alınır |
|---|---|---|
| Ana emsal (aynı tür sahne, v2) | `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s1/sahneler/06-hyperframes-kapak-c/uret.py` | dosya düzeni aynen: başlık/importlar (satır 1–17), `zaman.json`/`zamanlar.json` doğrulaması (satır 19–33; `cikti` = `kapak-c.png`), sabitler (satır 35–46), `hesapla_s_ve_baslik` boy döngüsü (satır 49–68), `blok_kutulari`, `kesisim`, `kurallari_dogrula` biçimi, HTML kabuğu ve GSAP tek `set` çizelgesi (satır 360–385), `__main__` (satır 389–409) |
| Otobüs çizimi | `/home/sef/01dev/_worktrees/kalem-0204/projeler/simple-present-temel-s1/sahneler/01-hyperframes-kanca/uret.py` satır 70–71, 171–180, 340–352 | `BUS = Y.coco("bus", BUS_KUTU)`; yol noktalarından kutu ölçümü (`re.findall` sayıları, x = çift, y = tek indis); `<path d=… stroke-width="4.4" vector-effect="non-scaling-stroke"/>` dizisi. **AYNA YOK**: `translate(1280 0) scale(-1 1)` KULLANMA (o sahnede otobüs sola gider; burada sağa gider, coco yönü zaten sağa) |
| Rozeti x 60'a alma | aynı dosya satır 88, 403, 451–452 | `rz_x, rz_w = Y.rozet_konumu()`; `gsap.set("#ku-konu", { opacity: 0 }); gsap.set("#rz0", { x: KENAR − rz_x })` (kapak A ile aynı yöntem) |
| v2 künye ve sabitler | `D/yardim.py` | `Y.kunye_svg()` (argümansız; `<g id="kunye">` içinde `#kanal` = `#logoimg` + `#kanal-yazi`, `#ku-konu`, `#rz0`), `Y.HUD` (`kenar` 60, `sagSinir` 960, `icerikBas` 460, `icerikSon` 1380, `kanalYaziX` 263, `kanalYaziBoy` 42), `Y.rozet_konumu()` → `(x, w)`, `Y.KANAL_YAZI`, `Y.genislik`, `Y.coco`, `Y.RENK`, `Y.font_css()`, `Y.ZEMIN_CSS`, `Y.zemin_html()`, `Y.font_kopyala()`, `Y.W`, `Y.H` |

## 3. Sabitler

`KENAR = Y.HUD["kenar"]` (60) · `SAG = Y.HUD["sagSinir"]` (960) · `ICERIK_BAS = Y.HUD["icerikBas"]` (460) · `ICERIK_SON = Y.HUD["icerikSon"]` (1380) ·
`ORTA = (KENAR + SAG) / 2` (510) · `BASLIK_GEN = 900` · `BASLIK_UST = 470` · `ZEMIN_Y = 1360` · `BUS_W = 780` · `BUS_H = 303`.
Modül docstring'i: "Bantlar: kanal (280–350) → künye (360–450; yalnız rozet) → içerik (460–1380: başlık 470–873, otobüs ≈ 1053–1356, zemin çizgisi 1360) → alt boş (1570–1920)".

## 4. Yerleşim (y = yazı tabanı, px; x içerik bandı 60–960, orta 510)

```
y    0 ┌──────────────────────────────────────┐────────┐
       │ (boş zemin, çip YOK)                  │        │
   280 │ [logo] @ydspublishing                 │ sağ    │  Y.kunye_svg() → #kanal (değiştirme)
   360 │ (YDT · TEMEL)                         │ 960–   │  #rz0 x 60'a kayar, #ku-konu gizli
   470 │   HE GO[ES]                           │ 1080   │  Fredoka 700 S=190; hap 470–664
   842 │      I GO                             │ boş    │  GO, üstteki GO ile aynı x'te
  1053 │     ┌──otobüs (sağa)──┐               │        │  coco/bus, 780×303 kutu, ayna yok
  1360 │ ────┴─────────────────┴────────────── │        │  zemin çizgisi x 70–950
  1380 ├──────────────────────────────────────┤        │  içerik sonu
  1570 │ (boş)                                 │        │
```

### 4.1 Kanal + künye
`Y.kunye_svg()` çıktısı değiştirilmeden SVG'ye girer. uret.py logo, `@ydspublishing`, rozet, konu adı YAZMAZ.
JS'de (çizelgeden önce): `gsap.set("#ku-konu", { opacity: 0 })` ve `gsap.set("#rz0", { x: RZ_KAYMA })`, `RZ_KAYMA = KENAR − rz_x` (≈ −249,67).
Sonuç: künye satırında yalnız rozet, hap x 60 – 60 + rz_w (≈ 263,6), y 386–434.

### 4.2 Başlık — `<g id="baslik">`
- `g(m) = Y.genislik("Fredoka", 700, m, S)`; `p = 0,08·S` (hap iç payı); `a = 0,14·S` (GO ile ES arası boşluk; agy 0,10·S ile yazdı, karede hap O'ya 6 px kaldı → şef 0,14'e çıkardı, 15.11);
  `gb = g("HE GO") + a + g("ES") + p`.
- Boy: önce S = 100 ile `gb_100` ölç; `S = floor(min(190, BASLIK_GEN·100 / gb_100))`; `gb > BASLIK_GEN` iken S'yi 1 azalt (emsal döngüsü).
  Beklenen S = 190, gb ≈ 808,1.
- `x0 = ORTA − gb/2` (≈ 105,95).
- `T1 = BASLIK_UST + 0,86·S` (= 633,4; hap üstü tam 470'e oturur). `T2 = T1 + 1,10·S` (= 842,4).
- Satır 1: `bs-1` = `HE GO`, x = x0, taban T1. `bs-1es` = `ES`, x = `ES_X = x0 + g("HE GO") + a` (≈ 681,25), taban T1.
- Hap `es-hap` (`<rect>`): sol `ES_X − p` (≈ 666,05), sağ `ES_X + g("ES") + p` (= x0 + gb ≈ 914,05); üst `T1 − 0,86·S` (= 470),
  alt `T1 + 0,16·S` (= 663,8); `rx = 0,10·S`. Hap sol kenarı `> x0 + g("HE GO") + 0,01·S` (hap `O` harfine değmez) — assert.
- Satır 2: `bs-2` = `I GO`, x = `VX − g("I ")`, `VX = x0 + g("HE ")` (≈ 388,65; satır 2'deki `GO` satır 1'deki `GO` ile aynı x'ten başlar), taban T2.
- Renk ve stil:
  - `bs-1`, `bs-2`: `fill` = `R["murekkep"]`, **kontursuz** (stroke YOK), `style="font-kerning:none"`.
  - `es-hap`: `fill` = `R["vurgu"]` (`#f2a93b`; hf_tema açıkta `vurguDolgu #ffe066` yapar).
  - `bs-1es`: `fill` = `R["zemin"]` (`#1b1a17`; hf_tema açıkta `pilMetin #1b2440` yapar), kontursuz, `style="font-kerning:none"`.
  - Sıra: bs-1, es-hap, bs-1es, bs-2. Bütün `<text>`: `font-family="Fredoka" font-weight="700" font-size="{S}"`.
- Başlık bloğu: x0, y `BASLIK_UST`, w gb, alt `T2 + 0,16·S` (≈ 872,8).

### 4.3 Otobüs + zemin — `<g id="eskiz" fill="none" stroke=R["murekkep"] stroke-linecap="round" stroke-linejoin="round">`
| Öğe | Ölçü |
|---|---|
| otobüs `<g id="otobus">` | `BUS_KUTU = [ORTA − BUS_W/2, ZEMIN_Y − 4 − BUS_H, BUS_W, BUS_H]` = `[120, 1053, 780, 303]`; `BUS = Y.coco("bus", BUS_KUTU)`; her yol `<path d="{d}" stroke-width="4.4" vector-effect="non-scaling-stroke"/>`; transform YOK (ayna yok; coco otobüsü sağa bakar = `HE GOES` okuma yönü) |
| zemin çizgisi `<path id="zc">` | `M70 1360 L950 1360`, `stroke-width` 4, `vector-effect="non-scaling-stroke"` |

Otobüs kutusu sabit sayıyla değil, `BUS` yol noktalarından ölçülür (min/max x, y; 01-kanca satır 171–180 kalıbı).
Beklenen: x ≈ 120–900, y ≈ 1053–1356.

## 5. Tema (hf_tema.py ile uyum)
- `Y.ZEMIN_CSS`, `Y.zemin_html()`, `Y.font_css()` DEĞİŞTİRMEDEN kullan. Renkler yalnız `Y.RENK` anahtarları, SVG özniteliği, küçük harf hex.
- id `t2`, `ku-nokta`, `rz1` KULLANMA (hf_tema özel kurallar). `<path fill="#1b1a17">` YOK. Logo `#logoimg` `Y.kunye_svg()` içinde gelir.
- Koyu tema: aynı HTML, hf_tema paketin koyu paletini uygular (zemin `#1b1a17`, mürekkep `#f3efe6`, hap `#f2a93b`, `ES` `#1b1a17`).

## 6. Kurallar ve kabul ölçütü (uret.py içinde `assert`)
1. Bloklar (`kanal`, `kunye`, `baslik`, `es-hap`, `otobus`, `zc`): x ≥ 0, x + w ≤ 960, y ≥ 280, y + h ≤ 1380.
   İçerik blokları (`baslik`, `es-hap`, `otobus`, `zc`): x ∈ [KENAR, SAG], y ∈ [ICERIK_BAS, ICERIK_SON].
2. Yazı boyu: başlık S ≥ 64. Başlık 2 satır. Her satır ≤ 24 karakter (`HE GOES`, `I GO`).
3. Blok tanımları:
   - `kanal`: x 60, y 280, w = `Y.HUD["kanalYaziX"] + Y.genislik("Lexend", 700, Y.KANAL_YAZI, Y.HUD["kanalYaziBoy"]) − 60`, h 70.
   - `kunye`: x 60, y 360, w = `rz_w` (rozet x 60'a kaydı), h 90. `KENAR + rz_w ≤ 960` assert.
   - `baslik`: §4.2 bloğu. `es-hap`: §4.2 hap. `otobus`: §4.3 ölçülen kutu. `zc`: x 70, y 1358, w 880, h 4.
   Çiftler arası kesişim 0: kanal, kunye, baslik, otobus, zc (`es-hap` başlığın içinde, listeye girmez).
   `baslik` üstü ≥ ICERIK_BAS; `otobus` üstü − `baslik` altı ≥ 48; `otobus` üstü ≥ 1020;
   `ZEMIN_Y − 8 ≤ otobus altı ≤ ZEMIN_Y − 2` (tekerlek zemine oturur, çizgiyi kesmez); `ZEMIN_Y + 2 ≤ ICERIK_SON`;
   hap `O`'ya değmez (§4.2); `es-hap` sağı ≤ SAG.
4. `nesneler.json`: `[{"ad", "x", "y", "w", "h"}]` tam sayı (round); sıra: kanal, kunye, baslik, es-hap, otobus, zc.
5. Yasak: emoji, kırmızı (`kirmizi`), yeşil, gradyan, gölge, kontur halesi (`paint-order`), `Math.random`, `Date`, try/catch, hareket
   (çizelgede tek `set` çifti dışında tween yok; `gsap.set` yalnız §4.1'deki iki satır).
6. Dosyada şu sözcükler GEÇMEZ (yorum dahil): "tam ders", "dakika", "QR", "izle". Python: tür ipuçları bütün işlevlerde.
7. `/usr/bin/python3 uret.py` stdout'a `index.html yazıldı <bayt>` ve `S=<boy>` basar; hata yoksa çıkış 0.

## 7. Olay listesi
Durağan kare; ses, altyazı, çip yok. `olaylar.json` = `[]` (olay.py). Çizelge 1,0 sn (HyperFrames en az), yakalama 0,5 sn; ilk = orta = son kare.

| Olay | Kare / sn | Cümle sözcüğü |
|---|---|---|
| kapak tam görünür (kanal, rozet, başlık, hap, otobüs, zemin çizgisi) | 0 / 0,00 → son | — (anlatımdan bağımsız; küresel anlatım saniyesi yok) |

Kabul (şef koşturur, ajan koşturmaz): `bash calistir.sh --tema acik|koyu` → `P/kapak-c.png` ve `D/k/koyu/kapak-c-koyu.png` 1080×1920;
kanal katmanı x 60'tan, y 280–350; rozet y 386–434, x 60'tan; içerik 460–1380 ve x ≤ 960; 0–280 ve 1570–1920 boş; taşma, kesik yazı, üst üste binme yok.
