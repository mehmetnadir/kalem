# SPEC — simple-present-temel-s2 · sahne 06-hyperframes-kapak-b (huni v2; HyperFrames, 1080×1920, tek kare, ses yok)

Yazan: şef (15.11.2026, istem D-V2 `uretim-tutanagi/istem/sahne/D-06-hyperframes-kapak-b.md`). Tasarım verir; tam kod yok.
K = `/home/sef/01dev/_worktrees/kalem-0204`. D = `K/projeler/simple-present-temel-s2/sahneler/06-hyperframes-kapak-b/`. P = `K/projeler/simple-present-temel-s2/`.
Bağlayıcı: `/home/sef/01dev/dijital-anlatim/.claude/docs/huni-v2-standart.md` §1, §2, §6; `P/BRIEF-S2.md` "Kapak" B; `P/uretim-tutanagi/kapak-taslak.md` §4.

## 1. Dosyalar

| Dosya | İş |
|---|---|
| `D/uret.py` | **agy yazar** (yeni dosya): `/home/sef/01dev/_worktrees/kalem-0204/projeler/simple-present-temel-s2/sahneler/06-hyperframes-kapak-b/uret.py` |
| `D/yardim.py`, `D/calistir.sh`, `D/olay.py`, `D/zamanlar.json`, `D/cizim/` | DOKUNMA (şef kurdu: emsal kopyası + küçük Edit) |
| `D/nesneler.json`, `D/proje/index.html`, `D/proje/assets/fonts/` | uret.py yazar |

Başka dosyaya dokunma. Silme yok. Test, render, git YOK. `P/ortak/`, `P/zaman.json`, başka sahneler salt okunur.

## 2. Var olan kod ve alınacak kalıp

