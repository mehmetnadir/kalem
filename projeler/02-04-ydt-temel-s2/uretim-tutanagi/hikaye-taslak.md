# 02-04-ydt-temel-s2 · hikâye karesi taslağı — 2 sürüm (1080×1920 durağan PNG)

Durum: TASLAK (istem S2-A, 15.11.2026). Görsel üretim ve render YOK.
Biçim: yalnız durağan PNG (istem). Ses yok, süre yazmaz. MP4 sürümü bu istemde yok.
Kaynak: huni-plan §2 (veri: `senaryo.json` → `meta.kapak.satir1`, `satir2`, `meta.canAlici`), §5 (platform), §7 (dil). Emsal: S1 `hikaye-taslak.md`.
Düzeltme (istem S2-C, 15.11): jüri dil 1 + kaynak 1 (B kökü `Look!`), dil 2 (`geçebilir`), kaynak 4b (dil gerekçesi) işlendi; `S2-duzeltme.md`.
Dosyalar (çok sürüm, Nadir 15.11): A = sahne `04-hyperframes-hikaye` → `hikaye-a.png` (+ `hikaye.png` kopyası); B = sahne
`07-hyperframes-hikaye-b` → `hikaye-b.png`.

## 1. Platform (S1 §1 ile aynı)

| Platform | Hikâye | Bağlantı |
|---|---|---|
| Instagram | API ile (`media_type=STORIES`) ya da elle | API ile yok. Elle paylaşımda bağlantı çıkartması (uygulama özelliği, doğrulanmadı) |
| TikTok | yalnız mobil uygulama, elle | açıklamada tıklanmaz |
| YouTube | yok (özellik kapandı) | — |

## 2. Dil kararı (huni-plan §7)

**Seçim:** metin öğretmene ve YDT öğrencisine birlikte seslenir; veli dili yok (D-0278, istem S2-A). Kare sen/siz hitabı taşımaz.
**Not:** srv21'deki `kovan-defteri/kararlar.jsonl` kopyası D-0096'da biter; D-0278 metnini burada okuyamadım. Karar istemde geçti, sicilde
doğrulanmadı.

