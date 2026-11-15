# İstem S2-A raporu — 02-04-ydt-temel-s2 Shorts senaryo taslağı + çok sürümlü huni seti · 15.11.2026

| Dosya | İçerik | Durum |
|---|---|---|
| `senaryo-taslak.md` | Shorts 3 sahne (kapak · örnek · tam ders çağrısı), 3 cümle, ses/ekran/görsel tablosu, kaynak eşlemesi, süre | TASLAK |
| `kapak-taslak.md` | 3 kapak sürümü (A kod · B soru · C karşıt çift), yerleşim, `senaryo.json` alanları | TASLAK |
| `hikaye-taslak.md` | 2 hikâye karesi (A bilgi kartı · B soru kartı "Hangisi doğru?"), UTM | TASLAK |
| `aciklama-taslak.md` | 2 açıklama seti (A doğrudan · B soruyla açılan) × YouTube / Instagram / TikTok, UTM tablosu, yer tutucular | TASLAK |
| `S2-A-RAPOR.md` | bu rapor | — |

Yapılmayan (istem kuralı): ses sentezi, ElevenLabs çağrısı, render, sahne kodu, git commit, alt ajan, silme. Yazma yalnız bu dizinde.
Kovan kaydı yazılmadı (yazma kapsamı dışında). Ölçüm: ana ders `cikti.mp4` ffprobe 265,676 sn (bu istemde yeniden ölçüldü).

## 1. Süre tahmini ve hesabı

| Kalem | sn | Kaynak |
|---|---|---|
| İlk söz | 1,00 | S1 `zaman.giris.ilkSoz` |
| Cümle 1 `Genel mi, şu an mı?` | 1,44 | ana ders cümle 18'de aynı tümce, ölçülmüş 2,96–4,40 |
| Cümle arası | 0,55 | S1 kuralı |
| Cümle 2 (5 parça) | 12,83 | 2,32 + 1,84 + 2,72 + 1,95 + 3,10 (ölçülmüş ikizler) + parça araları 0,25 × 3 + 0,15 |
| Cümle arası | 0,55 | |
| Cümle 3 (S1 birebir) | 9,02 | S1 `sureler.json` ölçülmüş; S1 önbelleğinden |
| Kuyruk | 1,00 | son söz + 1,0 sn |
| **Toplam** | **26,39** | hedef 24–28 sn içinde |

- Yöntem değişikliği: S1-A tahmini sözcük/dk ortalamasıyla yaptı ve 3,56 sn kısa kaldı (27 → 30,56). S2 her parçayı aynı sesin ölçülmüş
  ikiziyle tahmin eder (parça tablosu `senaryo-taslak.md` §5).
- Üst sınır: yeni parçalara S1 sapması (+%11) eklenince 27,86 sn. 28 sn içinde; pay 0,14 sn.
- Aşarsa B planı metne dokunmaz: ilk söz 0,50 (−0,50 sn) ve/veya kuyruk 0,44 (−0,56 sn).
- Sahneler (tahmin): 01 0,00–2,44 · 02 2,44–15,82 · 03 15,82–26,39.

## 2. Kararlar ve gerekçe

1. **Kapanış S1 cümle 3 ile birebir.** Gerekçe: istem "S1 ile aynı kalıp"; metin S1-B jürisinden ve S1-C düzeltmesinden geçti; ses önbellekten
   gelir (ücretsiz, Whisper 1,00 / 1,00 / 0,90). Önbellek anahtarı aynı cümlenin komşu parçalarını içerir (`el.py` satır 88, 140–142); cümle birebir aynı olunca üç parça da tutar.
2. **Ana dersle birebir aynı cümle yok.** EN parçalar ve iki TR tümce ana dersle aynıdır, ama komşu parça değiştiği için yeniden sentezlenir.
   Yeni karakter: 188 (≈ 0,92 TL, S1 oranıyla).
3. **Can alıcı = 1. farkın sorusu + *today* bilgisi.** Cümle 1 `canAlici[0]` ilk sorusu (ana ders cümle 18'de aynı tümce); cümle 2 son parça
   `canAlici[3]` ile birebir. Sırası: soru → iki örnek → *today* iki zamanda da geçer → karar anlamda (soru satırı altçizgi alır).
4. ***today* bilgisi örneksiz.** Geniş zamanlı *today* örneği ana derste tren cümlesidir (cümle 10, 3. fark: tarife). İstem kaynağı cümle 3 ve 9;
   tren cümlesi S2'ye alınmadı. Video bilgiyi söyler, örneği tam derse bırakır. Görselde *today* oku kart 1'e gitmez (yanlış eşleşme önlenir).
5. ***wear* TR parçada yok.** Ana derste "Fiil aynı: wear." "Where" duyuldu (0,95). *today* TR parçada kalır (ana derste 1,00 duyuldu).
6. **Kapak A için `TODAY = İKİ ZAMAN` seçilmedi.** S1 kalıbının harfiyen kopyası olurdu; ama video *today*'i iki zamanda göstermez. A bunun
   yerine `GENEL ≠ ŞU AN` kodunu taşır; *today* B'de soru olur ve video cevap verir.
7. **UTM `utm_campaign` = `ING-YDT-GR-02-04-T` (olduğu gibi).** İstem talimatı ve huni-plan §6 şeması. S1 küçük harf yazar (açık nokta 1).
8. **Dil:** Instagram/TikTok öğretmen + YDT öğrencisi, veli dili yok (D-0278, istem). YouTube öğrenci + öğretmen ortak (§7).

## 3. Sürümler arası fark özeti

| Öğe | Sürüm | Ne söyler | Biçim | Tek vurgu |
|---|---|---|---|---|
| Kapak | A | kural kodu: `GENEL` / `≠ ŞU AN` + etiket `wears` / `is wearing` | figür + 2 nesne (S1 kalıbı) | `≠ ŞU AN` hapı |
| Kapak | B | soru: `TODAY VARSA` / `HANGİ ZAMAN?` | düşünen figür + takvim yaprağı | `?` |
| Kapak | C | örnek: `AYNI FİİL,` / `İKİ ZAMAN` + iki cümle üst üste | 2 kart, figür yok | `is wearing` |
| Hikâye | A | bilgi kartı: soru + 2 etiketli kart + *today* notu + "Farkı anlam yapar." | oku, kaydet | `today` hapı |
| Hikâye | B | soru kartı: `Hangisi doğru?` `She ____ her pink T-shirt today.` A) wears · B) is wearing | seç; cevap karede yok (doğru: B) | yok (cevabı vermesin) |
| Açıklama | A | kural cümlesiyle açılır | kısa, doğrudan; `utm_content=s2-a` | — |
| Açıklama | B | "Cümlede today var: hangi zaman?" ile açılır | soru → cevap; `utm_content=s2-b` | — |

