# SPEC — 02-04-ydt-temel-dikey · sahne 07-hyperframes-kural (HyperFrames, 1080×1920, 523 kare)

Kaynak: `projeler/02-04-ydt-temel-dikey/BRIEF-DIKEY.md` §2 + §3 satır 7. Yazan: şef (15.11.2026). Tasarım verir, tam kod yazmaz.
K = `/home/sef/01dev/_worktrees/kalem-0204`. Sahne dizini D = `K/projeler/02-04-ydt-temel-dikey/sahneler/07-hyperframes-kural/`.

## 1. Dosyalar

| Dosya | Durum | İş |
|---|---|---|
| `D/uret.py` | YOK | §4–§6'ya göre YAZ (tek iş bu) |
| `D/yardim.py` | VAR (dikey sahne 01 kopyası: `W,H = 1080,1920`, `u()`, `Sahne`, `kunye_svg`, `altyazi_svg`, `altyazi_dilimleri`, `el_cizgi`, `html`, `kontrol`) | DOKUNMA |
| `D/olay.py` | VAR | DOKUNMA; `s, _ = U.uret()` ve `U.Z["kare"]` ister |
| `D/calistir.sh` | VAR | DOKUNMA |

Başka dosyaya dokunma. Silme yok. Test, render, git yok.

## 2. Kalıp kaynakları (salt oku)

