# SPEC — sahne 08 hikâye karesi B, huni v2 (simple-present-temel-s3) · 15.11.2026

MAKİNE: Linux x86_64 (srv21). Python `/usr/bin/python3` (fontTools kurulu). Şef yazdı (istem D-08); kodu agy yazar.

| Ne | Değer |
|---|---|
| Yazılacak dosya | `/home/sef/01dev/_worktrees/kalem-0204/projeler/simple-present-temel-s3/sahneler/08-hyperframes-hikaye-b/uret.py` (yeni) |
| Kalıp 1 (iskelet, salt okunur) | `/home/sef/01dev/_worktrees/kalem-0204/projeler/simple-present-temel-s3/sahneler/05-hyperframes-hikaye-a/uret.py` (aynı paket, hikâye A; kapıdan geçti) |
| Kalıp 2 (zaman.json denetimi, salt okunur) | `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s1/sahneler/07-hyperframes-hikaye-b/uret.py` satır 17–31 |
| Kalıp 3 (boşluk çizgisi, salt okunur) | `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s2/sahneler/07-hyperframes-hikaye-b/uret.py` satır 222–233 (`kok-bos`) |
| Yardımcı (HAZIR, değiştirme) | `.../08-hyperframes-hikaye-b/yardim.py` (`Y.kunye_svg()`, `Y.genislik`, `Y.RENK`, `Y.rozet_konumlari`, `Y.font_css`, `Y.ZEMIN_CSS`, `Y.zemin_html`, `Y.font_kopyala`, `Y.W`, `Y.H`; `KONU = "Simple Present"`) |
| Bağlayıcı | `/home/sef/01dev/dijital-anlatim/.claude/docs/huni-v2-standart.md` §1, §2, §6 · `.../simple-present-temel-s3/BRIEF-S3.md` "Hikâye kareleri" B · `.../uretim-tutanagi/hikaye-taslak.md` §4 |
| Çıktı (uret.py yazar) | `proje/index.html`, `nesneler.json` (sahne dizininde) |

Kare: 1080×1920, durağan, ses yok, altyazı yok, çip yok, hitap yok (tek istisna `Kaydet`). Zaman çizelgesi 1,0 sn,
yakalama 0,5 sn (`zamanlar.json` hazır, değişmez). Cevap karede YAZMAZ (doğru şık A; yalnız açıklama notunda). Şıklarda işaret yok.

## 1. Kalıplardan aynen alınacaklar

- Dosya başı (`#!/usr/bin/python3`, belge dizesi, `from __future__ import annotations`, `AD`, `sys.path.insert`, `import yardim as Y`,
  `PAKET = AD.parent.parent`).
- `zaman.json` denetimi Kalıp 2 satır 17–26 aynen: `duragan` listesinde `klasor == AD.name` olan TEK kayıt; `kare == 1`;
  `cikti == "hikaye-b.png"`; `AD.name` `sahneler[]` içinde yok. `zamanlar.json` 3 assert (sure 1,0 · kare 1 · fps 30) aynen.
- `R = Y.RENK`; anahtar assert'i (`zemin`, `murekkep`, `ikincil`, `vurgu`, `kirmizi`).
- Kalıp 1'den: `kaydet_svg()` (birebir aynı değerler), `kesisim()`, `kurallari_dogrula()` yapısı (bant sözlüğü, ardışık boşluk döngüsü),
  HTML iskeleti (Kalıp 1 satır 290–319: `font_css`, `ZEMIN_CSS`, `#sahne` kuralı, `#root` `data-duration` = `Z['sure']`, `zemin_html()`,
  `<svg id="sahne">`, GSAP iki `tl.set`, `window.__timelines["main"]`), `__main__` (font kopyası, `index.html`, `nesneler.json` tam sayı,
  `print(f"index.html yazıldı {len(html)}")`).
- Kalıp 1'in `etiket_svg`, `kart_svg`, `yanlis_svg`, `dogru1_svg`, `dogru2_svg` işlevleri ALINMAZ (içerik farklı).
- Künye ve kanal katmanı yalnız `Y.kunye_svg()` çağrısından gelir; uret.py içinde künye/logo kodu YOK.
- Tür ipucu zorunlu, girinti 4 boşluk, satır ≤ 130 karakter. Bütün `<text>` öğelerine `style="font-kerning:none"`.
- Dosyaya yasak söz listesi YAZMA (dış grep kapısı tarar). Emoji, `Math.random`, `Date`, try/except, gradyan, gölge YOK.

## 2. Sabitler

```
BOY_BASLIK = 88   BOY_KOK = 64   BOY_SIK = 64   BOY_OZET = 56   BOY_KAYDET = 52
BASLIK_TABAN = 545
KOK_L1, KOK_L2 = 652, 732
BOS_W = 200        BOS_KAYMA = 6
SIK_Y = (772, 872)          # şık kartı çizgisinin dış üst kenarı
SIK_H = 86                  # dış yükseklik (çizgi dahil)
SIK_TABAN = (833, 933)
SIK_TX = 100
OZET_TABAN = 1027
```

## 3. Ekran metni ve renk

