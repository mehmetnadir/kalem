# Sahne 07 · kural kartı DİKEY (HyperFrames 1080×1920, 523 kare, 113,37–130,40 sn; cümle 8)

Durum: istem D-dikey (15.11.2026, srv21). Önizleme hazırlığı `ONIZLE_YALNIZ=1` ile koştu. Render yok, commit yok.
Tema: koyu

| Kapı | Sonuç |
|---|---|
| `qa-yerel.sh` çıkış kodu | 0 |
| Çakışma kapısı | çakışma yok (69 örnek) |
| Kare bakışı (açık 3 + koyu 1 + ara 5) | taşma, kesik yazı, binme, okunmaz kontrast, boş kare, altyazı çakışması, platform bandında öğe YOK |
| Düzeltme turu | 0 / 4 (QA sonrası 1 kimlik adı eşlemesi: `ku-rozet` → `ku-rz`, sözleşme satırı 49; görsel etkisi yok, kapı yeniden koştu) |

## Yerleşim (BRIEF-DIKEY §3 satır 7 + `SPEC.md`)

```
HUD 0–320     logo 48,48 387×96 · ders 2 satır (Fredoka 56, taban 212/276) · rozet YDT · BASIC x≈670 · çip Rule
380–560       [mont] general            ┃            right now [tişört]
570–750       [ev] permanent            ┃            temporary [bavul]
760–940       [tren] timetable/(future) ┃  arrangement/(future) [bilet]
950           ─────────── ad ayırıcı (mürekkep) ───────────
960–1250      SIMPLE / PRESENT / V1 / V-s ┃ PRESENT / CONTINUOUS / am / is / are / + V-ing
1270–1390     MEANING FIRST (Fredoka 110) + sarı belirteç
1400–1536     altyazı (cümle 8, 3 dilim)   ·   1536–1920 boş
```

- Hücreler ayna: sol `[simge 56–176] – yazı x 228'den`, sağ `yazı 852'de biter – [simge 904–1024]`. Bağ çizgisi 24 px.
- Terimler Caveat 700 64 `murekkep`; kalıplar Caveat 700 72 `ikincil`; adlar Fredoka 700 64. En küçük içerik yazısı 64.
- Simgeler 120 px kutu (mont, tişört, ev, bavul yatay 07 verisi aynen). Tren ve bilet dikeyde sadeleştirildi (`SPEC.md` §4.4):
  yatay biçimleri 120 px kutuda 41 px yüksek kalıyordu. Tren = yalnız lokomotif (≈ 120×81), bilet = yarı genişlik 110 (≈ 120×76).
- Boş tablo yok: ayraç parçası ve satır ayırıcısı kendi satırının ilk sözcüğüyle birlikte çizilir.
- Tek vurgu sarı: rozet, çip, MEANING FIRST belirteci. Kırmızı, yeşil, emoji yok.

## Olay listesi (cümle 8; yerel sn = küresel − 113,37; kare = yerel × 30)

| # | Olay | Küresel sn | Yerel sn | Kare | Cümle sözcüğü (i) |
|---|---|---|---|---|---|
| 1 | satır 1 sol: ayraç + `general` + bağ + mont | 117,44 | 4,07 | 122 | Genel (7) |
| 2 | satır 1 sağ: `right now` + bağ + tişört | 118,24 | 4,87 | 146 | konuşma (10) |
| 3 | satır 2 sol: ayırıcı + ayraç + `permanent` + bağ + ev | 119,44 | 6,07 | 182 | Kalıcı (12) |
| 4 | satır 2 sağ: `temporary` + bağ + bavul | 120,48 | 7,11 | 213 | geçici (15) |
| 5 | satır 3 sol: ayırıcı + ayraç + `timetable` + bağ + tren | 121,52 | 8,15 | 244 | Tarifeli (17) |
| 6 | `(future)` sol | 122,04 | 8,67 | 260 | gelecek (18) |
| 7 | satır 3 sağ: `arrangement` + bağ + bilet | 122,80 | 9,43 | 283 | planlanmış (20) |
| 8 | `(future)` sağ | 123,44 | 10,07 | 302 | gelecek (21) |
| 9 | ad ayırıcı + ayraç + `SIMPLE` / `PRESENT` | 124,32 / 124,54 | 10,95 | 328 | Soldakiler (22) |
| 10 | `V1 / V-s` | 124,96 | 11,59 | 348 | geniş (23) |
| 11 | `PRESENT` / `CONTINUOUS` | 126,00 / 126,22 | 12,63 | 379 | sağdakiler (25) |
| 12 | `am / is / are` · `+ V-ing` | 126,72 · 127,16 | 13,35 · 13,79 | 400 · 414 | şimdiki (26) · zaman (27) |
| 13 | `MEANING` · `FIRST` kinetik (0,22 sn, `back.out(1.6)`) | 128,08 · 128,56 | 14,71 · 15,19 | 441 · 456 | Seçmeden (28) · önce (29) |
| 14 | sarı belirteç MEANING FIRST altı (0,45 sn) | 129,52 | 16,15 | 484 | anlamına (31) |

Hareket 4,07–16,60 yerel sn: ilk 12 ve son 12 kare durgun (`Y.kontrol` geçti). `olaylar.json`: 40 ses olayı (22 `cizgi`).
Her olay `T(i, bas)` ile alınır; sözcük kayarsa üretim durur. Altyazı: 3 dilim, kare kare `aktif(t)` ile tek dilim açık.

