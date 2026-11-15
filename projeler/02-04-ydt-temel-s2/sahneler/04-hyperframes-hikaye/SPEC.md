# SPEC — 02-04-ydt-temel-s2 · sahne 04-hyperframes-hikaye (Hikâye A, HyperFrames, 1080×1920, tek kare, ses yok)

Yazan: şef (15.11.2026). Kod yazmaz; tasarım verir. K = `/home/sef/01dev/_worktrees/kalem-0204`.
Sahne dizini D = `K/projeler/02-04-ydt-temel-s2/sahneler/04-hyperframes-hikaye/`. Paket P = `K/projeler/02-04-ydt-temel-s2/`.
Kaynak: `P/BRIEF-S2.md` "Hikâye A" sütunu · `P/uretim-tutanagi/hikaye-taslak.md` §3 · `K/projeler/present-continuous-dikey/BRIEF-DIKEY.md` §0, §2, §3.

## 1. Dosyalar

| Dosya | Durum | İş |
|---|---|---|
| `D/uret.py` | YOK | **YAZILACAK** (bu spec; mutlak yol `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s2/sahneler/04-hyperframes-hikaye/uret.py`) |
| `D/yardim.py` | VAR (S1 örneğinin birebir kopyası) | DOKUNMA; yalnız içe aktar |
| `D/calistir.sh`, `D/olay.py`, `D/zamanlar.json` | VAR (şef yazdı) | DOKUNMA |
| `D/nesneler.json` | YOK | uret.py yazar (§6) |

Başka dosyaya dokunma. Silme yok. Test, render, snapshot, git yok. `P/ortak/`, BRIEF, S1 paketi ve başka sahneler salt okunur.

## 2. Kalıp kaynakları (salt oku)

| Kalıp | Mutlak yol | Ne alınır |
|---|---|---|
| **İskelet (aynı ders, aynı motor, dikey, durağan)** | `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s1/sahneler/04-hyperframes-hikaye/uret.py` | Dosyanın bütün düzeni: docstring, `AD`, `sys.path` + `import yardim as Y`, `PAKET`, `zaman.json` / `zamanlar.json` okuma + assert'ler, `R = Y.RENK`, sabitler, `kunye_svg()`, `blok_kutulari()`, `kesisim()`, `kurallari_dogrula()`, `uret()` → HTML kabuğu (`Y.font_css()`, `Y.ZEMIN_CSS`, `#sahne` CSS, `#root` öznitelikleri, `Y.zemin_html()`, tek `<svg id="sahne" … viewBox="0 0 1080 1920">`, `lib/gsap.min.js`, 2 `tl.set` + `window.__timelines["main"]`), `__main__` içinde `proje/` + `Y.font_kopyala` + `index.html` + `nesneler.json` yazımı + 2 satır stdout. **İçerik bloğu (ust, ek, kart, alt) bu sahnede DEĞİŞİR** (§4) |
| Künye sayıları | `P/ortak/kunye.js` satır 56–62 (`KUNYE`) | §4.1; metinler dosyadan okunur (§3) |
| Mont + tişört çizimi | `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel/sahneler/03-paperjs-ornek1/sahne-03.js` satır 17–32 (`MONT` 100×120 ızgara, `TISORT` 100×90 ızgara) | nokta listeleri birebir; uret.py'de Python listesi olarak yazılır (§4.4) |
| Kart + zaman bandı görsel dili | `K/projeler/02-04-ydt-temel/sahneler/08-canvas-karsit1/sahne.js` satır 131–160 | today gün bandı, now noktası bandın içinde. Bu sahnede bant SARI DEĞİL (§4.4), `now` yazısı yok |
| Tema dönüşümü | `P/ortak/hf_tema.py` | §5 |

## 3. Okuma ve sabitler

- `PAKET = AD.parent.parent`. `PAKET/zaman.json` oku; `hikaye` alanı: `klasor == AD.name`, `kare == 1`, `cikti == "hikaye-a.png"` assert.
  `sahneler[]` içinde `AD.name` YOK assert (hikâye zaman çizelgesi dışında kalır).