| Kimlik | Metin | Yazı | Renk |
|---|---|---|---|
| `baslik` | `Hangisi doğru?` | Fredoka 700 88 | `R["murekkep"]` |
| `kok-s1` | `Does she` | Fredoka 700 64 | `R["murekkep"]` |
| `kok-bos` | (çizgi, yazı değil) | path, stroke 5 | `R["murekkep"]` |
| `kok-s2` | `to school?` | Fredoka 700 64 | `R["murekkep"]` |
| `sikA-yazi` | `A) go` | Fredoka 700 64 | `R["murekkep"]` |
| `sikB-yazi` | `B) goes` | Fredoka 700 64 | `R["murekkep"]` |
| `ozet` | `Does varsa fiil yalın.` | Fredoka 700 56 | `R["murekkep"]` |
| `kaydet-yazi` | `Kaydet` | Lexend 700 52 | `R["zemin"]` (hf_tema açıkta `pilMetin` yapar) |

Sarı (`R["vurgu"]`) YALNIZ `kaydet-hap` (+ künye rozeti, `Y.kunye_svg()`). Kırmızı YOK. Yeşil (`#167a4a`) YOK. İki şık aynı biçim.
Alt çizgi karakteri (`_`) html'de YOK: boşluk SVG çizgisidir.

## 4. Yerleşim (px, mutlak; y = yazı tabanı; bütün içerik x 60–960)

```
y   0 ─ 280  boş zemin
  291 ─ 339  kanal: logo + @ydspublishing           (Y.kunye_svg)
  386 ─ 434  künye: Simple Present + YDT · BASIC     (Y.kunye_svg)
  470 ─ 570  Hangisi doğru?             taban 545, Fredoka 700 88
  590 ─ 750  Does she ________          taban 652 (çizgi kalemle)
             to school?                 taban 732, Fredoka 700 64
  770 ─ 860  [ A) go               ]    kart dış 772–858, yazı taban 833
  870 ─ 960  [ B) goes             ]    kart dış 872–958, yazı taban 933
  980 ─ 1050 Does varsa fiil yalın.     taban 1027, Fredoka 700 56
 1060 ─ 1140 [yer imi] (Kaydet)         sarı hap (hikâye A ile aynı)
 1150 ─ 1920 BOŞ ZEMİN (bağ çıkartması / test çıkartması elle konur; kutu, çerçeve, çizgi ÇİZME)
```

### 4.1 Soru başlığı
`<text id="baslik" x="60" y="545">Hangisi doğru?</text>` (Fredoka 700 88, `R["murekkep"]`).

### 4.2 Kök (`<g id="kok">`; çerçeve YOK, düz yazı)
- `<text id="kok-s1" x="60" y="652">Does she</text>` (Fredoka 700 64).
- Boşluk çizgisi (Kalıp 3 ile aynı yöntem): `bx0 = 60 + Y.genislik("Fredoka", 700, "Does she ", 64)`, `bx1 = bx0 + BOS_W`,
  `x0 = bx0 + 4`, `x1 = bx1 - 4`, `yb = KOK_L1 + BOS_KAYMA` (658), `xc = (x0 + x1) / 2`, `yc = yb + 5`, `y1 = yb + 1`;
  `<path id="kok-bos" d="M {x0:.1f} {yb:.1f} Q {xc:.1f} {yc:.1f} {x1:.1f} {y1:.1f}" fill="none" stroke=R["murekkep"] stroke-width="5"
  stroke-linecap="round"/>`.
- `<text id="kok-s2" x="60" y="732">to school?</text>` (Fredoka 700 64).

### 4.3 Şık kartları (`<g id="sikA">`, `<g id="sikB">`; aynı işlev `sik_svg(grup_id, y0, taban, metin)`)
- Çerçeve: `<rect id="{grup_id}-crv" x="62" y="{y0 + 2}" width="896" height="{SIK_H - 4}" rx="26" fill="none" stroke=R["murekkep"]
  stroke-width="4"/>` (çizginin dış kenarı x 60–960, y y0 … y0 + 86). Dolgu YOK.
- Yazı: `<text id="{grup_id}-yazi" x="100" y="{taban}">{metin}</text>` (Fredoka 700 64, `R["murekkep"]`).
- A: `y0 = 772`, taban 833, `A) go` · B: `y0 = 872`, taban 933, `B) goes`. Harf dairesi, tik, çarpı, sarı YOK.

### 4.4 Kural özeti
`<text id="ozet" x="60" y="1027">Does varsa fiil yalın.</text>` (Fredoka 700 56, `R["murekkep"]`, tek satır).

### 4.5 Kaydet (`<g id="kaydet">`; Kalıp 1 `kaydet_svg()` BİREBİR)
- Yer imi `translate(39 1052) scale(4)`, `path id="kaydet-imi"` (Kalıp 1 ile aynı yol).
- `hap_w = Y.genislik("Lexend", 700, "Kaydet", 52) + 56`; `<rect id="kaydet-hap" x="132" y="1060" width=hap_w height="80" rx="40"
  fill=R["vurgu"]/>`; `<text id="kaydet-yazi" x={132 + hap_w/2} y="1118" text-anchor="middle">Kaydet</text>` Lexend 700 52, `R["zemin"]`.

