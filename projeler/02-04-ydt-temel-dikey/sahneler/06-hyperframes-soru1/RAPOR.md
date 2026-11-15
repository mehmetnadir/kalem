# Sahne 06 · soru anı 1 DİKEY (HyperFrames 1080×1920, 613 kare, 93,35–113,37 sn + 12 kare geçiş payı)

Durum: istem D-dikey (15.11.2026, srv21). Önizleme hazırlığı `ONIZLE_YALNIZ=1` ile koştu. Render yok, commit yok.
Tema: koyu

| Kapı | Sonuç |
|---|---|
| `qa-yerel.sh` çıkış kodu | **0** |
| Çakışma kapısı | çakışma yok (81 örnek, 35067 kutu) |
| Kare bakışı (açık 3 + koyu 1 + ara 7) | taşma, kesik yazı, binme, okunmaz kontrast, boş kare, platform bandında öğe YOK |
| Düzeltme turu | 0 (QA'dan önce SPEC 1 kez düzeltildi, §Kod yolu) |

## İçerik
- Kare 0: HUD tam (logo, ders adı 2 satır, rozet `YDT · BASIC`, çip `Question`). Üst şerit Fredoka 64: `The train … leaves at 7 pm today.` /
  `I am going … tonight.`; *leaves* ve *am going* sarı altlı.
- Soru anı 1: öğrenci başı (240 px) + el balonu, soru Caveat 64 sözcük sözcük (10 sözcük ≤ 12). Sarı nokta *tren* üstünde, bağ satır 2'nin
  sağından yükselir, satır arası kanaldan *leaves*'e gelir. *-ing* sarı altı. 97,74–98,41 olaysız duraklama; cevap 0,67 sn sonra.
- Cevap: balon söner, baş küçülüp alt sağa iner. Cevap 1: erkek öğretmen figürü (`standing-3`, 420 px) + `person ↳ plan ↳ am / is / are + V-ing`,
  sarı ok figürden *am going*'e. Cevap 2: `train ↳ timetable ↳ V1 / V-s` + tren (476 px), sarı ok trenden *leaves*'e. Öğrenci 1 sn baş sallar.
  "özne genelde cansızdır": *The train* altı, tren nabzı, uçak ve kitap simgesi (140 px).
- yanılgı: tarifeli gelecek planlanmış gelecekle karışır (docstring). Kırmızı, yeşil, emoji yok. `V-ing`, `V1 / V-s` hap (sözleşme satır 36).
- En çok 3 sarı belirteç: eski belirteç silinmez, `ikincil` ikizine solar (`klm_s`, `krm_s`, `ok_fig_s`, `ok_trn_s`); `V-ing` hapı 109,53'te düz yazıya döner.

## Olay listesi (olay · kare · küresel sn · cümle sözcüğü)

| # | Olay | Kare · sn | Sözcük |
|---|---|---|---|
| 1 | baş 3 yolu kalemle | 13 · 93,78 | — (ilk 12 kare durgun) |
| 2 | balon | 15 · 93,85 | 6 · Hocam, |
| 3 | soru sözcükleri (ilki) | 17 · 93,90 | 6 · her sözcük kendi t0'ında |
| 4 | sarı nokta + bağ (kanal) → *leaves* | 38 · 94,62 | 6 · tren |
| 5 | *-ing* altı; *am going* altı `ikincil`e | 109 · 96,98 | 6 · -ing |
| — | duraklama, olay yok | 97,74–98,41 | — |
| 6 | balon söner; baş alt sağa (x 892–1008, y 1230–1390) | 152 · 98,41 | 7 · Planı |
| 7 | figür + `person`; *leaves* altı `ikincil`e | 171 · 99,05 | 7 · kişi |
| 8 | ↳ `plan` | 179 · 99,33 | 7 · yapar: |
| 9 | sarı ok figür → *am going*; *am going* altı parlar | 205 · 100,17 | 7 · ben, |
| 10 | ↳ `am / is / are +` + hap `V-ing` | 243 · 101,45 | 7 · arkadaşım. |
| 11 | tren + `train`; figür oku ve *am going* altı `ikincil`e | 277 · 102,57 | 7 · Tren |
| 12 | ↳ `timetable` | 317 · 103,93 | 7 · tarifeye |
| 13 | sarı ok tren → *leaves* (kanal); *leaves* altı parlar | 334 · 104,49 | 7 · uyar. |
| 14 | öğrenci 1 sn baş sallar | 348 · 104,95 | 7 · uyar. sonu |
| 15 | TIMETABLE nabzı: *leaves* altı kalınlık + `timetable` nabız | 356 · 105,21 | 7 · Tarife |
| 16 | ↳ hap `V1 / V-s`; tren oku `ikincil`e | 406 · 106,89 | 7 · geniş |
| 17 | *The train* altı; `V-ing` hapı düz yazıya | 485 · 109,53 | 7 · özne |
| 18 | tren nabzı | 544 · 111,49 | 7 · tren, |
| 19 | uçak simgesi | 566 · 112,21 | 7 · uçak, |
| 20 | kitap simgesi (son hareket yerel 19,97 ≤ 20,03) | 589 · 112,97 | 7 · ders. |

`olaylar.json`: 44 ses olayı (27 `cizgi`). Altyazı: 4 dilim (cümle 6 + cümle 7 ×3), iki dilim aynı anda görünmez.

## Kapı sonucu (son koşu)
```
== KAPI
06-hyperframes-soru1 | çakışma yok (81 örnek, 35067 kutu)
== KARE (açık)  97.6 · 104.45 · 113.3
== KARE (koyu)  108
kapı çıkış kodu: 0
```
Komut: `cd K && bash araclar/qa-yerel.sh 02-04-ydt-temel-dikey 06-hyperframes-soru1 97.6,104.45,113.3 108.0 --hazirla`
(97,6 = soru, bağ, *-ing* altı bitti · 104,45 = cevap 1 + tren + `timetable` bitti · 113,3 = son düzen · koyu 108 = `V1 / V-s` + tren oku sönük).

## Bakılan kareler ve bulgu

| Kare | Bulgu |
|---|---|
| `k/06-hyperframes-soru1-97.6.png` | balon 3 satır tam; bağ satır 2'ye değmeden *leaves*'e iner; *am going* altı `ikincil`; altyazı 2 satır |
| `k/06-hyperframes-soru1-104.45.png` | figür erkek (şapka, yelek); zincir 1 + `V-ing` hapı okunur; tren 1005–1209; baş alt sağda, trene 21 px |
| `k/06-hyperframes-soru1-113.3.png` | son düzen: 3 sarı (*The train*, *leaves*, `V1 / V-s`); tren oku kanalda `ikincil`; uçak + kitap + baş tek sıra; bant 355–1390 dolu |
| `k/koyu/06-hyperframes-soru1-108.png` | koyu: hap yazısı koyu, turuncu dolgu üstünde okunur; `ikincil` oklar seçilir |
| `k/ara/` 93,5 · 95,3 · 98,75 · 100,9 · 101,95 · 105,3 · 109,95; kontak `k/ara/kontak-ara.png` | her anda ≤ 3 sarı belirteç; baş taşıma balonla çakışmaz; sarı → `ikincil` geçişleri doğru karede |

## Kod yolu
- Şef: `SPEC.md` yazdı; `yardim.py`, `olay.py`, `calistir.sh` dikey 01'den kopyalandı (`yardim.py` değişmedi). `calistir.sh` Edit:
  başlık, `KARE=613`, telefon kontağı `tile=5x4`. `olay.py`: docstring sahne no.
- agy 1. koşu: başlatıldıktan sonra şef sözleşmede iki ölçülmüş kural buldu (kuyruklu sözcük altçizgisi 0,48 em / Caveat 0,52 em; HF'de sarı yazı
  yerine hap). Koşu durduruldu, dosya yazılmadan önce. SPEC düzeltildi.
- agy 2. koşu (`agy-filo tek --rol kod`, gemini-3.8-flash-high, 236 sn, başarılı): `uret.py` yazdı.
  Özet: `/home/sef/.claude/canavar/agy-filo/20261115-122758/`. "değişen" listesindeki 09–12 sahne dosyaları ve `sozlesme.md` paralel oturumlarındır
  (sözleşmedeki yeni satır bir canvas sahnesine ait); bu iş yalnız `06-hyperframes-soru1/uret.py` yazdı.
- Şef okuması: SPEC'e birebir uyuyor; düzeltme gerekmedi.

## Açık noktalar
1. **Şerit satır 1 = 34 karakter.** İstem "satır ≤ 24 karakter" der; BRIEF §3 satır 6 metni açıkça verir (`The train … leaves at 7 pm today.`).
   Fredoka 64'te 968 px, 984 px'e sığar. BRIEF izlendi.
2. **TIMETABLE etiketi şeritte yok.** BRIEF "105,21 TIMETABLE nabzı (şeritte)" der ama şerit metninde etiket yok (satır 1'e yer kalmıyor).
   Nabız *leaves* altçizgisine (şeritteki tarife belirteci) + zincirdeki `timetable` sözcüğüne verildi.
3. **Altyazı boyu 44 ve bant karaokesi yok.** İstem "yazı tabanı ≥ 50" ve "karaoke alt bantta" der; BRIEF §2 ve öteki dikey sahneler (01) altyazıyı
   44 yazar, bantta karaoke çizmez. Tutarlılık için BRIEF izlendi; balon sözcükleri söylendiği anda gelir. 14 sahne için ortak karar ister.
4. **Soru anında alt bant boş.** 93,35–99,05 arası y ≈ 960–1392 boş (balon BRIEF'teki gibi y 540–960); cevap 2 bölgesi 102,57'de dolar.
   Sahne bitiminde bant dolu (§2.10).
5. **Figür oku başın yanından değil gövdenin yanından** çıkar (BRIEF §0 kuralı); Open Peeps pozlarında işaret eden kol yok (sözleşme satır 42).
6. **Baş başlangıç boyu 240 px.** BRIEF §2.8 "baş 160 px" der, satır 6 "baş küçülüp alt sağa iner" der: soru anında 240, cevapta 160.
7. Kare 0 sahne 05'in son düzeniyle birebir değil (05 son düzeni `leaves → TIMETABLE` şeridi + kart B); geçiş BookFlip, BRIEF satır 6 izlendi.
8. Render kısmı (`calistir.sh` sonu) koşmadı: istem render yasaklar. `nesneler.json` / `zamanlar.json` yok (dikey 01 kalıbı).

Dosyalar: `SPEC.md`, `uret.py`, `yardim.py`, `olay.py`, `calistir.sh`, `proje/index.html`, `olaylar.json`, `k/`, `RAPOR.md`.
