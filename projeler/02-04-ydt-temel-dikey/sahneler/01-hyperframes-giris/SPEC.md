# SPEC — 02-04-ydt-temel-dikey · sahne 01-hyperframes-giris (HyperFrames, 1080×1920, 102 kare)

Kaynak: `projeler/02-04-ydt-temel-dikey/BRIEF-DIKEY.md` §2 + §3 satır 1. Yazan: şef (15.11.2026). Kod yazmaz; tasarım verir.
K = `/home/sef/01dev/_worktrees/kalem-0204`. Sahne dizini: `K/projeler/02-04-ydt-temel-dikey/sahneler/01-hyperframes-giris/` (= D).

## 1. Yazılacak dosyalar

| Dosya | Durum | İş |
|---|---|---|
| `D/yardim.py` | VAR (yatay `02-04-ydt-temel/sahneler/01-hyperframes-giris/yardim.py` kopyası) | §3'e göre dikeye çevir |
| `D/uret.py` | YOK | §4'e göre yaz |
| `D/olay.py` | VAR (yatay kopya) | DOKUNMA; `U.uret()` → `(s, _)` ve `U.Z["kare"]` ister |
| `D/calistir.sh` | VAR (şef uyarladı) | DOKUNMA |

Başka dosyaya dokunma. Silme yok. Test, render, git yok. `ortak/`, BRIEF, yatay paket salt okunur.

## 2. Kalıp kaynakları (salt oku)

| Kalıp | Mutlak yol | Ne alınır |
|---|---|---|
| Ana iskelet (aynı içerik, yatay) | `K/projeler/02-04-ydt-temel/sahneler/01-hyperframes-giris/uret.py` | `Sahne` kullanımı, `vur()`, `metin()`, `g()`, `ek_ayir` kurgusu (yaşı + yor + um. bitişik → kayma, kutu büyür, renk değişimi, tireler), logo damgası + uçuş, `Y.kontrol(..., ilk=False)`, `Y.html(...)` çağrısı. QA ile düzeltilmiş paylar (TIRE_PAY, TIRE_ARA, KUTU_UST/ALT, 2,14 tek kare renk değişimi, tire 2,22) AYNEN korunur |
| Dikey HUD + altyazı + zemin | `K/projeler/present-continuous-dikey/sahneler/01-hyperframes-giris/yardim.py` | `W, H = 1080, 1920`; `kunye_svg()` içindeki çip (`ku-bolum`) çizimi; `altyazi_svg()`; `zemin_html()`, `ZEMIN_CSS` (vinyet `circle 1150px`, `40%`) |
| Altyazı dilimleme | `K/projeler/present-continuous-dikey/sahneler/06-hyperframes-form/uret.py` `altyazi_dilimleri()` (satır 90–124) | ≤ 2 satır (Lexend 500 44, genişlik 984) dilim kuralı; cümle listesi parametre olur |
| HUD sayıları | `K/projeler/02-04-ydt-temel-dikey/ortak/kunye.js` `KUNYE`, `kunyeCiz`, `altyaziMetin` | çip: x = 1032 − cw, y 48, h 80, rx 40, çerçeve 4 px, Lexend 700 40, metin tabanı y 102, cw = metin + 64. Altyazı görünürlüğü: `t0 − 0,05 ≤ t < t1 + 0,35` |
| Tema dönüşümü | `K/projeler/present-continuous/ortak/hf_tema.py` | uret.py KOYU hex yazar; hf_tema CSS'e çevirir (aşağıda §5) |

## 3. `yardim.py` değişiklikleri (dikey)

1. Başlık docstring: "02-04 DİKEY HF sahnesi kopyası; 1080×1920; HUD BRIEF-DIKEY §2" anlamında güncelle.
2. `W, H = 1080, 1920`. `u(n)` = `n * W / 1080` (dikey taban 1080; docstring buna göre).
3. `AJANDA`, `ajanda_konumlari()` ve yatay `kunye_svg()` kaldırılır (dikey HUD ajanda çizmez).
4. Yeni `kunye_svg(bolum, gizli=False)`: `<g id="kunye"><g id="ku-bolum"[ style="opacity:0"]>` içinde yalnız çip:
   `rect` (x = 1032 − cw, y 48, w cw, h 80, rx 40, `fill="none"`, `stroke=RENK["vurgu"]`, `stroke-width="4"`) +
   `text` (x = 1032 − cw/2, y 102, `text-anchor="middle"`, Lexend 700 40, `fill=RENK["vurgu"]`). cw = `genislik("Lexend", 700, bolum, 40) + 64`.
   Ders adı ve rozet bu sahnede YOK (BRIEF §2.2): ku-ders / ku-rz öğesi üretme.
