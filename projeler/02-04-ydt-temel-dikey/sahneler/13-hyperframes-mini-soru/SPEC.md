# SPEC — 02-04-ydt-temel-dikey · sahne 13-hyperframes-mini-soru (HyperFrames, 1080×1920, 940 kare)

Kaynak: `projeler/02-04-ydt-temel-dikey/BRIEF-DIKEY.md` §2 + §3 satır 13. Yazan: şef (15.11.2026). Kod yazmaz; tasarım verir.
MAKİNE: Linux x86_64 (srv21). K = `/home/sef/01dev/_worktrees/kalem-0204`.
D = `K/projeler/02-04-ydt-temel-dikey/sahneler/13-hyperframes-mini-soru/`. Ağır adım yok (fontTools ölçümü derlemede bir kez).

## 1. Dosyalar

| Dosya | Durum | İş |
|---|---|---|
| `D/uret.py` | YOK | §4–§7'ye göre YAZ (tek iş bu) |
| `D/yardim.py` | VAR (dikey sahne 01 kopyası) | DOKUNMA. `Sahne`, `u`, `genislik`, `el_cizgi`, `el_ok`, `tik_yolu`, `balon_sol`, `kunye_svg`, `altyazi_svg`, `altyazi_dilimleri`, `html`, `kontrol`, `RENK`, `ORTAK`, `LOGO_EN_BOY` buradan |
| `D/olay.py` | VAR | DOKUNMA. `s, _ = U.uret()` ve `U.Z["kare"]` ister |
| `D/calistir.sh` | VAR | DOKUNMA |

Başka dosyaya dokunma. Silme yok. Test, render, git yok. `ortak/`, BRIEF, yatay paket salt okunur.

## 2. Kalıp kaynakları (salt oku)

| Kalıp | Mutlak yol | Ne alınır |
|---|---|---|
| Aynı içerik, yatay | `K/projeler/02-04-ydt-temel/sahneler/13-hyperframes-mini-soru/uret.py` | iskelet: `SAH`/`Z`/`SOZ` okuma, `T(c, i, bas)` sözcük assert'i, `yerlestir()` fikri, `pil()` parça çizimi, öğrenci başı okuma (`re.findall` 3 path), `bas%d` draw komutları, balon sözcükleri, `#balg` sönmesi, `dogru` kurgusu, `NOT` döngüsü (imleç → pil → satır soluklaşır), `Y.kontrol`. Ölçüler/yerleşim ALINMAZ (yatay) |
| Dikey iskelet (aynı paket) | `K/projeler/02-04-ydt-temel-dikey/sahneler/01-hyperframes-giris/uret.py` | `PAKET`, `Z` sözlüğü, `uret()` → `(s, kun)` dönüşü, `__main__` (index.html yazımı, sayım satırı), altyazı SVG'sinin `ek=` ile geçmesi |
| Altyazı aç/kapa (tek dilim görünür) | `K/projeler/present-continuous-dikey/sahneler/06-hyperframes-form/uret.py` satır 303–320 | kare kare tarama: `aktif(t)` = `t0 − 0,05 ≤ t < t1 + 0,35` koşulunu sağlayan SON dilim; değişince eskisine `set opacity 0`, yenisine `set opacity 1` (`#alt{i}`) |
| HUD sayıları | `K/projeler/02-04-ydt-temel-dikey/ortak/kunye.js` `KUNYE`, `kunyeCiz` | aşağıda §4.2 |
| Tema eşlemesi | `K/projeler/present-continuous/ortak/hf_tema.py` satır 17–28 | uret.py KOYU hex yazar; tablo §6 |

## 3. Zaman ve veri (sabit yazma; dosyadan oku)

- `PAKET = AD.parent.parent`; `zaman.json` → `klasor == AD.name` (t_bas 220,33 · kare 940). `Z = {t_bas, kare, sure = kare/30}`.
- `PAKET/ortak/anlatim/sozcukler.json` → `SOZ[c]` (c = 15, 16, 17), cümle içi sıra `i`. Yerel sn = küresel − t_bas (`s.S()`).
- Her zaman `T(c, i, bas)` ile alınır (yatay işlevin aynısı; sözcük kayarsa assert). Kullanılan sözcükler:
  15: 0 Mini · 2 My · 3 brother · 4 lives · 5 in · 6 Ankara, · 7 but · 8 this · 9 month · 10 he · 11 with · 12 us. · 13 Boşluğa · 17 Beş.
  16: 0 Bence … 6 durum. (7 sözcük). 17: 0 Ankara'da · 6 bu · 13 geçici · 17 B · 20 is · 22 C · 25 E · 27 özneyle · 28 uyumsuz. · 29 D · 31 tek.

