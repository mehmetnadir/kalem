# 02-04-ydt-temel-s2 · kapak taslağı — 3 sürüm (1080×1920 PNG)

Durum: TASLAK (istem S2-A, 15.11.2026). Görsel üretim ve render YOK.
Kural: `dijital-anlatim/.claude/docs/dikey-senaryo-kalibi.md` §4 ve "Uygulandı (04.11)" bant tablosu. Emsal: S1 `kapak-taslak.md` (S1-C düzeltmesi 4).
Kapak = Shorts'un ilk karesi (kalıp §5). Üç sürüm yalnız sahne 01'de ayrışır; sahne 02 ve 03 ortaktır.
Düzeltme (istem S2-C, 15.11): jüri kaynak 4a işlendi (C can alıcısı tek kaynak `canAlici[0]`); çok sürüm kararı (Nadir 15.11) dosya
adlarına işlendi: A = sahne 01 karesi `kapak-a.png` (+ `kapak.png` kopyası), B = durağan sahne `05-hyperframes-kapak-b` → `kapak-b.png`,
C = durağan sahne `06-hyperframes-kapak-c` → `kapak-c.png`. Ayrıntı `S2-duzeltme.md`.

## 1. Sürümler bir bakışta

| | A — can alıcı kod | B — soru / merak | C — karşıt çift |
|---|---|---|---|
| Başlık satır 1 | `GENEL` | `TODAY VARSA` | `AYNI FİİL,` |
| Başlık satır 2 | `≠ ŞU AN` (sarı hap) | `HANGİ ZAMAN?` | `İKİ ZAMAN` |
| Sözcük sayısı | 3 (GENEL · ŞU · AN) | 4 | 4 |
| Can alıcı | `canAlici[0]` ilk sorusu, kod olarak: genel → *wears*, şu an → *is wearing* | `canAlici[3]` soru biçiminde: *today* hangi zamanı ister? | `canAlici[0]` ilk sorusu, örnek olarak: iki kart genel ↔ şu an (S2-C, jüri kaynak 4a) |
| Görsel | askıda mont (sol) · işaret eden öğretmen (orta) · askıda pembe tişört (sağ); etiket `wears` / `is wearing` | düşünen öğretmen; elinde `today` yazan takvim yaprağı; yanında büyük sarı `?` | iki cümle kartı üst üste; kart köşesinde küçük mont / tişört; figür yok |
| Tek vurgu (sarı) | `≠ ŞU AN` hapı | `?` işareti | kart 2'de `is wearing` |
| Kalem hareketi 0,3–0,8 sn | `≠` işareti hapın içinde kalemle | `?` kalemle | `is wearing` altına sarı el altçizgisi |
| Seste karşılık | cümle 1 "Genel mi, şu an mı?" + kart etiketleri | cümle 2 parça 4 "Today iki zamanda da geçebilir; farkı anlam yapar." (S2-C) | cümle 2'nin iki EN parçası |
| Dosya | `kapak-a.png` + kopyası `kapak.png` (sahne 01 karesi) | `kapak-b.png` (sahne 05, durağan) | `kapak-c.png` (sahne 06, durağan) |

Fark ilkesi: A bir kural kodu söyler, B bir soru sorar ve cevabı videoya bırakır, C örneğin kendisini gösterir. Üçünde de başlık ayrı sözcüklerdir.

## 2. Ortak öğeler (üç sürüm)

| Öğe | Değer | Kural (§4) |
|---|---|---|
| Zemin | açık: kâğıt `#f7f3ea`, mürekkep `#1b2440` | K19 |
| Hap | dolgu `#ffe066` (`RENK.vurguDolgu`), yazı `#1b2440` (`RENK.pilMetin`); kaynak S1 `ortak/kunye.js` satır 11–12, 154–155 | S1-C düzeltme 4 |
| Rozet | `YDT · BASIC` (tek rozet; S1 ile aynı) | ders + seviye |
| Logo | `dijital-anlatim/varlik/logo/yds-publishing.svg`, alt sol (y ≈ 1478) | gerçek marka SVG'si |
| Başlık boyu | iki satır aynı boy; 952 px genişliğe (1080 − 2 × 64) sığan en büyük değer, üst sınır 190 px; motor ölçer, elle boy yazılmaz | büyük, 2 satır, kalın kontur |
| Yazı tabanı | etiket ve kart yazısı en az 64 px (dikey v2) | küçük yazı yasak |
| Kapak karesi | t 0,90 (kare 27): başlık tam, kalem hareketi bitmiş, soru satırı ve altyazı henüz yok | §5 "Kapak = ilk kare" |
| Yasak | üçüncü başlık satırı, emoji, kalabalık sahne | §4 |

