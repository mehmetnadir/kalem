# SPEC — sahne 05 hikâye karesi A, kural kartı (simple-present-temel-s2, huni v2) · 15.11.2026

> DUZ2 (16.11): kart 2. satırı `every day: çoğunlukla` (sesle aynı terim, A3); `G2 = genislik("every day: çoğunlukla")`; kart yüksekliği değişmedi.

MAKİNE: Linux x86_64 (srv21). Python `/usr/bin/python3` (fontTools kurulu). Şef yazdı (istem D-V2 `05-hyperframes-hikaye-a`); kodu agy yazar.

| Ne | Değer |
|---|---|
| Yazılacak dosya | `/home/sef/01dev/_worktrees/kalem-0204/projeler/simple-present-temel-s2/sahneler/05-hyperframes-hikaye-a/uret.py` (yeni) |
| Kalıp 1 (iskelet, salt okunur) | `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s1/sahneler/04-hyperframes-hikaye/uret.py` |
| Kalıp 2 (kart, salt okunur) | `/home/sef/01dev/_worktrees/kalem-0204/projeler/simple-present-temel-s2/sahneler/03-hyperframes-kaydet/uret.py` (`kart_kenar_yolu()` satır 80–108, CSS satır 296–297) |
| Yardımcı (HAZIR, değiştirme) | aynı dizindeki `yardim.py` (`Y.kunye_svg()`, `Y.genislik`, `Y.rozet_konumlari`, `Y.RENK`, `Y.ORTAK`, `Y.font_css`, `Y.ZEMIN_CSS`, `Y.zemin_html`, `Y.font_kopyala`, `Y.W`, `Y.H`) |
| Hazır dosyalar (dokunma) | `calistir.sh`, `olay.py`, `zamanlar.json` (sure 1,0 · kare 1 · fps 30 · yakala_sn 0,5) |
| Bağlayıcı standart | `/home/sef/01dev/dijital-anlatim/.claude/docs/huni-v2-standart.md` §1, §2, §6; paket `BRIEF-S2.md` "Hikâye kareleri" A sütunu |
| Çıktı (uret.py yazar) | `proje/index.html`, `nesneler.json` (sahne dizininde) |

Kare: 1080×1920, durağan, ses yok, altyazı yok, çip yok. Zaman çizelgesi 1,0 sn.

## 1. Kalıp 1'den aynen alınacak yapı
- Dosya başı: shebang, belge dizgesi (sahne 05 hikâye A, kural kartı), `from __future__ import annotations`, `AD`, `sys.path.insert`,
  `import yardim as Y`, `PAKET = AD.parent.parent`.
- `zaman.json` (`hikaye` kaydı: `klasor == AD.name`, `kare == 1`, `sahneler[]` içinde değil) ve `zamanlar.json` (sure 1,0, kare 1, fps 30)
  assert'leri aynen. `R = Y.RENK` assert'i aynen.
- `kesisim()`, `blok_kutulari()` + `kurallari_dogrula()` yapısı, HTML iskeleti (`Y.font_css()`, `Y.ZEMIN_CSS`, `#sahne` CSS, `#root`
  öznitelikleri, `Y.zemin_html()`, tek `<svg id="sahne">`, GSAP iki `tl.set` + `window.__timelines["main"]`), `__main__` (font kopyası,
  `index.html`, `nesneler.json` tam sayıya yuvarlanmış, 2 satır özet).
- Kalıp 1'in içerik öğeleri (`ek`, `kart1`, `kart2`, `ozet`, `BAVUL`, sarı `kaydet-hap`) ALINMAZ.
- Tür ipucu zorunlu, girinti 4 boşluk, satır ≤ 120 karakter. Bütün ölçüler Python'da hesaplanır; aşağıdaki sabitler dışında sayı uydurma.

