# İstem P0202-S2-A raporu — simple-present-temel-s2 kısa video taslağı (huni v2) + kapak, hikâye, açıklama · 15.11.2026

| Dosya | İçerik | Durum |
|---|---|---|
| `senaryo-taslak.md` | 4 sahne (kanca · değer · kaydet · çağrı), 4 cümle / 8 parça, ses–ekran–görsel tablosu, kaynak ve önbellek eşlemesi, süre | TASLAK |
| `kapak-taslak.md` | 3 kapak (A kanca karesi · B soru · C kural kartı), v2 yerleşimi, `senaryo.json` alanları | TASLAK |
| `hikaye-taslak.md` | 2 hikâye karesi (A kural kartı + Kaydet · B "Hangisi doğru?" + Kaydet), UTM | TASLAK |
| `aciklama-taslak.md` | 2 açıklama seti (A doğrudan · B soruyla açılan) × YouTube / Instagram / TikTok, UTM tablosu, yer tutucular | TASLAK |
| `S2-A-RAPOR.md` | bu rapor | — |

Yapılmayan (istem kuralı): ses sentezi, ElevenLabs çağrısı, render, sahne kodu, git commit, alt ajan, silme. Yazma yalnız bu dizinde
(dizin bu istemde açıldı; pakette başka dosya yok). Kovan kaydı yazılmadı (yazma kapsamı dışında). Sözleşme kancası satır istemedi.

## 1. Süre tahmini ve hesabı

Yöntem: ölçülmüş ikizi olan parça ikizin süresini alır. İkizi olmayan TR parça için ana dersin ölçülmüş öğretmen hızından model kuruldu:
süre = 0,1731 sn × hece + 0,649 sn × iç duraklama. Kaynak: ana ders `sureler.json` 20 TR öğretmen parçası, en küçük kareler (5,78 hece/sn);
uyum hatası ortalama %10,9, en büyük %29,3. Kaydet ve çağrı parçaları `02-04-ydt-temel-s2` (aynı iki ses) ölçümünden.

| Kalem | sn | Kaynak |
|---|---|---|
| İlk söz | 1,00 | v2 pilot |
| C1 `Usually görünce hangi zaman?` | 1,73 | model (10 hece, 0 duraklama) |
| Cümle arası | 0,55 | |
| C2 EN `My brother usually goes to school by bus.` | 2,96 | ana ders cümle 4 parça 2 ölçülmüş |
| C2 `Alışkanlık işareti.` | 1,21 | model (7 · 0) |
| C2 `Şu an değil, her sabah yedide kalkarım gibi.` | 3,25 | model (15 · 1) |
| C2 parça araları | 0,40 | 0,25 (EN → TR) + 0,15 (TR → TR) |
| Cümle arası | 0,55 | |
| C3 `Usually, always, every day: Simple Present.` | 4,03 | model (12 · 3); ana dersin aynı biçimli iki parçasında model %2–3 uzun kaldı |
| C3 `Bu kuralı kaybetme. Kaydet.` | 2,48 | 02-04 S2 cümle 3 parça 2 ölçülmüş |
| C3 parça arası | 0,15 | |
| Cümle arası | 0,55 | |
| C4 öğrenci (2 parça + 0,15) | 5,11 | 02-04 S2 cümle 4 ölçülmüş; birebir aynı → önbellek |
| Kuyruk | 1,00 | son söz + 1,0 sn |
| **Toplam** | **24,97** | hedef 22–26 içinde |

- Sahneler: 01 0,00–2,73 · 02 2,73–11,10 · 03 11,10–18,31 · 04 18,31–24,97.
- Olağan sapma (modelli parçalar +%10,9, komşusu değişen ikizler +%10): 26,63 sn. En kötü (modelli +%29,3): 28,51 sn.
- 28 sn aşılırsa B planı metne dokunmaz: ilk söz 0,50 + kuyruk 0,44 = −1,06 sn → en kötü 27,45 sn. C planı (`yedide` çıkar) jüri ister.
- Maliyet tahmini: yeni 202 karakter ≈ 0,99 TL; cümle 4 ücretsiz.

