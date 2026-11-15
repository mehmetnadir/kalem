# SPEC v2 — 02-04-ydt-temel-s2 · sahne 06-hyperframes-kapak-c (huni v2; HyperFrames, 1080×1920, tek kare, ses yok)

Yazan: şef (15.11.2026, istem D-S2-V2). Kod yazmaz; tasarım verir. K = `/home/sef/01dev/_worktrees/kalem-0204`.
Sahne dizini D = `K/projeler/02-04-ydt-temel-s2/sahneler/06-hyperframes-kapak-c/`. Paket P = `K/projeler/02-04-ydt-temel-s2/`.
Bağlayıcı: `/home/sef/01dev/dijital-anlatim/.claude/docs/huni-v2-standart.md` §1–§2, §6 · `P/BRIEF-S2.md` "Yerleşim" + "Kapak B ve Kapak C" C sütunu.
v1 (SPEC, RAPOR, kod) yedeği: `~/Silinecekler/2026-11-15-huni-v2/02-04-ydt-temel-s2/sahneler/06-hyperframes-kapak-c/`.
İçerik v1 ile aynı (başlık, iki kart, mont, tişört, tek sarı altçizgi). Değişen yalnız yerleşim: v1 HUD (0–288) kalkar, v2 bantları gelir.

## 1. Dosyalar

| Dosya | Durum | İş |
|---|---|---|
| `D/uret.py` | VAR (v1) | **YERİNDE DÜZENLE** — mutlak yol `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s2/sahneler/06-hyperframes-kapak-c/uret.py` |
| `D/yardim.py` | VAR (v2; şef S2 sahne 01 v2 kopyasını koydu) | DOKUNMA; `import yardim as Y`; künye `Y.kunye_svg()` |
| `D/calistir.sh`, `D/olay.py`, `D/zamanlar.json` | VAR (v2) | DOKUNMA |
| `D/nesneler.json` | uret.py yazar | §6 madde 6 |

Başka dosyaya dokunma. Silme yok. Test, render, snapshot, `calistir.sh`, git YOK. `P/ortak/`, `P/zaman.json`, başka sahneler salt okunur.

## 2. Kalıp (salt oku)

| Kalıp | Mutlak yol | Ne alınır |
|---|---|---|
| v1 kod (aynı sahne) | `D/uret.py` | dosya düzeni KORUNUR: `zaman.json` + `zamanlar.json` assert'leri (aynen) · `MONT` / `TISORT` dizileri (aynen) · `ikon_cizim_svg` (yalnız `IKON_X` sabitine bağlanır) · `kesisim` · HTML kabuğu (aynen) · `__main__` (aynen) |
| v2 künye | `D/yardim.py` `kunye_svg()`, `HUD`, `konu_boyu()`, `rozet_konumlari()`, `genislik()` | uret.py'deki YEREL `kunye_svg()` SİLİNİR; yerine `Y.kunye_svg()` çağrılır |
| v2 kapak hizası | `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s2/sahneler/01-hyperframes-kapak/uret.py` satır 65 (`SOL = 60`), 424 | başlık sol hizalı `x = 60`; başlık konturu `stroke` zemin `stroke-width="12"` (v1 ile aynı öznitelikler) |

## 3. Sabitler (v1 sabitlerinin YERİNE)

```
SOL = 60 · SAG = 960 · ICERIK_UST = 460 · BASLIK_ALT = 800 · SAHNE_UST = 820 · ICERIK_ALT = 1380 · ALTYAZI_UST = 1400
BASLIK_GEN = 900 · KART_H = 256 · KART_ARA = 28 · YAZI_X = 100 · IKON = 140 · IKON_X = 790 (= SAG − 30 − IKON)
```
v1 sabitleri `KENAR 48`, `SAG 1032`, `BASLIK_GEN 952`, `SAHNE_UST 864`, `SAHNE_ALT 1344`, `PLATFORM 1536`, `IKON_X 862` KALKAR.
Renk yalnız `Y.RENK`: `zemin`, `murekkep`, `vurgu`. Başka hex YOK.

