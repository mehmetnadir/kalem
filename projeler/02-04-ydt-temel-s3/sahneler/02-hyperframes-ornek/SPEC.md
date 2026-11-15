# SPEC v2 — 02-04-ydt-temel-s3 · sahne 02-hyperframes-ornek (değer) · huni v2 · 15.11.2026

> DUZ2 (15.11): cümle 3 yeni metin (13 sözcük, SOZ 27–39); balonda TR soru yok, yalnız EN `-ing?` (A5); altyazı karaoke (tspan, ikincil → mürekkep; sahne 03 düzeni); etiketler `kesin düzenleme` (kart 2) ve `tarife` (kart 1), Caveat ikincil; `person → plan` / `train → timetable` kalktı; kol b için SOZ/TB kayması veriden. Kaynak `uret.py`; aşağıdaki eski zamanlar 28,31 sn sürümündendir.


Şef tasarımı. Uygulayıcı (agy) YALNIZ şu dosyayı yerinde düzenler:
`/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s3/sahneler/02-hyperframes-ornek/uret.py`
Başka dosyaya dokunma. Silme yok. Test, render, git yok. Şef koşturur.
`yardim.py`, `olay.py`, `calistir.sh`, `nesneler.json`, `cizim/ogretmen.json` HAZIR; değiştirme.
`yardim.altyazi_dilimleri(cumleler, gen=None)` artık `gen` (satır genişliği px) alır.

## 1. Başlangıç noktası ve kalıp

| Kalıp | Mutlak yol | Ne alınır |
|---|---|---|
| Var olan v1 kodu (yerinde düzenlenecek dosya) | `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s3/sahneler/02-hyperframes-ornek/uret.py` | BÜTÜN yapı, zamanlama, olay sırası, kimlikler, `soldur`, `ok_tek`, kalem geometrisi (`hash_`, `gurul`, `elips`, `kutu`), `tren_svg` parça listesi, `bilet_yollari` parça listesi, balon/baş/öğretmen kalıbı, altyazı aç/kapa, `__main__`. Olay ZAMANLARI v1 ile aynı kalır (ses ve sözcük çapaları değişmedi) |
| v1 tasarımı (yalnız başvuru) | `/home/sef/Silinecekler/2026-11-15-huni-v2/02-04-ydt-temel-s3/sahneler-v1/02-hyperframes-ornek/SPEC.md` | olay tablosu (§4); v2 yalnız KONUM, künye, kanal, altyazı değiştirir |
| Huni v2 standardı (bağlayıcı) | `/home/sef/01dev/dijital-anlatim/.claude/docs/huni-v2-standart.md` §2 | bölge sınırları |

Değişiklik kapsamı: (a) sabit konumlar (aşağıdaki geometri tablosu), (b) `kunye_tam()` → `kunye_v2()`, (c) kanal katmanı, (d) altyazı
bandı (x 60–960, orta 510). Olay listesi, sözcük çapaları, `BEKLENEN_SOZ` ve `assert SOZ[...]` blokları, `EKRAN`, `cevir_ekran`,
`olay.py` sözleşmesi (`uret()` → `(s, parca)`, modül düzeyinde `Z`) değişmez.

## 2. Yerleşim (1080×1920; bütün içerik x 60–960, y 460–1380)

| Bölge | y | İçerik |
|---|---|---|
| Üst boş | 0–280 | yalnız zemin (v1 HUD kalkar: üst logo 48–144, 2 satır ders adı 212/276, çip `Example`) |
| Kanal katmanı | 291–339 | logo + `@ydspublishing` (§3) |
| Künye | 360–450 | konu + rozet hapı (§3) |
| İçerik | 460–1380 | kart 1, zaman çizgisi, kart 2, balon, öğretmen |
| Altyazı | 1400–1550 | x 60–960, orta x 510 (§5) |
| Alt boş | 1570–1920 | yalnız zemin |

Faz düzeni (ok diyagramı yerine kutu çizimi; px):