5. `altyazi_svg(parcalar)`: dikey örnekteki işlevin aynısı (y0 = 1400 + 84 tek satır / + 56 iki satır, satır 56, x 540 ortalı,
   Lexend 500 44, `fill=RENK["murekkep"]`, her parça `<g id=… style="opacity:0">`). `&` kaçışı korunur.
6. `altyazi_dilimleri(cumleler)`: 06 kalıbı; `ORTAK / "anlatim"` altındaki `altyazi.json` + `sozcukler.json`'u okur, `cumle in cumleler`
   parçalarını `[(t0, t1, metin)]` döndürür. Genişlik `W − 96`.
7. `zemin_html()` ve `ZEMIN_CSS`: dikey örnekteki metin (1080×1920, `circle 1150px at 50% 50%,rgba(0,0,0,0) 40%`).
   hf_tema şu 4 dizgiyi ARAR, harfi harfine kalmalı: `overflow:hidden;background:#1b1a17;}` ·
   `#zemin{position:absolute;inset:0;background:#1b1a17;}` · `opacity:.045;mix-blend-mode:overlay;}` · `rgba(0,0,0,.38) 100%)`.
8. `html(...)`: imza aynı kalır; varsayılanlar `W=W, H=H, vin=1150`. 1920×1080 dizgi değişimleri artık gereksiz (zemin zaten dikey);
   sonuçta `#root` `data-width="1080" data-height="1920"`, `#sahne` `viewBox="0 0 1080 1920"`. `#logo > #logoimg` yapısı kalır
   (hf_tema canlı kipte logoyu `#logoimg` ile değiştirir).
9. Geri kalan işlevler (`Sahne`, `kontrol`, `genislik`, `font_css`, `font_kopyala`, yol yardımcıları) değişmez.

## 4. `uret.py` (yeni) — yerleşim, olaylar, kurallar

### 4.1 Okuma
- `PAKET = AD.parent.parent`; `zaman.json`'dan `klasor == AD.name` sahnesi (t_bas 0,00, kare 102, sure 3,4).
- `PAKET/ortak/anlatim/sozcukler.json` cümle 1 sözcükleri. İlk 4 sözcük `["İstanbul'da", "yaşıyorum.", "Amcamla", "yaşıyorum."]` assert.
- Zaman: sahne 01'de küresel sn = yerel sn (t_bas 0). Sözcük zamanları dosyadan okunur, sabit yazılmaz.

### 4.2 Sabitler (BRIEF-DIKEY §3 satır 1; px = `u()` ile)
| Ad | Değer | Not |
|---|---|---|
| SOL | u(96) | yazı sol kenarı, sola hizalı |
| BOY | u(128) | Fredoka 700 |
| Y1, Y2, Y3 | u(560), u(740), u(960) | satır tabanları: İstanbul'da / yaşıyorum. / Amcamla |
| Y4 | u(1140) | 4. satır yuvası: BOŞ (sahne 02 çizer); yalnız assert için |
| TIRE_PAY, TIRE_ARA, KUTU_UST, KUTU_ALT | 0,14 · 0,08 · 0,64 · 0,36 em | yatayla aynı |
| Kutu köşe | u(14) | |
| LOGO_H (damga) | u(192) | LOGO_W = LOGO_H × `Y.LOGO_EN_BOY` (≈ 774) |
| LOGO_BX, LOGO_BY | (W − LOGO_W)/2, (352 + 1392)/2 − LOGO_H/2 | içerik bandı ortası (≈ 153, 776) |
| HUD logo hedefi | sol üst (48, 48), yükseklik 96 | bitişte görüntü kutusu 48, 48, 387×96 (kunye.js ile birebir) |
| UCUS | (0,50, 0,45) | bitiş 0,95 |
| VURUS | 0,22 sn, `back.out(1.6)` | stil §4 |

