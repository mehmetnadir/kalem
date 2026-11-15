# DUZ3-0206T — `present-perfect-temel` dersin kendi içerik düzeltmeleri (jüri c sınıfı) · 16.11.2026

> Girdi: `uretim-hatti/raporlar/YV-DUZ-1511.md` §4 (bu dersin 1 satırı: c7) ve §3 (kapak dokunulmaz), `uretim-tutanagi/juri/YVJ-hukum.md`
> son not. Makine srv21 (Linux x86_64). Render yok, mp4 yok, alt ajan yok, commit yok. Silinen dosya yok: eski ses ve önceki oturumun paket
> içi yedeği `~/Silinecekler/2026-11-16-duz3-0206T/` altında (`~/Silinecekler/LISTE.md` satırı yazıldı). Dikey rapor:
> `../present-perfect-temel-dikey/uretim-tutanagi/DUZ3-RAPOR.md`.
> Önceki oturum bellek arızasıyla kesildi: senaryoda c4 ve c7 metni yazılmış, rozet `YDT · TEMEL` yapılmış, c4'ün 4 parçası sunucu önbelleğine
> sentezlenmişti (`_is/duz3/` altında HEAD kopyaları). Bu oturum metni yeniden denetledi, c5'i ekledi, c7'nin 2 parçasını değiştirdi, gerisini yaptı.

## 1. Cümle tablosu

| # | Cümle | Önce | Sonra | Kaynak | Gerekçe |
|---|---|---|---|---|---|
| 1 | c7 p3 | `For ve since süre,` | `For süreyi, since başlangıç noktasını söyler.` | jüri | since süre değil, başlangıç noktasıdır (c4 ve sahne 04 bunu doğru söyler). YV-DUZ önerisinin ilk yarısı aynen. |
| 2 | c7 p4 | `… just ve already yeni biten iş.` | `Bu zamanda never ve ever deneyimi, just az önce biten işi, already çoktan biten işi anlatır.` | jüri + kendi | already "yeni biten" değildir. YV-DUZ önerisi "already beklenenden önce biten işi" already'nin yalnız bir anlamını verir; *I've already seen this film* beklenti taşımaz. Jürinin kendi karşılığı ve sözlük karşılığı "çoktan"dır. YV-DUZ önerisi never/ever'ı düşürmüştü; ders onları da öğretir, geri kondu. "Bu zamanda" kapsam sınırıdır (EK-5b): never ve ever başka zamanlarda deneyim anlatmaz (*I never eat meat*). |
| 3 | c7 p1 | `Çünkü iş geçmişte bitti, ama etkisi şimdiye uzanıyor.` | `Çünkü üçünde de geçmiş şimdiye bağlanıyor.` | kendi | c4 örneği (*has played … for five years*, "başladı ve hâlâ çalıyor") bitmemiş iştir; "iş geçmişte bitti" üç örneğin birini yanlışlar (EK-5b). Önceki oturum metni virgüllüydü (`geçmiş, şimdiye`); özne–yüklem arasında virgül kaldırıldı. |
| 4 | c7 p5 | `Kod: have artı üçüncü hâl, geçmiş iş, şimdiki etki.` | `Kod: have artı üçüncü hâl, geçmişten şimdiye köprü.` | kendi | Aynı sorun (geçmiş "iş" bitmiş iş çağrışımı); c1–c2 köprüsüyle aynı dil. |
| 5 | c4 p4 | `Bu kez has, çünkü özne tek kişi.` | `Bu kez has, çünkü özne üçüncü tekil kişi.` | kendi | Yanlış kural: *I* da tek kişidir ama *have* alır. has yalnız üçüncü tekil kişide gelir. |
| 6 | c5 p4 | `Never gibi sözcükler hayatın bugüne kadarki kısmını anlatır.` | `Burada never, hayatın bugüne kadarki kısmını kapsar.` | kendi | Mutlak kural (EK-5b/5c): never genel olarak "hayatın bugüne kadarki kısmını" anlatmaz (*I never eat meat*, *I never saw him again*). "Burada" iddiayı bu cümleye sınırlar. Sahne 05 aynı anda `never · ever · just` etiketleri gösteriyordu; just bugüne kadarki dönemi anlatmaz → tek `never` etiketi kaldı. |

