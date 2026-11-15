# DUZ3-0209I — `present-perfect-cont-ileri` dersin kendi içerik düzeltmeleri (jüri c sınıfı) · 16.11.2026

> Girdi: `uretim-hatti/raporlar/YV-DUZ-1511.md` §4 (bu dersin satırı; kapak sütunu "—"), §3 "Dokunulmayan kapaklar" (bu ders yok),
> `uretim-tutanagi/juri/YVJ-hukum.md` "Kapsam dışı gözlem" (c3, c5, c7). Makine srv21 (Linux x86_64). Render yok, mp4 yok, alt ajan yok.
> Silinen dosya yok: eski ses `~/Silinecekler/2026-11-16-duz3-0209I/present-perfect-cont-ileri/anlatim-eski-0209I.wav`
> (`~/Silinecekler/LISTE.md` satırı yazıldı). Dikey paketin raporu: `../present-perfect-cont-ileri-dikey/uretim-tutanagi/DUZ3-RAPOR.md`.
> Önceki oturum bellek arızasıyla kesildi: yalnız `senaryo.json` metni yazılmıştı (c3, c5, c7, meta, rozet); sentez, zaman, sahne, rapor yoktu.
> Bu oturum metni denetledi, c7 son parçasını ve 1 meta satırını değiştirdi, gerisini yaptı.

## 1. Cümle tablosu

| # | Cümle | Önce | Sonra | Gerekçe |
|---|---|---|---|---|
| 1 | c3 parça 5 (jüri) | `Ana cümlede have been ve -ing gelir.` | `Burada iş hâlâ sürüyor: ana cümlede have been ve -ing.` | since + geçmiş yan cümle için mutlak okunur; dersin 3. örneği (*have known … since*) çürütür. YV-DUZ önerisi "Burada ana cümlede …" yönünde; "iş hâlâ sürüyor" Continuous'ı seçtiren koşulu söyler (önceki oturumun metni, denetlendi, korundu). |
| 2 | c5 parça 5 (jüri) | `Durum fiili -ing almaz.` | `Durum anlatan fiiller genellikle -ing almaz.` | Mutlak. Durum fiili eylem anlamında -ing alır (*I have been thinking about it*). YV-DUZ önerisi "Durum anlamındaki fiil -ing almaz" hâlâ "almaz" der; "genellikle" kural cümlesini yumuşatır, istisnayı açık bırakır (önceki oturumun metni, korundu). |
| 3 | c7 parça 1 (jüri) | `Olmaz. Durum fiilleri -ing almaz.` | `Olmaz. Bu fiil bir durum anlatır, süreç değil.` | Aynı mutlak kural. "Olmaz" bu cümle için doğrudur (*have been knowing* standart İngilizcede yok); gerekçe artık tek fiile (know) bağlı (önceki oturumun metni, korundu). |
| 4 | c7 parça 4 (kendi taramam) | `Türkçede -yor süreci, -di sonucu söyler.` | `İkinci örnekte okuyorum süreci, bitirdim sonucu söyler.` | Birebir Türkçe–İngilizce denklik: *biliyorum* -yor alır ama *I know*; -di İngilizcede çoğu zaman Simple Past'tır, Present Perfect değil. Yeni cümle dersin 2. örneğine bağlı (önceki oturum yazmıştı, korundu). |
| 5 | c7 parça 5 (kendi taramam) | `Aklında kalsın: süreç varsa been var, sonuç varsa been yok.` | `Aklında kalsın: süreç için been ve -ing, sonuç ve durum için have ve üçüncü hâl.` | Mutlak "X varsa Y" kalıbı. Önceki oturum "bitmiş sonuç için have ve üçüncü hâl" yazmıştı; öğrenci sorusundan hemen sonra örnek 3 (*have known*: bitmiş sonuç değil, süren durum) özetin dışında kalıyordu. Bu oturum "sonuç ve durum" yaptı: özet üç örneği de kapsar. |

