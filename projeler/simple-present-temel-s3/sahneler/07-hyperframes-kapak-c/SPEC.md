# SPEC — simple-present-temel-s3 · sahne 07-hyperframes-kapak-c (huni v2; HyperFrames 1080×1920, tek kare, ses yok) · 15.11.2026

Yazan: şef (istem D-07, P0202-S3-C). Kod yazmaz; tasarım verir. MAKİNE: Linux x86_64 (srv21). Python `/usr/bin/python3` (fontTools kurulu).
K = `/home/sef/01dev/_worktrees/kalem-0204`. Sahne dizini D = `K/projeler/simple-present-temel-s3/sahneler/07-hyperframes-kapak-c/`.
Bağlayıcı: `/home/sef/01dev/dijital-anlatim/.claude/docs/huni-v2-standart.md` §1, §2, §6 · `K/projeler/simple-present-temel-s3/BRIEF-S3.md`
"Kapak" (C) + "Kanal katmanı" · `uretim-tutanagi/kapak-taslak.md` §2, §5.

## 1. Dosyalar

| Dosya | Durum | İş |
|---|---|---|
| `/home/sef/01dev/_worktrees/kalem-0204/projeler/simple-present-temel-s3/sahneler/07-hyperframes-kapak-c/uret.py` | YOK | **YAZILACAK** (tek dosya) |
| `D/yardim.py` | HAZIR (emsal 06 v2 kopyası, `KONU = "Simple Present"`) | DOKUNMA; yalnız `import yardim as Y` |
| `D/calistir.sh`, `D/olay.py`, `D/zamanlar.json` | HAZIR | DOKUNMA |
| `D/proje/index.html`, `D/nesneler.json` | uret.py yazar | §7 |

Başka dosyaya dokunma. Silme yok. Test, render, `calistir.sh`, git YOK (şef koşar).

## 2. Kalıp kaynakları (salt oku)

| Kalıp | Mutlak yol | Ne alınır |
|---|---|---|
| emsal kapak C (aynı tür sahne) | `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s1/sahneler/06-hyperframes-kapak-c/uret.py` | dosya başı (satır 1–17), `zaman.json`/`zamanlar.json` okuma ve assert'ler (satır 19–36; `cikti == "kapak-c.png"`), sabitler (satır 38–43), başlık konturu biçimi (`baslik_svg`: `stroke` zemin, `stroke-linejoin="round"`, `style="font-kerning:none;paint-order:stroke fill"`), `kesisim()`, `kurallari_dogrula()` yapısı, HTML kabuğu ve GSAP iki `tl.set` (satır 360–385), `__main__` (satır 389–409) |
| aynı paket, yanlış/doğru satır kalıbı | `/home/sef/01dev/_worktrees/kalem-0204/projeler/simple-present-temel-s3/sahneler/05-hyperframes-hikaye-a/uret.py` (ve aynı dizindeki `SPEC.md` §2–§3) | kart zemini + çerçeve (`fill-opacity`, içe 2 px çerçeve), `es` tspan + kırmızı üstü çizgi, `✗`/`✓` SVG `<path>` yöntemi, renk sayım assert'i |
| yardımcılar | `D/yardim.py` | `Y.kunye_svg()` (argümansız; `#kanal` = `#logoimg` + `@ydspublishing`, `#ku-konu`, `#rz0`), `Y.HUD`, `Y.rozet_konumu()` → `(x, w)`, `Y.KANAL_YAZI`, `Y.genislik`, `Y.RENK`, `Y.font_css`, `Y.ZEMIN_CSS`, `Y.zemin_html`, `Y.font_kopyala`, `Y.W`, `Y.H` |

Emsaldeki `eskiz_svg`, `etiketler_svg`, `hesapla_s_ve_baslik` (kutu/hap), `I LIVE` içeriği ALINMAZ.

## 3. Sabitler

