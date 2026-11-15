# BK-RAPOR — simple-present-temel-s2b (kol b, değişken `kapanis`) öz denetim · 15.11.2026 (istem BK-0202S2)

| Denetim | Sonuç |
|---|---|
| (a) Tek değişken | evet; değişkenin zorunlu sonuçları ve 1 küçük ses riski aşağıda |
| (b) Dilbilgisi | yeni İngilizce cümle yok; 2 yeni Türkçe cümle "jüri bakacak" |
| (c) Huni v2 §5 | 5 / 6 evet (eşik 4); kol a ile aynı |
| (d) Varsayım | aşağıda, 1 cümle |
| (e) Açık nokta | 7 |

Yazılan: `senaryo-taslak.md`, `kol-b.json` (ayrıştırıldı: `json.load` OK), bu rapor. `kapak-taslak.md` yazılmadı: değişken `kanca` değil.

## (a) Fark tablosu (kol a ↔ kol b)

| Öğe | Kol a | Kol b | Değişken içi mi |
|---|---|---|---|
| Kanca sesi ve ekranı (sahne 01) | `Usually görünce hangi zaman?` · kapak A başlığı · takvim 4/5 tik | aynı | — (aynı) |
| Değer sesi ve ekranı (sahne 02) | 3 parça · kart, soluk TR, oklar, gün kutuları | aynı | — (aynı) |
| Kural özeti sözü (sahne 03 parça 1) | `Usually, always, every day: Simple Present.` (EN) | aynı metin | — (aynı) |
| Kural özeti kartı | 3 satır, `Simple Present.` sarı hap | aynı | — (aynı) |
| Kaydet kalıbı sözü | `Bu kuralı kaybetme. Kaydet.` | `Ekran görüntüsü al, sınav günü bak.` | evet |
| Kaydet simgesi | yer imi, `Kaydet.` çapasında | ekran görüntüsü çerçevesi (4 köşe parantezi), `al,` çapasında | evet (istem: ekran kalıba uyar) |
| Kaydet yazısı | `Kaydet` | `Ekran görüntüsü al` | evet |
| Çağrı girişi sözü (öğrenci) | `Bitmedi, gel.` | `Konu burada bitmiyor.` | evet |
| Çağrı girişi ekranı | 96 px, 2 kinetik adım | ≈ 89 px (900 px'e sığan), 3 kinetik adım | zorunlu sonuç (yazı uzun) |
| Çekirdek cümle | `Dersin tamamı YDS Publishing YouTube kanalında.` | aynı metin | — (aynı) |
| Ana ders kapağı kartı, `@ydspublishing · YouTube` hapı | 900×506 kart; sarı hap `YDS` çapasında | aynı | — (aynı) |
| Kanal katmanı, künye, tema, ses kadrosu | aynı değerler | aynı | — (aynı) |
| Kuyruk ve ilk söz | son söz + 1,0 sn · ilk söz 1,00 | aynı | — (aynı) |
| Sahne 03 süresi | 7,20 sn (kart sabit 3,21) | ≈ 7,48 sn (kart sabit ≈ 3,49) | zorunlu sonuç (kalıp +0,28 sn) |
| Sahne 04 süresi | 6,66 sn | ≈ 6,94 sn | zorunlu sonuç (giriş +0,28 sn) |
| Toplam süre | 25,73 sn (ölçülen) | ≈ 26,29 sn (tahmin; aralık 25,61–27,04) | zorunlu sonuç (+0,56 sn) |
| Sahne 03 parça 1 ses dalgası | ölçülen kayıt | aynı metin, yeniden sentez (sonraki parça değişti) | risk: küçük ikinci değişken (açık nokta 2) |
| Çekirdek ses dalgası | önbellek (02-04 s2 ile aynı) | aynı metin, yeniden sentez (önceki parça değişti) | risk: küçük (6 ölçümde hep 3,52 sn) |
| Türevler (kapak, hikâye, açıklama) | grup türevleri | yinelenmez; grubunkiler | — (sözleşme §4) |

Sonuç: söz ve ekranda yalnız kaydet kalıbı ile çağrı girişi değişti. Süre, kinetik adım ve yazı boyu farkları değişkenin zorunlu sonucudur.

## (b) Dilbilgisi

| Cümle | Durum | Not |
|---|---|---|
| `Usually, always, every day: Simple Present.` | kesin | kol a ile birebir; kol a jürisi geçti (`../../simple-present-temel-s2/uretim-tutanagi/juri/s2.dil.md`, madde 2 sonrası `en` parça) |
| `My brother usually goes to school by bus.` | kesin | kol a ile birebir, ana ders cümle 4 parça 2 |
| `Ekran görüntüsü al, sınav günü bak.` | jüri bakacak | standart §4 listesinde. `bak` nesnesizdir; nesne bağlamdan gelir (ekran görüntüsüne). `sınav günü` zaman zarfıdır; duyuşta `sınav gününe bak` (tarihe bak) ile karışma riski düşük ama var. Whisper kapısı `görüntüsü` ↔ `görüntüsünü` ayrımına bakmalı |
| `Konu burada bitmiyor.` | jüri bakacak | standart §4 listesinde; kurallı, doğal konuşma Türkçesi. Öğrenci sesinde çekirdekle birlikte söylenir |

Yeni kural cümlesi ve yanlış–doğru cümlesi yok (değişken `kanca` değil).

## (c) Huni v2 §5 ölçütleri (kol b)

| # | Ölçüt | Kol b | Not |
|---|---|---|---|
| 1 | Sınavda çıkar mı? | evet | içerik kol a ile aynı (zaman ifadesi sinyali) |
| 2 | Öğrenci en çok burada mı yanılır? | hayır (kanıt yok) | kol a raporu ile aynı karar; yanılgı verisi yok |
| 3 | Kural tek cümleye sığar mı? | evet | `Usually, always, every day: Simple Present.` |
| 4 | Türkçe köprüyle gösterilir mi? | evet | `Her sabah yedide kalkarım` + soluk TR çeviri |
| 5 | Dersi izlemeden anlaşılır mı? | evet | soru → örnek → kural kısa içinde kapanır |
| 6 | Sınav günü yeniden bakılır mı? | evet | kaydet kalıbı bunu doğrudan söyler: `sınav günü bak` |

Sonuç 5 / 6 (eşik 4).

## (d) Kol b neden farklı sonuç verebilir (varsayım)

Ekran görüntüsü tek dokunuşluk, telefonda kalıcı ve sınav gününe bağlanmış somut bir eylemdir; izleyici bu çağrıya "Kaydet"ten daha çok
uyabilir, ama bu uyum platformun kaydetme sayacına düşmez.

## (e) Açık noktalar

1. **Ölçü yanlılığı:** ekran görüntüsü YouTube ve Instagram kaydetme sayacına girmez. Sözleşme §6 ölçü sırasında kaydetme 2. sıradadır;
   `kapanis` değişkeninde bu ölçü kol b aleyhine eğilir. Şef kararı: bu değişkende kaydetme ölçüsü tek başına karar vermesin mi?
2. **Ses birebirliği:** sahne 03 parça 1 ve çekirdek cümlenin metni aynıdır, ama `el.py` anahtarı komşu parçayı içerdiği için yeniden
   sentezlenir. Kural özeti sesi kol a'dan küçük farkla ayrılabilir (vurgu, süre). Önerim: kabul + kulak + Whisper ≥ 0,9; sözleşme §4
   önbelleği cümle düzeyinde söz verir. Birebir ses gerekiyorsa cümle 1–3 parça 1 kol a anlatımından kesilir; bu, var olan araçta yok.
3. **Paket yapısı:** sözleşme §4 `ortak/` için "kol a'ya simge bağı" der. Kol b'nin `ortak/anlatim` dizini ayrı olmalıdır (yeni senaryo,
   ses, sözcük zamanı); `ortak/` altındaki öteki dizinler bağ olabilir. Sözleşme metni bu ayrımı yazmıyor.