## 2. Renkler (yalnız bu hex değerleri; tema `ortak/hf_tema.py` ile çevrilir)
| Yazılan | Nerede | Koyu | Açık |
|---|---|---|---|
| `fill="#f3efe6"` / `stroke="#f3efe6"` | soru, örnek yazıları, altçizgi, otobüs, yer imi, `Kaydet` | `#f3efe6` | `#1b2440` |
| `text fill="#1b1a17"` | kart yazıları + hap yazısı | `#1b1a17` | pilMetin `#1b2440` |
| `rect fill="#f2a93b"` | `Simple Present.` hapı (karenin TEK sarısı) | `#f2a93b` | vurguDolgu `#ffe066` |
| `fill="#fff9e6"` | `#kagit` (eşlemesiz) | `#fff9e6` | CSS `.tema-acik #kagit{fill:#fffdf8;}` |
| `stroke="#1b1a17"` | `#kart-kenar` | CSS `#root #kart-kenar{stroke:var(--pilMetin,#1b1a17);}` | `#1b2440` |

İki CSS satırını `<style>` içinde `Y.ZEMIN_CSS`'ten sonra yaz (kalıp 2 satır 296–297 ile aynı). `uret.py` metninde ve HTML'de
`#root.tema-acik` dizgisi OLMAZ (hf_tema onu "çevrildi" sayar, açık tema koyu çıkar).

## 3. Yerleşim (px, mutlak; SVG sırası bu tablo sırası)
| Blok (`nesneler.json` adı) | Kimlik | Değer |
|---|---|---|
| kanal + künye | `Y.kunye_svg()` | argümansız çağır; dokunma, tween verme |
| soru | `<text id="soru">` | `Usually görünce hangi zaman?` · Caveat 700, 72, `#f3efe6`, x 60, taban `SORU_Y = 522` (şef QA 1: 528 → 522, kâğıt büyüdü) |
| kart | `<g id="kart">` | §3.1 |
| örnek | `<g id="ornek">` | §3.2 |
| otobüs | `<svg id="otobus">` | §3.3 |
| kaydet | `<g id="kaydet">` | §3.4 |
| boş | — | y 1150–1920 hiçbir öğe yok (bağ çıkartması elle konur; kutu, çerçeve çizme) |

### 3.1 Kart (`#kart`; çocuklar bu sırayla)
- Taban dikdörtgen sabitleri: `KX0 = 76`, `KX1 = 944`, `KY0 = 568`, `KY1 = 851` (şef QA 1: kâğıdın 15/12 px içi).
- `kart_kenar_yolu() -> str`: kalıp 2'deki işlevin aynı yapısı, bu dikdörtgenle: başlangıç `(KX0 + 10, KY0)`; üst kenar 3 ara nokta
  x = KX0 + (KX1 − KX0)·k/4 (k = 1, 2, 3), y = KY0 + kay[0..2]; köşe `(KX1, KY0)`; sağ kenar 3 ara nokta y = KY0 + (KY1 − KY0)·k/4,
  x = KX1 + kay[3..5]; köşe `(KX1, KY1)`; alt kenar 3 ara nokta (x azalarak) y = KY1 + kay[6..8]; köşe `(KX0, KY1)`; sol kenar 3 ara nokta
  (y azalarak) x = KX0 + kay[9..11]; `(KX0, KY0)`; bitiş `(KX0 + 24, KY0)` (başlangıcı 14 px geçer). Tek `M` + `L` dizisi, `Z` yok,
  `kay = [1.6, -1.2, 2.2, -0.8, 1.0, -2.0, 0.6, 1.8, -1.4, 0.4, -2.2, 1.2]`. Assert: her nokta KX0 − 2,5 ≤ x ≤ KX1 + 2,5 ve
  KY0 − 2,5 ≤ y ≤ KY1 + 2,5.
- `<rect id="kagit" x="61" y="557" width="898" height="305" rx="18" fill="#fff9e6" stroke="#c9c2b3" stroke-width="2"/>`
  (dış 60–960 × 556–863; sahne 03 kâğıdı gibi). Şef QA 1: ilk sürümde dolgu kalem kenarının kendisiydi; koyu temada kenar
  (`#1b1a17`) zeminle birleşti, el çizimi görünmedi.
