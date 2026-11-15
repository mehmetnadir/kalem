# SPEC — 02-04-ydt-temel-s1 · sahne 04-hyperframes-hikaye (HyperFrames, 1080×1920, tek kare, ses yok)

Yazan: şef (15.11.2026). Kod yazmaz; tasarım verir. K = `/home/sef/01dev/_worktrees/kalem-0204`.
Sahne dizini D = `K/projeler/02-04-ydt-temel-s1/sahneler/04-hyperframes-hikaye/`. Paket P = `K/projeler/02-04-ydt-temel-s1/`.
Kaynak: `P/BRIEF-S1.md` "Hikâye karesi" · `P/uretim-tutanagi/hikaye-taslak.md` §3 · `K/projeler/present-continuous-dikey/BRIEF-DIKEY.md` §0, §2, §3.

## 1. Dosyalar

| Dosya | Durum | İş |
|---|---|---|
| `D/uret.py` | YOK | **YAZILACAK** (bu spec; mutlak yol `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s1/sahneler/04-hyperframes-hikaye/uret.py`) |
| `D/yardim.py` | VAR (örneğin birebir kopyası) | DOKUNMA; yalnız içe aktar |
| `D/calistir.sh`, `D/olay.py`, `D/zamanlar.json`, `D/nesneler.json` | VAR (şef yazdı) | `nesneler.json` dışında DOKUNMA; `nesneler.json`'u uret.py yazar (§6) |

Başka dosyaya dokunma. Silme yok. Test, render, snapshot, git yok. `P/ortak/`, BRIEF ve başka sahneler salt okunur.

## 2. Kalıp kaynakları (salt oku)

| Kalıp | Mutlak yol | Ne alınır |
|---|---|---|
| İskelet (aynı motor, dikey) | `K/projeler/present-continuous-ileri-s1/sahneler/03-hyperframes-cta/uret.py` | Dosya düzeni: docstring, `AD`, `sys.path` + `import yardim as Y`, `Z = zamanlar.json`, `R = Y.RENK`, sabitler, `uret()` → `html` dizgisi, `if __name__ == "__main__":` içinde `proje/` + `Y.font_kopyala(...)` + `proje/index.html` yazımı. HTML kabuğu: `Y.font_css()`, `Y.ZEMIN_CSS`, `#sahne` CSS, `<div id="root" data-composition-id="main" data-start="0" data-duration=… data-fps="30" data-width="1080" data-height="1920">`, `Y.zemin_html()`, tek `<svg id="sahne" width="1080" height="1920" viewBox="0 0 1080 1920">`, `lib/gsap.min.js`, `window.__timelines["main"]` kaydı |
| Yardımcılar | `D/yardim.py` | `Y.genislik(aile, agirlik, metin, boy)`, `Y.tabler("home")`, `Y.RENK`, `Y.LOGO_EN_BOY`, `Y.font_css`, `Y.ZEMIN_CSS`, `Y.zemin_html`, `Y.font_kopyala`. `Y.kunye_svg` ve `Y.altyazi_*` KULLANILMAZ (tek satır ders adı ve altyazı yazar; bu sahnede ikisi de yanlış) |
| `ek_ayir` görünümü (yaşı-yor-um) | `K/projeler/02-04-ydt-temel/sahneler/01-hyperframes-giris/uret.py` satır 24–29 ve 63–79 | parça dizilişi: `yaşı` + tire + kutu(`yor`) + tire + `um`; `TIRE_PAY` 0,14 em, `TIRE_ARA` 0,08 em; kutu dolgusu vurgu, kutu üstündeki yazı zemin rengi, tireler ikincil. Bu sahne SON hâli durağan çizer (kayma, opaklık geçişi yok) |
| Künye (HUD) sayıları | `P/ortak/kunye.js` `KUNYE`, `kunyeCiz` (satır 145–162), `dersDuzen` | §4.1 |
| Ev ikonu | `P/ortak/cizim/tabler/home.svg` → `Y.tabler("home")` | 3 yol, 24×24 ızgara |
| Bavul ikonu | `K/projeler/02-04-ydt-temel/sahneler/04-canvas-ornek2/sahne.js` satır 19–27 (`BAVUL_SVG`) | 6 `<path d>` dizgisi, 24×24 ızgara; uret.py'de `BAVUL = [...]` listesi olarak yazılır |
| Kart + zaman bandı görsel dili | aynı `sahne.js` satır 70–152 | eksen ikincil + ok ucu, bant vurgu dolgusu, "now" noktası mürekkep. Bu sahnede `now` yazısı YOK (64 px altı yazı yasağı; kartta yer yok) |
| Tema dönüşümü | `P/ortak/hf_tema.py` | §5 |