Eşleşme önerisi: kapak A ↔ açıklama A · kapak B ↔ açıklama B (aynı soru) · kapak C ↔ açıklama A.
`huni-surumler.json` kimlik önerisi (şef taşır): `kapak-a`, `kapak-b`, `kapak-c`, `hikaye-a`, `hikaye-b`, `aciklama-a`, `aciklama-b`.

## 4. Yeni metin (ana derste yok, jüri bakacak)

| Metin | Nerede | Ana derste yakını |
|---|---|---|
| `Konuşma anı: şimdiki zaman.` | ses, cümle 2 parça 4 | cümle 9 "konuşma anında olan durum, şimdiki zaman" · cümle 14 |
| `Today iki zamanda da geçer; farkı anlam yapar.` | ses, cümle 2 parça 5 | `canAlici[3]` birebir · cümle 10 "Today iki cümlede de var. Farkı anlam yapıyor" |
| Kapak başlıkları `GENEL` / `≠ ŞU AN` · `TODAY VARSA` / `HANGİ ZAMAN?` · `AYNI FİİL,` / `İKİ ZAMAN` | kapak | cümle 18 "Genel mi, şu an mı?" · cümle 9–10 · cümle 3 "Fiil aynı: wear." |
| `Hangisi doğru?` · `Cevap ve neden:` / `tam derste` · `iki zamanda da geçer` · `Farkı anlam yapar.` | hikâye | — |
| Açıklama açılışları (set A ilk satır, set B "Cümlede today var: hangi zaman? Cevap sözcükte değil, anlamda") | açıklama | — |
| Kart 1 altında tekrar eden kış bantları (`zaman_cizgisi`) | görsel, sahne 02 | yok (ana ders sahne 03'te çizgi yok) |

Ana derste aynı tümce olanlar: `Genel mi, şu an mı?` (cümle 18), `Genel durum: geniş zaman.` (cümle 3), iki EN cümle (cümle 3, 9). Cümle 3 S1 metnidir.

## 5. Açık noktalar

| # | Nokta | Önerim |
|---|---|---|
| 1 | `utm_campaign`: S2 `ING-YDT-GR-02-04-T` (istem), S1 `ing-ydt-gr-02-04-t`. Analitik büyük/küçük harfi ayırırsa aynı ders iki kampanyaya bölünür | S1 `aciklama.md` 5 bağlantısını büyük harfe eşitle (S1 yayınlanmadı; bu istemin kapsamı dışında) |
| 2 | *today* bilgisi örneksiz (geniş zaman örneği 3. farkta, S3 alanı). Dil/kaynak jürisi "kendi başına anlaşılır" (kalıp §1 kural 4) maddesi açabilir | `canAlici[3]` metniyle kalsın. Jüri isterse yerine `Today tarifede geniş zamanla da gelir.` (S3'e kanca; süre ≈ aynı) |
| 3 | Profil bağlantısı hesap başına tek; set A ve B profilde aynı anda ölçülemez. Ayrım yalnız YouTube açıklamasında ve hikâye çıkartmasında | profilde set A; B ikinci dönemde |
| 4 | Kapak C figürsüz: kalıp §4 "figür + nesne" maddesinden sapma (istem tanımı "iki cümle üst üste") | figürsüz kalsın; kart köşesinde mont / tişört |
| 5 | Üç kapak videonun ilk karesi mi, yalnız platform kapağı mı? | video ilk karesi A; B ve C PNG. Video çeşidi gerekirse yalnız sahne 01 (≈ 73 kare) |
| 6 | Kapak PNG karesi t 0,90 (S1: t 1,97, altyazı dilimiyle) | üç sürüm karşılaştırılırken altyazısız kare temiz; şef onaylasın |
| 7 | Süre üst sınırı 27,86 sn (pay 0,14) | ölçülen 28'i aşarsa B planı (`senaryo-taslak.md` §5) |
| 8 | D-0278 metni srv21 `kovan-defteri` kopyasında yok (kopya D-0096'da biter) | karar istemden alındı; Mac defterinde doğrulanır |
| 9 | Sentezde kulak kontrolü: *today* (TR parça başında "Today"), *wears* / *is wearing* (ana ders jürisi koşulu) | Whisper kapısı + 3021 kulak |
| 10 | `platform_url` canlılığı ve TikTok `@ydspublishing` doğrulanmadı (S1 açık noktalarıyla aynı) | yayın öncesi |

Sonraki adım: S2-B jürisi (dil + kaynak-kural) bu 4 taslağı okur; sonra `senaryo.json` → sentez (yalnız cümle 1–2).