Kapak karesi S1'den farklıdır (S1: t 1,97, altyazı dilimi ile). Gerekçe: üç sürümün kapak PNG'si aynı anda karşılaştırılır; altyazı dilimi
üç sürümde aynı olduğu için ayırt edici değildir ve kalabalık ekler. Sahne 01 boyu 2,44 sn (tahmin); uçuş son 0,6 sn'de.

## 3. Sürüm A — can alıcı kod (S1 kalıbı)

S1 `YAŞIYORUM` / `= İKİ ZAMAN` kalıbı: satır 1 tek anahtar sözcük, satır 2 simgeli sarı hap, sahnede iki nesne ve iki etiket.

```
0 ─────── 288   HUD: rozet YDT · BASIC
288 ───── 768   başlık: GENEL / ≠ ŞU AN (hap)   (y 346–768)
864 ──── 1344   askıda mont · öğretmen (işaret pozu) · askıda pembe tişört
                etiketler: mont altında wears · tişört altında is wearing (Caveat ≥ 72)
1344 ─── 1536   boş (altyazı bandı) · logo sol alt y ≈ 1478
1536 ─── 1920   platform arayüzü: BOŞ
```

- Kısa kod: başlık + etiketler birlikte okunur → "genel durum: *wears* · şu an: *is wearing*" (`canAlici[1]`–`[2]`'nin 1. fark dilimi).
- Kaba boy: satır 2 `≠ ŞU AN` 7 karakter → üst sınır 190 px'e takılır (0,55 em/karakter, ölçülmedi).

## 4. Sürüm B — soru / merak

```
0 ─────── 288   HUD: rozet YDT · BASIC
288 ───── 768   başlık: TODAY VARSA / HANGİ ZAMAN?   (y 346–768)
864 ──── 1344   öğretmen (düşünme pozu, el çenede) · elinde takvim yaprağı "today" · sağda büyük sarı ?
1344 ─── 1536   boş (altyazı bandı) · logo sol alt y ≈ 1478
1536 ─── 1920   platform arayüzü: BOŞ
```

- Soru videoda cevaplanır: cümle 2 parça 4 "Today iki zamanda da geçebilir; farkı anlam yapar." + cümle 1 karar sorusu "Genel mi, şu an mı?"
  + cümle 2 sonu "Konuşma anı: şimdiki zaman." (S2-C sırası).
- Başlıkta `TODAY` İngilizce yazılır (noktasız I yok; sorun yok). `HANGİ` Türkçe büyük harf: İ noktalı.
- Kaba boy: en uzun satır `HANGİ ZAMAN?` 12 karakter → ≈ 144 px (ölçülmedi). A'dan küçük; satır 2 hapsız, tek sarı `?`.
- B, sesteki ilk soru ile aynı değildir. Gerekçe: başlık sesin metnini tekrarlarsa ekran metni sesten önce gelir; B başka bir soru sorar.

## 5. Sürüm C — karşıt çift (iki cümle üst üste, tek vurgu)

```
0 ─────── 288   HUD: rozet YDT · BASIC
288 ───── 768   başlık: AYNI FİİL, / İKİ ZAMAN   (mürekkep, hap yok)
864 ──── 1344   kart 1: She wears her coat / in the winter.      (köşede küçük mont)
                kart 2: She is wearing her / pink T-shirt today. (köşede küçük tişört; is wearing sarı altçizgi)
1344 ─── 1536   boş (altyazı bandı) · logo sol alt y ≈ 1478
1536 ─── 1920   platform arayüzü: BOŞ
```

- Cümle kırılımı ana ders `sahne-03.js` `SAT` dizisi ile aynı. En uzun satır `pink T-shirt today.` 19 karakter; Fredoka 72'de ≈ 752 px (kaba).
- Tek vurgu `is wearing`: başlık "iki zaman" der; göz *wears* ile *is wearing* farkına gider. `today` vurgulanmaz: B sürümü *today* üzerinedir; C ayrışık kalır.
- Başlık hapsız: kartta tek sarı öğe kalsın. Rozet hapı künye öğesidir, vurgu sayılmaz.
- **DİKKAT:** kalıp §4 "Görsel: figür + nesne" maddesinden sapma. İstem C'yi "iki cümle üst üste" tanımlar; figür eklenirse sahne bandı kalabalıklaşır. Karar şefte (`S2-A-RAPOR.md` açık nokta).

## 6. `senaryo.json` alanları (huni-plan §2 veri kaynağı)

Paket bir anda tek kapak taşır; varsayılan A. B ve C aynı alanlarla, sahne 01'in ayrı koşusunda kullanılır (yeni şema alanı açılmaz).
S2-C (çok sürüm, Nadir 15.11): `senaryo.json` yalnız A'yı taşır. B ve C sahne 01'in ayrı koşusu DEĞİL, durağan kare sahneleri 05 ve 06'dır;
aşağıdaki B/C değerleri o sahnelerin istemine (`istem/sahne/D-05-…`, `D-06-…`) girer.

```json
"giris": {
  "logo": "varlik/logo/yds-publishing.svg",
  "satir1": "GENEL",
  "satir2": "≠ ŞU AN",
  "rozetler": ["YDT · BASIC"],
  "sahne": [
    {"ad": "coat", "x": 24, "y": 58, "olcek": 0.45},
    {"figur": "ogretmen", "x": 50, "y": 58, "olcek": 0.8},
    {"ad": "t-shirt", "x": 76, "y": 60, "olcek": 0.4}
  ]
},
"meta": {
  "kapak": {
    "satir1": "GENEL",
    "satir2": "≠ ŞU AN",
    "canAlici": "Önce anlama bak: genel mi, şu an mı? Kalıcı mı, geçici mi? Tarife mi, plan mı?"
  }
}
```

| Sürüm | `satir1` | `satir2` | `meta.kapak.canAlici` | `giris.sahne` |
|---|---|---|---|---|
| B | `TODAY VARSA` | `HANGİ ZAMAN?` | `today iki zamanda da geçer; farkı anlam yapar` (`canAlici[3]`) | `{"figur": "ogretmen", "x": 40, …}`, `{"ad": "calendar", …}`, `{"ad": "question", …}` |
| C | `AYNI FİİL,` | `İKİ ZAMAN` | `Önce anlama bak: genel mi, şu an mı? Kalıcı mı, geçici mi? Tarife mi, plan mı?` (`canAlici[0]`; S2-C, jüri kaynak 4a: `canAlici[2]` geçici durum ve planlanmış gelecek taşır, Shorts göstermez) | figür yok; iki kart sahne 06 kodunda çizilir |

- İkon adları (`coat`, `t-shirt`, `calendar`, `question`) öneridir. Mont ve tişört için ana ders `sahne-03.js` MONT / TISORT kalem dizileri
  hazırdır; HyperFrames'e taşınması sahne kodu istemindedir. Katalogda yoksa Open Doodles / Tabler taranır (ana ders §6 kuralı).
- x, y, olcek başlangıç önerisidir; sahne kodu yazılırken kontak sayfasında düzeltilir.
- `meta.kapak.canAlici` alanına `canAlici` listesinden birebir madde yazılır. A için `canAlici[0]` (kod onun ilk sorusudur).

## 7. Karar notu

- İlk kare = kapak: başlık 0. karede tam. Gerekçe: TikTok ve Instagram'da kapak seçilmezse akışta ilk kare görünür; YouTube Shorts kapağı
  yalnız Studio'da seçilir (huni-plan §5).
- Videonun ilk karesi A (S1 kalıbı, seri kimliği). B ve C platform kapağı olarak yüklenir; ilk kareleri de B/C olsun istenirse yalnız sahne 01
  yeniden koşar (≈ 2,4 sn, 73 kare). Önerim: önce PNG, video çeşidi ölçüm sonucuna göre.
- S2-C: B ve C PNG'leri durağan sahne 05 ve 06'dan gelir (S1 sahne 05/06 kalıbı). Ölçülen sahne 01 boyu 2,84 sn (85 içerik karesi).
- Kullanılmayan seçenek: A için `TODAY` / `= İKİ ZAMAN` (S1 kalıbının harfiyen kopyası). Neden: video *today*'i iki zamanda göstermez, yalnız söyler;
  kapak gösterilmeyen bir eşleşmeyi vaat eder. *today* sorusu B'de soru olarak kalır, video ona cevap verir.
