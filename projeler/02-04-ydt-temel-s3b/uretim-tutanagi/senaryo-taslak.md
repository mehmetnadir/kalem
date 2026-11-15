# 02-04-ydt-temel-s3b · kol b senaryo taslağı (A/B deneme kolu, değişken `kanca`)

Durum: TASLAK (istem BK-0204S3, 15.11.2026). Ses sentezi, sahne kodu, render YOK.
Bağlayıcı: `D/.claude/docs/huni-ab-sozlesme.md` (v1, §2–§4) · `D/.claude/docs/huni-v2-standart.md` (§1–§7).
Kol a: `../../02-04-ydt-temel-s3/` (ölçülmüş süre 28,31 sn, `anlatim.m4a` ffprobe 28.310000; `zaman.json`, `ortak/anlatim/sureler.json`).

## 1. Künye

| Alan | Değer |
|---|---|
| Paket | `02-04-ydt-temel-s3b` · sürüm kimliği `s3b` · `utm_content` = `s3b-<açıklama seti>` (sözleşme §4) |
| Varyant | `{"grup": "s3", "kol": "b", "degisken": "kanca", "deger": "yanlis-cumle"}` |
| Kol a değeri | `kopru`: kapak başlığı Türkçe kavram (`TARİFE ≠ PLAN`), etiketler İngilizce biçim (`leaves` / `am going`), ses İngilizce örnek cümle. Kısa kod `tarife → leaves · plan → am going` (kol a `meta.kapak.canAlici`). Üç değerden en yakını; tam uymaz (BK-RAPOR §e 4) |
| Kol b değeri | `yanlis-cumle`: ekranda gerçekten yanlış İngilizce cümle + "Hata nerede?" sorusu; düzeltmeyi değer cümlesinin kendisi (cümle 1, kol a sesi) verir |
| Neden bu değer | s1 çifti {`kopru`, `soru`} (`../../02-04-ydt-temel-s1b/uretim-tutanagi/kol-b.json`). s3 çifti s1'den farklı olmalı (sözleşme §3) ve S1b değeri `soru` seçilmez (istem) → tek seçenek `yanlis-cumle`. Kol a `soru` sayılsa da sonuç aynıdır |
| Yanlış cümle | `The train to İzmir is leave at 7 pm today.` (yalnız ekranda; seslendirilmez). Hata `is leave`: `be` + yalın fiil, İngilizcede kurulmaz. Doğrusu = değer cümlesi `The train to İzmir leaves at 7 pm today.` (ana ders cümle 5, D-0204) |
| Neden bu yanlış | iki zamanın karışımıdır (şimdiki zamanın `is` yardımcısı + geniş zamanın yalın fiili). İzleyiciyi dersin sorusuna götürür: `leaves` mı, `-ing` mi? Değer sahnesindeki öğrenci sorusu ("Neden -ing yok?") bu soruyu sürdürür. Kol a jürisinin elediği tartışmalı yanlışlar (`I go … tonight`, `is leaving`) kullanılmaz (`../../02-04-ydt-temel-s3/uretim-tutanagi/juri/s3.dil.md` madde 2, `s3.kaynak-kural.md` madde 1) |
| Ses kadrosu | kol a ile aynı: öğretmen `gsJ9nrlXYbPztJxC4fwc` (kanca, değer, kaydet) · öğrenci `oPC5I9GKjMReiaM29gjY` (değer sorusu, çağrı) |
| Kanal katmanı, künye, rozet | kol a ile aynı (`../../02-04-ydt-temel-s3/sahneler/01-hyperframes-kapak/SPEC.md` §3.5; `@ydspublishing`, `YDT · BASIC`) |

## 2. Senaryo

**TR** / **EN** = ses parçasının dili. Kalın = kol b'de değişen. Zamanlar küresel sn. Kol b zamanı tahmindir (§4): kanca sözü ölçülmedi,
sonraki her söz kol a'nın ölçülmüş zamanı + 1,15 sn.

