# simple-present-temel-s1 · kapak taslağı — 3 sürüm (1080×1920 PNG) · huni v2

Durum: TASLAK (istem P0202-S1-A, 15.11.2026). Görsel üretim ve render YOK.
Kural: `huni-v2-standart.md` §1 (kanal katmanı), §2 (yerleşim), §6 (A = kanca karesi, B ve C ayrı tasarım, en az biri karakter);
`dikey-senaryo-kalibi.md` §4 (başlık 2 satır, en çok 4 sözcük; yasaklar); `kapak-standardi.md` §2–§3 (karakter düzeni, kapak metni).
Ana dersin kapağı `GİDER = GOES` (+ küçük satır `he · she · it → -s`). Üç kısa kapağı bu metni yinelemez.

## 1. Sürümler bir bakışta

| | A — kanca karesi | B — soru / merak | C — karşıt çift |
|---|---|---|---|
| Başlık satır 1 | `GO mu,` | `FİİLE -S` | `HE GOES` (`ES` sarı hap) |
| Başlık satır 2 | `GOES mu?` (sarı hap) | `HANGİ ÖZNEYLE?` (siyah kutuda krem) | `I GO` |
| Sözcük sayısı | 4 (GO · mu · GOES · mu) | 4 (FİİLE · -S · HANGİ · ÖZNEYLE) | 4 (HE · GOES · I · GO) |
| Can alıcı | `canAlici[0]` "gider = goes", soru biçiminde: tek Türkçe söz, iki İngilizce aday | `canAlici[3]` "he, she, it fiile s alır; I, you, we, they almaz", soru biçiminde | `canAlici[3]`, örnek biçiminde: bir s'li, bir s'siz özne |
| Görsel | kalem çizimi genç figür (`open-peeps/standing-2.svg`) + otobüs (`coco/bus.svg`) | karakter `../../simple-present-temel/ortak/kapak/karakter.png` (işaret eden genç) + otobüs `nesne.png` | otobüs (`coco/bus.svg`, kalem) `HE GOES` satırının altında; figür yok |
| Zemin | kâğıt `#f7f3ea`, mürekkep `#1b2440` (video ailesi) | sarı `#fece00`, yazı `#141414` (kapak standardı ailesi) | kâğıt `#f7f3ea`, mürekkep `#1b2440` |
| Tek vurgu | `GOES mu?` hapı | `HANGİ ÖZNEYLE?` kutusu | `ES` hapı |
| Rozet | `YDT · BASIC` | `YDT · BASIC` | `YDT · BASIC` |
| Seste karşılık | cümle 1 `Kardeşim gider: go mu, goes mu?` | cümle 2 parça 2–3 (he, she, it ↔ I, you, we, they) | cümle 2 parça 1 (`goes`) + parça 3 (`I … ile gelmez`) |
| Dosya | `kapak-a.png` + kopyası `kapak.png` (sahne 01 karesi) | `kapak-b.png` (durağan sahne `06-hyperframes-kapak-b`) | `kapak-c.png` (durağan sahne `07-hyperframes-kapak-c`) |

Fark ilkesi: A videonun sorusunu sorar ve ilk karede durur. B başka bir soru sorar; cevabı videoya bırakır. C cevabın kendisini bir çift olarak
gösterir, ama kuralın tamamını vermez (she, it, you, we, they kapakta yok; `kapak-standardi.md` §3).

## 2. Ortak öğeler (üç sürüm)

| Öğe | Değer | Kural |
|---|---|---|
| Kanal katmanı | y 280–350, x 60: yazı logosu (yükseklik ≈ 48 px) + `@ydspublishing` (Lexend 700, 42 px); A ve C'de lacivert logo, B'de siyah | standart §1 kural 1, §2 |
| Künye satırı | y 360–450: yalnız rozet `YDT · BASIC` (hap, Lexend 700 ≈ 26 px); konu adı yok | standart §2; kapak standardı §3 (konu adı büyük yazı olmaz) |
| Başlık | Fredoka 700, iki satır aynı boy; 900 px'e (x 60–960) sığan en büyük değer, üst sınır 190 px; motor ölçer | kalıp §4, standart §2 (sağ 960–1080 platform arayüzü) |
| Başlık bandı | y 470–900 (B ve C'de 470–1000'e kadar uzayabilir) | standart §2 içerik bandı 460–1380 |
| Görsel bandı | y 920–1380 | standart §2 |
| Hap (kâğıt zemin) | dolgu `#ffe066` (`vurguDolgu`), yazı `#1b2440` (`pilMetin`) | S2 `kapak-taslak.md` §2; `kalem/.claude/docs/sozlesme.md` (14.11, 02-04 s12) |
| Altyazı | yok; y 1400–1550 boş | standart §6 |
| Alt boş | y 1570–1920 yalnız zemin | standart §2 |
| Büyük harf | Türkçe kural (`HANGİ` noktalı İ, `ALIR` noktasız I); `mu` soru eki küçük harf | kapak standardı §3 |
| Yasak | üçüncü satır, küçük yazı (< 64 px içerik yazısı), kalabalık sahne, emoji, süre rozeti | kalıp §4, standart §1 kural 5 |

