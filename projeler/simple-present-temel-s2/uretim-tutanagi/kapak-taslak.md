# simple-present-temel-s2 · kapak taslağı — 3 sürüm (1080×1920 PNG)

Durum: TASLAK (istem P0202-S2-A, 15.11.2026). Görsel üretim ve render YOK.
Kural: `huni-v2-standart.md` §1 (kanal katmanı), §2 (yerleşim), §6 (A = kanca karesi, B ve C ayrı tasarım, en az biri karakter görseli, altyazı yok);
`dikey-senaryo-kalibi.md` §4 (başlık 2 satır, ≤ 4 sözcük, kalın kontur; küçük yazı, üçüncü satır, kalabalık, emoji yasak).
Dosyalar (v2 pilot adlandırması): A = sahne 01 karesi `kapak-a.png` (+ kopyası `kapak.png`) · B = durağan sahne `05-hyperframes-kapak-b` →
`kapak-b.png` · C = durağan sahne `06-hyperframes-kapak-c` → `kapak-c.png`.
Ana dersin kapak metni `GİDER = GOES` (karakter + minibüs). Bu üç kapak o metni ve o nesneyi yinelemez.
**S2-C (15.11) istem uyumu:** istem Huni v2 "karakter görseli kapak B ya da C'de kullanılır" der → `karakter.png` (sola işaret eden "buldum"
duruşu) A'dan C'ye geçer: C'de kartın sağında, karta işaret eder (C'nin figürsüz sapması kalkar). A'da karakterin yerine kalem çizgisi
figür (`kadro.ogrenci`, peeps-kit) takvime işaret eder. B değişmez. Klasörler: A `01-hyperframes-kanca`, B `06-hyperframes-kapak-b`,
C `07-hyperframes-kapak-c`. Bağlayıcı tarif: `../BRIEF-S2.md`.

## 1. Sürümler bir bakışta

