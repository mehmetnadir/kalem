# SPEC — 02-04-ydt-temel-s1 · sahne 07-hyperframes-hikaye-b (HyperFrames, 1080×1920, tek kare, ses yok)

Yazan: şef (15.11.2026, istem S1-VAR). Kod yazmaz; tasarım verir. K = `/home/sef/01dev/_worktrees/kalem-0204`.
Sahne dizini D = `K/projeler/02-04-ydt-temel-s1/sahneler/07-hyperframes-hikaye-b/`. Paket P = `K/projeler/02-04-ydt-temel-s1/`.
Kaynak: `P/uretim-tutanagi/hikaye-taslak.md` §6. Hikâye B = soru kartı: Türkçe cümle + "Hangisi doğru?" + iki seçenek; CEVAP YOK.

## 1. Dosyalar

| Dosya | Durum | İş |
|---|---|---|
| `D/uret.py` | YOK | **YAZILACAK** (mutlak yol `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s1/sahneler/07-hyperframes-hikaye-b/uret.py`) |
| `D/yardim.py` | VAR (sahne 01'in birebir kopyası) | DOKUNMA; yalnız `import yardim as Y` |
| `D/calistir.sh`, `D/olay.py`, `D/zamanlar.json` | VAR (şef yazdı) | DOKUNMA |
| `D/nesneler.json` | uret.py yazar | §6 |

Başka dosyaya dokunma. Silme yok. Test, render, snapshot, `calistir.sh`, git YOK. `P/ortak/`, `P/zaman.json` ve başka sahneler salt okunur.

## 2. Kalıp (salt oku) — en yakın örnek

`K/projeler/02-04-ydt-temel-s1/sahneler/04-hyperframes-hikaye/uret.py` (hikâye A). Bu sahne onun kardeşidir; aynısını al:
- Dosya düzeni, `zaman.json` / `zamanlar.json` doğrulaması (§3'teki farkla), sabitler, HTML kabuğu, tek `set` çizelgesi, `__main__`.
- `kunye_svg()` (satır 87–115) BİREBİR; tek fark çip metni `Full lesson` → **`Quiz`**.
- Kart çerçevesi (`kart_svg` içindeki `crv`: x 48, w 984, rx 28, `fill="none"`, `stroke` murekkep 4).
- Çağrı bandı: `cg1`, `cg2` (Caveat 700 72, x 48, taban 1418 ve 1498), `@ydspublishing` hapı (sağa hizalı, y 1398, h 84, rx 42, Fredoka 700 64).
- `blok_kutulari`, `kesisim`, `kurallari_dogrula` kalıbı (bloklar §6'ya göre değişir).
Kart içeriği (ikon, etiket, bant, now noktası, altçizgi) bu sahnede YOK.

## 3. Okuma ve sabitler

- `PAKET = AD.parent.parent`. `PAKET/zaman.json` oku. `duragan` listesinde `klasor == AD.name` olan TEK kayıt var assert; kaydın
  `kare == 1` ve `cikti == "hikaye-b.png"` assert. `sahneler[]` içinde `AD.name` YOK assert. (`hikaye` alanı sahne 04'ündür; okuma.)
- `Z = D/zamanlar.json`: `sure` 1,0 · `kare` 1 · `fps` 30 assert.
- Renk yalnız `Y.RENK`: `zemin #1b1a17`, `murekkep #f3efe6`, `ikincil #c9c2b3`, `vurgu #f2a93b`. Başka hex YOK.
- `W, H = Y.W, Y.H`; `KENAR = 48`; `SAG = 1032`; `ICERIK = (352, 1392)`; `CAGRI = (1344, 1536)`; `PLATFORM = 1536`.

## 4. Yerleşim (y = yazı tabanı, px; x sol kenar)

```
y    0 ┌───────────────────────────────────────────┐
       │ [logo]                              [Quiz] │ HUD (sahne 04 ile aynı, çip Quiz)
   212 │ SIMPLE PRESENT vs                         │
   276 │ PRESENT CONTINUOUS  (YDT · BASIC)          │
   440 │ Şimdilik amcamla                           │ Fredoka 700 88
   540 │ yaşıyorum.                                 │ Fredoka 700 88
   660 │ (Hangisi doğru?)                           │ sarı hap 596–680
   716 │ ┌ kart A ───────────────────────────────┐  │ 716–976
       │ │ (A)  I live                            │  │
       │ │      with my uncle.                    │  │
  1008 │ ┌ kart B ───────────────────────────────┐  │ 1008–1268
       │ │ (B)  I am living                       │  │
       │ │      with my uncle.                    │  │
  1418 │ Cevap tam derste:        [@ydspublishing]  │ Caveat 72 · hap sağa hizalı
  1498 │ profildeki bağlantı                        │ Caveat 72
  1536 ├───────────────────────────────────────────┤ PLATFORM: boş
```

### 4.1 İçerik
| # | id | Öğe | Ölçü | Renk |
|---|---|---|---|---|
| 1 | `tr1` | `Şimdilik amcamla` | Fredoka 700 88, x 48, taban 440 | murekkep |
| 2 | `tr2` | `yaşıyorum.` | Fredoka 700 88, x 48, taban 540 | murekkep |
| 3 | `soru` (grup) | hap `<rect>` | x 48, y 596, h 84, rx 42, w = `Y.genislik("Fredoka", 700, "Hangisi doğru?", 64) + 56` | `fill` vurgu |
| 4 | `soru` yazısı | `Hangisi doğru?` | Fredoka 700 64, `text-anchor="middle"`, x = hap ortası, taban 596 + 42 + 22 = 660 | `fill` zemin (`#1b1a17`) |
| 5 | `kA` (grup) | seçenek kartı A | y0 = 716; §4.2 | §4.2 |
| 6 | `kB` (grup) | seçenek kartı B | y0 = 1008; §4.2 | §4.2 |
| 7 | `cg1` | `Cevap tam derste:` | Caveat 700 72, x 48, taban 1418 | murekkep |
| 8 | `cg2` | `profildeki bağlantı` | Caveat 700 72, x 48, taban 1498 | murekkep |
| 9 | `hap` | `@ydspublishing` hapı | sahne 04 ile aynı | sahne 04 ile aynı |

Tek vurgu `soru` hapıdır (ve HUD rozeti, çağrı hapı — bunlar kalıbın parçası). Başka sarı öğe, altçizgi YOK.

### 4.2 Seçenek kartı (y0 = 716 ya da 1008; iki kart BİREBİR aynı biçim)
| Öğe | Ölçü | Renk |
|---|---|---|
| çerçeve `<rect>` | x 48, y y0, w 984, h `KART_H = 260`, rx 28, `fill="none"`, `stroke-width` 4 | `stroke` murekkep |
| harf dairesi `<circle>` | merkez (136, y0 + 130), r 52, `fill="none"`, `stroke-width` 4 | `stroke` murekkep |
| harf | Fredoka 700 64, `text-anchor="middle"`, x 136, taban y0 + 130 + 22. Kart A `A`, kart B `B` | `fill` murekkep |
| satır 1 | Fredoka 700 72, x 228, taban y0 + 112. Kart A `I live`, kart B `I am living` | `fill` murekkep |
| satır 2 | Fredoka 700 72, x 228, taban y0 + 202. İki kartta `with my uncle.` | `fill` murekkep |

- id: `kA-crv`, `kA-daire`, `kA-harf`, `kA-s1`, `kA-s2` (B için `kB-…`). Her `<text>` `xml:space="preserve"`.
- Cevap belirtisi YOK: tik, çarpı, renk farkı, kalın çerçeve, altçizgi, ikon (ev/bavul ipucu verir) YOK.

## 5. Tema (hf_tema.py ile uyum)
- `Y.ZEMIN_CSS` ve `Y.zemin_html()` DEĞİŞTİRMEDEN kullan. Renkler SVG özniteliği, küçük harf hex; CSS `style` içinde renk YOK.
- Dönüşüm: `rect fill #f2a93b` → açıkta `#ffe066` · `text fill #1b1a17` → `#1b2440` · `fill/stroke #f3efe6` → `#1b2440`.
  Hap ve rozet dolgusu `<rect fill="#f2a93b">`; hap/rozet/soru yazısı `<text fill="#1b1a17">`. `<circle fill="#1b1a17">` YOK (daireler `fill="none"`).
- id `t2`, `ku-nokta`, `rz1` KULLANMA.

## 6. Kurallar ve kabul ölçütü (uret.py içinde `assert`)
1. Bütün metin ve kutular x ∈ [48, 1032]; hiçbir öğe y ≥ 1536 değil (yazı alt sınırı = taban + 0,30·boy).
2. Yazı boyu ≥ 64 (HUD hariç: ders adı 56, rozet 36, çip 40).
3. Her ekran satırı ≤ 24 karakter (`len`), HUD dahil.
4. Blok kutuları çakışmaz. Yazı kutusu y_üst = taban − 0,75·boy, y_alt = taban + 0,30·boy (Caveat) / 0,25·boy (diğer).
   Bloklar: `hud` (0–288) · `tr` (tr1+tr2) · `soru` · `kA` · `kB` · `cg1` · `cg2` · `hap`. Çiftler arası kesişim 0; dikey komşular arası
   boşluk ≥ 16 (istisna: `cg1`–`cg2`, yalnız kesişim 0); `cg1` ve `cg2` sağ kenarı ile `hap` sol kenarı arası ≥ 24.
   Kart içi: satır 1 ve satır 2 sağ kenarı ≤ 1000; harf dairesi sağı (188) ile yazı solu (228) arası ≥ 24.
5. `tr` üstü ≥ 352; `kB` altı ≤ 1344; `hap`, `cg1`, `cg2` [1344, 1536] içinde.
6. `nesneler.json`: `[{"ad", "x", "y", "w", "h"}]` tam sayı (yukarıdaki bloklar).
7. Yasak: emoji, kırmızı, yeşil, gradyan, gölge, `Math.random`, `Date`, try/catch, `opacity:0` başlangıç, hareket (tek `set` dışında tween yok).
8. Ekranda "kanal", QR, süre, cevap YOK. Python: tür ipuçları bütün işlevlerde.
9. `/usr/bin/python3 uret.py` stdout'a `index.html yazıldı <bayt>` basar; hata yoksa çıkış 0.

Kabul (şef koşturur, ajan koşturmaz): `ONIZLE_YALNIZ=1 bash calistir.sh` → "önizleme hazır"; `bash calistir.sh --tema acik|koyu` →
`P/hikaye-b.png` ve `D/k/koyu/hikaye-b-koyu.png` 1080×1920; taşma, kesik yazı, üst üste binme yok.
