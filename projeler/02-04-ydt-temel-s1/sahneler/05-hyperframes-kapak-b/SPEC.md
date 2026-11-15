# SPEC v2 — 02-04-ydt-temel-s1 · sahne 05-hyperframes-kapak-b (huni v2; HyperFrames, 1080×1920, tek kare, ses yok)

Yazan: şef (15.11.2026, istem D-V2 `uretim-tutanagi/istem/sahne-v2/D-05-hyperframes-kapak-b.md`). Tasarım verir; tam kod yok.
K = `/home/sef/01dev/_worktrees/kalem-0204`. D = `K/projeler/02-04-ydt-temel-s1/sahneler/05-hyperframes-kapak-b/`. P = `K/projeler/02-04-ydt-temel-s1/`.
Bağlayıcı: `/home/sef/01dev/dijital-anlatim/.claude/docs/huni-v2-standart.md` §1, §2, §6; `kapak-standardi.md` §2 (çıkartma kenarı).
v1 SPEC yedeği: `~/Silinecekler/2026-11-15-huni-v2/02-04-ydt-temel-s1/sahneler/05-hyperframes-kapak-b/SPEC.md`.

## 0. v1 → v2 farkı

| Öğe | v1 | v2 |
|---|---|---|
| Üst bant | logo 48–144, rozet 216–288 | 0–280 BOŞ; kanal katmanı 280–350; künye 360–450 |
| Künye | yalnız rozet `YDT · BASIC` (36 px) | konu `Simple Present vs Present Continuous` + rozet (yardim.py `kunye_svg()`) |
| Görsel | doodle öğretmen figürü + zemin çizgisi | `P/ortak/kapak/karakter.png` + 10 px krem çıkartma kenarı; zemin çizgisi YOK |
| Başlık | 952 px'e sığan boy, orta x 540 | 888 px'e sığan boy, orta x 510 (içerik bandı 60–960) |
| Balon | x 360–1032 (sağ 960–1080 doluydu) | x `bx0`–960, yükseklik 140 |
| Yasak taraması | bütün HTML'de "kanal" | yalnız görünen `<text>` içeriğinde (id `kanal` serbest) |

## 1. Dosyalar

| Dosya | İş |
|---|---|
| `D/yardim.py` | **agy koşusu 1.** §2'deki ekleme. Başka satır değişmez |
| `D/uret.py` | **agy koşusu 2.** Baştan yazılır (`/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s1/sahneler/05-hyperframes-kapak-b/uret.py`) |
| `D/calistir.sh`, `D/olay.py`, `D/zamanlar.json`, `D/cizim/` | DOKUNMA |
| `D/nesneler.json`, `D/proje/index.html`, `D/proje/assets/karakter.png`, `D/proje/assets/fonts/` | uret.py yazar |

Başka dosyaya dokunma. Silme yok. Test, render, git YOK. `P/ortak/`, `P/zaman.json`, başka sahneler salt okunur.

## 2. yardim.py (agy koşusu 1)