c7 p2 (`Have ya da has şimdiyi taşır, üçüncü hâl işi söyler.`) metni değişmedi; komşu parça değiştiği için el.py önbellek anahtarı yenilendi, yeniden sentezlendi.

Değişen dosyalar (1–6 ortak): `ortak/anlatim/senaryo.json` (parça + `metin`), `METIN.md`, `altyazi.json`, `sureler.json`, `sozcukler.json`,
`sozcuk_uret.py` (BASLAR), `zaman.json`, sahne 04 `sahne.js` + `calistir.sh`, sahne 05 `sahne.js` + `calistir.sh`, sahne 06 `uret.py` +
`zamanlar.json` + `calistir.sh` → `proje/index.html`, `olaylar.json`; `surumler.json`, `youtube.json`, `youtube-aciklama.md`, `BRIEF.md`.

| Alan | Önce | Sonra |
|---|---|---|
| `meta.canAlici[4]` (senaryo, önceki oturum) ve `surumler.json` `canAlici[4]` | `3 örnek, 1 kural: üçünde de have + üçüncü hâl` | `… üçünde de have / has + üçüncü hâl` (c4 has kullanır) |
| `meta.canAlici[2]` `for = süre, since = başlangıç noktası` | doğru | değişmedi |
| `youtube.json`, `youtube-aciklama.md` | aynı iddia yok ("never, ever, just, already gibi sinyal sözcükler") | metin değişmedi; zamanlar §6 |
| Sahne 06 kartları | `geçmişte bitti` / `etkisi şimdiye uzanıyor`; tablo `for · since → süre`, `just · already · yet → yeni biten iş`; kod `geçmiş iş → şimdiki etki` | `geçmiş` / `şimdiye bağlanıyor`; tablo `for · since → süre · başlangıç`, `never · ever → deneyim`, `just · already → az önce · çoktan`; kod `geçmişten → şimdiye` |

### Kendi taramam (dersin öteki cümleleri)

| Cümle | Hüküm | Gerekçe |
|---|---|---|
| c1 `Kaybettim, kapıda kaldım.` | doğru | Kanca; kural kurmaz. |
| c2 `… geçmişte oldu, ama sonucu şimdi bizimle. İngilizce bunun için ayrı bir zaman kullanır.` | doğru, dokunulmadı | Varlık iddiası ("ayrı bir zaman kullanır"), "yalnız" demez; *I lost my key* seçeneği iddiayı yanlışlamaz. YV-DUZ §3 aynı köprüyü kabul etti. |
| c3 `Kırma işi geçmişte oldu, ama ekran şimdi de kırık.` · `Have, artı fiilin üçüncü hâli.` | doğru | Örneğe bağlı yorum; form tam. |
| c4 `For süreyi söyler. Başlangıç olsaydı since derdik.` | doğru | — |
| c6 (öğrenci) `Hocam, üçünde de have var.` | dokunulmadı | Öğrenci sorusu; has, have'in biçimidir. Kural cümlesi değil. |
| c7 p2 `Have ya da has şimdiyi taşır, üçüncü hâl işi söyler.` | doğru | Öğretici benzetme; mutlak kural kurmaz. |
| `meta.canAlici[3]` `never · ever · just · already · yet = Present Perfect sinyalleri` | dokunulmadı | "Sinyal" yumuşak söz (YVJ YV-6 aynı hüküm). Not: ders sesi yet'i hiç söylemez (aşağıda §9). |
| Rozet `YDT · BASIC` | düzeltildi | HV-24; §4. |

## 2. Ses ve süre

1. Önbellek anahtarı ağsız benzetildi (`~/is/duz3-0206T/anahtar.py`): c4'ün 4 parçası `HIZ_EN=0.9` ile önbellekteydi (önceki oturum), c5 ve c7 yoktu.
   Kanal standardı `HIZ_EN` 0,9 (`ses-sunucu.sh` varsayılanı; 02-04 ana ders 47/47 parça) korundu.
