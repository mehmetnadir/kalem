KARAR: GEÇTİ

# Dil jürisi · tur 2 — 02-04-ydt-temel · 14.11.2026
Denetlenen: `uretim-tutanagi/senaryo-taslak.md` (tur 2) · Tur 1: `juri/02-04-ydt-temel.dil.md` · Yazar kaydı: `juri/tur1-duzeltme.md`
Yeni kanıtlı madde: 0.

## 1. Tur 1 maddeleri

| Tur 1 | Durum | Kanıt (taslak satırı) |
|---|---|---|
| 1 · satır 9 *today* konuşma anını gösterir | kapandı | Ses: "Burada /təˈdeɪ/ bugünü gösterir. Bugünkü kıyafet: konuşma anında olan durum, şimdiki zaman." Ekran `today → this day only`. Satır 10 ve 14 ile artık çelişmiyor. |
| 2 · satır 11 "İngilizcede ing yok" | kapandı | "Ama bu cümlede /ɪŋ/ eki yok." Genel kural görünümü kalkmış; satır 3, 13 ile çelişki yok. |
| 3 · satır 7 belirsiz "Bu" | kapandı | "Tarife cümlelerinde özne genelde cansızdır: tren, uçak, ders." Örnek özneler §3 Türetilmiş 3'te işaretli. |
| 4 · satır 2 ↔ 8 terim | kapandı | Satır 2 "üç kullanım farkı", satır 8 "üç fark". Aynı kavram, aynı çekirdek sözcük. |
| Ek · satır 15 | kapandı | "Boşluğa hangi şık gelir?" |

## 2. Okunuş riskleri

| Yer | Durum |
|---|---|
| Satır 3 *wear* | kapandı: `/wɛr/` |
| Satır 9, 10 *today* | kapandı: tr parçalarda `/təˈdeɪ/` (4 yer); EN parçalar düz *today* |
| Satır 3, 17 yalın *wearing*, *living* | açık, kabul: metin değişmedi; `/ɪz/` önde olduğu için kabul. Dinleme notu §6'da var. Ses üretiminde dinlenir. |
| Satır 11, 13 "yor eki" | açık, kabul: Türkçe hece; dinleme notu var |
| Satır 15 `[sus 0,5 sn]` | açık, kabul: iki `en` parça tonu ses üretiminde dinlenir |
| Satır 5, 10 *p.m.* | değişiklik gerekmedi |

## 3. Düzeltmenin yarattığı yeni sorunlar

Bakılan yerler: satır 3, 6, 7, 8, 9, 10, 11, 18 (değişen satırlar) ve §6 ses notu. Dilbilgisi, anlam çelişkisi, sözlük uyumu, IPA yazımı kontrol edildi. Yeni hata yok.
- `/ɪŋ/` yazımı: `ses-sozluk.json` `ipa["-ing"]` = `ɪŋ`; tr parçada tek başına "ing" için yazarın gerekçesi (tiresiz "ing" çevrilmez) tutarlı.
- `/wɛr/`, `/təˈdeɪ/`, `/lɪv/`: sözlükte yok, §6'da elle yazıldığı belirtilmiş; ekran ve kıyas metni düz sözcük kalıyor. Tutarlı.
- Satır 9 "iki cümlede aynı sözcük var" yalnız bir cümleyi okutur; ikinci cümle satır 10'da gelir. Bölüm tek birim, anlatım doğru; madde değil.

## 4. Açık nokta cevabı (dil)

- **9 (IPA mı ayrı `en` parça mı):** IPA kabul. Gerekçe: tek sözcüklük `en` parça zayıf duyuldu (13.11 KULAK, `ses_metni.py` Kural 6; yazarın kaydı); IPA biçimi sözlükteki işlev sözcükleri ile aynı mantıkta. Koşul: ses denemesinde (3021) *wear*, *today*, *live* dinlenir; düz okunursa ayrı `en` parçaya geçilir. Taslak §6 bunu zaten yazıyor.
  Kanıt: taslak §6 "Ses metni dönüşümü" ve "Riskler"; `ses-sozluk.json` `_aciklama`, `ipa`.
