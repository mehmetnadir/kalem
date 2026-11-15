# SPEC — 02-04-ydt-temel-s3 · sahne 07-hyperframes-hikaye-b (HyperFrames, 1080×1920, tek kare, ses yok)

Yazan: şef (15.11.2026, istem D-S3). Kod yazmaz; tasarım verir. K = `/home/sef/01dev/_worktrees/kalem-0204`.
Sahne dizini D = `K/projeler/02-04-ydt-temel-s3/sahneler/07-hyperframes-hikaye-b/`. Paket P = `K/projeler/02-04-ydt-temel-s3/`.
Kaynak: `P/BRIEF-S3.md` "Hikâye karesi B" + `P/uretim-tutanagi/hikaye-taslak.md` §3 (S3-C) + `P/uretim-tutanagi/S3-duzeltme.md` madde 2.
Hikâye B = soru kartı "Tarife mi, plan mı?": İngilizce cümle kartı + tren + saat + iki şık (A TARİFE · B PLAN). CEVAP YOK.

## 1. Dosyalar

| Dosya | Durum | İş |
|---|---|---|
| `D/uret.py` | YOK | **YAZILACAK** (mutlak yol `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s3/sahneler/07-hyperframes-hikaye-b/uret.py`) |
| `D/yardim.py` | VAR (S1 sahne 07 kopyası) | DOKUNMA; yalnız `import yardim as Y` |
| `D/calistir.sh`, `D/olay.py`, `D/zamanlar.json` | VAR (şef kopyaladı) | DOKUNMA |
| `D/nesneler.json` | uret.py yazar | §6 madde 6 |

Başka dosyaya dokunma. Silme yok. Test, render, snapshot, `calistir.sh`, git YOK. `P/ortak/`, `P/zaman.json`, S1 paketi ve başka
sahneler salt okunur.

## 2. Kalıp (salt oku) — en yakın örnek

`/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s1/sahneler/07-hyperframes-hikaye-b/uret.py` (aynı dersin S1 hikâye B'si,
aynı motor, aynı boyut). Oradan al:
- Dosya düzeni, docstring biçimi, `from __future__ import annotations`, `sys.path` + `import yardim as Y`.
- `zaman.json` / `zamanlar.json` doğrulaması (satır 17–29) BİREBİR (`duragan` kaydı, `kare == 1`, `cikti == "hikaye-b.png"`,
  `sahneler[]` içinde yok; `sure` 1,0 · `kare` 1 · `fps` 30).