| Kalıp | Mutlak yol | Ne alınır |
|---|---|---|
| Aynı içerik, yatay | `K/projeler/02-04-ydt-temel/sahneler/07-hyperframes-kural/uret.py` | `T(i, bas)` (sözcük önek assert'i), ikon verileri `MONT`, `TISORT`, `EV`, `BAVUL` (AYNEN), `_kutu`, `_kutusu`, `_daire_yolu`, `ikon_yollari` (AYNEN; yalnız `IKON_BOY`, `IKON_EN` sabitleri dikey değer alır), `hucre()` zamanlama kalıbı (yazı → +0,30 bağ çizgisi 0,2 sn → +0,45 ikon, `Y.cizgi_zamanlari`), MEANING FIRST kinetik kalıbı (`fromto` opaklık 0 / y +34 / ölçek 0,86 → 1, 0,22 sn `back.out(1.6)`, `svgOrigin`), `kayit()` olay raporu ve `__main__` çıktı biçimi |
| Aynı paket, dikey HF iskeleti | `K/projeler/02-04-ydt-temel-dikey/sahneler/01-hyperframes-giris/uret.py` | `PAKET`, `SAH`, `Z`, `SOZ` okuma; `Y.Sahne(Z["t_bas"])`; `Y.altyazi_dilimleri` + `Y.altyazi_svg`; `Y.html(...)` çağrısı (`ek=altyazi`) |
| Altyazı görünürlüğü (çok dilim) | `K/projeler/present-continuous-dikey/sahneler/06-hyperframes-form/uret.py` satır 303–321 | `aktif(t)` kare taraması: her karede tek dilim açık, değişimde `set` opaklık 0/1. (Sahne 01'in `t1 + 0,35` kapatması burada YETMEZ: ardışık dilimler 0,4 sn üst üste biner) |
| HUD sayıları ve metinleri | `K/projeler/02-04-ydt-temel-dikey/ortak/kunye.js` `KUNYE` | ders 2 satır, rozet, çip (§4.2) |
| Tema dönüşümü | `K/projeler/02-04-ydt-temel-dikey/ortak/hf_tema.py` | uret.py KOYU hex yazar: `RENK["murekkep"]`, `RENK["ikincil"]`, `RENK["vurgu"]`; rozet `rect fill="#f2a93b"` → vurguDolgu, rozet yazısı `fill="#1b1a17"` → pilMetin. `rz1` kimliğini KULLANMA |

## 3. Zaman (tek kaynak)

- `zaman.json` → `klasor == AD.name`: t_bas 113,37, kare 523, sure = 523/30. Yerel sn = küresel − t_bas (`s.S()`).
- `ortak/anlatim/sozcukler.json` cümle 8 (33 sözcük). Her olay `T(i, bas)` ile alınır; sabit saniye YAZMA.
- İlk 12 ve son 12 kare durgun: `Y.kontrol(s, Z["kare"])` (ilk=True) geçmeli. Hareket 4,07–16,60 yerel sn arasında kalır.

## 4. Yerleşim (1080×1920; bant: HUD 0–320 · içerik 352–1392 · altyazı 1400–1536 · platform 1536–1920 BOŞ)

### 4.1 Genel
- Tek sütun, kenar 48. Ayraç x 540. Sol hücre x 48–540, sağ hücre x 540–1032. Sol ve sağ hücre AYNA düzen:
  - sol: `[simge kutusu x 56–176] [14] [bağ çizgisi 190→214] [14] [yazı x 228'den SOLA hizalı]`
  - sağ: `[yazı x 852'de biten SAĞA hizalı] [14] [bağ çizgisi 866→890] [14] [simge kutusu x 904–1024]`
- Simge kutusu 120 × 120 (BRIEF: 120–140). `IKON_BOY = IKON_EN = u(120)`. Sol simge sağ kenarı 176'da (`ikon_yollari(…, 176, cy, True)`),
  sağ simge sol kenarı 904'te (`ikon_yollari(…, 904, cy, False)`); dikey merkez satır ortası `cy`.
- Simge kalemi: ana parça `RENK["murekkep"]` w 4, `ince` parça `RENK["ikincil"]` w 3. Bağ çizgisi `ikincil` w 3, `Y.el_cizgi(…, 0.6)`.
- Ayraç parçası: her satırın kendi parçası, x 540 (± 2 el eğimi), satır üstü + 14 → satır altı − 14, `ikincil` w 4, 0,3 sn.
- Satır ayırıcısı: satır 2, satır 3 ve ad satırının ÜSTÜNDE yatay el çizgisi x 64–1016, o satırın İLK yazısıyla aynı anda çizilir
  (0,35 sn). Satır 1'in üst çizgisi yok. Satır ayırıcısı `ikincil` w 3; ad satırı ayırıcısı `murekkep` w 4.
- Boş satır, boş tablo, boş başlık YOK: hiçbir çizgi kendi satırının ilk sözcüğünden önce çizilmez.

### 4.2 HUD (kare 0'dan sabit; `kunye_tam_svg()` uret.py içinde yazılır, yardim.py değişmez)
- Metinleri `ortak/kunye.js`'ten düzenli ifadeyle oku ve assert et: `ders` = `["SIMPLE PRESENT vs", "PRESENT CONTINUOUS"]`,
  `rozet` = `"YDT · TEMEL"`, `cipler["07-hyperframes-kural"]` = `"Rule"`.
- `<g id="kunye">` içinde üç grup:
  - `ku-ders`: iki `<text>` Fredoka 700 56, `fill=RENK["murekkep"]`, x 48, taban y 212 ve 276.
  - `ku-rozet`: `rect` x = 48 + genislik(Fredoka 700, ders[1], 56) + 24 (≈ 670), y 216, w = genislik(Lexend 700, rozet, 36) + 56, h 72,
    rx 36, `fill=RENK["vurgu"]`; `text` ortalı (rect ortası), taban y 265, Lexend 700 36, `fill=RENK["zemin"]`.
  - `ku-bolum`: çip; `Y.kunye_svg("Rule")` ile AYNI çizim (x = 1032 − cw, y 48, h 80, rx 40, çerçeve `vurgu` 4 px, Lexend 700 40, taban 102).
    En kolayı: `Y.kunye_svg(cip)` çıktısındaki `<g id="kunye">` sarmalını açıp içini kullan.
- Logo: `Y.html(…, logo=(48, 48, 96 * Y.LOGO_EN_BOY, 96))` (sahne 01'in uçuş sonu konumu; hareket yok).

### 4.3 Tablo satırları (Caveat 700 64, `murekkep`; satır ortası cy; tek satır yazı tabanı = cy + 18)

| Satır | y bandı | cy | Sol hücre (simge · yazı · küresel sn = `T`) | Sağ hücre (yazı · simge · sn) |
|---|---|---|---|---|
| 1 | 380–560 | 470 | MONT · `general` · T(7,"Genel") 117,44 | `right now` · TISORT · T(10,"konuşma") 118,24 |
| 2 | 570–750 | 660 | EV · `permanent` · T(12,"Kalıcı") 119,44 | `temporary` · BAVUL · T(15,"geçici") 120,48 |
| 3 | 760–940 | 850 | TREN_D · `timetable` T(17,"Tarifeli") 121,52 / `(future)` T(18,"gelecek") 122,04 | `arrangement` T(20,"planlanmış") 122,80 / `(future)` T(21,"gelecek") 123,44 · BILET_D |

- Satır 3 iki satırlı: 1. satır tabanı 834, 2. satır (`(future)`) tabanı 902. Sağ hücrede iki satır da 852'de biter.
- Yazı açılışı soldan maske (`s.yazi`, süre: general 0,35 · arrangement 0,45 · `(future)` 0,35 · öteki 0,4). Sağa hizalı yazı: `anchor="end"`, x 852.
- Bağ çizgisi ilk yazıdan 0,30 sn sonra (0,2 sn), simge 0,45 sn sonra başlar, `min(0.75, 0.25 + 0.06 * parça)` sn sürer (yatay `hucre()`).
- Ayraç parçası ve (satır 2–3 için) üst ayırıcı, satırın SOL yazısıyla aynı anda başlar.
- Ölçülen genişlikler (fontTools): general 158 · right now 212 · permanent 235 · temporary 223 · timetable 202 · (future) 174 ·
  arrangement 286. Sol yazı en çok 463'te biter; sağ yazı en erken 566'da başlar (ayraçtan 26 px).

### 4.4 Dikey için iki sade simge (yatay TREN ve BILET 120 px kutuda 41 px yüksek kalıyor; telefonda okunmaz)
- `TREN_D` = yatay `TREN` listesinden yalnız lokomotif: gövde `_kutu(200,55,170,75)`, kabin `_kutu(200,10,75,45)`, baca `_kutu(320,22,26,33,True)`,
  mahmuz `[(370,95),(398,130),(370,130)]`, kabin camı `_kutu(215,20,42,25,True)`, iki teker `daire (240,138,17)` ve `(335,138,17)`,
  ray `[(190,158),(410,158)]` ince. Vagon, bağlantı, vagon camları ve vagon tekerleri ALINMAZ. Kutu 220×148 → ≈ 120×81.
- `BILET_D` = yatay `_bilet()` ile aynı kurgu, yarı genişlik 180 yerine 110: kenar (−110…110, ±70, iki yanda 22 yarıçaplı çentik),
  delik çizgisi x 50 (6 kısa çizgi, ince), baskı satırları ince: y −30 (−85→20), y 0 (−85→0), y 30 (−85→30). Eğim −0,06. ≈ 120×76.
- MONT ≈ 93×120 · TISORT ≈ 120×101 · EV 120×120 · BAVUL ≈ 115×120.

### 4.5 Ad satırı (y 960–1250) — "Soldakiler geniş zaman, sağdakiler şimdiki zaman"
- Sol blok, sol hücrede ORTALI (merkez x 294): `SIMPLE` taban 1018 · `PRESENT` 1088 (Fredoka 700 64, `murekkep`) · `V1 / V-s` 1166 (Caveat 700 72, `ikincil`).
- Sağ blok, sağ hücrede ORTALI (merkez x 786): `PRESENT` 1018 · `CONTINUOUS` 1088 (Fredoka 700 64) · `am / is / are` 1166 · `+ V-ing` 1232 (Caveat 700 72, `ikincil`).
- Ortalı yazı: x0 = merkez − genişlik/2, `anchor="start"`.
- Zaman: `SIMPLE` T(22,"Soldakiler") 124,32 · `PRESENT` +0,22 · `V1 / V-s` T(23,"geniş") 124,96 · `PRESENT` T(25,"sağdakiler") 126,00 ·
  `CONTINUOUS` +0,22 · `am / is / are` T(26,"şimdiki") 126,72 · `+ V-ing` T(27,"zaman") 127,16. Açılış 0,3 sn.
- Ayırıcı y 950 (`murekkep` w 4) ve ayraç parçası 964→1246, ikisi de T(22) anında.

### 4.6 Alt (y 1270–1390) — "Seçmeden önce cümlenin anlamına bak."
- `MEANING ` + `FIRST` Fredoka 700 110, `murekkep`, tek satır ortalı (x 540; genişlik ≈ 802 → x 139–941), taban 1364.
- Kinetik: `MEANING` T(28,"Seçmeden") 128,08, `FIRST` T(29,"önce") 128,56 (yatay kalıp, `y: u(34)`).
- Sarı belirteç: `Y.el_cizgi` x0 − 6 → x1 + 6, y 1380 / 1379, `RENK["vurgu"]` w 11, 0,45 sn, T(31,"anlamına") 129,52; olay `vurus` 0,7.

### 4.7 Altyazı (1400–1536)
- `dil = Y.altyazi_dilimleri([8])` (3 dilim, her biri ≤ 2 satır). `Y.altyazi_svg([{id: "alt%d", metin}])` → `Y.html(…, ek=…)`.
- Görünürlük 06 kalıbı: her yerel kare f için küresel tg = t_bas + f/30; açık dilim = koşulu `t0 − 0,05 ≤ tg < t1 + 0,35` olan SON dilim;
  değişince eskisine `set` opaklık 0, yenisine 1 (zaman `f/30`). Karaoke yok (Nadir 03.11: şerit yok; sahne 01 ile aynı).

## 5. Olay listesi (beklenen)

| Olay | Küresel sn | Cümle sözcüğü (i) |
|---|---|---|
| satır 1 sol: ayraç + `general` + bağ + mont | 117,44 | Genel (7) |
| satır 1 sağ: `right now` + bağ + tişört | 118,24 | konuşma (10) |
| satır 2 sol: ayırıcı + ayraç + `permanent` + bağ + ev | 119,44 | Kalıcı (12) |
| satır 2 sağ: `temporary` + bağ + bavul | 120,48 | geçici (15) |
| satır 3 sol: ayırıcı + ayraç + `timetable` + bağ + tren | 121,52 | Tarifeli (17) |
| `(future)` sol | 122,04 | gelecek (18) |
| satır 3 sağ: `arrangement` + bağ + bilet | 122,80 | planlanmış (20) |
| `(future)` sağ | 123,44 | gelecek (21) |
| ad ayırıcı + ayraç + `SIMPLE` / `PRESENT` | 124,32 / 124,54 | Soldakiler (22) |
| `V1 / V-s` | 124,96 | geniş (23) |
| `PRESENT` / `CONTINUOUS` | 126,00 / 126,22 | sağdakiler (25) |
| `am / is / are` · `+ V-ing` | 126,72 · 127,16 | şimdiki (26) · zaman (27) |
| `MEANING` · `FIRST` kinetik | 128,08 · 128,56 | Seçmeden (28) · önce (29) |
| sarı belirteç | 129,52 | anlamına (31) |

Ses olayları (`s.olay`): yazı başı `tik` 0,5 · çizgi `cizgi` 0,35–0,6 (simgenin ilk 2 parçası) · kinetik `tik` 0,55 · belirteç `vurus` 0,7.

## 6. Kurallar ve kabul

- `uret()` → `(s, kun)` döner (olay.py bunu ister). Olay raporu `s.rapor = [(ad, yerel sn, sözcük)]`; `__main__` yatay biçimde basar.
- `__main__`: `proje/index.html` yazar: `Y.html(s, Z["sure"], kun, None, logo, ek=altyazi)`.
- Assert'ler (üretim durur): her yazı ve simge kutusu x 48–1032, y 352–1392 içinde · sol yazı sonu ≤ 516 · sağ yazı başı ≥ 564 ·
  MEANING FIRST genişliği ≤ 984 · `Y.kontrol` geçer · T() önekleri tutar.
- Renk: tek vurgu sarı (yalnız belirteç, rozet, çip). Kırmızı, yeşil, emoji yok. `ikincil` yazı yalnız ≥ 72 px.
- Python 3, `/usr/bin/python3` ile koşar (fontTools kullanıcı site-packages'ta). Satır ≤ 120 karakter. Tür ipucu gerekmez (komşu dosyalarla aynı üslup).
- Kabul: `cd D && /usr/bin/python3 uret.py && /usr/bin/python3 olay.py` hatasız; `proje/index.html` oluşur; olay listesi §5 ile aynı.
