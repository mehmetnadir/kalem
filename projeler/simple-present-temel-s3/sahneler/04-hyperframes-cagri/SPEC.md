# SPEC v2 — simple-present-temel-s3 sahne 04 Çağrı (HyperFrames, DİKEY 1080×1920, huni v2) · 15.11.2026

Kök: K = `/home/sef/01dev/_worktrees/kalem-0204`. Sahne dizini: S = `K/projeler/simple-present-temel-s3/sahneler/04-hyperframes-cagri`.
Paket: P = `K/projeler/simple-present-temel-s3`. Bağlayıcı standart: `/home/sef/01dev/dijital-anlatim/.claude/docs/huni-v2-standart.md`
(§1, §2). Paket belgesi: `P/BRIEF-S3.md` ("Sahne içeriği" 18,10–25,08 satırları).

Yazılacak tek dosya: `S/uret.py` (baştan; yeni dosya). Başka dosyaya dokunma. Silme yok. Test, render, git yok.
S'de hazır olanlar (dokunma): `yardim.py` (emsal v2 kopyası, `KONU = "Simple Present"`), `olay.py`, `calistir.sh`, `nesneler.json`.

Genel kurallar: Python 3, type hint zorunlu, 4 boşluk girinti, satır ≤ 120. Sabit saniye YAZMA (zaman sözcük çapasından).
Renkler HER ZAMAN koyu taban değerleriyle yazılır (`Y.RENK`): `ortak/hf_tema.py` CSS öznitelik seçicileriyle açık temaya çevirir.
Eşleme: `fill="#f3efe6"` → murekkep · `stroke="#f3efe6"` → murekkep · `stroke="#f2a93b"` → vurgu · `rect fill="#f2a93b"` → vurguDolgu
(`#ffe066` açık) · `text fill="#1b1a17"` → pilMetin (`#1b2440` açık). Başka renk yok (kırmızı, yeşil yok).
Ekranda yasak sözler: "Tam ders", "dakika", "kanal", "izle", QR, emoji. Bu iki söz ("tam ders", "dakika") kodda yorum dahil hiç geçmez.
Çip YOK. Saat simgesi, oynat/izle düğmesi, YouTube logosu taklidi YOK. Figür YOK.

---

## 1. Kalıp kaynakları (yalnız okunur)

| Ne | Dosya · satır | Alınacak |
|---|---|---|
| İskelet | `K/projeler/02-04-ydt-temel-s1/sahneler/03-hyperframes-cta/uret.py` 1–82 | docstring, `AD`, `sys.path`, `import yardim as Y`, `PAKET`, `SAH`, `T_BAS`, `KARE`, `SURE`, kapak `SystemExit` kontrolü, `SOZ`, `ALT`, `R`, `yerel()`, `T()`, `E()`, beklenen sözcük assert'i |
| HTML iskeleti | aynı dosya 193–236 | `<style>` (`Y.font_css()`, `Y.ZEMIN_CSS`, `#sahne`), `#root` öznitelikleri, `Y.zemin_html()`, tek `<svg id="sahne">`, `<defs>` + `kart-kirp` clipPath, `#kapakimg` image |
| Tema uyumlu kapak | aynı dosya 237–253 | IIFE: iki dosyayı önceden yükle, `tema-acik` → `assets/ana-kapak.png`, yoksa `assets/ana-kapak-koyu.png`, MutationObserver (birebir al) |
| JS deseni | aynı dosya 254–302 | `gsap.timeline({paused:true})`, `ac()`, altyazı aç/kapa döngüsü, karaoke döngüsü, `fromTo` + `immediateRender:false`, `gsap.set(svgOrigin)`, `window.__timelines["main"] = tl` |
| `__main__` | aynı dosya 307–314 | font kopyası, `index.html` + `zamanlar.json` yazımı |
| Kalem çerçeve | `K/projeler/simple-present-temel-s3/sahneler/03-hyperframes-kaydet/uret.py` 353–361 | `getTotalLength()` + `strokeDasharray = L + " " + (L + 2)` + `strokeDashoffset` L→0, `sine.inOut` |
| Konuşma balonu yolu | `K/projeler/simple-present-temel/sahneler/06-hyperframes-form/uret.py` 102–110 | `konusma_balonu(x, y, w, h, ty)` işlevini birebir kopyala (type hint ekle; yol biçimi aynı kalır) |
| Altyazı kuralları | `S/yardim.py` 216–340 (`altyazi_satirlari`, `altyazi_cumleleri`, `altyazi_svg`) | parça aç/kapa kuralı, karaoke sözcük eşleme kuralı, dönüş biçimi (aşağıda §4 farklarla) |