## 4. Yerleşim (1080×1920 mantıksal px; dikey `u(n) = n`; bantlar BRIEF §2)

```
y   48 ┌ logo 387×96 (48,48)                      [ Mini question ] çip ┐  HUD 0–320, kare 0'dan sabit
   212 │ SIMPLE PRESENT vs                                               │  ders satır 1 (Fredoka 700 56)
   276 │ PRESENT CONTINUOUS  ( YDT · TEMEL )                             │  ders satır 2 + rozet hapı
   380 ├─ MINI QUESTION ─────────────────────────────────────  ( 5 ) ──┤  kart üst kenarı; etiket kenarın ÜSTÜNDE (lejant)
   472 │  My brother lives in                                            │  kök satır 1  Fredoka 700 72
   558 │  Ankara, but this month                                         │  kök satır 2
   644 │  he [ __is living__ ] with us.                                  │  kök satır 3 (boşluk)
   712 └─────────────────────────────────────────────────────────────────┘
   730 ┌ > A) lives        ( this month → temporary )                    ┐  şık satırı 80 px, adım 88
   818 │   B) is living  ████████████████████████████████████████ ✓      │  doğru: satır dolgusu + tik
   906 │ > C) live         ( he ↔ live )                                 │
   994 │ > D) to live      ( to live: no tense )                         │
  1082 │ > E) are living       ( he ↔ are )                              │  satır 5 altı 1162
  1198 │ [baş]  ( Bence A şıkkı.                  )                      │  öğrenci başı 160 px + balon
  1384 │  160   ( Yaşamak kalıcı bir durum.        )                      │
  1400 │ altyazı (Lexend 500 44, ≤ 2 satır, ortalı)                      │  1400–1536
  1536 └ PLATFORM: hiçbir öğe yok                                        ┘
```

### 4.1 Sabitler

| Ad | Değer | Not |
|---|---|---|
| KART | x 48, y 380, w 984, h 332 (alt 712) | el çerçevesi, kalem 4 px, `murekkep` |
| ETK (etiket) | `MINI QUESTION` Lexend 700 56, x 88, taban 400, `murekkep` (şef düzeltmesi: açık temada vurgu yazısı ≈ 2,3:1, sözleşme) | lejant: çerçeve üst kenarı x 72 … 88 + etiket_w + 16 arasında AÇIK kalır (§5.1) |
| KX (kök sol) | 88 | üç satır sola hizalı |
| KB (kök tabanları) | 480, 566, 652 (şef düzeltmesi: +8) | satır aralığı 86; Fredoka 700 72 |
| BOŞLUK genişliği | `genislik("is living") + 48` | satır 3'te `he` ile `with` arası (sözcük arası boşluk = `genislik(" ")`) |
| BOŞLUK çizgisi y | KB[2] + 0,48 × 72 (≈ 679) | sözleşme: kalıcı altçizgi taban + 0,48 × boy; `g` kuyruğu değmez (şef düzeltmesi) |
| ALT_Y(taban, sözcük) | taban + 25 (sözcükte g j p q y ya da virgül varsa), değilse taban + 21 | karaoke + odak altçizgisi (BRIEF §0: 0,28 em; kuyruğun altından) |
| SAYAÇ | merkez (972, 440), r 40, kalem 8, `vurgu`; ortada `5` Fredoka 700 56 `murekkep` | kartın sağ üst köşesi; kök satır 1 sağ ucu (≈ 703) ile arası ≥ 16 |
| ŞIK satırı k (0–4) | y0 = 730 + 88·k, yükseklik 80, cy = y0 + 40 | satırlar 730–810 · 818–898 · 906–986 · 994–1074 · 1082–1162 |
| ŞIK yazısı | `A) lives` … Fredoka 700 64 `murekkep`, x 128, taban cy + 22 | tek metin (`A) ` + şık) |
| İMLEÇ | `el_ok(58, cy, 112, cy, 1)`, `vurgu`, kalem 9 | şık yazısının solunda |
| SATIR KUTUSU | x 48, y0, w 984, h 80, rx 24 | A soluk çerçeve ve B dolgusu bu ölçüde |
| PİL | x = max(420, şık_sağ + 40), y cy − 40, h 80, rx 40, çerçeve `ikincil` 4 px, iç pay 24 | şık satırının sağında (BRIEF: x ≥ 420); sağ uç ≤ 1032 |
| PİL yazısı | Caveat 700 64 `murekkep`, taban cy + 14; parça arası 18; ok 52 px; iç pay sol 24, sağ 34 (şef düzeltmesi) | ok (`→`, `↔`) kalemle çizilir, `murekkep`, kalem 5, y = cy + 1 (glif setinde yok) |
| TİK (B) | `tik_yolu(944, cy_B − 24, 48)`, kalem 9 | `pilMetin` (§6) |
| BAŞ | `ogrenci-bas.svg` (viewBox −45 0 240 330), yükseklik 160 → ölçek 160/330; sol üst (48, 1210) | `translate(48 + 45·ölçek, 1210) scale(ölçek)`; kalem 4,4/ölçek, `murekkep` |
| BALON | `balon_sol(x0 220, y0 1198, x1, y1 1384, tx 176, ty 1318)`, kalem 4,2, `murekkep` | x1 = 220 + 36 + max(satır_w) + 44 |
| BALON yazısı | Caveat 700 64 `murekkep`, x 256, tabanlar 1272 ve 1346 | satır 1 sözcük 0–2, satır 2 sözcük 3–6 (BRIEF bölümü) |