### 4.6 SVG sırası
`Y.kunye_svg()` → `baslik` → `kok` → `sikA` → `sikB` → `ozet` → `kaydet`. Animasyon yok; timeline yalnız `#sahne` opaklık 1.

## 5. Blok kutuları (`blok_kutulari`, `nesneler.json`; yazı kutusu = taban − 0,75·boy … taban + 0,25·boy; sıra aynen)

| ad | x | y | w | h |
|---|---|---|---|---|
| kanal | 53,2 | 291 | 263 + genişlik(Lexend 700 `@ydspublishing` 42) − 53,2 | 48 |
| kunye | 60 | 386 | `rz_x + rz_w − 60` (`Y.rozet_konumlari()[0]`) | 48 |
| baslik | 60 | 545 − 66 = 479 | genişlik(Fredoka 700 `Hangisi doğru?` 88) | 88 |
| kok | 60 | 652 − 48 = 604 | max(`bx1` − 60, genişlik(Fredoka 700 `to school?` 64)) | (732 + 16) − 604 = 144 |
| sikA | 60 | 772 | 900 | 86 |
| sikB | 60 | 872 | 900 | 86 |
| ozet | 60 | 1027 − 42 = 985 | genişlik(Fredoka 700 `Does varsa fiil yalın.` 56) | 56 |
| kaydet | 60 | 1060 | 132 + hap_w − 60 | 80 |

## 6. Kurallar (`kurallari_dogrula(bloklar, html)`, assert)

1. İçerik blokları (baslik, kok, sikA, sikB, ozet, kaydet): x ≥ 60, x + w ≤ 960, y ≥ 460, y + h ≤ 1140.
2. Her içerik bloğu kendi istem bandında: baslik 470–570 · kok 590–750 · sikA 770–860 · sikB 870–960 · ozet 980–1050 · kaydet 1060–1140.
3. kanal ve kunye: y ≥ 280, y + h ≤ 450.
4. Bütün blok çiftlerinin kesişim alanı 0. Ardışık dikey boşluk (kunye → baslik → kok → sikA → sikB → ozet → kaydet) ≥ 16;
   tek istisna sikA → sikB ≥ 12 (istem bantları arası 10 px; kartlar 2 px içeride).
5. Kök: boşluk çizgisinin en alt noktası (`yb + 5 + 2,5`) < `KOK_L2 − 0,75·64` − 12 (alt satıra değmez); `bx1 ≤ 960`.
6. Şık içi: `SIK_TX + genişlik(Fredoka 700 metin 64) ≤ 960 − 24` (A ve B); her şık için yazı kutusu (taban − 48 … taban + 16)
   kart dış kenarının içinde (`y0 + 4 ≤ taban − 48`, `taban + 16 ≤ y0 + 86 − 4`).
7. Yazı boyları (sabitler): başlık 88, kök 64, şık 64, özet 56, hap 52; hepsi ≥ 50; başlık, kök, şık ≥ 64.
8. Ekran satırı ≤ 24 karakter (`len`): `Hangisi doğru?`, `Does she ____`, `to school?`, `A) go`, `B) goes`, `Does varsa fiil yalın.`, `Kaydet`.
9. Renk: `html.count(R["kirmizi"]) == 0`; `html.count(R["vurgu"]) == 2` (künye rozeti + `kaydet-hap`); `"#167a4a"` yok;
   `"✗"`, `"✓"` ve `"_"` karakteri sahne SVG dizesinde yok (dize = `<svg id="sahne"` ile ilk `</svg>` arası; betikteki
   `window.__timelines` bu dizeye girmez).
10. HTML'de `id="kanal"` ve `id="logoimg"` tam 1 kez; `#root.tema-acik` 0 kez.
11. Var: `id="baslik"`, `kok-s1`, `kok-bos`, `kok-s2`, `sikA-crv`, `sikA-yazi`, `sikB-crv`, `sikB-yazi`, `ozet`, `kaydet-imi`, `kaydet-hap`,
    `kaydet-yazi`. Yok: `ku-cip`, `cg1`, `cg2`, `ipucu`, `etiket`, `kart`, `dogru1`, `yanlis`, `kA`, `kB`.

## 7. Olay listesi (tek kare)

| Olay | Kare / küresel sn | Cümle sözcüğü |
|---|---|---|
| bütün öğeler görünür (kanal, künye, başlık, kök + boşluk çizgisi, şık A, şık B, kural özeti, kaydet) | kare 0 (yakalama 0,5; çizelge 1,0); zaman çizelgesi dışı, küresel sn yok | — (anlatım yok; `olay.py` boş liste yazar) |

## 8. Kabul ölçütü

- `/usr/bin/python3 uret.py` rc 0; çıktı `index.html yazıldı <n>`.
- `nesneler.json` 8 blok (kanal, kunye, baslik, kok, sikA, sikB, ozet, kaydet), tam sayı.
- `proje/index.html` §6 madde 9–11'i sağlar.
- Test, render, `calistir.sh`, git YOK (şef koşar). Başka dosyaya dokunma.