- `Y.RENK` doğrulaması (satır 31–36) BİREBİR.
- Seçenek kartı kalıbı `secenek_karti_svg` (satır 90–115): çerçeve + harf dairesi + harf + yazı. Bu sahnede ŞIK KUTUSU olarak §4.3 ölçüleriyle.
- Çağrı bandı `cg1`, `cg2`, `hap` (satır 293–303) BİREBİR (Caveat 72 taban 1418 / 1498; hap sağa hizalı y 1398 h 84 rx 42, Fredoka 64).
- `kesisim`, `blok_kutulari`, `kurallari_dogrula` kalıbı (bloklar §6'ya göre).
- HTML kabuğu (satır 305–335: `font_css`, `ZEMIN_CSS`, `#root` data-* öznitelikleri, `zemin_html`, tek `<svg id="sahne">`, tek `set` çizelgesi)
  ve `__main__` (satır 339–358) BİREBİR.
FARK: künye için S1'deki yerel `kunye_svg()` YAZILMAZ; `Y.kunye_svg(cip)` çağrılır (aynı px, `yardim.py` satır 171).
S1 içeriği (Türkçe cümle, `Hangisi doğru?` hapı, `I live` / `I am living`, `with my uncle.`) TAŞINMAZ.

## 3. Okuma ve sabitler

- `PAKET = AD.parent.parent`. Doğrulamalar §2'deki gibi.
- Çip metni: `PAKET / "ortak" / "kunye.js"` dosyasını oku; `"07-hyperframes-hikaye-b": "<metin>"` deseninden metni regex ile al
  (beklenen `Full lesson`). Bulunamazsa `assert` ile dur. Elle yazılmaz.
- Renk yalnız `Y.RENK`: `zemin #1b1a17`, `murekkep #f3efe6`, `ikincil #c9c2b3`, `vurgu #f2a93b`. Başka hex YOK.
- `W, H = Y.W, Y.H`; `KENAR = 48`; `SAG = 1032`; `ICERIK = (352, 1392)`; `CAGRI = (1344, 1536)`; `PLATFORM = 1536`.

## 4. Yerleşim (y = yazı tabanı, px; x sol kenar)

```
y    0 ┌───────────────────────────────────────────┐
       │ [logo]                       [Full lesson] │ HUD = Y.kunye_svg(cip)
   212 │ SIMPLE PRESENT vs                         │
   276 │ PRESENT CONTINUOUS  (YDT · BASIC)          │ HUD sonu 288
   448 │ Tarife mi, plan mı?                       │ Fredoka 700 96, mürekkep (sarı DEĞİL)
   512 │ ┌ cümle kartı ─────────────────────────┐  │ 512–1014
       │ │  [tren 88–604]      (saat r 96)      │  │ ikon satırı 552–770
   870 │ │  The train to İzmir                  │  │ Fredoka 700 64
   958 │ │  leaves at 7 pm today.               │  │ Fredoka 700 64
  1054 │ ┌ şık A ────────┐  ┌ şık B ────────┐     │ 1054–1274, yan yana
       │ │ (A)  TARİFE   │  │ (B)  PLAN     │     │ Fredoka 700 72
  1418 │ Cevap tam derste:        [@ydspublishing]  │ Caveat 72 · hap sağa hizalı
  1498 │ profildeki bağlantı                        │ Caveat 72
  1536 ├───────────────────────────────────────────┤ PLATFORM: boş
```

### 4.1 Soru
| id | Öğe | Ölçü | Renk |
|---|---|---|---|
| `soru` | `Tarife mi, plan mı?` | Fredoka 700 96, x 48, taban 448, `xml:space="preserve"` | `fill` murekkep |

### 4.2 Cümle kartı (grup `kart`)
| id | Öğe | Ölçü | Renk |
|---|---|---|---|
| `kart-crv` | çerçeve `<rect>` | x 48, y 512, w 984, h 502, rx 28, `fill="none"`, `stroke-width` 4 | `stroke` murekkep |
| `tren` (grup) | tren çizimi | §4.2.1; ölçek s = 1,2; köken ox = 100, oy = 580 | §4.2.1 |
| `saat` (grup) | saat çizimi | §4.2.2; merkez (772, 661), r = 96 | murekkep |
| `kart-s1` | `The train to İzmir` | Fredoka 700 64, x 88, taban 870 | `fill` murekkep |
| `kart-s2` | `leaves at 7 pm today.` | Fredoka 700 64, x 88, taban 958 | `fill` murekkep |

Vurgu YOK: altçizgi, sarı sözcük, hap, sarı akrep YOK (cevabı ele vermesin). `İzmir` Türkçe İ (U+0130), `7 pm` rakamla.

#### 4.2.1 Tren (kaynak: ana ders `K/projeler/02-04-ydt-temel/sahneler/05-canvas-ornek3/sahne.js` `trenParcalari`, satır 80–103)
Dönüşüm: ekran X = ox + s·x, Y = oy + s·y (s = 1,2). Koordinatları Python'da hesapla; `transform="scale"` KULLANMA (çizgi kalınlığı
ölçeklenmesin). Bütün parçalar `fill="none"`, `stroke-linecap="round"`, `stroke-linejoin="round"`. Dikdörtgenlerde rx = 6.