Künye doğrulaması (uret.py başında assert; yardim.py v2 değilse dur):
`Y.HUD["logoY"] == 291`, `Y.HUD["logoYuk"] == 48`, `Y.HUD["kanalX"] == 263`, `Y.HUD["kanalTaban"] == 330`, `Y.HUD["kanalYazi"] == 42`,
`Y.HUD["konuX"] == 60`, `Y.HUD["konuTaban"] == 420`, `Y.HUD["rozetY"] == 386`, `Y.HUD["rozetH"] == 48`, `Y.HUD["rozetYazi"] == 26`,
`Y.ROZET == "YDT · BASIC"`, `Y.KONU == "Simple Present vs Present Continuous"`; `Y.kunye_svg()` çıktısında `id="kanal"`, `id="logoimg"`,
`@ydspublishing` geçer; `id="ku-cip"` GEÇMEZ.

## 4. Olay listesi

| Olay | Kare / küresel sn | Cümle sözcüğü |
|---|---|---|
| kare tam görünür (iki `set`, hareket yok) | kare 0 · zaman çizelgesi dışı (`zaman.json` → `duragan`) · yakalama 0,5 sn | yok — ses yok |

`olaylar.json` = `[]` (`olay.py` yazar). Tween YOK: kanal katmanı, künye, başlık, kartlar hiçbir `to`/`from`/opaklık/ölçek hareketine girmez.

## 5. Yerleşim (y = yazı tabanı, px; beklenen değerler S = 151, B = 72)

```
y    0 ┌──────────────────────────────────────┬────┐
       │ yalnız zemin (0–280)                 │    │ sağ 960–1080: platform arayüzü
   291 │ [logo 193,5×48] @ydspublishing      │    │ kanal katmanı 280–350  (Y.kunye_svg)
   420 │ Simple Present vs Present Continuous (YDT · BASIC)  künye 360–450
   460 │ ┄ başlık kutusu üstü (İ noktası + kontur)    │
  ≈606 │ AYNI FİİL,                           │    │ Fredoka 700 S, mürekkep + zemin konturu, hapsız
  ≈786 │ İKİ ZAMAN                            │    │ x 60, sol hizalı
   800 │ ┄ başlık kutusu altı                 │    │
   840 │ ┌ kart 1 ────────────────── [mont] ┐ │    │ 840–1096
   936 │ │ She wears her coat               │ │    │ Fredoka 700 B
  1036 │ │ in the winter.                   │ │    │
  1124 │ ┌ kart 2 ────────────────── [tişört]┐│    │ 1124–1380
  1220 │ │ She is wearing her               │ │    │ "is wearing" altında sarı el altçizgisi
  1320 │ │ pink T-shirt today.              │ │    │
  1380 └──────────────────────────────────────┘    │
  1400 │ boş (altyazı bandı; ses yok)                  1400–1920 yalnız zemin
```

### 5.1 Kanal katmanı + künye
- `kunye = Y.kunye_svg()` (logo `<image id="logoimg">` x 53,15 y 291 h 48 w 193,5 · `@ydspublishing` Lexend 700 42 x 263 taban 330 ·
  konu Fredoka 700 `Y.konu_boyu()` x 60 taban 420 · rozet hapı y 386–434). SVG'de İLK grup. Değer YAZMA, yardim.py verir.
- v1'deki yerel `kunye_svg()` (logo y 48 h 96, rozet y 216) TAMAMEN kalkar. Çip YOK.

### 5.2 Başlık — `<g id="baslik">` (hapsız, tek renk)
- Metin: satır 1 `AYNI FİİL,` · satır 2 `İKİ ZAMAN` (büyük noktalı İ = U+0130).
- `g(m, s) = Y.genislik("Fredoka", 700, m, s)`; `gmax(s) = max(g(satır1, s), g(satır2, s))`.
- Boy: `S = floor(min(190, BASLIK_GEN·100 / gmax(100), (BASLIK_ALT − ICERIK_UST − 12) / 2,17))` → beklenen 151 (yüksekliği bant sınırlar).
  Assert: `gmax(S) ≤ 900` · `S ≥ 64`.
