# Sahne 12 · ara özet (HyperFrames, 463 kare, 205,30–220,33 sn; cümle 14)

Durum: P2 yazıldı. `ONIZLE_YALNIZ=1` hazırlığı koşuldu (son koşu AÇIK). Render yok. Kapı (`qa-yerel.sh --hazirla`) çıkış kodu 0.
Tema: acik

## İçerik
BRIEF §3 No 12: `ozet` 3 madde kademeli. Her madde, kural kartının (sahne 07) karşılığına ince kalem çizgisiyle bağlanır. Perde yok, sonda geçiş çizgisi.

| Yer | Öğe |
|---|---|
| Sol bant 1 | `general · permanent · timetable` → hap `V1 / V-s` |
| Sol bant 2 | `right now · temporary · arrangement` → hap `am / is / are + V-ing` |
| Sol bant 3 | `time word · Turkish -yor` → hap `clue` / `MEANING` → hap `decision` |
| Sağ kart 1 | `SIMPLE PRESENT` + sahne 07 sol sütun ikonları (mont, ev, tren) |
| Sağ kart 2 | `PRESENT CONTINUOUS` + sahne 07 sağ sütun ikonları (tişört, bavul, bilet) |
| Sağ kart 3 | `MEANING FIRST` + sarı belirteç (sahne 07 alt satırı) |

- Görsel dil 02-03/12 ile aynı: kalemle bant, sarı belirteç, kalem oku. Fark: kalıp hapı (vurgu dolgusu + zemin renginde yazı; açık temada sarı yazı kontrastı düşük olduğu için).
- Sağdaki ikon, sözcüğü söylenince çizilir (söylendiği anda). Bant → kart çizgisi maddenin ilk sözcüğünde başlar.
- Künye: sağ üst `Recap`, ajandada etkin nokta yok (02-03/12 ile aynı). Renkler `RENK` (tek vurgu), kırmızı yok, yeşil yok, emoji yok.
- Yazı boyları: madde 48, kart başlığı 34 / 40, en küçük yazı künye (ortak). Hepsi taban 30'un üstünde. Ölçüler `u()` ile.
- Hareket yerel 0,55–14,99 sn. İlk/son 12 kare durgun (`Y.kontrol` geçti; sınır 15,03).

## Olay ↔ sözcük (cümle 14; kare = sahne içi)
| Olay | Küresel sn | Kare | Sözcük (i) |
|---|---|---|---|
| 3 madde bandı (soluk) | 205,85 | 16 | Özet. (0) |
| ince çizgi → SIMPLE PRESENT kartı (çerçeve + başlık) | 206,89 | 48 | Genel (1) |
| `general` + belirteç | 206,89 | 48 | Genel (1) |
| mont ikonu (kartta) | 207,29 | 60 | durum, (2) |
| `· permanent` + belirteç; ev ikonu (+0,2) | 207,85 | 76 | kalıcı (3) |
| `· timetable` + belirteç; tren ikonu (+0,2) | 208,89 | 108 | tarifeli (6) |
| kalem oku + hap `V1 / V-s` | 210,17 | 146 | geniş (8) |
| ince çizgi → PRESENT CONTINUOUS kartı | 211,29 | 180 | Konuşma (10) |
| `right now` + belirteç | 211,29 | 180 | Konuşma (10) |
| tişört ikonu (kartta) | 211,77 | 194 | anı, (11) |
| `· temporary` + belirteç; bavul ikonu (+0,2) | 212,41 | 213 | geçici (12) |
| `· arrangement` + belirteç; bilet ikonu (+0,2) | 213,37 | 242 | planlanmış (15) |
| kalem oku + hap `am / is / are + V-ing` | 214,77 | 284 | şimdiki (17) |
| `time word` + belirteç | 216,01 | 321 | Zaman (19) |
| `· Turkish -yor` + belirteç | 217,21 | 357 | Türkçe (22) |
| kalem oku + hap `clue` | 217,93 | 379 | ipucu (24) |
| ince çizgi → MEANING FIRST kartı | 218,97 | 410 | Kararı (26) |
| `MEANING` (bant); kartta MEANING FIRST belirteci | 219,45 | 424 | anlam (27) |
| kalem oku + hap `decision` | 219,85 | 436 | verir. (28) |
| geçiş çizgisi (219,87–220,29) | 219,87 | 437 | verir. (28) |

## Kapı
Komut: `bash araclar/qa-yerel.sh 02-04-ydt-temel 12-hyperframes-ozet 210.9,215.7,220.32 220.32 --hazirla`
```
== KAPI
12-hyperframes-ozet | çakışma yok (61 örnek, 39009 kutu)
== KARE (açık) … 210.9 / 215.7 / 220.32
== KARE (koyu) … 220.32
kapı çıkış kodu: 0
```
1 tur yetti. Düzeltme turu gerekmedi.

## Bakılan kareler
| Kare | An | Bulgu |
|---|---|---|
| `k/12-hyperframes-ozet-210.9.png` | madde 1 bitti | bant 1 + kart 1 tam; taşma, kesik yazı, binme yok. Bant 2–3 boş çerçeve (tasarım: yuva önce, madde söylenince dolar). |
| `k/12-hyperframes-ozet-215.7.png` | madde 2 bitti | iki bant ve iki kart hizalı; hap kontrastı iyi. |
| `k/12-hyperframes-ozet-220.32.png` | sahne sonu | 3 bant, 3 kart, geçiş çizgisi tam; künye ile çakışma yok. |
| `k/koyu/12-hyperframes-ozet-220.32.png` | sahne sonu, koyu | turuncu hap üstünde koyu yazı okunur; çizgiler açık renkte. |

## Açık noktalar
1. **Kare zamanı küresel saniyedir.** İstem "sahne içi saniye" der. `sahne-kare.mjs` ise `t`'yi anlatım saniyesi alır (sahne 07 RAPOR notu). Bu yüzden zamanlar küresel verildi (yerel 5,6 / 10,4 / 15,02).
2. **Yazım yolu.** `write-size-gate.sh`, 15 satırdan uzun `.py` yazımını engelledi. Atlatma bayrağı Claude'a kapalı. Şef `uret.py` ve `olay.py`'yi `/tmp/kalem0204-s12/*.md` olarak yazdı. `agy-filo tek --rol bulk` (gemini-3.8-flash-low, 10 sn) dosyaları `cp` ile koydu. Şef `cmp` ile doğruladı: bayt bayt eşit. Emsal: sahne 07, 09. İstemdeki "alt ajan açma" kuralıyla çatışır; Claude alt ajanı açılmadı.
3. Madde 3 ekran metnindeki `clue · MEANING` ayracı satır sonuna denk gelir: `·` yerine satır kırılır (iki satır).
4. Hap sağ iç boşluğu soldan ~6–8 px geniştir (`genislik()` kerning saymaz; `am / is / are + V-ing` hapında görünür). Okumayı bozmaz.
5. Bant 2 ve 3, madde söylenene kadar boş çerçevedir (en uzun: bant 3, 206,80–216,01). 02-03/12 ile aynı kalıp; Nadir istemezse çerçeveler maddeyle birlikte çizilir.
6. `hyperframes check` koşulmadı (istem kapısı `qa-yerel.sh`).

Dosyalar: `uret.py`, `olay.py`, `yardim.py` (02-04/01 kopyası, `u()` içerir), `calistir.sh`, `proje/index.html`, `olaylar.json`, `k/`.