| Sahne | Konuşan | Ses metni (söylenen) | Ekran metni | Görsel fikir |
|---|---|---|---|---|
| **1 Kanca · `01-hyperframes-kapak` · 0,00–4,15** (kol a 0,00–3,00) | **öğretmen** | **TR "Hata nerede?"** · **ilk söz 0,40** · **YENİ CÜMLE — jüri bakacak** · 2,15'ten **EN** "The train to Izmir leaves at seven …" (cümle 1 başı; kol a ile aynı ses, önbellek) | **0,00: başlık `HATA` / `NEREDE?` (sarı hap) · rozet `YDT · BASIC` · kanal katmanı** · **0,40 (`Hata`): yanlış kart satır 1 `The train to İzmir`** · **≈ 0,85 (`nerede?`): satır 2 `is leave at 7 pm today.`** · **altyazı `Hata nerede?`**, 2,10'dan altyazı `The train to İzmir leaves at 7 pm today.` (kol a ile aynı metin) · **3,35 / 3,71 / 3,95: satır 2 doğrusu `leaves` · `at` · `7`** (kol a kalıbı) · **`leaves` / `am going` etiketleri YOK** | **Kol a çizimleri: solda tren + saat (kollar yedide, rakamsız). Sağda öğretmen figürü küçük (≈ 250 px), trene işaret eder; bilet yok. `nerede?` sonunda satır 1'in sağına mürekkep el çizimi `?`. 2,15–2,79 bekleme (arama süresi). 2,79 (`Izmir`): `is leave` üstüne mürekkep çizgi. 3,05–3,30 yanlış satır 2 solar. 3,15–4,00 kol a uçuşu: tren kart köşesine, satırlar 568 / 666'ya; başlık solar (uçmaz), konu adı açılır. Son hal = kol a sahne 02 kare 0. Ayrıntı §3** |
| 2 Değer · `02-hyperframes-ornek` · 4,15–17,14 (kol a 3,00–15,99) | öğretmen | kol a ile aynı: **EN** "… p.m. today." · **EN** "I am going to the movie theater tonight." (cümle 1 sonu) | kol a ile aynı: Kart 1 `The train to İzmir` / `leaves at 7 pm today.` · zaman çizgisi `now` · `7 pm` · `tonight` · etiketler `gelecek · V-s` · `gelecek · am + V-ing` · Kart 2 `I am going to the` / `movie theater tonight.` · künye `Simple Present vs Present Continuous` + `YDT · BASIC` · `@ydspublishing` · altyazı | kol a ile aynı: `pm`, `today.` sözcük sözcük (`p.m.` 4,15 · `today.` 4,55); `today.` çapasında eksen, `now`, `7 pm` çentiği, kalem oku, sarı daire, `gelecek · V-s`; kart 2 sözcük sözcük + bilet (`I` 5,60 … `tonight.` 7,08); `tonight` noktası + `gelecek · am + V-ing` |
| | öğrenci | kol a ile aynı: **TR** "Hocam, tren de plana göre kalkmıyor mu? Neden -ing yok?" | kol a ile aynı: balon `Hocam, tren de plana` / `göre kalkmıyor mu?` / `Neden -ing yok?` | kol a ile aynı: zaman çizgisi söner, kart 2 yukarı; öğrenci başı + balon, soru sözcük sözcük (`Hocam,` 8,15); `Neden` (10,87) çapasında sarı bağ balon → `leaves`; cümle sonu 0,75 sn duraklama |
| | öğretmen | kol a ile aynı: **TR** "Planı bir kişi yapar. Tren tarifeye uyar: geniş zaman." | kol a ile aynı: `person` → `plan` · `train` → `timetable` (oklar çizilir) | kol a ile aynı: balon söner, öğretmen kalemle (`Planı` 12,66); sarı ok el → `am going`, `person → plan`; tren bağı, `train → timetable` (`Tren` 14,58 · `tarifeye` 14,98); `geniş` (16,34) çapasında `leaves` sarı altçizgi |
| 3 Kaydet · `08-hyperframes-kaydet` · 17,14–22,48 (kol a 15,99–21,33) | öğretmen | kol a ile aynı: **TR** "Bu, üç farktan yalnız biri." · **TR** "Bir arkadaşına gönder; o da karıştırıyor." | kol a ile aynı: kart `Tarife → leaves,` / `plan → am going.` (oklar çizilir; tren ve bilet ikonu satır başında) · gönder simgesi + `Arkadaşına gönder` · yer imi + `Kaydet` · künye · `@ydspublishing` · altyazı | kol a ile aynı: kart `Bu,` (17,69) çapasında çizilir, sahne sonuna kadar sabit; `Bir` (19,92) çapasında gönder simgesi + yer imi + `Kaydet`; `arkadaşına` (20,16), `gönder;` (20,68) kinetik; `gönder;` çapasında `leaves` hapı altçizgiye döner (aynı anda tek sarı) |
| 4 Çağrı · `03-hyperframes-cta` · 22,48–29,46 (kol a 21,33–28,31) | öğrenci | kol a ile aynı: **TR** "Bu sadece başlangıç." · **TR** "Dersin tamamı YDS Publishing YouTube kanalında." | kol a ile aynı: ana dersin kapağı (16:9 kart) · `Bu sadece başlangıç.` · `@ydspublishing` (sarı hap) · `YouTube` · künye · kanal katmanı · altyazı | kol a ile aynı: kapak kartı sahne başında girer (22,48); `Bu` · `sadece` · `başlangıç.` kinetik (23,03 · 23,27 · 23,83); `YDS` (26,22) çapasında hap çizilir, hap yazısı kalemle; `YouTube` (27,34) kinetik; son söz + 1,0 sn durgun kuyruk |