## 2. Standart §5 ölçütleri (eşik: 6 sorudan en az 4 "evet")

| # | Soru | Cevap | Kanıt |
|---|---|---|---|
| 1 | Sınavda çıkar mı? | evet | ana ders amaç 2 "zaman ifadelerini tanımak"; cümle 7 "Kod: always, usually, every day, Simple Present"; kardeş ders 02-04 cümle 14 "Zaman sözcüğü … ipucu verir" ve cümle 18 "Dil sınavında boşluğu görünce …" |
| 2 | Öğrenci en çok burada mı yanılır? | hayır (kanıt yok) | yanılgı verisi yok. Temel düzeyde sık yanılgı `-s` (S1 konusu) ve şimdiki zamanla karışmadır; sinyal sözcük hızlı kazanımdır. Sayıma girmedi |
| 3 | Kural tek cümleye sığar mı? | evet | `Usually, always, every day: Simple Present.` (kaydet kartı, hikâye A) |
| 4 | Türkçe köprüyle gösterilir mi? | evet | `Her sabah yedide kalkarım` (ana ders cümle 1, geniş zaman) + soluk TR çeviri `Kardeşim genellikle okula otobüsle gider.`; `usually` ↔ `genellikle` oku |
| 5 | Dersi izlemeden anlaşılır mı? | evet | soru → örnek → kural kısa içinde kapanır; `goes`'taki `-es` açıklanmaz, kural için gerekmez |
| 6 | Sınav günü yeniden bakılır mı? | evet | kaydet kartı 2,63 sn sabit; hikâye A aynı kart; açıklama ilk satırı "Sınav günü bakmak için kaydet." |

**Sonuç: 5 / 6 evet** (eşik 4).

## 3. Sürümler arası fark

| Türev | A | B | C |
|---|---|---|---|
| Kapak | kanca karesi, kod: `USUALLY` / `= ALIŞKANLIK` (sarı hap); karakter + takvim | soru: `ALWAYS VARSA` / `HANGİ ZAMAN?`; öğrenci başı + balon `always?` + sarı `?` | kural kartı: `ÜÇ SÖZCÜK,` / `TEK ZAMAN` (S2-C düzeltmesi → `ÜÇ İFADE,` / `TEK İŞARET`, `S2-duzeltme.md` madde 4); üç sözcük → `Simple Present`; figür yok |
| Hikâye | kural kartı + örnek + Kaydet (oku, kaydet) | "Hangisi doğru?" `My brother usually ____` · `A) goes` / `B) is going` + ipucu + Kaydet (seç) | — |
| Açıklama | başlık kural kodu; 2. satır püf nokta | başlık soru (kapak B ile aynı); 2. satır soru + cevap | — |

Karakter görseli A'da (`ortak/kapak/karakter.png`); B'de ana dersin öğrenci başı (kalem çizgisi). Üç kapakta da `canAlici[2]` tek kaynak.

## 4. Yeni metinler (jüri bakacak)

| Yer | Metin | Ana derste |
|---|---|---|
| Ses C1 | `Usually görünce hangi zaman?` | yok |
| Ses C2 | `Alışkanlık işareti.` | cümle 4 parça 4'ün parçası |
| Ses C2 | `Şu an değil, her sabah yedide kalkarım gibi.` | `Her sabah yedide kalkarım` = cümle 1; geri kalanı yok |
| Ses C3 | `Usually, always, every day: Simple Present.` | içerik cümle 4 parça 4 + cümle 7 son parça; tümce yok |
| Ekran | `alışkanlık`, `şu an` (üstü çizili), başlıklar, kart metinleri, `Hangisi doğru?`, `Şu an mı, alışkanlık mı?` | yok |
| Açıklama | "püf nokta" cümlesi, "Türkçede de geniş zaman: …", set B soruları | yok |