### 4.2 HUD (kare 0'dan sabit; hareket yok)
- `kun = Y.kunye_svg("Mini question")` (yalnız çip; gizli DEĞİL). Ders + rozet bu dizginin `<g id="kunye">` açılışından hemen sonra eklenir:
  - `<g id="ku-ders">` iki `text`: `SIMPLE PRESENT vs` (x 48, taban 212) ve `PRESENT CONTINUOUS` (x 48, taban 276); Fredoka 700 56, `fill="#f3efe6"`.
  - `<g id="ku-rozet">`: `rect` x = 48 + genislik(Fredoka 700 56, "PRESENT CONTINUOUS") + 24, y 216, w = genislik(Lexend 700 36, "YDT · TEMEL") + 56,
    h 72, rx 36, `fill="#f2a93b"`; `text` ortası rect ortası, taban 265, Lexend 700 36, `fill="#1b1a17"`, `text-anchor="middle"`.
- Logo: `Y.html(..., logo=(48, 48, 96 * Y.LOGO_EN_BOY, 96))` → 387×96.
- ID yasağı: `t1`, `t2`, `rz1`, `ku-nokta` kullanma (hf_tema bunlara özel kural uygular).

## 5. Olay listesi (kare = yerel sn × 30; küresel sn; ses olayı `s.olay`)