```
 472 ┌ kart 1 (x 70–950) ─────────────── tren 719–934 × 492–583 ┐     A, B, C (statik)
 568 │ The train to İzmir                                         │
 666 │ leaves at 7 pm today.     (684 klm · 704 bağ şeridi)       │
 726 └────────────────────────────────────────────────────────────┘
 A:  808 now(130) · 7 pm(350, sarı daire) · tonight(726)   848 eksen 72→948   924 gelecek · V-s (350) · gelecek · am + V-ing (726)
     966 kart 2 (966–1220) · satırlar 1062 / 1160 · bilet köşede 783–935 × 982–1052
 B:  kart 2 −132 → 834–1088 (satırlar 930 / 1028; bilet 850–920) · balon 256–954 × 1112–1372 (1186 / 1262 / 1338) · baş 64–208 × 1144–1342
     bağ cn: nokta (767, 1112) → yukarı x 767 → y 704 → sola `leaves` altına
 C:  792 train → timetable (x 97) · krm 961 · öğretmen 72–155 × 1110–1376 · 1172 person → plan (x 300)
     tren bağı: (826.5, 592) → aşağı → y 704 → sola `leaves` altına
1400 ─ altyazı (Lexend 500 44, ≤ 2 satır, orta 510) ─ 1550 ─ BOŞ ─ 1920
```

### 2.1 Geometri tablosu (v1 → v2; modül başında adlı sabit olarak yaz, kodun gövdesinde çıplak sayı tekrarlama)