### 4.3 Olay listesi (kare = sn × 30; cümle 1)
| # | Olay | sn (kare) | Cümle sözcüğü | Ses olayı |
|---|---|---|---|---|
| 1 | logo damgası bant ortasında: opaklık 0→1, ölçek 1,18→1, dönme −2→0, `power3.out` | 0,00–0,40 (0–12) | söz öncesi | `vurus` 0,9 @0,05 |
| 2 | logo HUD sol üste uçar (`#logo` grubu x/y/scale, `power3.inOut`, svgOrigin = damga sol üst) | 0,50–0,95 (15–29) | söz öncesi | `parilti` 0,5 @0,50 |
| 3 | çip `Hook` açılır (`#ku-bolum` opaklık 0→1, 0,25 sn, `power1.out`) | 0,70–0,95 (21–29) | söz öncesi | `tik` 0,4 @0,95 − 1/30 |
| 4 | altyazı dilimi görünür (cümle 1 tek dilim, 2 satır) | 0,95 → sahne sonu | İstanbul'da t0 − 0,05 | — |
| 5 | `kinetik_baslik` `İstanbul'da` (x SOL, taban Y1) `vur()` | T(0)=1,00 (30) | İstanbul'da | `tik` 0,55 |
| 6 | `kinetik_baslik` `yaşıyorum.` bitişik (yaşı + yor + um., taban Y2) `vur()` | T(1)=1,64 (49) | yaşıyorum. | `tik` 0,55 |
| 7 | `ek_ayir`: yor ve um. kayar, sarı kutu büyür (0,36 sn `power3.out`) | te = T(1)+0,30 = 1,94 → 2,30 | "yor" hecesi | `cizgi` 0,55 @te |
| 8 | yor yazısı tek karede `pilMetin`e döner (kutu %90 dolu) | te+0,20 = 2,14 (64) | — | — |
| 9 | iki tire belirir (0,15 sn) → `yaşı-yor-um.` | te+0,28 = 2,22–2,37 | — | — |
| 10 | `kinetik_baslik` `Amcamla` (x SOL, taban Y3) `vur()` | T(2)=2,52–2,74 (76–82) | Amcamla | `tik` 0,55 |
| 11 | durgun; son 12 kare geçiş altında | 2,74–3,40 (82–101) | 2. yaşıyorum 3,08 → sahne 02 | — |

Hareket en geç 2,74'te biter. `Y.kontrol(s, Z["kare"], ilk=False)` (soğuk açılış: ilk 12 kare kuralı yok; son 12 kare kuralı var).
Altyazı: `Y.altyazi_dilimleri([1])` → her dilim `alt{i}`; `s.set` opaklık 1 @ max(0, t0 − 0,05); t1 + 0,35 < sure ise opaklık 0.
Ölçüm (fontTools): cümle 1 iki satıra sığar (969 / 619 px) → tek dilim, 0,95'ten sahne sonuna kadar.

### 4.4 Yerleşim (1080×1920; bantlar BRIEF §2)
```
y   48 ┌ logo 387×96 (0,95'ten)                 [ Hook ] çip 80 ┐   HUD 0–320
  ~438 │ İstanbul'da                         (taban 560)          │   içerik 352–1392
  ~658 │ yaşı-[yor]-um.  sarı kutu 658–786   (taban 740)          │   sağ uç ≈ 892 ≤ 1032
  ~872 │ Amcamla                             (taban 960)          │
  1140 │ (boş yuva: sahne 02 "yaşı-yor-um.")                      │
  1456 │ İstanbul'da yaşıyorum. Amcamla yaşıyorum.  (Lexend 44)   │   altyazı 1400–1536
  1512 │ Türkçede ikisi de yaşıyorum.                              │
  1536 └ PLATFORM bandı: hiçbir öğe yok                           ┘
```
Logo damgası 0,00–0,95 arası bant ortasında (≈ 153–927 × 776–968), yazılar 1,00'dan önce görünmez: üst üste binme yok.