- `Z = D/zamanlar.json` (`sure` 1,0 → `data-duration`). Anlatım, sözcük, altyazı dosyası OKUNMAZ (ses yok).
- Künye metni `PAKET/ortak/kunye.js`'den regex ile okunur (sabit yazılmaz): `ders: ["…", "…"]` (2 satır), `rozet: "…"`,
  `"04-hyperframes-hikaye": "…"` (çip). Beklenen değerler assert: `["SIMPLE PRESENT vs", "PRESENT CONTINUOUS"]`, `"YDT · BASIC"`, `"Full lesson"`.
  S1'deki `kunye_svg()` bu üç değeri parametre alır; geri kalan sayılar S1 ile aynı.
- Renk yalnız `Y.RENK` anahtarlarıyla: `zemin #1b1a17`, `murekkep #f3efe6`, `ikincil #c9c2b3`, `vurgu #f2a93b`. Başka hex YOK
  (yeşil, kırmızı, gri, beyaz yok). Koyu hex yazılır; açık tema hf_tema ile gelir (§5).

| Ad | Değer | Kaynak |
|---|---|---|
| `W, H` | `Y.W, Y.H` (1080, 1920) | yardim |
| `KENAR`, `SAG`, `GEN` | 48, 1032, 984 | BRIEF-DIKEY §2 |
| `ICERIK` | (352, 1392) | BRIEF-DIKEY §2 |
| `CAGRI` | (1344, 1536) | istem: altyazı yok, bant çağrıya ayrılır; içerik blokları 1344'ün üstünde biter |
| `PLATFORM` | 1536 | altında hiçbir öğe yok |
| `KART_H` | 272 | §4.4 |
| `KART1_Y`, `KART2_Y` | 468, 760 | §4.2 |
| `CUMLE_X`, `CUMLE_BOY` | 240, 64 | Fredoka 700 (BRIEF-S2 Hikâye A: Fredoka 64) |
| `ETIKET_BOY` | 64 | Caveat 700 |
| `AX0` | `round(80 + genislik(Caveat 700, "RIGHT NOW", 64) + 36)` (≈ 408) | eksen başı, iki kartta aynı |
| `AX1` | 988 | eksen ucu (ok başı burada) |
| `NOW_X` | `round((AX0 + AX1) / 2)` (≈ 698) | iki kartta aynı x: karşılaştırma |

## 4. Yerleşim (y = yazı tabanı, px; x sol kenar, aksi yazılmadıkça)

```
y    0 ┌───────────────────────────────────────────┐
       │ [logo 387×96]                [Full lesson] │ HUD (S1 ile aynı)
   212 │ SIMPLE PRESENT vs                         │
   276 │ PRESENT CONTINUOUS  (YDT · BASIC)          │ rozet 216–288
   424 │ Genel mi, şu an mı?                        │ Lexend 500 64
   468 │ ┌ kart 1 ───────────────────────────────┐  │ 468–740
       │ │ [mont]  She wears her coat            │  │ Fredoka 700 64
       │ │         in the winter.                │  │
       │ │ GENERAL   ──(*)─(*)──●──(*)─(*)──→    │  │ Caveat 64 · 4 kış bandı, now dışarıda
   760 │ ┌ kart 2 ───────────────────────────────┐  │ 760–1032
       │ │ [tişört] She is wearing her           │  │
       │ │          pink T-shirt today.          │  │
       │ │ RIGHT NOW ───────[══●══]──────────→   │  │ today bandı, now içinde
  1064 │ [today]                                    │ sarı hap 1064–1148 (TEK SARI)
  1212 │ iki zamanda da geçebilir                   │ Lexend 500 64
  1296 │ Farkı anlam yapar.                         │ Lexend 700 64
  1418 │ Tam ders:                 [@ydspublishing] │ Caveat 72 · hap sağa hizalı (S1 ile aynı)
  1498 │ profildeki bağlantı                        │ Caveat 72
  1536 ├───────────────────────────────────────────┤ PLATFORM: boş
  1920 └───────────────────────────────────────────┘
```

