# İstem S1-A raporu — 02-04-ydt-temel-s1 huni seti taslağı · 15.11.2026

| Dosya | İçerik | Durum |
|---|---|---|
| `senaryo-taslak.md` | Shorts 3 sahne (kapak · örnek · tam ders çağrısı), 3 cümle, ses/ekran/görsel tablosu, süre | TASLAK |
| `kapak-taslak.md` | kapak 1080×1920: başlık `YAŞIYORUM` / `= İKİ ZAMAN`, kod, görsel, rozet, `senaryo.json` alanları | TASLAK |
| `hikaye-taslak.md` | hikâye karesi PNG (+ isteğe bağlı MP4 ≤ 15 sn), dil kararı, UTM | TASLAK |
| `aciklama-taslak.md` | YouTube / Instagram / TikTok metni, UTM tablosu, yer tutucular | TASLAK |
| `S1-A-RAPOR.md` | bu rapor | — |

Yapılmayan (istem kuralı): ses sentezi, ElevenLabs çağrısı, sahne kodu, render, git commit, alt ajan, Kovan yazımı (yazma kapsamı dışında).

## 1. Sahne süreleri (tahmin)

| Sahne | Motor | sn | Süre | Ölçü |
|---|---|---|---|---|
| 01 kapak | HyperFrames | 0,00–3,00 | 3,0 | giriş sabit 3 sn, ilk söz 1,00 (K23) |
| 02 örnek | Paper.js | 3,00–18,71 | 15,7 | cümle 1 ölçülmüş (5,36 sn); cümle 2 tahmin, 24 sözcük × 122 sözcük/dk |
| 03 tam ders çağrısı | HyperFrames | 18,71–26,96 | 8,3 | cümle 3 tahmin, 13 sözcük × 117 sözcük/dk + 1,0 sn kuyruk |
| Toplam | | | ≈ 27 sn | aralık 25–29 sn; kalıp 15–30 sn |

Hız ölçüsü ana dersin gerçek sesinden: öğretmen 468 sözcük / 240,0 sn = 117 sözcük/dk (`ortak/anlatim/sureler.json`).

## 2. Kararlar ve gerekçe

1. **Can alıcı = ana ders kancası.** Cümle 1 ana ders cümle 1 ile birebir aynı; cümle 2 kancanın iki kartını ve
   Örnek 2'nin "kalıcı / geçici" etiketlerini taşır. Gerekçe: istem tutarlılık şartı; Shorts'tan gelen izleyici uzun derste aynı açılışı duyar.
   Bütün cümleler jüriden geçmiş ana ders metninden türedi; yeni kural ve yeni örnek cümle yok.
   **S1-C düzeltmesi (15.11, jüri kaynak-kural madde 4):** kavramlar ve örnekler ana dersten; bağlayıcı TR cümleler yeni
   (`İngilizcede ikisi ayrılır.` · `Hep orada: kalıcı durum, geniş zaman.` · `Şimdilik: geçici durum, şimdiki zaman.` ·
   `Üç farkın hepsi dört buçuk dakikada.` · S1-C eki `Bu, üç farktan yalnız biri.`). D-0204 jürisi bu metni görmedi.
2. **Cümle 1 sesi yeniden kullanılabilir (hesaplamadan önce 3 soru, soru 2).** Ana dersin `cumle-1.wav` dosyası (5,36 sn) Whisper
   kapısından geçmiş durumda. Sentez yalnız cümle 2 ve 3 için gerekir (37 sözcük). Ses adımı ayrı istemdedir; karar orada uygulanır.
3. **Tek örnek çifti, tek kart sütunu.** Kalıp §5 "1 örnek cümle" der. Can alıcı bir karşıtlıktır; tek cümle yeni türetilmiş cümle ister.
   Bu yüzden kancanın jüri onaylı iki kısa cümlesi tek sütunda üst üste durur. `I am living with my uncle.` 26 karakter → 2 satır (sınır 24).
