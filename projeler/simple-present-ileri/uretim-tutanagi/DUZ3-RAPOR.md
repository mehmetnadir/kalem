# DUZ3-0202I — `simple-present-ileri` dersin kendi içerik düzeltmeleri (jüri (c) sınıfı) · 16.11.2026

> İstem: `uretim-hatti/istemler/DUZ3-0202I.md`. Üretici: Claude Opus 5.5 (`claude-opus-5-5`). Makine srv21 (Linux x86_64).
> Girdi: `uretim-hatti/raporlar/YV-DUZ-1511.md` §3–§4, `uretim-tutanagi/juri/YVJ-hukum.md`, `juri-olcutleri.md` §1, §2b, §2c, §2f.
> Render yok, mp4 yok, commit yok, alt ajan yok. Silinen dosya yok: eski ses `~/Silinecekler/2026-11-16-duz3-0202I/` altında
> (`~/Silinecekler/LISTE.md` satırı yazıldı). Dikey paketin raporu: `../simple-present-ileri-dikey/uretim-tutanagi/DUZ3-RAPOR.md`.
> Ön durum (16.11 yarıda kalan koşu): pakette DUZ3 izi yoktu; yalnız YV-DUZ kapak değişikliği vardı (dokunulmadı).

| Ölçü | Değer |
|---|---|
| Düzeltilen ses cümlesi (parça) | 5 (jüri 2 + kendi taramam 3), 3 cümlede |
| Düzeltilen ekran iddiası | 5 (kendi taramam) + sesle giden 3 etiket |
| Yeniden sentezlenen | 3 cümle, 5 parça, 260 karakter (≈ 1,27 TL); öteki parçalar eski sesten örnek-eşit |
| Ders süresi | 90,43 → 93,71 sn (+3,28) |
| Whisper en düşük (eşik 0,85) | 0,98 |
| Yeniden üretilen sahne | yatay 6 / dikey 6 (02 yalnız künye rozeti) |
| Kapak | değişmedi (gerekçe §5) |
| Tutarlılık kapısı | çıkış 1 — bu derste 0 sorun; 10 sorun `02-03-ydt-temel`de (başka oturum) |
| Çakışma kapısı | yatay çıkış 1 (8 hata), dikey çıkış 1 (6 hata, 5 uyarı); hiçbiri değişen öğede değil (§7) |

## 1. Cümle tablosu

J = jüri bulgusu (YV-DUZ §4) · K = kendi taramam (istem: "dersin başka cümlelerini de aynı gözle tara").

