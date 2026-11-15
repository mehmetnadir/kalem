# BK-0204S1 öz denetim — 02-04-ydt-temel-s1b (kol b, değişken `kanca`) · 15.11.2026

| Ölçüm | Değer |
|---|---|
| Kol a değeri → kol b değeri | `kopru` → `soru` |
| Yeni kanca | "Bu iki yaşıyorum aynı mı?" (öğretmen, 5 sözcük, ilk söz 0,50) |
| Süre | kol a 31,75 (ölçülmüş) → kol b ≈ 27,79 (tahmin) · fark −3,96 sn · 28 sn payı 0,21 sn |
| Yeniden seslendirilecek | 1 cümle (cümle 1); cümle 2–4 önbellekten |
| Değer sahnesinin ilk cümlesi | değişmedi ("İngilizcede ikisi ayrılır.") |
| Yazılanlar | `senaryo-taslak.md`, `kol-b.json` (python `json.load` OK), `kapak-taslak.md`, bu rapor |

## (a) Tek değişken — satır satır fark (kol a ↔ kol b)

| # | Öğe | Kol a | Kol b | Durum |
|---|---|---|---|---|
| 1 | Kanca türü | `kopru` | `soru` | **değişken** |
| 2 | Kanca sözü | "İstanbul'da yaşıyorum. Amcamla yaşıyorum. Türkçede ikisi de yaşıyorum." | "Bu iki yaşıyorum aynı mı?" | **değişken** |
| 3 | İlk söz | 1,00 | 0,50 | kanca içi |
| 4 | Kanca sözü süresi | 5,36 sn | ≈ 1,90 sn | kanca içi |
| 5 | Sahne 01 başlık | `YAŞIYORUM` / `= İKİ ZAMAN` | `YAŞIYORUM` / `AYNI MI?` | kanca içi |
| 6 | Sahne 01 İngilizce etiket | `I live` / `I am living` | yok | kanca içi |
| 7 | Sahne 01 cümle satırları | satır 1 sözle (1,00), satır 2 sözle (2,52) | satır 1 `Bu`, satır 2 `iki` çapasında; seslendirilmez | kanca içi |
| 8 | ek_ayir (`yor` kutuları) | sahne 02 başında, `Türkçede` 3,96 ve 5,56 çapası | sahne 01'de, `yaşıyorum` çapası | kanca içi (kol a'da cümle 1 kuyruğu) |
| 9 | Sahne 01 görsel | ev + bavullu figür (400) | aynı, figür ≈ 280 | kanca içi |
| 10 | Sahne 01 geçiş | uçuş: başlık konu adına dönüşür | başlık solar, konu adı açılır | kanca içi |
| 11 | Kapak karesi (A) | t 1,97: başlık + satır 1 + etiketler | t ≈ 1,75: başlık + 2 satır + `yor` kutuları | kanca içi (sözleşme §4) |
| 12 | Sahne 02 baş parçası (cümle 1 kuyruğu) | 3,00–6,36: karaoke `yaşı-yor-um.`, ek_ayir | yok | **kanca içi; sahne 02'nin klasörüne dokunur** (§e 1) |
| 13 | Sahne 02 sözü (cümle 2, 5 parça) | metin | aynı metin, aynı wav | aynı |
| 14 | Sahne 02 ekranı (cümle 2'den sona) | kart 1 / kart 2, PERMANENT / TEMPORARY, bantlar | aynı (yerel kare −101, küresel −3,96) | aynı |
| 15 | Sahne 08 sözü | "Bu, üç farktan yalnız biri. Sınavdan önce lazım olacak. Kaydet." | aynı | aynı |
| 16 | Sahne 08 ekranı | `üç farktan biri` · kural kartı · yer imi + `Kaydet` | aynı | aynı |
| 17 | Sahne 03 sözü (öğrenci) | "Gerisi bizde. Dersin tamamı YDS Publishing YouTube kanalında." | aynı | aynı |
| 18 | Sahne 03 ekranı | ana ders kapağı kartı · `Gerisi bizde.` · `@ydspublishing · YouTube` | aynı | aynı |
| 19 | Kanal katmanı, künye, rozet | BRIEF-S1 tablosu | aynı | aynı |
| 20 | Ses kadrosu | öğretmen `…4fwc`, öğrenci `…9gjY` | aynı | aynı |
| 21 | Çağrı girişi + çekirdek cümle | "Gerisi bizde." + çekirdek | aynı | aynı |
| 22 | Kaydet kalıbı | "Sınavdan önce lazım olacak. Kaydet." | aynı | aynı |
| 23 | Toplam süre | 31,75 | ≈ 27,79 | **kancanın yan etkisi** (§e 2) |
| 24 | Kapak B / C, hikâye A / B, açıklama A / B | grup türevi | yinelenmez (grup) | aynı |

Sonuç: Değişen her öğe kanca bölgesindedir (cümle 2 başından önce). Kural sağlandı. İki yan etki var: sahne 02 klasörünün baş kırpımı
(satır 12) ve toplam süre farkı (satır 23).

## (b) Dilbilgisi

| Metin | Dil | Karar | Not |
|---|---|---|---|
| "Bu iki yaşıyorum aynı mı?" (ses) | TR | jüri bakacak | "yaşıyorum" ad gibi kullanılır (üst dil). Sözlü kullanımda doğal; yazıda tırnak isterdi. Altyazıda tırnaksız |
| `YAŞIYORUM` / `AYNI MI?` (başlık) | TR | jüri bakacak | büyük harf "mı" → `MI` doğru. Başlık telgraf biçimli: "yaşıyorum aynı mı?" |
| `İstanbul'da yaşı-yor-um.` · `Amcamla yaşı-yor-um.` | TR | kesin | kol a ile birebir aynı dizgi (jüriden geçti) |
| Yeni İngilizce cümle | EN | — | yok |
| Yeni kural | — | — | yok; kural kol a'nınkiyle aynı ("Kalıcıysa geniş zaman, geçiciyse şimdiki zaman.") |
| Yedek kanca "Bu ikisi aynı mı?" | TR | jüri bakacak | yalnız süre aşılırsa (senaryo §4) |

## (c) Huni v2 §5 — altı ölçüt (kol b)

| Ölçüt | Kol b | Kanıt |
|---|---|---|
| Sınavda çıkar mı | evet | ana ders amaç 2 (kalıcı / geçici); ana ders cümle 15–17 mini soru `is living` |
| Öğrenci en çok burada mı yanılır | evet | ana ders cümle 11–13 tuzak: Türkçe -yor → `am living` |
| Kural tek cümleye sığar mı | evet | kaydet kartı `Kalıcıysa geniş zaman,` / `geçiciyse şimdiki zaman.` |
| Türkçe köprüyle gösterilir mi | evet | değer sahnesi aynı: `yaşıyorum` → `I live` / `I am living` (kanca soru, içerik köprü) |
| Dersi izlemeden anlaşılır mı | evet | soru ve cevabı kısanın içinde; "üç farktan biri" kol a jüri düzeltmesiyle açık |
| Sınav günü yeniden bakılır mı | evet | kaydet sahnesi ve kural kartı aynı |

6 / 6 evet (eşik 4).

## (d) Kol b neden farklı sonuç verebilir

Kol a cevabı ilk saniyede verir (`= İKİ ZAMAN`, `I live` / `I am living`); kol b "aynı mı?" sorusuyla cevabı değer sahnesine saklar.
Bu yüzden kol b'de izleyip kalma oranı daha yüksek olabilir. Varsayım: Türkçe konuşan izleyici içinden "aynı" der ve "hayır, ayrılır"
cevabını görmek için kalır.

## (e) Açık noktalar

1. **Sahne 02 baş kırpımı.** Kol a'nın cümle 1'i sahne 02'ye taşar (3,00–6,36). Bu parça kancanın sözüdür; kol b'de kalkar. Kol b sahne 02
   = kol a sahne 02 yerel kare 101'den sona. Sonuç: `02-paperjs-ornek` düz simge bağı olamaz; başlangıç karesi ayarı ya da kol b kopyası
   gerekir. `kol-b.json` bu klasörü `ayni_sahneler` içinde tutar (söz ve ekran cümle 2'den sona aynı). Doğrulanmayanlar: (a) kol a olay 4
   (ek_ayir 2. kutu, kare 86) animasyonu kare 101'de bitmiş mi; (b) kol a kare 101'de satırların karaoke rengi ne (kol b satırları
   seslendirilmez). Öneri: kol b sahne 01 son karesi ↔ kol a sahne 02 kare 101 piksel karşılaştırması.
2. **Süre farkı −3,96 sn karışık değişkendir.** Kısa video ortalama izlenen yüzdeyi kendiliğinden yükseltir. Kazanan kuralında (sözleşme §6)
   önce izleyip kalma (kaydırmadan kalma) okunmalı; ortalama izlenen yüzde kol b lehine kayar. Kol a'yı 28 sn'ye çekmek ikinci değişken olur.
3. **Süre tahmindir.** Kanca sözü d ≤ 2,11 sn olmalı (pay 0,21 sn). Aşılırsa senaryo §4 sırası: ilk söz 0,40 → yedek kanca.
4. **Ekran sözden önce mi?** Başlık `YAŞIYORUM` / `AYNI MI?` 0. karede görünür; "yaşıyorum" 1,04'te, "aynı mı" ≈ 1,82'de söylenir. Kol a
   emsali aynıdır (başlık 0. karede, söz 1,64'te) ve jüriden geçti. İki cümle satırı hiç seslendirilmez; "bu iki" çapasında gelir. Jüri bakacak.
5. **Kapak karesinde 4 yazı satırı** (başlık 2 + cümle 2). Klişe 16 sınırı "≤ 3 satır". Jüri bakacak.
6. **Kapak B benzerliği.** Kol b A kapağı soru biçimlidir; grubun kapak B'si (`NASIL DENİR?`) de öyle. Kapak değişkeni sınanırken not edilmeli.
7. **s3 ataması.** Sözleşme §3: s3 de `kanca` sınar, s1'den farklı değer çiftiyle. s1 çifti = {kopru, soru}. s3 kol a kancası iki İngilizce
   cümledir ("The train to Izmir leaves …" / "I am going to …"); üç değerden hiçbirine tam uymaz. s3 çifti {kopru, yanlis-cumle} ya da
   {soru, yanlis-cumle} olmalı; sınıflama şefte.
8. **`yanlis-cumle` neden seçilmedi.** Bu konuda gerçekten yanlış cümle ya biçim hatasıdır ("I am live …", sıfat okunuşu riski taşır) ya da
   bağlam hatasıdır (kalıcı durumda `am living`; dilbilgisi olarak yanlış değil). İkisi de değer sahnesinin ilk cümlesini ve ekranını değiştirirdi.
9. **Kol a sürüm satırı.** Sözleşme §4 kol a satırına `varyant` (`kol: "a"`, `deger: "kopru"`) ister. Kol a paketine dokunma yasağı nedeniyle
   yazılmadı; şef yazar.