Gerekçe tablosu (S2-C, jüri kaynak 4b; S1 `hikaye-taslak.md` §2'den alındı):

| Gerekçe | Kanıt |
|---|---|
| YDT kitlesi 17–18 yaş, 15 yaş yasağının dışında; sosyal ağı doğrudan kullanır | huni-plan §7 "Kitle Etkisi" |
| §7 veli/öğretmen önerisinin kaynağı 9. sınıf (14 yaş) Maarif kitlesidir | huni-plan §7 + karar sorusu 3 ("14 yaşındaki 9. sınıf kitlesi") |
| Kare sen/siz hitabı taşımaz; öğrenci okur, öğretmen sınıfa iletir. Öğretmen satırı tek ve kısa | §3, §4 çağrı satırı |
| Seçim geri alınır, yalnız metin değişir | S1 §2 ile aynı |

Bu gerekçe açıklama taslağındaki "(öğretmen + YDT öğrencisi)" etiketlerinin de dayanağıdır.

## 3. Sürüm A — bilgi kartı

Amaç: Shorts'un öğrettiği şeyi tek karede vermek. Kaydedilip geri dönülecek kart.

| Bant (y px) | Öğe | Metin | Biçim |
|---|---|---|---|
| 0–288 HUD | rozet + ders adı | `YDT · BASIC` · `Simple Present vs Present Continuous` | rozet 36 px, ders adı 56 px, 2 satır (dikey v2) |
| 300–410 | üst satır (karar sorusu) | `Genel mi, şu an mı?` | Lexend 64, mürekkep |
| 430–700 | kart 1 | `She wears her coat` / `in the winter.` · `GENERAL` · küçük mont + tekrar eden kış bantları | Fredoka 64; etiket Caveat 64; Shorts sahne 02 kart 1 görseli |
| 720–990 | kart 2 | `She is wearing her` / `pink T-shirt today.` · `RIGHT NOW` · küçük tişört + today gün bandı, now noktası içinde | aynı; Shorts sahne 02 kart 2 görseli (ana ders sahne 08) |
| 1010–1095 | not satır 1 | `today` (sarı hap) | Fredoka 64, ortalı |
| 1105–1190 | not satır 2 | `iki zamanda da geçebilir` (S2-C, jüri dil 2) | Lexend 64, mürekkep |
| 1210–1300 | alt satır | `Farkı anlam yapar.` | Lexend 64, mürekkep |
| 1344–1536 | "tam ders" çağrısı | `Tam ders:` / `profildeki bağlantı` · `@ydspublishing` | `Tam ders:` Caveat 72; `@ydspublishing` sarı hap; logo sol alt y ≈ 1478 |
| 1536–1920 | boş | — | platform arayüzü; Instagram bağlantı çıkartması bu bandın üst kısmına (öneri) |

- Tek sarı öğe `today` hapı (rozet ve `@ydspublishing` hapı künye öğesidir). Kartta `odak` çizgisi yok; durağan karede ikinci sarı kalabalık ekler.
- `today iki zamanda da geçebilir` 30 karakter (kalıp §3 sınırı 24) → iki parçaya bölündü: hap `today` + `iki zamanda da geçebilir` (24).
- **DİKKAT:** geniş zamanlı *today* örneği karede yok (Shorts'ta da yok; tam derste cümle 10). S2-C: cümle `geçebilir` ile yumuşatıldı
  (jüri dil 2 (c)): olasılık söyler, örnek şart olmaz. Karede `today`'den `GENERAL` kartına bağ çizilmez.

## 4. Sürüm B — soru kartı "Hangisi doğru?"

Amaç: hikâyede etkileşim. Cevap karede yazmaz; izleyici Shorts'a ya da tam derse gider.

| Bant (y px) | Öğe | Metin | Biçim |
|---|---|---|---|
| 0–288 HUD | rozet + ders adı | `YDT · BASIC` · `Simple Present vs Present Continuous` | S1 ile aynı |
| 300–440 | soru başlığı | `Hangisi doğru?` | Fredoka 96, mürekkep |
| 480–700 | kök | `Look! She ____ her` / `pink T-shirt today.` (S2-C, jüri dil 1 + kaynak 1) | Fredoka 72; `Look!` kökün parçası, vurgusuz; boşluk kalemle çizilmiş çizgi; köşede küçük tişört |
| 740–860 | şık A | `A) wears` | kart, Fredoka 72 |
| 880–1000 | şık B | `B) is wearing` | kart, Fredoka 72 |
| 1040–1150 | ipucu | `Genel mi, şu an mı?` | Caveat 64, mürekkep (karar sorusu, cevap değil) |
| 1344–1536 | çağrı | `Cevap ve neden:` / `tam derste` · `@ydspublishing` | Caveat 72; sarı hap; logo sol alt y ≈ 1478 |
| 1536–1920 | boş | — | platform arayüzü |

- Doğru cevap: **B) is wearing**. Neden: `Look!` konuşma anını gösterir; bugünkü kıyafet şu an görülüyor (ana ders cümle 3 ve 9).
  Cevap anahtarı yalnız bu belgede ve açıklama notunda; karede yok.
- Tek sarı öğe yok; kart mürekkep ve kâğıt. Gerekçe: şıklardan birini sarıyla vurgulamak cevabı verir.
- Kök = ana ders cümlesi + `Look!` (S2-C). `Look!` olmadan *wears* da savunulabilir (*today* iki zamanda da geçebilir; jüri dil 1, kaynak 1);
  `Look!` karar bağlamını karenin içine koyar. `Look!` ana derste yok: yeni sözcük, iki jürinin ortak önerisi.
- Elle paylaşımda Instagram'ın test çıkartması (iki şık, doğru şık işaretli) karenin üstüne konabilir. Uygulama özelliği; doğrulanmadı.
  Çıkartma kullanılırsa kart şıkları çıkartmanın altında kalmasın: çıkartma 1040–1300 bandına (ipucu satırı o zaman çıkar).
- Bütün satırlar ≤ 24 karakter: en uzun `pink T-shirt today.` 19, `Look! She ____ her` 18, `Cevap ve neden:` 15.

## 5. Sürüm farkı

| | A bilgi kartı | B soru kartı |
|---|---|---|
| İzleyiciye görevi | oku, kaydet | seç, cevabı ara |
| Örnek | iki cümle, etiketli | bir cümle, boşluklu, `Look!` bağlamlı |
| *today* | açıkça söylenir (iki zamanda da geçebilir) | kökte durur; `Look!` konuşma anını verir, karar sorusu ipucudur |
| Çağrı | `Tam ders: profildeki bağlantı` | `Cevap ve neden: tam derste` |
| Sarı | `today` hapı | yok |

## 6. UTM (yalnız bağlantı çıkartması, elle Instagram paylaşımı)

`utm_medium=story` hikâyeyi ayırır; `utm_content` sürümü ayırır. `utm_campaign` = ders kodu olduğu gibi (istem; ayrıntı `aciklama-taslak.md` §2).

| Sürüm | Bağlantı |
|---|---|
| A | `https://ydspublishing.com/grammar/02-04-ydt-temel?utm_source=instagram&utm_medium=story&utm_campaign=ING-YDT-GR-02-04-T&utm_content=s2-a` |
| B | `https://ydspublishing.com/grammar/02-04-ydt-temel?utm_source=instagram&utm_medium=story&utm_campaign=ING-YDT-GR-02-04-T&utm_content=s2-b` |

Adres kaynağı, canlılık uyarısı ve `{PLATFORM_URL}` yer tutucusu: `aciklama-taslak.md` §1, §7.