- `<path id="kart-kenar" d="{kenar_d}" fill="none" stroke="#1b1a17" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/>`.
- Ölçü: `HAP_W = Y.genislik("Fredoka", 700, "Simple Present.", 72) + 56`; `G1 = genislik("Usually, always,")`,
  `G2 = genislik("every day:")` (Fredoka 700 72); `GMAX = max(G1, G2, HAP_W)`; `BX = round(510 − GMAX / 2, 1)` (≈ 230,9; sahne 03 ile aynı).
- Tabanlar: `T1 = 635`, `T2 = 719`, `T3 = 811`.
- `<text id="kart-s1" x=BX y=T1>Usually, always,</text>` · `<text id="kart-s2" x=BX y=T2>every day:</text>` (Fredoka 700 72, `fill="#1b1a17"`).
- `<rect id="kart-hap" x=BX y=T3−62 width=HAP_W height=88 rx=44 fill="#f2a93b"/>` +
  `<text id="kart-hap-yazi" x=BX+HAP_W/2 y=T3 text-anchor="middle">Simple Present.</text>` (Fredoka 700 72, `fill="#1b1a17"`;
  nokta hapın içinde, sahne 03 ile aynı).

### 3.2 Örnek (`#ornek`)
- `<text id="ornek-1" x="60" y="925">My brother usually goes</text>` · `<text id="ornek-2" x="60" y="1005">to school by bus.</text>`
  (Fredoka 700 64, `fill="#f3efe6"`, `xml:space="preserve"`).
- El altçizgisi `<path id="ornek-cizgi">` (`usually` altında; sarı DEĞİL): `UX0 = 60 + genislik("My brother ", 64) − 4`,
  `UX1 = 60 + genislik("My brother usually", 64) + 1` (Fredoka 700; şef QA 1: +6 ile uç `goes` g kuyruğuna 6 px kalıyordu), `UW = UX1 − UX0`, `UY = 937`. Yol:
  `M UX0 (UY+1.2) Q (UX0+UW/4) (UY−1.8) (UX0+UW/2) (UY+0.4) Q (UX0+3UW/4) (UY+2.2) UX1 (UY−1.0)`;
  `fill="none" stroke="#f3efe6" stroke-width="5" stroke-linecap="round"`. Rastgele sayı yok.

### 3.3 Otobüs (`#otobus`, köşede küçük, kalem çizgisi)
- Kaynak: `Y.ORTAK / "cizim" / "coco" / "bus.svg"` (CC0). `xml.etree.ElementTree` ile oku: kök `viewBox`, `fill="#030303"` olan `<path>`'in
  `d` ve `transform` öznitelikleri. Beyaz dolgulu (`fill="#fff"`) yol ALINMAZ. Yol verisini koda literal yazma.
- `<svg id="otobus" x="786" y="948" width="168" height=OH viewBox=(dosyadaki)>` + `<path d=… transform=… fill="#f3efe6"/>`;
  `OH = 168 · vb_yukseklik / vb_genislik` (≈ 65,2).

### 3.4 Kaydet (`#kaydet`, sağa yaslı)
- `<text id="kaydet-yazi" x="958" y="1110" text-anchor="end">Kaydet</text>` (Fredoka 700 88, `fill="#f3efe6"`).
  `YAZI_W = Y.genislik("Fredoka", 700, "Kaydet", 88)`; `YX0 = 958 − YAZI_W`.
- Yer imi (Tabler `bookmark`, MIT; yolu literal yaz, emoji değil): `<g id="kaydet-ikon" transform="translate(TX TY) scale(4.5)" fill="none"
  stroke="#f3efe6" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><path id="kaydet-imi"
  d="M18 7v14l-6 -4l-6 4v-14a4 4 0 0 1 4 -4h4a4 4 0 0 1 4 4z"/></g>`. Yol kutusu x 6–18, y 3–21; çizgi yarısı `HS = 1.4 · 4.5 / 2`.
  `TX = YX0 − 24 − HS − 18 · 4.5` (ikon mürekkebi yazıdan 24 px önce biter); `TY = 1110 − 31 − 12 · 4.5` (ikon ortası büyük harf ortasında).