## Kapı sonucu (son koşu)

```
== KAPI
07-hyperframes-kural | çakışma yok (69 örnek, 16053 kutu)
== KARE (açık)  124.1 · 127.6 · 130.2
== KARE (koyu)  130.2
kapı çıkış kodu: 0
```
Komut: `cd K && bash araclar/qa-yerel.sh 02-04-ydt-temel-dikey 07-hyperframes-kural 124.1,127.6,130.2 130.2 --hazirla`
(124,1 = tablo satırları bitti · 127,6 = ad satırı bitti · 130,2 = belirteç bitti, son düzen).

## Bakılan kareler ve bulgu

| Kare | Bulgu |
|---|---|
| `k/07-hyperframes-kural-124.1.png` | 3 satır + 6 simge tam; ad satırı ve alt boş (henüz söylenmedi); altyazı dilim 2 |
| `k/07-hyperframes-kural-127.6.png` | ad satırı tam (`+ V-ing` g kuyruğu ayraç ucunun üstünde, temas yok); alt boş (128,08'de gelir) |
| `k/07-hyperframes-kural-130.2.png` | son düzen: bant 380–1390 dolu; belirteç y 1380, altyazı 1440'tan başlar, arada boşluk var |
| `k/koyu/07-hyperframes-kural-130.2.png` | koyu: rozet turuncu dolgu + koyu yazı, `ikincil` kalıplar okunur |
| `k/ara/` 116,5 · 118,0 · 122,3 · 128,2 · 129,75; kontak `k/ara/kontak-ara.png` | 116,5 içerik bandı boş (aşağıda not 1); çizim ortası, kinetik ve belirteç ortası temiz |

Bilet simgesinin sağ ucu ≈ 1027 (eğim −0,06), kenar sınırı 1032 içinde.

## Kod yolu
- Şef: `SPEC.md` yazdı; `yardim.py`, `olay.py`, `calistir.sh` dikey sahne 01'den kopyalandı. `calistir.sh` Edit ile uyarlandı
  (başlık, `KARE=523`, telefon kontağı 3 sn aralık 6 kare). `ONIZLE_YALNIZ`, `yuk1`, koşullu Homebrew PATH kalıptan geliyor.
- agy (`agy-filo tek --rol kod`, gemini-3.8-flash-high, 312 sn, başarılı): `uret.py` (445 satır). Özet:
  `/home/sef/.claude/canavar/agy-filo/20261115-121935`.
- Şef okuması: SPEC'e uyuyor. Tek düzeltme Edit ile: rozet grubu kimliği `ku-rz` (sözleşme satırı 49 ile aynı ad).
- agy "değişen" listesi 06, 08, 09, 03, 05 sahne dosyalarını ve `sozlesme.md`'yi de gösterdi: paralel oturumların eşzamanlı işi
  (her birinin kendi `SPEC.md`'si var). Bu sahne o dosyalara dokunmadı.

## Açık noktalar
1. **İlk 4 sn içerik bandı boş.** 113,37–117,44 arasında yalnız HUD + altyazı var (geçiş sonrası 3,67 sn; ≤ 4 sn kuralı ve
   "9 sn boş çerçeve yok" kuralı tutuyor). Sebep: BRIEF ilk satırı 117,44'e koyar ve boş tablo/başlık yasaklar. "Kural kartı. Bu derste
   üç fark gördük." için görsel istenirse seçenek: 116,08'de (`üç`) satır yuvalarına soluk 1 · 2 · 3 numarası. Karar Nadir'de.
2. **Tren ve bilet sadeleştirmesi.** Kaynak çizimden türetildi (lokomotif, kısa bilet); 05 sahnesindeki tam tren/bilet ile birebir değil.
3. **Altyazı 44 px.** İstem "yazı tabanı ≥ 50" der; BRIEF §2 ve `kunye.js` altyazıyı 44 yazar. 14 sahne tutarlılığı için BRIEF izlendi.
4. **Bant karaokesi yok.** İstem "karaoke alt bantta" der; Nadir 03.11 kararı (şerit yok) ve sahne 01 ile aynı. Dilim 1 (113,87–120,43)
   söylenmeden önce görünür; `altyaziMetin` kuralıyla aynı.
5. **El yazısı.** Caveat yazıları soldan maskeyle açılır; HyperFrames sahnelerinde TegakiEngine "ayrı karar" (BRIEF §1, K26).
6. HUD bu sahnede `uret.py` içindeki `kunye_tam_svg()` ile çizilir; `yardim.py` dikey 01 kopyası olarak değişmeden kaldı (yalnız çip çizer).
   Ölçüler sözleşme satırı 49 ile aynı.
7. `hyperframes check` koşulmadı (istem kapısı `qa-yerel.sh`); render, `video.mp4`, `kontrol.png`, telefon kontağı yok (render yasak).
8. `uret.py` / `olay.py` `-I` olmadan koşar: fontTools kullanıcı site-packages içinde (sahne 01 not 6 ile aynı).

Dosyalar: `SPEC.md`, `uret.py`, `yardim.py`, `olay.py`, `calistir.sh`, `proje/index.html`, `olaylar.json`, `k/`, `RAPOR.md`.