## 3. Sürüm A — kanca karesi

```
0 ─────── 280   boş zemin
280 ───── 350   kanal katmanı: logo + @ydspublishing
360 ───── 450   rozet YDT · BASIC
470 ───── 900   başlık: GO mu, / GOES mu? (satır 2 sarı hap)
920 ──── 1380   genç figür (ayakta, sola dönük) · sağında otobüs (sola gidiyor)
1400 ─── 1550   altyazı bandı (kapak PNG'sinde boş)
1570 ─── 1920   boş zemin
```

- Kapak = videonun ilk karesi (kalıp §5; standart §6 "A = kanca karesi"). Kapak PNG karesi t 0,90 (kare 27): başlık tam, kalem hareketi bitmiş,
  ilk söz (1,00) ve altyazı henüz yok.
- Kalem hareketi: satır 2'deki `?` 0,3–0,8 sn'de kalemle çizilir. Başka hareket yok.
- Figür ve otobüs etiketsizdir: ekran metni sesten önce gelmez; tek istisna başlık (S2 emsali). `Kardeşim gider:` yazısı söylendikten sonra gelir.
- Kaba boy: `GOES mu?` 8 karakter → 0,55 em/karakter ile ≈ 190 px'e sığar (836 px + hap payı; ölçülmedi).
- Neden bu başlık: köprü biçiminin kendisi (bir Türkçe söz → iki İngilizce aday). Akışta duran izleyici ikisinden birini seçer, cevabı videoda arar.

## 4. Sürüm B — soru / merak (karakterli)

```
0 ─────── 280   boş zemin (sarı)
280 ───── 350   kanal katmanı (siyah logo + @ydspublishing)
360 ───── 450   rozet YDT · BASIC (siyah çerçeveli hap)
470 ───── 900   başlık: FİİLE -S / HANGİ ÖZNEYLE? (satır 2 siyah kutuda krem; jüri K1)
920 ──── 1380   sağda karakter (bel üstü, krem daire arkası, sola işaret) · işaret ettiği yerde küçük otobüs
1400 ─── 1920   boş zemin
```

- Karakter: `karakter.png` (896×1200, şeffaf; iri kıvırcık saç, yuvarlak gözlük, sola işaret eden "buldum" ifadesi; `KAYNAK.json`).
  10 px krem çıkartma kenarı (dört yön `drop-shadow`) ve krem daire: sarı saç sarı zeminde kaybolmaz (kapak standardı §2).
- Nesne: `nesne.png` (yandan minibüs, 1200×896); karakterin işaret ettiği yerde, küçük (≈ 360 px en). Otobüs videodaki örnek cümlenin
  nesnesidir (`My brother goes to school by bus.`).
- Kaba boy: `HANGİ ÖZNEYLE?` 14 karakter → ≈ 117 px (ölçülmedi); boy küçük kalırsa `-S HANGİ` / `ÖZNEYLE?` (3 sözcük; jüri K1). Glif: İ ve Ö Fredoka latin-ext'te var (kapak standardı §5 madde 3 denetlenir).
- B videonun sesindeki soruyu yinelemez. Gerekçe: A zaten o soruyu taşır; B ikinci bir giriş kapısı açar ("fiile -s hangi özneyle?"). -s fiile bağlanır, özneye değil (jüri K1: "hangi özne -s alır" çoğul isim özneyi çağırır).
- Cevap videoda: cümle 2 parça 2 (`Özne he, she ya da it olunca fiile s gelir.`) ve parça 3 (`I, you, we, they ile gelmez.`).
- **DİKKAT:** karakter erkek; videodaki öğrenci sesi kadın (`kadro.ogrenci`). Karakter kapakta konuşmaz, videoda konuşan figür olmaz (K22).
- Zemin seçimi: sarı, ana dersin kapağıyla aynı aile. A ve C kâğıt zeminde kalır; üç sürüm akışta iki ayrı görünüm verir. Başlık ve
  düzen ana kapaktan farklıdır (dikey; başlık üstte, görsel altta).