### 4.5 Ekran metni ve renk (KOYU hex yaz; hf_tema temaya çevirir)
| Öğe | Metin | Yazı | Renk (hex) → tema değişkeni |
|---|---|---|---|
| satır 1 | `İstanbul'da` | Fredoka 700 128 | `#f3efe6` → murekkep |
| satır 2 | `yaşı` `yor` `um.` (sonra `yaşı-yor-um.`) | Fredoka 700 128 | murekkep; kutu üstündeki yor 2,14'ten `#1b1a17` → pilMetin |
| tireler | `-` ×2 | Fredoka 700 128 | `#c9c2b3` → ikincil |
| ek kutusu | — | `rect` dolgu | `#f2a93b` → vurguDolgu (açık `#ffe066`) |
| satır 3 | `Amcamla` | Fredoka 700 128 | murekkep |
| çip | `Hook` | Lexend 700 40 | `#f2a93b` çerçeve + yazı → vurgu |
| altyazı | cümle 1 | Lexend 500 44 | murekkep |

Tek vurgu = ek kutusu. Kırmızı, yeşil, emoji, gradyan, gölge yok. Ders adı ve rozet YOK.

### 4.6 Kurallar
- ID yasağı: `t1`, `t2`, `rz1`, `ku-nokta` kullanma (hf_tema CSS bunlara özel kural uygular).
- Her sözcük `<g id="w1|w2|w3" style="opacity:0">`; ek öğeleri yatay ID'leriyle (`ek1k`, `ek1a`, `ek1y`, `ek1y1`, `ek1y2`, `ek1u`, `ek1t`).
- Assert'ler (uret.py içinde, ihlalde dur):
  - `yaşı-yor-um.` sağ ucu ≤ W − 48; her satırın sağ ucu ≤ W − 48.
  - satır 1 üstü (Y1 − 0,95·BOY) ≥ 352; kutu altı (ky + kh) ile `Amcamla` üstü (Y3 − 0,691·BOY) arası ≥ u(40); kutu üstü (ky) − Y1 ≥ u(40).
  - logo damga kutusu 352–1392 içinde ve 48 ≤ x, x + w ≤ 1032.
  - `Amcamla` altı < Y4 − 0,691·BOY (4. satır yuvası boş kalır).
- `__main__`: `proje/index.html` yaz (`Y.html(s, Z["sure"], kun, None, (LOGO_BX, LOGO_BY, LOGO_W, LOGO_H), ek=altyazi)`), komut/olay sayısını
  bas ve sahne 02 devri için tek satır `devir:` JSON bas: `sol`, `taban` [Y1, Y2, Y3, Y4], `boy`, `yasi_x`, `kutu` {x, y, w, h, rx}, `tire_x` [2 değer], `sag`.
- `uret()` tam 2 değer döndürür: `(s, kun)` (olay.py `s, _ = U.uret()` ile okur). Altyazı aç/kapa `s.set` komutları `uret()` içinde;
  altyazı SVG dizgisi `__main__`te aynı `Y.altyazi_dilimleri([1])` sonucundan `Y.altyazi_svg(...)` ile üretilir ve `ek=` ile geçer.
- Python: tip ipucu zorunlu değil (kopya kalıpla uyum); girinti 4 boşluk (yatay kalıp); satır ≤ 140.
- Çalıştırma: `/usr/bin/python3 uret.py` (fontTools kullanıcı site-packages'ta; `-I` ile açılmaz — yatay RAPOR not 7).

## 5. Tema notu
uret.py koyu hex yazar. `calistir.sh` → `tema_hf` (hf_tema.py) `#root`a CSS değişkenleri ve `tema-acik` sınıfını ekler:
`fill="#f3efe6"` → murekkep, `#c9c2b3` → ikincil, `#f2a93b` → vurgu (`rect`/`circle` dolgusu → vurguDolgu), `text[fill="#1b1a17"]` → pilMetin.

## 6. Kabul ölçütü
1. `cd D && /usr/bin/python3 uret.py && /usr/bin/python3 olay.py` çıkış 0; assert yok; `olaylar.json` 7 olay, hepsi kare < 90.
2. `proje/index.html`: `data-width="1080" data-height="1920"`, `#kunye` içinde yalnız `#ku-bolum`, `#logoimg`, `alt0`, `w1–w3`.
3. `cd K && bash araclar/qa-yerel.sh 02-04-ydt-temel-dikey 01-hyperframes-giris 0.98,2.45,2.95 2.95 --hazirla` çıkış 0 (şef koşar).
4. Kareler: taşma, kesik yazı, üst üste binme, okunmaz kontrast, boş kare, platform bandında öğe YOK; altyazı bandında 2 satır metin.