| Öğe | v1 | v2 |
|---|---|---|
| Kart 1 çerçevesi `kc0…kc3` | `kutu(57, 368, 966, 260, 71)` | `kutu(70, 472, 880, 254, 71)` |
| Kart 1 satır tabanları (`r1`, `r2`, `w7`, `w8`) | 468 · 566 | 568 · 666 (sol x 97 aynı) |
| Tren `g#tren` | `translate(790 404) scale(0.5)` | `translate(724 504) scale(0.5)` → ekranda kutu [719, 492, 934, 583] |
| Zaman çizgisi ekseni `tx` | `ok_tek(72, 748, 1008, 748, 0.5)` | `ok_tek(72, 848, 948, 848, 0.5)` |
| Nokta x: now · 7 pm · tonight | 150 · 400 · 790 | `XN 130` · `X7 350` · `XT 726` |
| Nokta y (eksen) `AY` | 748 | 848 |
| Üst etiket tabanı `LY` (`tl_now`, `tl_7`, `tl_t`; nokta x'ine ortalı) | 708 | 808 |
| Alt etiket tabanı `GY` (`tg1` X7'ye, `tg2` XT'ye ortalı) | 824 | 924 |
| `7 pm` çentiği `t7c` | `M 400 730 L 400 766` | `M X7 AY−18 L X7 AY+18` |
| Kalem oku `tok` (now → 7 pm) | `M 168 736 Q 277 696 388 738` + uç | başlangıç `(XN+18, AY−12)`, denetim `((XN+X7)/2+2, AY−52)`, bitiş `(X7−12, AY−10)`; uç v1 formülü (k 18, a = atan2(bitiş − denetim)) |
| Sarı daire `t7d` | `Y.el_daire(400, 688, 80, 38, 0.6)` | `Y.el_daire(X7, LY−20, 80, 38, 0.6)` |
| Kart 2 çerçevesi `kd0…kd3` (A konumu) | `kutu(57, 860, 966, 260, 72)`; `cizgi_zamanlari([966,260,966,260], …)` | `kutu(70, 966, 880, 254, 72)`; `cizgi_zamanlari([880, 254, 880, 254], …)` |
| Kart 2 satır tabanları (A) | 960 · 1058 | 1062 · 1160 (sol x 97 aynı) |
| Bilet `bl*` | `BS 0.55`, `BCX 900`, `BCY 926` | `BS 0.40`, `BCX 859`, `BCY 1017` (A; parça listesi ve `E −0.06` aynı) |
| Kart 2 kayması `#k2` (olay 15) | `y −124` | `y −132` (B/C: kart 2 834–1088, satır 1 tabanı 930) |
| Öğrenci başı | `BS0 240/330`, `BTX 72+45·BS0`, `BTY 1090` | `BS0 0.60`, `BTX 64+45·BS0`, `BTY 1144` (ekranda 64–208 × 1144–1342); `stroke-width 4/BS0` |
| Balon `bal` | `balon_sol(300, 1040, 996, 1340, 252, 1290)` | `balon_sol(256, 1112, 954, 1372, 214, 1300)` |
| Balon sözcükleri `bw17…bw26` | x başı 340; tabanlar 1124 · 1208 · 1292 | x başı 296; tabanlar 1186 · 1262 · 1338 (Fredoka 600 64 aynı) |
| Sarı nokta `nk` | `M 768 1036 L 768.1 1036` | `M CN_X 1112 L CN_X+0.1 1112`, `CN_X = 767` |
| Bağ `cn` | `M 768 1036 L 768 620 Q 768 604 752 604 L XU1 604` + `ok1` | `M CN_X 1112 L CN_X 720 Q CN_X 704 CN_X−16 704 L XU1 704` + `ok1` |
| `ok1` (bağ ucu, `leaves` altı) | y 593,5 · 604 · 614,5 | y `BAG_Y−10.5` · `BAG_Y` · `BAG_Y+10.5`, `BAG_Y = 704`; `XU1 = 97 + 0.75·g("leaves")` aynı |
| Öğretmen `g#fig` | `fs = 380/(y1−y0)`, üst 1010, sol 72 | `fs = 266/(y1−y0)`, üst `FY0 = 1110`, sol 72 (ekranda 72–155 × 1110–1376); `HX`, `HY` aynı formül, yeni değerlerle |
| Öğretmen oku `ok_fig*` bitişi | `(XG + WG/2, 1010)` | `(XG + WG/2, 1102)` (kart 2 B altı 1088 + 14) |
| `am going` altçizgisi `krm*` | y 867 | y 961 (B satır 1 tabanı 930 + 0,48·64 ≈ 31) |
| `person` · ok · `plan` (`lp0`, `lpo`, `lp1`) | x 300, taban 1080, ok y 1058 | x 300, taban 1172, ok y 1150 |
| Tren bağı `ok_trn*` | `M 892.5 492 L 892.5 588 Q 892.5 604 876.5 604 L XU1 604` + `ok1` | `M TRX 592 L TRX 688 Q TRX 704 TRX−16 704 L XU1 704` + `ok1`, `TRX = 826.5` (tren kutusu orta x; 592 = kutu altı 583 + 9) |
| `train` · ok · `timetable` (`lt0`, `lto`, `lt1`) | x 97, taban 694, ok y 672 | x 97, taban 792, ok y 770 |
| `leaves` odak `klm` | `el_cizgi(95, 584, 97+g+2, 584, 1)` | y 684 (kart 1 satır 2 tabanı 666 + 18) |

Not: kart 1 çerçevesi, satırları ve tren sahne 01'in son karesiyle ortak sabittir (sahne 01 `devir.json` v2). Sahne 01 henüz v2'ye
geçmedi; bu değerler şefin seçimidir, RAPOR'da karşılaştırılır.

## 3. Kanal katmanı ve künye (v1 HUD yerine; kare 0'dan son kareye sabit, hareket komutu YOK)

### 3.1 Künye `kunye_v2() -> str` (v1 `kunye_tam()` silinir değil, yerine yazılır; çip yok)
- `<g id="kunye">` içinde:
  - konu `<text id="ku-konu">`: `Simple Present vs Present Continuous`, Fredoka 700, x 60, taban y 420, fill KRE, boy `KB`.
  - rozet `<g id="ku-rz">`: `<rect>` x `RX`, y 386, genişlik `RW`, yükseklik 48, `rx 24`, fill SAR (tema `vurguDolgu` yapar) +
    `<text>` `YDT · TEMEL` Lexend 700 26, `text-anchor="middle"`, x `RX + RW/2`, taban y 419, fill ZEM (tema `pilMetin` yapar).
- `RW = g_l700("YDT · TEMEL", 26) + 40`. `KB` = 34'ten 28'e inen ilk tam sayı ki `60 + g_f700(konu, KB) + 20 + RW ≤ 960`; bulunamazsa `assert`.
  `RX = 60 + g_f700(konu, KB) + 20`. (Ölçüm: KB 34 → konu 584,6, rozet sağ ucu ≈ 868.)
- `id="t2"`, `id="rz1"`, `id="ku-nokta"`, `ku-ders1`, `ku-ders2`, `ku-bolum` YOK.

### 3.2 Kanal `__main__` içinde
- `logo = (53.2, 291, 193.5, 48)` ile `Y.html(...)` çağrılır (yükseklik 48, genişlik 48 × 1920 / 476,3 = 193,5; resim x 53,2 → SVG iç
  boşluğu 68/1920 düşülünce görünür sol kenar x 60; y 291–339).
- `Y.html` çıktısındaki `<g id="logo">…</g>` dizgisi birebir bulunur (`assert … in html`, tek eşleşme) ve şu yapıyla değiştirilir:
  `<g id="logo"><g id="kanal">` + AYNI `<image id="logoimg" href="assets/logo.svg" …/>` + `<text id="kanal-ad" x="263" y="330"
  font-family="Lexend" font-weight="700" font-size="42" fill="{KRE}" xml:space="preserve">@ydspublishing</text>` + `</g></g>`.
  (Kapı aracı `#logo` içindeki her şeyi `kunye` türü sayar; grup kimliği `kanal` → ad `kunye:kanal:…`. `logoimg` kimliği tema
  önizlemesi için kalır.)
- Kanal ve künye öğelerine `s.to/s.set/s.fromto/draw` komutu YAZMA; opaklık 1, giriş/çıkış yok.

## 4. Olay listesi (zamanlar v1 ile AYNI; yalnız konumlar §2.1)

Yerel = küresel − 3,00. Kodda çapa ifadesi kalır (`s.S(T(i, "…"))`); sabit saniye yazma.

| # | Olay | Küresel çapa | Yerel | v2 konum |
|---|---|---|---|---|
| 0 | Kare 0 (statik): kart 1, tren, `r1`, `r2`, künye v2, kanal, altyazı dilimi 0 açık | — | 0 | §2.1 |
| 1–2 | `pm`, `today.` | `p.m.` 3,00 · `today.` 3,40 | 0,40 · 0,52 | taban 666 |
| 3–8 | eksen, now, `7 pm` çentik + nokta + etiket, kalem oku, sarı daire (`isaret`), `gelecek · V-s` | `today.` | 0,52–1,45 | AY 848 · LY 808 · GY 924 |
| 9–12 | kart 2 çerçeve, `I am going to the` / `movie theater tonight.` sözcük sözcük, bilet (`movie`) | `I` 4,45 … `tonight.` 5,93 | 1,15–2,93 | kart 2 A 966 |
| 13 | `tonight` noktası + etiket + `gelecek · am + V-ing` | `tonight.` 5,93 | 2,93 | XT 726 |
| 14–15 | `#zc` söner; `#k2` −132 | `Hocam,` − 0,50 / − 0,42 | 3,50 · 3,58 | — |
| 16–18 | öğrenci başı, balon, soru sözcük sözcük | `Hocam,` 7,00 … `yok?` 10,33 | 3,90–7,33 | §2.1 |
| 19–20 | sarı nokta, sarı bağ balon → `leaves` | `Neden` 9,72 | 6,72 · 6,86 | CN_X 767, BAG_Y 704 |
| — | DURAKLAMA | 10,76–11,51 | 7,76–8,51 | olay yok |
| 21–22 | `#balg` söner; öğretmen kalemle | `Planı` 11,51 | 8,51 · 8,55 | FY0 1110 |
| 23–26 | sarı ok el → `am going` sütunu; `am going` sarı altçizgi; `person` → `plan` | `bir` 12,07 · `kişi` · `yapar.` | 9,07–9,66 | §2.1 |
| 27–30 | önceki sarı griye; tren bağı (sarı); `train` → `timetable` | `Tren` 13,43 · `tarifeye` 13,83 | 10,43–11,28 | TRX 826.5 |
| 31 | tren bağı griye; `leaves` sarı altçizgi (odak) | `geniş` 15,19 | 12,19 | y 684 |

Aynı anda tek sarı içerik öğesi kümesi (v1 ile aynı sıra): `7 pm` dairesi → `cn` → `ok_fig` + `krm` → `ok_trn` → `klm`.
Gruplar (`#zc`, `#k2`, `#balg`) ve `s.svg` ekleme sırası v1 ile aynı.

## 5. Altyazı bandı (v2)

- Dilimler: `Y.altyazi_dilimleri([1, 2, 3], gen=900)`; metin `cevir_ekran` ile (ekranda `İzmir`, `7 pm`).
- Yeni işlev `altyazi_v2_svg(parcalar: list[dict]) -> str` (uret.py içinde; `Y.altyazi_svg` kullanılmaz): her parça için sözcükleri
  satır genişliği ≤ 900 olacak biçimde böl (Lexend 500). Boy sırası 44 → 40 → 36: 2 satıra sığan ilk boy seçilir; 36'da da 2'yi aşarsa
  `assert`. Satır aralığı `round(boy × 1.27)` (44 → 56). Tek satır tabanı 1484; iki satır tabanları 1456 ve 1456 + aralık.
  `<text x="510" … text-anchor="middle" font-family="Lexend" font-weight="500" font-size="{boy}" fill="{KRE}">` (`&` → `&amp;`).
  Her parça `<g id="alt{i}" style="opacity:0">…</g>` (v1 biçimi; açık-0 dilim değişimi `replace` kalıbı aynen çalışmalı).
- Aç/kapa zamanlaması v1 ile aynı.

## 6. Kurallar ve bekçiler (`assert`; sessiz geçiş yok)

- Renk yalnız `Y.RENK` koyu değerleri (KRE, IKN, SAR, ZEM); açık tema hex'i (`#ffe066`, `#1b2440`, `#f7f3ea`) YAZMA. Kırmızı, yeşil,
  gradyan, gölge, emoji yok. `→` glifi yok (oklar çizilir). Her `s.svg` öğesinin ilk özniteliği `id`; kimlikler tekil.
- Ekran metni yalnız: kart satırları, `now`, `7 pm`, `tonight`, `gelecek · V-s`, `gelecek · am + V-ing`, balon sözcükleri, `person`, `plan`,
  `train`, `timetable`, künye (`Simple Present vs Present Continuous`, `YDT · TEMEL`), `@ydspublishing`, altyazı.
- `assert` listesi (v1 listesinin yerine):
  1. kart 1 satır 1 sağ ucu ≤ 719 − 24; satır 2 sağ ucu ≤ 950 − 40; kart 2 satır 1 sağ ucu ≤ bilet sol ucu − 24.
  2. üst etiketler arası (now ↔ 7 pm, 7 pm ↔ tonight) ≥ 24; `tg1` sağ ucu ile `tg2` sol ucu arası ≥ 24; `tg2` sağ ucu ≤ 948; `tl_now` sol ucu ≥ 60.
  3. bağ koridoru: kart 2 satır 2 sağ ucu + 10 ≤ CN_X − 3; bilet sol ucu (kenar noktalarından hesapla, − 2,25 çizgi payı) ≥ CN_X + 3 + 10.
  4. balon satırı sağ ucu ≤ 954 − 36; baş sağ ucu (`BTX + 195·BS0`; viewBox x −45…195) < balon kuyruk ucu x 214.
  5. `person → plan` ve `train → timetable` sağ ucu ≤ 760; öğretmen sağ ucu ≤ 290, altı ≤ 1380.
  6. `XU1 ≤ 97 + g("leaves")`.
  7. içerik sınırı: her kart çerçevesi `[x − 9, x + w + 9] × [y − 9, y + h + 9]` (kutu taşması), tren kutusu, bilet (A ve B), balon
     `[x0, x1 + 4] × [y0 − 6, y1 + 6]`, baş, öğretmen → hepsi x 60–960 ve y 460–1380 içinde.
  8. altyazı: her satır genişliği ≤ 900; satır sayısı ≤ 2.
- Python: tip ipucu (yeni işlevlerde `-> …`), satır ≤ 120, girinti 4, sessiz `try/except` yok. Dosya başı belge dizgisi: "huni v2" ve
  "Tasarım: SPEC.md (şef); kod agy-filo (15.11.2026)".

## 7. Kabul ölçütü (şef doğrular)

1. `cd <sahne> && /usr/bin/python3 uret.py` çıkış 0; `Y.kontrol` geçer; `/usr/bin/python3 olay.py` çıkış 0.
2. `proje/index.html`: `data-duration="13.4"`, `id="kanal"`, `@ydspublishing`, `id="ku-konu"`, `YDT · TEMEL`, `id="zc"`, `id="k2"`,
   `id="balg"`, `İzmir`, `x="510"`; `Example`, `SIMPLE PRESENT vs`, `ku-bolum`, `Izmir`, `seven`, `p.m.`, `→`, `#ffe066`, `#1b2440` YOK.
3. `logoimg` x 53.2, y 291, yükseklik 48; `kanal-ad` x 263, y 330.
4. Şef: `qa-yerel.sh … 3.0,9.5,15.96 13.5 --hazirla` çıkış 0; çakışma kapısı 0 uyarı.