| | A — kanca karesi (kod) | B — soru / merak | C — kural kartı |
|---|---|---|---|
| Başlık satır 1 | `USUALLY` | `ALWAYS VARSA` | `ÜÇ İFADE,` (S2-C: jüri dil 3 + kaynak 1a) |
| Başlık satır 2 | `= ALIŞKANLIK` (sarı hap) | `HANGİ ZAMAN?` | `TEK İŞARET` (S2-C: kaynak 1a) |
| Sözcük sayısı | 2 (+ `=` simgesi) | 4 | 4 |
| Can alıcı | `canAlici[2]` kısa kod: "usually, always, every day = tekrar eden iş sinyali" | `canAlici[2]` soru biçiminde: listedeki başka bir sözcük hangi zamanı ister? | `canAlici[2]` kural olarak: üç işaret → Simple Present |
| Görsel | karakter (`ortak/kapak/karakter.png`, sağda, sola işaret eder) + takvim yaprağı (solda, 5 gün kutusundan 4'ü tikli; S2-C, jüri dil 1) | soran öğrenci başı (`peeps-kit/ogrenci-bas.svg`, ana ders sahne 06) + konuşma balonu `always?` + büyük `?` | kart: `usually` · `always` · `every day` → `Simple Present`; köşede küçük takvim; figür yok |
| Tek vurgu (sarı) | `= ALIŞKANLIK` hapı | `?` işareti | `Simple Present` hapı |
| Kalem hareketi (yalnız A videoda) | takvimde 4 tik (5 kutudan), 0,30–0,80 sn | — (durağan) | — (durağan) |
| Seste karşılık | cümle 1 `Usually görünce hangi zaman?` + cümle 2 `Alışkanlık işareti.` | cümle 3 `Usually, always, every day: Simple Present.` (soru videoda cevaplanır) | cümle 3 aynı cümle (kartın birebir kaynağı) |
| Dosya | `kapak-a.png` + `kapak.png` | `kapak-b.png` | `kapak-c.png` |

Fark ilkesi: A bir kod söyler, B bir soru sorar ve cevabı videoya bırakır, C kuralın kendisini kart olarak verir. Üçünde başlık sözcükleri ayrıdır.
Ana kapakla fark: ana kapak Türkçe ek ↔ İngilizce ek köprüsüdür (`GİDER = GOES`); bu kısa zaman sözcüğü üzerinedir. Minibüs kullanılmaz.

## 2. Ortak öğeler (üç sürüm)

| Öğe | Değer | Kural |
|---|---|---|
| Zemin | açık: kâğıt `#f7f3ea`, mürekkep `#1b2440` | K19 |
| Kanal katmanı | y 280–350: logo (açık `ortak/logo/yds-publishing-lacivert.svg`, yükseklik 48, görünür sol kenar x 60) + `@ydspublishing` Lexend 700 42 px, mürekkep | standart §1 kural 1, §2; pilot `02-04-ydt-temel-s2/BRIEF-S2.md` ile aynı piksel |
| Künye | y 360–450: `Simple Present` (Fredoka 700, x 60) + rozet `YDT · BASIC` (hap; dolgu `#ffe066`, yazı `#1b2440`) | standart §2; rozet pilotla aynı (İngilizce ders → şablonda Türkçe yok, ana BRIEF §0 madde 5) |
| Başlık | y 460–800; iki satır aynı boy; 900 px genişliğe sığan en büyük değer, üst sınır 190 px; kalın kontur; motor ölçer, elle boy yazılmaz | kalıp §4; pilot |
| Görsel bandı | y 820–1380, x 60–960 | standart §2 içerik bölgesi |
| Alt | y 1400–1920 boş (altyazı yok, platform arayüzü) | standart §2, §6 |
| Yazı tabanı | etiket ve kart yazısı en az 64 px | dikey v2 |
| Yasak | üçüncü başlık satırı, emoji, kalabalık sahne, rakam (sayı sözcükle: `ÜÇ`, `TEK`), "Tam ders", süre | kalıp §4; standart §1 kural 4–5 |

## 3. Sürüm A — kanca karesi (video ilk karesi)

```
0 ─────── 280   üst boş (platform arayüzü)
280 ───── 450   kanal katmanı · künye: Simple Present  [YDT · BASIC]
460 ───── 800   başlık: USUALLY / = ALIŞKANLIK (sarı hap)
820 ──── 1380   solda takvim yaprağı (5 gün kutusu, 4'ü tikli) · sağda karakter (sola, takvime işaret eder)
1400 ─── 1920   boş (kapak PNG'de altyazı yok)
```

- Kod okunuşu: "usually = alışkanlık". Video önce soruyu sorar (`Usually görünce hangi zaman?`), sonra `Alışkanlık işareti.` der, en son `Simple Present`'i verir.
- Kapak karesi: t 0,90 (kare 27): başlık tam, tikler bitmiş, ses henüz başlamamış (ilk söz 1,00), altyazı katmanı gizli (pilot S1-KAPAK-A yöntemi).
- Kaba boy: satır 2 `= ALIŞKANLIK` 12 karakter → ≈ 136 px (0,55 em/karakter, ölçülmedi). Satır 1 aynı boya iner (iki satır aynı boy).
- Karakter ana kapakta da var (`karakter.png`). Tanıdıklık bilinçlidir: kısa ile ana ders aynı yüzü taşır. Ayrım nesne ve başlıkla yapılır.

## 4. Sürüm B — soru / merak

```
0 ─────── 280   üst boş
280 ───── 450   kanal katmanı · künye
460 ───── 800   başlık: ALWAYS VARSA / HANGİ ZAMAN?   (mürekkep, hapsız)
820 ──── 1380   solda öğrenci başı (kalem çizgisi) + el çizimi konuşma balonu: always? (Fredoka 72) · sağda büyük sarı ?
1400 ─── 1920   boş
```

- Başlık sesin metnini tekrarlamaz: ses `usually` ile sorar, B `always` ile sorar. Cevap videoda: cümle 3 `Usually, always, every day: Simple Present.`
- Kalıp uyumu: v2 pilot B (`TODAY VARSA` / `HANGİ ZAMAN?`) ile aynı soru kalıbı; seri tanınır.
- Figür kaynağı: öğrenci başı ana ders sahne 06'daki soran öğrencidir (kadın, gözlüklü; `kadro.ogrenci`). Kısanın çağrı sesi de öğrencidir.
- `HANGİ` İ noktalı; `ALWAYS` İngilizce, noktasız I sorunu yok. Kaba boy: `ALWAYS VARSA` 12 karakter → ≈ 136 px.

## 5. Sürüm C — kural kartı

```
0 ─────── 280   üst boş
280 ───── 450   kanal katmanı · künye
460 ───── 800   başlık: ÜÇ İFADE, / TEK İŞARET   (mürekkep, hapsız; S2-C)
820 ──── 1380   el çizimi kart: üç ifade kutusu alt alta  usually · always · every day  (Fredoka 72, mürekkep)
                kalem oku → Simple Present (sarı hap, Fredoka 80) · kart köşesinde küçük takvim
1400 ─── 1920   boş
```

- Kart, kaydet sahnesindeki kural özetinin görsel biçimidir; metin aynı sözcüklerdir (cümle 3).
- **DİKKAT:** kalıp §4 "Görsel: figür + nesne" maddesinden sapma (figür yok). Gerekçe: kural kartına figür eklenirse sahne bandı kalabalıklaşır.
  Emsal: 02-04 S2 kapak C figürsüz, iki jüri sapmayı kabul etti ("istem tanımı gerekçe; kalabalık yasağı ile uyumlu").
- En uzun kart satırı `every day` 9 karakter; Fredoka 72'de ≈ 360 px (kaba). Ok + hap 900 px içine sığar.

## 6. `senaryo.json` alanları (paket kurulunca)

Paket bir anda tek kapak taşır; video ilk karesi A. B ve C durağan sahne 05 ve 06'nın istemine girer (yeni şema alanı açılmaz).

```json
"giris": {
  "logo": "varlik/logo/yds-publishing.svg",
  "satir1": "USUALLY",
  "satir2": "= ALIŞKANLIK",
  "rozetler": ["YDT · BASIC"],
  "sahne": [
    {"ad": "calendar", "x": 26, "y": 60, "olcek": 0.45},
    {"gorsel": "ortak/kapak/karakter.png", "x": 70, "y": 58, "olcek": 0.8}
  ]
},
"meta": {
  "kapak": {
    "satir1": "USUALLY",
    "satir2": "= ALIŞKANLIK",
    "canAlici": "usually, always, every day = tekrar eden iş sinyali"
  }
}
```

| Sürüm | `satir1` | `satir2` | `meta.kapak.canAlici` | sahne öğeleri |
|---|---|---|---|---|
| B | `ALWAYS VARSA` | `HANGİ ZAMAN?` | `usually, always, every day = tekrar eden iş sinyali` (`canAlici[2]`) | `ogrenci-bas` (peeps-kit), balon `always?`, `question` (sarı) |
| C | `ÜÇ İFADE,` | `TEK İŞARET` | aynı (`canAlici[2]`) | kart sahne 06 kodunda çizilir; küçük `calendar` |

- `canAlici` tek kaynak: üç sürümde `canAlici[2]` (02-04 jüri kaynak 4a dersi: iki yerde farklı kaynak yazılmaz).
- İkon adları (`calendar`, `question`) öneridir: takvim ana ders `tabler/calendar.svg`, gün kutuları ana ders sahne 04 el çizimi.
  `karakter.png` raster çıkartmadır; HyperFrames sahnesine görsel olarak girer (pilot B'de aynı yol). `"gorsel"` alan adı öneridir;
  şema bunu tanımıyorsa sahne kodu istemi doğrudan dosya yolu verir.
- x, y, olcek başlangıç önerisidir; sahne kodu yazılırken kontak sayfasında düzeltilir.

## 7. Karar notu

- İlk kare = kapak A: başlık 0. karede tam (kalıp §5, standart §6). TikTok ve Instagram'da kapak seçilmezse akışta ilk kare görünür;
  YouTube Shorts kapağı Studio'da seçilir.
- B ve C platform kapağı olarak yüklenir. Video ilk karesi de B/C olsun istenirse yalnız sahne 01 yeniden koşar (≈ 2,7 sn).
- Kullanılmayan seçenekler: `HER GÜN` / `= EVERY DAY` (köprü kapağı; ana kapağın `GİDER = GOES` kalıbına çok yakın) ·
  `USUALLY` / `= SIMPLE PRESENT` (satır 2 14 karakter, boy küçülür; ayrıca kancanın cevabını tam verir).
