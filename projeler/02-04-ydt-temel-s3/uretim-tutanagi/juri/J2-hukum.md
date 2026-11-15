# J2 jüri hükmü — 02-04-ydt-temel-s3 (yayındaki kısa, kol a) · ÇIKTI jürisi · 15.11.2026

**Jüri modeli:** Claude Sonnet 5.5 (`claude-sonnet-5-5`), salt okuma. **Üretici model:** raporlarda yazılı değil → "bilinmiyor"; aynılık doğrulanamadı (juri-olcutleri §1e açık nokta sürer).

| Zaman | Değer |
|---|---|
| Bu jüri | 15.11.2026 ≈ 22:55–23:10 (+03:00) |
| Paketin son içerik değişikliği | dosya: `ortak/kunye.js` 19:40 · `sahneler/08-*/proje/index.html` 19:35 · son commit `2026-11-15T19:41:49+03:00` |
| Eski jüri | `juri/s3.dil.md` 12:21 · `juri/s3.kaynak-kural.md` 12:22 (KARAR: DÜZELT) |
| §1b | Bu jüri paket değişikliğinden SONRA (≈ 3 sa). Eski jüri v2 senaryosundan (18:24) ve v2 sahnelerinden (18:55–19:36) ÖNCE; bu paket için geçersiz. |

## Özet

| Hüküm | Sayı |
|---|---|
| Evet (geçti) | 35 |
| Hayır (kaldı) | 9 |
| Kanıt yok (kaldı) | 5 |
| Toplam madde | 49 (§2a 24 · §2c 10 · ek 15) |

**Sonuç: KALDI.** Teslim kapısı (§1g, D-0338) için görsel jüri GEÇTİ sayılmaz. Düzeltme 14 maddeden oluşur: 5 madde yalnız kanıt üretmek, 9 madde gerçek düzeltmedir.

Bakılan çıktı: `senaryo.json`, `sureler.json`, `sozcukler.json`, `sentez.wav.rapor.json` (Whisper), `zaman.json`, `surumler.json`, `aciklama.md/-a/-b`, sahne HTML'leri ve 33 kare (açık + koyu: sahne 01, 02, 03, 08; `kapak-a/b/c`; `hikaye-a/b`; her biri için koyu karşılık). Whisper'ı yeniden koşmadım; `sentez.wav.rapor.json` (18:25) son ses ile aynı koşunun çıktısıdır. Çakışma kapısını koşmadım (tarayıcı gerekir).

## Kaldı maddeleri — kısa liste

| Kimlik | Tek cümle |
|---|---|
| HV-13 | Kaydet sahnesinde "2 sn aynı piksel" kanıtı yok; 18,66 ve 21,3 sn karelerinde karttaki `leaves` vurgusu farklı. |
| HV-22 | Çakışma kapısı son hâl için koşmadı: 08 sahnesinde kayıt yok, 01/02/03 raporları 18:55–19:03 (kunye.js 19:40'ta değişti); 05–07 "ölçülemedi". |
| HV-19 | `utm_campaign` aynı derste tutarsız: `s2` ve `s2b` küçük harf `ing-ydt-gr-02-04-t` (16 kez), `s1`, `s3` büyük harf. |
| HV §3 / DK-1 | Sahne 01 ve 02'de karaoke yok (HTML'de `karaoke` 0 kez); 03 ve 08'de var. |
| KS-3 | Kısa kapakların ve hikâyelerin zemini krem `#f3efe6` (köşe 222,218,210), standart açık zemin sarı `#fece00`. |
| KS-4 | Kapak B'deki "NEDEN -ING YOK?" B setinin YouTube başlığındaki ifadeyle (`Neden -ing yok?`) aynı. |
| KS-5 | `ortak/kapak/` altında `KAYNAK.json` yok (ana derste var); model kaydı kanıtsız. |
| KS-6 | `kapak-168.png` yok. |
| EK-4 | Önizleme adresinin Nadir'e ne zaman gittiğine dair tutanak yok. |
| EK-5b | "Plan → şimdiki zaman / am going" denkliği koşulsuz yazılmış; doğrusu "kesinleşmiş düzenleme". |
| EK-6 | Rozet her kare ve kapakta `YDT · BASIC`; standart `YDT · TEMEL`. |
| EK-8 | Klişe kontak sayfası v1'den kalma (13:24), v2 yok. |
| DK-2 | Altyazı satırları 24 karakteri aşıyor (35–41 karakter). |
| ST-1 | Zemin vinyet gradyanı (`radial-gradient … var(--vin)`); stil anayasası "gradyan yok". |

