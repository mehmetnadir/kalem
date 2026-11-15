# S3 jüri düzeltmeleri — 02-04-ydt-temel-s3 · 15.11.2026 (istem S3-C)

Girdi: `juri/s3.dil.md` (DÜZELT, 4 madde), `juri/s3.kaynak-kural.md` (DÜZELT, 4 madde). 8 maddenin 8'i işlendi.
Hikâye B maddesi iki jüride ortaktır (dil 2, kaynak 1); tek düzeltme ikisini kapatır. Jürinin "karar şefte" dediği seçimler
aşağıda gerekçeyle yazıldı; geri alınabilir (yalnız taslak metni değişir, ses değişmez).

| # | Madde | Yapılan | Kanıt |
|---|---|---|---|
| 1 | dil 1 — "gelecek" çift anlamlı (`İKİSİ DE GELECEK`, `İkisi de gelecek`, Instagram ilk satırı) | Kapak C: jürinin 2. önerisi `İKİ ÖRNEK` / `İKİ ZAMAN` (1. öneri `GELECEĞİ / ANLATIYOR` öznesiz kalıyordu; 2. öneri kaynak madde 2'yi de kapatır, aşağıda). Hikâye A üst satır: jürinin metni `İkisi geleceği anlatıyor` (24 karakter). Instagram set A ilk satırı: `İki cümle de geleceği anlatıyor, zamanları farklı:` (ana ders cümle 5 sözü). Metin kaynağı tablosu güncellendi | `kapak-taslak.md` §1, §2, §3 · `hikaye-taslak.md` §2, §4 · `aciklama-taslak.md` §3 Instagram, §5 · `grep "İKİSİ\|de gelecek"` → yalnız düzeltme notları |
| 2 | dil 2 + kaynak 1 — hikâye B şık B (`I go to the movie theater tonight.`) tek doğru cevap vermiyor; soru kökü yok | Taslağın yedek B'si ana sürüm: soru `Tarife mi, plan mı?` (ana ders cümle 18'den birebir), cümle kartı `The train to İzmir` / `leaves at 7 pm today.`, şıklar `A TARİFE` · `B PLAN`. Cevap A. Sıfır yeni İngilizce cümle; türetilmiş yanlış cümle yok | `hikaye-taslak.md` §3 · ana ders `ortak/anlatim/senaryo.json` cümle 18 ("Tarife mi, plan mı?"), cümle 7 ("Tarife cümlelerinde özne genelde cansızdır") |
| 3 | dil 3 — "konusu püf noktası" izafet eksik | Set A YouTube açıklaması: `Simple Present ve Present Continuous konusunun püf noktası: …`; ders kodu parantezi çıktı (kod UTM'de) | `aciklama-taslak.md` §3 YouTube, §5 · `../aciklama-a.md` |
| 4 | dil 4 — hikâye A kare metni yoğun | Kartlar kısa: `The train leaves …` / `I am going …` (kapak B/C kısaltması, tek satır). Tam cümleler Shorts'ta ve açıklamada | `hikaye-taslak.md` §2 kartlar satırı, §4 |
| 5 | kaynak 2 — kapak B ve C kalıp §4'ü sağlamıyor (C figürsüz; B/C can alıcısı listede yok) | (a) C: sağ altta küçük öğretmen figürü. (b) Seçenek (i): B can alıcısı `canAlici[1]` (tarifeli gelecek: V-s), kısa kod `leaves` (kartta sarı altçizgili sözcük; görselde değişiklik yok). C can alıcısı `canAlici[1]` + `[2]`: iki kart `leaves` ↔ `am going`; başlık `İKİ ÖRNEK` / `İKİ ZAMAN` bu kodu okur. Sapma bildirimi gerekmedi | `kapak-taslak.md` §2 "Can alıcı", "Görsel" satırları · ana ders `surumler.json` `video.canAlici` |
| 6 | kaynak 3 — "gelecek" kavramı Shorts'ta yazılmıyor; plan tarafının zaman adı yok | Jürinin 0 sn'lik yolu: sahne 02 zaman çizgisine ekran etiketi `gelecek · V-s` (`today.` çapası, ölçülen 3,40) ve `gelecek · am + V-ing` (`tonight.` çapası, ölçülen 5,93). Etiket nokta altında isimdir; dil 1'in "gelir" okunuşu başlık içindi. Sesle düzeltme (+≈ 1,2 sn) yapılmadı | `senaryo-taslak.md` §2 sahne 02 satırı, §3 · `BRIEF-S3.md` "Sahne içeriği" · `istem/sahne/D-02-hyperframes-ornek.md` |
| 7 | kaynak 4 — hikâye A alt satırı `Tren tarifeye uyar` "kesit" değil; yeni metin listesinde yok | Satır "ana ders cümle 7 kısaltması (yeni metin)" diye işaretlendi; S3-A raporu açık nokta 4 listesine ek satır. Metin değişmedi (jüri: anlam ana derse uyar, doğru; aynı öbek cümle 3'te dil jürisinden geçti) | `hikaye-taslak.md` §2 alt satır · `S3-A-RAPOR.md` §5 |

Sayım: jüri maddesi 8 (dil 4 + kaynak 4) → 7 satır (dil 2 = kaynak 1), işlenen 8. Kapak taslağının ikincil izleri (Türkçe İ notu,
yerleşim diyagramında C figürü, uzunluk 9 / 9) madde 1 ve 5'e bağlıdır.

## Uygulanmayan / Nadir kararı

| Madde | Neden |
|---|---|
| dil 3 düzeltmesi S1 dosyasına (`02-04-ydt-temel-s1/aciklama.md`, `aciklama-a.md` "konusu püf noktası") | yazma kapsamı dışı (yalnız S3 paketi); şef / Nadir eşitler |
| `utm_campaign` büyük/küçük harf (S3 büyük, S1 küçük) | kaynak jürisi "karar Nadir'de, madde değil"; S3 istem S3-A gereği büyük harf kaldı |
| Instagram/TikTok dili (D-0278; huni-plan §7 önerisi tersi) | kaynak jürisi "madde değil"; defter eşitlenince karar kimliği doğrulanır |
| `platform_url` canlılığı, TikTok `@ydspublishing` | S1'den devreden yayın öncesi ölçüm; jüri "doğru, yayın öncesi ölçülür" |