Alınmayacak: emsalin içerik metinleri (`Gerisi`, `bizde.`), `kart_giris` sahne başı girişi, emsalin hap konumu (y 1160).

## 2. Zaman (tek kaynak)

- `SAH` = `P/zaman.json` → `sahneler[]` içinde `klasor == AD.name` (t_bas 18.10, kare 239). `SURE = round(KARE / 30, 4)` (7.9667).
- `SOZ` = `P/ortak/anlatim/sozcukler.json` içinde `cumle == 4` (9 sözcük). Baştan assert (`T(i, bas)` ile, ayrıca `len(SOZ) == 9`):
  `[(0,"Bu"), (1,"sadece"), (2,"başlangıç"), (3,"Dersin"), (4,"tamamı"), (5,"YDS"), (6,"Publishing"), (7,"YouTube"), (8,"kanalında")]`.
- `ALT` = `P/ortak/anlatim/altyazi.json` içinde YALNIZ `cumle == 4` parçaları (2 parça; assert). Cümle 3 parçası bu sahnede çıkmaz.
- `yerel(t) = round(t - T_BAS, 3)`; kare = `round(yerel * 30)`.
- Kapak: `P/ortak/kapak/ana-kapak.png` ve `ana-kapak-koyu.png` yoksa `SystemExit("ana kapak bekliyor: …")` (emsal ile aynı).
  Dosyaları `proje/assets/`'e `calistir.sh` kopyalar; uret.py kopyalamaz.

## 3. Olay listesi (yerel = küresel − 18,10; kare = round(yerel × 30))

| Olay (zamanlar.json anahtarı) | Çapa (küresel) | Yerel sn (kare) | Hareket · süre · ease |
|---|---|---|---|
| `bu_giris` `#bs0` `Bu` | `T(0,"Bu")` 18.65 | 0.55 (16) | opaklık 0→1 + y +24→0 · 0.22 · `back.out(1.6)` |
| `sadece_giris` `#bs1` `sadece` | `T(1,"sadece")` 18.89 | 0.79 (24) | aynı |
| `baslangic_giris` `#bs2` `başlangıç.` | `T(2,"başlangıç")` 19.45 | 1.35 (40) | aynı |
| `kart_cerceve` `#kart-cerceve` kalemle çizilir | `T(3,"Dersin")` 20.56 | 2.46 (74) | strokeDashoffset L→0 · 0.40 · `sine.inOut` |
| `kapak_belir` `#kapakimg` iç görsel | `T(3,"Dersin")` 20.56 | 2.46 (74) | opaklık 0→1 · 0.30 · `power2.out`; sonra sabit |
| `hap_giris` `#hap` `@ydspublishing` | `T(5,"YDS")` 21.84 | 3.74 (112) | opaklık 0→1 + ölçek 0.9→1 (svgOrigin `60 1220`) · 0.30 · `back.out(1.6)` |
| `youtube_giris` `#yt` `· YouTube` | `T(7,"YouTube")` 22.96 | 4.86 (146) | opaklık 0→1 + x −12→0 · 0.30 · `power3.out` |
| `kuyruk_durgun` | `E(8,"kanalında")` 24.16 → sahne sonu | 6.06 (182) → 7.9667 | tween yok |

Bütün öğeler girdikten sonra sahne sonuna kadar yerinde kalır (çıkış yok). `#kunye` (kanal + künye) 0. kareden son kareye opaklık 1,
hiç tween almaz.
Altyazı balonu: §4 → `#al<i>` aç/kapa (`tl.set` opaklık 1 / 0) + karaoke çizgisi her sözcükte (emsal karaoke döngüsü birebir:
`tl.set` opaklık 1 ac anında; `fromTo` strokeDashoffset uzunluk→0 0.15 sn `power2.out`; `tl.set` opaklık 0 kapat anında).
Beklenen parça zamanları: `al0` 0.50–2.41 (`Bu sadece başlangıç.`), `al1` 2.41–6.41 (`Dersin tamamı …`).

