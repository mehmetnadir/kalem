# simple-present-temel-s3b · kol b senaryo taslağı — A/B deneme kolu · değişken `kanca` (9:16)

Durum: TASLAK (istem BK-0202S3, 15.11.2026). Ses sentezi, sahne kodu ve render YOK.
Bağlayıcı: `dijital-anlatim/.claude/docs/huni-ab-sozlesme.md` (§2 kural 2–3, §3, §4) ve `huni-v2-standart.md` (§1–§7, §9).
Kol a: `../../simple-present-temel-s3/` (`ortak/anlatim/senaryo.json`, `sozcukler.json` ölçülmüş zamanlar, `zaman.json`, `BRIEF-S3.md`,
`uretim-tutanagi/senaryo-taslak.md`, `kapak-taslak.md`, `S3-duzeltme.md`, `juri/`). Ana ders: `../../simple-present-temel/`.
Kardeş kol b: `../../simple-present-temel-s1b/uretim-tutanagi/` (değişken `kanca`, değer `yanlis-cumle`).

## 1. Varyant

| Alan | Kol a | Kol b |
|---|---|---|
| Paket | `simple-present-temel-s3` | `simple-present-temel-s3b` |
| Sürüm kimliği | `s3` | `s3b` |
| Değişken | `kanca` | `kanca` |
| Değer | `yanlis-cumle` | **`soru`** |
| Kanca sözü | EN `He doesn't goes.` + TR `Hata nerede?` (2 parça) | **TR `Olumsuzda s nereye gider?` (1 parça)** |
| Kanca karesi başlığı | `BU CÜMLE` / `YANLIŞ` | **`S NEREYE` / `GİDER?`** (`kapak-taslak.md`) |
| Kanca karesi kartı | `He doesn't goes.` (yanlış cümle) | **`He goes.` (doğru cümle)** |
| `utm_content` | `s3-a` · `s3-b` | `s3b-a` · `s3b-b` |

Kol a değeri `yanlis-cumle`: kanca yanlış İngilizce cümleyi söyler ve gösterir, sonra "hata nerede" diye sorar. Kanıt: kol a
`senaryo.json` cümle 1 (`He doesn't goes.` · `Hata nerede?`); kol a taslak §1 "Biçim: yanlış–doğru".

Kol b neden `soru`:
- Sözleşme §3: s3 kancası "s1'den farklı değer çifti" taşır. s1 çifti {`kopru`, `yanlis-cumle`} (`../../simple-present-temel-s1b/
  uretim-tutanagi/kol-b.json`). s3 kol a `yanlis-cumle`; kol b `kopru` olursa çift s1 ile aynı olur. Kalan değer `soru`.
- s1 kol b `yanlis-cumle` seçti; `soru` ondan farklıdır (istem okuma 4). s1b BK-RAPOR açık nokta 4 aynı sonucu yazar.

Kanca değer sahnesine soru → cevap olarak bağlanır:

```
kanca  : "Olumsuzda s nereye gider?"
değer  : "Olumsuzda ve soruda does girer, s ona geçer."   (kol a ile aynı; "nereye" → "ona")
```

**Değer sahnesinin ilk cümlesi uyarlanmadı. Değer, kaydet ve çağrı sözü kol a ile birebir aynıdır.**

Kanca ekranı kol a kartına yakınsar: kapak karesi doğru `He goes.` kartını gösterir. "Olumsuzda" sözüyle karta `doesn't` girer.
1,60'ta kart kol a kartının aynısıdır (`He doesn't goes.`). Çıkış kol a kuralıyla olur; sahne 02 kare 0 değişmez. Bu yüzden değer
sahnesinde kanca izi yoktur (s1b'de 3 kanca izi vardı, `../../simple-present-temel-s1b/uretim-tutanagi/BK-RAPOR.md` (a) #14–#16).

Yineleme denetimi (`kapak-standardi.md` satır 41): kol b sözü ve başlığı grubun türevlerini yinelemez.

| Türev | Metin | Kol b ile ilişki |
|---|---|---|
| Kapak B | `GOES mu,` / `GO mu?` | farklı soru (seçim sorusu; kol b yer sorusu) |
| Kapak C | `DOES VARSA` / `FİİL YALIN` | kural; soru değil |
| Açıklama A başlığı | `Does varsa fiil yalın: He doesn't go` | kural; soru değil |
| Açıklama B başlığı | `Does gelince fiile s gelir mi?` | evet/hayır sorusu; kol b "nereye" sorar, ortak sözcük yalnız `s` |
| s2 kancası | `Usually görünce hangi zaman?` | aynı tür (`soru`), başka bilgi |

