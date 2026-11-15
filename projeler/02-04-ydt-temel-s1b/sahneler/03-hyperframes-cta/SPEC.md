# SPEC v2 — 02-04-ydt-temel-s1 sahne 03 Çağrı (HyperFrames, DİKEY 1080×1920, huni v2) · 15.11.2026

Kök: K = `/home/sef/01dev/_worktrees/kalem-0204`. Sahne dizini: S = `K/projeler/02-04-ydt-temel-s1/sahneler/03-hyperframes-cta`.
Bağlayıcı standart: `/home/sef/01dev/dijital-anlatim/.claude/docs/huni-v2-standart.md` (§1, §2). Eski (v1) kod yedeği:
`/home/sef/Silinecekler/2026-11-15-huni-v2/02-04-ydt-temel-s1/sahneler/03-hyperframes-cta/v1/` (yalnız okunur kalıp kaynağı).

İki dosya yazılır, iki ayrı agy koşusu:
- A: `S/yardim.py` (v2 künye + kanal katmanı + v2 altyazı/karaoke). Taban: S'deki var olan `yardim.py`.
- B: `S/uret.py` (baştan; yeni içerik). Kalıp: v1 yedeğindeki `uret.py`.
İki dosya bu belgedeki API ile birbirine bağlanır (§A.6). Başka dosyaya dokunma. Silme yok. Test, render, git yok.

Genel kurallar (ikisi için): Python 3, type hint zorunlu, 2 boşluk değil var olan dosyanın girintisi (4 boşluk) korunur, satır ≤ 120.
Renkler HER ZAMAN koyu taban değerleriyle yazılır (`Y.RENK`): `ortak/hf_tema.py` CSS öznitelik seçicileriyle açık temaya çevirir.
Eşleme (değiştirme): `fill="#f3efe6"` → murekkep · `stroke="#f3efe6"` → murekkep · `stroke="#f2a93b"` → vurgu ·
`rect fill="#f2a93b"` → vurguDolgu (`#ffe066` açık) · `text fill="#1b1a17"` → pilMetin (`#1b2440` açık).
Ekranda yasak sözler: "Tam ders", "dakika", "kanal", "izle", QR, emoji. Çip YOK. Saat simgesi YOK.

---

## A. `S/yardim.py` (var olan dosyayı değiştir)

Korunacaklar (dokunma): `AD`, `ORTAK`, `FONT`, `W`, `H`, `RENK`, `LOGO_EN_BOY`, `LOGO_KAYMA`, `_FONT_DOSYA`, `_font`, `genislik`,
`font_css`, `font_kopyala`, `_sayilar`, `yol_uzunluk`, `_etiket`, `peeps`, `tabler`, `altyazi_cumleleri`, `zemin_html`, `ZEMIN_CSS`,
`cizgi_zamanlari`. Dosya başı docstring'ine tek satır ekle: `huni v2 (15.11): kanal katmanı + v2 bantları (BRIEF-S1 "Kanal katmanı").`

Silinecek/yerine geçecekler: `HUD`, `DERS`, `ROZETLER`, `rozet_konumlari`, `cip_olcu`, `kunye_svg`, `altyazi_satirlari`, `altyazi_svg`.

### A.1 Sabitler (değerler `BRIEF-S1.md` "Kanal katmanı" ve "Yerleşim" tablosundan birebir; başka değer yazma)
```
HUD = {"kenar": 60, "sagSinir": 960,
       "kanalLogoX": 53.2, "kanalLogoY": 291, "kanalLogoYuk": 48, "kanalLogoEn": 193.5,
       "kanalYaziX": 263, "kanalYaziTaban": 330, "kanalYazi": 42,
       "konuTaban": 420, "konuEnBuyuk": 34, "konuEnKucuk": 28,
       "rozetY": 386, "rozetH": 48, "rozetYazi": 26, "rozetAra": 20, "rozetDolgu": 20,
       "icerikBas": 460, "icerikSon": 1380,
       "altyaziBas": 1400, "altyaziSon": 1550, "altyaziYazi": 44, "altyaziSatir": 56,
       "altyaziMerkez": 510, "altyaziEn": 900}
KONU = "Simple Present vs Present Continuous"
ROZETLER = ("YDT · TEMEL",)
KANAL_YAZI = "@ydspublishing"
```
`rozetDolgu` = rozet yazısının iki yanındaki iç boşluk (BRIEF'te değer yok; 20 seçildi, RAPOR'a açık nokta olarak girer).