Ses olayları (`zamanlar.json` "olaylar", `[yerel_sn, tur, guc]`; `olay.py` 12 ≤ kare < 227 ister):
`[t_bu, "tik", 0.4]` · `[t_dersin, "cizgi", 0.5]` · `[t_hap, "tik", 0.6]` · `[t_yt, "tik", 0.4]`.
`zamanlar.json` ayrıca: `fps`, `kare`, `sure`, `t_bas`, her olay anahtarı `[yerel_bas, sure]` (kuyruk için `[t, SURE - t]`), ve
`olay_listesi`: `[{"olay", "kare", "yerel", "kuresel", "sozcuk"}]` (yukarıdaki 8 satır; RAPOR tablosu için).

## 4. Konuşma balonu altyazısı (y 1400–1550; öğrenci sesi görünür olsun)

uret.py içinde `balon_altyazi(t_bas: float, sure: float, liste: list[dict]) -> tuple[str, list[list], list[list]]` yaz.
`Y.altyazi_svg` ile aynı mantık; yalnız şu farklar:

- Sabitler (uret.py başında): `BALON = {"x": 122, "y": 1404, "h": 142, "ty": 1470, "pay": 40, "satirEn": 760, "yazi": 44,
  "satirAra": 56, "taban1": 1490, "taban2": (1461, 1517)}`.
- `liste = Y.altyazi_cumleleri(liste)`; parça aç/kapa kuralı `Y.altyazi_svg` ile AYNI (`ac = max(0, t0 - 0.05 - t_bas)`,
  `son = t1 + 0.35`, sonraki parça varsa `min(son, sonraki.t0 - 0.05)`, `kapat = son - t_bas`, atlama ve `min(kapat, sure)`).
- Satır sarma: Lexend 500 44, satır eni ≤ `satirEn` (760), sözcük sözcük; en çok 2 satır (`assert len(satirlar) <= 2`).
  Beklenen: `["Bu sadece başlangıç."]` (≈ 455,5) ve `["Dersin tamamı YDS Publishing", "YouTube kanalında."]` (≈ 660,4 / 431,0).
- Balon eni `bw = max(satır eni) + 2 * pay`. Balon yolu `konusma_balonu(BALON["x"], BALON["y"], bw, BALON["h"], BALON["ty"])`
  (§1 kalıbı; kuyruk sol kenarda, ucu x = 122 − 58 = 64).
  Assert: kuyruk ucu ≥ 60 · gövde sağ ucu `x + bw + 4` ≤ 960 · üst `y - 1` ≥ 1400 · alt `y + h + 3` ≤ 1550.
- Balon öğesi: `<path id="ab<i>" d="…" fill="none" stroke="#f3efe6" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>`
  (renk `R["murekkep"]`), grubun İLK çocuğu; balon grupla birlikte açılır/kapanır (ayrı tween yok).
- Satır tabanı: 1 satır → `taban1` (1490); 2 satır → `taban2` (1461, 1517).
- Satır x (balon içinde ortalı, `text-anchor="start"`): `x = BALON["x"] + (bw - satirEni) / 2`;
  `<text>` öznitelikleri emsalle aynı: `font-family="Lexend" font-weight="500" font-size="44" fill="#f3efe6" style="font-kerning:none"`.
- Karaoke çizgisi `Y.altyazi_svg` ile aynı kural (sözcük eşleme `p.t0 - 0.05 <= w.t0 < p.t1 + 0.05`, sayı tutmazsa çizgi yok;
  `x1/x2` sözcük ölçüsü, sondaki `.,:;!?` atılır; `y = taban + 12`; `stroke="#f2a93b" stroke-width="6" stroke-linecap="round"
  style="opacity:0"`; id `ak<i>_<j>`; açılış `w.t0 - t_bas`, kapanış sonraki sözcüğün `t0 - t_bas`, son sözcükte
  `min(w.t1 - t_bas + 0.25, parça kapanışı)`; hepsi `round(…, 3)`).
