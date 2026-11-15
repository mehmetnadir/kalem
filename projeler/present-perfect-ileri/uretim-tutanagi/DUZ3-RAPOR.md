# DUZ3-0206I — `present-perfect-ileri` dersin kendi içerik düzeltmeleri (jüri c sınıfı) · 16.11.2026

> Girdi: `uretim-hatti/raporlar/YV-DUZ-1511.md` §4 (bu dersin 2 satırı) ve §3 (kapak "ses düzelince"), `uretim-tutanagi/juri/YVJ-hukum.md`
> (YV-6 ve ek bulgu 1–2). Makine srv21 (Linux x86_64). Render yok, mp4 yok, alt ajan yok, commit yok. Silinen dosya yok: eski ses ve kapaklar
> `~/Silinecekler/2026-11-16-duz3-0206I/` altında. Dikey paketin raporu: `../../present-perfect-ileri-dikey/uretim-tutanagi/DUZ3-RAPOR.md`.
> Önceki oturum (bellek arızası): pakette yarım değişiklik yoktu (git temiz, rapor yok); yalnız `Silinecekler/…/ozgun.tar` yedeği vardı.
> Sunucu ses önbelleğinde bu dersin sesi yoktu (ses Mac'te üretilmiş). İş baştan yapıldı.

| Ölçü | Değer |
|---|---|
| Düzeltilen cümle | 5 parça / 4 cümle: jüri 3 (c1, c3 p4, c7 p1) + kendi bulgum 2 (c6, c7 p4) |
| Yeniden sentezlenen cümle | 4 (c1, c3, c6, c7; 10 parça, 576 karakter ≈ 2,82 TL) |
| Whisper en düşük | 0,98 (c7 "Finished time: simple past. …"); 10 / 10 parça ≥ 0,85 |
| Ders süresi | 93,77 → 98,29 sn |
| Yeniden üretilen sahne | yatay 5 (01, 02, 03, 06, kapak) + 2 kayma (04, 05) · dikey 5 + 2 kayma |
| Kapak | değişti: `AGO VARSA / PERFECT YOK` → `AGO VARSA / SIMPLE PAST` (4 PNG + 168 px) |
| Tutarlılık kapısı | çıkış 1; bu derste 0 sorun (22 sorun başka derslerde) |
| Çakışma kapısı (yatay) | 01–05 çıkış 0 · 06 çıkış 1 (yalnız bilinçli çarpı çiftleri) |
| Çakışma kapısı (dikey) | 01–04 çıkış 0 · 05 çıkış 1 (eski yerleşim, içerik değişmedi) · 06 çıkış 1 (bilinçli çarpı; `bas × hay` düzeltildi) — dikey rapor §4 |

## 1. Cümle tablosu

| # | Cümle | Önce | Sonra | Gerekçe |
|---|---|---|---|---|
| 1 | c1 (jüri) | `Ago varsa Present Perfect yok.` | `Ago varsa, fiil Simple Past.` | Mutlak; dersin c5 örneği (`took off two hours ago, but it hasn't landed yet`) aynı cümlede ago + Present Perfect taşır. YV-DUZ önerisi `Ago varsa Simple Past.` iddiayı yine bütün cümleye yayar; `fiil` sözcüğü iddiayı ago'nun bağlı olduğu fiile daraltır (EK-5b kapsam sınırı). Kapak `AGO VARSA / SIMPLE PAST` aynı iddianın kısaltmasıdır. |
| 2 | c3 parça 4 (jüri) | `Since cümleciği Simple Past alır, ana cümle Present Perfect.` | `Since cümleciği çoğu zaman Simple Past alır, ana cümle burada Present Perfect.` | Since cümleciği süren durumda Present Perfect alır (*since I've lived here*). YV-DUZ önerisinin ikinci yarısı da mutlaktı: ana cümle her zaman Present Perfect değildir (*It's two years since we met*; Present Perfect Continuous). `burada` ikinci yarıyı bu köke bağlar. |
| 3 | c6 (kendi bulgum) | `Hocam, ago varken de has landed diyemez miyiz?` | `Hocam, took off yerine has taken off diyemez miyiz?` | c7 `Hayır.` ile cevaplanır. c5 aynı cümlede ago ve `hasn't landed` kullandığı için `Hayır` dersin kendi örneğini yanlış sayıyordu (EK-5b: "hayır" kaldı sayımına girer; YV-DUZ gönderideki aynı soruyu bu gerekçeyle kaldırdı). Yeni soru ago'nun bağlı fiilini sorar: *The plane has taken off two hours ago* gerçekten yanlıştır, `Hayır` ve kırmızı çarpı doğru olur (EK-5a). EK-9: 8 sözcük. |
| 4 | c7 parça 1 (jüri) | `Hayır. Bitmiş zaman bildiren sözcükler Present Perfect'i yasaklar:` | `Hayır. Bitmiş zaman bildiren sözcükler, bağlandıkları fiili Simple Past'a çeker:` | `yasaklar` cümle düzeyinde mutlaktır. YV-DUZ önerisi `aynı yan cümlede … dışlar`: c5'te ago yan cümlede değil, `but` ile bağlı ana cümlededir; `dışlar` istisnasız kural kalır (EK-5c). `bağlandıkları fiil` kapsamı doğru yere koyar; `çeker` eğilim bildirir (*I was sleeping yesterday* da doğrudur). |
| 5 | c7 parça 4 (kendi bulgum) | `Kodu aklında tut: ago varsa Simple Past, yet varsa Present Perfect.` | `Kodu aklında tut: ago'nun fiili Simple Past, yet'in fiili çoğu zaman Present Perfect.` | Cümle düzeyinde okununca c5'te (ago ve yet aynı cümlede) iki kural çatışır. `yet varsa Present Perfect` istisnasızdır: *I don't know yet*, *Is it ready yet?*, Amerikan İngilizcesinde *Did you eat yet?* |

Aynı ifadeyi taşıyan öteki yerler:

| Alan | Önce | Sonra |
|---|---|---|
| `senaryo.json` `kartlar.kanca.tr` | `Ago gördün mü, Present Perfect elenir.` | `Ago gördün mü, o fiil Simple Past.` |
| `senaryo.json` `meta.kapak.canAlici` | `ago gördün mü Present Perfect elenir` | `ago gördün mü, o fiil Simple Past` |
| `senaryo.json` `meta.kapak.kucuk` | (yok) | `ago → took off` (kapak §3 isteğe bağlı alan; kapak küçük satırı) |
| `meta.canAlici[0]` (senaryo + `surumler.json`) | `Ago varsa Simple Past, yet varsa Present Perfect` | `ago'nun fiili Simple Past, yet'in fiili çoğu zaman Present Perfect` |
| `meta.canAlici[2]` (senaryo + `surumler.json`) | `since cümleciği Simple Past, ana cümle Present Perfect` | `since cümleciği çoğu zaman Simple Past; bu kökte ana cümle Present Perfect` |
| Ekran metinleri | sahne 01–02 c1, sahne 03 formül kutusu, sahne 06 balon, `Present Perfect` üstü çizili + `yasak`, ⃠ işaretleri, kod kartı | §4 |
| `youtube.json`, `youtube-aciklama.md` | aynı iddia yok (`grep` 0); açıklama satır 1 YV-DUZ'un düzeltilmiş metni | yalnız zamanlar (§6) |
| `BRIEF.md` | c1, c6, rozet, ⃠ satırları | düzeltildi; başa DUZ3 notu (zamanların güncel kaynağı METIN.md / zaman.json) |

### Kendi taramam (dokunulmayan cümleler)

| Cümle | Hüküm | Gerekçe |
|---|---|---|
| c2 formül ve plan cümleleri | doğru | `subject plus have or has plus past participle` tam formül. |
| c4 `For süreyi söyler: otuz yıl. Yıl adı verseydin since gelirdi.` | doğru | Yıl (başlangıç noktası) ile bu Present Perfect cümlesinde since gelir. Türkçe çeviri `çalışıyor` doğal çeviridir, denklik iddiası değil. |
| c5 `Ago var, zaman bitmiş: Simple Past. Yet var, etki sürüyor: Present Perfect.` | doğru, dokunulmadı | Örnek cümlenin iki yanına bağlı açıklama; genel kural cümlesi değil. Sahne 05 kartları (`ago → Simple Past`, `yet → Present Perfect`) da örneğe bağlı. |
| c7 parça 2–3 `ago, yesterday, last year.` · `Finished time: simple past. Unfinished time: present perfect.` | dokunulmadı | Yaygın ders kalıbı; jüri "hayır" demedi. Not: bitmemiş zamanda Simple Past da olur (*I went to the gym this week*); kalıp sıkı okunursa EK-5c'ye takılabilir → şef kararı (§9). |
| `meta.amaclar`, `canAlici[1]`, `[3]`, `[4]` | doğru | `for = süre, since = başlangıç noktası` doğru; `[4]` c7 parça 3'ün Türkçesi (yukarıdaki not). |
| Rozet `YDT · ADVANCED` (senaryo, künye, sahne 01, 06), kapak `yardim.py` `YDT · BASIC` | düzeltildi | HV-24 → `YDT · İLERİ` (§4). |

## 2. Ses ve süre

Yöntem (öteki cümlelerin sesi değişmez):
1. Önbellek anahtarı ağsız benzetildi (`~/is/duz3-0206I/anahtar.py`): 7 cümlenin hiçbir parçası sunucu önbelleğinde yoktu.
2. Geçici senaryo yalnız c1, c3, c6, c7'yi taşıdı (`~/is/duz3-0206I/kok/…/senaryo.json`); `timeout 1500 bash araclar/ses-sunucu.sh --kok
   ~/is/duz3-0206I/kok present-perfect-ileri` → rc 0, 10 / 10 parça kapıdan geçti, 576 karakter (≈ 2,82 TL), `HIZ_EN` 0,9 (varsayılan).
   Hız denetimi: c3 EN parçası özgün 4,56 sn, yeni 4,72 sn (0,8 hızı daha uzun verirdi; özgün ses 0,9 ile tutarlı).
3. c2, c4, c5 eski `anlatim.wav`'dan örnek-eşit kesildi (`[başlangıç_N, başlangıç_N+1)`, 48 kHz; `~/is/duz3-0206I/kes.py`); c1, c3, c6, c7 =
   yeni `cumle-*.wav`. `kur.py` → `anlatim.wav`; `araclar/ses-paketle.py --yaz --paket present-perfect-ileri` → `anlatim.m4a` (+ `.imza`).
4. Kayma 0,1 sn (3 kare) ızgarasına yukarı yuvarlandı (dosya sonundan 0,55 sn cümle arası korunur): c1 +0,40 → c2–c7 +0,4;
   c3 +1,12 → c4–c7 +1,2; c6 +0,16 → c7 +0,2.
5. Kanıt: eski 4,03–18,52 = yeni 4,43–18,92 (PCM sha256 `5c7f6f6a0fefcc70`); eski 34,44–69,15 = yeni 36,04–70,75 (`b6e9b0d1f42dad56`);
   0–1,00 sn sessiz (en büyük örnek 0). Üreteçler önce eski dosyaları yeniden üretti: `sozcuk_uret.py` ve `altyazi_uret.py` `cmp` eşit;
   `metin.py` yalnız METIN.md c2 parça 1 sonunda ayrıştı (eski 9,71; `sureler.json` 5,52 → 9,55: eski kayıt hatası, yeni METIN `sureler`'le eşit).

| Ölçü | Önce | Sonra |
|---|---|---|
| c1 süresi | 2,48 sn | 2,88 sn |
| c3 süresi / sözcük | 15,37 sn / 33 | 16,49 sn / 35 |
| c6 süresi / sözcük | 3,92 sn / 8 | 4,08 sn / 9 |
| c7 süresi / sözcük | 19,15 sn / 31 | 21,87 sn / 35 |
| Cümle başları c1–c7 | 1,00 · 4,03 · 18,52 · 34,44 · 51,80 · 69,15 · 73,62 | 1,00 · 4,43 · 18,92 · 36,04 · 53,40 · 70,75 · 75,42 |
| Konuşma sonu (c7 bitişi) | 92,77 | 97,29 |
| Ders süresi (`zaman.json` son `t_son`, `anlatim.wav`, `anlatim.m4a`) | 93,77 sn | 98,29 sn |
| `anlatim.wav` sha256 | `6be49b46580c` | `ba129d0ebc5b` |
| `anlatim.m4a` sha256 | — (sunucuda yoktu) | `7846899d7e8a` |
| `sozcukler.json` | 178 sözcük | 186 sözcük |
| `altyazi.json` | 22 parça, son t1 92,85 | 22 parça, son t1 97,37 (≤ 98,29) |

Whisper (faster-whisper large-v3-turbo int8, eşik 0,85; `~/is/duz3-0206I/kok/projeler/present-perfect-ileri/ortak/anlatim/sentez.wav.rapor.json`):

| Cümle | Dil | Metin | Duyulan | Benzerlik |
|---|---|---|---|---|
| c1 | tr | Ago varsa, fiil Simple Past. | Ago varsa, fiil Simple Past. | 1,00 |
| c3 | tr | Birinci kök. | Birinci Kök | 1,00 |
| c3 | en | Ever since the company launched its new app, the number of users has doubled. | (aynı) | 1,00 |
| c3 | tr | Şirket yeni uygulamasını çıkardığından beri kullanıcı sayısı ikiye katlandı. | (aynı) | 1,00 |
| c3 | tr | Since cümleciği çoğu zaman Simple Past alır, ana cümle burada Present Perfect. | Since cümleciyi çoğu zaman simple past alır, … | 0,99 |
| c6 | tr | Hocam, took off yerine has taken off diyemez miyiz? | (aynı) | 1,00 |
| c7 | tr | Hayır. Bitmiş zaman bildiren sözcükler, bağlandıkları fiili Simple Past'a çeker: | … fiili simple pasta çeker. | 1,00 |
| c7 | en | ago, yesterday, last year. | (aynı) | 1,00 |
| c7 | en | Finished time: simple past. Unfinished time: present perfect. | Finish time. Simple past. Unfinished time. Present perfect. | **0,98** (en düşük) |
| c7 | tr | Kodu aklında tut: ago'nun fiili Simple Past, yet'in fiili çoğu zaman Present Perfect. | (aynı; noktalama farkı) | 1,00 |

## 3. Zaman zinciri

| Dosya | Değişiklik |
|---|---|
| `zaman.json` (iki paket) | 02: kare 461 → 473, 3,00–18,37 · 03: kare 490 → 526, 18,37–35,49 · 04: 35,49–52,85 · 05: 52,85–70,20 · 06: kare 785 → 873, 70,20–98,29 (içerik 843) |
| `sureler.json` | c1, c3, c6, c7 yeni sentezden; c2, c4, c5 aynı |
| `sozcuk_uret.py` | `BASLAR` yeni başlar |
| `sozcukler.json`, `altyazi.json`, `METIN.md` | üreteçlerle yeniden (`sozcuk_uret.py`, `araclar/altyazi_uret.py`, `~/is/duz3-0206I/metin.py`) |
| Sahne `calistir.sh` | 02 `N=473` · 03 `N=526`, `TBAS=18.37` · 04 `TBAS=35.49` · 05 `TBAS=52.85` (yeni küresel anlar, yerel kareler aynı) · 06 `KARE=873`, `TBAS=70.20`, yeni denetim anları |
| Sahne 06 `zamanlar.json` | t_bas 70,2, kare 873, süre 29,1 |
| `olaylar.json` (02–05) | dokunulmadı: Paper.js / canvas ses olayları yakalama (render) sırasında yeniden yazılır; render bu işte yasak |

## 4. Sahneler (yatay)

| Sahne | Ne değişti | Neden |
|---|---|---|
| 01 giriş | `uret.py` rozet `YDT · İLERİ`, `yardim.py` künye `· YDT İLERİ`; c1 sözcükleri `sozcukler.json`'dan → `proje/index.html` | HV-24, c1 |
| 02 kanca | c1 sözcük dizisi `Ago varsa, fiil Simple Past.` (`Ago` kırmızı çizgi korunur); c2 zaman değişmezleri +0,40 (bağlamlı: `FR(…)`, liste, `koy`); `KARE` 473; yorum saniyeleri | c1 metni, c1 +0,4 sn |
| 02–05 künye | `ortak/kunye.js` `seviye: "YDT İLERİ"` | HV-24 |
| 03 kök 1 | bütün sabit saniyeler sözcük çapalı eşlemeyle yeni sese (`~/is/duz3-0206I/esle.py`: eski ve yeni `sozcukler.json` difflib hizası, çapalar arası doğrusal); `KARE` 526, `T_BAS` 18,37; kutu 1'e soluk el yazısı `çoğu zaman` (Caveat 44, x 420–592, "Past" 32,45 ile) | c3 yeni ses + EK-5b kapsamı ekranda |
| 04 kök 2 | `kayma: -1.6` (sahne eski çerçevede, TBAS 33,89; yerel kareler aynı) | c1 + c3 kayması |
| 05 kök 3 | `kayma: -1.6` (TBAS 51,25) | aynı |
| 06 soru + kural | balon satırları `Hocam, took off yerine` / `has taken off diyemez miyiz?`; sarı belirteç `took off` altında; kırmızı çarpı `has taken off` üstünde (`has` anında); A2 satırı `fiil → Simple Past` (eski `Present Perfect` üstü çizili + `yasak` kalktı); B kutusu ⃠ işaretleri kalktı, kutu 700 → 460 px; kod kartı `ago → Simple Past` / `yet → Present Perfect` + soluk `çoğu zaman` (Caveat 44); bütün sabit saniyeler sözcüğe bağlandı (`I(c, sözcük)`, iskelet çizimleri `c6 başı + sn`); kullanılmayan `yasak()` işlevi kaldırıldı; künye `· YDT İLERİ` | c6, c7 yeni metin + HV-24 |
| 90 kapak | §5 | YV-DUZ §4 kapak notu |

HF kaynak üretimi: `uret.py` → `olay.py` → `tema_hf acik` (`~/is/duz3-0206I/hf-uret.sh`; render yok). Kökte `tema-acik` sınıfı var
(önceki işlenmiş dosya koyu temadaydı; editör temayı mesajla değiştirir).

Kareler (kendim baktım; `node araclar/sahne-kare.mjs present-perfect-ileri <sahne> <t,…> <dizin> --tema acik --port 41333 --sunucu 41022`,
dizin `sahneler/<sahne>/k/duz3/`, koyu örnekler `k/duz3/koyu/`, git dışı):

| Sahne | Anlar (sn) | Gözlem |
|---|---|---|
| 01 | 1,2 · 2,2 · 2,9 | hap `YDT · İLERİ` + `GRAMMAR`; c1 sözcük sözcük, 2,9'da uçuşta; künye `· YDT İLERİ` |
| 02 | 3,4 · 5,3 · 9,0 · 15,2 · 17,9 | c1 tam ve `Ago` çizgili; sol kutu 4,43'te, `formula` 5,11; `1.5 min` (98 sn); `V3 = past participle` 14,85'te yazılıyor |
| 03 | 21,3 · 24,3 · 29,5 · 32,3 · 33,6 · 35,4 | `launched` 21,25'te çiziliyor (ses ile eş); `+ Simple Past` 32,05; `çoğu zaman` kutu 1 içinde, `launched` dairesine değmez; `Present Perfect` 34,53; koyu 35,4 okunur |
| 04 | 36,3 · 39,6 | 36,3'te "2" dairesi (c4 36,04); 39,6'da `for thirty years` dairesi |
| 05 | 54,0 · 66,4 | 54,0'da "3" dairesi (c5 53,40); 66,4'te `ago → Simple Past` kartı, zaman çizgisi |
| 06 | 72,3 · 73,9 · 76,9 · 80,6 · 82,4 · 86,6 · 89,3 · 94,0 · 97,4 (+ koyu 97,4) | balon iki satır, B kutusuna değmez; çarpı `has taken off` üstünde; `Hayır. Bitmiş zaman` 76,9; `fiil → Simple Past` 80,6; ⃠ yok; kod kartı 97,4'te iki satır + `çoğu zaman` + tik + `Next lesson` |

## 5. Kapak

| Öğe | Önce | Sonra |
|---|---|---|
| Ana yazı | `AGO VARSA` / `PERFECT YOK` | `AGO VARSA` / `SIMPLE PAST` (YV-DUZ §4, `meta.kapak`) |
| Küçük satır | `ago → Simple Past` | `ago → took off` |
| Rozet | `YDT · İLERİ` (üretici sabiti) | aynı; kullanılmayan `yardim.py` `ROZET = "YDT · BASIC"` → `YDT · İLERİ` |
| Karakter, nesne, yerleşim | — | değişmedi (`ortak/kapak/` aynı dosyalar) |

1. Ana yazı dersin yeni c1'iyle aynı iddiadır (4 sözcük, KS-4).
2. Küçük satır eskisiyle kalsaydı vurgu kutusunu yinelerdi (`SIMPLE PAST` iki kez). Kapak standardı §2 küçük satırı "EN örnek" sayar;
   `ago → took off` dersin kanca örneğidir (`The plane took off two hours ago.`) ve iddiayı somutlar.
3. Üretici: `sahneler/90-hyperframes-kapak/uret.py` yalnız `SATIR2`, `KUCUK_SAG`; assert'ler dört düzende geçti. Eski 4 PNG ve 168 px
   `~/Silinecekler/2026-11-16-duz3-0206I/` altında (betik eski kapağı paylaşılan `…-kapak` klasörüne taşımadan önce ben taşıdım).
4. Kareye baktım: 4 kare + 168 px (açık ve koyu). Taşma yok; vurgu kutusu yatayda x ≈ 1055'te biter, karakter ≈ 1140'ta başlar; sağ alt boş;
   dikeyde kutu sağ kenar payı içinde; 168 px'te `AGO VARSA SIMPLE PAST` okunur.

| Dosya | sha256 (ilk 12) |
|---|---|
| `kapak.png` (1920×1080, açık) | `c92a956b9922` (eski `bbf7ca0bf128`) |
| `kapak-koyu.png` | `ca43825bc62e` |
| `../present-perfect-ileri-dikey/kapak.png` (1080×1920) | `b3e07bfd7c07` |
| `../present-perfect-ileri-dikey/kapak-koyu.png` | `a174264adf6e` |
| `uretim-tutanagi/kapak-168.png` (168×94) | `68af852fb98c`; koyu kopya `sahneler/90-hyperframes-kapak/k/koyu/kapak-koyu-168.png` |

## 6. Yayın verisi zamanı (`youtube.json`, `youtube-aciklama.md`; iki pakette aynı, dikey yalnız `utm_content` farkı)

| Öğe | Önce | Sonra |
|---|---|---|
| Bölüm 1 Formül | 0 (00:00) | 0 (00:00) |
| Bölüm 2 Ever since | 17,97 (00:18) | 18,37 (00:18) |
| Bölüm 3 for ve since | 33,89 (00:34) | 35,49 (00:35) |
| Bölüm 4 Tuzak | 51,25 (00:51) | 52,85 (00:53) |
| Bölüm 5 Bitmiş zaman | 68,6 (01:09) | 70,2 (01:10) |
| En kısa bölüm | 15,92 sn | 17,12 sn (son bölüm 28,09 sn) |
| Bildirim | 34,44 sn (c4 başı, %36,7) | 36,04 sn (c4 başı, %36,7); %30 = 29,49 ilk 30 sn içinde → 30 sn sonrası ilk cümle başı; önceki cümle 35,41'de biter; son 20 sn sınırı 78,29 |

Damga bloğu `bolumler` ile aynı (yuvarlama `int(t + 0,5)`). Bölümler sahne başındadır (`zaman.json` 01 dahil değil: giriş kancaya birleşik).

## 7. Kapılar

```
$ /usr/bin/python3 uretim-hatti/betikler/yv-tutarlilik.py --kilitli simple-present-temel,simple-present-temel-dikey,02-04-ydt-temel-dikey
present-perfect-ileri / -dikey: başlık 56 kr · açıklama 696 B · etiket 166 · bölüm 5 · süre 98.29 sn
[SORUN] zaman: 22 — hepsi present-perfect-cont-ileri{,-dikey}, present-perfect-cont-temel{,-dikey}, simple-past-temel{,-dikey}
  (bölüm başı zaman.json sahne başı değil; başka oturumların DUZ3 işi sürüyor)
sinir, damga, kanal-etiketi, emoji, baslik, liste, etiket-yazim, kopya, dikey → TAMAM
toplam sorun: 22 · kilitli pakette: 0 → çıkış 1 (bu derste 0)
```

Çakışma kapısı (yatay; sahne sahne, `--port 41333 --sunucu 41022`, kayıt `~/is/duz3-0206I/kapi-present-perfect-ileri-<sahne>.{json,log}`):

```
$ node araclar/cakisma-kapisi.mjs present-perfect-ileri --sahne <sahne> --port 41333 --sunucu 41022 --json …
01-hyperframes-giris  rc 0 — t1 × t2 (başlık satırları, 2,75 sn, 10×7 px) uyarı (eski; kalem dokunmadı)
02-paperjs-kanca      rc 0 — çakışma yok (63 örnek, 1753 kutu)
03-paperjs-ornek1     rc 0 — çakışma yok (70 örnek, 5499 kutu)
04-canvas-ornek2      rc 0 — çakışma yok (71 örnek, 1471 kutu)
05-canvas-ornek3      rc 0 — TR çeviri × `now` uyarı (62,10–70,20; sahne içeriği değişmedi, kayma yerel kareyi korur)
06-hyperframes-form   rc 1 — bw4/bw5/bw6 × xk1/xk2 (yanlış cümle `has taken off` × kırmızı çarpı) 6 hata; başka çift yok
```

06'daki hata çiftlerinin hepsi bilinçli çarpı ile çarpılan sözcük arasındadır (eski sürümde `has landed` × çarpı aynı sınıftı).
Yeni öğelerde (`af`, `afo`, `asp`, `k2c`, daralan `bk`, balonun 5 sözcüklü 2. satırı) hata 0.

## 8. Kısa video (`present-perfect-ileri-s1`; yalnız rapor, dokunulmadı)

| Dosya | Aynı sınıf ifade |
|---|---|
| `ortak/anlatim/senaryo.json` (c1 ses), `altyazi.json`, `METIN.md`, `sureler.json`, `uretim-tutanagi/art.json` | `Ago gördün mü, Present Perfect elenir.` (cümle düzeyinde mutlak; ana dersin c1 / kanca kartıyla aynı hata) |
| `sahneler/02-paperjs-ornek/sahne-02.js` (ekran) | `elenir.` el yazısı; `sahneler/01-hyperframes-kapak/uret.py` satır 2 `Present Perfect` |
| `senaryo.json` `kartlar`, `meta.kapak.canAlici`; `BRIEF-S1.md`; `RAPOR.md` | `ago gördün mü Present Perfect elenir` |
| `senaryo.json` `giris.rozetler`, `sahneler/01-hyperframes-kapak/yardim.py`, `sahneler/03-hyperframes-cta/yardim.py` | rozet `YDT · ADVANCED` (HV-24) |
| `surumler.json`, `senaryo.json` `meta.canAlici` | `Ago varsa Simple Past` (ana dersin eski canAlici biçimi; kapsam sözcüğü yok) |

Ana paketin `uretim-tutanagi/huni-konu.{json,md}` dosyası eski ifadeleri taşır ("AGO VARSA PERFECT YOK", "Since cümleciği Simple Past alır",
"ago varken de has landed"); tutanaktır, dokunulmadı. Sahne `RAPOR.md` dosyaları (01, 03, 06) eski üretim tutanağıdır, dokunulmadı.

## 9. Düzeltemediklerim / açık kalanlar

| Madde | Sebep |
|---|---|
| EK-11 kulak dinlemesi (c1, c3, c6, c7 yeni ses; `took off` / `has taken off` Türkçe parçada) | Nadir'in işi; Whisper süzgeçtir |
| YVJ ve kapak jürisi yeniden | içerik ve kapak değişti (`juri-olcutleri.md` §1b); jüri bu oturumun işi değil |
| `Finished time: simple past. Unfinished time: present perfect.` (c7 parça 3, `canAlici[4]`) | jüri hayır demedi; sıkı okunursa EK-5c'ye takılabilir; değişirse c7 EN parçası yeniden sentezlenir → şef kararı |
| Açıklama satır 1 `… Simple Past istediğini` | YV-DUZ / jüri metni; ders artık `çeker` der (daha yumuşak). Çelişki yok; uyum istenirse `çektiğini` |
| mp4'ler ve `olaylar.json` (02–05) bayat | render yasak; `calistir.sh` dosyaları güncel kare sayısında |
| Çakışma kapısı 06 çıkış 1, tutarlılık kapısı çıkış 1 | bilinçli çarpı (§7) · başka dersler |
| Yazım boyutu kapısı | engel çıkmadı |
| `.claude/docs/sozlesme.md`, Kovan | istem yazmayı iki paketle sınırladı |

---
Son Güncelleme: 16.11.2026 (DUZ3-0206I oturumu).
