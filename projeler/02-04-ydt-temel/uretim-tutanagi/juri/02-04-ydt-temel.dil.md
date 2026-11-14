KARAR: DÜZELT

# Dil jürisi — 02-04-ydt-temel · 14.11.2026
Denetlenen: `uretim-tutanagi/senaryo-taslak.md` · Kaynak kanıt: `istem/A-girdi.md` · Ses kuralı: `references/ses-tasarimi.md`, `ses-sozluk.json`

Genel: 7 İngilizce örnek cümlenin hepsi dilbilgisi olarak doğru ve doğal; YDT temel düzeyine uygun. Kısaltma yok (G-6 uyumlu). Tire ve `özne I` kuralı ihlali yok. Aşağıdaki 4 madde Türkçe anlatımdadır.

## Maddeler

1. **Satır 9 (bölüm 4 Karşıt çift) · ana madde** — Sorun: ses "Burada today konuşma anını gösterir" ve ekran `today → right now` yanlış genelleme. *today* konuşma anını göstermez; günü gösterir. Satır 10 hemen ardından *today*'in iki cümlede de bulunduğunu ve farkı anlamın yaptığını söyler; satır 9 bununla ve satır 14 ("zaman sözcüğü ipucu verir, kararı anlam verir") ile çelişir. Öğrenci "today = şimdi" kısayolunu öğrenir.
   Kanıt: `istem/A-girdi.md` §4 madde 6–7 (döküm 00:55–01:09: "bugün gerçekleşen olaya vurgu", "sadece bugüne ait"); taslak satır 9 ↔ satır 10, 14.
   Düzeltme: ses "Burada today bugünü gösterir. Bugünkü kıyafet: konuşma anında olan durum, şimdiki zaman." Ekran `today → this day only`.

2. **Satır 11 (bölüm 5 Tuzak)** — Sorun: "Ama İngilizcede ing yok." İngilizcede -ing vardır (satır 2, 3, 13); cümle genel kural gibi okunur ve yanlıştır. Ayrıca "İngilizcede ing" art arda sözcükleri kulakta karışır ("ing" /ɪŋ/ + "İngilizce"; taslak §6 Whisper riski).
   Kanıt: taslak satır 11 ↔ satır 3, 13 (*is wearing*, *am living*); `ses-tasarimi.md` §1 KULAK notu.
   Düzeltme: "Ama bu cümlede ing eki yok." (Satır 6 öğrenci sorusu "Neden ing yok?" doğru, kalır.)

3. **Satır 7 (bölüm 2)** — Sorun: "Bu cümlelerde özne genelde cansızdır." Belirsiz zamir: *bu* hem tarife hem plan cümlesini gösterebilir; plan cümlesinin öznesi kişidir.
   Kanıt: taslak satır 7 (4. cümle); `yazim-stili-ste100.md` §3 (belirsiz zamir yok).
   Düzeltme: "Tarife cümlelerinde özne genelde cansızdır: tren, uçak, ders."

4. **Satır 2, 8 (terim tutarlılığı)** — Sorun: aynı kavram iki adla geçer: "üç kullanım farkı" (satır 2), "üç karşıtlık" (satır 8). STE: bir kavram = bir sözcük.
   Kanıt: taslak satır 2 ve satır 8 ses metinleri.
   Düzeltme: satır 8 "Bu derste üç fark gördük. Genel durum ile konuşma anı. …" ("Karşıt çift" bölüm başlığı kalabilir.)

## Ek öneri (madde sayılmaz)
- Satır 15 "Boşlukta hangisi?" → "Boşluğa hangi şık gelir?" (doğal Türkçe).

## Okunuş riskleri (kulak kontrolü; sesi üreten bakar)

| Yer | Risk | Öneri |
|---|---|---|
| Satır 3 "Fiil aynı: wear." | tr parçada tek İngilizce sözcük; Türkçe "ver" gibi okunabilir | ayrı `en` parça ya da `/wɛr/` |
| Satır 9, 10 *today* (tr parçada 3 kez; biri cümle başı) | "tudey/todi" okunuşu | ayrı `en` parça ya da `/təˈdeɪ/` |
| Satır 3, 17 *wearing*, *living* (tr parçada yalın) | "-ing" Türkçe okunabilir | IPA ya da `en` parça; deneme sayfasında dinle |
| Satır 11, 13 "yor eki", "ing" | tek başına ek harf harf okunabilir | `ses_metni.py` çıktısını dinle (3021) |
| Satır 15 `[sus 0,5 sn]` | EN cümle ortadan bölünür; *he* düşen tonla biter | iki `en` parçanın tonunu dinle |
| Satır 5, 10 *p.m.* | EN parçada "pi em" okunur (doğru) | değişiklik yok (nokta 6) |

## Açık nokta cevapları (dil)

- **2 (Karşıt çift today):** Sonuç ("farkı anlam yapıyor") dil olarak doğru ve kaynak anlamdan türetilmiş; yeni kural sayılmaz. Satır 9'un *today = konuşma anı* cümlesi yanlış (madde 1).
  Kanıt: A-girdi §4 madde 6–7; taslak satır 9–10.
- **3 (Tuzak cümlesi):** *I am living in Istanbul.* doğru ve doğal ("şimdilik"). "Olur, ama anlam değişir" doğru. Türkçe "-yor" tuzağı burada kalıcı ↔ geçici içindir, 02-02'deki rutin tuzağından ayrı açı; yineleme sayılmaz. Düzeltilecek tek yer: "İngilizcede ing yok" (madde 2).
  Kanıt: A-girdi §2 S2; taslak satır 11–13.
- **4 (Mini soru):** *is living* doğal ve dersle koşut; *is staying* daha deyimsel ama gerekli değil. D) *to live* temel YDT'de standart çeldirici, uygun. A) *lives* tek başına doğru cümle kurar; dışlayan *this month* + *but* karşıtlığıdır ve satır 17 bunu açıkça söyler, yeterli. C) *live* ve E) *are living* özne uyumsuzluğudur, ayrım kesin.
  Kanıt: taslak satır 15–17.
- **6 ("7 pm" okunuşu):** G-6 Türkçe parçada İngilizce harf okumasını yasaklar (YDT → vay-di-ti). *p.m.* EN parçada İngilizce harf adlarıyla okunur ve doğrudur. "At seven in the evening" karaoke ekranla ayrışır; gerek yok. Kabul.
  Kanıt: `ses-tasarimi.md` §1 Kısaltma satırı; taslak satır 5, 10 EN parçalar.