## 2. Senaryo

**TR** / **EN** = ses parçasının dili. Ses metninde ve ekranda rakam yok.
**DEĞİŞTİ** satırı kol b'nin yeni satırıdır; hücrelerin tamamı kalındır. "kol a ile aynı" satırlarının metni kol a
`senaryo-taslak.md` §2'den aynen kopyalandı.

**DİKKAT:** Kopyalanan satırlardaki **TR**, **EN**, **[YENİ]**, **[ANA]** kalınlığı kol a'dan gelir; fark işareti değildir. O
satırlardaki saniyeler kol a taslağının sentez öncesi tahminidir. Kol b zamanı §5'tedir (kol a ölçülmüş zamanı − 0,41 sn).

Kanca satırının sözcük zamanları tahmindir (§5). İşaret: **[YENİ]** = ana derste yok, jüri bakacak.

| Sahne | Cümle | Konuşan | Ses metni (söylenen) | Ekran metni | Görsel fikir |
|---|---|---|---|---|---|
| **1 kanca (HyperFrames) · kol b 0,00–3,48 · DEĞİŞTİ** | **1** | **öğretmen** | **TR `Olumsuzda s nereye gider?` [YENİ; jüri bakacak] tek soru cümlesi; `Olumsuzda` ve `s` ana ders cümle 7 parça 4'ün sözcükleri; ilk söz 1,00 (kol a ile aynı)** | **0. kare = kol b kapak A (`kapak-taslak.md` §2): başlık `S NEREYE` / `GİDER?` (satır 2 sarı hapta) + kart `He goes.` (Fredoka 700 80; kart çerçevesi kol a ile aynı: x 60–737, y 840–1000; yazı kartta ortalı). Altyazı bandı sözcük zamanlı karaoke: `Olumsuzda` 1,00 · `s` 1,94 · `nereye` 2,29 · `gider?` 2,80. 1,00–1,60: karta `doesn't` girer; kart `He doesn't goes.` olur (kol a kartı, aynı yer ve boy). Kart yazısı karaoke almaz (söylenmez)** | **Kol a ile aynı: karakter sağda (ana `ortak/kapak/karakter.png`), sola, karta işaret eder; arkasında sarı daire; hap çerçevesi 0,30–0,80 kalemle. Yeni: 1,00–1,20 `He` ile `goes.` arasına mürekkep kalem şapka işareti `‸` (SVG). 1,00–1,40 `He` sola (x 100), `goes.` sağa kayar (kol a yerleri). 1,20–1,60 `doesn't` soldan sağa kalemle açılır (kırpma). 1,60–1,77 `‸` söner. 1,94 ("s"): `goes.` içindeki `es` altında sarı kalem çizgisi (karaoke gibi, sözcük sonunda kapanır). 2,29 ("nereye"): kırmızı kalem `?` kol a yerinde (kart sağ üst köşesi), 2,29–2,73. Çıkış kol a kuralıyla (son söz sonu − 0,50 = 2,98): başlık ve `?` söner, karakter sağa kayıp çıkar, kart y ≈ 480'e kayar. Son kare = kol a sahne 01 son karesi (altyazı metni hariç)** |
| kol a ile aynı · 2 değer (Paper.js) 3,79–12,90 | 2 | öğretmen | **TR** `Olumsuzda ve soruda does girer, s ona geçer.` **[ANA]** cümle 7 parça 4 ile birebir (4,34–8,18) | Altyazı bandı karaoke (Olumsuzda 4,34 · does 5,70 · s 6,66 · geçer 7,22). Kartta yazı değişmez | "does" (5,70): karttaki `doesn't` içinde `does` sarı kalem dairesi. "s ona" (6,66): `goes`'un `es` ekinden `does`'a kavisli kalem oku (ek yer değiştirir; ekranda `go-es` → `do-es`, ana ders ayırımı). |
| kol a ile aynı | | | **TR** `Fiile s gelmez.` **[YENİ]** ana derste yok (ana cümle 7 parça 3 "Fiile s gelir."in karşıtı; dil jürisi 2) (≈ 8,33–9,93) | Altyazı bandı karaoke (Fiile 8,33 · s ≈ 8,80 · gelmez ≈ 9,06) | "s" (≈ 8,80): `goes`'un `es` eki birlikte kırmızı kalemle üstü çizilir (`go` + çizili `es`). "gelmez" (≈ 9,06): kartın sağında kırmızı kalem `✗` (SVG, emoji değil). `does` dairesi mürekkebe döner. |
| kol a ile aynı | | | **EN** `He doesn't go. Does she go?` **[YENİ]** EN; yakın: cümle 7 parça 5 "He does not go. Does he go?" (≈ 10,18–12,90) | Kart 1 düzelir: `He doesn't go.` (Fredoka 72; He ≈ 10,18 · doesn't ≈ 10,46 · go ≈ 10,74) + soluk TR `O gitmez.` (Caveat 52, ikincil). Kart 2 altta: `Does she go?` (Does ≈ 11,70 · she ≈ 11,94 · go ≈ 12,40) + soluk TR `O gider mi?` (Caveat 52) | "He": üstü çizili `es` karttan düşer, solar; `✗` silinir; kart `go` ile kalır. Tek sarı: konuşulan `go` altında kalem altçizgisi (önce kart 1, sonra kart 2). |
| kol a ile aynı · 3 kaydet (HyperFrames) ≈ 12,90–17,90 | 3 | öğretmen | **TR** `Does varsa fiil yalın.` **[YENİ]** ana derste yok (≈ 13,45–15,19) · **TR** `Bir arkadaşına gönder; o da karıştırıyor.` **[STANDART]** §4 kaydet kalıbı, ana derste yok (≈ 15,34–17,90) | Kural özeti kartı, tek cümle: `Does varsa` / `fiil yalın.` (Fredoka 88, karaoke `Does`'tan; kart `yalın` sonunda tam ve sahne sonuna kadar sabit ≈ 2,7 sn). 15,34: yer imi simgesi + `Kaydet` (sarı hap). "gönder" (≈ 16,10): gönder simgesi (kâğıt uçak) + `Gönder` (Lexend 700 ≥ 50). Altyazı bandı karaoke | Kart çerçevesi kalemle çizilir (0,4 sn). Yer imi ve kâğıt uçak SVG, kalemle 0,4 sn'de çizilir. Hareket yalnız simgelerde; kart durgun. |
| kol a ile aynı · 4 çağrı (HyperFrames) ≈ 17,90–24,88 | 4 | **öğrenci** | **TR** `Bu sadece başlangıç.` · **TR** `Dersin tamamı YDS Publishing YouTube kanalında.` **[STANDART]** §3–§4 · **[02-04-S3]** (≈ 18,45–23,88) | `Bu sadece başlangıç.` Fredoka 700 64, y 470–590, sözcük zamanlı (`Bu`, `sadece`, `başlangıç` çapaları). "Dersin": ana ders kapağı kartı. "YDS": `@ydspublishing` sarı hap, y 1180–1260. "YouTube": hapın yanında `· YouTube`. Altyazı bandı öğrenci cümlesi, konuşma balonu biçiminde | Ana kapak 16:9 kart 900×506, x 60–960, y 620–1126 (standart §2 içerik sınırı x 960; S1 ve S2 ile aynı; jüri kaynak 5); kalemle çerçeve, içi 0,3 sn'de belirir. Balon biçimi ana ders sahne 06'daki öğrenci balonudur: ses değişimi gözle görünür. Figür yok. Son 1,0 sn durgun kuyruk. Döngü: ana kapaktaki karakter, kısanın ilk karesindeki (kapak A) karakterle aynıdır. |

Sahne sınırı = sonraki cümle başı − 0,55; son sahne = son söz + 1,0 sn (kol a ile aynı). Ekran metni sesten önce gelmez. İstisna
yalnız kapak A'dır (0. karede başlık ve `He goes.` kartı; kol a ile aynı istisna, kalıp §5 "Kapak = ilk kare").
`doesn't` sözcüğü söylenmez; "Olumsuzda" sözüyle aynı anda girer (Türkçe sözün İngilizce karşılığı; jüri bakacak).
Altyazı bandı (y 1400–1550, en çok 2 satır) söylenen bütün TR parçaları taşır; kapak PNG'sinde altyazı yok.

Klasör eşlemesi (kol b): `01-hyperframes-kanca` 0,00–3,48 (değişir) · `02-paperjs-deger` 3,48–12,43 · `03-hyperframes-kaydet`
12,43–17,69 · `04-hyperframes-cagri` 17,69–24,67. Klasör 02–04 kol a ile aynı süreyi ve iç zamanı taşır.

## 3. Kaynak eşlemesi ve ses önbelleği (kol b)

| Parça | Ana derste | Ses önbelleği |
|---|---|---|
| `Olumsuzda s nereye gider?` | tümce yok. `Olumsuzda` ve `s` cümle 7 parça 4'te ("Olumsuzda ve soruda does girer, s ona geçer.") | yok: yeni cümle |
| Cümle 2 (3 parça) | kol a ile aynı | VAR: kol a sentezi |
| Cümle 3 (2 parça) | kol a ile aynı | VAR: kol a sentezi |
| Cümle 4 (2 parça, öğrenci) | kol a ile aynı | VAR: kol a sentezi (kol a'da da `02-04-ydt-temel-s3` cümle 5 önbelleği) |

Önbellek anahtarı `[ses_metni, dil, önceki, sonraki, ses, model, tohum]` (`dijital-anlatim/araclar/iki-dilli/el.py` satır 88, 142).
`önceki` ve `sonraki` aynı cümlenin parçalarıdır (satır 138). Cümle 1'in değişmesi cümle 2–4 anahtarını değiştirmez.
Kol a'nın iki parçalı cümle 1 sesi kol b'de kullanılmaz.

## 4. Ses metni notları

- Yeni cümle 1, 1 parça, TR, 25 karakter. Seste İngilizce sözcük yok.
- Maliyet (tahmin): kol a oranıyla (184 karakter ≈ 0,90 TL) ≈ 0,12 TL.
- Tek harf `s` TR parçada geçer. Kol a cümle 2'de 2 kez geçti; Whisper "S" duydu, benzerlik 1,00 ve 0,96
  (`../../simple-present-temel-s3/ortak/anlatim/sentez.wav.rapor.json`). Kulakla dinlenir.
- Soru tonu: cümle `?` ile biter. Kulak kararı: `gider?` yükselen tonla duyulmalı. Düz tonla duyulursa başka tohum (`el.py` deneme
  döngüsü); metin değişmez.
- Kol a'nın Whisper riski (yanlış İngilizce cümleyi düzeltip duyma, kol a taslak §4) kol b'de yok: yanlış cümle seslendirilmez.
- Rakam, okunan kısaltma, hitap yok. "YDT" söylenmez.
- Yasak söz taraması (kol b yeni satırlar): standart §1 kural 4 ve kural 5 kapsamındaki sözler seste ve ekranda yok.

## 5. Süre (kol a ölçülmüş → kol b tahmini; gerçek süre sentez sonrası `zaman.json`)

Yöntem: yeni parça için aynı öğretmen sesinin (`gsJ9nrlXYbPztJxC4fwc`) ölçülmüş sözcük ikizleri; kontrol olarak ana dersin TR hece
hızı (4,03 hece/sn, kol a taslak §5). Cümle arası 0,55 sn. İlk söz 1,00 (kol a ile aynı). Değişmeyen cümleler kol a
`ortak/anlatim/sozcukler.json` ve `sureler.json` ölçümüdür.

| Sözcük | Ölçülmüş ikiz | sn |
|---|---|---|
| `Olumsuzda` | kol a cümle 2 ilk sözcük `Olumsuzda` 4,44–5,16 (cümle başı, aynı ses) | 0,72 |
| ara | kol a `Olumsuzda` → `ve` | 0,16 |
| `s` | kol a cümle 2 `s` 7,24–7,48 | 0,24 |
| ara | kol a cümle 2 sözcük arası (en sık değer) | 0,08 |
| `nereye` | ikiz yok; kol a cümle 2 `soruda` 5,80–6,20 (3 hece, cümle ortası, aynı ses) | 0,40 |
| ara | | 0,08 |
| `gider?` | ikiz yok; soru sonu. Kol a `nerede?` 0,80 (3 hece), `geçer.` 0,56 (2 hece, düz) | 0,64 |
| **Toplam (sözcük ikizi)** | | **2,32** |
| Kontrol: hece hızı | 10 hece ÷ 4,03 | 2,48 |

Tahmin büyük değeri alır: **2,48 sn**. Sözcük çapaları bu toplama ölçeklendi (× 1,069): `Olumsuzda` 1,00–1,77 · `s` 1,94–2,20 ·
`nereye` 2,29–2,72 · `gider?` 2,80–3,48.

| Cümle | Kol a ölçülmüş (sn) | Kol b tahmin (sn) | Fark |
|---|---|---|---|
| 1 kanca | 1,00–3,89 (2,89) | **1,00–3,48 (2,48)** | **−0,41** |
| 2 değer | 4,44–12,92 | 4,03–12,51 | 0 (kayma −0,41) |
| 3 kaydet | 13,39–18,10 | 12,98–17,69 | 0 |
| 4 çağrı | 18,65–24,08 | 18,24–23,67 | 0 |
| kuyruk | 24,08–25,08 | 23,67–24,67 | 0 |
| **Toplam** | **25,08** | **24,67** | **−0,41** |

| Klasör | Kol a (`zaman.json`) | Kol b | Not |
|---|---|---|---|
| `01-hyperframes-kanca` | 0,00–3,89 (117 + 12 kare) | 0,00–3,48 (≈ 104 + 12 kare) | içerik değişir |
| `02-paperjs-deger` | 3,89–12,84 (8,95) | 3,48–12,43 (8,95) | süre ve iç zaman aynı |
| `03-hyperframes-kaydet` | 12,84–18,10 (5,26) | 12,43–17,69 (5,26) | süre ve iç zaman aynı |
| `04-hyperframes-cagri` | 18,10–25,08 (6,98) | 17,69–24,67 (6,98) | süre ve iç zaman aynı |

Aralık: iyi durum (sözcük ikizi 2,32) → 24,51 sn · kötü durum (s1'de ölçülmemiş parçalar %11 uzun çıktı; 2,48 × 1,11 = 2,75)
→ 24,94 sn. Üç durumda da toplam 22–26 sn hedefinde ve 28 sn sınırının altında (pay ≥ 3,06 sn).

Standart §3 ile karşılaştırma: kanca 0–4 sn, ilk söz ≤ 1 sn ↔ kol b 0,00–3,48, ilk söz 1,00.
İlk 10 sn'de 3 hareket türü: kalem (hap çerçevesi, `‸`, `?`), kayma (`He` / `goes.` ayrılır, kart kayar, karakter çıkar), karaoke.

**DİKKAT:** kol a B planı (ilk söz 0,50, kuyruk 0,50) yalnız kol b'ye uygulanmaz. Uygulanırsa iki kola birlikte uygulanır; yoksa ilk
söz zamanı ikinci değişken olur (s1b emsali). Kol b kısaldığı için B planı gerekmez.