## 3. Okuma ve sabitler

- `PAKET = AD.parent.parent`. `PAKET/zaman.json` oku; `hikaye` alanı: `klasor == AD.name` assert, `kare == 1` assert.
  `sahneler[]` içinde `AD.name` YOK assert (hikâye zaman çizelgesi dışında kalır).
- `Z = D/zamanlar.json` (`sure` 1,0 → `data-duration`; `yakala_sn` 0,5 calistir.sh'da). Anlatım, sözcük, altyazı dosyası OKUNMAZ (ses yok).
- Renk yalnız `Y.RENK` anahtarlarıyla: `zemin #1b1a17`, `murekkep #f3efe6`, `ikincil #c9c2b3`, `vurgu #f2a93b`. Başka hex YOK
  (yeşil, kırmızı, gri, beyaz yok). Koyu hex yazılır; açık tema hf_tema ile gelir (§5).
- Ölçü sabitleri: aşağıdaki tablolar. Sabit adlar dosyanın başında; her sayı bu bantlardan türer (BRIEF-DIKEY §2–§3).

| Ad | Değer | Kaynak |
|---|---|---|
| `W, H` | `Y.W, Y.H` (1080, 1920) | yardim |
| `KENAR` | 48 | BRIEF-DIKEY §2 |
| `SAG` | `W − KENAR` = 1032 | |
| `GEN` | `W − 2·KENAR` = 984 | |
| `ICERIK` | (352, 1392) | BRIEF-DIKEY §2 |
| `CAGRI` | (1344, 1536) | istem: altyazı yok, bant çağrıya ayrılır |
| `PLATFORM` | 1536 | altında hiçbir öğe yok |

## 4. Yerleşim (y = yazı tabanı, px; x sol kenar, aksi yazılmadıkça)

```
y    0 ┌───────────────────────────────────────────┐
       │ [logo 387×96]                [Full lesson] │ HUD (kunye.js)
   212 │ SIMPLE PRESENT vs                         │
   276 │ PRESENT CONTINUOUS  (YDT · BASIC)          │ rozet 216–288
   424 │ Türkçede tek sözcük                        │ Lexend 500 64
   620 │      YAŞI - [YOR] - UM                      │ Fredoka 700 S≈139, ortalı
   690 │ ┌ kart 1 ───────────────────────────────┐  │ 690–926
       │ │ [ev]  I live              PERMANENT   │  │
       │ │ ──[══════════════●══════════════]──→  │  │ uzun bant
   950 │ ┌ kart 2 ───────────────────────────────┐  │ 950–1186
       │ │ [bavul] I am living       TEMPORARY   │  │
       │ │ ──────────[════●════]──────────────→  │  │ kısa bant
  1280 │ İngilizcede iki zaman                      │ Lexend 500 64
  1418 │ Tam ders:                 [@ydspublishing] │ Caveat 72 · hap sağa hizalı
  1498 │ profildeki bağlantı                        │ Caveat 72
  1536 ├───────────────────────────────────────────┤ PLATFORM: boş
  1920 └───────────────────────────────────────────┘
```

### 4.1 Künye (HUD) — `<g id="kunye">`, `P/ortak/kunye.js` ile birebir
| Öğe | Ölçü | Renk |
|---|---|---|
| logo `<g id="ku-logo"><image id="logoimg" href="assets/logo.svg" …/>` | x 48, y 48, yükseklik 96, genişlik `96 · Y.LOGO_EN_BOY` (≈ 387) | dosya (calistir temaya göre kopyalar) |
| ders adı `<text id="ku-ders1">`, `<text id="ku-ders2">` | Fredoka 700 56, x 48, taban 212 ve 276 (`dersTaban` + `dersSatir` 64); metin `KUNYE.ders`: `SIMPLE PRESENT vs` / `PRESENT CONTINUOUS` | murekkep |
| rozet `<g id="rz0">` hap | x = 48 + `genislik(Fredoka 700, "PRESENT CONTINUOUS", 56)` + 24; y 216; h 72; rx 36; w = `genislik(Lexend 700, "YDT · BASIC", 36)` + 56 | rect `fill` vurgu |
| rozet yazısı | Lexend 700 36, ortalı (`text-anchor="middle"`), taban 216 + 36 + 13 = 265 | `fill` zemin |
| çip `<g id="ku-cip">` | metin `KUNYE.cipler["04-hyperframes-hikaye"]` = `Full lesson`; cw = `genislik(Lexend 700, metin, 40)` + 64; x = 1032 − cw; y 48; h 80; rx 40; `fill="none"`, `stroke` vurgu, `stroke-width` 4 | vurgu |
| çip yazısı | Lexend 700 40, ortalı, taban 48 + 40 + 14 = 102 | `fill` vurgu |

### 4.2 İçerik bloğu
| # | id | Öğe | Ölçü | Renk |
|---|---|---|---|---|
| 1 | `ust` | `Türkçede tek sözcük` | Lexend 500 64, x 48, taban 424 | murekkep |
| 2 | `ek` (grup) | `YAŞI-YOR-UM` son hâli | §4.3 | §4.3 |
| 3 | `kart1` (grup) | kart 1 | y0 = 690; §4.4 | §4.4 |
| 4 | `kart2` (grup) | kart 2 | y0 = 950; §4.4 | §4.4 |
| 5 | `alt` | `İngilizcede iki zaman` | Lexend 500 64, x 48, taban 1280 | murekkep |
| 6 | `cg1` | `Tam ders:` | Caveat 700 72, x 48, taban 1418 | murekkep |
| 7 | `cg2` | `profildeki bağlantı` | Caveat 700 72, x 48, taban 1498 | murekkep |
| 8 | `hap` (grup) | `@ydspublishing` hapı | hw = `genislik(Fredoka 700, "@ydspublishing", 64)` + 56; x = 1032 − hw; y 1398; h 84; rx 42 | rect `fill` vurgu |
| 9 | `hap` yazısı | `@ydspublishing` | Fredoka 700 64, ortalı (x = hap ortası), taban 1398 + 42 + 22 = 1462 | `fill` zemin |

### 4.3 `ek` — `YAŞI-YOR-UM` (ek_ayir son hâli, durağan)
- Parçalar: `wa = g("YAŞI")`, `wt = g("-")`, `wy = g("YOR")`, `wu = g("UM")`; `g(m) = Y.genislik("Fredoka", 700, m, S)`.
- `p = 0,14·S` (TIRE_PAY), `ara = 0,08·S` (TIRE_ARA). Toplam genişlik `top = wa + wt + ara + 2p + wy + ara + wt + ara + wu`
  (şef QA tur 1: tire 2 UM'ye yapışıktı → tire 2 ile UM arasına bir `ara`; sonuç S = 137).
- Boy `S`: 952 px'e sığan en büyük tam sayı, üst sınır 170 (beklenen ≈ 139). Önce S = 100 ile ölç, sonra `S = min(170, floor(952·100/top100))`, sonra `top`'u S ile yeniden hesapla ve `top ≤ 952` assert.
- Yatay: ortalı. `x0 = 540 − top/2`. Taban `EK_Y = 620`.
- Diziliş (soldan): `YAŞI` x0 → tire 1 `x0 + wa` → kutu `kx0 = x0 + wa + wt + ara`, `kx1 = kx0 + 2p + wy` → `YOR` `kx0 + p` → tire 2 `kx1 + ara` → `UM` `kx1 + 2·ara + wt`.
- Kutu (`<rect id="ek-kutu">`): BÜYÜK HARF için ölçülmüş paylar: üst `EK_Y − 0,86·S`, alt `EK_Y + 0,16·S` (Fredoka büyük harf mürekkebi −0,02..0,70 em; ana dersin 0,64/0,36 payı küçük harf içindir, burada KULLANMA). `rx = 0,10·S`. `fill` vurgu.
- Renk: `YAŞI`, `UM` murekkep; tireler ikincil; `YOR` **zemin** (`#1b1a17` → açık temada pilMetin `#1b2440`). Kutu yazının ALTINDA çizilir.
- Her parça ayrı `<text … xml:space="preserve">`; id: `ek-yasi`, `ek-tire1`, `ek-kutu`, `ek-yor`, `ek-tire2`, `ek-um`. **`t2` adlı id YOK** (hf_tema `#t2`'yi vurguya boyar).

### 4.4 Kart (y0 = 690 ya da 950; iki kart aynı ızgara)
| Öğe | Ölçü | Renk |
|---|---|---|
| çerçeve `<rect>` | x 48, y y0, w 984, h `KART_H = 236`, rx 28, `fill="none"`, `stroke-width` 4 | `stroke` murekkep |
| ikon kutusu | sol-üst (80, y0 + 28), 128×128; 24×24 ızgara `scale(128/24)`; `fill="none"`, `stroke-width = 4 / ölçek` (görünür 4 px), `stroke-linecap`/`linejoin` round. Kart 1 = `Y.tabler("home")`, kart 2 = `BAVUL` | `stroke` murekkep |
| başlık | Fredoka 700 80, x 240, taban y0 + 118. Kart 1 `I live`, kart 2 `I am living` | murekkep |
| odak altçizgisi | odak sözcüğü: kart 1 `live`, kart 2 `am living`. x: sözcüğün sol kenarı − 4 → sağ kenarı + 4 (sol kenar = 240 + `genislik("I ")`); y = taban + 0,48·boy (= taban + 38; `.claude/docs/sozlesme.md` satır 35: kuyruğa değmez, `living` g kuyruğu); hafif el eğrisi (`M x0 y Q orta y+3 x1 y+1` biçimi); `stroke-width` 8, round uç, `fill="none"` | `stroke` vurgu |
| etiket | Caveat 700 64, `text-anchor="end"`, x 980 (şef QA tur 1: 1000'de son T çerçeveye 18 px yakındı; Caveat ölçüsü kuyruğu eksik verir), taban y0 + 118. Kart 1 `PERMANENT`, kart 2 `TEMPORARY` | murekkep |
| zaman ekseni | yatay çizgi (80, y0 + 190) → (988, y0 + 190) + sağ uçta ok başı (iki kısa çizgi, uzunluk 20, açı ±0,5 rad); `stroke-width` 4, round | `stroke` ikincil |
| bant `<rect>` | y y0 + 176, h 28, rx 14. Kart 1 (uzun, "hep"): x 104 → 928. Kart 2 (kısa, "şimdilik"): `NOW_X ± 100` (440 → 640). `fill` vurgu + `stroke` vurgu, `stroke-width` 4 | vurgu |
| now noktası `<circle>` | merkez (`NOW_X = 540`, y0 + 190), r 14 (iki kartta aynı x: karşılaştırma) | `fill` murekkep |

Çizim sırası kart içinde: çerçeve → ikon → başlık → altçizgi → etiket → eksen → bant → nokta (nokta en üstte).

### 4.5 Olay listesi (tek kare; zaman çizelgesi dışı, anlatım yok)
| Olay | Kare / küresel sn | Cümle sözcüğü | Not |
|---|---|---|---|
| bütün öğeler görünür (HUD + §4.2 1–9) | kare 0 (yakalama 0,5 sn) / — | — (hikâye karesi sese bağlı değil; metin `hikaye-taslak.md` §3) | hiçbir öğe `opacity:0` başlamaz; giriş/çıkış hareketi yok |

GSAP: `gsap.timeline({ paused: true })`, kayıt `window.__timelines["main"]`. Çizelge `data-duration` ile aynı boyda olsun:
`#sahne` için 0'da ve `Z["sure"]`'de birer `set` (opaklık 1, `immediateRender: false`). Başka tween YOK.

## 5. Tema (hf_tema.py ile uyum — bunlar bozulursa açık tema yanlış çıkar)
- `Y.ZEMIN_CSS` ve `Y.zemin_html()` DEĞİŞTİRMEDEN kullan (hf_tema 4 CSS dizgisini harfi harfine arar).
- Renkler SVG öznitelik olarak, küçük harf hex: `fill="#f3efe6"`, `stroke="#f2a93b"` vb. CSS `style` içinde renk YAZMA.
- Dönüşüm: `rect fill #f2a93b` → açıkta `#ffe066` (vurguDolgu) · `text fill #1b1a17` → `#1b2440` (pilMetin) · `stroke #f2a93b` → `#d9900f` ·
  `fill/stroke #f3efe6` → `#1b2440` · `#c9c2b3` → `#5a6275`. Bu yüzden: hap/rozet/kutu/bant dolgusu `<rect fill="#f2a93b">`;
  hap/rozet/`YOR` yazısı `<text fill="#1b1a17">`. `<circle fill="#1b1a17">` ya da `<path fill="#1b1a17">` YOK (açıkta koyu kalır).
- id `t2`, `ku-nokta`, `rz1` KULLANMA (hf_tema bunlara özel kural yazar).

## 6. Kurallar ve kabul ölçütü (uret.py içinde `assert`)
1. Bütün metin ve kutular x ∈ [48, 1032]; hiçbir öğe y ≥ 1536 değil (yazı alt sınırı = taban + 0,30·boy).
2. Yazı boyu ≥ 64 (HUD hariç: ders adı 56, rozet 36, çip 40 BRIEF-DIKEY §2 ölçüsü).
3. Her ekran satırı ≤ 24 karakter (`len`), HUD dahil.
4. Blok kutuları çakışmaz. Kutu = (x, y_üst, w, h); yazı için y_üst = taban − 0,75·boy, y_alt = taban + 0,30·boy (Caveat) / 0,25·boy (diğer).
   Bloklar: HUD (0–288) · `ust` · `ek` · `kart1` · `kart2` · `alt` · `cg1` · `cg2` · `hap`. Çiftler arası kesişim alanı 0;
   dikey komşular arası boşluk ≥ 16 (istisna: `cg1`–`cg2` aynı paragrafın iki satırı, yalnız kesişim 0);
   `cg1` ve `cg2` sağ kenarı ile `hap` sol kenarı arası ≥ 24.
5. İçerik ilk bloğu `ust` üstü ≥ 352; `alt` altı ≤ 1344; `hap`, `cg1`, `cg2` [1344, 1536] içinde.
6. `nesneler.json`'a blok kutularını yaz: `[{"ad": …, "x": …, "y": …, "w": …, "h": …}]` (tam sayı).
7. Yasak: emoji, kırmızı, yeşil, gradyan (vinyet zeminin kendisidir, ekleme), gölge, `Math.random`, `Date`, try/catch, `opacity:0` başlangıç.
8. Ekranda "kanal" sözü, QR, süre ("6 dk" vb.) YOK. Python: tür ipuçları (type hints) bütün işlevlerde.
9. `python3 uret.py` stdout'a `index.html yazıldı <bayt>` ve `S=<boy>` basar; hata yoksa çıkış 0.

Kabul (şef koşturur, ajan koşturmaz): `ONIZLE_YALNIZ=1 bash calistir.sh` → "önizleme hazır"; `bash calistir.sh --tema acik|koyu` →
`P/hikaye.png` ve `D/k/hikaye-koyu.png` 1080×1920; karede taşma, kesik yazı, üst üste binme, boş bant yok.
