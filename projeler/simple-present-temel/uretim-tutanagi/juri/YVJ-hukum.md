# YVJ-0202T — `simple-present-temel` YouTube yayın verisi ÇIKTI jürisi · 15.11.2026

Jüri modeli: Claude Sonnet 5.5 (`claude-sonnet-5-5`). Üretici modeli: Claude Opus 5.5. Aynı model DEĞİL.
Kapsam: ana paket + dikey paket (`youtube.json` iki pakette bayt bayt aynı; `youtube-aciklama.md` yalnız `utm_content` farklı: `ana-yatay` / `dikey-tam`).

## Özet

| Küme | evet | hayır | kanıt yok |
|---|---|---|---|
| YV-1 … YV-9 | 8 | 0 | 1 (YV-8) |
| §3 bildirim (7 satır) | 6 | 1 (Yer) | 0 |
| Toplam | 14 | 1 | 1 |

Kaldı: YV-8 (kanıt yok), §3 Yer (hayır).

## YV tablosu (`juri-olcutleri.md` §2f)

| Kimlik | Hüküm | Kanıt | Not |
|---|---|---|---|
| YV-1 | evet | `baslik` = "Simple Present \| YDT İngilizce" · 30 karakter (≤ 100) · kalıp `<Konu> \| <kitle> İngilizce`; konu = `senaryo.json` `baslik`, kitle = `kitle: YDT` | Aynı başlık `02-02-ydt-ileri` için de çıkar (Studio'da çift başlık). Seviye başlıkta yok; kalıp bunu istemiyor |
| YV-2 | evet | `youtube-aciklama.md` 661 bayt (≤ 5.000), 13 satır. Sıra: satır 1 değer cümlesi · satır 2 kaydet · satır 4–8 damgalar · satır 10 sıradaki ders · satır 11 bağlantı (utm) · satır 13 etiket satırı. utm: source/medium/campaign/content hepsi var, `utm_campaign=ING-YDT-GR-02-02-T` = `senaryo.json` `meta.kod` | Damgalar giriş klibi eklenince kayar (standart §2); açıklamada ham değer, araç düzeltir (araç bu worktree'de yok, bkz. YV-3 notu) |
| YV-3 | evet | İlk damga 00:00. 5 bölüm. `zaman.json` sahne başları 0 · 15,45 · 27,69 · 43,36 · 60,47, son 93,47. Bölüm süreleri 15,45 · 12,24 · 15,67 · 17,11 · 33,00 (en kısa 12,24 ≥ 10). Açıklama damgaları 00:00 · 00:15 · 00:28 · 00:43 · 01:00 = en yakın saniye; `youtube.json` `bolumler[].t` ile eşleşti | Yuvarlama bölümü ≤ 0,5 sn erken açar; sözden önce düşer (söz başları 16,00 · 28,24 · 43,91 · 61,02). Giriş kayması aracın işi; `ortak/youtube/uret.py` ve damga kaydıran kod aranmadı, kanıt yok → YV-3 kapsamı dışı ama araç yazılırken sınanmalı |
| YV-4 | evet | Senaryo/METİN ile eşleme: B1 "Geniş zamandan köprü: Simple Present" = cümle 1–2 (0–15,45; "Türkçede buna geniş zaman deriz… karşılığı Simple Present"). B2 "Doğa kanunu: The sun rises in the east" = cümle 3 ("Doğa kanunu: hep böyledir"). B3 "Alışkanlık: usually, always, every day" = cümle 4 ("Usually, always, every day: alışkanlık işareti"). B4 "Tarife ve program: Our plane takes off" = cümle 5 ("Tarife, program, takvim"). B5 "Neden hep s? He, she, it ve does" = cümle 6–7 (öğrenci sorusu; "özne üçüncü tekil kişi: he, she, it… does girer"). İç ad ("Örnek N", "Soru + Form") yok | B3 adı üç sözcüğü dersin kendi ifadesiyle verir; "her zaman alışkanlık" iddiası yok. En uzun ad 38 karakter |
| YV-5 | evet | 13 etiket; düz toplam 134, virgülle birleşik 158, JSON gösterimi 186 (hepsi ≤ 500). Konu "Simple Present", zaman adı "geniş zaman" + "Present Simple", kitle "YDT", "İngilizce", "gramer" var. Yineleme yok (büyük/küçük harf duyarsız) | `surumler.json` `video.etiketler` 4 etiketi (İngilizce, temel, gramer, Simple Present) hepsi içinde |
| YV-6 | evet | Başlık, açıklama (satır 1–2), sabit yorum, gönderi g1 sözce sözce okundu. Mutlak kural yok; yanlış denklik yok; doğru cümle yanlış gösterilmiyor. Gönderi: `"he goes" ama "I go"` doğru; "fiile gelen s harfini üç örnekle" = rises · goes · takes (off) → doğru. Sabit yorum: tek cümle, dilbilgisi iddiası yok. Emoji taraması 0 (iki pakette `youtube.json`, `youtube-aciklama.md`) | Açıklama satır 1 "…doğa kanunu, alışkanlık, tarife ve fiile gelen s" dört öğeyi eş sayar ama "üç örnekle" der; okuma belirsizliği küçük, hata değil |
| YV-7 | evet | `katalog.json` ünite 02 `ad: Tenses`, `sira: 2`; konu GR-02-02 `sira: 2`; kitle `ydt`→"YDT", seviye `temel`→"Temel" → liste adı "Tenses · YDT Temel" ✓, `sira: 2` ✓. Önceki `02-01-ydt-temel` (GR-02-01) ✓, sonraki `02-03-ydt-temel` (GR-02-03) ✓. Açıklamadaki "Sıradaki ders" adı `02-03-ydt-temel/surumler.json` `konu` ile bire bir | `02-01-ydt-temel` paketi bu worktree'de yok; kimlik katalogda var |
| YV-8 | **kanıt yok** | `altyazi.json` ölçüldü: 26 satır, `t0 < t1`, sıra bozuk değil, son satır t1 = 92,55 ≤ ders 93,47 ✓. Ama `altyazi.srt` hiçbir yerde yok (pakette tutulmaz, standart §2) ve `.srt` türeten kod `dijital-anlatim` altında bulunamadı | Maddenin "srt süreleri json ile aynı" yarısı ölçülemez. Panelin türeticisi çıkınca iki dosya karşılaştırılmalı |
| YV-9 | evet | `kapak.png` ana pakette 1920×1080, dikey pakette 1080×1920; ikisi de var. `gonderiler[0].gorsel = "kapak.png"`. `KAPAK-RAPOR.md` açık/koyu ayrı dosya (`kapak.png` açık). Gönderi metninde emoji 0 | Dikey `kapak.png` açık tema olarak yetmez diye gönderi dikeyde paylaşılmamalı (üretici notu 4 ile aynı: yalnız ana sürümden) |

## `youtube-surumu-standart.md` §3 bildirim kuralları

| Kural | Hüküm | Kanıt | Not |
|---|---|---|---|
| Sayı | evet | Ders 93,47 sn < 4 dk → 1 bildirim; `bildirimler` uzunluğu 1 | |
| Zaman ≈ %30 | evet | t = 43,91 (%47,0). Cümle başları (`METİN.md` / `senaryo.json` cümle sınırı): 1,00 · 3,31 · 16,00 · 28,24 · **43,91** · 61,02 · 65,73. %30 = 28,04 sn ama ilk 30 sn yasak; 28,24 yasak bölgede. 30 sn sonrası ilk cümle başı 43,91 | Standartta "%30" ile "ilk 30 sn yok" 93 sn'lik derste çakışır; 43,91 kuralların birlikte izin verdiği en yakın cümle başı. Standarda "≈ %30 ya da ilk 30 sn sonrası ilk cümle başı" yazılmalı |
| Cümle sınırı | evet | 43,91 = cümle 5 "Üçüncü örnek." başı; önceki cümle 43,36'da biter (0,55 sn boşluk) | |
| İlk 30 sn / son 20 sn | evet | 43,91 ≥ 30; 43,91 + 3,0 = 46,91 ≤ 93,47 − 20 = 73,47 | |
| `giris`, `cikis` alanları | evet | ikisi `true`; şema örneğiyle aynı (`bildirimler` / `giris` / `cikis`) | |
| Yer (sağ üst) | **hayır** | Standart §3: "sağ üst". `ortak/youtube/bildirim/yer.json` = `sol_alt` (x 240, y 900). `ortak/youtube/RAPOR.md` satır 69–92 sapmayı belgeler: sağ üst 02-04'te standart anlarda 2/54 ve 0/50 kare boş, sol alt 54/54 ve 50/50; "karar Nadir'de" | Veri dosyası (`youtube.json`) yeri taşımaz; sapma YV'yi değil standardı etkiler. Hüküm: standart ile uygulama çelişiyor; Nadir kararı gelene kadar kaldı |
| Ses (yok) | evet | `youtube.json` ses alanı yok; kural metni uygun. Ölçüm render ister (YT-3) | |

## Kaldı maddeleri — düzeltme önerisi

| Madde | Öneri |
|---|---|
| YV-8 | Paneli yazan işte `altyazi.json` → `altyazi.srt` türetici + eşitlik testi (satır sayısı 26, her satırın başı/sonu ±1 ms) eklensin; o zamana kadar YV-8 "kanıt yok" kalır. Veri tarafında düzeltme gerekmez |
| §3 Yer | `standart §3` satırı şöyle güncellensin: "Yer: sol alt (`bildirim/yer.json`), ölçüm RAPOR.md §4; sağ üst yalnız boşsa" — Nadir kararıyla. Karar sağ üst çıkarsa `yer.json` tek satır değişir |

Not (kapsam dışı, bilgi): ders içi söz iddiaları — "Türkçedeki er eki gibi: git-er, go-es" (-er her kişide gelir, -s yalnız üçüncü tekilde), `canAlici` "geniş zaman eki = s" ve "Kod: always, usually, every day" (always öteki zamanlarla da gelir) — `juri-olcutleri.md` §1c çıktı jürisine aittir. YV metinleri bu üç iddiayı taşımaz.