2. `el.py` yalnız c4, c5, c7'yi taşıyan geçici senaryoyla koştu: `timeout 1500 bash araclar/ses-sunucu.sh --kok ~/is/duz3-0206T/kok present-perfect-temel`
   → rc 0; 14 / 14 parça kapıdan geçti; kapı önbelleği 3 / 14; 459 karakter (≈ 2,25 TL; c5 + c7).
3. c1, c2, c3, c6 eski `anlatim.wav`'dan örnek-eşit kesildi (`[başlangıç_N, başlangıç_N+1)`, 48 kHz; `~/is/duz3-0206T/kes.py`); c4, c5, c7 = yeni
   `cumle-1/2/3.wav`. `birlestir.py` → `sureler.json` + `sozcuk_uret.py` BASLAR + `zaman.json`; `kur.py` → `anlatim.wav`; `araclar/ses-paketle.py --yaz` → `anlatim.m4a`.
4. Cümle arası 0,55 sn korundu (c4 sonu 52,56 → c5 53,11; c5 sonu 68,23 → c6 68,78; c6 sonu 72,62 → c7 73,17). Kuyruk 1,00 sn.
5. Kanıt: 0–34,71 sn PCM sha256 eski = yeni (`5c488c7b9ad6537a`); c6 eski 67,74–72,13 = yeni 68,78–73,17 (`0737d28f27854b3f`); 52,56–53,11 ve
   97,6–98,53 sn sessiz (en büyük örnek 0). Üreteçler önce eski dosyaları birebir üretti (`sozcuk_uret.py`, `altyazi_uret.py`: `cmp` eşit).
6. `METIN.md` `~/is/duz3-0206T/metin.py` ile `sureler.json`'dan yeniden kuruldu. Yan düzeltme: eski c2 satırı bayattı (biter 18,73, parçalar
   [3,71–8,35] …); ses 18,5'te biter, `sureler.json` 18,57 der. Ses değişmedi, satır kaynağa getirildi.

| Ölçü | Önce | Sonra |
|---|---|---|
| c4 süresi / sözcük | 16,41 sn / 34 | 17,85 sn / 35 |
| c5 süresi / sözcük | 15,52 sn / 29 | 15,12 sn / 28 |
| c7 süresi / sözcük | 21,73 sn / 41 | 24,36 sn / 46 |
| Cümle başları c5 · c6 · c7 | 51,67 · 67,74 · 72,13 | 53,11 · 68,78 · 73,17 |
| Konuşma sonu | 93,86 | 97,53 |
| Ders süresi (`zaman.json` son `t_son`, `anlatim.wav`, `anlatim.m4a`) | 94,86 sn | 98,53 sn |
| `anlatim.wav` sha256 | `15ffac14fd0d` | `d2d68143c965` |
| `anlatim.m4a` sha256 | — (sunucuda yoktu) | `f82b1c906b26` |
| `sozcukler.json` | 173 sözcük | 178 sözcük |
| `altyazi.json` | 23 parça, son t1 93,94 | 24 parça, son t1 97,61 (≤ 98,53) |

Whisper (faster-whisper large-v3-turbo int8, eşik 0,85; `~/is/duz3-0206T/kok/projeler/present-perfect-temel/ortak/anlatim/sentez.wav.rapor.json`):

| Cümle | Dil | Metin | Duyulan (fark) | Benzerlik |
|---|---|---|---|---|
| c4 | tr / en / tr | İkinci örnek. · My brother has played the guitar for five years. · Kardeşim beş yıldır … hâlâ çalıyor. | aynı ("5 yıldır", "hala") | 1,00 · 1,00 · 1,00 |
| c4 | tr | For süreyi söyler. Başlangıç olsaydı since derdik. Bu kez has, çünkü özne üçüncü tekil kişi. | aynı (virgüller) | 1,00 |
| c5 | tr / en / tr | Üçüncü örnek. · I have never flown in a plane. · Hayatımda hiç uçağa binmedim. Bugüne kadar hiç olmadı. | aynı | 1,00 · 1,00 · 1,00 |
| c5 | tr / tr | Burada never, hayatın bugüne kadarki kısmını kapsar. · Yine have, artı flown. | aynı | 1,00 · 1,00 |
| c7 | tr / tr | Çünkü üçünde de geçmiş şimdiye bağlanıyor. · Have ya da has şimdiyi taşır, üçüncü hâl işi söyler. | aynı ("hal") | 1,00 · 1,00 |
| c7 | tr | For süreyi, since başlangıç noktasını söyler. | aynı | 1,00 |
| c7 | tr | Bu zamanda never ve ever deneyimi, just az önce biten işi, already çoktan biten işi anlatır. | aynı | 1,00 |
| c7 | tr | Kod: have artı üçüncü hâl, geçmişten şimdiye köprü. | aynı ("Kod,", "hal") | 1,00 |