## §2a — Kısa video (huni v2)

| Kimlik | Hüküm | Kanıt | Not |
|---|---|---|---|
| HV-1 | evet | `k/01-hyperframes-kapak-0.png` (0 sn), `k/02-…-9.5.png` (orta), `k/03-…-28.28.png` (son); ayrıca 15,99 ve 21,33 sn ilk kareleri | Logo x 60, y 298–330; `@ydspublishing` y 295–340. Dört sahnede de var; giriş/çıkış animasyonu yok. |
| HV-2 | evet | `senaryo.json` cümle 5 `ses: ogrenci` (`oPC5…`); `sentez.wav.rapor.json` | Çağrı parçası öğrenci sesi. |
| HV-3 | evet | `senaryo.json` cümle 5; Whisper "Dersin tamamı YEDESE Publishing YouTube kanalında." | Çekirdek cümle birebir. |
| HV-4 | evet | `grep -rniE "tam ders\|full lesson"` senaryo, `sozcukler.json`, `METIN.md`, `aciklama*.md`, sahne HTML, `ortak/*.js` → 0 | `uret.py` ve SPEC dosyalarındaki geçişler yasak liste (tarayıcı), yüzey değil. `kunye.js` temiz. |
| HV-5 | evet | aynı tarama `dakika`, `\bdk\b` → 0 (yüzeylerde) | Yalnız betik yorumlarında "1 dk yük" (yük bekçisi). |
| HV-6 | evet | Sahne 08 (`k/08-…-21.3.png`: yer imi + "Kaydet"); `aciklama*.md` ilk satır | Üç platformun da ilk satırı "Sınav günü bakmak için kaydet. …" |
| HV-7 | evet | `k/03-…-24.82.png`, `-28.28.png`: kart x 60–960, y 620–1127 | ≈ 900×507 (≈ 920×518). `ortak/kapak/ana-kapak.png` ana dersin `kapak.png` ile byte-eş değil (karakter bölgesi farklı: fark kutusu 845,129–1834,1080); görsel olarak aynı tasarım. Geri besleme: ana derse bak. |
| HV-8 | evet | `senaryo.json` | 6 sorudan 4 evet: sınavda çıkar · yanılma noktası · tek cümleye sığar (`Tarife → leaves, plan → am going.`) · sınav günü bakılır. Türkçe köprü yok. |
| HV-9 | evet | `find . -name "*.mp4"` → boş | Paket kökünde ve altında mp4/mov/webm yok. |
| HV-10 | evet | tüm kareler | Yazı ve çizim y 0–280 ile 1570–1920 dışında; en alttaki altyazı y ≈ 1425–1525. |
| HV-11 | evet | `zaman.json` | 4 sahne, 28,31 sn ≤ 35. Hedef 22–26 aşıldı; D-0279 istisnası S1 içindi. |
| HV-12 | evet | `sureler.json` / `METIN.md` | İlk söz 1,00 sn (sınırda, ≤ 1); kanca 3,00 sn. |
| HV-13 | **kanıt yok** | `k/08-…-18.66.png`, `-21.3.png`, `koyu/-19.6.png` | Yer imi SVG ✓, "Kaydet" ✓, tek cümle kartı ✓. Ama kartı 2 sn aralıkla iki karede karşılaştıracak kare yok; 18,66 sn'de `leaves` sarı hap içinde, 21,3 sn'de altı çizili, 19,6 sn (koyu) geçişin ortasında. "2 sn aynı piksel" doğrulanamaz, tersine işaret var. |
| HV-14 | evet | `k/03-…-24.82.png`, `-28.28.png` | Kart konumu doğru; "Bu sadece başlangıç." Fredoka 700; `@ydspublishing` hapı + altında `YouTube` (tek satır `@ydspublishing · YouTube` değil, iki öğe). |
| HV-15 | evet | `s1` "Gerisi bizde." · `s2` "Bitmedi, gel." · `s2b` "Konu burada bitmiyor." · `s3` "Bu sadece başlangıç." | Listeden, yinelenmiyor. `s1b`/`s3b` senaryosu yok, kıyaslanamadı. |
| HV-16 | evet | `s1` "Sınavdan önce lazım olacak. Kaydet." · `s2` "Bu kuralı kaybetme. Kaydet." · `s2b` "Ekran görüntüsü al…" · `s3` "Bir arkadaşına gönder; o da karıştırıyor." | Listeden, yinelenmiyor. |
| HV-17 | evet | `araclar/iki-dilli/ses-sozluk.json`: `"YDS": "YeDeSe"`; `sentez.wav.rapor.json` `ses_metni: "… YeDeSe Publishing …"` | Whisper "YEDESE Publishing" duyuyor, "YDS Publishing" değil; standart §9 bunu kabul etmiş (ses metniyle 1,00). |
| HV-18 | evet | `aciklama*.md` | İlk satır sabit. Instagram ve TikTok açıklamasında bağ yok ("profildeki bağlantı"). |
| HV-19 | **hayır** | `grep -rhoE utm_campaign=` 02-04: `s2/aciklama*.md` ve `s2b/aciklama*.md` → `ing-ydt-gr-02-04-t` (16×); `s1`, `s3` → `ING-YDT-GR-02-04-T` (81×) | `s3` kendi içinde tutarlı (büyük harf, `utm_content=s3-a/b`). Aynı dersin kardeşleri tutarsız. 02-02 paketlerinde hepsi büyük harf. |
| HV-20 | evet | dosya listesi | Kapak ×3 (altyazı yok, kanal katmanı var, B karakterli), hikâye ×2, açıklama ×2. `kapak.png`, `hikaye.png`, `aciklama.md` kopyadır (A ile aynı boyut). |
| HV-21 | evet | `hikaye-a.png`, `hikaye-b.png` ve koyu karşılıkları | Kanal katmanı + kural özeti + Kaydet; y 1150–1380 boş zemin. |
| HV-22 | **kanıt yok** | `sahneler/*/RAPOR.md` | 01 ve 02: "çakışma yok" (18:55–19:03). 03: "kapı GEÇTİ". 08: çakışma satırı yok. 05, 06, 07: çıkış 2, "ölçülemedi". `ortak/kunye.js` 19:40'ta değişti, yani bütün kapı çıktılarından sonra. Gözümle statik karelerde çakışma görmedim ama bu kapı kanıtı değil. |
| HV-23 | evet | `sentez.wav.rapor.json` | Çağrı parçaları 1,00 (ses metniyle); 8/8 parça ≥ 0,98. |
| HV §3 / DK-1 | **hayır** | `grep -c karaoke`: `01/proje/index.html` 0 · `02/proje/index.html` 0 · `03` ve `08` var. `k/02-…-9.5.png`: "Neden -ing yok?" henüz söylenmemişken (9,72 sn) tüm satır tek tip koyu | Huni §3 Sahne 2 (değer) "karaoke" ister; DK-1 karaoke zorunlu. Sahne 03'te gri → koyu, sahne 08'de altı çizgi: iki sahnede iki farklı mekanizma, iki sahnede hiç yok. |