- Taban: `T1 = ICERIK_UST + 6 + 0,93·S` (İ noktası 0,921 em + kontur 6) · `T2 = T1 + 1,19·S` (v1 satır aralığı; virgül kuyruğu ile İ noktası arası ≥ 0,10·S).
  Beklenen T1 ≈ 606,4 · T2 ≈ 786,1.
- `x = SOL` (60), iki satır aynı x, `text-anchor` YOK (sol hizalı).
- İki `<text>` id `bs-1`, `bs-2`: Fredoka 700 S; `fill` murekkep; `stroke` zemin, `stroke-width="12"`, `stroke-linejoin="round"`,
  `style="font-kerning:none;paint-order:stroke fill"` (v1 ile aynı). Başlıkta sarı YOK (kutu, hap, altçizgi, renkli sözcük yok).
- Başlık kutusu (kesişim ve bant denetimi için): `x = SOL`, `w = gmax(S) + 6`, `y = T1 − 0,93·S − 6`, `h = (T2 + 0,05·S + 6) − y`.
  Assert: `y ≥ 460` · `y + h ≤ 800` · `x + w ≤ 960`.

### 5.3 Kartlar — `<g id="kart1">`, `<g id="kart2">`
| Ölçü | Değer |
|---|---|
| Kart dış kutusu | x 60–960 (w 900); `ust1 = ICERIK_ALT − 2·KART_H − KART_ARA` = 840; kart 1 y 840–1096; kart 2 y `ust2 = ust1 + KART_H + KART_ARA` = 1124 → 1380 |
| Çerçeve `<rect id="k1-crv">` / `k2-crv` | x 62, w 896, y = dış üst + 2, h 252, rx 24, `fill="none"`, `stroke` murekkep, `stroke-width="4"` |
| Yazı | Fredoka 700 B; `B = 72`; 4 satırdan biri `YAZI_X + g(satır, B) + 32 > IKON_X` ise B 1'er küçülür; assert `B ≥ 64` |
| Yazı x | `YAZI_X` = 100 (sol hizalı, iki satır) |
| Taban | satır 1 = dış üst + 96 · satır 2 = dış üst + 196 → kart 1: 936 / 1036 · kart 2: 1220 / 1320 (satır aralığı 100, v1 ile aynı) |
| Yazı öznitelikleri | `fill` murekkep, KONTURSUZ, `style="font-kerning:none"` |
| id | `k1-s1`, `k1-s2`, `k2-s1`, `k2-s2` |

Ekran metni (BİREBİR, v1 ile aynı): kart 1 `She wears her coat` / `in the winter.` · kart 2 `She is wearing her` / `pink T-shirt today.` (`T-shirt` tireli).

### 5.4 Tek vurgu — `<path id="k2-alti">` (kart 2, `is wearing` altı)
- `x0 = YAZI_X + g("She ", B) − 4` · `x1 = YAZI_X + g("She is wearing", B) + 4` (beklenen ≈ 231 → 568).
- `y = kart 2 satır 1 tabanı + 0,40·B` (≈ 1248,8; v1 QA 1 değeri).
- `d = "M{x0} {y} Q{(x0+x1)/2} {y+3} {x1} {y+1}"`; `fill="none"`, `stroke` vurgu, `stroke-width="10"`, `stroke-linecap="round"` (v1 ile aynı).
- Kartta, başlıkta ve ikonlarda başka sarı YOK. `today` ve `wears` vurgusuz. (Rozet hapı künye öğesidir, vurgu sayılmaz.)