### A.2 `konu_boyu() -> int`
34'ten 28'e 1'er azalarak ilk uyan boyu döndür: `kenar + genislik("Fredoka", 700, KONU, boy) + rozetAra + rozet_hap_eni() <= sagSinir`.
Hiçbiri uymazsa 28. (Ölçüm: 34 px'te konu 584,6 px, rozet hapı 203,6 px → sağ uç 868 → 34 döner.)
`rozet_hap_eni() -> float` = `genislik("Lexend", 700, ROZETLER[0], rozetYazi) + 2 * rozetDolgu`.

### A.3 `rozet_konumlari() -> list[tuple[float, float]]`
`x = kenar + genislik("Fredoka", 700, KONU, konu_boyu()) + rozetAra`; her rozet için `(x, genislik(Lexend 700, m, 26) + 2*rozetDolgu)`,
sonraki rozet `x += w + 12` (şu an tek rozet).

### A.4 `kunye_svg(cip: str | None = None) -> str`
`cip` parametresi geriye uyum için kalır, KULLANILMAZ (çip çizilmez). Çıktı tam olarak bu yapıdadır (sıra önemli):
```
<g id="kunye">
  <g id="kanal">
    <image id="logoimg" href="assets/logo.svg" x="53.2" y="291" width="193.5" height="48"/>
    <text id="kanal-yazi" x="263" y="330" font-family="Lexend" font-weight="700" font-size="42" fill="#f3efe6">@ydspublishing</text>
  </g>
  <text id="ku-konu" x="60" y="420" font-family="Fredoka" font-weight="700" font-size="<konu_boyu()>" fill="#f3efe6">Simple Present vs Present Continuous</text>
  <g id="rz0">
    <rect x="<x>" y="386" width="<w>" height="48" rx="24" fill="#f2a93b"/>
    <text x="<x + w/2>" y="419" text-anchor="middle" font-family="Lexend" font-weight="700" font-size="26" fill="#1b1a17">YDT · TEMEL</text>
  </g>
</g>
```
Sayılar `HUD`'dan okunur (yukarıdaki sayılar sonuçtur, kodda sabit yazılmaz). Rozet yazı tabanı = `rozetY + rozetH/2 + 9`.
Kanal öğeleri: opaklık 1, `style` yok, sınıf yok, animasyon yok. `#logoimg` kimliği `hf_tema.py` canlı tema geçişi içindir (değiştirme).
Kanal ve künye `#kunye` içinde kalır: çakışma kapısı (`araclar/hf-kutu.mjs`) `#kunye` altındaki her şeyi tür `kunye` sayar.

### A.5 Altyazı + karaoke (y 1400–1550, x 60–960)
`altyazi_satirlari(metin: str) -> list[str]`: Lexend 500 44, satır genişliği ≤ `altyaziEn` (900); sözcük sözcük sar; en çok 2 satır
(fazlası 2. satıra eklenir; var olan kural).

`altyazi_svg(t_bas: float, sure: float, liste: list[dict]) -> tuple[str, list[list], list[list]]`:
- `liste = altyazi_cumleleri(liste)` (var olan işlev).
- Parça açılış/kapanış kuralı var olan işlevle AYNI: `ac = max(0, t0 - 0.05 - t_bas)`; `son = t1 + 0.35`, sonraki parça varsa
  `min(son, sonraki.t0 - 0.05)`; `kapat = son - t_bas`; `kapat <= 0` ya da `ac >= sure` ise parça atlanır; kapanış `min(kapat, sure)`.
- Satır tabanı: 1 satır → `altyaziBas + 84` (1484); 2 satır → `altyaziBas + 56` ve `+ 56 + altyaziSatir` (1456, 1512).
- Her satır `<text>`: `text-anchor="start"`, `x = altyaziMerkez - satirEni/2` (satirEni = `genislik("Lexend", 500, satir, 44)`),
  `font-family="Lexend" font-weight="500" font-size="44" fill="#f3efe6" style="font-kerning:none"` (tarayıcı ölçümü fontTools ile aynı olsun).
- Grup: `<g id="al<i>" style="opacity:0">` satırlar + karaoke çizgileri `</g>`.
- Karaoke (Nadir 03.11: okunan sözcük sakin sarı altçizgi; ölçek ve renk değişmez): parçanın her sözcüğü için bir
  `<line id="ak<i>_<j>" x1 y1 x2 y2 stroke="#f2a93b" stroke-width="6" stroke-linecap="round" style="opacity:0"/>`.
  `x1 = satır x + genislik(satırın sözcükten önceki kısmı + boşluk)`, `x2 = x1 + genislik(sözcüğün sondaki .,:;!? atılmış hâli)`;
  `y1 = y2 = satır tabanı + 12`.
- Sözcük zamanı: `ORTAK/anlatim/sozcukler.json` içinden `p["t0"] - 0.05 <= w["t0"] < p["t1"] + 0.05` olanlar, sırayla; sözcük sayısı
  parçanın sözcük sayısına eşit değilse o parçada karaoke çizgisi ÜRETİLMEZ (altyazı yine çıkar).
  Çizgi açılışı (yerel) `w.t0 - t_bas`; kapanışı sonraki sözcüğün `t0 - t_bas`; son sözcükte `min(w.t1 - t_bas + 0.25, parçanın
  yerel kapanışı)`. Hepsi `round(…, 3)`.
- Dönüş: `(svg, zaman, karaoke)`; `zaman = [["al<i>", ac, kapat], …]`, `karaoke = [["ak<i>_<j>", ac, kapat, uzunluk], …]` (yerel sn;
  uzunluk = x2 - x1).
- Uyarı: satır x aralığı 60–960 dışına çıkarsa `assert` ile dur.

### A.6 B'nin kullandığı API (özet)
`Y.RENK`, `Y.HUD`, `Y.genislik`, `Y.font_css()`, `Y.ZEMIN_CSS`, `Y.zemin_html()`, `Y.font_kopyala(dizin)`, `Y.kunye_svg()`,
`Y.altyazi_svg(t_bas, sure, liste) -> (svg, zaman, karaoke)`.

---

## B. `S/uret.py` (baştan yaz)

Kalıp kaynağı: `/home/sef/Silinecekler/2026-11-15-huni-v2/02-04-ydt-temel-s1/sahneler/03-hyperframes-cta/v1/uret.py`.
Oradan alınacak: dosya iskeleti (satır 1–28: `AD`, `sys.path`, `import yardim as Y`, `PAKET`, `SAH`, `T_BAS`, `KARE`, `SURE`),
`T()` / `E()` işlevleri (satır 30–46; assert'li), HTML iskeleti (satır 335–345: `<style>` içinde `Y.font_css()` + `Y.ZEMIN_CSS` +
`#sahne{position:absolute;left:0;top:0;}`, `#root` öznitelikleri, `Y.zemin_html()`, tek `<svg id="sahne">`, `<defs>`),
JS deseni (satır 399–481: `gsap.timeline({paused:true})`, `ac()`, altyazı aç/kapa döngüsü, `gsap.set(svgOrigin)` + `fromTo`,
`window.__timelines["main"] = tl`), `__main__` bloğu (satır 485–493).
Alınmayacak: bütün v1 içerik metinleri ve olayları (`üç`, `farktan`, `Tam ders:`, bant, ev, bavul, saat, `dört buçuk dakikada`,
`BAVUL`, `ikon_yollari`, `CIP`), sabit saniye.

### B.1 Zaman (tek kaynak; sabit saniye yazma)
- `SAH` = `PAKET/"zaman.json"` → `sahneler[]` içinde `klasor == AD.name` (t_bas 25.49, kare 218). `SURE = round(KARE / 30, 4)` (7.2667).
- `SOZ` = `PAKET/"ortak/anlatim/sozcukler.json"` içinde `cumle == 4` (8 sözcük). Baştan doğrula (assert):
  `[(0,"Gerisi"), (1,"bizde"), (2,"Dersin"), (3,"tamamı"), (4,"YDS"), (5,"Publishing"), (6,"YouTube"), (7,"kanalında")]`.
- `ALT` = `PAKET/"ortak/anlatim/altyazi.json"` içinde YALNIZ `cumle == 4` olan parçalar (2 parça). Cümle 3 parçası bu sahnede çıkmaz.
- `yerel(t) = round(t - T_BAS, 3)`; kare = `round(yerel * 30)`.
- Kapak dosyaları: `PAKET/"ortak/kapak/ana-kapak.png"` ve `ana-kapak-koyu.png` var olmalı; yoksa `SystemExit("ana kapak bekliyor: …")`.
  (Dosyaları `proje/assets/`'e `calistir.sh` kopyalar; uret.py kopyalamaz.)

### B.2 Olay listesi
| Olay (zamanlar.json anahtarı) | Başlangıç (küresel) | Yerel sn (kare) | Süre · ease | Çapa |
|---|---|---|---|---|
| `kart_giris` kapak kartı: ölçek 0.94→1 (svgOrigin kart merkezi), opaklık 0→1 | `T_BAS` (25.49) | 0.00 (0) | ölçek 0.50 `power3.out`; opaklık 0.25 `power2.out` | sahne başı; 26,04'ten önce biter |
| `gerisi_giris` `Gerisi` kinetik (y +24→0, opaklık) | `T(0,"Gerisi")` 26.04 | 0.55 (17) | 0.22 `back.out(1.6)` | Gerisi |
| `bizde_giris` `bizde.` kinetik | `T(1,"bizde")` 26.52 | 1.03 (31) | 0.22 `back.out(1.6)` | bizde. |
| `hap_giris` `@ydspublishing` hapı (ölçek 0.9→1, svgOrigin hapın sol-orta noktası, opaklık) | `T(4,"YDS")` 28.51 | 3.02 (91) | 0.30 `back.out(1.6)` | YDS |
| `youtube_giris` `· YouTube` (x −12→0, opaklık) | `T(6,"YouTube")` 29.63 | 4.14 (124) | 0.30 `power3.out` | YouTube |
| kuyruk durgun | `E(7,"kanalında")` 30.83 → sahne sonu | 5.34–7.27 | tween yok | — |
Altyazı: `Y.altyazi_svg(T_BAS, SURE, ALT)` → `#al<i>` aç/kapa (`tl.set` opaklık 1 / 0) + karaoke çizgisi her sözcükte
(`tl.set` opaklık 1 ac anında; `tl.fromTo` strokeDashoffset uzunluk→0, 0.15 sn, `power2.out`, ac anında; `tl.set` opaklık 0 kapat anında;
çizgiye `strokeDasharray = uzunluk + " " + (uzunluk + 2)`).
Ses olayları (`zamanlar.json` "olaylar", `[yerel_sn, tur, guc]`; `olay.py` ilk/son 12 kareyi yasaklar → kare 12 ≤ k < 206):
`[0.40, "vurus", 0.6]` (kart oturur) · `[gerisi, "tik", 0.4]` · `[hap, "tik", 0.6]` · `[youtube, "tik", 0.4]`.
`zamanlar.json` ayrıca: `fps`, `kare`, `sure`, `t_bas`, her olay anahtarı `[yerel_bas, sure]`, ve `olay_listesi`:
`[{"olay", "kare", "yerel", "kuresel", "sozcuk"}]` (RAPOR tablosu için).

### B.3 Yerleşim (px; içerik bandı 460–1380, x 60–960)
| Öğe | Yazı · boy | Konum | Renk (koyu taban) |
|---|---|---|---|
| `#gerisi` `Gerisi` · `#bizde` `bizde.` (iki ayrı `<text>`, aynı taban) | Fredoka 700 · `G_BOY` = 96 (900 px'e sığmazsa 1'er küçült; assert ≥ 64) | x 60; `bizde.` x = 60 + genislik(Fredoka 700, "Gerisi ", G_BOY); taban 560 (yazı ≈ 489–560, bant 470–590) | `#f3efe6` |
| `#kart` kapak kartı | — | x 60, y 620, 900×506 (16:9) | — |
| ↳ `<clipPath id="kart-kirp"><rect x=60 y=620 width=900 height=506 rx=24/></clipPath>` | | `<defs>` içinde | |
| ↳ `<image id="kapakimg" href="assets/ana-kapak.png" x=60 y=620 width=900 height=506 preserveAspectRatio="xMidYMid slice" clip-path="url(#kart-kirp)"/>` | | | |
| ↳ kenar `<rect x=62 y=622 width=896 height=502 rx=22 fill="none" stroke="#f3efe6" stroke-width=4/>` (dış kenar tam 60–960 / 620–1126) | | | murekkep |
| `#hap` = `<rect>` + `<text>` `@ydspublishing` | Lexend 700 · 56 | rect x 60, y 1160, en = genislik(Lexend 700, "@ydspublishing", 56) + 2×28, boy 80, rx 40; yazı ortalı (`text-anchor="middle"`), taban 1220 | rect `#f2a93b`, yazı `#1b1a17` |
| `#yt` `· YouTube` | Lexend 700 · 56 | x = 60 + hap eni + 18, taban 1220; sağ uç ≤ 960 (assert) | `#f3efe6` |
| `#kunye` | — | `Y.kunye_svg()` (kanal + künye; 0. kareden son kareye, animasyonsuz) | — |
| `#altyazi` | — | `<g id="altyazi">` + `Y.altyazi_svg` svg'si | — |
SVG sırası: defs → `#kart` → `#gerisi`, `#bizde` → `#hap`, `#yt` → `#kunye` → `#altyazi`.
Başlangıç durumları `style="opacity:0"` (kart, gerisi, bizde, hap, yt); `#kunye` opaklığı hiç değişmez.
Tek vurgu: yalnız `@ydspublishing` hapı (+ karaoke altçizgisi aynı renk). Yeşil, kırmızı, emoji yok.

### B.4 Tema uyumlu kapak (`hf_tema.py` logo geçişi gibi `href` değişimi)
`gsap` betiğinden önce ayrı küçük `<script>` (IIFE): iki dosyayı önceden yükle (`new Image().src = …`), sonra
`k()` = `#root` sınıfında `tema-acik` varsa `#kapakimg` href → `assets/ana-kapak.png`, yoksa `assets/ana-kapak-koyu.png`;
`k()` hemen çağrılır + `new MutationObserver(k).observe(root, {attributes: true, attributeFilter: ["class"]})`.
(Render'da sınıf dosyaya gömülüdür → doğru dosya; canlı önizlemede `hf_tema.py` sınıfı değiştirir → gözlemci href'i değiştirir.)

### B.5 Kabul ölçütü (B yazarı kendisi koşmaz; şef doğrular)
- `/usr/bin/python3 S/uret.py` hatasız; `proje/index.html` ve `zamanlar.json` yazılır; `olay.py` assert'i geçer.
- `grep -niE 'tam ders|dakika'` sahne HTML/JS/PY dosyalarında boş (yorum satırları dahil; bu iki söz kodda hiç geçmez).
  "kanal" sözü ekranda metin olarak yok (kimlik `kanal`, `kanal-yazi` serbest).
- Bütün içerik x 60–960, y 460–1380; altyazı 1400–1550; 0–280 ve 1570–1920 boş.
- `#kunye` (kanal dahil) her karede opaklık 1.