### 4.1 Künye (HUD) — `<g id="kunye">`, S1 `kunye_svg()` ile birebir
Logo (x 48, y 48, h 96, w `96 · Y.LOGO_EN_BOY`) · ders adı 2 satır Fredoka 700 56 taban 212 / 276 (`ku-ders1`, `ku-ders2`) ·
rozet `<g id="rz0">` (x = 48 + genislik(Fredoka 700, ders[1], 56) + 24; y 216; h 72; rx 36; w = genislik(Lexend 700, rozet, 36) + 56;
rect `fill` vurgu; yazı Lexend 700 36 ortalı taban 265 `fill` zemin) · çip `<g id="ku-cip">` (cw = genislik(Lexend 700, çip, 40) + 64;
x = 1032 − cw; y 48; h 80; rx 40; `fill="none"`, `stroke` vurgu 4; yazı Lexend 700 40 ortalı taban 102 `fill` vurgu).
Logo BRIEF-DIKEY §0 gereği HUD'da; alt bantta logo YOK.

### 4.2 İçerik bloğu
| # | id | Öğe | Ölçü | Renk |
|---|---|---|---|---|
| 1 | `ust` | `Genel mi, şu an mı?` | Lexend 500 64, x 48, taban 424 | murekkep |
| 2 | `kart1` (grup) | kart 1 | y0 = 468; §4.4 | §4.4 |
| 3 | `kart2` (grup) | kart 2 | y0 = 760; §4.4 | §4.4 |
| 4 | `today` (grup) | `today` hapı: rect `today-kutu` + text `today-yazi` | hw = genislik(Fredoka 700, "today", 64) + 56; x 48; y 1064; h 84; rx 42; yazı Fredoka 700 64 ortalı (x = 48 + hw/2), taban 1064 + 42 + 22 = 1128 | rect `fill` vurgu · text `fill` zemin |
| 5 | `not1` | `iki zamanda da geçebilir` | Lexend 500 64, x 48, taban 1212 | murekkep |
| 6 | `not2` | `Farkı anlam yapar.` | Lexend 700 64, x 48, taban 1296 | murekkep |
| 7 | `cg1` | `Tam ders:` | Caveat 700 72, x 48, taban 1418 | murekkep |
| 8 | `cg2` | `profildeki bağlantı` | Caveat 700 72, x 48, taban 1498 | murekkep |
| 9 | `hap` (grup) | `@ydspublishing` hapı | S1 ile birebir: hw = genislik(Fredoka 700, "@ydspublishing", 64) + 56; x = 1032 − hw; y 1398; h 84; rx 42; yazı Fredoka 700 64 ortalı taban 1462 | rect `fill` vurgu · text `fill` zemin |

**Tek sarı öğe `today` hapıdır** (rozet, çip ve `@ydspublishing` hapı künye öğesidir). Kartta odak altçizgisi YOK, bant sarı DEĞİL,
`today` hapından kart 1'e (GENERAL) ya da kart 2'ye bağ/ok YOK.

### 4.3 Ekran metni (tamamı; başka metin yok)
HUD: `SIMPLE PRESENT vs` · `PRESENT CONTINUOUS` · `YDT · BASIC` · `Full lesson`.
İçerik: `Genel mi, şu an mı?` · `She wears her coat` · `in the winter.` · `GENERAL` · `She is wearing her` · `pink T-shirt today.` ·
`RIGHT NOW` · `today` · `iki zamanda da geçebilir` · `Farkı anlam yapar.` · `Tam ders:` · `profildeki bağlantı` · `@ydspublishing`.
`T-shirt` ASCII tire ile (U+002D). Türkçe karakterler aynen (ş, ı, ç, ğ).

