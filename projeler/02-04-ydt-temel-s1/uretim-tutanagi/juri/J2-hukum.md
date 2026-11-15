# J2 hüküm — 02-04-ydt-temel-s1 (yayındaki kısa, kol a) · çıktı jürisi · 15.11.2026

**JÜRİ MODELİ: Sonnet 5.5 (`claude-sonnet-5-5`).**
Üretici modeli: sahne üretimi `gemini-3.8-flash-high` (agy-filo rol `kod`, S1-VAR-RAPOR §66–70). Şef oturum modeli raporda yazılı değil → **bilinmiyor**.
Üretici ile jüri aynı model DEĞİL (§1e: sahne üretimi için sağlandı; şef oturumu için doğrulanamadı).

Ölçüt kaynağı: `juri-olcutleri.md` §2a (HV-1…23) ve §2c (KS-1…10). Ek bulgular §4'te; sayıma girmez.
Jüri yalnız bu dosyayı yazdı; üretim dosyasına dokunmadı. Çıktı karelerinin hepsi Read ile açıldı (kapak A/B/C, hikâye A/B, sahne 01·02·08·03, koyu kareler 5/5).

## 1. Özet

| Sonuç | Sayı | Maddeler |
|---|---|---|
| Geçti (evet) | 28 | HV-1…18, 20, 21, 23 · KS-1, 5…10 |
| Kaldı (hayır) | 4 | HV-19 · KS-2 · KS-3 · KS-4 |
| Kaldı (kanıt yok) | 1 | HV-22 |
| Ek bulgu (sayım dışı) | 5 | §4 (bir tanesi §1b ihlali, bir tanesi dilbilgisi) |

Zaman kapısı (§1b): paketin son içerik değişikliği `2026-11-15T22:38:38+03:00` (`bce68bd`, "bağımsız inceleme düzeltmeleri"). Eski jüri dosyaları
`juri/s1.kaynak-kural.md` 11:38:40 ve `juri/s1.dil.md` 11:39:09 → içerikten ~11 sa ESKİ ve v1 taslağa bakıyor (içinde "Tam ders … dört buçuk dakika" geçiyor).
Bu hüküm dosyası içerikten yenidir. `git status` s1 için değişiklik göstermiyor (22:38 sonrası içerik değişikliği yok).

## 2. Madde tablosu — §2a kısa video