## §2c — Kapak ve hikâye karesi

Açtığım her kare: `kapak-a`, `kapak-b`, `kapak-c`, `hikaye-a`, `hikaye-b` (açık) ve `kapak-a-koyu`, `kapak-b-koyu`, `kapak-c-koyu`, `hikaye-a-koyu`, `hikaye-b-koyu`.

| Kimlik | Hüküm | Kanıt | Not |
|---|---|---|---|
| KS-1 | evet | `file`: hepsi 1080×1920 PNG; koyu karşılıklar `sahneler/*/k/koyu/` altında | Koyu PNG'ler paket kökünde değil, sahne klasörlerinde. |
| KS-2 | evet | `kapak-a/b/c.png` | Ana yazı 2 satır Fredoka 700; üst y 0–280 boş, alt (y > 1400) boş. Ölçüt metni yatay/ana dikey düzeni anlatıyor ("orta bant y 600–1320", "üst %20 boş"); kısa kapakta HV-1 gereği kanal katmanı y 295–340'ta, yani üst %20 içinde. İki standart çelişiyor, uygulama huni v2'ye uyuyor. |
| KS-3 | **hayır** | `kapak-a/b/c.png`: köşe (222,218,210), orta (244,241,232) krem; koyu zemin `#1b1a17` | Standart: açık sarı `#fece00`, koyu `#141414`. Aynı karede CTA'daki ana ders kartı sarı, kısa kapağın kendisi krem. Kapak A "kanca karesi" ise krem doğal; B ve C için standart sarı ister. Çıkartma kenarı (B): açıkta çok silik, koyuda belirgin. |
| KS-4 | **hayır** | `kapak-b.png` "NEDEN -ING YOK?" ↔ `aciklama-b.md` YouTube başlığı "Tren de plana göre kalkmıyor mu? Neden -ing yok? …" | B kapağı B başlığını yineliyor. A "TARİFE ≠ PLAN" sahne 1 yazısıyla aynı (huni §6 bunu istiyor: A = kanca karesi); C "İKİ ÖRNEK İKİ ZAMAN" 4 sözcük, yinelenme yok. |
| KS-5 | **hayır** | `find . -name "KAYNAK*"`: yalnız `sahneler/*/cizim/KAYNAK.md` (çizim kaynağı); `ortak/kapak/` içinde `karakter.png` ve `ana-kapak*.png` var, `KAYNAK.json` yok. Ana derste `02-04-ydt-temel/ortak/kapak/KAYNAK.json` var. | Görselde yazı, harf, rakam, logo yok (`karakter.png` RGBA, şeffaf). Model `nano-banana-2` pakette belgelenmemiş. |
| KS-6 | **kanıt yok** | `kapak-168.png` yok | Kendi küçültmem (168×299, `/tmp/j2-kapak-168.png`, pakete eklenmedi): üç kapakta ana yazı okunuyor. Kanıt dosyası yine de yok. |
| KS-7 | evet | `kapak-a.png` (TARİFE, İzmir), `kapak-c.png` (İKİ, ÖRNEK), CTA kartı (ŞİMDİ) | İ, Ş doğru çiziliyor, yedek yazı tipine düşmüyor. Ğ bu kapaklarda yok. |
| KS-8 | evet | `kapak-b.png`, `kapak-c.png` | Taşma yok; karakter yazıya binmiyor (C'de figür kutunun dışında, sağda). |
| KS-9 | evet | bütün kareler | Emoji yok; yer imi ve kâğıt uçak SVG. Gradyan için ST-1'e bak. |
| KS-10 | evet | `senaryo.json` `kadro.ogrenci: kadin, GlassRound, LongBangs`; `kapak-b.png`, sahne 02 | Karakter kadın, uzun saç, gözlük: eşleşiyor. Sahne 02'deki öğretmen figürü erkek: `kadro.ogretmen: erkek` ile eşleşiyor. |

## Ek maddeler (§2b ve metin taramaları; görevde açıkça aranan hatalar)

| Kimlik | Hüküm | Kanıt | Not |
|---|---|---|---|
| EK-1 | evet | `sentez.wav.rapor.json` | "YDT" anlatımda yok; "YDS" → "YeDeSe" (sözlük); `-ing` → `/ɪŋ/`; "p.m." İngilizce cümlede. |
| EK-2 | evet | bütün kareler | Emoji yok. |
| EK-3 | evet | matris: dikey × açık+koyu × (sahne 01, 02, 03, 08; kapak A/B/C; hikâye A/B) | Boş hücre yok. Koyu örnek karelerden ikisi geçiş ortasında (02 @13,5; 08 @19,6). |
| EK-4 | **kanıt yok** | `surumler.json`: `durum: inceleme`, `onizleme` adresi yazılı | Adresin Nadir'e ya da karta gittiği zamanı gösteren tutanak yok; GEÇTİ'den önce gitmediği doğrulanamaz. |
| EK-5a | evet | tüm kareler, sahne HTML | Üstü çizili ya da "yanlış" işaretli cümle yok. |
| EK-5b | **hayır** | `kapak-a.png`, `hikaye-a.png` "Tarife → leaves, plan → am going."; `aciklama-a.md` başlık "Tarife geniş zaman, plan şimdiki zaman" | İki örnek cümle doğru. Denklik koşulsuz: "plan" tek başına şimdiki zaman demek değil; `be going to` ve `will` da plan bildirir. Doğrusu: kesinleşmiş düzenleme (zaman, yer, kişi belli) → Present Continuous; kurumsal tarife → Simple Present. `am going` görsel olarak `am going to` ile de karışabilir. Ana ders aynı "planlanmış gelecek" ifadesini taşıyor (`surumler.json` amaçlar); ana derse geri besleme. Ek: sahne 02 "Planı bir kişi yapar" cümlesi öğrencinin haklı sorusuna ("tren de plana göre kalkmıyor mu?") cevap vermiyor, tarifeyi de bir kurumun yaptığı plan yapıyor; "kişisel karar ↔ sabit tarife" ayrımı daha doğru. |
| EK-5c | evet | senaryo, başlık, kapak, açıklama | "Her zaman / hep / always" kısa paketin hiçbir yüzeyinde yok. Son sahnedeki ana ders kartı "HER ZAMAN mı ŞİMDİ mi?" soru biçiminde, iddia değil. |
| EK-6 | **hayır** | bütün kareler, `senaryo.json` `giris.rozetler`, `meta` | Şablon kaynaklı sabit metin: rozet `YDT · BASIC` (standart `YDT · TEMEL`, huni §9 açık iş, Ç4 kararı). Aynı karede CTA'daki ana ders kartı `YDT · TEMEL` diyor. `s1`, `s2`, `s2b` senaryolarında da `BASIC` var. Yazım/tamlama hatası bulunmadı (`konusunun püf noktası` doğru); küçük tutarsızlık: ses/senaryo "p.m.", ekran ve açıklama "7 pm". `{UZUN_VIDEO_URL}` yer tutucusu dolmadı (belgelenmiş). |
| EK-7 | evet | 10 koyu kare | Kapak, hikâye, sahne 01, 02, 03 koyuda okunuyor. Sahne 08 @19,6: `leaves` hapı sönerken koyu mürekkep kahverengi zeminde kısa süre düşük kontrast (≈ 0,1 sn geçiş; HTML: hap söner, `leaves,` 0,10 sn sonra gelir). Kalıcı karede sorun yok. |
| EK-8 | **kanıt yok** | `uretim-tutanagi/kontak/s3-huni-yanyana.png` 13:24 | v1 kontak sayfası; v2 kontak yok. 18 maddelik klişe sayımı yapılamaz. Gözle bakışta işaret görmedim (mor gradyan, neon, 3B yok), ama ST-1 vinyeti için aşağıya bak. |
| EK-9 | evet | `senaryo.json` cümle 2 | 1 soru anı, 10 sözcük; soru sonrası boşluk 0,75 sn (10,76 → 11,51). |
| EK-10 | evet | `sentez.wav.rapor.json` | `-ing` → `/ɪŋ/` ses metninde, şık harfi yok, tire kuralı uygulanmış. |
| EK-12 | evet | `k/02-…-3.png`, `-9.5.png`, `-15.96.png`; `k/08-…` | Kartlar ve oklar söylenen sözcükle birlikte ya da sonra geliyor. Motor zaman kapısı çıktısı pakette yok; yalnız kare düzeyinde doğruladım. |
| DK-2 | **hayır** | `k/02-…-9.5.png`, `-15.96.png`, `k/08-…-21.3.png` | Altyazı satırları 35–41 karakter ("Planı bir kişi yapar. Tren tarifeye uyar:"), ölçüt ≤ 24. Sahne 02'de TR soru hem baloncukta hem altyazıda iki kez yazılı; balondaki TR yazı EN kartlar kadar büyük ("TR soluk" ihlali). |
| ST-1 | **hayır** | `sahneler/*/proje/index.html` satır 14: `radial-gradient(circle … rgba(0,0,0,var(--vin)))`; kare köşe (222,218,210) → orta (244,241,232) | Stil anayasası: "Gradyan, parlama, gölge yok". Vinyet düz zemini gradyana çeviriyor. Şef: ya vinyeti kaldır ya anayasaya istisna yaz. Tek vurgu rengi: amber çizgi + sarı hap + yeşil ✓ (hikâye B'de yeşil yalnız doğru şıkta) kabul. |

## Düzeltme önerileri (kaldı maddeleri, tek cümle)

| Kimlik | Öneri |
|---|---|
| HV-13 | Kaydet sahnesinde kartı 2 sn sabit tut (vurguyu kart girişinden önce bitir) ve iki kareyi 2 sn arayla çekip piksel farkını ölç. |
| HV-22 | `node araclar/cakisma-kapisi.mjs 02-04-ydt-temel-s3` komutunu son `kunye.js` ve sahne 08 ile koştur, çıktıyı `sahneler/*/RAPOR.md` yerine paket tutanağına yaz. |
| HV-19 | `s2` ve `s2b` açıklamalarında `ing-ydt-gr-02-04-t` değerlerini `ING-YDT-GR-02-04-T` yap, `grep` ile 0 küçük harf doğrula. |
| HV §3 / DK-1 | Sahne 01 ve 02'ye karaoke ekle ve 03/08 ile aynı mekanizmaya (gri → koyu ya da altı çizgi) birleştir. |
| KS-3 | Kapak B ve C (isteğe bağlı A) zeminini açıkta `#fece00`/`#141414`, koyuda `#141414` yap; kısa kapak için krem kalacaksa `kapak-standardi.md`'ye "kısa kapak = kanca karesi teması" istisnasını yaz. |
| KS-4 | Kapak B'yi başlıkla çakışmayan 2–4 sözcükle değiştir ya da B başlığından "Neden -ing yok?" ifadesini çıkar. |
| KS-5 | `ortak/kapak/KAYNAK.json` dosyasını ana dersten kopyala/güncelle: `uretim_id`, `nano-banana-2`, istem, tarih. |
| KS-6 | `kapak-a/b/c-168.png` dosyalarını üret ve pakete koy. |
| EK-4 | Önizleme adresini Nadir'e yazmadan önce bu jürinin GEÇTİ saatini tutanağa yaz. |
| EK-5b | Kural kartını "kesinleşmiş düzenleme → am going · tarife → leaves" olarak güncelle; başlıkta "plan şimdiki zaman" yerine "tarife geniş zaman, düzenleme şimdiki zaman" yaz. |
| EK-6 | `senaryo.json` `giris.rozetler`, `kunye.js` ve `meta` içinde `YDT · BASIC` → `YDT · TEMEL`; `s1`, `s2`, `s2b` aynı değişiklik. |
| EK-8 | v2 sahnelerinden yeni kontak sayfası üret; 18 madde sayımını yaz. |
| DK-2 | Altyazıyı 24 karakter satırlara böl; sahne 02'de TR soruyu yalnız baloncukta ya da yalnız altyazıda göster. |
| ST-1 | `--vin` değerini 0 yap (düz zemin) ya da stil anayasasına vinyet istisnası yaz. |

## Ana derse geri besleme (`02-04-ydt-temel`)

- "Plan = planlanmış gelecek = şimdiki zaman" denkliği (`amaclar`, `canAlici`) aynı eksik genellemeyi taşıyor; "kesinleşmiş düzenleme" ifadesi doğru.
- `kapak.png` ve paketteki `ortak/kapak/ana-kapak.png` byte-eş değil; kısa pakete kopyalanan sürümün tek kaynak olduğunu garantile (sha256 kaydı).
- Rozet metni `YDT · BASIC` ders ailesinin bütün kısalarında var; şablon kaynağında bir kez düzelt.
- `utm_campaign` büyük/küçük harf tutarsızlığı `s2` ile `s2b`'de kaldı; `s1`, `s3` doğru.
- `kapak-standardi.md` KS-2 ve KS-3 ölçütleri kısa kapak için ayrı bir satıra ihtiyaç duyuyor (kanal katmanı üst %20'de; kanca karesi teması).

Not: `juri-olcutleri.md` §3'teki betikler (metin taraması, utm, kapsam matrisi) hâlâ yazılmadı; bu jüri onları elle yaptı: metin taraması `grep`, utm `grep -rhoE`, kapsam matrisi yukarıdaki EK-3 satırı.
