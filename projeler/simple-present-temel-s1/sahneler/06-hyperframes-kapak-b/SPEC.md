# SPEC — simple-present-temel-s1 · sahne 06-hyperframes-kapak-b (huni v2; HyperFrames, 1080×1920, tek kare, ses yok)

Yazan: şef (15.11.2026, istem D-S1 06-hyperframes-kapak-b). Tasarım verir; tam kod yok.
K = `/home/sef/01dev/_worktrees/kalem-0204`. D = `K/projeler/simple-present-temel-s1/sahneler/06-hyperframes-kapak-b/`.
P = `K/projeler/simple-present-temel-s1/`. Bağlayıcı: `/home/sef/01dev/dijital-anlatim/.claude/docs/huni-v2-standart.md` §1, §2, §6;
`P/BRIEF-S1.md` "Kanal katmanı" + "Kapak"; `P/uretim-tutanagi/kapak-taslak.md` §4 (jüri K1); `kapak-standardi.md` (çıkartma kenarı, daire).

## 1. Dosyalar

| Dosya | İş |
|---|---|
| `D/uret.py` | **agy koşusu.** Baştan yazılır: `/home/sef/01dev/_worktrees/kalem-0204/projeler/simple-present-temel-s1/sahneler/06-hyperframes-kapak-b/uret.py` |
| `D/yardim.py`, `D/calistir.sh`, `D/olay.py`, `D/zamanlar.json` | DOKUNMA (şef kurdu) |
| `D/nesneler.json`, `D/proje/index.html`, `D/proje/assets/{karakter,nesne}.png`, `D/proje/assets/fonts/` | uret.py yazar |

Kopyalanacak emsal kod: `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s1/sahneler/05-hyperframes-kapak-b/uret.py`.
Oradan alınacak kalıp: iskelet ve okuma (satır 1–33), `alfa_kutusu`, `maske`, `bos_mu`, `maske_kutusu` (71–98), `gorsel_kopyala`
(101–108; iki görsel için genelleştir: `gorsel_kopyala(kaynak: Path, hedef_dizin: Path)` → `hedef_dizin / kaynak.name`), `gorsel_img`
(111–117; `id`, `src`, kaynak boyutu parametre), `.kenar` filtresi (573–578), `kesisim`, `kurallari_dogrula` yapısı (452–555),
HTML şablonu ve zaman çizelgesi (580–608), `__main__` (614–638). Balon, düşünce izi, `hesapla_yerlesim`, `sahne_svg` ALINMAZ.

## 2. Okuma ve sabitler

