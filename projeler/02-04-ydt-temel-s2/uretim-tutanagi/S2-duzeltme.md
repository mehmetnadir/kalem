# S2 jüri düzeltmeleri — 02-04-ydt-temel-s2 · 15.11.2026 (istem S2-C)

Girdi: `juri/s2.dil.md` (DÜZELT, 3 madde), `juri/s2.kaynak-kural.md` (DÜZELT, 4 madde; 4a + 4b). 8 maddenin 8'i işlendi.
İki jürinin hikâye B maddesi (dil 1, kaynak 1) ve *today* maddesi (dil 2, kaynak 3) aynı sorundur; birer düzeltme ikisini kapatır.

| # | Madde | Yapılan | Kanıt |
|---|---|---|---|
| 1 | dil 1 + kaynak 1 — hikâye B kökünde karar bağlamı yok; *wears* da savunulabilir | Köke `Look!` girdi (iki jürinin ilk önerisi): `Look! She ____ her` / `pink T-shirt today.` İpucu satırı kaldı. Cevap notu bağlamı yazar: "`Look!` konuşma anını gösterir" | `hikaye-taslak.md` §4 kök satırı, cevap notu, satır uzunluğu (18 · 19 karakter) · `aciklama-taslak.md` §4 son not |
| 2 | dil 2 + kaynak 3 — "Today iki zamanda da geçer" Shorts içinde örneksiz | Ses: `Today iki zamanda da geçebilir; farkı anlam yapar.` (dil (c), iddia yumuşadı, örnek şart değil). Görsel: `Simple Present`'e ok yok, kart 1'e bağ yok; `today` dairesinden yalnız `RIGHT NOW`'a tek ok (kaynak (b)). Açıklama: set A'da *today* satırı çıktı (kaynak (b)); set B'de `geçebilir` ile kaldı. Tren örneği yazılmadı (dil (c)). Hikâye A not satırı `iki zamanda da geçebilir` (24 karakter) | `ortak/anlatim/senaryo.json` cümle 2 parça 4 · `sentez.wav.rapor.json`: duyulan "Today, iki zamanda da geçebilir. Farkı anlam yapar.", benzerlik 1,00 · `senaryo-taslak.md` §2 · `aciklama-taslak.md` §3–§4 · `hikaye-taslak.md` §3 |
| 3 | kaynak 2 — cümle 3 "Bu, üç farktan yalnız biri." *today* notuna bağlanıyor | Cümle 2 sırası: EN `She wears…` · `Genel durum: geniş zaman.` · EN `She is wearing… today.` · `Today… geçebilir…` · `Konuşma anı: şimdiki zaman.` Cümle 2 çift ile biter; "Bu" genel ↔ konuşma anına bağlanır. Cümle 3'e dokunulmadı. Açıklamada aynı ilke: "Bu, üç farktan biri." her yerde iki örneğin hemen ardından | `senaryo.json` cümle 2 · `cumle-3.wav` md5 `80e56127…` = S1 `cumle-3.wav` (önbellek, ücretsiz) · `aciklama-taslak.md` §3–§4 |
| 4 | dil 3 — "konusu püf noktası" tamlaması bozuk | Set A YouTube: `… (ING-YDT-GR-02-04-T) konusunda püf nokta: …` | `aciklama-taslak.md` §3 · `../aciklama-a.md` §1 |
| 5 | kaynak 4a — kapak C can alıcısı iki yerde farklı (`cümle 3` ↔ `canAlici[2]`) | Tek kaynak `canAlici[0]` (jüri önerisi; C'nin iki kartı genel ↔ şu an farkını gösterir). §1 tablosundaki "ana ders cümle 3" atfı kaldırıldı | `kapak-taslak.md` §1 can alıcı satırı, §6 C satırı |
| 6 | kaynak 4b — 15 yaş dil kararı gerekçesiz; D-0278 sicilde yok | S1 `hikaye-taslak.md` §2 gerekçe tablosu alındı. "İstemde geçti, sicilde doğrulanmadı" notu korundu. Açıklama §1'e gerekçe satırı | `hikaye-taslak.md` §2 · `aciklama-taslak.md` §1 son satır |

## İki jürinin önerisi ayrıştığı yer (madde 2)

| Katman | dil 2 önerisi | kaynak 3 önerisi | Uygulanan |
|---|---|---|---|
| Ses | (c) `geçebilir` | (b) metin değişmez | (c) `geçebilir` |
| Ekran oku | (a) "yalnız PC'ye ok" zayıf: sesle çelişir | (b) `Simple Present`'e ok yok | (b) |
| Açıklama | tren örneği yazma | *today* satırını çıkar | set A çıkar · set B `geçebilir` · tren yok |

Gerekçe: dil jürisinin (a)'ya itirazı ses `geçer` (kesin iddia) iken ekranın yalnız PC'yi göstermesiydi. Ses `geçebilir` olunca kesin
iddia kalmaz; ekran yalnız bu cümlenin anlamını (konuşma anı) gösterir. Çelişki kalmaz. Set B *today* üzerine kurulu olduğu için satır
silinmedi, yumuşadı. Karar geri alınabilir: ses parçası 50 karakter (≈ 0,25 TL). Şef onayı: `S2-C-RAPOR.md` açık nokta 2.

## Çok sürüm kararı (Nadir 15.11; jüri maddesi değil)

| Öğe | Yapılan | Dosya |
|---|---|---|
| Kapak A/B/C | A = sahne 01 karesi `kapak-a.png` + kopyası `kapak.png`; B = sahne 05, C = sahne 06 (durağan) | `kapak-taslak.md` üst not, §1, §6, §7 |
| Hikâye A/B | A = sahne 04 `hikaye-a.png` + kopyası `hikaye.png`; B = sahne 07 `hikaye-b.png` | `hikaye-taslak.md` üst not |
| Kapak dosyası satırı | set A YouTube "Kapak: `kapak-a.png`" | `aciklama-taslak.md` §3 |

## Uygulanmayan / şef ya da Nadir kararı

| Madde | Neden |
|---|---|
| S1 `aciklama.md` / `aciklama-a.md` / `aciklama-b.md` "konusu püf noktası" (dil 3) | S1 dosyası; yazma kapsamı dışı. Jüri: "şef istek açsın" |
| `utm_campaign` büyük/küçük harf (S1 küçük, S2 büyük) | iki jüri: karar Nadir'de; S2 şemaya uyar |
| D-0278 sicil doğrulaması | srv21 defter kopyası D-0096'da biter; Mac defterinde doğrulanır |
| dil 2 (b) seçeneği (sahne 02 sonuna tren kartı) | (c) seçildi; süre payı da yok (ölçülen 27,98 sn) |