Kaynak: `K/projeler/02-04-ydt-temel-s1/sahneler/01-hyperframes-kapak/yardim.py` (sahne 01, v2'ye çevrilmiş).
1. Satır 1 docstring ilk satırı: `"""02-04-ydt-temel-s1 sahne 05 kapak B; huni v2 (15.11): kanal katmanı + künye satırı + v2 bantları (BRIEF-S1 "Kanal katmanı").`
2. `D/yardim.py` satır 147 (`# ---- künye ...`) ile satır 194 (`return '<g id="kunye">' + ders + rz + chip + logo + '</g>'`) ARASI (dahil)
   silinir; yerine sahne 01 `yardim.py` satır 147–257 bloğu BİREBİR konur: `HUD` (kenar 60, sagSinir 960, kanalLogoX 53.2,
   kanalLogoY 291, kanalLogoEn 193.5, kanalLogoYuk 48, kanalYaziX 263, kanalYaziTaban 330, kanalYaziBoy 42, konuX 60, konuTaban 420,
   konuBoyUst 34, konuBoyAlt 28, rozetY 386, rozetH 48, rozetAra 20, rozetYazi 26, rozetPay 20, icerikBas 460, icerikSon 1380,
   altyaziBas 1400, altyaziSon 1550, altyaziYazi 44, altyaziSatir 56, altyaziOrta 510, altyaziGen 900), `KONU`, `KONU_PARCA`, `ROZET`,
   `KANAL_YAZI`, `rozet_genislik()`, `konu_boyu()`, `rozet_konumu()`, `kunye_svg()` (argümansız; `<g id="kunye">` içinde
   `<g id="kanal">` (`<image id="logoimg" href="assets/logo.svg" …>` + `<text id="kanal-yazi">`) + `<g id="ku-konu">` + `<g id="rz0">`).
3. Eski `DERS`, `cip_olcu()`, eski `rozet_konumu()` kalkar. Satır 195'ten sonrası (`altyazi_satirlari` … `cizgi_zamanlari`) AYNEN kalır.

## 3. uret.py — okuma ve sabitler

- İskelet v1 ile aynı (yedek `uret.py`): `AD`, `sys.path` + `import yardim as Y`, `PAKET = AD.parent.parent`, `ORTAK = PAKET / "ortak"`.
- `zaman.json`: `duragan` içinde `klasor == AD.name` TEK kayıt, `kare == 1`, `cikti == "kapak-b.png"`; `sahneler[]` içinde `AD.name` YOK (assert).
- `zamanlar.json`: `sure` 1.0 · `kare` 1 · `fps` 30 (assert). Anlatım, sözcük, altyazı dosyası OKUNMAZ.
- Renk yalnız `Y.RENK` (`zemin #1b1a17`, `murekkep #f3efe6`, `ikincil #c9c2b3`, `vurgu #f2a93b`). `KREM = Y.RENK["murekkep"]`.
- Bant sabitleri: `X0, X1 = 60, 960` · `XC = 510` · `Y0, Y1 = 460, 1380` · `KANAL_Y = (280, 350)` · `KUNYE_Y = (360, 450)`.
- Başlık: `BASLIK_GEN = 888` (900 − 2 × 6 kontur payı) · `BAS_UST = 480` (satır 1 kutu üstü).
- Karakter: `KARAKTER = ORTAK / "kapak" / "karakter.png"` (896×1200 RGBA) · `ESIK = 64` · `KENAR_PX = 10` · `KENAR_GECIS = 3` · `PAY = 24` ·
  `BAS_SATIR = 300` (PNG'de saçın sağ üst bölgesi; düşünce izinin çıkış satırı, göz ölçümü) · ölçek adayları 0.60 → 0.40, adım 0.01.
- Balon: `BL1_Y = 864` · `BL_H = 140` · `BL_ARA = 24` → `BL2_Y = 1028` · sağ `BL_X1 = 958` (4 px çizginin dış kenarı 960) · `rx 48` ·
  `IK = 56` (ikon kutusu) · `PAD = 24` · `PAD_SAG = 40` (Caveat `?` glifi ilerleme genişliğini ≈ 10 px aşar) · `IK_ARA = 16`.
- Şef QA (15.11): `BL_X1` 960 → 958, sağ pay `PAD_SAG` 40 (tur 1: `?` kenara 11 px), karakter `kx` + 2 px (tur 2: kenar yumuşatması x 58).

## 4. Yerleşim (y = yazı tabanı ya da kutu, px)

```
y    0 ┌──────────────────────────────────────────────┐
       │                (boş zemin)                    │ 0–280
   291 │ [logo 193,5×48] @ydspublishing                │ kanal 280–350 (Y.kunye_svg)
   420 │ Simple Present vs Present Continuous (YDT·BASIC)│ künye 360–450
   480 │       YAŞI[YOR]UM                             │ başlık, orta x 510
   ≈781│      NASIL DENİR?                             │ (S ≈ 142)
   864 │ ┌karakter┐   o  ┌─[ev]  I live? ──────────┐    │ bl1 864–1004
       │ │ (kenar)│ o    └────────────────────────┘    │
  1028 │ │  ✋  ✋ │O     ┌─[bavul] I am living? ───┐   │ bl2 1028–1168
       │ └────────┘      └────────────────────────┘    │
  1380 ├───────────── karakter alt (kenar dahil) ──────┤ x 60–960 içerik
  1920 └──────────────── boş ─────────────────────────┘ 1380–1920 boş (altyazı yok)
```

### 4.1 Kanal + künye
`Y.kunye_svg()` aynen (argümansız). uret.py künyeye kendi değer yazmaz.

### 4.2 Başlık — `<g id="baslik">` (v1 algoritması, iki değişiklik)
- Parçalar ve ölçüm v1 ile aynı (`YAŞI` · `YOR` · `UM`; `NASIL DENİR?`; kutu payı `p = 0,08·S`; `g1 = wa + 2p + wy + wu`).
- `S = floor(min(190, 888·100/g1_100, 888·100/g2_100))`; S ile yeniden ölç, `g1 ≤ 888`, `g2 ≤ 888` assert.
- Taban: `T1 = BAS_UST + 0,86·S`; `T2 = T1 + 1,26·S`. Yatay: `x1 = XC − g1/2`, `x2 = XC − g2/2`.
- Kutu, renk, kontur, id'ler v1 ile birebir: `bk-kutu` (`<rect fill=vurgu>`, YOR'un ALTINDA), `bs-yasi`, `bs-yor` (`fill` zemin, kontursuz),
  `bs-um`, `bs-2` (`fill` murekkep, `stroke` zemin 12, round, `style="font-kerning:none;paint-order:stroke fill"`). `t2` id YOK.

### 4.3 Karakter — HTML `<img>` (SVG dışı)
Kalıp: `K/projeler/02-04-ydt-temel-dikey/sahneler/90-hyperframes-kapak/uret.py` → `alfa_kutusu`, `maske`, `bos_mu`, `maske_kutusu`,
`gorsel_kopyala` (yalnız KARAKTER; hedef `AD/"proje"/"assets"/"karakter.png"`), `gorsel_img`, `.kenar` filtresi (`html_yaz` içinde `kenar`).
- `ax0, ay0, ax1, ay1 = alfa_kutusu(KARAKTER)` (ölçüm: 21, 173, 878, 1112).
- Ölçek `s` için: `kx = X0 + KENAR_PX + 2 − ax0·s` (görünür sol 72, kenarla 62) · `ky = Y1 − KENAR_PX − ay1·s` (görünür alt 1370, kenarla 1380).
- Öğe: `<img id="karakter" class="abs kenar" src="assets/karakter.png" alt="" style="left:..px;top:..px;width:896·s px;height:1200·s px">`,
  `Y.zemin_html()`'den SONRA, `<svg id="sahne">`'den ÖNCE.
- CSS: `.kenar{filter: …}` = `KENAR_GECIS` × 4 yön `drop-shadow(±adım px 0 0 KREM)` / `drop-shadow(0 ±adım px 0 KREM)`, `adım = KENAR_PX / KENAR_GECIS`
  (90 kapak ile aynı). Kenar rengi iki temada krem kalır (hf_tema CSS dizesine dokunmaz). Krem daire YOK (açık zemin zaten krem).

### 4.4 Ölçek araması (büyükten küçüğe; ilk geçen ölçek seçilir)
Her `s` için sırayla:
1. `m = maske(KARAKTER, kx, ky, s)`; görünür üst `kust = ky + ay0·s`. Şart: `kust − KENAR_PX ≥ baslik_alt + 40` (`baslik_alt = T2 + 0,10·S + 6`).
2. Balon solu: `bx0 = ceil(sağ_kenar + KENAR_PX + PAY)`; `sağ_kenar` = maskenin `[BL1_Y − KENAR_PX − PAY, BL2_Y + BL_H + KENAR_PX + PAY]`
   satırlarındaki en sağ dolu sütun (+1). Balon genişliği `bw = BL_X1 − bx0`.
3. Balon yazısı: `tx = bx0 + PAD + IK + IK_ARA`; `TB = min(88, floor((BL_X1 − PAD_SAG − tx)·100 / Y.genislik("Caveat", 700, "I am living?", 100)))`.
   Şart `TB ≥ 72`. Sonuç (15.11): `s = 0,49`, `bx0 = 525`, `TB = 74`, `S = 142`.
4. Düşünce izi (§4.6) şartları.
Hiçbir `s` geçmezse `AssertionError("yerleşim bulunamadı: …")` (son ölçeğin gerekçeleriyle). Beklenen sonuç `s ≈ 0,52`, `bx0 ≈ 550`.

### 4.5 Balonlar — `<g id="eskiz" fill="none" stroke=murekkep stroke-linecap="round" stroke-linejoin="round">`
| Öğe | Ölçü |
|---|---|
| `<rect id="bl1">` | x `bx0`, y 864, w `bw`, h 140, rx 48, `stroke-width` 4 |
| `<rect id="bl2">` | x `bx0`, y 1028, w `bw`, h 140, rx 48, `stroke-width` 4 |
| `<g id="bl1-ikon">` | `Y.tabler("home")`; `translate(bx0 + PAD, orta_y − IK/2) scale(IK/24)`, `stroke-width = 4 / (IK/24)` |
| `<g id="bl2-ikon">` | `Y.tabler("luggage", AD / "cizim")`; aynı kalıp |
| `<g id="iz">` | §4.6 daireleri |

Balon yazısı (`<text>`, eskiz grubunun DIŞINDA, `fill` murekkep, kontursuz, `xml:space="preserve"`): `bl1-yazi` = `I live?`,
`bl2-yazi` = `I am living?`; Caveat 700, boy TB (iki balonda aynı); x `tx`; taban `orta_y + 0,30·TB` (`orta_y = balon y + 70`).
Sağ kenar `tx + genişlik ≤ BL_X1 − PAD` assert.

### 4.6 Düşünce izi — karakterin başından iki balonun arasına
- `P0`: PNG satırı `BAS_SATIR` → ekran `y = ky + BAS_SATIR·s`; `x` = maskenin o satırdaki en sağ dolu sütunu + `KENAR_PX` + 14.
- `P1 = (bx0 − 12 − 16, (BL1_Y + BL_H + BL2_Y) / 2)`.
- 3 daire `<circle id="dn-1|2|3" fill="none" stroke-width="4">`: (t, r) = (0,10, 8) · (0,45, 12) · (0,85, 16); merkez `P0 + t·(P1 − P0)`.
- Şartlar: `P1.x − P0.x ≥ 60`; her daire için `bos_mu(m, daire kutusu, KENAR_PX + 8)` (karaktere ve kenarına değmez);
  `cx + r ≤ bx0 − 8`; ardışık daireler arası merkez uzaklığı `≥ r_i + r_j + 8`.

## 5. Tema (hf_tema.py ile uyum)
- `Y.ZEMIN_CSS`, `Y.zemin_html()`, `Y.font_css()` DEĞİŞTİRMEDEN. `#sahne{position:absolute;left:0;top:0;}`.
- Renkler SVG özniteliği, küçük harf hex. CSS'te tek renk: `.kenar` filtresindeki KREM.
- `rect fill #f2a93b` → açıkta `#ffe066`; `text fill #1b1a17` → `#1b2440`. `<circle fill=…>`, `<path fill="#1b1a17">` YOK. id `t2`, `ku-nokta`, `rz1` YOK.
- Kanal logosu kimliği `logoimg` (yardim.py); `calistir.sh` tema logosunu `proje/assets/logo.svg` olarak kopyalar.

## 6. Kurallar ve kabul ölçütü (uret.py içinde `assert`)
1. Bloklar (x, y, w, h; kutu payları): `kanal` (x 60, y 291, sağ = 263 + genişlik(`@ydspublishing`, Lexend 700, 42), alt 339) ·
   `kunye` (x 60, y = min(386, 420 − 0,75·konu_boyu), sağ = rozet sağı, alt = max(434, 420 + 0,25·konu_boyu)) ·
   `baslik` (min(x1, x2) − 6 … max(x1+g1, x2+g2) + 6; y `T1 − 0,86·S − 6` … `T2 + 0,10·S + 6`) · `bk-kutu` · `karakter`
   (`maske_kutusu(m)` ± KENAR_PX) · `bl1`, `bl2` (± 2 çizgi) · `bl1-yazi`, `bl2-yazi` (üst `taban − 0,75·TB`, h `1,0·TB`) · `dn-1..3` (± r + 2).
2. `kanal` ⊂ x [60, 960] × y [280, 350]; `kunye` ⊂ x [60, 960] × y [360, 450]; öteki bütün bloklar ⊂ x [60, 960] × y [460, 1380].
   Böylece 0–280 ve 1380–1920 boş, sağ 960–1080 boş.
3. Kesişim 0: `kanal`, `kunye`, `baslik`, `bl1`, `bl2` çiftleri; `baslik` ile `karakter` (kutu); `dn-*` ile `bl1`, `bl2`, `baslik`.
   Karakter ile balon/iz maskeyle (§4.4–4.6). `bl1` alt ile `bl2` üst arası ≥ 24; `baslik` alt ile `bl1` üstü arası ≥ 40.
4. Yazı boyu ≥ 64 (kanal 42 ve künye ≤ 34 / 26 hariç). Başlık 2 satır, toplam 3 sözcük. Her satır ≤ 24 karakter.
5. Görünen metin taraması: bütün `<text>` içerikleri (regex `>([^<]+)</text>`) küçük harfe çevrilir; şu sözler YOK: `tam ders`, `dakika`,
   `izle`, `qr`, `kanal`, `ikisi de`, `kalıcı`, `geçici`. Görünen metinde U+2FFF üstü karakter (emoji) YOK.
6. Bütün HTML'de (küçük harf) YOK: `math.random`, `date.now`, `new date`, `opacity:0`. HTML'deki her `#rrggbb` değeri `Y.RENK`'in
   zemin/murekkep/ikincil/vurgu kümesinde. `id="kanal"` ve `id="logoimg"` TAM bir kez.
7. Yasak: kırmızı, yeşil, gradyan (zemin vinyeti dışında), gölge (kenar filtresi dışında), try/except, tween (tek `set` dışında). Python: tür
   ipuçları bütün işlevlerde.
8. Zaman çizelgesi v1 ile aynı: `tl.set("#sahne", {opacity: 1, immediateRender: false}, 0)` ve `…, Z["sure"])`; `window.__timelines["main"]`.
9. `nesneler.json`: `[{"ad", "x", "y", "w", "h"}]` tam sayı; sıra kanal, kunye, baslik, bk-kutu, karakter, bl1, bl2, bl1-yazi, bl2-yazi, dn-1, dn-2, dn-3.
10. `/usr/bin/python3 uret.py` stdout: `index.html yazıldı <bayt>` ve `S=<S> TB=<TB> s=<ölçek> bx0=<bx0>`; çıkış 0.

Kabul (şef koşturur, ajan koşturmaz): `bash calistir.sh --tema acik|koyu` → `P/kapak-b.png` ve `D/k/koyu/kapak-b-koyu.png` 1080×1920;
taşma, kesik yazı, üst üste binme yok; kanal katmanı görünür; 0–280, 1380–1920 ve x 960–1080 boş.
