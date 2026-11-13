# Sahne 08 — Tuzak (HyperFrames, 1864 kare = 1852 içerik + 12 geçiş; t_bas 218,97)

Tema: acik

Durum: önizleme hazır (koyu, sonra açık). Render, kapı ve kare görüntüsü bu turda YOK (şef EK 13.11 12:40).

## İçerik
- Perde: `TUZAK` + "hata iki yerde çıkar:" + çipler olumsuz / soru.
- İki yanlış kart `She doesn't eats fish.` / `Does she eats fish?` + kırmızı çarpı (kırmızı YALNIZ bu sahnede: iki çarpı + gets çarpısı).
- Soru anı 2 (cümle 42, `yanılgı:` she var, doesn't eats): öğrenci başı + 3 satır balon, `eats` sarı daire.
- `does = do + s` (s kutusu); sarı s `eats`'ten `does`'a kayar (yay hareketi), "takı yardımcı fiilde zaten var".
- "she → s (zihin se ister)": sarı oklar s → eats (kırmızı çarpı) ve s → does (yeşil tik).
- `fark_tablosu`: olumlu → eat|s ("yardımcı fiil yok") · olumsuz, soru → doe|s + eat ("yardımcı fiil var", eat soluk, yalın altı çizgi).
- İki doğru kart (yeşil tik, eat soluk) → kanca kartı (I get up at seven every morning.) → He doesn't get up… / Does he get up… (get soluk, daire) → `get` tik, `gets` çarpı → "Kod: takı bir kez gelir." + `s → yardımcı fiil`.
- Künye: `Trap` (ajanda etkin 4. sözcük Trap).

## Olay ↔ sözcük t0 (sapma ≤ 0,15; küresel sn, yerel = küresel − 218,97)
| Olay | Cümle / sözcük | Sözcük t0 | Olay küresel | Yerel | Sapma |
|---|---|---|---|---|---|
| `TUZAK` açılır | 39 Şimdi | 219,52 | 219,52 | 0,55 | 0,00 |
| `doesn't` (yanlış kart 1) | 40 doesn't | 225,59 | 225,59 | 6,62 | 0,00 |
| `Does` (yanlış kart 2) | 41 Does | 227,58 | 227,58 | 8,61 | 0,00 |
| `eats` sarı daire (balonda) | 42 eats | 232,64 | 232,64 | 13,67 | 0,00 |
| s kutusu (does = do + s) | 43 se | 238,07 | 238,07 | 19,10 | 0,00 |
| sarı s kayışı başlar | 43 Takı | 239,27 | 239,27 | 20,30 | 0,00 |
| `she` | 44 she | 243,75 | 243,75 | 24,78 | 0,00 |
| kırmızı çarpı (s → eats) | 44 yanlış. | 247,88 | 247,88 | 28,91 | 0,00 |
| `eats` + s kutusu (tablo) | 45 eats. | 254,96 | 254,96 | 35,99 | 0,00 |
| s kutusu `does`'ta (tablo) | 45 ona | 259,77 | 259,77 | 40,80 | 0,00 |
| `get` sarı daire (kartlarda) | 49 Get | 272,85 | 272,85 | 53,88 | 0,00 |
| `Kod:` | 50 Kod: | 276,47 | 276,47 | 57,50 | 0,00 |
Çarpı/tik: kart cümlesi biter bitmez (son sözcük t0 + 0,15).

## Kontroller (kapı/görüntü yok)
- Uret sırasında taşma sınaması (assert): kartlar, balon, tablo, kod satırı sığıyor. `node --check` 2 blok OK · yinelenen id yok · negatif zaman yok.
- İlk hareket 0,55 sn (kare 16), son hareket 61,56 sn (içerik 61,73 sn). olaylar.json 70 olay (kare 16–1838).

## Açık
- Sağ bölge "yaklas" (yanlış cümle büyür) yok; kırmızı çarpı vuruşu ile verildi.
- Yanlış kart 1'deki `s` (eats) 239,3 sn'de gizlenip sarı kutu olarak `does`'a taşınır; kart gruplarının solması 248,7 sn'de.

## QA 13.11
- Kapı: ölçülmedi (HyperFrames). Düzeltme (uret.py): YESIL = Y.YESIL → R["vurgu"] (doğru tik/kartlar vurgu); kırmızı yalnız yanlış çarpılarında kaldı. Önizleme sunucuda yenilendi (--hazirla).
- Kareler k/08-…-224, -235, -255, -275, k/koyu/…-245. Göz: yanlış kartlar + kırmızı çarpı, she→s oku, eat|s, doğru kartlar + tik, get ✓ / gets okunur; taşma yok. Kalan yok.

- Halka kuralı: DEĞİŞTİ: `she` halkası (bd) ve iki `get` halkası (g1, g2) → altçizgi (uret.py). Kare k/…-275 temiz. Kapı HyperFrames: ölçülmedi.

- zaman eşitleme 13.11: calistir.sh KARE 1864→1879; --hazirla ile yeniden kuruldu; kareler k/…-244.5…276.2.
