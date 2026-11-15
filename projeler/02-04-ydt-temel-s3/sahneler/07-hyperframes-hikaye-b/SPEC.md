# SPEC v2 — 02-04-ydt-temel-s3 · sahne 07-hyperframes-hikaye-b (hikâye B, soru + cevap) · huni v2

Yazan: şef (15.11.2026, istem D-V2-S3). Kod yazmaz; tasarım verir. K = `/home/sef/01dev/_worktrees/kalem-0204`.
Sahne dizini D = `K/projeler/02-04-ydt-temel-s3/sahneler/07-hyperframes-hikaye-b/`. Paket P = `K/projeler/02-04-ydt-temel-s3/`.
Bağlayıcı: `/home/sef/01dev/dijital-anlatim/.claude/docs/huni-v2-standart.md` §2, §6 · `P/BRIEF-S3.md` "Yerleşim" + "Hikâye karesi B".
v1 yedeği: `~/Silinecekler/2026-11-15-huni-v2/02-04-ydt-temel-s3/sahneler-v1/07-hyperframes-hikaye-b/`.

Durağan kare: ses yok, altyazı yok, zaman çizelgesi 1,0 sn (yakalama 0,5 sn), kare 1. Zaman çizelgesi dışı (`zaman.json` → `duragan`).
Olay listesi YOK (`olaylar.json` = `[]`, `olay.py` değişmez). Küresel sn ve sözcük çapası bu sahneye uygulanmaz.
Metin kaynağı: kural özeti = anlatım cümle 3 ikinci yarısı ("Tren tarifeye uyar: geniş zaman.", 11,51–15,99); cümle kartı = cümle 1
ilk parçası (ekranda `İzmir` noktalı, `7 pm` rakamla). v1'den fark: cevap karede açık (A doğru şık yeşil); v1 çağrı satırı kalkar.

## 1. Dosyalar

| Dosya | Durum | İş |
|---|---|---|
| `D/uret.py` | VAR (v1) | **YERİNDE YENİDEN YAZ** — mutlak yol `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s3/sahneler/07-hyperframes-hikaye-b/uret.py` |
| `D/yardim.py` | VAR (v1 HUD) | DOKUNMA; yalnız `Y.genislik`, `Y.font_css`, `Y.font_kopyala`, `Y.ZEMIN_CSS`, `Y.zemin_html`, `Y.RENK`, `Y.LOGO_EN_BOY`, `Y.LOGO_KAYMA`. `Y.kunye_svg`, `Y.HUD`, `Y.rozet_konumu`, `Y.cip_olcu` KULLANILMAZ (v1) |
| `D/calistir.sh`, `D/olay.py`, `D/zamanlar.json` | VAR | DOKUNMA (şef düzenler) |
| `D/nesneler.json`, `D/proje/index.html` | uret.py yazar | §9 |

Başka dosyaya dokunma. Silme yok. Test, render, snapshot, `calistir.sh`, git YOK.

## 2. Kalıp kaynakları (salt oku)