| Kaynak (salt okunur, mutlak yol) | Alınacak |
|---|---|
| `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s1/sahneler/05-hyperframes-kapak-b/uret.py` | iskelet: `AD`, `sys.path.insert(0, str(AD))` + `import yardim as Y`, `PAKET = AD.parent.parent`, `ORTAK = PAKET / "ortak"`; `zaman.json` + `zamanlar.json` doğrulaması (§3, AYNEN; çıktı adı `kapak-b.png`); başlık `<text>` konturu (`fill` murekkep, `stroke` zemin, `stroke-width="12"`, `stroke-linejoin="round"`, `style="font-kerning:none;paint-order:stroke fill"`, `xml:space="preserve"`); `hesapla_s()` döngüsü (önce 100 ile ölç, sonra 1'er küçült); `kesisim()`; HTML kabuğu (`Y.font_css()`, `Y.ZEMIN_CSS`, `#sahne{position:absolute;left:0;top:0;}`, `Y.zemin_html()`, `#root data-…`, `lib/gsap.min.js`, iki `tl.set`, `window.__timelines["main"]`); `__main__` (`proje/`, `Y.font_kopyala`, `proje/index.html`, `nesneler.json`, stdout). Karakter PNG, maske, numpy, PIL, `.kenar` filtresi ALINMAZ |
| `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s2/sahneler/05-hyperframes-kapak-b/uret.py` | `hesapla_s()` sol hizalı başlık tabanları (`T1 = 630 − 0,25·S`, `T2 = T1 + 1,26·S`); `soru_svg()` (Tabler `question-mark`, 2 yol, başları assert, `stroke` vurgu, `stroke-width = 26/q`) — §4.5 değerleriyle |
| `/home/sef/01dev/_worktrees/kalem-0204/projeler/simple-present-temel/sahneler/06-hyperframes-form/uret.py` | öğrenci başı okuma (satır 116–123: `re.findall(r'<path id="ogrbas-\d+"\s+d="([^"]+)"', …)`, 3 yol, `<g transform="translate(..) scale(..)" fill="none" stroke=… stroke-linecap="round" stroke-linejoin="round">`); `konusma_balonu()` el çizimi balon yolu (satır 102–110) — §4.4'teki uç değişikliğiyle |

## 3. Okuma ve sabitler

- `zaman.json`: `duragan` içinde `klasor == AD.name` TEK kayıt, `kare == 1`, `cikti == "kapak-b.png"`; `sahneler[]` içinde `AD.name` YOK (assert).
- `zamanlar.json`: `sure` 1.0 · `kare` 1 · `fps` 30 (assert). Anlatım, sözcük, altyazı dosyası OKUNMAZ.
- Renk yalnız `Y.RENK` (`zemin #1b1a17`, `murekkep #f3efe6`, `ikincil #c9c2b3`, `vurgu #f2a93b`); HTML'e başka hex yazılmaz.
- Bantlar: `X0, X1 = 60, 960` · `Y0, Y1 = 460, 1380` · `KANAL_Y = (280, 350)` · `KUNYE_Y = (360, 450)` · `GORSEL_Y = (820, 1380)`.
- Başlık: `BAS_X = 60` · `BASLIK_GEN = 894` (900 − 6 sağ kontur payı) · `S_UST = 190` · satırlar `"ALWAYS VARSA"`, `"HANGİ ZAMAN?"` (İ = U+0130).
- Baş: `KIT = ORTAK / "cizim" / "peeps-kit" / "ogrenci-bas.svg"` · `BS = 1.70` · `BAS_CIZGI = 4` (ekran px) · sol görünür kenar 60 · alt görünür kenar 1378.
- Balon: `BL_X = 524` · `BL_Y = 836` · `BL_W = 426` · `BL_H = 148` · `BL_R = 28` · `BL_CIZGI = 4` · uç `UC = (472, 1040)` · yazı `"always?"` Fredoka 700 `BL_YAZI = 72`.
- Soru: `Q = 24` · `QX = 939 − 16·Q` (= 555) · `QY = 1363 − 19·Q` (= 907) · çizgi 26 px.

## 4. Yerleşim (ölçülen değerler 15.11; uret.py hesaplar, assert eder)

```
y    0 ┌─────────────────────────────────────────────┐
       │                (boş zemin)                   │ 0–280
   291 │ [logo] @ydspublishing                        │ kanal 280–350 (Y.kunye_svg)
   420 │ Simple Present (YDT · BASIC)                 │ künye 360–450
   601 │ ALWAYS VARSA                                 │ başlık x 60, S 116, sol hizalı
   747 │ HANGİ ZAMAN?                                 │
   836 │ ╭────╮        ╭──────────────────────────╮   │ balon 524–950 × 836–984
       │ │saç │        │         always?          │   │
       │ │ ◉◉ │      ◄─╰──────────────────────────╯   │ kuyruk ucu (472, 1040)
  1014 │ │ yüz│                       ┌──┐            │ soru 734–952 × 1014–1376
       │ │    │                          │            │
  1376 │ ╰────╯                       •               │ baş 60–458 × 836–1378
  1920 └──────────────── boş ──────────────────────────┘ 1380–1920 boş (altyazı yok)
```

### 4.1 Kanal + künye
`Y.kunye_svg()` aynen (argümansız; `KONU = "Simple Present"`, rozet `YDT · BASIC`). uret.py künyeye kendi değer yazmaz.

### 4.2 Başlık — `<g id="baslik">` iki `<text>` (`bs-1`, `bs-2`)
- `S = floor(min(S_UST, BASLIK_GEN·100/g1_100, BASLIK_GEN·100/g2_100))` (`g = Y.genislik("Fredoka", 700, satır, …)`); sonra `g1, g2 ≤ BASLIK_GEN` olana kadar 1'er küçült. Beklenen `S = 116`, `g1 ≈ 887,3`, `g2 ≈ 835,1`.
- `T1 = 630 − 0,25·S` (= 601,0), `T2 = T1 + 1,26·S` (= 747,16). İki satır `x = BAS_X` (sol hizalı, künye ile aynı sol kenar), aynı boy.
- Kontur `stroke` zemin 12 → sol 6 px kontur zemin renginde, görünmez; blok kutusu x 60'tan başlar (§6.1).

### 4.3 Öğrenci başı — `<g id="bas">`
- KIT dosyasından 3 yol (`ogrbas-0..2`) okunur; yol komutları yalnız `M` ve `C` (assert).
- Kit kutusu: yolların bütün sayı çiftlerinin min/max'ı (kontrol noktaları dahil; eğri bu kutunun dışına çıkmaz). Beklenen
  `(kx0, ky0, kx1, ky1) = (−41,907, 5,467, 189,831, 322,116)`; ±0,01 assert.
- `BTX = 60 + BAS_CIZGI/2 − kx0·BS` (≈ 133,24) · `BTY = 1378 − BAS_CIZGI/2 − ky1·BS` (≈ 828,40).
- Öğe: `<g id="bas" transform="translate(BTX BTY) scale(BS)" fill="none" stroke=murekkep stroke-width="{BAS_CIZGI/BS}" stroke-linecap="round" stroke-linejoin="round">`
  + üç `<path id="bas-0|1|2" d="…"/>` (kitteki `d` aynen; `pathLength`, `style`, `clip-path` yazılmaz).
- Yüz sağa bakar (gözlük sapı sola uzanır); balon sağda olduğu için aynalama YOK.

### 4.4 Konuşma balonu — `<g id="balon" fill="none" stroke=murekkep stroke-width="4" stroke-linecap="round" stroke-linejoin="round">` + `<path id="balon-yol">`
- Yol işlevi `balon_yolu(x, y, w, h, ux, uy) -> str`: ana ders `konusma_balonu()` ile AYNI noktalar ve sıra (üst kenar, sağ kenar, alt kenar,
  sol alt köşe, sol kenar, sol üst köşe, `Z`; r = `BL_R`), tek fark sol kenardaki kuyruk: ana derste `L x,ty+46 L x−58,ty L x+2,ty−34` olan üç nokta
  burada `L x,b1 L ux,uy L x+2,b0`; `b1 = y + h − r − 2`, `b0 = b1 − 58`. Böylece kuyruk balonun sol altından aşağı-sola, yüze doğru iner.
- Değerler: `x = BL_X`, `y = BL_Y`, `w = BL_W`, `h = BL_H`, `(ux, uy) = UC` → `b1 = 954`, `b0 = 896`.
- Uç denetimi: `uy`'nin kit karşılığı `kyu = (uy − BTY)/BS` (≈ 124,5); yol 0'ın sayı çiftlerinden `|y − kyu| ≤ 12` olanların en büyük x'i
  → ekran `saç_sağ = BTX + x·BS` (≈ 449,6). Şart `ux − saç_sağ ≥ 16` (uç saça değmez).
- Yazı `<text id="balon-yazi">` (balon grubunun DIŞINDA): `always?`, Fredoka 700 `BL_YAZI`, `fill` murekkep, kontursuz, `text-anchor="middle"`,
  `xml:space="preserve"`; `x = BL_X + BL_W/2` (= 737), taban `= BL_Y + BL_H/2 + 0,28·BL_YAZI` (≈ 930,2).

### 4.5 Soru işareti — `<g id="soru" transform="translate(QX QY) scale(Q)" fill="none" stroke=vurgu stroke-width="{26/Q}" stroke-linecap="round" stroke-linejoin="round">`
- Yollar: `Y.tabler("question-mark", AD / "cizim")`; 2 yol; `[0]` `M8 8a3.5` ile, `[1]` `M12 19l0` ile başlar (assert). Tabler mürekkep kutusu x 8–16, y 5–19.
- Görünür kutu: x `8Q + QX − 13` … `16Q + QX + 13` (= 734–952), y `5Q + QY − 13` … `19Q + QY + 13` (= 1014–1376). Karenin tek sarısı
  (hf_tema `stroke="#f2a93b"` → açıkta `#d9900f`, koyuda `#f2a93b`; seri pilotu 02-04-s2 kapak B ile aynı).

## 5. Tema (hf_tema.py ile uyum)
- `Y.ZEMIN_CSS`, `Y.zemin_html()`, `Y.font_css()` DEĞİŞTİRMEDEN. Ek CSS yalnız `#sahne{position:absolute;left:0;top:0;}`.
- Renkler SVG özniteliği, küçük harf hex. `#root.tema-acik` dizgisi HTML'de GEÇMEZ (geçerse hf_tema tema değişkenlerini eklemez).
- Kanal logosu kimliği `logoimg` (yardim.py); `calistir.sh` tema logosunu `proje/assets/logo.svg` olarak kopyalar.

## 6. Kurallar ve kabul ölçütü (uret.py içinde `assert`)
1. Bloklar `{ad, x, y, w, h}` (kutu payları):
   `kanal` (x 60, y 291, sağ = 263 + genişlik(`@ydspublishing`, Lexend 700, 42), alt 339) ·
   `kunye` (x 60, y = min(386, 420 − 0,75·`Y.konu_boyu()`), sağ = `Y.rozet_konumu()` x + genişlik, alt = max(434, 420 + 0,25·konu_boyu)) ·
   `baslik` (x 60 … `60 + max(g1, g2) + 6`; y `T1 − 0,86·S − 6` … `T2 + 0,10·S + 6`) ·
   `bas` (kit kutusunun ekran karşılığı ± `BAS_CIZGI/2`: ≈ 60–458 × 835,7–1378) ·
   `balon` (balon gövdesi, kuyruksuz: x `BL_X − 4` … `BL_X + BL_W + 6`; y `BL_Y − 3` … `BL_Y + BL_H + 5`; el çizimi kayması + çizgi payı) ·
   `kuyruk` ((x, b0), (x, b1), (ux, uy) noktalarının kutusu ± 2) ·
   `balon-yazi` (x `737 − w/2`, üst `taban − 0,75·BL_YAZI`, w genişlik(`always?`), h `1,0·BL_YAZI`) ·
   `soru` (§4.5 görünür kutu).
2. `kanal` ⊂ x [60, 960] × y [280, 350]; `kunye` ⊂ x [60, 960] × y [360, 450]; öteki bütün bloklar ⊂ x [60, 960] × y [460, 1380];
   `balon` sağı ≤ 958. Böylece 0–280 ve 1380–1920 boş, sağ 960–1080 boş.
3. Kesişim 0: `kanal`, `kunye`, `baslik`, `bas`, `balon`, `kuyruk`, `soru` bütün çiftleri; tek istisna (`balon`, `kuyruk`) (kuyruk balona bağlıdır).
   `balon-yazi` ⊂ `balon` iç kutusu (x `BL_X + 24` … `BL_X + BL_W − 24`, y `BL_Y + 16` … `BL_Y + BL_H − 16`).
   Boşluk: `balon.y − baslik.alt ≥ 40`; `bas.y − baslik.alt ≥ 40`; `soru.y − balon.alt ≥ 20`; `kuyruk.x − bas.sağ ≥ 8`; `soru.x − bas.sağ ≥ 32`;
   §4.4 uç şartı (`ux − saç_sağ ≥ 16`).
4. Yazı boyu ≥ 64 (kanal 42 ve künye ≤ 34 / 26 hariç): `S ≥ 64`, `BL_YAZI ≥ 64`. Başlık 2 satır, toplam 4 sözcük. Her satır ≤ 24 karakter
   (`ALWAYS VARSA`, `HANGİ ZAMAN?`, `always?`). `HANGİ` içinde U+0130 var.
5. Görünen metin taraması: bütün `<text>` içerikleri (regex `>([^<]+)</text>`) küçük harfe çevrilir; `izle` ve `qr` YOK; U+2FFF üstü karakter
   (emoji) YOK. Yasak söz listesi (standart §1 kural 4–5) koda literal YAZILMAZ — denetim dış `grep` ile (sözleşme, S1 s04).
6. Bütün HTML'de (küçük harf) YOK: `math.random`, `date.now`, `new date`, `opacity:0`, `#root.tema-acik`. HTML'deki her `#rrggbb` değeri
   `Y.RENK`'in zemin/murekkep/ikincil/vurgu kümesinde. `id="kanal"` ve `id="logoimg"` TAM bir kez. `<img` YOK.
7. Yasak: kırmızı, yeşil, gradyan (zemin vinyeti dışında), gölge, filtre (gren dışında), try/except, tween (iki `set` dışında). Python: tür ipuçları
   bütün işlevlerde; yalnız standart kütüphane + `yardim` (numpy, PIL yok).
8. Zaman çizelgesi: `tl.set("#sahne", {opacity: 1, immediateRender: false}, 0)` ve `…, Z["sure"])`; `window.__timelines["main"]`.
9. `nesneler.json`: `[{"ad", "x", "y", "w", "h"}]` tam sayı; sıra `kanal, kunye, baslik, bas, balon, kuyruk, balon-yazi, soru`.
10. `/usr/bin/python3 uret.py` stdout: `index.html yazıldı <bayt>` ve `S=<S> BS=<BS> Q=<Q> uc=<ux>,<uy> sac_sag=<…>`; çıkış 0.

Kabul (şef koşturur, ajan koşturmaz): `bash calistir.sh --tema acik|koyu` → `P/kapak-b.png` ve `D/k/koyu/kapak-b-koyu.png` 1080×1920;
taşma, kesik yazı, üst üste binme yok; kanal katmanı görünür; 0–280, 1380–1920 ve x 960–1080 boş.