Değişen dosyalar (1–5 ortak): `ortak/anlatim/senaryo.json` (parça + `metin`), `METIN.md`, `altyazi.json`, `sureler.json`, `sozcukler.json`,
`sozcuk_uret.py` (cümle başları), sahne 03 (`sahne-03.js`), 05 (`sahne.js`), 06 (`uret.py` → `proje/index.html`, `olaylar.json`),
`surumler.json` (`amaclar[3]`, `canAlici`, revizyon), `BRIEF.md`.

| Alan | Önce | Sonra |
|---|---|---|
| `meta.canAlici[0]` (senaryo + `surumler.json`) | `Süreç varsa been var, sonuç varsa been yok` | `Süreç için been + -ing; sonuç ve durum için have + V3` |
| `meta.canAlici[1]` | `Since + geçmiş zamanlı yan cümle -> ana cümle have been -ing` | `Since + geçmiş zamanlı yan cümle -> ana cümle çoğu zaman Present Perfect; iş hâlâ sürüyorsa have been -ing` |
| `meta.canAlici[3]` | `know, like, belong: durum fiili, have been knowing olmaz` | `know, like, belong çoğu zaman durum anlatır: have been knowing olmaz` (bu oturum; *like* eylem anlamında -ing alabilir) |
| `meta.canAlici[4]` | `Türkçede -yor süreci, -di sonucu söyler` | `İkinci örnekte okuyorum süreci, bitirdim sonucu söyler` |
| `meta.amaclar[3]` | `durum fiillerinin -ing almadığını bilmek` | `durum anlatan fiillerin genellikle -ing almadığını bilmek` |
| `meta.kapak.canAlici` | `been varsa süreç var, been yoksa sonuç var` | `been + -ing süreci, have + V3 bitmiş sonucu anlatır` (kapak görseli değişmedi, §5) |
| `giris.rozetler[0]` | `YDT · ADVANCED` | `YDT · İLERİ` (HV-24) |
| `youtube.json`, `youtube-aciklama.md` | aynı iddia yok (grep 0; gönderi, bölüm adları, açıklama jüride "doğru") | metin değişmedi; zamanlar §6 |

### Kendi taramam (dersin öteki cümleleri)

| Cümle | Hüküm | Gerekçe |
|---|---|---|
| c1 `Süreç mi, sonuç mu?` | doğru | Soru; iddia yok. |
| c2 `Have or has, plus been, plus the -ing form.` · `… iki tuzağı görüyoruz.` | doğru | Tam form; kural iddiası yok. |
| c3 `Since, plus a simple past clause.` | doğru | Örneğin yapısını anlatır, genel kural kurmaz. |
| c4 `Süreç, been reading. Sonuç ve sayı, have finished.` | doğru | Sayı/miktar → Present Perfect (yerleşik ölçüt; jüri gönderide aynı iddiayı "doğru" saydı). |
| c5 `Know is a state verb.` | doğru | *know* sınıflaması; -ing hakkında iddia yok. |
| c6 öğrenci sorusu | doğru | Soru. |
| c7 `Process: …` · `Result: …` | doğru | Form tanımı. |
| Ekran: sahne 03 kural kartı `since + past simple, have been + V-ing ✓` (yatay) ve `since + past simple → have been + V-ing` (dikey) | düzeltildi | Ekrandaki "→" ve kart, c3'ün eski mutlak okumasının görsel karşılığıydı. §4. |
| Ekran: 05 `durum fiili: -ing yok`, 06 `durum fiilleri -ing almaz`, `-yor → süreç`, `-di → sonuç`, `süreç varsa been var` / `sonuç varsa been yok` | düzeltildi | Sesle aynı iddialar. §4. |

## 2. Ses ve süre