| Parça | Yerel geometri (x, y, w, h ya da noktalar) | Çizgi | Renk |
|---|---|---|---|
| lokomotif gövdesi | rect 200, 55, 170, 75 | 4,8 | murekkep |
| kabin | rect 200, 10, 75, 45 | 4,8 | murekkep |
| baca | rect 320, 22, 26, 33 | 4,0 | murekkep |
| ön burun | polyline (370,95) → (398,130) → (370,130) | 4,8 | murekkep |
| vagon | rect 0, 45, 175, 85 | 4,8 | murekkep |
| bağlantı | line (175,112) → (200,112) | 4,0 | murekkep |
| vagon camları | rect 20, 60, 50, 30 · rect 100, 60, 50, 30 | 4,0 | murekkep |
| kabin camı | rect 215, 20, 42, 25 | 4,0 | murekkep |
| tekerlekler | circle merkez (40,138) (135,138) (240,138) (335,138), r 17 | 4,8 | murekkep |
| ray | line (−10,158) → (420,158) | 4,0 | ikincil |
| duman | ellipse merkez (345,2) rx 11 ry 9 · ellipse merkez (372,−16) rx 8 ry 7 | 4,0 | ikincil |

Ekran kutusu (yaklaşık): x 88–604, y 552–770. r ve rx/ry de s ile çarpılır.

#### 4.2.2 Saat (kaynak: aynı dosya `saatParcalari`, satır 105–116; kollar yedide, rakamsız)
| Parça | Geometri | Çizgi | Renk |
|---|---|---|---|
| kadran | circle (cx, cy), r | 4,8 | `stroke` murekkep, `fill="none"` |
| 4 çentik | 12, 3, 6, 9 yönünde, merkezden 0,66·r → 0,80·r | 4,0 | murekkep |
| yelkovan | (cx, cy) → (cx, cy − 0,66·r) | 5 | murekkep |
| akrep | (cx, cy) → (cx + sin(210°)·0,5·r, cy − cos(210°)·0,5·r) (= saat 7 yönü, sol alt) | 7 | murekkep (sarı DEĞİL) |
| göbek | circle (cx, cy), r 7 | — | `fill` murekkep |

Çizgiler `stroke-linecap="round"`. Ekran kutusu: x 676–868, y 565–757.

### 4.3 Şıklar (yan yana; iki şık BİREBİR aynı biçim)
| Öğe | Şık A | Şık B | Ortak ölçü | Renk |
|---|---|---|---|---|
| grup id | `sA` | `sB` | — | — |
| çerçeve `<rect>` (`-crv`) | x 48 | x 556 | y 1054, w 476, h 220, rx 28, `fill="none"`, `stroke-width` 4 | `stroke` murekkep |
| harf dairesi `<circle>` (`-daire`) | cx 140 | cx 648 | cy 1164, r 52, `fill="none"`, `stroke-width` 4 | `stroke` murekkep |
| harf `<text>` (`-harf`) | `A`, x 140 | `B`, x 648 | Fredoka 700 64, `text-anchor="middle"`, taban 1186 | `fill` murekkep |
| şık yazısı `<text>` (`-yazi`) | `TARİFE`, x 224 | `PLAN`, x 732 | Fredoka 700 72, taban 1190 | `fill` murekkep |

- Harf rozeti mürekkep çerçeve, SARI DEĞİL. Doğru şık YEŞİL DEĞİL. Tik, çarpı, renk farkı, kalın çerçeve, altçizgi YOK.
- `TARİFE` Türkçe İ (U+0130), elle büyük harf; `text-transform` YOK.

### 4.4 Çağrı bandı (S1 satır 293–303 BİREBİR)
`cg1` `Cevap tam derste:` · `cg2` `profildeki bağlantı` (Caveat 700 72, x 48, taban 1418 / 1498, murekkep) · `hap` `@ydspublishing`
(rect `fill` vurgu, yazı `fill` zemin; hap genişliği = `Y.genislik("Fredoka", 700, "@ydspublishing", 64) + 56`, x = 1032 − genişlik).
Altyazı ve karaoke YOK (ses yok). Logo yalnız HUD'da (BRIEF-DIKEY §0: alt bantta logo yok).

Sarı öğeler yalnız: HUD rozeti, HUD çipi (kalıp), `@ydspublishing` hapı. Başka sarı öğe YOK.

