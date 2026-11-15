# SPEC v2 — 02-04-ydt-temel-s3 sahne 03 Çağrı (HyperFrames, DİKEY 1080×1920) · huni v2 · 15.11.2026

MAKİNE: Linux x86_64 (srv21). Python `/usr/bin/python3`. Bağlayıcı: `/home/sef/01dev/dijital-anlatim/.claude/docs/huni-v2-standart.md`.

## 0. Görev
Yazılacak dosya (yalnız bu): `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s3/sahneler/03-hyperframes-cta/uret.py`
Dosyayı BAŞTAN yaz (üzerine yaz). v1 içeriği (üç farktan biri, Tam ders, ders bandı, saat, dört buçuk dakikada, tren, bilet,
`CIP`, `Y.kunye_svg`, `Y.altyazi_svg`) TAMAMEN kalkar. Başka dosyaya dokunma. Silme yok. Test, render, git yok.

Kalıp kaynağı (yalnız okunur, v1): `/home/sef/Silinecekler/2026-11-15-huni-v2/02-04-ydt-temel-s3/sahneler-v1/03-hyperframes-cta/uret.py`.
Oradan aynen al: docstring biçimi, `AD`/`PAKET`/`SAH`/`T_BAS`/`KARE`/`SURE` okuma (zaman.json `sahneler[]`, `klasor == AD.name`),
`SOZ` ve `ALT` okuma, `T(i, bas)` ve `E(i, bas)` işlevleri, `BEKLENEN_SOZLER` döngüsü, `clipPath` + `yaz()` kalıbı, JS işlevleri
`ac`, `darbe`, `kinetik` (ease aşağıda değişir), altyazı aç/kapa döngüsü, `window.__timelines["main"]`, `__main__` bloğu
(`Y.font_kopyala`, `proje/index.html` + `zamanlar.json` yazımı). Yardımcılar `yardim.py`'den: `Y.genislik`, `Y.font_css()`,
`Y.ZEMIN_CSS`, `Y.zemin_html()`, `Y.RENK`, `Y.font_kopyala`. `yardim.py`'deki `kunye_svg`, `altyazi_svg`, `HUD` KULLANILMAZ (v1 HUD).

Type hint zorunlu (her işlev ve modül sabiti). Satır ≤ 120 karakter. Girinti 4 boşluk (v1 gibi).

## 1. Zaman (sabit saniye yazma; hepsi sözcük çapasından)
- `SAH` = zaman.json `03-hyperframes-cta`: `t_bas` 21.33, `kare` 239. `SURE = round(KARE / 30, 4)` (7.9667).
- `SOZ` = `ortak/anlatim/sozcukler.json` içinde `cumle == 5` (9 sözcük).
- `BEKLENEN_SOZLER`: (0 "Bu") (1 "sadece") (2 "başlangıç") (3 "Dersin") (4 "tamamı") (5 "YDS") (6 "Publishing") (7 "YouTube")
  (8 "kanalında"). Kayarsa assert durdurur.
- Yerel sn = küresel − T_BAS (`y_sn`), 4 basamak yuvarla.
- `ALT` = `ortak/anlatim/altyazi.json` içinde YALNIZ `cumle == 5` parçaları (2 parça: 21,88–23,64 ve 23,79–27,39).