4. **Değer dizesi biçimi:** sözleşmede `kapanis` değeri için dize biçimi yok. Ben `<kaydet kalıbı> | <çağrı girişi>` yazdım. Sözleşme §6
   "aynı değer en az 3 konuda" ölçüsü dize eşitliğine dayanır; 12 dersin kol b dosyaları aynı dizeyi kullanmalıdır.
5. **Süre:** tahmin 26,29 sn, standart §3 yaklaşık hedefini (22–26) 0,29 sn aşar; istem sınırı (28) içinde. Kuyruk ya da ilk söz
   kısaltılırsa ikinci değişken doğar; önerilmez.
6. **Türev uyumu:** açıklama ilk satırı (`Sınav günü bakmak için kaydet.`) ve hikâye karelerindeki `Kaydet` + yer imi gruba aittir; kol b
   videosu "ekran görüntüsü al" der, açıklaması "kaydet" der. Sözleşme gereği değişmedi; değişirse değişken açıklamaya da taşınır.
7. **Simge:** yerel `ortak/cizim/tabler/` içinde ekran görüntüsü simgesi yok (`camera.svg` fotoğraf makinesidir). 4 köşe parantezi yolu
   sahnede literal yazılır. Chrome kesik deseni her `M`'de baştan başlar (kol a SPEC §6 notu); 4 köşe ayrı `path` olarak sırayla ya da
   tek `M` yolu olarak çizilmelidir. Bu iş sahne SPEC'inindir.