`KENAR = Y.HUD["kenar"]` (60) · `SAG = Y.HUD["sagSinir"]` (960) · `ICERIK_BAS = Y.HUD["icerikBas"]` (460) · `ICERIK_SON = Y.HUD["icerikSon"]` (1380) ·
`ORTA = (KENAR + SAG) / 2` (510) · `BASLIK_GEN = 900` · `BASLIK_UST = 470` · `KONTUR = 10` · `SAT1 = "DOES VARSA"` · `SAT2 = "FİİL YALIN"`
(`FİİL`: U+0130 noktalı büyük İ, iki kez) · `KB = 72` (kart yazısı) · `KX = 60`, `KW = 900`, `KH = 200`, `KRX = 24` ·
`K1_Y = 840`, `K2_Y = 1100` · `KYX = 108` (kart yazısı sol x) · `IM = 72` (işaret kutusu kenarı) · `IM_X = 848` (işaret kutusu sol x) ·
Fredoka 700 ölçüleri (fontTools'tan ölçüldü, sabit yaz): `CAP = 0.691` (büyük harf üstü), `NOKTA = 0.921` (`İ` noktası üstü), `ALT = 0.22` (`g` kuyruğu).

## 4. Yerleşim (y = yazı tabanı, px)

```
y    0 ┌────────────────────────────────────────────┬────────┐
       │ (boş zemin, çip YOK)                       │        │
   280 │ [logo] @ydspublishing                      │  sağ   │  Y.kunye_svg() → #kanal
   360 │ Simple Present (YDT · BASIC)               │ 960–   │  #ku-konu + #rz0
   470 │          DOES VARSA                        │ 1080   │  Fredoka 700 S≈147, orta x 510, kontur 10
   ~748│          FİİL YALIN                        │  boş   │
   840 │ ┌ kart1 (soluk) He doesn't go[es].      ✗ ┐ │        │  ikincil; es kırmızı üstü çizili; ✗ kırmızı
  1040 │ └───────────────────────────────────────────┘ │        │
  1100 │ ┌ kart2 He doesn't go.                  ✓ ┐ │        │  murekkep; go altında sarı el altçizgisi
  1300 │ └───────────────────────────────────────────┘ │        │
  1380 ├────────────────────────────────────────────┤        │  içerik sonu
 1400+ │ (boş: altyazı yok, alt boş)                │        │
```

### 4.1 Kanal + künye
`Y.kunye_svg()` çıktısı değiştirilmeden SVG'ye girer. uret.py logo, rozet, konu, çip YAZMAZ.

### 4.2 Başlık — `<g id="baslik">` (hap YOK, kutu YOK)
- `g(m, s) = Y.genislik("Fredoka", 700, m, s)`; `gm(s) = max(g(SAT1, s), g(SAT2, s))`.
- Boy: `S = floor(min(190, (BASLIK_GEN − KONTUR) · 100 / gm(100)))`; `gm(S) + KONTUR > BASLIK_GEN` iken S'yi 1 azalt. Beklenen S = 147
  (`g(SAT1,147)` ≈ 889,6; `g(SAT2,147)` ≈ 694,1). Elle boy yazma; motor ölçer.
- `T1 = BASLIK_UST + CAP·S + KONTUR/2` (≈ 576,6); `T2 = T1 + 1,12·S` (≈ 741,2). `İ` noktası üstü `T2 − NOKTA·S − KONTUR/2` (≈ 600,8) > `T1 + KONTUR/2` (≈ 581,6).
- `<text id="bs-1">` SAT1 ve `<text id="bs-2">` SAT2: `x = ORTA`, `text-anchor="middle"`, `font-family="Fredoka" font-weight="700" font-size=S`,
  `fill=R["murekkep"]`, `stroke=R["zemin"]`, `stroke-width=KONTUR`, `stroke-linejoin="round"`, `style="font-kerning:none;paint-order:stroke fill"`.
- Başlık alt = `T2 + 0,009·S + KONTUR/2` (≈ 747,5).

### 4.3 Kart 1 — `<g id="kart1">` (soluk, yanlış)
Sıra: zemin → çerçeve → yazı → üstü çizgi → `✗`.
- `<rect id="k1-zemin" x=KX y=K1_Y width=KW height=KH rx=KRX fill=R["ikincil"] fill-opacity="0.08"/>`
- `<rect id="k1-cerceve" x=KX+2 y=K1_Y+2 width=KW−4 height=KH−4 rx=KRX−2 fill="none" stroke=R["ikincil"] stroke-width="4"/>`
  (çizgi merkezde; dış kenar 60–960).
- Taban `T_1 = K1_Y + KH/2 + 0,35·KB` (= 965,2). `<text id="k1-yazi" x=KYX y=T_1 font-family="Fredoka" font-weight="700" font-size=KB
  fill=R["ikincil"] style="font-kerning:none">He doesn't go<tspan id="k1-es">es</tspan>.</text>` (kesme işareti ASCII `'`; `es` de `ikincil`).
- Üstü çizgi (`go` + çizili `es`; yalnız `s` DEĞİL): `x_es = KYX + g("He doesn't go", KB)` (≈ 543,7), `w_es = g("es", KB)` (≈ 71,4).
  `<path id="k1-cizik" d="M{x_es+4:.1f} {T_1−17:.1f} L{x_es+w_es−2:.1f} {T_1−24:.1f}" fill="none" stroke=R["kirmizi"] stroke-width="7"
  stroke-linecap="round"/>` (x-yüksekliği 0,5·KB = 36 → çizgi `es` gövdesinin ortasından geçer, hafif yukarı eğik).
- `✗` (kalem çizimi, emoji/karakter DEĞİL): işaret kutusu x `IM_X … IM_X+IM` (848–920), y `oy−IM/2 … oy+IM/2`, `oy = K1_Y + KH/2` (940).
  `<path id="k1-carpi" d="M{IM_X+4} {oy−32} Q{IM_X+38} {oy+2} {IM_X+68} {oy+34} M{IM_X+68} {oy−34} Q{IM_X+36} {oy+2} {IM_X+6} {oy+32}"
  fill="none" stroke=R["kirmizi"] stroke-width="9" stroke-linecap="round"/>` (≈ `M852 908 Q886 942 916 974 M916 906 Q884 942 854 972`).

### 4.4 Kart 2 — `<g id="kart2">` (doğru)
Sıra: zemin → çerçeve → altçizgi → yazı → `✓`.
- `<rect id="k2-zemin" x=KX y=K2_Y width=KW height=KH rx=KRX fill=R["murekkep"] fill-opacity="0.06"/>`
- `<rect id="k2-cerceve" x=KX+2 y=K2_Y+2 width=KW−4 height=KH−4 rx=KRX−2 fill="none" stroke=R["murekkep"] stroke-width="4"/>`
- Taban `T_2 = K2_Y + KH/2 + 0,35·KB` (= 1225,2). `<text id="k2-yazi" x=KYX y=T_2 font-family="Fredoka" font-weight="700" font-size=KB
  fill=R["murekkep"] style="font-kerning:none">He doesn't go.</text>`
- Sarı el altçizgisi (TEK sarı öğe): `x_go = KYX + g("He doesn't ", KB)` (≈ 464,2), `w_go = g("go", KB)` (≈ 79,5).
  `<path id="k2-alt" d="M{x_go−6:.1f} {T_2+30:.1f} Q{x_go+w_go/2:.1f} {T_2+24:.1f} {x_go+w_go+8:.1f} {T_2+27:.1f}" fill="none"
  stroke=R["vurgu"] stroke-width="9" stroke-linecap="round"/>` (`g` kuyruğu altı `T_2 + ALT·KB` ≈ 1241; çizgi üstü ≥ 1244, kuyruğa değmez).
  Renk `stroke` özniteliğidir: hf_tema açıkta `--vurgu` (`#d9900f`), koyuda `#f2a93b` yapar.
- `✓` (kalem çizimi): `oy2 = K2_Y + KH/2` (1200). `<path id="k2-tik" d="M{IM_X+4} {oy2+2} L{IM_X+28} {oy2+30} Q{IM_X+42} {oy2−4} {IM_X+70} {oy2−34}"
  fill="none" stroke=R["murekkep"] stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/>` (≈ `M852 1202 L876 1230 Q890 1196 918 1166`).

### 4.5 SVG sırası
`Y.kunye_svg()` → `baslik` → `kart1` → `kart2`. Figür, karakter görseli, altyazı, çip YOK.

## 5. Tema (hf_tema.py ile uyum)
- `Y.ZEMIN_CSS`, `Y.zemin_html()`, `Y.font_css()` DEĞİŞTİRMEDEN kullan. Renkler yalnız `Y.RENK` anahtarları (`zemin`, `murekkep`, `ikincil`, `vurgu`,
  `kirmizi`), SVG özniteliği, küçük harf hex. CSS ile renk yazma.
- `rect`/`circle` için `fill=R["vurgu"]` KULLANMA (rozet künyede zaten var). `<path fill=…>` dolgulu yol YOK. id `t2`, `ku-nokta`, `rz1`, `ku-cip` KULLANMA.

## 6. Blok kutuları ve kurallar (`blok_kutulari`, `kurallari_dogrula`, assert)

Blok listesi (sıra = `nesneler.json` sırası):

| ad | x | y | w | h |
|---|---|---|---|---|
| kanal | 60 | 280 | `Y.HUD["kanalYaziX"] + Y.genislik("Lexend", 700, Y.KANAL_YAZI, 42) − 60` (≈ 541,9) | 70 |
| kunye | 60 | 360 | `rx + rw − 60` (`rx, rw = Y.rozet_konumu()`) | 90 |
| baslik | `ORTA − gm(S)/2 − KONTUR/2` | `T1 − CAP·S − KONTUR/2` (= 470) | `gm(S) + KONTUR` | başlık alt − y (≈ 277,5) |
| kart1 | KX | K1_Y | KW | KH |
| kart2 | KX | K2_Y | KW | KH |

Assert'ler:
1. Her blok: `x ≥ 0`, `x + w ≤ 960`, `y ≥ 280`, `y + h ≤ 1380`. İçerik blokları (baslik, kart1, kart2): `x ≥ KENAR`, `x + w ≤ SAG`, `y ≥ ICERIK_BAS`, `y + h ≤ ICERIK_SON`.
2. `rx + rw ≤ 960`. Bütün blok çiftlerinin kesişim alanı 0.
3. Dikey aralar: `baslik` alt → `kart1` üst ≥ 48; `kart1` alt → `kart2` üst ≥ 40.
4. Başlık: `S ≥ 64`; `S ≤ 190`; `gm(S) + KONTUR ≤ BASLIK_GEN`; `T2 − NOKTA·S − KONTUR/2 > T1 + KONTUR/2`; başlık alt ≤ 800.
5. Kart içi: `KYX + g("He doesn't goes.", KB) + 40 ≤ IM_X` (yazı ile işaret arası ≥ 40); işaret kutusu `IM_X + IM ≤ KX + KW − 24`;
   `oy ± IM/2` kart1 içinde, `oy2 ± IM/2` kart2 içinde; `T_1 − CAP·KB ≥ K1_Y + 24`; `T_2 + ALT·KB ≤ K2_Y + KH − 24`;
   altçizgi `T_2 + 30 + 4,5 ≤ K2_Y + KH − 12` ve `T_2 + 24 − 4,5 > T_2 + ALT·KB`.
6. Yazı boyu: `KB = 72 ≥ 64`. Ekran satırları ≤ 24 karakter: `DOES VARSA`, `FİİL YALIN`, `He doesn't goes.`, `He doesn't go.`. Başlık 2 satır.
7. Renk sayımı (html dizesinde): `html.count(R["kirmizi"]) == 2` (ikisi de `kart1` grubunda: `k1-cizik`, `k1-carpi`);
   `html.count(R["vurgu"]) == 2` (künye rozeti + `k2-alt`); yeşil (`#167a4a`, `green`) yok; `"✗"`, `"✓"` karakteri html'de yok; emoji yok.
8. HTML'de `id="kanal"` ve `id="logoimg"` tam 1 kez. Var: `bs-1`, `bs-2`, `k1-zemin`, `k1-cerceve`, `k1-yazi`, `k1-es`, `k1-cizik`, `k1-carpi`,
   `k2-zemin`, `k2-cerceve`, `k2-yazi`, `k2-alt`, `k2-tik`. Yok: `bk-kutu`, `eskiz`, `fig`, `ku-cip`, `<image` (logo dışında; `html.count("<image") == 1`).
9. Yasak: `Math.random`, `Date`, try/except, `opacity:0` başlangıç, tween (yalnız iki `tl.set`). Dosyaya standart §1 kural 4–5'in yasak sözlerini YAZMA
   (dış grep kapısı tarar; listeyi koda koyma).
10. Python: tür ipuçları bütün işlevlerde; girinti 4 boşluk; satır ≤ 130 karakter; ASCII dışı karakter yalnız Türkçe metin ve yorumlarda.

## 7. Çıktı ve kabul

- `/usr/bin/python3 uret.py` → `proje/index.html` (emsal HTML kabuğu: `#root` `data-duration=Z['sure']`, `Y.zemin_html()`, `<svg id="sahne" width="1080"
  height="1920" viewBox="0 0 1080 1920">`, iki `tl.set`, `window.__timelines["main"]`), `nesneler.json` (`[{"ad","x","y","w","h"}]` tam sayı, §6 sırası).
- stdout: `index.html yazıldı <bayt>` ve `S=<boy>`; hata yoksa çıkış 0.
- Şef koşar: `bash calistir.sh --tema acik|koyu` → `K/projeler/simple-present-temel-s3/kapak-c.png` ve `D/k/koyu/kapak-c-koyu.png` 1080×1920; kanal x 60'tan
  y 280–350; künye y 360–450; içerik 460–1380 ve x ≤ 960; 0–280 ve 1400–1920 boş; taşma, kesik yazı, üst üste binme yok.

## 8. Olay listesi (tek kare)

| Olay | Kare / küresel sn | Cümle sözcüğü |
|---|---|---|
| kapak tam görünür (kanal, künye, başlık, kart 1, kart 2) | kare 0 → son (çizelge 1,0 sn, yakalama 0,5 sn) | — (anlatımdan bağımsız; zaman çizelgesi dışı; `olay.py` boş liste yazar) |