- `AD`, `sys.path.insert(0, str(AD))`, `import yardim as Y`, `PAKET = AD.parent.parent`, `ORTAK = PAKET / "ortak"`.
- `zaman.json`: `duragan` içinde `klasor == AD.name` TEK kayıt, `kare == 1`, `cikti == "kapak-b.png"`; `sahneler[]` içinde `AD.name` YOK (assert).
- `zamanlar.json`: `sure` 1.0 · `kare` 1 · `fps` 30 (assert). Anlatım, sözcük, altyazı dosyası OKUNMAZ.
- Renkler (sabit; Y.RENK'ten değil): `SARI = "#fece00"`, `SIYAH = "#141414"`, `KREM = "#f3efe6"`.
- Bant: `X0, X1 = 60, 960` · `KANAL_Y = (280, 350)` · `KUNYE_Y = (360, 450)` · `BASLIK_Y = (470, 900)` · `GORSEL_Y = (920, 1380)`.
- Başlık: `SATIRLAR = ("FİİLE -S", "HANGİ ÖZNEYLE?")`, yedek `YEDEK = ("-S HANGİ", "ÖZNEYLE?")` · `UST_SINIR = 190` · `ALT_SINIR = 64` ·
  `PX = 0.16` (kutu yatay payı, ×S) · `UST = 0.93` (İ/Ö noktası üstü, ×S; Fredoka yMax 921/928 ÷ 1000) · `ARA = 0.18` (satır 1 tabanı → kutu üstü) ·
  `KUTU_UST = 1.05` (kutu üstü → satır 2 tabanı) · `KUTU_ALT = 0.24` (satır 2 tabanı → kutu altı) · `RX = 0.10`.
- Görsel: `KARAKTER = ORTAK / "kapak" / "karakter.png"` (896×1200), `NESNE = ORTAK / "kapak" / "nesne.png"` (1200×896) · `ESIK = 64` ·
  `KENAR_PX = 10` · `KENAR_GECIS = 3` · `KAR_KUTU = (152, 89, 744, 1113)` · `NES_KUTU = (96, 254, 1057, 643)` (ikisi `alfa_kutusu` ile assert) ·
  `BAS_X = 462` (PNG'de baş ortası) · `PARMAK = (154, 715)` (PNG'de işaret parmağı ucu) · `DAIRE_R = 220` · `NESNE_EN = 360` · `NESNE_ARA = 24`.

## 3. Yerleşim (y = yazı tabanı ya da kutu, px)

```
y    0 ┌──────────────────────────────────────────────┐ zemin (açık #fece00 · koyu #141414)
   291 │ [logo 193,5×48] @ydspublishing                │ kanal 280–350 (Y.kunye_svg)
   386 │ (YDT · TEMEL)  ← çerçeveli hap, x 60           │ künye 360–450
  ≈558 │ FİİLE -S                                      │ başlık bloğu, 470–900'de dikey orta
  ≈676 │ ┌HANGİ ÖZNEYLE?───────────────────────────┐   │ satır 2 kutuda (S ≈ 106)
  ≈812 │ └─────────────────────────────────────────┘   │
   930 │                      ( krem daire r 220 )     │ görsel 920–1380
       │   [otobüs 360] ◄──☝ karakter (sağ, bel üstü) │
  1370 │                                               │
  1380 └──── 1380–1920 boş (altyazı yok) ─────────────┘
```

### 3.1 Kanal + künye
`Y.kunye_svg(konu=False, cerceve=True)` aynen; uret.py künyeye kendi değer yazmaz. Çıktı: `#kanal` (logo `#logoimg` x 53,2 y 291
193,5×48 + `#kanal-yazi` Lexend 700 42 x 263 taban 330) ve `#rz0` (hap x 60–263,6, y 386–434, 3 px çerçeve, `YDT · TEMEL` Lexend 700 26).
Logo dosyası `calistir.sh` yazar (açık: tek renk #141414; koyu: `yds-publishing-seffaf.svg`).

### 3.2 Başlık — `<g id="baslik">`
1. `S` hesabı: `w1 = Y.genislik("Fredoka", 700, s1, 100)`, `w2 = Y.genislik(…, s2, 100)`;
   `S = floor(min(UST_SINIR, 900·100 / w1, 900·100 / (w2 + 2·PX·100)))`. S ile yeniden ölç; `g1 ≤ 900`, `g2 + 2·PX·S ≤ 900` değilse S−1 (döngü).
   `S < ALT_SINIR` ise `YEDEK` satırlarla yeniden hesapla; yine `< 64` ise `AssertionError`. Beklenen: SATIRLAR, `S = 106`.
2. Blok yüksekliği `bh = (UST + ARA + KUTU_UST + KUTU_ALT)·S`; blok üstü `by = 470 + (430 − bh) / 2`.
   `T1 = by + UST·S` · kutu üstü `ky0 = T1 + ARA·S` · `T2 = ky0 + KUTU_UST·S` · kutu altı `ky1 = T2 + KUTU_ALT·S`.
   Beklenen (S 106): by 557,8 · T1 656,4 · ky0 675,5 · T2 786,8 · ky1 812,2.
3. Yatay: sola yaslı. `bs-1` x 60; `bk-kutu` x 60, genişlik `g2 + 2·PX·S` (≈ 892,7); `bs-2` x `60 + PX·S`.
4. Öğeler (sıra): `<text id="bs-1">` s1 · `<rect id="bk-kutu" rx=RX·S>` · `<text id="bs-2">` s2. Fredoka 700, `font-size` S,
   `style="font-kerning:none"`, `xml:space="preserve"`. Üç öğede `fill` özniteliği YOK (renk §5 CSS'ten). Kontur yok.
5. Glif denetimi: s1 + s2'deki her karakter Fredoka 700 `latin` ya da `latin-ext` cmap'inde var (`Y._font("Fredoka", 700, bolge).getBestCmap()`); assert.

### 3.3 Görsel — HTML öğeleri (SVG dışı), sıra: daire → nesne → karakter
- Karakter ölçeği `s = floor(436 / (1113 − 89) · 1000) / 1000` (= 0,425; görünür yükseklik 933 … 1368).
  `kx = (960 − DAIRE_R) − BAS_X·s` (baş ortası daire ortasında, x 740) · `ky = 933 − 89·s`. Beklenen: kx 543,6 · ky 895,2; görünür x 608–860, y 933–1368.
  Şef QA tur 1 (15.11): ilk sürüm 440 / 930 idi (s 0,429); krem kenar + yumuşak alfa saçta maskeden 13 px taştı, karede üst y 917 (bant 920).
- Daire: `<div id="kb-daire" class="abs" style="left:520px;top:930px;width:440px;height:440px">` (merkez 740, 1150; r 220).
  Yalnız açık temada görünür (§5). İçinde öğe yok.
- Nesne ölçeği `sn = round(NESNE_EN / (1057 − 96), 4)` (= 0,3746). Parmak ucu ekranda `px = kx + 154·s`, `py = ky + 715·s` (≈ 607,9, 1198,5).
  Nesne görünür sağı `px − 2·KENAR_PX − NESNE_ARA`; `nx = o değer − 1057·sn`; görünür dikey orta parmak hizasında: `ny = py − (254 + 643)/2·sn`.
  Beklenen: nx 168,0 · ny 1030,5; görünür x 204–564, y 1126–1271. Yön: otobüs PNG'deki gibi (sağa, karaktere doğru); çevirme yok.
- `<img id="nesne" class="abs kenar" src="assets/nesne.png">` ve `<img id="karakter" class="abs kenar" src="assets/karakter.png">`,
  `left/top/width/height` px (`gorsel_img` kalıbı). Sıra: `Y.zemin_html()` → `<div id="kb-zemin"></div>` → daire → nesne → karakter → `<svg id="sahne">`.
- `.kenar` filtresi emsalle aynı: `KENAR_GECIS` × 4 yön `drop-shadow(±adım px 0 0 KREM)` / `drop-shadow(0 ±adım px 0 KREM)`, `adım = KENAR_PX / KENAR_GECIS`.
  İki temada krem kalır.

## 4. SVG
`<svg id="sahne" width="1080" height="1920" viewBox="0 0 1080 1920">` içinde yalnız `{kunye}{baslik}`. Başka öğe yok.

## 5. Tema (hf_tema.py ile uyum)
- `Y.font_css()`, `Y.ZEMIN_CSS`, `Y.zemin_html()` DEĞİŞTİRMEDEN (hf_tema bu dizeleri arar). `#sahne{position:absolute;left:0;top:0;}`.
- uret.py `<style>` içine şu kuralları (bu sırayla) yazar; renk değişkenleri `kb` önekli, hf_tema'nın değişkenleriyle çakışmaz:
  ```
  #root{--kbZemin:#141414;--kbYazi:#f3efe6;--kbKutu:#fece00;--kbKutuYazi:#141414;--kbDaire:#f3efe6;}
  #root.tema-acik{--kbZemin:#fece00;--kbYazi:#141414;--kbKutu:#141414;--kbKutuYazi:#f3efe6;}
  #kb-zemin{position:absolute;inset:0;background:var(--kbZemin);}
  #kb-daire{border-radius:50%;background:var(--kbDaire);display:none;}
  #root.tema-acik #kb-daire{display:block;}
  #root #kanal-yazi,#root #rz0 text,#root #bs-1{fill:var(--kbYazi);}
  #root #rz0 rect{stroke:var(--kbYazi);}
  #root #bk-kutu{fill:var(--kbKutu);}
  #root #bs-2{fill:var(--kbKutuYazi);}
  ```
  Gerekçe: `#root #…` (özgüllük 2,0,x) hf_tema'nın `#root [fill="#f3efe6"]` (1,1,0) kuralını geçer. `#kb-zemin` gren ve vinyeti örter (düz zemin, ana kapak gibi).
- Sonuç: açık = sarı zemin, siyah yazı, siyah kutuda krem satır 2, krem daire · koyu = #141414 zemin, krem yazı, sarı kutuda siyah satır 2, daire yok.

## 6. Kurallar ve kabul ölçütü (uret.py içinde `assert`)
1. Bloklar (x, y, w, h): `kanal` (x 60, y 291, sağ = 263 + genişlik(`@ydspublishing`, Lexend 700, 42), alt 339) · `kunye` (rozet hapı: x 60,
   y 386, w = `Y.rozet_konumlari(False)[0][1]`, h 48) · `baslik` (x 60, y `by`, sağ = max(60 + g1, kutu sağı), alt `ky1`) · `bk-kutu` ·
   `daire` (520, 930, 440, 440) · `nesne` ve `karakter` (`maske_kutusu(maske(...))` ± KENAR_PX).
2. `kanal` ⊂ x [60, 960] × y [280, 350]; `kunye` ⊂ x [60, 960] × y [360, 450]; `baslik`, `bk-kutu` ⊂ x [60, 960] × y [470, 900];
   `daire`, `nesne`, `karakter` ⊂ x [60, 960] × y [920, 1380]. Böylece 0–280, 1380–1920 ve sağ 960–1080 boş.
3. Kesişim 0: `kanal`–`kunye`, `kanal`–`baslik`, `kunye`–`baslik`, `baslik`–`daire`, `baslik`–`nesne`, `baslik`–`karakter`.
   `bos_mu(m_karakter, nesne görünür kutusu, 2·KENAR_PX + 4)` True (otobüs ve kenarı karaktere değmez).
4. `S ≥ 64`. Başlık 2 satır; sözcük sayısı 4 (yedekte 3); her satır ≤ 24 karakter.
5. Görünen metin taraması: bütün `<text>` içerikleri (regex `>([^<]+)</text>`). Küçük harfe çevrilmiş metinde YOK: `"tam" + " ders"`,
   `"dak" + "ika"` (parçalı yaz; istem grep'i koruma listesini ekran metni saymasın), `izle`, `qr`, `"you" + "tube"`, `abone`.
   Birleşik metinde (büyük harf) `ALIR` YOK ve `re.search(r"ÖZNE(?!YLE)", …)` boş (jüri K1: eski `HANGİ ÖZNE` / `-S ALIR?` yasak).
   Görünen metinde U+2FFF üstü karakter (emoji) YOK.
6. Bütün HTML'de (küçük harf) YOK: `math.random`, `date.now`, `new date`, `opacity:0`. HTML'deki her `#rrggbb` değeri
   {`#1b1a17` (ZEMIN_CSS), `#f3efe6`, `#fece00`, `#141414`} kümesinde. `id="kanal"`, `id="logoimg"`, `id="kb-daire"`, `id="bk-kutu"` TAM bir kez;
   `id="ku-konu"` YOK.
7. Yasak: kırmızı, yeşil, gradyan (zemin vinyeti dışında), gölge (kenar filtresi dışında), try/except, tween (tek `set` dışında). Python: tür
   ipuçları bütün işlevlerde.
8. Zaman çizelgesi emsalle aynı: `tl.set("#sahne", {opacity: 1, immediateRender: false}, 0)` ve `…, Z["sure"])`; `window.__timelines["main"]`.
   `#root` öznitelikleri emsalle aynı (`data-composition-id="main"`, `data-duration` = `Z["sure"]`, 1080×1920, fps 30).
9. `nesneler.json`: `[{"ad", "x", "y", "w", "h"}]` tam sayı; sıra kanal, kunye, baslik, bk-kutu, daire, nesne, karakter.
10. `/usr/bin/python3 uret.py` stdout: `index.html yazıldı <bayt>` ve `S=<S> s=<s> sn=<sn> kx=<kx> nx=<nx> satir=<ana|yedek>`; çıkış 0.

Kabul (şef koşturur, ajan koşturmaz): `bash calistir.sh --tema acik|koyu` → `P/kapak-b.png` ve `D/k/koyu/kapak-b-koyu.png` 1080×1920;
taşma, kesik yazı, üst üste binme yok; kanal katmanı görünür; 0–280, 1380–1920 ve x 960–1080 boş.