- Grup: `<g id="al<i>" style="opacity:0">` balon + satırlar + karaoke çizgileri `</g>`.
- Dönüş: `(svg, [["al<i>", ac, kapat], …], [["ak<i>_<j>", ac, kapat, uzunluk], …])` (yerel sn).

## 5. Yerleşim (px; içerik bandı 460–1380, x 60–960)

| Öğe | Yazı · boy | Konum | Renk (koyu taban) |
|---|---|---|---|
| `#bs0` `Bu` · `#bs1` `sadece` · `#bs2` `başlangıç.` (3 ayrı `<text>`, aynı taban) | Fredoka 700 · `G_BOY`: 96'dan 1'er küçült, `60 + genislik(Fredoka 700, "Bu sadece başlangıç.", G_BOY) <= 960` olan ilk boy; assert ≥ 64 (beklenen 96) | x: `bs0` 60 · `bs1` 60 + genislik("Bu ") · `bs2` 60 + genislik("Bu sadece "); taban 560 (yazı ≈ 493–583, bant 470–590); `style="font-kerning:none;opacity:0"` | `#f3efe6` |
| `#kart` grup (opaklık değişmez) | — | x 60, y 620, 900×506 (16:9) | — |
| ↳ `<clipPath id="kart-kirp"><rect x=60 y=620 width=900 height=506 rx=24/></clipPath>` | | `<defs>` içinde | |
| ↳ `<image id="kapakimg" href="assets/ana-kapak.png" x=60 y=620 width=900 height=506 preserveAspectRatio="xMidYMid slice" clip-path="url(#kart-kirp)" style="opacity:0"/>` | | | |
| ↳ `<rect id="kart-cerceve" x=62 y=622 width=896 height=502 rx=22 fill="none" stroke="#f3efe6" stroke-width=4 stroke-linecap="round" stroke-linejoin="round"/>` (dış kenar tam 60–960 / 620–1126) | | çizim öncesi strokeDashoffset = L (görünmez); JS ilk satırlarda ayarlar | murekkep |
| `#hap` = `<rect>` + `<text>` `@ydspublishing` | Lexend 700 · 56 | rect x 60, y 1180, en = genislik(Lexend 700, "@ydspublishing", 56) + 2×28, boy 80, rx 40; yazı ortalı (`text-anchor="middle"`, x = 60 + en/2), taban 1240 | rect `#f2a93b`, yazı `#1b1a17` |
| `#yt` `· YouTube` | Lexend 700 · 56 | x = 60 + hap eni + 18, taban 1240; sağ uç ≤ 960 (assert) | `#f3efe6` |
| `#kunye` | — | `Y.kunye_svg()` (kanal + künye; animasyonsuz) | — |
| `#altyazi` | — | `<g id="altyazi">` + `balon_altyazi` svg'si | — |

SVG sırası: defs → `#kart` → `#bs0..2` → `#hap`, `#yt` → `#kunye` → `#altyazi`.
Başlangıç durumları `style="opacity:0"`: `bs0..2`, `kapakimg`, `hap`, `yt`. `#kart-cerceve` opaklığı 1 kalır, görünmezliği dash ile.
Tek vurgu: yalnız `@ydspublishing` hapı (+ karaoke altçizgisi aynı renk).

## 6. Kabul ölçütü (yazar kendisi koşmaz; şef doğrular)

- `/usr/bin/python3 S/uret.py` hatasız; `S/proje/index.html` ve `S/zamanlar.json` yazılır; `olay.py` assert'i geçer.
- `grep -niE 'tam ders|dakika'` uret.py ve index.html'de boş. "kanal" sözü ekranda metin olarak yok (kimlik `kanal`, `kanal-yazi` serbest).
- Bütün içerik x 60–960, y 460–1380; balon 1400–1550; 0–280 ve 1570–1920 boş; sağ 960–1080 boş.
- `#kunye` (kanal dahil) her karede opaklık 1. Koyu temada `#kapakimg` href `assets/ana-kapak-koyu.png`.