Yöntem (öteki cümlelerin sesi değişmez):
1. `el.py` önbellek anahtarı ağsız denetlendi (`~/is/duz3-0209I/sure.py`): sunucu önbelleğinde bu dersin hiçbir parçası yoktu (özgün ses Mac'te).
2. `el.py` yalnız c3, c5, c7'yi taşıyan geçici senaryoyla koştu: `timeout 1500 bash araclar/ses-sunucu.sh --kok ~/is/duz3-0209I/kok present-perfect-cont-ileri`
   → rc 0; 15 / 15 parça kapıdan geçti; 662 karakter (≈ 3,24 TL). Bağlam metni anahtara girdiği için değişen cümlenin bütün parçaları yeniden istendi.
3. Hız denetimi: değişmeyen EN parçalar eskiyle birebir aynı sürede (c3 EN 4,32 = 4,32 sn; c5 EN 3,04 = 3,04 sn) → özgün ses `HIZ_EN=0.9`; varsayılan korundu.
4. c1, c2, c4, c6 eski `anlatim.wav`'dan örnek-eşit kesildi (`[başlangıç_N, başlangıç_N+1)`, 48 kHz; kuyruk son 0,2 sn tepe 0; `~/is/duz3-0209I/kes.py`);
   c3, c5, c7 = yeni `cumle-1/2/3.wav`. `kur.py` → `anlatim.wav`; `araclar/ses-paketle.py --yaz --paket present-perfect-cont-ileri` → `anlatim.m4a`.
5. Kayma 0,1 sn (3 kare) katına yukarı yuvarlandı: c3 +1,52 → c4–c5 +1,60 sn; c5 +1,12 → c6–c7 +2,80 sn. Değişmeyen sahnelerin yerel kareleri aynı kalır.
6. Kanıt: PCM sha256 eski 0–17,80 = yeni 0–17,80 (`97dd9c6474121b36`); eski 34,23–49,75 = yeni 35,83–51,35 (`e1f513124d182e64`);
   eski 62,42–66,75 = yeni 65,22–69,55 (`008a6687d719403b`); cümle araları ve son 1 sn sessiz (tepe 0).
   Üreteçler önce eski dosyaları birebir üretti (`sozcuk_uret.py`, `altyazi_uret.py`: `cmp` eşit). `METIN.md` c2 satırı zaten bayattı
   (17,25 / eski parça sınırları); `sureler.json` ile yeniden kurulunca 16,77 oldu (ses ve sözcük satırı değişmedi).

| Ölçü | Önce | Sonra |
|---|---|---|
| c3 süresi / sözcük | 15,88 sn / 30 | 17,40 sn / 33 |
| c5 süresi / sözcük | 12,12 sn / 26 | 13,24 sn / 28 |
| c7 süresi / sözcük | 18,18 sn / 32 | 22,34 sn / 41 |
| Cümle başları c4 · c5 · c6 · c7 | 34,23 · 49,75 · 62,42 · 66,75 | 35,83 · 51,35 · 65,22 · 69,55 |
| Konuşma sonu | 84,93 | 91,89 |
| Ders süresi (`zaman.json` son `t_son`, `anlatim.wav`, `anlatim.m4a`) | 85,93 sn | 92,89 sn |
| `anlatim.wav` sha256 | `2258f618086a` | `164e00d44df2` (dikey bağ aynı dosya) |
| `anlatim.m4a` sha256 | — (sunucuda yoktu) | `4b43916542a0` |
| `sozcukler.json` | 157 sözcük | 171 sözcük |
| `altyazi.json` | 26 parça, son t1 85,01 | 26 parça, son t1 91,97 (≤ 92,89) |

Whisper (faster-whisper large-v3-turbo int8, eşik 0,85; rapor `~/is/duz3-0209I/kok/projeler/present-perfect-cont-ileri/ortak/anlatim/sentez.wav.rapor.json`):

| Cümle | Dil | Metin | Duyulan | Benzerlik |
|---|---|---|---|---|
| c3 | tr | Birinci örnek. | (aynı) | 1,00 |
| c3 | en | Since the school changed the timetable, students have been complaining. | (aynı) | 1,00 |
| c3 | tr | Program değişeli beri öğrenciler yakınıyor. | (aynı) | 1,00 |
| c3 | en | Since, plus a simple past clause. | (aynı) | 1,00 |
| c3 | tr | Burada iş hâlâ sürüyor: ana cümlede have been ve -ing. | Burada iş hala sürüyor. Ana cümlede have been ve ing. | 1,00 |
| c5 | tr | Üçüncü örnek. | (aynı) | 1,00 |
| c5 | en | We have known each other since we were at primary school. | (aynı) | 1,00 |
| c5 | tr | İlkokuldan beri birbirimizi tanıyoruz. | (aynı) | 1,00 |
| c5 | en | Know is a state verb. | No is a state verb. | **0,95** (en düşük; sesteş) |
| c5 | tr | Durum anlatan fiiller genellikle -ing almaz. | … ing almaz. | 1,00 |
| c7 | tr | Olmaz. Bu fiil bir durum anlatır, süreç değil. | (aynı) | 1,00 |
| c7 | en | Process: have been plus -ing. | process, have been plus ing. | 1,00 (tohum 1) |
| c7 | en | Result: have plus the third form. | Result. Have plus the third form. | 1,00 |
| c7 | tr | İkinci örnekte okuyorum süreci, bitirdim sonucu söyler. | İkinci örnekte, okuyorum … | 1,00 |
| c7 | tr | Aklında kalsın: süreç için been ve -ing, sonuç ve durum için have ve üçüncü hâl. | … Süreç için bin ve ing, … üçüncü hal. | 0,98 |

## 3. Zaman zinciri

| Dosya | Değişiklik |
|---|---|
| `zaman.json` (iki paket; `~/is/duz3-0209I/zaman.py`) | 03: kare 505 → 553, t_son 35,28 (içerik 541) · 04: 35,28–50,80 (kare aynı 478) · 05: 50,80–64,67, kare 392 → 428 (içerik 416) · 06: 64,67–92,89, kare 752 → 877 (içerik 847) |
| `sozcuk_uret.py` | `BASLAR` c4–c5 +1,60, c6–c7 +2,80 |
| `sozcukler.json`, `sureler.json` | c3, c5, c7 yeni; öteki cümleler yalnız kaydı |
| `altyazi.json` | `araclar/altyazi_uret.py` ile yeniden |
| `METIN.md` | `~/is/duz3-0209I/metin.py` ile yeniden (c3, c5, c7 yeni; c4–c7 kaydı; c2 bayat satırı düzeldi) |
| Sahne 03 `calistir.sh` | `N=553`, denetim anları `24 28 33` |
| Sahne 06 `zamanlar.json`, `calistir.sh` | t_bas 64,67, kare 877; denetim anları kaydı |

## 4. Sahneler (yatay)

| Sahne | Ne değişti | Neden |
|---|---|---|
| 01 giriş | `uret.py`, `yardim.py`: rozet `YDT · İLERİ` → `proje/index.html` (kök `tema-acik` sınıfı da geldi; HEAD'de yalnız bu sahnede eksikti) | HV-24 |
| 02–05 künye | `ortak/kunye.js` `seviye: "YDT İLERİ"` (çalışma anında çizilir) | HV-24 |
| 03 örnek 1 | p1–p4 sabitleri yeni sözcük sınırlarına doğrusal eşlendi (`~/is/duz3-0209I/esle.py`, `yama03.py`; sapma ≤ 0,20 sn); kural kartı `since + past simple, hâlâ sürüyor: have been + V-ing ✓` (Caveat 56 sarı, sözcük pencereli: hâlâ 30,76 · sürüyor: 31,20); have been 33,28, -ing 34,64, tik 34,95 | c3 yeni metin + süre |
| 04 örnek 2 | `kayma: -1.6` (sahne eski çerçevede, TBAS 33,68; yerel kareler aynı) | c3 +1,60 sn |
| 05 örnek 3 | TBAS 49,20 → 50,80, kare 428; p1–p4 sabitleri eşlendi (`yama05.py`); not `durum fiili: genellikle -ing yok` (Caveat 72, 4 parça, sağ uç 1642); ok 62,19, Present Perfect kutusu 62,9, tik 63,9 | c5 yeni metin + süre |
| 06 soru + form | `dn` `durum anlatır, süreç değil` ("durum" 71,23); balon toplanma `S(T(7, 7)) + 0,33` (eski sabit 69,4); kart dizinleri +3 (`yama06.py`); oklar `okuyorum → süreç`, `bitirdim → sonuç`; kod `süreç → been + -ing ✓` / `sonuç, durum → have + V3 ✓` (el oku, Fredoka 100); `Next lesson` T1(7, 40) − 0,3 | c7 yeni metin |
| 90 kapak | `yardim.py` kullanılmayan `ROZET = "YDT · BASIC"` → `YDT · İLERİ` (kapak `uret.py` kendi `YDT · İLERİ` sabitini kullanır; kapak çıktısı değişmez) | HV-24 |

HF kaynak üretimi: `uret.py` → `olay.py` → `tema_hf acik` (`~/is/duz3-0209I/hf-uret.sh`; render yok).

Kareler (kendim baktım; `node araclar/sahne-kare.mjs present-perfect-cont-ileri <sahne> <t,…> <dizin> --tema acik --port 41333 --sunucu 41022`,
dizin `sahneler/<sahne>/k/duz3/`, git dışı; kontak sayfaları `~/is/duz3-0209I/y0*.png`):

| Sahne | Anlar (sn) | Gözlem |
|---|---|---|
| 01 | 1,2 · 2,9 | hap `YDT · İLERİ` + `GRAMMAR`; künye `· YDT İLERİ` |
| 02 | 9,0 · 16,5 | künye `· YDT İLERİ`; süre etiketi `1.5 min` (92,9 sn → değişmez) |
| 03 | 19,5 · 22,6 · 26,0 · 29,5 · 30,9 · 31,9 · 33,6 · 34,8 · 35,25 | `hâlâ sürüyor:` sesle yazılır, karta sığar (sağ uç ≈ 1611, kutu 1740); â, ü doğru; zaman çizgisi ve etiketlerle çakışma yok |
| 04 | 36,0 · 38,2 · 43,0 · 47,5 · 50,7 | 36,0'da `2` dairesi başlar (ses 35,83); yerleşim eskisiyle aynı |
| 05 | 51,6 · 54,4 · 57,6 · 60,4 · 62,5 · 63,6 · 64,6 | not tek satır, Present Perfect kutusunun üstünde; `genellikle` sesle (62,83) |
| 06 | 66,6 · 70,0 · 72,4 · 73,6 · 76,0 · 79,6 · 82,6 · 84,4 · 85,5 · 87,3 · 89,2 · 90,6 · 92,3 · 92,85 | `durum anlatır, süreç değil` sağ sütunda; oklar sütun içinde; kod satırları ve tikler `Next lesson`dan uzak. `+V3` arası V glifinden dar görünür, okunur |

## 5. Kapak

Kapak değişmedi. YV-DUZ §4 bu dersin kapak sütunu "—"; §3 "Dokunulmayan kapaklar" listesinde bu ders yok. Kapak yazısı `SÜREÇ mi / SONUÇ mu?`
soru biçimidir, iddia kurmaz; yeni cümlelerle çelişmez. Kapak kareleri yeniden çekilmedi (kaynak ve çıktı değişmedi).

## 6. Yayın verisi zamanı (`youtube.json`, `youtube-aciklama.md`; iki pakette aynı, `cmp` eşit)

| Öğe | Önce | Sonra |
|---|---|---|
| Bölüm 1 Süreç mi, sonuç mu? | 0,00 (00:00) | 0,00 (00:00) |
| Bölüm 2 Since cümlesi | 17,25 (00:17) | 17,25 (00:17) |
| Bölüm 3 Süreç ve sonuç | 33,68 (00:34) | 35,28 (00:35) |
| Bölüm 4 Durum fiili know | 49,20 (00:49) | 50,80 (00:51) |
| Bölüm 5 Have been knowing olur mu? | 61,87 (01:02) | 64,67 (01:05) |
| En kısa bölüm | 12,67 sn | 13,87 sn (son bölüm 28,22 sn) |
| Bildirim | 34,23 sn (%39,8) | 35,83 sn (%38,6); c4 başı, önceki cümle 35,20'de biter; ilk 30 sn sonrası ilk cümle başı; son 20 sn sınırı 72,89 |

Damga bloğu `bolumler` ile aynı (yuvarlama `int(t + 0,5)`).

## 7. Kapılar

```
$ /usr/bin/python3 uretim-hatti/betikler/yv-tutarlilik.py --kilitli simple-present-temel,simple-present-temel-dikey,02-04-ydt-temel-dikey
present-perfect-cont-ileri / -dikey: süre 92.89 sn, bölüm 5; sinir, damga, kanal-etiketi, emoji, baslik, liste, dikey → TAMAM
[SORUN] zaman: 8 — hepsi simple-past-temel ve -dikey (bölüm 2–5 sahne başı değil; başka ders)
→ çıkış 1 (bu derste sorun 0; kilitli pakette 0)

$ node araclar/cakisma-kapisi.mjs present-perfect-cont-ileri --port 41333 --sunucu 41022 --json ~/is/duz3-0209I/kapi-ana.json
02, 03, 04: çakışma yok
01: cg:path0 × cg:text0 (giriş cümlesi uçuşu, 2,25–3,00) hata; t1 × t2 uyarı
05: STATE VERB × know, -ing × STATE VERB (kart içi etiket) uyarı
06: hb0/hb1/hb2 × hbx (have been knowing × kırmızı üstü çizgi, 69,92–85,17) 3 hata
→ çıkış 1 (4 hata, 3 uyarı)
```

Hata çiftlerinin hepsi kasıtlı çizim (giriş uçuşu, üstü çizgi) ile bu işte geometrisi değişmeyen öğe arasındadır. Yeni öğelerde
(`hâlâ sürüyor:`, `genellikle`, `dn`, `o1`/`o2`, `k1o`/`k2o`, `k1t`/`k2t`) hata 0. HEAD sürümü için taban ölçümü koşulmadı (eski kaynağı
sunacak ayrı paket yazma alanı dışında); çiftlerin eski olduğu çıkarımı konum değişmemesine dayanır.

## 8. Kısa video (`present-perfect-cont-ileri-s1`; yalnız rapor, dokunulmadı)

| Dosya | Aynı sınıf ifade |
|---|---|
| `ortak/anlatim/senaryo.json` ses parçaları, ekran kartları | yok (ses: "Süreç, been reading. Sonuç, have finished." doğru) |
| `ortak/anlatim/senaryo.json` `meta.canAlici[0]`, `surumler.json` | `Süreç varsa been var, sonuç varsa been yok` (ana derste düzeltilen mutlak kalıp) |
| `ortak/anlatim/senaryo.json` `meta.kapak.canAlici` | `been varsa süreç var, been yoksa sonuç var` |
| `ortak/kunye.js`, `sahneler/01-hyperframes-kapak/yardim.py`, `sahneler/03-hyperframes-cta/yardim.py`, `senaryo.json` `giris.rozetler`, `BRIEF-S1.md` | rozet `YDT · ADVANCED` (HV-24) |

## 9. Düzeltemediklerim / açık kalanlar

| Madde | Sebep |
|---|---|
| EK-11 kulak dinlemesi (c3, c5, c7 yeni ses) | Nadir'in işi; Whisper süzgeçtir |
| mp4'ler bayat | render yasak; `calistir.sh` dosyaları güncel kare sayısında (03 `N=553`, 06 `KARE=877`; 05 `sahne.js` `KARE = 428`) |
| Çakışma kapısı çıkış 1 | kasıtlı çizim çiftleri (§7); yeni öğe kaynaklı değil |
| Tutarlılık kapısı çıkış 1 | `simple-past-temel` (başka ders) |
| `uretim-tutanagi/huni-konu.{json,md}` | tutanak; eski kural özetini taşıyabilir, dokunulmadı |
| Yazım boyutu kapısı | `write-size-gate` 15 satır üstü 1 düzenlemeyi durdurdu (03 yatay); atlama bayrağı açılmadı, düzenleme ≤ 14 satırlık parçalara bölündü |
| `.claude/docs/sozlesme.md`, Kovan | istem yazmayı iki paketle sınırladı |

---
Son Güncelleme: 16.11.2026 (DUZ3-0209I oturumu).