### 4.4 Kart (y0 = 468 ya da 760; iki kart aynı ızgara)
| Öğe | Ölçü | Renk |
|---|---|---|
| çerçeve `<rect id="{k}-crv">` | x 48, y y0, w 984, h `KART_H` 272, rx 28, `fill="none"`, `stroke-width` 4 | `stroke` murekkep |
| ikon `<g id="{k}-ikon">` | kutu (80, y0 + 44, 128, 120); ölçek `s = min(128/gw, 120/gh)` (gw, gh = ızgara: mont 100×120, tişört 100×90); kutuda ortalı: `translate(80 + (128 − gw·s)/2, y0 + 44 + (120 − gh·s)/2) scale(s)`; `fill="none"`, `stroke-width = 4 / s` (görünür 4 px), `stroke-linecap`/`linejoin` round. Kart 1 = `MONT`, kart 2 = `TISORT` | `stroke` murekkep |
| ikon yolları | her `n` öğesi bir `<path d>`: `egri: true` ve 3 nokta → `M p0 Q p1 p2`; diğerleri `M p0 L p1 L p2 …`. `daire: [cx, cy, r]` → `<circle cx cy r fill="none"/>` | grup rengini alır |
| cümle | Fredoka 700 64, x `CUMLE_X` 240, satır 1 taban y0 + 84, satır 2 taban y0 + 164. Kart 1 `She wears her coat` / `in the winter.`; kart 2 `She is wearing her` / `pink T-shirt today.` Her satır ayrı `<text … xml:space="preserve">` (`{k}-s1`, `{k}-s2`) | murekkep |
| etiket `<text id="{k}-etiket">` | Caveat 700 64, x 80, taban y0 + 242. Kart 1 `GENERAL`, kart 2 `RIGHT NOW` | murekkep |
| zaman ekseni `<path id="{k}-eksen">` | yatay çizgi (`AX0`, AY) → (`AX1`, AY), AY = y0 + 222; sağ uçta ok başı (iki kısa çizgi, uzunluk 20, açı ±0,5 rad; S1 `kart_svg` eksen kalıbı); `stroke-width` 4, round. **Şef QA tur 1:** çizgi bantların içinden geçmez, her bant aralığında kesilir (`M … L bant_sol M bant_sag …`); yoksa kar tanesi ve now noktası çizgiyle kesişir | `stroke` ikincil |
| bant (ortak biçim) | `<rect>` y AY − 18, h 36, rx 18; `fill` murekkep + `fill-opacity="0.14"`, `stroke` murekkep, `stroke-width` 3 | murekkep (soluk dolgu) |
| kart 1 kış bantları `{k}-kis0..3` | 4 bant, w 64; merkez x = `NOW_X + d`, d ∈ (−187,5, −62,5, 62,5, 187,5) → bant `x = merkez − 32` | yukarıdaki biçim |
| kart 1 kar tanesi `{k}-kar0..3` | her bandın merkezinde (merkez x, AY); 3 doğru parçası, yarı uzunluk 11, açı 90°, 30°, 150° (tek `<path>`: `M … L … M … L … M … L …`); `fill="none"`, `stroke-width` 3, round uç | `stroke` murekkep |
| kart 2 today bandı `{k}-bant` | x `NOW_X − 80`, w 160 | yukarıdaki biçim |
| now noktası `<circle id="{k}-now">` | merkez (`NOW_X`, AY), r 12. Kart 1'de bantların ARASINDA (dışında), kart 2'de bandın İÇİNDE | `fill` murekkep |

Çizim sırası kart içinde: çerçeve → ikon → cümle → etiket → eksen → bantlar → kar taneleri → nokta (nokta en üstte).
`now` yazısı YOK (64 px altı yazı yasağı; kartta yer yok).

### 4.5 Olay listesi (tek kare; zaman çizelgesi dışı, anlatım yok)
| Olay | Kare / küresel sn | Cümle sözcüğü | Not |
|---|---|---|---|
| bütün öğeler görünür (HUD + §4.2 1–9) | kare 0 (yakalama 0,5 sn; çizelge 1,0 sn) / küresel sn yok (zaman çizelgesi dışı) | — (sese bağlı değil; metin `hikaye-taslak.md` §3) | hiçbir öğe `opacity:0` başlamaz; giriş/çıkış hareketi yok |

GSAP: S1 ile aynı (`gsap.timeline({ paused: true })`, `#sahne` için 0'da ve `Z["sure"]`'de birer `set`, `immediateRender: false`; başka tween YOK).