## 3. Kanca ayrıntısı (sahne 01, kol b)

Zaman sözcük çapasından okunur (kol b `ortak/anlatim/sozcukler.json`, sentez sonrası). Kanca sözcükleri tahmindir; cümle 1 sözcükleri kol a
`sureler.json` göreli zamanı + 2,15 (`The` +0,00 · `train` +0,28 · `Izmir` +0,64 · `leaves` +1,20 · `at` +1,56 · `seven` +1,80 · `p.m.` +2,00).

| # | Olay | sn | Çapa |
|---|---|---|---|
| 1 | Kapak tabanı: kanal katmanı · rozet son konumunda · başlık `HATA` / `NEREDE?` sarı hap (boy motor ölçer, üst sınır kol a B 190) · tren + saat (sol) · öğretmen figürü (sağ, ≈ 250 px, işaret pozu; kapak B figürü). Kart yeri boş. Konu adı, etiket, bilet YOK | 0,00 | söz öncesi |
| 2 | `HATA` altına sarı el altçizgisi (kol a darbesi) | 0,30–0,80 | söz öncesi |
| 3 | Altyazı dilimi `Hata nerede?` açılır | 0,35 | `Hata` − 0,05 |
| 4 | Satır 1 `The train to İzmir` kırpmayla (Fredoka 700 64, x 97, taban 986 = kol a R1_K) | 0,40–0,70 | `Hata` |
| 5 | Satır 2 `is leave at 7 pm today.` kırpmayla (taban 1084 = kol a R2_K) | ≈ 0,85–1,25 | `nerede?` |
| 6 | Mürekkep el çizimi `?` satır 1'in sağında (darbe) | ≈ 1,30–1,55 | `nerede?` sonu |
| 7 | KAPAK KARESİ: kol b A kapağı (`kapak-taslak.md`) | ≈ 1,75 (kare 52) | bekleme |
| 8 | Altyazı kapanır; cümle 1 altyazısı açılır (kol a EKRAN metni) | ≈ 1,95 · 2,10 | `The` − 0,05 |
| 9 | Söz `The train to Izmir`: satır 1 zaten ekranda, hareket yok (izleyicinin arama süresi; yanlış satır görünür kalır) | 2,15–2,79 | `The` |
| 10 | `is leave` üstüne mürekkep el çizgisi (darbe 0,20 sn); `?` solar | 2,79–2,99 | `Izmir` |
| 11 | Yanlış satır 2 solar (`power1.in`) | 3,05–3,30 | `leaves` öncesi |
| 12 | Başlık iki satır solar (uçuş yok; satırlar yükselmeden önce) · saat + figür solar · tren kart köşesine uçar · satır 1 ve satır 2 yeri DY −418 kayar (986 → 568, 1084 → 666) | başlık 3,15–3,33 · çizim 3,15–3,45 · uçuş 3,15–4,00 | kol a `ucus` + 1,15 |
| 13 | Satır 2 doğrusu `leaves` · `at` · `7` kırpmayla (kol a satır 2 kalıbı) | 3,35 · 3,71 · 3,95 | `leaves` · `at` · `seven` |
| 14 | Konu adı açılır (`kunye_ac`) · kart 1 çerçevesi 4 kenar | 3,77–4,00 · 3,77–4,05 | kol a + 1,15 |
| 15 | Son hal = kol a sahne 02 kare 0 (devir): kanal + künye + kart (71, 472, 878×254) + satır 1 taban 568 + satır 2 `leaves at 7` taban 666 + tren köşede + altyazı. Son 12 kare geçiş altında | 4,07–4,15 | `p.m.` 4,15 → sahne 02 |