4. **Kapanış: süre ölçülmüş, "kanal" yok.** Ses: "Üç farkın hepsi dört buçuk dakikada." (265,7 sn = 4 dk 26 sn → "dört buçuk").
   Ekran: `@ydspublishing`. Kimlik sesle okunmaz (harf harf okunma riski). QR yok.
5. **Hitap yok.** Shorts sesi sen/siz kullanmaz. Gerekçe: tek video üç platforma ve iki kitleye gider (karar A: tek üretim).
6. **Kapak = ilk kare.** Başlık 0. karede tam; kalem hareketi yalnız `YOR` altçizgisinde. Gerekçe: TikTok ve Instagram'da kapak seçilmezse ilk kare görünür.
7. **Sarı yazı yerine sarı hap.** `= İKİ ZAMAN` ve `@ydspublishing` hap içinde (açık temada sarı yazı kontrastı ≈ 2,3:1; kalem `sozlesme.md` 14.11).
   **S1-C düzeltmesi (15.11, jüri kaynak-kural madde 1):** hap = dolgu `#ffe066` (`RENK.vurguDolgu`), yazı `#1b2440` (`RENK.pilMetin`);
   kaynak `present-continuous-ileri-s1/ortak/kunye.js` satır 9–10, 139–140. "Kalem `sozlesme.md` 14.11" atfı geçersiz (o satır ses hattıdır).
8. **Instagram/TikTok dili: öğretmen + YDT öğrencisi, veli dili yok.** Gerekçe `hikaye-taslak.md` §2 (YDT 17–18 yaş yasak dışında;
   §7 veli önerisinin kaynağı 14 yaş Maarif kitlesi). YouTube: öğrenci + öğretmen ortak (§7).
9. **Platform adresi dolduruldu, yer tutucu yedekte.** `https://ydspublishing.com/grammar/02-04-ydt-temel`
   (kaynak: dijital-anlatim `sozlesme.md` madde 5, K35, `worker/grammar-kapi/wrangler.toml`). YouTube uzun ders adresi `{UZUN_VIDEO_URL}`.

## 3. Açık noktalar

| # | Nokta | Etki | Önerim |
|---|---|---|---|
| 1 | grammar-kapi Worker canlı değil (belge 11.11: "Worker yayında değil, R2'ye yazılmadı"); canlılığı ölçmedim | ders sayfası bağlantısı 404 verebilir | paylaşımdan önce adres açılır; açılmazsa satır çıkar |
| 2 | Ana ders `surumler.json` durumu `inceleme`; 02-04-ydt-temel sahnelerinde commit edilmemiş değişiklik var | yeniden render süreyi değiştirirse "dört buçuk dakika" ve "4 dakika 26 saniye" yeniden ölçülür | yayın anında ffprobe (huni-plan §4: elle süre yasak) |
| 3 | Profil bağlantısı tek; her paylaşımda derse göre değişirse eski gönderiler yanlış derse gider | ölçüm karışır | ders listesi sayfası (yoksa açılır) ya da bağlantı sayfası |
| 4 | TikTok `@ydspublishing` adı ve profil bağlantısı koşulu doğrulanmadı | TikTok çağrısı boşa düşebilir | hesap açıldığında doğrulanır |
| 5 | Biçim örneği present-continuous-ileri-s1'de `senaryo.json` cümle 3 hâlâ "Tam dersi kanalda izle" diyor; `BRIEF-S1.md` ve `METIN.md` "6 dakika" taşıyor; dikey kalıp §5 şablonu `@ydspublishing · 6 dk` | sonraki S1 paketleri yanlış kalıbı kopyalayabilir | kalıp §5 satırı ve örnek paket düzeltilir (bu istemin yazma kapsamı dışında) |
| 6 | `kadro.ogretmen` ana ders `senaryo.json`'da yok; present-continuous-ileri-s1 kaydı önerildi | figür seçimi | sahne kodu isteminde ana ders kadrosuna eklenir |

**Nadir'e soru:** Instagram/TikTok metni öğretmen + YDT öğrencisi diliyle mi kalsın, veli dili yalnız Maarif 9–10'da mı? Önerim: evet.