| Kalıp | Mutlak yol | Ne alınır |
|---|---|---|
| v2 iskelet (en yakın örnek; aynı paket, aynı v2 yerleşim) | `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s3/sahneler/04-hyperframes-hikaye/uret.py` | Satır 1–35 düzeni (shebang, docstring, importlar, `AD`, `sys.path` + `import yardim as Y`, `PAKET`, `Z`, `R`); `_kutu`, `TREN` (satır 36–56), `_kutusu`, `_daire_yolu`, `ikon_yollari` (satır 83–146) **BİREBİR**; `HUD`, `KONU`, `ROZET`, `konu_boyu`, `rozet_konumlari`, `kunye_svg` (satır 148–217) **BİREBİR**; `kaydet_svg` kalıbı (satır 370–382; y değerleri §7'ye göre değişir); `kesisim`; `uret()` HTML kabuğu (satır 590–620: `font_css`, `ZEMIN_CSS`, `#sahne text{font-kerning:none;}`, `#root` data-* öznitelikleri, `Y.zemin_html()`, tek `<svg id="sahne">`, iki `tl.set`, `window.__timelines["main"]`); `__main__` (satır 625–646). `BILET`, `_bilet`, `bas_svg`, `hesapla_s_ve_bas`, `esitdegil-stil`, `ust` ALINMAZ |
| v1 saat çizimi | `D/uret.py` (v1, şu anki dosya) `saat_svg` (satır 108–127) | parça listesi (kadran, 4 çentik, yelkovan 12, akrep 7 = 210°, göbek); merkez ve r §5.3'e göre, çizgi kalınlıkları §5.3 |
| v1 doğrulama | `D/uret.py` (v1) satır 17–33 | `zaman.json` → `duragan` içinde `klasor == AD.name` kaydı, `kare == 1`, `cikti == "hikaye-b.png"`, `AD.name` `sahneler[]` içinde YOK; `zamanlar.json` `sure` 1,0 · `kare` 1 · `fps` 30 |
| sarı altçizgi kalıbı | `K/projeler/02-04-ydt-temel-s3/sahneler/05-hyperframes-kapak-b/uret.py` satır 236–237 | `<path id="alti" d="M… Q… …" fill="none" stroke=R["vurgu"] stroke-width="10" stroke-linecap="round"/>` |

v1'den TAŞINMAYAN: `kunye_svg` çağrısı (`Y.kunye_svg(cip)`), `CIP_METIN` / `kunye.js` okuması, `KENAR = 48`, `SAG = 1032`, `ICERIK`, `CAGRI`,
`PLATFORM`, büyük tren (`tren_svg`, ölçek 1,2), `cg1`, `cg2`, `hap` (Caveat çağrı + alt `@ydspublishing` hapı), `Cevap tam derste`, `profildeki bağlantı`.

## 3. Renk ve tema (`P/ortak/hf_tema.py` ile)

Kaynak renkler koyu temadır; `hf_tema.py` açık temaya çevirir.
- Yazı/çizgi mürekkep `R["murekkep"]` (`#f3efe6` → açıkta `#1b2440`); ince detay `R["ikincil"]` (`#c9c2b3` → `#5a6275`).
- Künye rozeti: `rect fill=R["vurgu"]` (→ açıkta `--vurguDolgu` `#ffe066`), yazı `text fill=R["zemin"]` (→ `--pilMetin` `#1b2440`). `id="rz1"` YASAK; grup `rz0`.
- `leaves` altçizgisi: `stroke=R["vurgu"]` (→ açıkta `--vurgu` `#d9900f`, koyuda `#f2a93b`). Karedeki TEK sarı içerik öğesi budur (+ künye rozeti, standart parça).
- Doğru şık YEŞİL: hf_tema yeşil tanımaz → sahne `<style>` içine yerel kural yaz:
  `#root .dogru{stroke:#3a9a6a}` ve `.tema-acik #sahne .dogru{stroke:#167a4a}` (`#root.tema-acik` dizgisi YASAK: hf_tema onu görünce dönüştürmeyi atlar). Yeşil öğeler `class="dogru"` + `stroke="#3a9a6a"` özniteliği
  (koyu tema değeri). Yeşil yalnız şık A çerçevesi ve ✓ çizgisi. `fill` yeşil YOK.
- Kırmızı (`R["kirmizi"]`), gradyan, gölge, emoji YOK. `#1b1a17` dolgulu `<circle>` YOK.

## 4. Yerleşim (1080×1920; bütün sayılar px; y = yazı tabanı)

| Bant (y) | Öğe | Kimlik | Değer |
|---|---|---|---|
| 0–280 | boş | — | yalnız zemin |
| 291–339 | kanal katmanı | `<g id="kunye"><g id="kanal">` | 04 `kunye_svg` BİREBİR (logo `#logoimg` x 53,15 y 291 w 193,49 h 48 · `#kanal-yazi` `@ydspublishing` Lexend 700 42, x 263, taban 330) |
| 386–434 | künye | `#ku-konu`, `#rz0` | 04 `kunye_svg` BİREBİR (konu Fredoka 700 `konu_boyu()` = 34, x 60, taban 420 · rozet `YDT · BASIC` Lexend 700 26). Çip YOK |
| 460–560 | soru | `#soru` | §5.1 |
| 580–760 | cümle kartı | `#kart` | §5.2–5.3 |
| 780–900 | şıklar | `#sA`, `#sB` | §6 |
| 920–1060 | kural özeti | `#kural` | §7.1 |
| 1070–1140 | kaydet satırı | `#kaydet` | §7.2 |
| 1150–1380 | bağ çıkartması yeri | — | yalnız zemin: boş kutu, çerçeve, ok, "buraya" yazısı ÇİZME |
| 1400–1920 | boş | — | altyazı YOK |

Yatay: içerik x 60–960; sağ şerit x 960–1080'e öğe girmez. Sol hizalı kolon.

## 5. Soru + cümle kartı

### 5.1 Soru `Tarife mi, plan mı?`
`S_SORU = min(96, floor(900 / (genislik(Fredoka 700, SORU, 100) / 100)))` (beklenen 96; genişlik 795,2 → sağ 855,2).
`<text id="soru" x="60" y="532" font-family="Fredoka" font-weight="700" font-size="{S_SORU}" fill=R["murekkep"] xml:space="preserve">`.
Kutu: üst `532 − 0.73·S`, alt `532 + 0.221·S` (beklenen 461,9–553,2). Sarı YOK.

### 5.2 Kart çerçevesi + iki satır
- `<rect id="kart-crv" x="62" y="582" width="896" height="176" rx="28" fill="none" stroke=R["murekkep"] stroke-width="4"/>` (dış kenar 60–960 × 580–760).
- Satır 1: `<text id="kart-s1" x="88" y="655" Fredoka 700 64 fill=murekkep xml:space="preserve">The train to İzmir</text>`
  (`İ` U+0130; kutu üst `655 − 0.921·64` = 596,1; genişlik 507,1 → sağ 595,1).
- Satır 2: `<text id="kart-s2" x="88" y="730" Fredoka 700 64 fill=murekkep xml:space="preserve">leaves at 7 pm today.</text>`
  (kutu alt `730 + 0.229·64` = 744,7; genişlik 617,3 → sağ 705,3). `7 pm` rakamla.
- `leaves` altçizgisi (kapak-b kalıbı): `LW = genislik(Fredoka 700, "leaves", 64)` (190,2).
  `<path id="alti" d="M{88 − 4} 741 Q{88 + LW/2} 746 {88 + LW + 4} 738" fill="none" stroke=R["vurgu"] stroke-width="10" stroke-linecap="round"/>`.
  Kutu: x 79–287,2, y 733–751. Kart iç alanında kalır (y ≤ 754).

### 5.3 İkonlar (sağda bir sütun: üstte tren, altında saat)
- Tren (04 `TREN` + `ikon_yollari`): `ikon_yollari(TREN, mx=842, my=625, en=180, boy=64)` → kutu ≈ 752–932 × 594–656.
  Renk ve kalınlık 04 `kart_svg` tren kalıbı: son parça (ray) ikincil 3 · `ince` parçalar mürekkep 3 · diğerleri mürekkep 4.
  `<g id="kart-tren" fill="none" stroke-linecap="round" stroke-linejoin="round">`.
- Saat (v1 `saat_svg` parçaları): merkez `(842, 712)`, `r = 34`. Kadran `circle fill="none"` mürekkep 4 · 4 çentik (12, 3, 6, 9;
  0,66·r → 0,80·r) mürekkep 3 · yelkovan `(cx, cy) → (cx, cy − 0.66·r)` mürekkep 4 · akrep `(cx, cy) → (cx + sin210°·0.5·r, cy − cos210°·0.5·r)`
  mürekkep 5 (saat 7, sarı DEĞİL) · göbek `circle r 3.5 fill=murekkep`. Rakam YOK. `<g id="kart-saat" stroke-linecap="round">`.
  Kutu (çizgi payıyla) ≈ 805,6–878,4 × 675,6–748,4.

## 6. Şıklar (bant 780–900; yan yana, aynı ölçü)

| Öğe | Şık A (`#sA`, doğru) | Şık B (`#sB`, soluk) |
|---|---|---|
| grup | `<g id="sA">` | `<g id="sB" opacity="0.4">` |
| çerçeve `rect` (`-crv`) | x 63, y 782, w 432, h 116, rx 24, `fill="none"`, `class="dogru"` `stroke="#3a9a6a"` `stroke-width="6"` | x 524, y 782, w 434, h 116, rx 24, `fill="none"`, `stroke=R["murekkep"]` `stroke-width="4"` |
| harf dairesi `circle` (`-daire`) | cx 120, cy 840, r 38, `fill="none"`, mürekkep 4 | cx 582, cy 840, r 38, `fill="none"`, mürekkep 4 |
| harf `text` (`-harf`) | `A`, x 120, taban 862, `text-anchor="middle"`, Fredoka 700 64, mürekkep | `B`, x 582, aynı biçim |
| şık yazısı `text` (`-yazi`) | `TARİFE`, x 176, taban 865, Fredoka 700 72, mürekkep (`İ` U+0130; genişlik 245,5 → sağ 421,5) | `PLAN`, x 638, taban 865, Fredoka 700 72, mürekkep |
| kalem ✓ `path` (`-tik`) | `d="M437 842 L451 857 L476 826"`, `fill="none"`, `class="dogru"` `stroke="#3a9a6a"` `stroke-width="8"`, linecap/linejoin round (kutu ≈ 433–480 × 822–861) | YOK |

- Dış kenarlar: A 60–498 (çizgi 6: 63 − 3 … 495 + 3), B 522–960. Aradaki boşluk ≥ 20.
- `✓` (U+2713) karakteri HTML'de YOK; yalnız çizgi. `text-transform` YOK (elle büyük harf).
- Şık A yazısı ve harfi mürekkep (okunurluk); yeşil yalnız çerçeve + ✓.

## 7. Kural özeti + Kaydet

### 7.1 Kural özeti (bant 920–1060; çerçeve YOK, sarı YOK)
- `<g id="kural">`: satır 1 `<text id="kural-s1" x="60" y="970" font-family="Lexend" font-weight="500" font-size="64" fill=murekkep>Tren tarifeye uyar:</text>`
  (kutu üst `970 − 0.782·64` = 920; genişlik 590,5).
- Satır 2 `<text id="kural-s2" x="60" y="1043" font-family="Lexend" font-weight="700" font-size="64" fill=murekkep>geniş zaman.</text>`
  (kutu alt `1043 + 0.246·64` = 1058,7; genişlik 431,7). Vurgu yalnız ağırlıkla (700); renk YOK.

### 7.2 Kaydet satırı (bant 1070–1140, x 60'tan; 04 kalıbı, y kaydırılmış)
- Yer imi (SVG yol, emoji DEĞİL): `<path id="kaydet-imi" d="M63 1078 Q63 1074 67 1074 H103 Q107 1074 107 1078 V1134 L85 1118 L63 1134 Z"
  fill="none" stroke=R["murekkep"] stroke-width="5" stroke-linejoin="round"/>` (dış kenar ≈ 60,5–109,5 × 1071,5–1136,5). Sarı dolgu YOK.
- `<text id="kaydet-yazi" x="131" y="1122" font-family="Fredoka" font-weight="700" font-size="64" fill=murekkep>Kaydet</text>`
  (kutu 1075,4–1136,7; sağ 338,9). `<g id="kaydet">` = simge + yazı.

## 8. SVG sırası ve CSS

SVG sırası: `kunye` (kanal + konu + rozet) → `soru` → `kart` (crv, tren, saat, s1, s2, alti) → `sA` → `sB` → `kural` → `kaydet`.
`<style>`: `Y.font_css()`, `Y.ZEMIN_CSS`, `#sahne{position:absolute;left:0;top:0;}`, `#sahne text{font-kerning:none;}`,
`#root .dogru{stroke:#3a9a6a}`, `.tema-acik #sahne .dogru{stroke:#167a4a}` (`#root.tema-acik` dizgisi YASAK: hf_tema onu görünce dönüştürmeyi atlar). Tween, opacity animasyonu, transform YOK (tek kare; iki `tl.set`).
`data-duration` = `Z['sure']`.

## 9. Blok kutuları, nesneler.json ve iç kurallar (`kurallari_dogrula`, assert)

Bloklar (sıra; nesneler.json bu listeden yuvarlanır, alanlar `ad,x,y,w,h`, `indent=2`):
`kanal` {60, 291, 263 + genislik(Lexend 700 "@ydspublishing", 42) − 60, 48} · `kunye` {60, 386, rozet sağ − 60, 48} ·
`soru` {60, 532 − 0.73·S, genişlik, (0.73 + 0.221)·S} · `kart` {60, 580, 900, 180} · `sA` {60, 779, 438, 122} · `sB` {522, 780, 438, 120} ·
`kural` {60, 920, max(590,5; 431,7), 1058,7 − 920} · `kaydet` {60.5, 1071.5, 338.9 − 60.5, 1136.7 − 1071.5} ·
iç öğeler (çakışma listesine girmez, yalnız kart içi denetim + nesneler.json): `tren`, `saat`, `alti`, `tik`.

Kurallar:
1. Her blok: `x ≥ 60 − 1e-4`, `x + w ≤ 960 + 1e-4`, `y ≥ 280`, `y + h ≤ 1140 + 1e-4` (1150–1920'de öğe yok).
2. Bant içi: kanal ⊂ [280, 350] · kunye ⊂ [360, 450] · soru ⊂ [460, 560] · kart ⊂ [580, 760] · sA, sB ⊂ [778, 902] · kural ⊂ [920, 1060] · kaydet ⊂ [1070, 1140].
3. Ana bloklar kesişmez (alan 0); dikey komşu boşluğu ≥ 10; `sA`–`sB` yatay boşluk ≥ 20.
4. Kart içi (çerçeve iç alanı x 64–956, y 584–756): `kart-s1`, `kart-s2`, `alti`, `tren`, `saat` kutuları bu alanda; `kart-s1` sağ ≤ tren sol − 24;
   `kart-s2` sağ ≤ saat sol − 24; tren alt ≤ saat üst − 10; `kart-s1` alt (taban + 0.02·64) ≤ `kart-s2` üst (taban − 0.73·64) − 10; `alti` üst ≥ 730 + 2.
5. Şık içi: daire sağı + 12 ≤ yazı solu; A: yazı sağı + 10 ≤ ✓ sol, ✓ sağ ≤ 496 − 10; B: yazı sağı ≤ 958 − 24.
6. İçerik yazı boyu ≥ 64: soru S ≥ 64, kart 64, harf 64, şık 72, kural 64, kaydet 64. Kanal 42 ve künye 28–34 standart ölçüsü (muaf).
7. Ekran satırları ≤ 24 karakter: `@ydspublishing`, `YDT · BASIC`, `Tarife mi, plan mı?`, `The train to İzmir`, `leaves at 7 pm today.`,
   `TARİFE`, `PLAN`, `Tren tarifeye uyar:`, `geniş zaman.`, `Kaydet`. Künye satırı `Simple Present vs Present Continuous` (36) standart ölçüsü: listede `muaf` notuyla.
8. Üretilen HTML'de şu dizgiler YOK (büyük/küçük harf duyarsız): `tam ders`, `dakika`, `Full lesson`, `profildeki`, `Cevap`, `font-family="Caveat"`
   (font-face tanımı serbest), `✓`, `id="altyazi"`, `id="rz1"`, `kirmizi`, `#e0473b`. Büyük/küçük harf DUYARLI: `Izmir` YOK; `İzmir` ve `7 pm` VAR.
   Emoji yok: HTML'de U+1F000 üstü karakter yok.
9. Tür ipuçları bütün işlevlerde; 4 boşluk girinti (04 düzeni).

## 10. Kabul ölçütü

1. `/usr/bin/python3 D/uret.py` hatasız biter; stdout `index.html yazıldı N` ve `S_SORU=96`; nesneler.json 12 kayıt (8 blok + 4 iç öğe).
2. §9 kuralları assert ile koşar (hepsi geçer).
3. HTML'de `#kanal` içinde tam 1 `image` (`#logoimg`) + 1 `text` (`@ydspublishing`); `#kunye` içinde konu + rozet; altyazı öğesi yok.
4. Şef `calistir.sh --tema acik|koyu` ile tek kare çeker ve PNG'ye bakar (agy render/snapshot KOŞMAZ).
