# SPEC — sahne 08 hikâye karesi B (soru kartı), huni v2 · simple-present-temel-s1 · 15.11.2026

MAKİNE: Linux x86_64 (srv21). Python `/usr/bin/python3` (fontTools kullanıcı site-packages'ta; `-I` YOK). Şef yazdı (istem D-S1-08);
kodu agy yazar.

| Ne | Değer |
|---|---|
| Yazılacak dosya | `/home/sef/01dev/_worktrees/kalem-0204/projeler/simple-present-temel-s1/sahneler/08-hyperframes-hikaye-b/uret.py` (YENİ; başka dosyaya dokunma) |
| Emsal kod (v2, salt okunur, kapıdan geçti) | `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s1/sahneler/07-hyperframes-hikaye-b/uret.py` |
| Yardımcı (HAZIR, değiştirme) | `.../simple-present-temel-s1/sahneler/08-hyperframes-hikaye-b/yardim.py` (`Y.kunye_svg()`, `Y.rozet_konumlari()`, `Y.genislik`, `Y.RENK`, `Y.font_css`, `Y.ZEMIN_CSS`, `Y.zemin_html`, `Y.font_kopyala`, `Y.W`, `Y.H`) |
| Bağlayıcı standart | `/home/sef/01dev/dijital-anlatim/.claude/docs/huni-v2-standart.md` §1, §2, §6 |
| Çıktı (uret.py yazar) | `proje/index.html`, `nesneler.json` (sahne dizininde) |

Kare: 1080×1920, durağan, ses yok, altyazı yok, çip yok. Zaman çizelgesi 1,0 sn (yakalama 0,5 sn; `zamanlar.json` hazır, değişmez).
Düzen B = soru kartı: `Hangisi doğru?` → kök cümle (boşluklu) → iki şık yan yana (A doğru, yeşil) → kural özeti → `Kaydet`.

## 1. Emsalden (07 uret.py) aynen alınacak kalıplar

- Dosya başı (satır 1–15): shebang, belge dizgesi (metni sahne 08'e göre yaz), `from __future__ import annotations`, `AD`,
  `sys.path.insert`, `import yardim as Y`, `PAKET = AD.parent.parent`.
- `zaman.json` doğrulaması (satır 17–26) AYNEN: `duragan` içinde `klasor == AD.name` TEK kayıt; `kare == 1`, `cikti == "hikaye-b.png"`;
  `sahneler[]` içinde `AD.name` yok.
- `zamanlar.json` okuma + 3 assert (satır 28–31) AYNEN.
- `R = Y.RENK` + anahtar assert'i (satır 33–34), `W, H`, `YESIL = "#167a4a"`, `YESIL_KOYU = "#4fbf85"` (satır 36–39).
- `kaydet_svg()` (satır 111–126) AYNEN (koordinatlar dahil: imi `translate(39 1412) scale(4)`, hap x 128 y 1416 h 88, yazı taban 1482).
- `kesisim()` (satır 167–171) AYNEN.
- `uret()` HTML şablonu (satır 273–302) AYNEN; yalnız `<svg id="sahne">` içindeki gruplar §3.6 sırasıyla değişir.
  CSS satırı `#root:not(.tema-acik) [stroke="{YESIL}"]{{stroke:{YESIL_KOYU}}}` korunur.
- `__main__` (satır 308–327) AYNEN.
- ALINMAYAN emsal işlevleri: `tr_svg`, `dogru_svg`, `yanlis_svg`, `ozet_svg` (içerik farklı; aşağıdaki §3 ile yeniden yaz).
- Künye ve kanal katmanı yalnız `Y.kunye_svg()` çağrısından gelir. uret.py içinde künye/logo kodu YOK.
- Tür ipucu bütün işlevlerde; girinti 4 boşluk; satır ≤ 120 karakter. Her `<text>`'e `xml:space="preserve"`.
- Yazı boyu sabitleri: `BOY_SORU = 80`, `BOY_KOK = 72`, `BOY_SIK = 72`, `BOY_OZET = 64`, `BOY_KAYDET = 64`.

## 2. Renk

Yalnız `R["murekkep"]` (metin, boşluk çizgisi), `R["ikincil"]` (B şıkkı çerçevesi), `R["vurgu"]` (yalnız `kaydet-hap`), `R["zemin"]`
(yalnız `kaydet-yazi`), `YESIL` (yalnız A şıkkı çerçevesi + tik). Başka hex YAZMA. `R["kirmizi"]`, `R["logoSari"]` KULLANMA.
Tema dönüşümü `ortak/hf_tema.py` ile dışarıda yapılır (açık temada `vurgu` hap → `#ffe066`, hap yazısı → `#1b2440`).

## 3. Yerleşim (px, mutlak; y = yazı tabanı; bütün metin Fredoka 700, `text-anchor` yok = sol hizalı, x 60)

```
y   0 ─ 280  boş zemin
  291 ─ 339  kanal: logo + @ydspublishing                    (Y.kunye_svg)
  386 ─ 434  künye: Simple Present + YDT · TEMEL              (Y.kunye_svg)
  535        Hangisi doğru?                                   80
  650 / 740  My parents ⎯⎯⎯⎯ (kalem çizgisi) / to work by bus.  72
  790 ─ 890  [ A) go        ✓ ]   [ B) goes        ]          72; A yeşil çerçeve + yeşil tik, B soluk (opaklık 0,45)
  970 /1050  He, she, it: s gelir; / I, you, we, they: s yok.  64
 1060 ─1400  BOŞ ZEMİN (1150–1380 bağ çıkartması elle konur; kutu, çerçeve, çizgi ÇİZME)
 1416 ─1504  [yer imi] (Kaydet)                               sarı hap (emsal kaydet_svg aynen)
 1570 ─1920  boş zemin
```

### 3.1 Soru başlığı (`soru_svg()`)
`<text id="soru" x="60" y="535" ...font-size=BOY_SORU fill=R["murekkep"]>Hangisi doğru?</text>` (grup gerekmez).

### 3.2 Kök cümle (`kok_svg()` → `<g id="kok">`)
- `<text id="kok1" x="60" y="650">My parents</text>` · `<text id="kok2" x="60" y="740">to work by bus.</text>`; BOY_KOK, `R["murekkep"]`.
- Alt çizgi karakteri (`_`) YAZMA. Boşluk = kalem çizgisi `<path id="kok-bosluk">`:
  `BOS_X1 = round(60 + genişlik("My parents", 72) + genişlik(" ", 72) + 4, 1)` (≈ 450,8), `BOS_X2 = BOS_X1 + 216`.
  `d = f"M{BOS_X1} 657 C{BOS_X1 + 70} 652 {BOS_X1 + 146} 662 {BOS_X2} 655"` (hafif el titremesi; sabit, rastgele YOK),
  `fill="none" stroke=R["murekkep"] stroke-width="7" stroke-linecap="round"`.

### 3.3 Şıklar (`siklar_svg()` → `<g id="siklar">`; iki eşit kart, 420 × 100, ara 60)
- A (doğru) `<g id="sik-a">`:
  - `<rect id="sik-a-crv" x="63" y="793" width="414" height="94" rx="26" fill="none" stroke=YESIL stroke-width="6"/>`
    (çizginin dış kenarı x 60–480, y 790–890).
  - `<text id="sik-a-yazi" x="96" y="862">A) go</text>`; BOY_SIK, `R["murekkep"]`.
  - Kalem tik: `<g id="sik-a-tik" transform="translate(360 792) scale(4)" fill="none" stroke=YESIL stroke-width="2.5"
    stroke-linecap="round" stroke-linejoin="round"><path d="M5 12l5 5l10 -10"/></g>` (görünür ≈ x 380–440, y 820–860). Emoji YOK.
- B (soluk) `<g id="sik-b" opacity="0.45">`:
  - `<rect id="sik-b-crv" x="542" y="792" width="416" height="96" rx="26" fill="none" stroke=R["ikincil"] stroke-width="4"/>`
    (dış kenar x 540–960, y 790–890).
  - `<text id="sik-b-yazi" x="576" y="862">B) goes</text>`; BOY_SIK, `R["murekkep"]`.
  - Üstü çizgi, çarpı, kırmızı YOK.

### 3.4 Kural özeti (`ozet_svg()` → `<g id="ozet">`)
`<text id="ozet1" x="60" y="970">He, she, it: s gelir;</text>` · `<text id="ozet2" x="60" y="1050">I, you, we, they: s yok.</text>`;
BOY_OZET, `R["murekkep"]`.

### 3.5 Kaydet
Emsal `kaydet_svg()` AYNEN (y 1416–1504; istem: içerik 460–1140 bandına 70 px'te 64 px yazılı hap sığmıyor → 1400–1520 bandı).

### 3.6 SVG sırası
`Y.kunye_svg()` → `soru` → `kok` → `siklar` → `ozet` → `kaydet`. Animasyon yok; timeline yalnız `#sahne` opaklık 1 (emsalle aynı).

## 4. Blok kutuları (`blok_kutulari()`, `nesneler.json`; sıra aynen; kutu = taban − 0,75·boy … taban + 0,25·boy)

| ad | x | y | w | h |
|---|---|---|---|---|
| kanal | 53,2 | 291 | 263 + genişlik(Lexend 700 `@ydspublishing` 42) − 53,2 | 48 |
| kunye | 60 | 386 | rozet x + rozet w − 60 (`Y.rozet_konumlari()[0]`) | 48 |
| soru | 60 | 535 − 0,75·80 | genişlik(`Hangisi doğru?` 80) | 80 |
| kok | 60 | 650 − 0,75·72 | max(BOS_X2 + 3,5 − 60, genişlik(`to work by bus.` 72)) | (740 + 0,25·72) − y |
| sik-a | 60 | 790 | 420 | 100 |
| sik-b | 540 | 790 | 420 | 100 |
| ozet | 60 | 970 − 0,75·64 | max(genişlik(`He, she, it: s gelir;` 64), genişlik(`I, you, we, they: s yok.` 64)) | (1050 + 0,25·64) − y |
| kaydet | 60 | 1416 | 128 + hap_w − 60 | 88 |

## 5. Kurallar (`kurallari_dogrula(bloklar, html)`, assert; emsal satır 174–259 deseni)

1. soru, kok, sik-a, sik-b, ozet: x ≥ 60, x + w ≤ 960, y ≥ 460, y + h ≤ 1140.
2. kaydet: x ≥ 60, x + w ≤ 960, y ≥ 1400, y + h ≤ 1520.
3. kanal ve kunye: y ≥ 280, y + h ≤ 450.
4. Bütün blok çiftlerinin kesişim alanı 0.
5. Dikey boşluk ≥ 16: kunye → soru, soru → kok, kok → sik-a, kok → sik-b, sik-a → ozet, sik-b → ozet.
6. Kart içi: `96 + genişlik("A) go", 72) ≤ 380 − 24` · `576 + genişlik("B) goes", 72) ≤ 960 − 36`.
7. Yazı boyları ≥ 64: BOY_SORU, BOY_KOK, BOY_SIK, BOY_OZET, BOY_KAYDET.
8. Ekran satırı ≤ 24 karakter (`len`): `Hangisi doğru?`, `My parents ____`, `to work by bus.`, `A) go`, `B) goes`,
   `He, she, it: s gelir;`, `I, you, we, they: s yok.`, `Kaydet` (künye ve kanal hariç).
9. HTML: `id="kanal"` ve `id="logoimg"` tam 1 kez; `#root.tema-acik` 0 kez; şu kimlikler var: `soru`, `kok1`, `kok2`, `kok-bosluk`,
   `sik-a`, `sik-a-crv`, `sik-a-yazi`, `sik-a-tik`, `sik-b`, `sik-b-crv`, `sik-b-yazi`, `ozet1`, `ozet2`, `kaydet-imi`, `kaydet-hap`,
   `kaydet-yazi`; şunlar yok: `ku-cip`, `cg1`, `cg2`, `hap-kutu`, `soru-kutu`, `kA`, `kB`.
10. `svg = html.split('<svg id="sahne"', 1)[1]` içinde: `stroke="{YESIL}"` tam 2 kez; `R["vurgu"]` değeri tam 2 kez (künye rozeti + hap);
    `R["kirmizi"]` 0 kez; `>_` ve `→` dizisi 0 kez. Tüm html'de `#4fbf85` tam 1 kez; `id="sik-b" opacity="0.45"` 1 kez.
11. Kodda ve yorumlarda yasak söz listesi YOK (dış grep kapısı); "tam ders", "dakika" sözleri GEÇMEZ. Emoji, `Math.random`, `Date`,
    `random`, try/except, gradyan, gölge, filtre YOK.

## 6. Olay listesi (tek kare)

| Olay | Kare / sn | Cümle sözcüğü |
|---|---|---|
| bütün öğeler görünür (kanal, künye, soru, kök + kalem boşluğu, A yeşil + tik, B soluk, özet, Kaydet) | kare 0 (yakalama 0,5 sn; çizelge 1,0 sn) | — (anlatım yok; kural özeti BRIEF-S1 girişi) |

## 7. Kabul ölçütü

- `/usr/bin/python3 uret.py` rc 0; stdout `index.html yazıldı <n>`.
- `nesneler.json` 8 blok (kanal, kunye, soru, kok, sik-a, sik-b, ozet, kaydet), tam sayı.
- `proje/index.html` §5 madde 9–10'u sağlar.
- Test, render, `calistir.sh`, git YOK (şef koşar).