En düşük benzerlik: 1,00 (14 / 14 parça, hepsi tohum 0).

## 3. Zaman zinciri

| Dosya | Değişiklik |
|---|---|
| `zaman.json` (iki paket) | 04: kare 521 → 564, t_son 51,12 → 52,56 (içerik 552) · 05: 52,56–68,23, kare 494 → 482 (içerik 470) · 06: 68,23–98,53, kare 860 → 939 (içerik 909) |
| `sozcuk_uret.py` | `BASLAR` c5 53,11 · c6 68,78 · c7 73,17 |
| `sozcukler.json`, `altyazi.json`, `METIN.md` | üreteçlerle yeniden (§2) |
| Sahne 04 `sahne.js` | 27 sabit yeni sözcük zamanlarına (Kardeşim 39,61 · Başladı 42,01 · hâlâ 42,89 · For 44,64 · since 47,92 · has 49,76 · çünkü 50,36 · üçüncü 51,36); KARE 564 |
| Sahne 05 `sahne.js` | 37 sabit (Üçüncü 53,11 · I 54,40 · never 54,88 · Hayatımda 56,81 · Bugüne 58,92 · never 61,84 · bugüne 63,12 · Yine 65,35 · have 65,99 · flown 67,51); TBAS 52,56, KARE 482 |
| Sahne 06 `zamanlar.json` | t_bas 68,23, kare 939; balon c6 +1,04; yeni anahtarlar `gecmis`, `simdiye`, `sure_`, `since`, `baslangic`, `ever`, `deneyim`, `az_once`, `already`, `coktan` |
| `calistir.sh` (04, 05, 06) | kare sayısı ve denetim anları yeni sürede |

## 4. Sahneler (yatay)

| Sahne | Ne değişti | Neden |
|---|---|---|
| 01 giriş | `uret.py` rozet `YDT · TEMEL`, `yardim.py` künye `· YDT TEMEL` → `proje/index.html` (`olaylar.json` aynı çıktı) | HV-24 |
| 02–05 künye | `ortak/kunye.js` `seviye: "YDT TEMEL"` (çalışma anında çizilir) | HV-24 |
| 04 örnek 2 | c4 yeni ses zamanları (§3); yerleşim aynı | c4 yeni metin + süre |
| 05 örnek 3 | c5 yeni ses zamanları; `never · ever · just` etiket dizisi → tek `never` etiketi (ok aynı `now` noktasına) | c5 yeni metin (madde 6) |
| 06 soru + form | notlar `geçmiş` → `şimdiye bağlanıyor`; V3 "üçünde"de; sinyal tablosu parça parça sözcüğünde (`SINYAL_SATIRLARI`); kod kartı `geçmişten → şimdiye`, ok "köprü"de; ok aralıkları açıldı (tablo L + 36, kod kartı + 18 / + 86); `yardim.py` künye `· YDT TEMEL` | c7 yeni metin + HV-24 |
| 90 kapak | `yardim.py` kullanılmayan `ROZET = "YDT · BASIC"` → `YDT · TEMEL` (kapak `uret.py` kendi `YDT · TEMEL` sabitini kullanır; kapak çıktısı değişmez, yeniden üretilmedi) | HV-24 |

HF kaynak üretimi: `uret.py` → `olay.py` → `tema_hf acik` (`~/is/duz3-0206T/hf-uret.sh`; render yok). Taban denetimi: HEAD kaynağı geçici ağaçta
(`~/is/duz3-0206T/taban`) yeniden üretildi; `olaylar.json` 4/4 eşit; `index.html` farkı yalnız önceden var olan sapmalar (01'de `tema-acik`
sınıfı; ana 06'da eski bir genişlik değeri; dikey 06'da 2 karelik altyazı yuvarlaması).