## 5. Sürüm C — karşıt çift

```
0 ─────── 280   boş zemin
280 ───── 350   kanal katmanı
360 ───── 450   rozet YDT · BASIC
470 ──── 1000   başlık: HE GO[ES] / I GO   (ES sarı hap; satır 2 mürekkep)
1020 ─── 1380   otobüs (kalem çizimi), HE GOES satırının yönünde
1400 ─── 1920   boş zemin
```

- Çift, ana ders cümle 7'nin iki ucudur: `he` → s var · `I` → s yok. `ES` vurgusu ana derste `go-es` görseliyle aynı.
- Satır 2 vurgusuz: karşıtlığı satır 1'deki `ES` hapı kurar; ikinci renk (kırmızı çizgi) eklenmez.
- Kaba boy: `HE GOES` 7 karakter → 190 px üst sınırına takılır (731 px; ölçülmedi).
- Kuralın tamamı kapakta yok: she, it, you, we, they videoda gelir (kapak standardı §3 "kural cümlesinin tamamını vermez").
- **DİKKAT:** kalıp §4 "Görsel: figür + nesne" maddesinden sapma (figür yok). Gerekçe: başlık iki özne taşır; figür eklenirse "he"
  ile "I"nın hangisi olduğu belirsizleşir. S2 kapak C ile aynı sapma; karar şefte (`S1-A-RAPOR.md` açık nokta 4).

## 6. `senaryo.json` alanları (önerilen; sahne istemine girer)

```json
"giris": {
  "logo": "varlik/logo/yds-publishing.svg",
  "satir1": "GO mu,",
  "satir2": "GOES mu?",
  "rozetler": ["YDT · BASIC"],
  "sahne": [
    {"figur": "open-peeps/standing-2", "x": 34, "y": 60, "olcek": 0.8},
    {"ad": "bus", "x": 70, "y": 64, "olcek": 0.45}
  ]
},
"meta": {
  "kapak": {
    "satir1": "GO mu,",
    "satir2": "GOES mu?",
    "canAlici": "Türkçedeki geniş zaman eki = İngilizcedeki s: gider = goes"
  }
}
```

| Sürüm | `satir1` | `satir2` | `meta.kapak.canAlici` | Görsel |
|---|---|---|---|---|
| B | `FİİLE -S` | `HANGİ ÖZNEYLE?` | `he, she, it fiile s alır; I, you, we, they almaz` (`canAlici[3]`) | `karakter.png` + `nesne.png`, sarı zemin; durağan sahne 06 |
| C | `HE GOES` | `I GO` | `he, she, it fiile s alır; I, you, we, they almaz` (`canAlici[3]`) | `coco/bus.svg` kalem; durağan sahne 07 |

- `meta.kapak.canAlici` alanına `canAlici` listesinden birebir madde yazılır.
- x, y, olcek başlangıç önerisidir; sahne kodu yazılırken kontak sayfasında düzeltilir.
- Eski paketin `giris` alanı (`GİDER` / `= GOES`, rozet `YDT · BASIC` + `GRAMMAR`) v2'de değişir: ana kapakla aynı başlık kalkar, rozet
  emsal 02-04-ydt-temel-s1 ile aynı `YDT · BASIC` olur (istem P0202-S1-C "Rozet emsaldeki gibi"; standart §2 örneği `YDT · TEMEL`).

## 7. Karar notu

- Videonun ilk karesi A'dır. B ve C platform kapağı olarak yüklenir (YouTube Shorts kapağı Studio'da elle; huni-plan §5).
- Kullanılmayan seçenek: A için `GİDER` / `= GOES?` (ana kapağın soru biçimi). Neden: ana kapağı neredeyse aynen yineler (istem kuralı).
- Kullanılmayan seçenek: B için `I GOES` / `DENİR Mİ?`. Neden: yanlış–doğru biçimi bu dersin ek kısalarına ayrıldı (standart §5).