## 2. Renkler (tema CSS'i `ortak/hf_tema.py` bu değerleri değişkene çevirir; başka renk yazma)
| Rol | Yazılacak değer | Açık tema sonucu |
|---|---|---|
| murekkep (yazı, çerçeve) | `fill`/`stroke` `#f3efe6` | `#1b2440` |
| ikincil (altyazı okunmamış sözcük) | `fill` `#c9c2b3` | `#5a6275` |
| hap/rozet dolgusu (vurguDolgu) | `<rect fill="#f2a93b">` | `#ffe066` |
| hap/rozet yazısı (pilMetin) | `<text fill="#1b1a17">` | `#1b2440` |
| hap kalem çizgisi (vurgu) | `<path stroke="#f2a93b" fill="none">` | `#d9900f` |
Kırmızı yok, emoji yok, gradyan/gölge yok. Şu kimlikleri KULLANMA: `t2`, `rz1`, `ku-nokta` (tema CSS'inde özel kural var).

## 3. Yerleşim (px, 1080×1920; sabitler modül başında, adlı)
Bütün öğeler tek `<svg id="sahne" width="1080" height="1920" viewBox="0 0 1080 1920">` içinde (kapı yalnız `#sahne` altını ölçer).

### 3.1 Kanal katmanı + künye — `<g id="kunye">` (kapı `#kunye` altını `kunye` türü sayar)
Kare 0'dan son kareye opaklık 1. Bu grubun hiçbir öğesine tween, `style="opacity:0"`, giriş/çıkış YOK.
1. `<g id="kanal">` (ad kapıda `kunye:kanal:*`):
   - `<image id="logoimg" href="assets/logo.svg" x="53.2" y="291" width="193.5" height="48"/>` (genişlik = 48 × 1920 / 476,3;
     id `logoimg` zorunlu: canlı önizleme koyu temada logo dosyasını bu id ile değiştirir).
   - `<text>` `@ydspublishing`, Lexend 700, 42 px, `fill="#f3efe6"`, x 263, y (taban) 330.
2. Künye konu `<text id="ku-konu">` `Simple Present vs Present Continuous`, Fredoka 700, `fill="#f3efe6"`, x 60, taban y 420.
   Boy: 34'ten 28'e inen döngü; ilk `60 + w_konu + 20 + w_rozet <= 960` olan boy (ölçüm: 34 sığar, son x 868).
3. Rozet `<g id="rz0">`: `<rect>` x = 60 + w_konu + 20, y 386, h 48, rx 24, genişlik = Lexend 700 26 `YDT · TEMEL` + 40,
   `fill="#f2a93b"`; `<text>` `YDT · TEMEL` Lexend 700 26, `text-anchor="middle"`, x = rozet ortası, taban y 419, `fill="#1b1a17"`.
   Çip YOK. 2 satır ders adı YOK. Üst logo (y 48–144) YOK.

### 3.2 Giriş sözü `Bu sadece başlangıç.` — y 470–600
- Fredoka 700. Boy = min(96, floor(900 / genislik(Fredoka 700, metin, 1))) (ölçüm: 96 → 890,9 px). Assert boy ≥ 64, w ≤ 900.
- Sol hizalı x 60, taban y 560. Üç ayrı `<text>`: `#gs0` `Bu` · `#gs1` `sadece` · `#gs2` `başlangıç.`; x = 60 + genislik("Bu ")
  ve 60 + genislik("Bu sadece ") (aynı boy). `fill="#f3efe6"`, başta `style="opacity:0"`.

### 3.3 Ana ders kapağı kartı — x 60–960, y 620–1126 (900×506)
- `<defs>` içinde `<clipPath id="kapakkirp"><rect x="60" y="620" width="900" height="506" rx="24"/></clipPath>`.
- `<g id="kapakg" style="opacity:0">` içinde:
  - `<image id="kapakA" href="assets/ana-kapak.png" x="60" y="620" width="900" height="506" preserveAspectRatio="xMidYMid slice"
    clip-path="url(#kapakkirp)"/>` (açık tema)
  - `<image id="kapakK" href="assets/ana-kapak-koyu.png" …aynı…/>` (koyu tema)
  - `<rect id="kapakcer" x="60" y="620" width="900" height="506" rx="24" fill="none" stroke="#f3efe6" stroke-width="3"/>`
- Tema seçimi CSS ile (render tema sınıfını dosyaya gömer; canlı önizleme sınıfı değiştirir), `<style>` içine:
  `#kapakA{display:none}#root.tema-acik #kapakA{display:inline}#root.tema-acik #kapakK{display:none}`
- Kapağın üstüne oynat düğmesi, ilerleme çubuğu, süre etiketi, yazı KOYMA.

### 3.4 `@ydspublishing` / `YouTube` — y 1150–1370
- Önce tek satır dene: Lexend 700 64; hap genişliği = w(`@ydspublishing`) + 64; tek satır toplam = hap + 20 + w(`· YouTube`).
  Toplam ≤ 900 ise tek satır (hap y 1160–1264, `· YouTube` hap sonu + 20'de, taban 1234); değilse İKİ SATIR (ölçüm: 946,6 > 900 →
  iki satır). İki dal da kodda olsun; seçilen dalı `zamanlar.json` içine `"cagri_satir": 1|2` yaz.
- İki satır düzeni:
  - Hap `<g id="hapg">`: `<rect id="hapdolgu">` x 60, y 1160, w = w(`@ydspublishing`) + 64, h 104, rx 52, `fill="#f2a93b"`,
    başta `style="opacity:0"`; `<path id="hapcizgi">` aynı yuvarlak dikdörtgenin çevresi (tek kapalı yol, sol orta noktadan başla,
    saat yönünde; köşeler yay `A` ya da `C` ile), `fill="none" stroke="#f2a93b" stroke-width="4" stroke-linecap="round"`,
    başta `style="opacity:0"`; `<text id="hapyazi">` `@ydspublishing` Lexend 700 64, x 92, taban 1234, `fill="#1b1a17"`,
    `clip-path="url(#cph)"` (kırpma dikdörtgeni `#crh`, genişlik 0'dan açılır; v1 `cp()` kalıbı).
  - `<text id="yt">` `YouTube` Lexend 700 64, x 60, taban 1346, `fill="#f3efe6"`, başta `style="opacity:0"`. (İki satırda `·` yok.)
- YouTube logosu, kırmızı düğme, ok, "izle" düğmesi YOK.

### 3.5 Altyazı + karaoke `<g id="altyazi">` — y 1400–1550, x 60–960 (orta x 510)
- Her parça `<g id="al{i}" style="opacity:0">`. Satır kırma: Lexend 500 44, satır genişliği ≤ 900, en çok 2 satır; 2 satıra
  sığmazsa boy 40, sonra 36 (en küçük boyda da sığmazsa assert).
- Satır `<text>` `text-anchor="middle"` x 510. 1 satır: taban 1490. 2 satır: taban 1462 ve 1518.
- Her sözcük ayrı `<tspan id="al{i}w{k}" fill="#c9c2b3">` (tspan'a `x`/`y`/`dy` VERME; sözcük arası tek boşluk tspan dışında metin).
- Karaoke: sözcük kendi `t0` anında `fill` özniteliği `#c9c2b3` → `#f3efe6` (GSAP `tl.set(…, {attr:{fill:"#f3efe6"}})`,
  `immediateRender:false`). Ölçek, zıplama, sarı YOK (klişe #10). Parça sözcükleri `SOZ` içinden zaman aralığıyla eşlenir
  (`p.t0 − 0.05 ≤ w.t0 < p.t1 + 0.05`); sözcük sayısı metindeki sözcük sayısına eşit değilse assert.
- Aç/kapa (yerel sn): aç = max(0, p.t0 − 0.05 − T_BAS); kapat = min(p.t1 + 0.35, sonraki p.t0 − 0.05) − T_BAS.
- Ekranda marka `YDS Publishing` (altyazi.json metni olduğu gibi).

### 3.6 Boş bölgeler
y 0–280 ve 1570–1920 yalnız zemin; x 960–1080 içerik yok. Hiçbir öğe bu bölgelere taşmaz (künye ve kanal 280–450 içinde).

## 4. Olay listesi (yerel kare = round((t − 21,33) × 30); JS'te süreler yerel sn)
| # | Olay | Küresel sn | Yerel sn | Kare | Çapa |
|---|---|---|---|---|---|
| 1 | Kanal + künye tam | 21,33 | 0 | 0 | sahne başı (tween yok) |
| 2 | Kapak kartı girer: `#kapakg` opaklık 0→1, ölçek 0,96→1 (svgOrigin 510 873), `power3.out` 0,40 sn | 21,33 | 0,00 | 0 | sahne başı |
| 3 | `#gs0` `Bu` kinetik | 21,88 | 0,55 | 16 | `T(0,"Bu")` |
| 4 | `#gs1` `sadece` kinetik | 22,12 | 0,79 | 24 | `T(1,"sadece")` |
| 5 | `#gs2` `başlangıç.` kinetik | 22,68 | 1,35 | 40 | `T(2,"başlangıç")` |
| 6 | Altyazı parça 0 açılır / parça 1'e geçer | 21,83 / 23,74 | 0,50 / 2,41 | 15 / 72 | `ALT` |
| 7 | Hap çizgisi `darbe("hapcizgi", …, 0.30)` | 25,07 | 3,74 | 112 | `T(5,"YDS")` |
| 8 | Hap dolgusu opaklık 0→1, 0,15 sn | 25,27 | 3,94 | 118 | `T(5,"YDS") + 0.20` |
| 9 | Hap yazısı kalemle yazılır: `#crh` genişlik 0 → w + 24 | 25,17 → 26,11 | 3,84 → 4,78 | 115 → 143 | `T(5,"YDS") + 0.10` → `E(6,"Publishing")` |
| 10 | `#yt` `YouTube` kinetik | 26,19 | 4,86 | 146 | `T(7,"YouTube")` |
| 11 | Durgun kuyruk (hiçbir tween yok) → son kare | 27,31 | 5,98 | 179 | `kanalında.` sesi biter |
`kinetik`: `fromTo` opaklık 0 → 1, y +24 → 0, `power3.out`, 0,30 sn, `immediateRender:false` (stil anayasası §4).
Son tween en geç `E(8,"kanalında")` (27,39) bitmeli; ondan sonra son kareye kadar düzen sabit (son kare = tam düzen).

Ses olayları `zamanlar.json` `"olaylar"`: `[yerel_sn, tur, guc]` — `olay.py` 12 ≤ kare < 227 ister:
| Kare | Tür | Güç | Çapa |
|---|---|---|---|
| 16 | `tik` | 0.40 | `Bu` |
| 40 | `tik` | 0.45 | `başlangıç.` |
| 112 | `cizgi` | 0.50 | `YDS` (hap çizgisi) |
| 115 | `hisirti` | 0.45 | hap yazısı |
| 146 | `tik` | 0.50 | `YouTube` |

`zamanlar.json` en az: `fps` 30, `kare`, `sure`, `t_bas`, `cagri_satir`, her olayın `[yerel_bas, sure]` çifti (adlı), `olaylar`.

## 5. Ekran metni (tam liste; başka yazı YOK)
`@ydspublishing` (kanal) · `Simple Present vs Present Continuous` · `YDT · TEMEL` · `Bu sadece başlangıç.` · `@ydspublishing` (hap) ·
`YouTube` · altyazı 2 parçası. Yasak: `Tam ders`, `tam ders`, `dakika`, süre sözü, `izle`, QR, emoji. Satır ≤ 24 karakter
(altyazı hariç).

## 6. Kabul ölçütü (agy kendi kendine koşmaz; şef ölçer)
1. `/usr/bin/python3 uret.py && /usr/bin/python3 olay.py` hatasız; `zamanlar.json` `cagri_satir` = 2; `olaylar.json` 5 olay.
2. `grep -ciE "tam ders|dakika" proje/index.html` → 0.
3. `index.html` içinde `id="kunye"` altında `id="kanal"` ve `id="logoimg"` var; `#kunye` öğelerinde `opacity:0` ve tween yok.
4. Kapı `araclar/cakisma-kapisi.mjs` 0 uyarı; künye/kanal × içerik, yazı × kapak görseli çakışması yok.
5. Kare 0 (21,33): kanal + künye tam görünür. Kare 104 (24,82): kapak + giriş sözü + altyazı. Kare 208 (28,28): kapak + giriş sözü +
   hap + `YouTube`, altyazı yok. Koyu karede koyu kapak (`kapakK`) görünür.