Standart kalıplar (`Bu kuralı kaybetme. Kaydet.`, `Bitmedi, gel.`, çekirdek çağrı) istemden ve standart §4'ten geldi; jüri dışı.

## 5. Açık noktalar

1. **"Şu an değil" (jüri dil + kaynak):** ana ders Simple Present'i şimdiki zamanla karşılaştırmaz; kısa yalnız Türkçe söyler, `-ing` örneği vermez.
   İstemin "(konuşma anı değil)" notu için girdi. Ayrıca `always` + `-ing` (yakınma: "is always complaining") temel derste yok; kısa "işaret" der,
   ana dersin "Kod"undan güçlü iddia kurmaz. Jüri örneksiz bulursa C2 parça 3 `Her sabah yedide kalkarım gibi.` olur (−1,35 sn, toplam 23,62).
2. **Hikâye B şık B:** `is usually going` özel bağlamda kurulabilir; kökte bağlam yok, cevap A. Jüri ek bağlam isterse kök `… every day.` (`hikaye-taslak.md` §4).
3. **Whisper riski:** C1 ve C3 TR parçaları İngilizce sözcük taşır. Emsal var (02-04 S2 `Today …` 1,00; ana ders cümle 4 ve 7 aynı biçim), ama ana
   pakette `sentez.wav.rapor.json` yok; sentezde kulak + Whisper kapısı.
4. **Kaydet sahnesi uzun:** 7,21 sn (standart tablosu ≈ 3 sn). Neden: istem kural özetini seslendirtir; pilot S1–S3 kaydet sahnesinde kuralı
   seslendirmedi ("Bu, üç farktan yalnız biri." dedi). Toplam hedef içinde; şef onayı.
5. **Kapak A başlığı** `= ALIŞKANLIK` sesteki `Alışkanlık` sözünden (6,49) önce görünür. Kapak istisnası (kalıp §4–§5; 02-04 A emsali).
6. **Kapak C figürsüz:** kalıp §4 sapması; 02-04 S2'de iki jüri kabul etti.
7. **Aynı örnek iki kısada:** 02-02 S1 (`simple-present-temel-s1`, v1) `My brother goes to school by bus.` kullanır; S2 aynı cümlenin `usually`'li
   ana ders biçimini kullanır. Yıl boyu yayında tekrar algısı olabilir. S1 henüz v1'dir ("Tam dersi kanalda izle."); v2 çevirisinde çağrı girişi
   `Bitmedi, gel.` ve kaydet kalıbı `Bu kuralı kaybetme.` OLMAMALI (standart §4: aynı derste yinelenmez).
8. **Önbellek varsayımı:** cümle 4'ün ücretsiz gelmesi srv21 önbelleğinde 02-04 S2 kaydının durmasına ve sentezin varsayılan hızda koşmasına bağlı
   (`el.py` satır 69 `HIZ_EK`). Önbellek kaydı bu istemde açılmadı.
9. **Sonraki ders adı** `Present Continuous ve Simple Present` kimlik sırasından (02-02 → 02-03) türedi; katalogda doğrulanmadı.
10. **Adresler:** `platform_url` belgeden türedi, canlılığı ölçülmedi; `{UZUN_VIDEO_URL}` yer tutucu.
11. **Kanal ayarı:** kanal "çocuklara özel" ise Shorts'ta listeye kaydetme kapalıdır (standart §8); denetlenmedi.
12. **Metin taraması (standart §7 kapı 3):** bu taslaklarda "Tam ders" ve "dakika" yalnız kural alıntısı olarak geçer; tarama `uretim-tutanagi/`
    dizinini dışarıda bırakmalı (02-04 pilot taslakları da aynı durumda). Senaryo ses ve ekran metninde yoktur.