| Kimlik | Hüküm | Kanıt | Not |
|---|---|---|---|
| HV-1 | evet | kare 0 sn (`01-hyperframes-kapak-0.png`), 11,5 sn (`02-paperjs-ornek-11.5.png`), 31,7 sn (`03-hyperframes-cta-31.7.png`) | `ydspublishing` logo + `@ydspublishing`, y ≈ 295–340, x = 60; 3 karede de var, animasyonsuz |
| HV-2 | evet | `senaryo.json` cümle 4 `ses: ogrenci`; `sureler.json` 4. kayıt | perde ölçümü (kendi): cümle 4 medyan 258 Hz, cümle 1–3 145–164 Hz → ikinci ses ayrı ve kadın; `ses-sentez-v2.log` yalnız öğretmen kimliğini yazıyor (öğrenci kimliği log'da yok) |
| HV-3 | evet | `senaryo.json` cümle 4: "Dersin tamamı YDS Publishing YouTube kanalında." | birebir; ses metni `YeDeSe Publishing` (`sentez.wav.rapor.json`) |
| HV-4 | evet | tarama: paket (tutanak, SPEC/RAPOR/BRIEF hariç) `*.html *.js *.json *.md *.svg *.txt` → 0 eşleşme; `ortak/*.js` temiz | "Dersin tamamı" ifadesi kullanılıyor; "Tam ders" yok. Kapak ve hikâye PNG metinleri gözle: yok |
| HV-5 | evet | aynı tarama (`dakika`, `dk`) → 0 | seste, ekranda, açıklamada yok |
| HV-6 | evet | `zaman.json` sahne 3 "Kaydet" (19,99–25,49 sn); `aciklama-a/b.md` ilk satır | ilk satır: "Sınav günü bakmak için kaydet. Dersin tamamı @ydspublishing YouTube kanalında." |
| HV-7 | evet | `03-hyperframes-cta-31.7.png`: kart x 60–960, y ≈ 622–1125 | `ortak/kapak/ana-kapak.png` ile ana paket `kapak.png` aynı görüntü (1920×1080, ort. piksel farkı 0,22/255; md5 farklı = yeniden kodlama). Kapak metni "HER ZAMAN mı ŞİMDİ mi?" — bkz. §4-3 |
| HV-8 | evet | `senaryo.json` | 6/6: sınavda çıkar, en çok yanılınır, tek cümleye sığar, Türkçe köprü ("yaşıyorum"), dersi izlemeden anlaşılır, sınav günü yeniden bakılır. Kural cümlesinin doğruluğu için bkz. §4-2 |
| HV-9 | evet | `find . -name '*.mp4' -o '*.mov' -o '*.webm'` → boş | |
| HV-10 | evet | piksel ölçümü: 5 türevde y 0–280 ve 1570–1920 içerik pikseli 0; sahne kareleri gözle | altyazı y ≈ 1440–1520; en alt öğe hikâye B "Kaydet" (y ≈ 1415–1500) |
| HV-11 | evet | `zaman.json`: 4 sahne, 31,75 sn | hedef 22–26 sn aşılıyor; 35 sn sınırı içinde, D-0279 istisnası kalır |
| HV-12 | evet | `baslar.json`: ilk söz 1,00 sn; `zaman.json` sahne 1 = 3,0 sn | ses kanca cümlesi 6,36 sn'ye dek sürer (üç kısa cümle); ekran kancası 3 sn |
| HV-13 | evet | kart bölgesi (x 60–960, y 600–980) 22,75 sn ↔ 25,4 sn: 0 piksel fark (2,65 sn sabit) | yer imi vektör çizim, "Kaydet" hapı ve "Kaydet." yazısı var; HTML'de emoji 0 |
| HV-14 | evet | `03-hyperframes-cta-31.7.png`; `proje/index.html` `<text id="gerisi" … font-family="Fredoka" font-weight="700">` | `@ydspublishing · YouTube` satırı y ≈ 1180 |
| HV-15 | evet | `senaryo.json`: "Gerisi bizde." (liste 1. madde) | s2 "Bitmedi, gel.", s3 "Bu sadece başlangıç." → derste yinelenme yok |
| HV-16 | evet | `senaryo.json`: "Sınavdan önce lazım olacak. Kaydet." (liste 1. madde) | s2/s3 `Bu kuralı kaybetme. Kaydet.` / `Bir arkadaşına gönder…` → yinelenme yok |
| HV-17 | evet | `araclar/iki-dilli/ses-sozluk.json` `kisaltma.YDS = YeDeSe`; `sentez.wav.rapor.json` `ses_metni` "YeDeSe Publishing" | Whisper "YEDESE Publishing" duyuyor; ses metniyle benzerlik 1,0 (standart §9 bunu kabul ediyor, D-0340) |
| HV-18 | evet | `aciklama.md`, `aciklama-a.md`, `aciklama-b.md` (3 platform) | ilk satır sabit; Reels ve TikTok metninde bağ yok ("profildeki bağlantı") |
| HV-19 | **hayır** | s1: `utm_campaign=ING-YDT-GR-02-04-T` (büyük), `utm_content=s1-a` / `s1-b` doğru. **s2**: `02-04-ydt-temel-s2/aciklama.md:91`, `aciklama-a.md`, `aciklama-b.md` → `utm_campaign=ing-ydt-gr-02-04-t` (küçük harf) | altı paket birlikte aynı biçimde değil (§1d; denetimin 3. hatası bu paketlerde tekrar etti). s1b/s2b/s3b'de açıklama dosyası yok → ölçülemedi. s1 `uretim-tutanagi/aciklama-taslak.md` de küçük harf taşıyor (taslak, çıktı değil) |
| HV-20 | evet | `kapak-a/b/c.png` (kapak.png = kapak-a, md5 aynı), `hikaye-a/b.png`, `aciklama-a/b.md` | 3 kapak altyazısız, kanal katmanlı; karakter: B'de öğrenci (kadın, uzun saç, gözlük), A ve C'de öğretmen figürü. `kapak-b` kaynak kaydı: bkz. KS-5 |
| HV-21 | evet | piksel: `hikaye-a/b.png` y 1150–1380 içerik pikseli 0 | kanal katmanı, kural özeti, Kaydet iki karede de var |
| HV-22 | **kanıt yok** | `node araclar/cakisma-kapisi.mjs 02-04-ydt-temel-s1` → "4 sahne ölçülemedi (ölçüm hatası); kapı geçti sayılmaz": `ECONNREFUSED 127.0.0.1:9333` (tarayıcı havuzu kapalı) | göz denetimi: karelerde çakışma ve taşma yok; yalnız 11,5 sn karesinde bkz. §4-4. Kapı havuz açılınca yeniden koşmalı |
| HV-23 | evet | `sentez.wav.rapor.json`: "Gerisi bizde." 1,0; çekirdek cümle 1,0 | eşik 0,9 |

## 3. Madde tablosu — §2c kapak ve hikâye karesi

KS-2/KS-3 ölçütleri ana ders kapağı (16:9) için yazılmış; kısa türevler `huni-v2-standart.md` §2/§6'ya göre okundu (`kapak-standardi` başlığı da öyle diyor).

| Kimlik | Hüküm | Kanıt | Not |
|---|---|---|---|
| KS-1 | evet | `file`: `kapak-a/b/c.png`, `hikaye-a/b.png` = 1080×1920; koyu kareler 5/5 = 1080×1920 (`sahneler/*/k/koyu/*-koyu.png`) | koyu kareler pakette `k/koyu/` altında; kökte koyu PNG yok ve `surumler.json` yalnız açık listeler (huni §6 koyu PNG istemiyor) |
| KS-2 | **hayır** | `kapak-a/b/c.png`, `hikaye-a/b.png`: rozet **`YDT · BASIC`**; ana kapak kartının içinde `YDT · TEMEL` (`03-…-31.7.png`) | standart: rozet `YDT · TEMEL` (kapak §2, huni §2, §9 açık iş "ilk dokunuşta düzeltilir"). Öteki düzen geçti: 2 satır Fredoka 700, kenar ≥ %5, sağ alt boş, kanal y 295–340, künye y 360–450 |
| KS-3 | **hayır** | `kapak-b.png` zemin (240,236,227) krem + vinyet; koyu (25,24,21) | ölçüt açık `#fece00`/`#141414`, koyu `#141414`. Kısa türevin zemin rengi standartta tanımlı DEĞİL (belge boşluğu; üretim hatası değil). Çıkartma kenarı: B'de krem kenar var, açık zeminle birleşiyor |
| KS-4 | **hayır** | `kapak-b.png` "YAŞIYORUM NASIL DENİR?" ↔ `aciklama-b.md` başlık `"Yaşıyorum" İngilizcede nasıl denir?` | kapak B başlığı yineliyor (yapma listesi #3: kapakta başlığı aynen tekrarlama). A (3 sözcük) ve C (4 sözcük) uzunluk ve yineleme açısından geçti; A = kanca karesi (standart izin veriyor) |
| KS-5 | evet | kapak B karakterinde yazı/harf/rakam/logo yok; `ortak/kapak/karakter.png` md5 = ana paket `ortak/kapak/karakter.png`; ana paket `KAYNAK.json`: `nano-banana-2`, 1k, uretim `3c22184a…` | s1 paketinde `KAYNAK.json` YOK (kaynak ana pakette izlenebilir); panel paketi tek başına taşırsa kayıt gider |
| KS-6 | evet | 168 px genişlikte küçültülmüş A/B/C (kendi ölçümüm) | ana yazı üçünde de okunuyor; pakette `kapak-168.png` yok |
| KS-7 | evet | kapak A "YAŞIYORUM", "İKİ"; B "YAŞI", "DENİR"; hikâye "Şimdilik" | büyük İ, Ş Fredoka glifiyle çiziliyor; HTML `@font-face` latin + latin-ext var; Ğ bu pakette geçmiyor |
| KS-8 | evet | 5 türev | taşma yok (en sağ kenar x ≈ 960 ≤ 1026); yazı karakterle binmiyor |
| KS-9 | evet | 5 türev + 8 sahne karesi | emoji yok (ikonlar vektör). Yapma listesi: #3 dışında uyum (bkz. KS-4) |
| KS-10 | evet | `senaryo.json` `kadro`; kapak B | öğrenci = kadın, genç, uzun kâkül, yuvarlak gözlük ↔ kapak B figürü; öğretmen = erkek ↔ A/C figürü |

## 4. Ek bulgular (sayım dışı)

1. **§1b ihlali:** eski jüri dosyaları içerik değişikliğinden 11 sa eski ve v1 taslağa bakıyor. Bu koşu onları geçersiz kılar; eski iki dosya "geçti" kanıtı sayılmaz.
2. **EK-5b (dilbilgisi): hayır.** Kural kartı "Kalıcıysa geniş zaman, geçiciyse şimdiki zaman." (sahne 3, hikâye A/B, kapak ana ders dahil) fiil sınırı koymadan genelliyor.
   Durum fiillerinde yanlış: `I have a cold this week.` geçici ama basit zaman; `I am having a cold` hatalı. İki örnek cümle (`I live in Istanbul.`, `I am living with my uncle.`) doğru; "yaşıyorum" ↔ iki zaman denkliği doğru. Ana derste aynı genelleme var (`canAlici` "Genel durum, kalıcı durum … V1 / V-s"; geçici için "am/is/are + V-ing"). Sıradaki ders Stative Verbs; öğrenci kartı sınav gününde bu kuralla bakar.
3. **EK-5c: kural cümlelerinde mutlak sözcük yok.** Yalnız iki kullanım not edildi: "**Hep** orada: kalıcı durum, geniş zaman." (durumu anlatıyor, kural değil) ve ana ders kapağı "**HER ZAMAN** mı ŞİMDİ mi?" (soru). İkisi kural iddiası değil; şef kararı.
4. **Sahne 02, 11,5 sn karesi:** ikinci kutu henüz çizilmeden başıboş bir `yor` etiketi (x ≈ 375, y ≈ 920) görünüyor; geçiş ara karesi mi kalıcı kusur mu, kareden ayırt edilemiyor (çakışma kapısı da koşmadı → HV-22).
5. **Arka plan:** bütün karelerde radyal vinyet + tane (köşe 222,218,210 → orta 244,241,232). ST-1 "gradyan yok" ile çelişir; sahne şablonunun parçası (`ortak/hf_tema.py`), ana derste de aynı. İsteğe bağlı: şef ST-1'e vinyet istisnası yazsın ya da şablon sadeleşsin. İngilizce cümlede `İstanbul` (açıklama) ↔ `Istanbul` (ses metni): yazım tutarsızlığı, düşük önem.

## 5. Kaldı maddeleri için düzeltme (tek cümle)

| Kimlik | Düzeltme |
|---|---|
| HV-19 | `02-04-ydt-temel-s2/aciklama*.md` içindeki `utm_campaign=ing-ydt-gr-02-04-t` değerini `ING-YDT-GR-02-04-T` yap; s1 taslak dosyasını da hizala; altı paketi betikle yeniden tara. |
| HV-22 | Tarayıcı havuzu açılınca `node araclar/cakisma-kapisi.mjs 02-04-ydt-temel-s1` koş; 0 uyarı yoksa `yor` etiketini (§4-4) gider. |
| KS-2 | `senaryo.json` `giris.rozetler` değerini `YDT · TEMEL` yap, 8 sahneyi ve 5 türev PNG'yi yeniden üret. |
| KS-3 | Standarda kısa türev satırı ekle ("açık zemin `#f7f3ea`, koyu `#1b1a17`") ya da ölçütü ana derse sınırla; şef karar verir. |
| KS-4 | Kapak B metnini başlık B'den ayır (örn. soru yerine tek kelime köprü) ya da A/B setinin başlık–kapak koşutluğunu standarda istisna olarak yaz. |
| §4-2 | Kural kartına fiil sınırı ekle ("live, work, stay gibi eylem fiilleriyle") ya da kartı örnek cümleye bağla. |

## 6. Ana derse geri besleme

- Kural cümlesi genellemesi (§4-2) ana dersin kural kartında ve `canAlici` satırında da var; durum fiili kısıtı eklenmeli.
- Ana ders kapağı "HER ZAMAN mı ŞİMDİ mi?" soru olarak kalabilir; kapakta "HER ZAMAN" büyük yazı, kural dersi olan bir dersin başlığında mutlak çağrışım yapar (şef kararı).
- Kısa paketlerinde rozet `YDT · BASIC`: kalan 5 kısa ve ders paketleri aynı taramadan geçmeli.
- Altı paketlik `utm_campaign` taramasını betiğe bağla (jüri ölçütü §3-4 hâlâ elle).

## 7. Karar

Teslim kapısı (§1g, D-0338): **GEÇMEDİ.** Kaldı 5 (4 hayır + 1 kanıt yok). Önizleme adresi Nadir'e ve karta bu hâlde yazılmaz; HV-19, KS-2, KS-4 ve HV-22 kapanınca bu jüri yeniden koşar (§1b).
