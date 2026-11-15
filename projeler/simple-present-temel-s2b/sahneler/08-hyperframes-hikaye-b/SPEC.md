# SPEC — sahne 08 hikâye karesi B, soru kartı (simple-present-temel-s2, huni v2) · 15.11.2026

MAKİNE: Linux x86_64 (srv21). Python `/usr/bin/python3` (fontTools kurulu). Şef yazdı (istem D-V2 `08-hyperframes-hikaye-b`); kodu agy yazar.
Tasarım verir; tam kod yazmaz. **CEVAP KAREDE YOK** (doğru şık A; not yalnız `aciklama-b.md`'de).

| Ne | Değer |
|---|---|
| Yazılacak dosya | `/home/sef/01dev/_worktrees/kalem-0204/projeler/simple-present-temel-s2/sahneler/08-hyperframes-hikaye-b/uret.py` (yeni) |
| Kalıp 1 (iskelet, salt okunur) | `/home/sef/01dev/_worktrees/kalem-0204/projeler/simple-present-temel-s2/sahneler/05-hyperframes-hikaye-a/uret.py` (aynı paket, hikâye A v2; `otobus_svg()`, `kaydet_svg()`, `kart_kenar_yolu()`, `kesisim()`, `uret()` HTML kabuğu, `__main__`) |
| Kalıp 2 (boşluklu kök + şık kartı, salt okunur) | `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s2/sahneler/07-hyperframes-hikaye-b/uret.py` (`zaman.json` → `duragan` assert'leri satır 22–28; `kok_karti_svg()` içindeki boşluk çizgisi; `secenek_karti_svg()`; cevap-yok normalleştirme denetimi) |
| Yardımcı (HAZIR, değiştirme) | aynı dizindeki `yardim.py` (`Y.kunye_svg()`, `Y.genislik`, `Y.rozet_konumlari`, `Y.RENK`, `Y.ORTAK`, `Y.font_css`, `Y.ZEMIN_CSS`, `Y.zemin_html`, `Y.font_kopyala`, `Y.KONU`) |
| Hazır dosyalar (dokunma) | `calistir.sh`, `olay.py`, `zamanlar.json` (sure 1,0 · kare 1 · fps 30 · yakala_sn 0,5), `yardim.py` |
| Bağlayıcı | `/home/sef/01dev/dijital-anlatim/.claude/docs/huni-v2-standart.md` §1, §2, §6 · paket `BRIEF-S2.md` "Hikâye kareleri" B sütunu · `uretim-tutanagi/hikaye-taslak.md` §4 |
| Çıktı (uret.py yazar) | `proje/index.html`, `nesneler.json` (sahne dizininde) |

Kare: 1080×1920, durağan, ses yok, altyazı yok, çip yok. Zaman çizelgesi 1,0 sn.

## 1. Kalıptan alınacak yapı
- Dosya başı kalıp 1 gibi: shebang, belge dizgesi (sahne 08 hikâye B, soru kartı), `from __future__ import annotations`, `AD`,
  `sys.path.insert(0, str(AD))`, `import yardim as Y`, `PAKET = AD.parent.parent`.
- `zaman.json`: kalıp 2 satır 22–28 birebir (`duragan` içinde `klasor == AD.name` TEK kayıt, `kare == 1`, `cikti == "hikaye-b.png"`,
  `sahneler[]` içinde `AD.name` yok). `zamanlar.json` assert'leri (sure 1,0, kare 1, fps 30) kalıp 1 gibi.
- `assert Y.KONU == "Simple Present"`. `R = Y.RENK`; `assert R["murekkep"] == "#f3efe6"` ve `assert R["vurgu"] == "#f2a93b"`.
- `kesisim()`, `blok_kutulari()` + `kurallari_dogrula()` yapısı, HTML kabuğu (`<style>`: yalnız `Y.font_css()`, `Y.ZEMIN_CSS`,
  `#sahne{position:absolute;left:0;top:0;}`; `#root` öznitelikleri; `Y.zemin_html()`; tek `<svg id="sahne">`; GSAP iki `tl.set("#sahne", …)`
  0 ve `Z['sure']`, `window.__timelines["main"]`), `__main__` (font kopyası, `index.html`, `nesneler.json` tam sayı) kalıp 1 gibi.
- Kalıp 1'in `soru`, `kart` (kâğıt, `#kagit`, `#kart-kenar` CSS satırları), `ornek` öğeleri ALINMAZ. Kalıp 2'nin `Look! She`, tişört, ipucu,
  sarı yer imi dolgusu, `clipPath` ALINMAZ.
- Tür ipucu zorunlu, girinti 4 boşluk, satır ≤ 120 karakter. Ölçüler Python'da hesaplanır; aşağıdaki sabitler dışında sayı uydurma.

## 2. Renk (yalnız bu hex; tema `ortak/hf_tema.py` ile çevrilir)
- Bütün içerik yazıları ve çizgileri `#f3efe6` (`R["murekkep"]`; açıkta `#1b2440`). `fill="#f3efe6"` yazı/otobüs, `stroke="#f3efe6"` çizgiler.
- Sarı YOK: içerikte `#f2a93b` geçmez (karede tek sarı künye rozetidir, `Y.kunye_svg()` içinden). Yeşil yok, kırmızı yok.
- İçerikte (künye dışı) `<path|circle fill="#1b1a17">` YOK, `text fill="#1b1a17"` YOK (künye rozet yazısı yardim'dan gelir, dokunma). `uret.py` metninde ve HTML'de `#root.tema-acik` dizgesi OLMAZ
  (hf_tema onu "çevrildi" sayar, açık tema koyu çıkar). CSS içinde renk yok.

## 3. Sabitler
| Ad | Değer | Not |
|---|---|---|
| `BASLIK_BOY`, `BASLIK_TABAN` | 88, 536 | `Hangisi doğru?` Fredoka 700 (≈ 585 px) |
| `KOK_BOY`, `L1`, `L2` | 64, 634, 714 | kök iki satır tabanı, Fredoka 700, x 60 |
| `BOS_W`, `BOS_KAYMA` | 180, 6 | boşluk genişliği (goes ≈ 134, is going ≈ 218: ikisine de eşit değil, cevabı ele vermez) · çizgi tabanı L1 + 6 |
| `OTO_X`, `OTO_Y`, `OTO_W` | 818, 668, 138 | küçük otobüs; yükseklik `OTO_H = OTO_W · vb_h / vb_w` (≈ 53,6) |
| `SIK_Y` | (775, 895) | şık kartı A, B taban dikdörtgeni üstü; `SIK_X0 = 65`, `SIK_X1 = 955`, `SIK_H = 90` |
| `DAIRE_X`, `DAIRE_R`, `HARF_KAYMA` | 125, 36, 19 | harf rozeti merkezi, yarıçap; harf tabanı `cy + 19` (kalıp 2 QA değeri) |
| `SIK_TX`, `SIK_BOY`, `METIN_KAYMA` | 186, 64, 22 | şık metni x, Fredoka 700, taban `cy + 22` |
| `KURAL_BOY`, `ALT_TABAN` | 64, 1094 | kural özeti Caveat 700 ve `Kaydet` ortak tabanı |
| `KAYDET_BOY`, `YI_S`, `YI_SW` | 72, 4, 1.5 | `Kaydet` Fredoka 700 · yer imi ölçeği · yer imi çizgi kalınlığı (görünür 6 px) |
| `BOS_UST` | 1150 | bu y'den aşağısı boş (bağ çıkartması 1150–1380 + 1400–1920) |

## 4. Yerleşim (px, mutlak; SVG sırası bu tablo sırası)
```
y   0 ┌───────────────────────────────────────┐ boş zemin 0–280
  291 │ [logo] @ydspublishing                 │ Y.kunye_svg() (kanal + künye, 291–434)
  386 │ Simple Present (YDT · TEMEL)          │
  536 │ Hangisi doğru?                        │ Fredoka 88 · 471–557
  634 │ My brother usually ________           │ Fredoka 64 · boşluk = kalem çizgisi (x 636–808)
  714 │ to school by bus.            [otobüs] │ Fredoka 64 · otobüs 818–956 × 668–722
  775 │ ╭(A) goes ───────────────────────────╮│ el çizimi kart, dış ≈ 771–869
  895 │ ╭(B) is going ───────────────────────╮│ A ile birebir aynı biçim, dış ≈ 891–989
 1094 │ usually = alışkanlık     [imi] Kaydet │ Caveat 64 sola · Fredoka 72 sağa (x ≤ 958)
 1150 │ (boş zemin: bağ çıkartması)           │ 1150–1920 hiçbir şey çizilmez
 1920 └───────────────────────────────────────┘
```

| Blok (`nesneler.json` adı) | Kimlik | Değer |
|---|---|---|
| kanal + künye | `Y.kunye_svg()` | argümansız çağır; dokunma, tween verme |
| baslik | `<text id="baslik">` | `Hangisi doğru?` · Fredoka 700 88, `fill="#f3efe6"`, x 60, taban 536, `xml:space="preserve"` |
| kok | `<g id="kok">` | §4.1 |
| otobus | `<svg id="otobus">` | §4.2 (`#kok` grubunun DIŞINDA, ondan sonra) |
| sikA, sikB | `<g id="sikA">`, `<g id="sikB">` | §4.3 |
| kural | `<text id="kural">` | `usually = alışkanlık` · Caveat 700 64, `fill="#f3efe6"`, x 60, taban 1094, sola yaslı, vurgusuz |
| kaydet | `<g id="kaydet">` | §4.4 |

### 4.1 Kök (`#kok`; kart YOK, düz yazı — hikâye A'nın örnek bloğu gibi)
- `<text id="kok-s1" x="60" y="634">My brother usually</text>` (sonda boşluk YOK) · `<text id="kok-s2" x="60" y="714">to school by bus.</text>`;
  Fredoka 700 64, `fill="#f3efe6"`, `xml:space="preserve"`. `usually` vurgusuz (aynı renk, aynı boy, altçizgi yok).
- `<path id="kok-bos">` (kalıp 2 `kok-bos` biçimi): `bx0 = 60 + Y.genislik("Fredoka", 700, "My brother usually ", 64)` (≈ 632,2) ·
  `bx1 = bx0 + BOS_W` · `x0 = bx0 + 4`, `x1 = bx1 − 4`, `yb = L1 + BOS_KAYMA`; `d = M x0 yb Q (x0+x1)/2 (yb+5) x1 (yb+1)` (1 ondalık);
  `fill="none" stroke="#f3efe6" stroke-width="5" stroke-linecap="round"`.
- Boşlukta yazı YOK: `_`, `goes`, `is going` kök grubunda geçmez.

### 4.2 Otobüs (`#otobus`, kök bloğunun sağ alt köşesinde, kalem çizgisi)
- Kalıp 1 `otobus_svg()` aynen; yalnız konum ve boy: `x=OTO_X y=OTO_Y width=OTO_W height=OTO_H`. Kaynak `Y.ORTAK / "cizim" / "coco" / "bus.svg"`
  (CC0), `fill="#030303"` olan `<path>`'in `d` + `transform`'u, `fill="#f3efe6"`; beyaz dolgulu yol ALINMAZ; yol verisi koda literal yazılmaz.

### 4.3 Şık kartları (`#sikA` y0 = 775, `#sikB` y0 = 895; iki kart BİREBİR aynı biçim; `cy = y0 + SIK_H / 2`)
- `kenar_yolu(x0, y0, x1, y1, kay) -> str`: kalıp 1 `kart_kenar_yolu()` yapısı, parametreli: başlangıç `(x0 + 10, y0)`; üst kenar 3 ara nokta
  x = x0 + (x1 − x0)·k/4 (k = 1, 2, 3), y = y0 + kay[0..2]; köşe `(x1, y0)`; sağ kenar 3 ara nokta y = y0 + (y1 − y0)·k/4, x = x1 + kay[3..5];
  köşe `(x1, y1)`; alt kenar 3 ara nokta (x azalarak) y = y1 + kay[6..8]; köşe `(x0, y1)`; sol kenar 3 ara nokta (y azalarak) x = x0 + kay[9..11];
  `(x0, y0)`; bitiş `(x0 + 24, y0)` (başlangıcı 14 px geçer). Tek `M` + `L` dizisi, `Z` yok, 1 ondalık. Assert: her nokta
  x0 − 2,5 ≤ x ≤ x1 + 2,5 ve y0 − 2,5 ≤ y ≤ y1 + 2,5.
- Şık sabiti `SIK_KAY = [1.4, -1.0, 1.8, -0.6, 0.8, -0.8, 0.6, 1.6, -1.2, 0.4, -0.8, 0.6]` (dikey kenarlar ≤ 0,8: kart kısa). İki kartta AYNI liste.
- Grup çocukları (B için `sikB-…`, harf `B`, metin `is going`):
  - `<path id="sikA-kenar" d=kenar_yolu(SIK_X0, y0, SIK_X1, y0 + SIK_H, SIK_KAY) fill="none" stroke="#f3efe6" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>`
  - `<circle id="sikA-daire" cx=DAIRE_X cy=cy r=DAIRE_R fill="none" stroke="#f3efe6" stroke-width="4"/>` (harf rozeti, mürekkep)
  - `<text id="sikA-harf" x=DAIRE_X y=cy+HARF_KAYMA text-anchor="middle">A</text>` (Fredoka 700 64, `fill="#f3efe6"`)
  - `<text id="sikA-metin" x=SIK_TX y=cy+METIN_KAYMA>goes</text>` (Fredoka 700 64, `fill="#f3efe6"`, `xml:space="preserve"`)
- Cevap belirtisi YOK: tik, çarpı, renk farkı, dolgu, kalın çerçeve, altçizgi, ikon, yeşil, sarı YOK.

### 4.4 Kaydet (`#kaydet`, sağa yaslı, sarısız)
- `<text id="kaydet-yazi" x="958" y="1094" text-anchor="end">Kaydet</text>` (Fredoka 700 72, `fill="#f3efe6"`).
  `YAZI_W = Y.genislik("Fredoka", 700, "Kaydet", 72)`; `YX0 = 958 − YAZI_W`.
- Yer imi (Tabler `bookmark`, MIT; yolu literal yaz, yorumda kaynak + lisans; emoji değil): `<g id="kaydet-ikon" transform="translate(TX TY) scale(4)"
  fill="none" stroke="#f3efe6" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path id="kaydet-imi"
  d="M18 7v14l-6 -4l-6 4v-14a4 4 0 0 1 4 -4h4a4 4 0 0 1 4 4z"/></g>`. Yol kutusu x 6–18, y 3–21; `HS = YI_SW · YI_S / 2` (3).
  `TX = YX0 − 22 − HS − 18 · YI_S` (ikon mürekkebi yazıdan 22 px önce biter); `TY = 1094 − 25 − 12 · YI_S` (ikon ortası büyük harf ortasında).
  Dolgu YOK (karenin sarısı yok).

## 5. Blok kutuları (`blok_kutulari()`; Fredoka/Lexend: üst = taban − 0,74·boy, alt = taban + 0,24·boy; Caveat alt = taban + 0,30·boy)
| ad | x | y | w | h |
|---|---|---|---|---|
| kanal | 53,2 | 291 | 263 + genişlik(Lexend 700 `@ydspublishing` 42) − 53,2 | 48 |
| kunye | 60 | 386 | rozet x + rozet w − 60 (`Y.rozet_konumlari()[0]`) | 48 |
| baslik | 60 | 536 − 0,74·88 | genişlik(Fredoka 700 `Hangisi doğru?` 88) | 0,98·88 |
| kok | 60 | L1 − 0,74·64 | max(x1 + 2,5, 60 + genişlik(`to school by bus.` 64)) − 60 | (L2 + 0,24·64) − y |
| otobus | OTO_X | OTO_Y | OTO_W | OTO_H |
| sikA | SIK_X0 − 4,5 | 775 − 4,5 | SIK_X1 − SIK_X0 + 9 | SIK_H + 9 (kay ≤ 2,5 + çizgi yarısı 2) |
| sikB | SIK_X0 − 4,5 | 895 − 4,5 | aynı | aynı |
| kural | 60 | 1094 − 0,74·64 | genişlik(Caveat 700 `usually = alışkanlık` 64) | 0,74·64 + 0,30·64 |
| kaydet | TX + 6·YI_S − HS | min(TY + 3·YI_S − HS, 1094 − 0,74·72) | 958 − x | max(TY + 21·YI_S + HS, 1094 + 0,24·72) − y |

## 6. Kurallar (`kurallari_dogrula`, assert)
1. İçerik blokları (baslik, kok, otobus, sikA, sikB, kural, kaydet): x ≥ 60, x + w ≤ 960, y ≥ 460, y + h ≤ 1140.
   Bant ayrıca: baslik 460–560 · kok ve otobus 580–740 · sikA 770–870 · sikB 890–990 · kural ve kaydet 1010–1140.
2. kanal ve kunye: y ≥ 280, y + h ≤ 450.
3. Bütün blok çiftlerinin kesişim alanı 0.
4. Dikey boşluk ≥ 12: kunye → baslik, baslik → kok, kok → sikA, otobus → sikA, sikA → sikB, sikB → kural, sikB → kaydet.
   Yatay: `kaydet.x − (kural.x + kural.w) ≥ 32`; `OTO_X − (x1 + 2,5) ≥ 6`; otobüs üstü − (L1 + 0,24·64) ≥ 12.
5. Kök içi: boşluk çizgisinin en alt noktası (`yb + 5 + 2,5`) + 8 ≤ `L2 − 0,74·64` (2. satıra değmez); `kok-s1` ve boşluk yazı üstü ≥ 580.
6. Şık içi: daire sağı (`DAIRE_X + DAIRE_R + 2`) + 20 ≤ `SIK_TX`; harf ve metin yazı kutusu (taban − 0,74·64 … taban + 0,24·64) ve
   daire (`cy ± (DAIRE_R + 2)`) taban dikdörtgeninin içinde (`y0 + 4 … y0 + SIK_H − 4`); metin sağı ≤ `SIK_X1 − 24`.
7. Kaydet: ikon görünür sağı (`TX + 18·YI_S + HS`) + 20 ≤ `YX0`; yazı sağı 958 ≤ 960.
8. Satır ≤ 24 karakter (`len`): `Hangisi doğru?`, `My brother usually ____` (boşluk 4 karakter sayılır), `to school by bus.`, `A) goes`, `B) is going`,
   `usually = alışkanlık`, `Kaydet`.
9. Yazı boyları ≥ 64 (künye ve kanal hariç): başlık 88, kök 64, harf 64, şık 64, kural 64, Kaydet 72.
10. HTML'de `id="kanal"` ve `id="logoimg"` tam 1 kez; `#root.tema-acik` (dizgeyi `"#root" + ".tema-acik"` diye kur) ve `id="rz1"` hiç geçmez.
11. HTML'de şu kimlikler var: `baslik`, `kok`, `kok-s1`, `kok-bos`, `kok-s2`, `otobus`, `sikA`, `sikA-kenar`, `sikA-daire`, `sikA-harf`,
    `sikA-metin`, `sikB`, `sikB-kenar`, `sikB-daire`, `sikB-harf`, `sikB-metin`, `kural`, `kaydet`, `kaydet-ikon`, `kaydet-imi`, `kaydet-yazi`.
12. Tek sarı künye rozetidir: `html.count('#f2a93b') == 1` (büyük/küçük harf duyarsız say); `stroke="#f2a93b"` 0.
13. Cevap yok: `sikA` ve `sikB` grup dizeleri; `sikA`/`sikB` önekini, harf ve metin içeriğini, y/cy/taban sayılarını normalleştirince EŞİT
    (`re` ile; iki kartın biçimi birebir); `kok` grubunda `goes` ve `is going` YOK; HTML'de `#167a4a` (duyarsız) YOK.
14. Yasak söz listesini koda literal yazma (dış grep kapısını kirletir). Ekranda yalnız §4 metinleri ve künye metinleri var. Emoji (U+1F000 üstü,
    U+2600–U+27BF), QR, düğme taklidi, gradyan, gölge, `opacity:0`, `Math.random`, `Date`, try/except YOK.

## 7. Kabul ölçütü
- `/usr/bin/python3 uret.py` rc 0; stdout iki satır: `index.html yazıldı <n>` ve
  `baslik=<üst>-<alt> kok=… otobus=… sikA=… sikB=… kural=… kaydet=…` (tam sayı y aralıkları).
- `nesneler.json` 9 blok (kanal, kunye, baslik, kok, otobus, sikA, sikB, kural, kaydet), tam sayı.
- Test, render, `calistir.sh`, git YOK (şef koşar). Başka dosyaya dokunma. Silme yok.