Kareler (kendim baktım; `node araclar/sahne-kare.mjs present-perfect-temel <sahne> <t,…> <dizin> --tema acik --port 41333 --sunucu 41022`,
dizin `sahneler/<sahne>/k/duz3/`, git dışı; koyu: `k/duz3/koyu/`):

| Sahne | Anlar (sn) | Gözlem |
|---|---|---|
| 01 | 1,2 · 2,9 | hap `YDT · TEMEL` + `GRAMMAR`; künye `PRESENT PERFECT · YDT TEMEL` |
| 04 | 36,5 · 41 · 43,3 · 46 · 48,6 · 51,7 · 52,5 | yerleşim eskisiyle aynı; `for → süre` 44,64'te, `since → başlangıç` 47,92'de; `has + played` kartı sağda, takvime değmez |
| 05 | 53,5 · 56,2 · 58,7 · 60,3 · 62,3 · 63,9 · 65,3 · 67,9 | tek `never` etiketi yaşam çizgisinin altında; ok `bugüne kadar hiç` yazısına değmeden `now`a varır; kart `have + flown` |
| 06 | 70,5 · 73,5 · 75,6 · 78,8 · 82 · 83,6 · 87,7 · 91,6 · 94,2 · 96,3 · 97,4 · 98,4 | tablo 3 satır kutu içinde (x 140–1140); `already` ile ok arası açık; kod kartı `geçmişten → şimdiye` kartın içinde; `Next lesson →` ajandanın üstünde |
| 06 koyu, 05 koyu | 98,4 · 63,9 | yeni yazılar koyu zeminde okunur |

## 5. Kapak

Kapak değişmedi. YV-DUZ §4 bu dersin satırında kapak sütunu "—"; §3 "Dokunulmayan kapaklar" `KAYBETTİM = HAVE LOST` için "kapak jürisi
isterse ikinci sıra" der. Kapak yazısı yeni cümlelerle çelişmez (ders c1–c2 aynı köprüyü "sonucu şimdi" şartıyla kurar). Kapak rozeti
`uret.py` içinde zaten `YDT · TEMEL`. Kapak kareleri bu işte yeniden çekilmedi (dosya değişmedi: `kapak.png`, `kapak-koyu.png` 15.11 19:28).

## 6. Yayın verisi zamanı (`youtube.json`, `youtube-aciklama.md`; iki pakette aynı)

| Öğe | Önce | Sonra |
|---|---|---|
| Bölüm 1 Kaybettim | 0,00 (00:00) | 0,00 (00:00) |
| Bölüm 2 Have + üçüncü hâl | 18,73 (00:19) | 18,73 (00:19) |
| Bölüm 3 For ve since | 34,16 (00:34) | 34,16 (00:34) |
| Bölüm 4 Deneyim | 51,12 (00:51) | 52,56 (00:53) |
| Bölüm 5 Neden hep üçüncü hâl? | 67,19 (01:07) | 68,23 (01:08) |
| En kısa bölüm | 15,43 sn | 15,43 sn (son bölüm 30,30 sn) |
| Bildirim | 34,71 sn (%36,6) | 34,71 sn (%35,2); c4 başı, değişmedi; ilk 30 sn dışında, kart 37,71'de biter ≤ son 20 sn sınırı 78,53 |

Damga bloğu `bolumler` ile aynı (yuvarlama `int(t + 0,5)`). Bölüm adları yeni metinle çelişmez.

## 7. Kapılar

```
$ /usr/bin/python3 uretim-hatti/betikler/yv-tutarlilik.py --kilitli simple-present-temel,simple-present-temel-dikey,02-04-ydt-temel-dikey
present-perfect-temel / -dikey: süre 98.53 sn, bölüm 5; sinir, damga, kanal-etiketi, emoji, baslik, liste, etiket-yazim, kopya, dikey → TAMAM
[SORUN] zaman: 22 — hepsi present-perfect-cont-ileri(-dikey), present-perfect-cont-temel(-dikey), present-perfect-ileri(-dikey)
        (bölüm başı sahne başı değil; başka oturumların DUZ3 işi)
→ çıkış 1 (bu derste sorun 0; kilitli pakette 0)

$ node araclar/cakisma-kapisi.mjs present-perfect-temel --sahne <s> --port 41333 --sunucu 41022 --json ~/is/duz3-0206T/kapi-ana-<s>.json
01 çıkış 0 (1 uyarı: t1 × t2, 2,75 sn, başlık uçuşu; önceden var) · 02 çıkış 0 · 03 çıkış 0 · 04 çıkış 0 · 05 çıkış 0 · 06 çıkış 0
```