## 5. Tema (hf_tema.py ile uyum)
- `Y.ZEMIN_CSS` ve `Y.zemin_html()` DEĞİŞTİRMEDEN kullan. Renkler SVG özniteliği, küçük harf hex; CSS `style` içinde renk YOK.
- `hf_tema.py` dönüşümü: `rect fill #f2a93b` → açıkta `#ffe066` (`vurguDolgu`) · `text fill #1b1a17` → `#1b2440` (`pilMetin`) ·
  `fill/stroke #f3efe6` → `#1b2440` · `stroke #c9c2b3` → `#5a6275`. Hap dolgusu `<rect fill="#f2a93b">`, hap yazısı `<text fill="#1b1a17">`.
- `<circle fill="#1b1a17">` YOK. id `t2`, `ku-nokta`, `rz1` KULLANMA.

## 6. Kurallar ve kabul ölçütü (uret.py içinde `assert`)
1. Bütün metin ve kutular x ∈ [48, 1032]; hiçbir öğe y ≥ 1536 değil (yazı alt sınırı = taban + 0,30·boy).
2. Yazı boyu ≥ 64 (HUD hariç: ders adı 56, rozet 36, çip 40).
3. Her ekran satırı ≤ 24 karakter (`len`), HUD ve çip dahil.
4. Blok kutuları çakışmaz. Yazı kutusu y_üst = taban − 0,75·boy, y_alt = taban + 0,30·boy (Caveat) / 0,25·boy (diğer).
   Bloklar: `hud` (0–288) · `soru` · `kart` (çerçeve) · `sA` · `sB` · `cg1` · `cg2` · `hap`. Çiftler arası kesişim 0.
   Dikey komşular (`hud` → `soru` → `kart` → `sA`/`sB` → `cg1`/`hap`) arası boşluk ≥ 16; `sA`–`sB` yatay boşluk ≥ 24;
   `cg1` ve `cg2` sağ kenarı ile `hap` sol kenarı arası ≥ 24.
   Kart içi: `tren`, `saat`, `kart-s1`, `kart-s2` kutuları çerçevenin iç alanında (her kenardan ≥ 32); `tren`–`saat` yatay boşluk ≥ 24;
   ikon satırı altı (max(tren, saat) alt) ile `kart-s1` üstü arası ≥ 32; `kart-s1`–`kart-s2` kesişim 0.
   Şık içi: harf dairesi sağı ile şık yazısı solu arası ≥ 24; şık yazısı sağı ≤ çerçeve sağı − 32 (`TARİFE` en geniş).
5. `soru` üstü ≥ 352; `sA` ve `sB` altı ≤ 1344; `hap`, `cg1`, `cg2` [1344, 1536] içinde. İçerik bandı doluluğu:
   (max(sA, sB) alt − `soru` üst) / 1040 ≥ 0,85.
6. `nesneler.json`: `[{"ad", "x", "y", "w", "h"}]` tam sayı; §6 madde 4'teki 8 blok + `tren` + `saat` (S1 biçimi, `indent=2`).
7. Ekran metni denetimi: bütün `<text>` içerikleri bir listede toplanır; listede `kanal`, `QR`, `dk`, `Hangisi doğru?`, `I go to`,
   `movie theater` GEÇMEZ; `İzmir` (U+0130 ile) ve `7 pm` GEÇER; `Izmir` (noktasız) GEÇMEZ.
8. Yasak: emoji, kırmızı (`kirmizi` anahtarı kullanılmaz), yeşil, gradyan, gölge, `Math.random`, `Date`, try/catch, `opacity:0`
   başlangıç, hareket (tek `set` dışında tween yok). Python: tür ipuçları bütün işlevlerde.
9. `/usr/bin/python3 uret.py` stdout'a `index.html yazıldı <bayt>` basar; hata yoksa çıkış 0.

Kabul (şef koşturur, ajan koşturmaz): `ONIZLE_YALNIZ=1 bash calistir.sh` → "önizleme hazır"; `bash calistir.sh --tema acik|koyu` →
`P/hikaye-b.png` ve `D/k/koyu/hikaye-b-koyu.png` 1080×1920; taşma, kesik yazı, üst üste binme yok; açık temada hap `#ffe066` dolgu,
`#1b2440` yazı.