- Ekran metni sesten önce gelmez: kart satırları `Hata` ve `nerede?` çapasında gelir; doğrusu `leaves` sesiyle gelir. Başlık 0. karede
  görünür (kapak karesi istisnası; kol a `TARİFE ≠ PLAN` emsali). Jüri bakacak (BK-RAPOR §e 6).
- Yanlış cümle seslendirilmez. Öğretmen yanlışı okumaz; doğrusunu okur (cümle 1, kol a sesi). Ses ile ekran 2,15–3,05 arasında ayrışır
  (ses doğru, ekran yanlış); çizgi `Izmir` sözünde hatanın yerini gösterir, düzeltme `leaves` sözüyle gelir.
- Tek vurgu: `HATA` altçizgisi + `NEREDE?` hapı (kol a kuralı). `?` ve üstü çizme mürekkep renginde; kırmızı, yeşil, ✗ simgesi, emoji YOK.
- Yerleşim denetimi (sahne kodunda, motor ölçer): satır 2 `is leave at 7 pm today.` sağ ucu ≤ 960 − 20; figür üstü ≥ satır 2 altı + 24;
  saat üstü ≥ satır 2 altı + 6 (kol a denetim 3); `?` satır 2 ile çakışmaz.

## 4. Süre

Kanca hızı (kol a öğretmen, `sureler.json`): "Planı bir kişi yapar." 7 hece 1,68 sn (4,2 hece/sn) · "Bu, üç farktan yalnız biri." 9 hece
2,08 sn (4,3 hece/sn) · "geniş zaman." 4 hece 0,88 sn (4,5 hece/sn). "Hata nerede?" 5 hece → 5 / 4,3 = 1,16 + soru tonu → **≈ 1,20 sn**
(tahmin, aralık 1,00–1,40).

| Parça | Kol a (ölçülmüş) | Kol b (tahmin) | Fark (sn) |
|---|---|---|---|
| İlk söz | 1,00 (cümle 1) | 0,40 (kanca) | −0,60 |
| Kanca sözü | yok (kanca sesi = cümle 1 başı) | 0,40–1,60 (1,20; 2 sözcük) | +1,20 |
| Kanca → cümle 1 arası | — | 0,55 (cümle arası kuralı) | +0,55 |
| Cümle 1 (5,45 sn, aynı dosya) | 1,00–6,45 | 2,15–7,60 | +1,15 |
| Cümle 2 (öğrenci, 3,76) | 7,00–10,76 | 8,15–11,91 | +1,15 |
| Cümle 3 (4,48) | 11,51–15,99 | 12,66–17,14 | +1,15 |
| Cümle 4 (4,79) | 16,54–21,33 | 17,69–22,48 | +1,15 |
| Cümle 5 (öğrenci, 5,43) | 21,88–27,31 | 23,03–28,46 | +1,15 |
| Sahne 01 | 0,00–3,00 (3,00; 102 kare) | 0,00–4,15 (4,15; içerik 124–125 + 12 = 136–137 kare) | +1,15 |
| Sahne 02 | 3,00–15,99 (12,99; 402 kare) | 4,15–17,14 (12,99; 402 kare) | 0 |
| Sahne 08 | 15,99–21,33 (5,34; 172 kare) | 17,14–22,48 (5,34; 172 kare) | 0 |
| Sahne 03 | 21,33–28,31 (6,98; 239 kare) | 22,48–29,46 (6,98; 239 kare) | 0 |
| **Toplam** | **28,31** | **≈ 29,46** (aralık 29,26–29,66) | **+1,15** |