| # | Yer | Önce | Sonra | Gerekçe |
|---|---|---|---|---|
| J1 | ses c7 parça 1 | Hayır. Tarife, program, takvim kesinse Simple Present. | Yarın tek başına will istemez. Tarife, program, takvim kesinse Simple Present seçilir. | "Hayır" `will take off`u yanlış sayar; cümle dilbilgisi olarak doğrudur (EK-5c). Jüri önerisinin ikinci yarısı ("will tahmin ve ani karar içindir") parça 2'yi yineler ve öğrencinin gerekçesini (yarın → will) düzeltmez. Yeni cümle gerekçeyi düzeltir, will'i yasaklamaz. |
| J2 | ses c4 parça 4 | Owns ve costs durum fiilidir: ing almaz. | Owns ve costs burada durum anlatır: -ing almaz. | Mutlak kural; `cost` geçici durumda -ing alır (*The repairs are costing us a fortune.*). Jüri önerisi doğru, aynen alındı. "-ing" yazımı ses kuralı 4'tür: yalın "ing" Türkçe "ink/İngi" okunur, "-ing" /ɪŋ/ okunur. |
| K1 | ses c7 parça 2 | Will is for predictions and sudden decisions. | We often use will for predictions and sudden decisions. | Kapalı liste; will kesin/planlı gelecekte de doğrudur (*The meeting will start at nine.*). "Hayır" kalkınca bu cümle aynı yanlış izlenimi tek başına taşırdı. |
| K2 | ses c7 parça 3 | Durum fiilleri know, own, cost: now gelse bile ing almaz. | Durum anlamındaki know, own, cost: now gelse bile -ing almaz. | Mutlak kural (istemin "-ing almaz" örneği); kapsam "durum anlamı" ile çizildi (*It's costing me a lot.* doğrudur). |
| K3 | ses c3 parça 4 | Bağlaç var, zaman değişmez: gives. | Bağlaç gelse de genel gerçek Simple Present kalır: gives. | Mutlak kural; zaman bağlaçlarında zaman değişir (*I'll call you when I arrive*, when + will değil). Doğru kapsam: genel gerçek Simple Present kalır. |
| K4 | ekran 05 kart | `tomorrow` `≠ will` (kırmızı) | `tomorrow` `tuzak` (kırmızı) | Yanlış denklik (*I'll see you tomorrow.*). Yeni yazı sesle birebir: "Tomorrow tuzaktır." (61,81). |
| K5 | ekran 06 | `will take off` üstünde büyük kırmızı ✗ ("Hayır" anı) | ✗ yok; `will take off ?` kalır, «seçilir» sözünde `takes off ✓` | EK-5a: üstü çizili cümle hatalı değil. |
| K6 | ekran 06 | `will` `=` `predictions` · `sudden decisions` | `will` el oku + `often` → `predictions` · `sudden decisions` | "=" denkliği; ses K1 ile aynı iddia. |
| K7 | ekran (sesle) | 03 `zaman değişmez:` · 04 `durum fiili:` · 06 başlık `durum fiilleri` | 03 `genel gerçek:` · 04 `durum anlamı:` · 06 `durum anlamında` | Ekran yazısı yeni sesle aynı iddiayı taşır; sözcük zamanlı. |

Meta (`senaryo.json` `meta` + `surumler.json` `video`):

| Alan | Önce | Sonra |
|---|---|---|
| `canAlici[1]` | Tomorrow gördün diye will deme: tarife, program, takvim = Simple Present | Tomorrow tek başına will istemez: tarife, program, takvim kesinse Simple Present seçilir |
| `canAlici[2]` | Durum fiilleri (know, own, cost) now gelse bile ing almaz | Durum anlamındaki know, own, cost now gelse bile -ing almaz |
| `canAlici[4]` | Bağlaçtan sonra da zaman değişmez: Although ... it gives | Bağlaç gelse de genel gerçek Simple Present kalır: Although ... it gives |
| `amaclar[3]` | YDT kökünde bağlaç sonrası zamanı korumak | YDT kökünde bağlaçlı cümlede genel gerçeği Simple Present ile kurmak |
| `surumler[dikey-tam].kapak` | TARİFE = SIMPLE | YARIN / WILL mi? (gerçek dikey kapak; YV-DUZ'da değişmişti) |

Gözden geçirdim, değiştirmedim:
- c2 "Negative and question: does plus base verb." — hemen önceki "he, she, it takes s" bağlamında doğrudur (temel ders DUZ2 emsali).
  Bağlamsız okunursa I/you/we/they için `do` gerekir; cümle 2 yeniden sentezlenirse bütün sahneler kayar. Dil jürisine not.
- c5 "Tarife kesin, Simple Present. Tomorrow tuzaktır." — bu kökün tuzağıdır; yeni c7 ile tutarlı.
- c7 "Kod: tarife varsa Simple Present, tahmin varsa will." — seçim kodu; jüri ve YV-DUZ §3 doğru saydı. Not: kanıtlı tahminde
  `be going to` da gelir; kod iki seçenek arasındaki ayrımı verir.
- `canAlici[0]`, `canAlici[3]`, `youtube.json` metinleri (YV-6 geçti), `youtube-aciklama.md` (aynı iddia yok).

Değişen dosyalar (iki paket ortak `ortak/anlatim` dizinini kullanır; dikey dizin bağdır):
`ortak/anlatim/{senaryo.json, sureler.json, sozcukler.json, sozcuk_uret.py (BASLAR), altyazi.json, METIN.md}`,
git dışı `ortak/anlatim/{anlatim.wav, anlatim.m4a, anlatim.m4a.imza, cumle-1…7.wav}`, `zaman.json`, `surumler.json`, `BRIEF.md`,
`youtube.json`, `youtube-aciklama.md`, `ortak/kunye.js`, `sahneler/01/{uret.py, yardim.py, proje/index.html}`,
`sahneler/03/{sahne-03.js, calistir.sh}`, `sahneler/04/{sahne.js, calistir.sh}`, `sahneler/05/{sahne.js, calistir.sh}`,
`sahneler/06/{uret.py, yardim.py, zamanlar.json, calistir.sh, olaylar.json, proje/index.html}`, `sahneler/90-hyperframes-kapak/yardim.py`.

## 2. Ses ve süre

Yöntem (değişmeyen ses değişmez):
1. Sunucu önbelleğinde bu dersin parçası yoktu (ağsız anahtar benzetimi 0 / 22, iki hız anahtarı). Cümlenin bütününü sentezlemek
   değişmeyen İngilizce kökleri de yeni sesle değiştirirdi (EK-11 kulak dinlemesi yeniden gerekirdi) ve sahne zamanlarını bozardı.
2. `el.py` yalnız değişen parçaları taşıyan geçici senaryoyla koştu: c3 p4 ve c4 p4 tek parçalı cümle, c7 p1–p3 üç parçalı cümle.
   Komut: `HIZ_EN=0.8 timeout 1500 bash araclar/ses-sunucu.sh --kok ~/is/uretim-0204/duz3-0202I/kok simple-present-ileri`
   (vekil, eleven_v4, öğretmen sesi). rc 0, 5 / 5 parça kapıdan geçti, 260 karakter. `HIZ_EN` 0,8 = Mac hattının `el.py` varsayılanı.
3. Ekleme: eski parçalar eski `anlatim.wav`'dan 48 kHz örnek-eşit kesildi; yeni parça `aresample=48000` (kur.py süzgeci).
   Parça arası el.py kuralıyla (tr → tr 0,15 sn; tr → en 0,25 sn). Cümle arası 0,55 sn korundu. Betik metni dosyaya yazılmadı
   (yazma kapısı 15+ satır `.py` engeli); stdin ile koştu.
4. `kur.py` → `anlatim.wav`; `altyazi_uret.py` → `altyazi.json`; `metin_kur.py` → `METIN.md`; `ses-paketle.py --yaz --paket` → m4a.

Örnek-eşitlik kanıtı (PCM sha256, ilk 16):

| Bölge | Eski aralık (sn) | Yeni aralık (sn) | sha256 | Sonuç |
|---|---|---|---|---|
| 0 → c3 p4 başı | 0–28,93 | 0–28,93 | `62d831671895bdbb` | EŞİT |
| c4 p1–p3 | 33,00–44,29 | 33,88–45,17 | `b3c2551b7842adc7` | EŞİT |
| c5 + c6 | 48,84–65,88 | 50,04–67,08 | `b14a93cbed67c3e3` | EŞİT |
| c7 p4–p5 | 81,26–89,43 | 84,54–92,71 | `e0ecc92923229d84` | EŞİT |

| Ölçü | Önce | Sonra |
|---|---|---|
| c3 süresi | 14,25 sn | 15,13 sn |
| c4 süresi | 15,29 sn | 15,61 sn |
| c7 süresi | 23,00 sn | 25,08 sn |
| Cümle başları | 1,00 · 3,55 · 18,20 · 33,00 · 48,84 · 61,96 · 66,43 | 1,00 · 3,55 · 18,20 · 33,88 · 50,04 · 63,16 · 67,63 |
| Ders süresi (`zaman.json` son `t_son`) | 90,43 sn | 93,71 sn |
| Sözcük sayısı (`sozcukler.json`) | 170 | 182 |
| `anlatim.wav` sha256 | `b9466ff421aa` | `cd3d7cdf8829` |
| `anlatim.m4a` sha256 | — (sunucuda yoktu) | `c305265deb78` |

Whisper (faster-whisper large-v3-turbo int8, eşik 0,85; rapor `~/is/uretim-0204/duz3-0202I/kok/…/sentez.wav.rapor.json`):

| Parça | Dil | Metin | Duyulan | Benzerlik |
|---|---|---|---|---|
| c3 p4 | tr | Bağlaç gelse de genel gerçek Simple Present kalır: gives. | Bağlaç gelse de genel gerçek Simple Present kalır, Gives. | 1,00 |
| c4 p4 | tr | Owns ve costs burada durum anlatır: -ing almaz. | Owns ve Costs burada durum anlatır. Ink almaz. | **0,98** |
| c7 p1 | tr | Yarın tek başına will istemez. Tarife, program, takvim kesinse Simple Present seçilir. | (aynı; "Will") | 1,00 |
| c7 p2 | en | We often use will for predictions and sudden decisions. | (aynı) | 1,00 |
| c7 p3 | tr | Durum anlamındaki know, own, cost: now gelse bile -ing almaz. | … Now gelse bile ING'yi almaz. | **0,98** |

**DİKKAT:** "-ing" iki parçada Whisper'da "Ink" ve "ING'yi" diye yazıldı. Ses metni /ɪŋ/ IPA'dır; "ING'yi" fazladan "-yi"
duyulduğunu gösterebilir. EK-11 kulak dinlemesi (Nadir): c4 48,57 sn ve c7 83,17 sn.

## 3. Sahneler ve kareler (kendim baktım)

| Sahne | Değişiklik | Kare / içerik kare |
|---|---|---|
| 01 giriş | rozet `YDT · ADVANCED` → `YDT · İLERİ`, künye `· YDT İLERİ` (HV-24) | 102 / 90 |
| 02 kanca | künye rozeti (`ortak/kunye.js`) | 451 / 439 |
| 03 örnek 1 | c3 p4 bloğu yeni sözcüklere: ok 29,81, `genel gerçek:` 30,21–30,93, formül 30,61–31,41, `gives` dairesi 32,58, tepki 32,26 | 456 → 482 / 470 |
| 04 örnek 2 | `TBAS` 32,45 → 33,33, p1–p3 sabitleri +0,88; p4 bloğu: kutu 47,41, `durum anlamı:` 47,66, `is own-ing` 48,10, silme 48,57 | 487 → 497 / 485 |
| 05 örnek 3 | `TBAS` 48,29 → 49,49, bütün sabitler +1,20 (yerel kare aynı); `≠ will` → `tuzak` 61,85 | 406 / 394 |
| 06 soru + form | sözcük sıraları yeni c7'ye; ✗ kalktı; takvim ve balon «istemez»de; `takes off ✓` «seçilir»de; `will —often→`; `durum anlamında`; çipler Durum − 0,46 / Kod − 0,42; `Next lesson` will + 0,13 | 901 → 963 / 933 |

`calistir.sh` dosyalarında `N`/`KARE`, `TBAS`, kare anları yeni değerlere çekildi. Kaydırma aracı aralıktaki her ondalık sabiti
listeledi (04: 47, 05: 45); hepsi zaman değeriydi. HF 01 ve 06: `uret.py` + `olay.py` + tema (render öncesi adımlar), assert'ler geçti.

Komut: `node araclar/sahne-kare.mjs simple-present-ileri <sahne> <t,…> sahneler/<sahne>/k/duz3 --tema acik --port 41333 --sunucu 41022`
(var olan başsız Chrome ve önizleme sunucusu; yeni tarayıcı açılmadı). Kareler git dışı:

| Sahne | Anlar (sn) | Gözlem |
|---|---|---|
| 01 | 1,2 · 2,9 | künye `· YDT İLERİ`, İ doğru; taşma yok |
| 02 | 9,0 | künye aynı |
| 03 | 22,0 · 29,6 · 30,8 · 31,6 · 32,4 · 33,25 | `genel gerçek:` sözle yazılıyor; formül kartı ve `gives` dairesi doğru sırada. Tepki figürünün eli kart sol kenarına değiyor (yerleşim değişmedi, eski tasarım) |
| 04 | 36,0 · 45,9 · 47,9 · 48,75 · 49,4 | `durum anlamı: own · cost · know` kutuya sığıyor; `is owning` silme ve ✗ doğru |
| 05 | 53,0 · 61,9 · 62,4; koyu 62,4 | `tomorrow` `tuzak` kırmızı; sesle aynı an |
| 06 | 66,0 · 69,3 · 73,8 · 77,2 · 80,8 · 85,9 · 89,0 · 92,8; koyu 85,9 | ✗ yok; `takes off ✓`; `will —often→ predictions · sudden decisions`; `durum anlamında`; Kod satırları ve `Next lesson` taşmıyor; koyuda okunur |

## 4. Kapak

Değişmedi. YV-DUZ §4 bu ders için "kapak düzeltildi (§3)" der; kapak YV-DUZ'da "YARIN / WILL mi?" oldu. Yeni metin dersin c6
sorusudur ve yeni c7 ("Yarın tek başına will istemez") ile aynı iddiayı taşır. `sahneler/90-hyperframes-kapak/yardim.py`
`ROZET` sabiti `YDT · BASIC` → `YDT · İLERİ` (kullanılmayan sabit; kapak `uret.py` kendi `ROZET`ini kullanır, kapakta zaten
`YDT · İLERİ`). Kapak PNG'leri ve 168 px önizleme yeniden çekilmedi.

## 5. Yayın verisi zamanı (`youtube.json`, `youtube-aciklama.md`; ders zamanı)

| Öğe | Önce | Sonra | Kural |
|---|---|---|---|
| Bölüm 1 | 0,00 (00:00) | 0,00 (00:00) | ilk bölüm 0 |
| Bölüm 2 | 17,65 (00:18) | 17,65 (00:18) | sahne 03 başı |
| Bölüm 3 | 32,45 (00:32) | 33,33 (00:33) | sahne 04 başı |
| Bölüm 4 | 48,29 (00:48) | 49,49 (00:49) | sahne 05 başı |
| Bölüm 5 | 61,41 (01:01) | 62,61 (01:03) | sahne 06 başı |
| En kısa bölüm | 13,12 sn | 13,12 sn | ≥ 10 sn |
| Bildirim | 33,00 | 33,88 | 30 sn sonrası ilk cümle başı (c4); son 20 sn dışı (sınır 73,71) |

Dikey `youtube.json` yatayla birebir; `youtube-aciklama.md` tek fark `utm_content=dikey-tam`.

## 6. Kapılar

```
$ python3 uretim-hatti/betikler/yv-tutarlilik.py --kilitli simple-present-temel,simple-present-temel-dikey,02-04-ydt-temel-dikey
[SORUN] zaman: 10   (hepsi 02-03-ydt-temel: bölüm 4–13 sahne başı değil — başka oturumun dersi)
öteki 8 denetim TAMAM · toplam sorun 10 · kilitli pakette 0           → çıkış 1
simple-present-ileri: sorun 0 (bilgi: başlık 62 karakter, hedef ≤ 60)

$ node araclar/cakisma-kapisi.mjs simple-present-ileri --port 41333 --sunucu 41022 --json …/kapi-ana.json   → çıkış 1
01 cg:path0 × cg:text0 (3,00) · 04 araba × sahip, genellikle × otobus · 06 fing × s3:path1/2, rb0/rb1/rb2 × s3:path5
02, 03, 05: çakışma yok · toplam 8 hata, 0 uyarı
```

Çakışma çözümlemesi: 01 halka "kalkıyor" sözcüğünü kasıtlı sarar. 04 etiketleri (`sahip`, `genellikle`) ve çizimler değişmedi
(yalnız zaman kaydı). 06 `fing × s3:path1/2` = `-ing` üstündeki kasıtlı çarpı; `rb* × s3:path5` = `I am knowing` üstündeki kasıtlı
kırmızı çizgi. Değişen öğelerde (`genel gerçek`, `durum anlamı`, `tuzak`, `often`, el oku) hata 0. Taban (HEAD) ölçülmedi.

`python3 -m py_compile`: 06 `uret.py` (iki paket) üretim sırasında koştu; JS sahneleri karelerde hatasız çizildi.

## 7. Kısa video (`simple-present-ileri-s1`, yalnız rapor; dokunulmadı)

| Dosya | Aynı hata |
|---|---|
| `ortak/anlatim/senaryo.json` cümle 1 (+ `METIN.md`, `altyazi.json`) | ses "Tarife varsa will deme." — mutlak; will de doğru olabilir (J1 ile aynı aile) |
| `sahneler/02-paperjs-ornek/sahne-02.js` satır 99–127 | ekran `tomorrow ≠ will`, will kırmızı çizgi (K4 ile aynı) |
| `sahneler/01-hyperframes-kapak` (sahne-02.js satır 3 açıklaması) | `will` + kırmızı çarpı ("Tarife varsa / will ✗ / deme.") |
| `surumler.json` satır 13–20, `senaryo.json` `meta` satır 101–108 | eski `canAlici[1,2,4]` ve `amaclar[3]` kopyası |
| `senaryo.json` `meta.kancaKapak`, `BRIEF-S1.md` satır 1, 20 | `TARİFE = SIMPLE` ("=" denkliği) |

## 8. Düzeltemediklerim / açık kalanlar

| Madde | Sebep |
|---|---|
| EK-11 kulak dinlemesi (5 yeni parça; özellikle "-ing") | Nadir'in işi; Whisper süzgeçtir |
| Çakışma kapısı çıkış 1 | 8 hata değişmeyen ya da kasıtlı öğelerde (§6); bu işin kapsamı dışı |
| Tutarlılık kapısı çıkış 1 | 10 sorun `02-03-ydt-temel`de; yazma alanım dışında |
| 03 ve 04 `olaylar.json`, `zamanlar.json` | render yan ürünü (`yakala.py` son karede yazar); `calistir.sh` render öncesi yeniler. 05 yerel kareleri değişmedi. |
| c2 "does plus base verb" bağlamsız okunuşu | §1 notu; dil jürisi isterse c2 yeniden sentezlenir |
| `GRAMMAR` rozeti İngilizce | istem yalnız seviye rozetini istedi |
| mp4'ler bayat | render yasak; `calistir.sh` değerleri güncel |
| YVJ jürisi + DUZ3J ders jürisi | içerik değişti; §1b gereği yeniden koşmalı |

---
Son Güncelleme: 16.11.2026 (DUZ3-0202I oturumu).