Dikey çakışma kapısı: 6 / 6 çıkış 0 (ilk koşuda 04 çıkış 1 idi; dikey raporu §4).

## 8. Kısa video (`present-perfect-temel-s1`; yalnız rapor, dokunulmadı)

Bu işte düzeltilen cümlelerin hiçbiri kısada yok (grep: `tek kişi`, `since süre`, `yeni biten`, `geçmişte bitti`, `şimdiki etki`, `Never gibi` → 0).
Aynı taramada görülen başka bulgular:

| Dosya | Bulgu | Ölçüt |
|---|---|---|
| `ortak/anlatim/senaryo.json` (`giris.rozetler`), `ortak/kunye.js`, `sahneler/01-hyperframes-kapak/yardim.py`, `sahneler/03-hyperframes-cta/yardim.py`, iki `proje/index.html` | rozet `YDT · BASIC` | HV-24 |
| `senaryo.json` `meta.canAlici`, `surumler.json` | `Türkçede -dı, İngilizcede have + üçüncü hâl` (birebir denklik; *I lost* de -dı) | EK-5b |
| `senaryo.json` cümle 3 | `Tam ders: Present Perfect. Tam dersi kanalda izle.` ("Tam ders" sözü) | HV-4 |

Ana paketin `uretim-tutanagi/huni-konu.md` dosyası satır 67'de eski cümleyi alıntılar (`Bu kez has, çünkü özne tek kişi.`); tutanaktır, dokunulmadı.

## 9. Düzeltemediklerim / açık kalanlar

| Madde | Sebep |
|---|---|
| EK-11 kulak dinlemesi (c4, c5, c7 yeni ses) | Nadir'in işi; Whisper süzgeçtir |
| mp4'ler bayat | render yasak; `calistir.sh` dosyaları yeni kare sayısında (04 `N=564`, 05 `N=482`, 06 `KARE=939`) |
| Sahne 04 ve 05 `olaylar.json` (ses olayları) bayat | düz canvas sahnelerinde `olaylar.json` yalnız `calistir.sh` → `yakala.py` (tam kare yakalama) ile üretilir; render adımında yenilenir. Sahne 01 ve 06 `olaylar.json` `olay.py` ile güncel |
| Sahne `RAPOR.md` dosyaları (04, 05, 06) eski zamanları anar | sahne üretim tutanağı; render sonrası yenilenir |
| `meta.amaclar[2]` ve `canAlici[3]` yet'i sayar, ders sesi yet'i hiç söylemez | önceden de böyleydi; eski tablo yet'i "yeni biten iş" diye yanlış gösteriyordu, satırdan çıktı. Şef kararı: amaçtan yet çıkar ya da sese bir cümle eklenir |
| Kapak `KAYBETTİM = I HAVE LOST` (-dı ↔ PP köprüsü) | YV-DUZ §3: kapak jürisine bırakıldı; bu işte kapak notu yok |
| Tutarlılık kapısı çıkış 1 | başka 3 ders (6 paket), bu derste 0 |
| Kısa video bulguları (§8) | yazma alanı dışında |
| `.claude/docs/sozlesme.md`, Kovan | istem yazmayı iki paketle sınırladı |

Eski ses ve önceki oturum yedeği: `~/Silinecekler/2026-11-16-duz3-0206T/anlatim-eski-1511.wav`, `…/is-duz3-onceki-oturum/` (paketteki `_is/duz3`
buradan taşındı; boş `_is/` dizini git dışı kaldı). Yardımcı betikler ve geçici çıktılar: `~/is/duz3-0206T/`.

---
Son Güncelleme: 16.11.2026 (DUZ3-0206T oturumu).