- Formül: toplam = ilk söz + d + 0,55 + 5,45 + 21,86 = 28,26 + d (d = kanca sözü süresi; 21,86 = cümle 1 bitişinden sona kadar kol a ile aynı).
- **UYARI: 28 sn sınırı aşılır.** Kol a cümle 1 ve sonrası değişmezse 28,00 − 27,31 = 0,69 sn kalır; ilk söz + kanca + ara buna sığmaz.
  Sesli her kanca 28'i aşar. Seçenekler BK-RAPOR §e 1.
- Sahne sınırları: 01 → 02 = cümle 1 başı + 2,00 (`p.m.` öncesi; kol a kuralı); 02, 08, 03 sınırları kol a + 1,15.
- Kare katı kayma: kayma = ilk söz + d − 0,45. Sentezden sonra ilk söz 0,35–0,45 arasında seçilir ki kayma 1/30 sn'nin katı olsun
  (örnek: d = 1,20 → ilk söz 0,4167, kayma 1,1667 = 35 kare). Böylece sahne 02, 08, 03 kol a karesiyle birebir hizalanır.

## 5. Ses

- Yeniden seslendirilecek: 1 cümle (yeni cümle 1, öğretmen, tek TR parça, 12 karakter): "Hata nerede?"
- Önbellekten: kol a cümle 1–5 (kol b'de cümle 2–6; `cumle-1.wav` … `cumle-5.wav`). Metin, dil, komşu parçalar, ses, model eleven_v4,
  tohum 0, HIZ_EN 0,9 aynı → anahtar aynı (`dijital-anlatim/araclar/iki-dilli/el.py` anahtarı; komşu yalnız aynı cümlenin parçasıdır,
  yeni cümle komşu anahtarı değiştirmez).
- `anlatim.m4a`, `sozcukler.json`, `altyazi.json`, `baslar.json` kol b için yeniden kurulur (sentez değil; `kur.py` zinciri).
- Okunuş: TR parça, IPA gerekmez. Soru tonu "nerede?" ile. Rakam, kısaltma, "Tam ders", süre sözü yok. Whisper kapısı (eşik 0,85) kısa
  sözde yanılabilir; kulak denetimi gerekir.

## 6. Paket notu (sözleşme §4)

- Kol b taşır: sahne 01 (yeni; kol a `01-hyperframes-kapak` kopyasından türer), kendi `zaman.json`, kendi `ortak/anlatim/`
  (cümle 1 yeni, 2–6 önbellek), `kapak-a.png` (`s3b-kapak-a`).
- Kol b `zaman_uret.py` farkları: `GIRIS_SN` 3,0 → cümle 2 başı + 2,00 (≈ 4,15; kol a yorumu "giriş ≤ 3 sn"); sahne son cümle numaraları
  02 → 4, 08 → 5, 03 → 6 (kanca cümle 1 olduğu için +1).
- Simge bağı: `02-hyperframes-ornek`, `08-hyperframes-kaydet`, `03-hyperframes-cta`, `ortak/` içindeki anlatım dışı klasörler.
  Bu sahnelerin `uret.py` dosyası paketi `Path(__file__).resolve()` ile bulur → kol a `sozcukler.json` ve `zaman.json` okunur → yerel zaman
  çizelgesi kol a ile aynıdır (bütün sözler aynı miktar kayar). Kol b'de yeniden koşturmak gerekmez; birleştirme kol b `zaman.json`'u kullanır.
- Hikâye kareleri, kapak B / C, açıklama setleri gruba aittir; kol b'de yinelenmez.