## 5. Tema (hf_tema.py ile uyum — bunlar bozulursa açık tema yanlış çıkar)
- `Y.ZEMIN_CSS` ve `Y.zemin_html()` DEĞİŞTİRMEDEN kullan (hf_tema 4 CSS dizgisini harfi harfine arar).
- Renkler SVG öznitelik olarak, küçük harf hex: `fill="#f3efe6"`, `stroke="#f2a93b"` vb. CSS `style` içinde renk YAZMA.
- Dönüşüm: `rect fill #f2a93b` → açıkta `#ffe066` (vurguDolgu) · `text fill #1b1a17` → `#1b2440` (pilMetin) · `stroke #f2a93b` → `#d9900f` ·
  `fill/stroke #f3efe6` → `#1b2440` · `#c9c2b3` → `#5a6275`. Bu yüzden: hap/rozet dolgusu `<rect fill="#f2a93b">`; hap/rozet yazısı
  `<text fill="#1b1a17">`. `<circle fill="#1b1a17">` ya da `<path fill="#1b1a17">` YOK (açıkta koyu kalır). now noktası `fill="#f3efe6"`.
- id `t2`, `ku-nokta`, `rz1` KULLANMA (hf_tema bunlara özel kural yazar).

## 6. Kurallar ve kabul ölçütü (uret.py içinde `assert`)
1. Bütün metin ve kutular x ∈ [48, 1032]; hiçbir öğe y ≥ 1536 değil (yazı alt sınırı = taban + 0,30·boy).
2. Yazı boyu ≥ 64 (HUD hariç: ders adı 56, rozet 36, çip 40 BRIEF-DIKEY §2 ölçüsü).
3. Her ekran satırı ≤ 24 karakter (`len`), HUD dahil (§4.3 listesinin tamamı).
4. Blok kutuları çakışmaz. Kutu = (x, y_üst, w, h); yazı için y_üst = taban − 0,75·boy, y_alt = taban + 0,30·boy (Caveat) / 0,25·boy (diğer).
   Bloklar: `hud` (48, 0, 984, 288) · `ust` · `kart1` · `kart2` · `today` · `not1` · `not2` · `cg1` · `cg2` · `hap`. Çiftler arası kesişim alanı 0;
   dikey sıra `hud → ust → kart1 → kart2 → today → not1 → not2` komşular arası boşluk ≥ 16; `not2` ile `cg1` / `hap` arası ≥ 16;
   `cg1`–`cg2` aynı paragrafın iki satırı (yalnız kesişim 0); `cg1` ve `cg2` sağ kenarı ile `hap` sol kenarı arası ≥ 24.
5. `ust` üstü ≥ 352; `not2` altı ≤ 1344; `hap`, `cg1`, `cg2` [1344, 1536] içinde.
6. Kart içi (iki kartta): cümle satırları sağ kenarı ≤ 1000; satır 2 alt sınırı (taban + 0,25·64) < etiket üstü (taban − 0,75·64);
   etiket sağ kenarı + 24 ≤ `AX0`; bütün bantlar [`AX0` + 24, `AX1` − 24] içinde; kart 1'de now noktası (r 12) ile her bant arası ≥ 12;
   kart 2'de now noktası today bandının içinde; ikon kutusu sağ kenarı (208) + 24 ≤ `CUMLE_X`.
7. `nesneler.json`'a blok kutularını yaz: `[{"ad": …, "x": …, "y": …, "w": …, "h": …}]` (tam sayı, §6.4 sırası).
8. Yasak: emoji, kırmızı (`kirmizi` anahtarı kullanılmaz), yeşil, gradyan (vinyet zeminin kendisidir, ekleme), gölge, `Math.random`, `Date`,
   try/catch, `opacity:0` başlangıç. Üretilen HTML'de `kanal`, `QR`, `dk`, `dakika` dizgisi YOK (assert, küçük/büyük harf duyarsız; `dk` için
   yalnız SVG metinleri taranır).
9. Python: tür ipuçları (type hints) bütün işlevlerde. `python3 uret.py` stdout'a `index.html yazıldı <bayt>` ve `ust=… kart1=… kart2=… today=… not2=…`
   (blok y aralıkları) basar; hata yoksa çıkış 0.

Kabul (şef koşturur, ajan koşturmaz): `ONIZLE_YALNIZ=1 bash calistir.sh` → "önizleme hazır"; `bash calistir.sh --tema acik|koyu` →
`P/hikaye-a.png` + `P/hikaye.png` ve `D/k/hikaye-a-koyu.png` 1080×1920; karede taşma, kesik yazı, üst üste binme, boş bant yok;
tek sarı öğe `today` hapı (künye hariç).