| # | Olay | Küresel sn (yerel kare) | Cümle sözcüğü | Uygulama | Ses |
|---|---|---|---|---|---|
| 1 | kart çerçevesi (lejant boşluklu) | 220,88 (16) | 15.0 Mini | `s.yol("kart", …, 0.6, murekkep, 4)` | cizgi 0,7 |
| 2 | etiket `MINI QUESTION` | 220,88 + 0,15 | 15.0 | `s.yazi("etiket", …, d 0.3)` | tik 0,45 |
| 3 | kök sözcük sözcük (11 sözcük) | 221,93 → 225,64 (48 → 159) | 15.2 My … 15.12 us. | her sözcük `s.yazi("w{n}", x, KB, …, Fredoka 700 72, T(15,i), d 0.14)` | ilk sözcükte tik 0,5 |
| 4 | karaoke altı her kök sözcükte | sözcük t0 | aynı | `s.yol("ka{n}", el_cizgi(x−2, ALT_Y, x+w+2, ALT_Y, 1), t0, 0.12, vurgu, 6, tur=None)` + `s.to("#ka{n}", t0+0.30, opacity 0, 0.15)` | yok |
| 5 | boşluk çizgisi (soluk) | 15.10 he t1 + 0,06 = 224,71 (131) | susma | `s.yol("bl0", el_cizgi(…, 2), …, 0.3, ikincil, 5)` | cizgi 0,5 |
| 6 | boşluk vurgu çizgisi (bl0 0,15 sn'de söner, aynı yere) | 227,25 → 227,40 (212) | 15.13 Boşluğa | `s.to("#bl0", 227,25, opacity 0, 0.15)`; `s.yol("gb0", …, 227,40, 0.35, vurgu, 10)` | cizgi 0,5 |
| 7 | sayaç halkası dolar + `5` | 229,33 (270) | 15.17 Beş | yay yolu (yatay `say` kalıbı) 0,96 sn; `say5` +0,04; ikisi +1,12'de söner (0,25 sn) | cizgi 0,55 · tik 0,5 |
| 8 | 5 şık satırı, 0,18 sn arayla | 229,33 + 0,18·k (270 → 275) | 15.17 Beş | `s.goster("#row{H}", t, 0.35, 0, 24)` | tik 0,5 @t · tik 0,4 @t+0,4 |
| 9 | öğrenci başı (3 path, 0,05 arayla, 0,32 sn) | 16.0 − 0,18 = 230,58 (307) | 16.0 Bence | `{"m":"draw","id":"bas{i}"…}` (yatay kalıp) | cizgi 0,55 ×3 |
| 10 | balon çerçevesi | 230,68 | 16.0 | `s.yol("bal", balon_sol(…), t, 0.55, murekkep, 4.2)` | cizgi 0,7 |
| 11 | balon sözcük sözcük (7) | 230,76 → 233,80 | 16.0 … 16.6 | `s.yazi("bw{i}", …, Caveat 700 64, SOZ[16][i].t0, 0.12)` | tik @0 ve @3 |
| 12 | A soluk sarı çerçeve | 231,40 (332) | 16.1 A | `rect#afr` (SATIR KUTUSU, fill none, `vurgu`, 4) → opacity 0,55 (0,3 sn) | tik 0,5 |
| 13 | balon söner, BAŞ KALIR | 235,03 (441) | 17.0 Ankara'da | `s.to("#balg", …, opacity 0, 0.4, power2.in)`; `bal_ids` = bal + bw0–bw6 (bas YOK) | vurus 0,6 |
| 14 | odak *lives in* (satır 1) | 235,13 (444) | 17.0 (+0,1) | `odak1a`: x(lives)−4 … x(in)+w+4, ALT_Y(KB0, "lives in"), 0,35 sn, `vurgu`, 10, alfa 0,85 | cizgi 0,5 |
| 15 | odak *Ankara* (satır 2, virgül dışarıda) | 235,48 | 17.0 | `odak1b`: x(Ankara,)−4 … x+genislik("Ankara")+4, ALT_Y(KB1, "Ankara"), 0,3 sn | yok |
| 16 | odak *this month*; odak1a/1b `ikincil`e döner | 238,55 (547) | 17.6 bu | `odak2` x(this)−4 … x(month)+w+4, ALT_Y(KB1, "this month"), 0,4 sn; `ikincile_don(["odak1a","odak1b"], 238,55)` (§5.2) | cizgi 0,5 |
| 17 | A pili; A çerçevesi söner; A satırı soluklaşır | 241,43 (633) | 17.13 geçici | pil A (§5.3); `afr` opacity 0 (0,25); `#rowA` opacity 0,4 @+0,2 (0,35) | tik 0,4 |
| 18 | doğru B: satır dolgusu + yazı `pilMetin` | 243,43 (693) | 17.17 B | `#grB` opacity 0→1 (0,3); `#rowB .m` opacity 0, `#rowB .p` opacity 1 (0,3) (§6) | vurus 0,85 |
| 19 | B tiki | 243,63 (699) | 17.17 (+0,2) | `s.yol("ck", tik_yolu(…), t, 0.3, "#1b1a17", 9)` | cizgi 0,55 |
| 20 | boşluğa *is living*; odak2 `ikincil`e döner | 244,95 (739) | 17.20 is | `s.yazi("fl0", BOŞLUK ortası, KB2, …, murekkep, d 0.3)`; `ikincile_don(["odak2"], 244,95)` | tik 0,55 |
| 21 | C imleci; gb0 `ikincil`e döner | 246,07 (772) | 17.22 C | `pt C` (İMLEÇ, 0,25 sn); `ikincile_don(["gb0"], 246,07)` | tik 0,45 |
| 22 | E imleci | 246,95 (799) | 17.25 E | `pt E` | tik 0,45 |
| 23 | C pili `he ↔ live`; C soluklaşır | 247,67 (820) | 17.27 özneyle | pil C; `#rowC` 0,4 @+0,2 | tik 0,4 |
| 24 | E pili `he ↔ are`; E soluklaşır | 248,15 (835) | 17.28 uyumsuz. | pil E; `#rowE` 0,4 @+0,2 | tik 0,4 |
| 25 | D imleci; C ve E imleci söner (0,15) | 249,11 (863) | 17.29 D | `pt D`; `#ptC`, `#ptE` opacity 0 | tik 0,45 |
| 26 | D pili `to live: no tense`; D soluklaşır | 249,83 (885) | 17.31 tek | pil D; `#rowD` 0,4 @+0,2 | tik 0,4 |
| 27 | durgun; son 12 kare geçiş (fade) altında | 250,38 → 251,27 | — | `Y.kontrol(s, Z["kare"])` (ilk VE son 12 kare kuralı) | — |

Altyazı: `dil = Y.altyazi_dilimleri([15, 16, 17])`; her dilim `#alt{i}`; aç/kapa §2 satır 3 kalıbı (aynı anda tek dilim).
SVG: `Y.altyazi_svg([{"id": "alt%d" % i, "metin": m} …])`, `__main__`te `ek=` ile.

### 5.1 Lejant çerçeve yolu
`el_kutu` kalıbında (yardim.py) tek açık yol yaz (uret.py içinde küçük işlev): başlangıç (g1, 380) → sağ üst köşe → sağ kenar → alt kenar →
sol kenar → sol üst köşe → bitiş (g0, 380); g0 = 72, g1 = 88 + etiket_w + 16. Kenarlar hafif eğri (Q), köşe sapması ±3 px. Yol kapanmaz.

### 5.2 `ikincile_don(ids, t)` (BRIEF §0: aynı anda en çok 3 sarı belirteç; eskisi kaybolmaz, `ikincil`e döner)
Her sarı yol için aynı `d` ile ikiz `<path id="{id}_i" stroke="#c9c2b3" stroke-width="6" fill="none" stroke-linecap="round" style="opacity:0"/>`
`s.svg`'ye eklenir. t'de: `#{id}` opacity 0 ve `#{id}_i` opacity 1 (ikisi 0,3 sn). GSAP ile stroke rengi DEĞİŞTİRME (satır içi renk temayı ezer).
Sarı sayımı (karaoke ≤ 0,45 sn, sayılmaz): 235,13 gb0+afr+odak1 = 3 · 238,55 gb0+afr+odak2 = 3 · 243,43 gb0+odak2+B = 3 ·
244,95 gb0+B = 2 · 246,07 B+C = 2 · 246,95 B+C+E = 3 · 249,11 B+D = 2.

### 5.3 Pil (sik_not)
`NOT` (yatay sırası): A `[t "this month", "->", t "temporary"]` imleçsiz · C imleç 17.22, pil 17.27 `[t "he", "<>", t "live"]` ·
E imleç 17.25, pil 17.28 `[t "he", "<>", t "are"]` · D imleç 17.29, pil 17.31 `[t "to live: no tense"]`. Çarpı (✗) YOK.
Grup `<g id="pil{H}" style="opacity:0">`: çerçeve rect + parça `text`'leri (Caveat 700 64, `fill="#f3efe6"`, `xml:space="preserve"`) +
ok yolları (`->`: düz ok sağa; `<>`: iki uçlu). `s.goster("#pil{H}", tn, 0.3, -24, 0)`. Pil, satır grubunun DIŞINDA: satır solunca pil tam kalır.

## 6. Renk ve tema (KOYU hex yaz; hf_tema temaya çevirir)

| Öğe | Hex (yazılan) | Tema sonucu |
|---|---|---|
| kök, şık, balon, pil yazısı, `5`, kart/balon/baş çizgisi, `is living`, pil okları | `#f3efe6` | murekkep |
| boşluk çizgisi bl0, pil çerçevesi, `_i` ikizleri | `#c9c2b3` | ikincil (yalnız çizgi; yazı değil) |
| çip, sayaç, gb0, odak, karaoke, imleç, A çerçevesi (stroke) | `#f2a93b` | vurgu |
| B satır dolgusu `rect#grB`, rozet `rect` | `#f2a93b` (rect fill) | vurguDolgu |
| B doğru yazısı `.p`, rozet yazısı | `text fill="#1b1a17"` | pilMetin |
| B tiki `#ck` | `stroke="#1b1a17"` + `s.svg`'ye `<style id="pm13">#root #ck{stroke:var(--pilMetin)}</style>` | pilMetin (kural olmasa zemin olurdu) |

- B satırı: `<g id="rowB">` içinde sırayla `rect#grB` (opacity 0), `text.m` (`#f3efe6`), `text.p` (`#1b1a17`, opacity 0). Diğer satırlarda
  yalnız `text.m`. 18. olayda `.m` söner, `.p` belirir (satır içi renk ataması YOK).
- Kırmızı, ham yeşil (`#167A4A`), emoji, gradyan, gölge yok. Tek vurgu sarı.

## 7. Kurallar ve assert'ler (uret.py içinde; ihlalde dur)

- Kök satır sağ uçları ≤ 1032 − 40; satır 3 boşluk dahil. Sayaç sol kenarı (932) − satır 1 sağ ucu ≥ 16.
- Şık yazısı sağ ucu + 40 ≤ pil x; pil x ≥ 420; pil sağ ucu ≤ 1032. B tiki sol (944) − B yazısı sağ ucu ≥ 32.
- Balon x1 ≤ 1032 − 8; balon satır sağ ucu ≤ x1 − 36; y1 ≤ 1392; şık satır 5 altı (1162) + 24 ≤ balon y0.
- Kart 352–1392 içinde; etiket üstü (400 − 0,7·56) ≥ 352. Her satırda ≤ 24 karakter (kök, şık, pil); balon satır 2 BRIEF metnidir (25), assert dışı.
- `Y.kontrol(s, Z["kare"])` (ilk=True). Hareket aralığı yerel ≈ 0,55–30,05 (izin 0,40–30,93).
- ID'ler: `kart, etiket, w{n}, ka{n}, bl0, gb0, say, say5, row{A–E}, grB, afr, bas, bas0–2, bal, bw0–6, odak1a, odak1b, odak2, {id}_i, ck, fl0,
  pt{C,E,D}, pil{A,C,E,D}, pm13, alt{i}`. `html()` bal_ids ile `#balg` grubunu kurar.
- `uret()` tam 2 değer döndürür: `(s, {"kun": kun, "bal_ids": bal_ids, "aralik": (bas, son)})`.
- `__main__`: `proje/index.html` = `Y.html(s, Z["sure"], kun, None, (48, 48, 96 * Y.LOGO_EN_BOY, 96), ek=altyazi_svg, bal_ids=bal_ids)`;
  sayım satırı `index.html yazıldı; komut N olay M hareket (bas, son)`.
- Python: girinti 4 boşluk (kalıpla uyum), satır ≤ 140, tip ipucu işlev imzalarında. Çalıştırma `/usr/bin/python3 uret.py` (`-I` yok: fontTools).

## 8. Kabul ölçütü

1. `cd D && /usr/bin/python3 uret.py && /usr/bin/python3 olay.py` çıkış 0; assert yok; olaylar hepsi kare < 928.
2. `proje/index.html`: `data-width="1080" data-height="1920"`; `#kunye` içinde `ku-ders`, `ku-rozet`, `ku-bolum`; `#balg` içinde `bas` YOK.
3. `cd K && bash araclar/qa-yerel.sh 02-04-ydt-temel-dikey 13-hyperframes-mini-soru 234.5,245.9,251.0 251.0 --hazirla` çıkış 0 (şef koşar).
4. Kareler: taşma, kesik yazı, üst üste binme, okunmaz kontrast (açık temada B yazısı ve tiki koyu), boş kare yok; platform bandı boş.