### 5.5 Köşe ikonları — `<g id="mont">` (kart 1), `<g id="tisort">` (kart 2)
- Kutu x `IKON_X`–`IKON_X + 140` (790–930), y = dış üst + 28 … + 168 (sağ üst köşe).
- `ikon_cizim_svg` v1 ile aynı; içindeki sabit `862.0` → `IKON_X` (iki yerde: `ox` hesabı). Izgara, eğri, daire kuralları değişmez.
  Beklenen: mont kutusu x 801,7 w 116,7 y 868 h 140 · tişört x 790 w 140 y 1159 h 126.
- Grup öznitelikleri v1 ile aynı (`fill="none"`, `stroke` murekkep 4, yuvarlak uç/birleşim). Pembe YOK.

## 6. Kurallar ve kabul ölçütü (uret.py içinde `assert`)

1. Bant: kanal ve künye dışındaki her blok `x ≥ 60`, `x + w ≤ 960`, `y ≥ 460`, `y + h ≤ 1380`. 0–280 ve 1400–1920'de blok YOK.
   Başlık `460 ≤ y`, `y + h ≤ 800`; kartlar ve çocukları `y ≥ 820`.
2. Kanal kutusu `kanal` = (60, 291, `263 + Y.genislik("Lexend", 700, "@ydspublishing", 42) − 60`, 52) → y 280–350 içinde, `x + w ≤ 960`.
   Künye kutusu `kunye` = (60, 386, `rx + rw − 60`, 48), `(rx, rw) = Y.rozet_konumlari()[0]` → y 360–450 içinde, `x + w ≤ 960`.
3. Yazı boyu: başlık S ≥ 64, kart B ≥ 64 (kanal 42, konu ≤ 34, rozet 26 hariç). Başlık 2 satır. Her satır ≤ 24 karakter
   (başlık 2 satır, kart 4 satır, rozet).
4. Kesişim 0: üst düzey `kanal`, `kunye`, `baslik`, `kart1`, `kart2` çiftleri. Başlık–künye arası `baslik.y − 450 ≥ 10`;
   `kart1.y − (baslik.y + baslik.h) ≥ 20`.
5. Kart içi (her kart): satır 1, satır 2, ikon (çizilen kutu) çiftler arası kesişim 0; hepsi kart iç kutusunda (dış kutu her yandan 4 px içeri).
   `k2-alti` kutusu (x0, y − 5, x1 − x0, 12): üstü ≥ `k2-s1` alt · altı ≤ `k2-s2` üst. Yazı kutusu: y_üst = taban − 0,75·B, h = B, w = `g(satır, B)`.
   Her satır `YAZI_X + g(satır, B) + 32 ≤ IKON_X`.
6. `nesneler.json`: `[{"ad", "x", "y", "w", "h"}]` tam sayı; sıra: kanal, kunye, baslik, kart1, k1-s1, k1-s2, mont, kart2, k2-s1, k2-s2, k2-alti, tisort.
7. Yasak: emoji, kırmızı, yeşil, pembe, gradyan, gölge, `Math.random`, `Date`, try/except, `opacity:0` başlangıç, hareket (iki `set` dışında
   tween yok), figür, karakter görseli, altyazı öğesi, çip, sol alt logo, QR, oynat/izle düğmesi.
8. Ekran metninde `Tam ders`, `dakika`, `dk` YOK. Python: bütün işlevlerde tür ipuçları; satır ≤ 140 karakter.
9. `/usr/bin/python3 uret.py` stdout'a `index.html yazıldı <bayt>` ve `S=<başlık boyu> B=<kart boyu>` basar; hata yoksa çıkış 0.

Kabul (şef koşturur, ajan koşturmaz): `ONIZLE_YALNIZ=1 bash calistir.sh` → "önizleme hazır"; `bash calistir.sh --tema acik|koyu` →
`P/kapak-c.png` ve `D/k/koyu/kapak-c-koyu.png` 1080×1920; kanal katmanı yerinde; taşma, kesik yazı, üst üste binme yok; altçizgi `g` kuyruğuna değmez.