## 4. Blok kutuları (`blok_kutulari()`; üst = taban − 0,74·boy, alt = taban + 0,24·boy)
| ad | x | y | w | h |
|---|---|---|---|---|
| kanal | 53,2 | 291 | 263 + genişlik(Lexend 700 `@ydspublishing` 42) − 53,2 | 48 |
| kunye | 60 | 386 | rozet x + rozet w − 60 (`Y.rozet_konumlari()[0]`) | 48 |
| soru | 60 | SORU_Y − 0,74·72 | genişlik(Caveat 700 soru 72) | 0,98·72 |
| kart | 60 | 556 | 900 | 307 (kâğıt dış kenarı) |
| ornek | 60 | 925 − 0,74·64 | genişlik(Fredoka 700 `My brother usually goes` 64) | (1005 + 0,24·64) − y |
| otobus | 786 | 948 | 168 | OH |
| kaydet | TX + 6·4,5 − HS | min(TY + 3·4,5 − HS, 1110 − 0,74·88) | 958 − x | max(TY + 21·4,5 + HS, 1110 + 0,24·88) − y |

## 5. Kurallar (`kurallari_dogrula`, assert)
1. İçerik blokları (soru, kart, ornek, otobus, kaydet): x ≥ 60, x + w ≤ 960, y ≥ 460, y + h ≤ 1140.
2. kanal ve kunye: y ≥ 280, y + h ≤ 450.
3. Bütün blok çiftlerinin kesişim alanı 0.
4. Dikey boşluk ≥ 12: kunye → soru, soru → kart, kart → ornek, kart → otobus, ornek → kaydet, otobus → kaydet.
   Yatay: otobus.x − (ornek.x + ornek.w) ≥ 16.
5. Kart içi: `BX ≥ KX0 + 24`, `BX + GMAX ≤ KX1 − 24`; `T1 − 0.74·72 ≥ KY0 + 12`; `T3 + 26 ≤ KY1 − 12`;
   satır 1 altı (`T1 + 0.24·72`) + 8 ≤ satır 2 üstü (`T2 − 0.74·72`); satır 2 altı + 8 ≤ hap üstü (`T3 − 62`).
6. Altçizgi: `UY + 2.5 + 2.5 ≤ 1005 − 0.74·64 − 8` (2. satıra değmez).
7. Satır ≤ 24 karakter: `Usually, always,`, `every day:`, `Simple Present.`, `My brother usually goes`, `to school by bus.`, `Kaydet`.
   İSTİSNA: soru satırı (28 karakter; istem metni, tek satır bandı 460–560) → onun yerine `genislik(Caveat 700 soru 72) ≤ 900` assert'i;
   koda kısa yorum yaz.
8. Yazı boyları ≥ 64 (künye ve kanal hariç): soru 72, kart 72, örnek 64, Kaydet 88.
9. HTML'de `id="kanal"` ve `id="logoimg"` tam 1 kez; `#root.tema-acik` ve `id="rz1"` hiç geçmez.
10. HTML'de şu kimlikler var: `soru`, `kagit`, `kart-kenar`, `kart-s1`, `kart-s2`, `kart-hap`, `kart-hap-yazi`, `ornek-1`, `ornek-2`,
    `ornek-cizgi`, `otobus`, `kaydet-ikon`, `kaydet-imi`, `kaydet-yazi`.
11. Yasak söz listesini koda literal yazma (dış grep kapısını kirletir). Ekranda yalnız §3 metinleri var. Emoji, QR, düğme taklidi,
    gradyan, gölge yok. `html.count('fill="#f2a93b"') == 2` (künye rozeti + kart hapı; başka sarı yok).

## 6. Kabul ölçütü
- `/usr/bin/python3 uret.py` rc 0; çıktı `index.html yazıldı <n>` ve `BX=<n>`.
- `nesneler.json` 7 blok (kanal, kunye, soru, kart, ornek, otobus, kaydet), tam sayı.
- Test, render, git YOK (şef koşar). Başka dosyaya dokunma. Silme yok.
