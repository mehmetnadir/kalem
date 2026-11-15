# KBJ-0202S1 jüri hükmü — simple-present-temel-s1b (A/B kol b, değişken `kanca`) · 15.11.2026 23:17

**Jüri modeli: Claude Sonnet 5.5 (`claude-sonnet-5-5`), tek oturum, alt ajan yok.**
**Üretici modeli: Claude Opus 5.5 (`claude-opus-5-5`)** (KBC-RAPOR.md). İkisi farklı: §1e sağlandı.

Kapsam: `juri-olcutleri.md` §2a (HV-1…23) + §2d (AB-1…7) = 30 madde. Paket: `projeler/simple-present-temel-s1b/`; karşılaştırma `simple-present-temel-s1/`.
Bakılanlar: `senaryo.json`, `sureler.json`, `sentez.wav.rapor.json`, `zaman.json`, `surumler.json` (iki kol), `aciklama{,-a,-b}.md`, `ortak/kunye.js`,
kol b kareleri (kanca 0 / 2,2 / 2,95 / koyu 2,65 · kapak + koyu kapak · değer 4,25 / 6,2 / 14,9 + koyu 4,25 / 8,8 · kaydet 16,2 + koyu 17,65 ·
çağrı 20,9 / 23,95 + koyu 23,95), kol a karşılaştırma kareleri (kapak, değer 8,8), `diff -rq` (82 satır, kendim koştum), sha256, `ffprobe`, metin taramaları.
Jüri zamanı 23:17; paketin son içerik değişikliği `surumler.json`/`aciklama*.md` 23:10 → §1b sağlandı.

## Özet

| Hüküm | Sayı | Maddeler |
|---|---|---|
| Geçti (evet) | **19** | HV-2,3,4,5,6,8,9,10,11,15,16,17,18,19,20,23 · AB-1,2,6 |
| Hayır | **2** | HV-12 · AB-3 |
| Kanıt yok | **9** | HV-1,7,13,14,21,22 · AB-4,5,7 |
| **Kaldı** (hayır + kanıt yok) | **11** | |

Kök neden 1 (6 madde): sahne 03 ve 04 karelerinin hepsi KOL A'DAN KOPYA (mtime 19:23 ve 19:28; 04 karesi `cmp` ile kol a ile bayt aynı). Kol b'nin
`qa-yerel.sh` koşusu yalnız 01 ve 02 için yapılmış (KBC-RAPOR §7). 03/04 `proje/index.html` kol a ile bayt aynı (`cmp`) ama jüri kare olmadan var saymaz.
Kök neden 2: kanca cümlesi 4,45 sn'de bitiyor ve sahne 02'ye taşıyor (HV-12, AB-3).
Kök neden 3 (3 madde): Şef ya da API girdisi gerekiyor (AB-4, AB-5, AB-7); jüri kanıt göremez.

## Madde tablosu — §2a kısa video

| Kimlik | Hüküm | Kanıt | Not |
|---|---|---|---|
| HV-1 | kanıt yok | 0. sn: `01-…/k/01-hyperframes-kanca-0.png` (kanal katmanı y 296–339, x 60) · orta: `02-…/k/…-4.25.png`, `koyu/…-8.8.png` (görünür) · SON kare: `04-…/k/…-23.95.png` kol a kopyası | Üç karenin ikisi kol b'ye ait; son kare kol b'nin değil. Kol b son karesi çekilmeli |
| HV-2 | evet | `sentez.wav.rapor.json` cümle 4 öğrenci sesi (`ogrenci` `…M29gjY`); `senaryo.json` cümle 4 `ses: ogrenci` | Whisper 1,00 |
| HV-3 | evet | `senaryo.json` cümle 4 parça 2: "Dersin tamamı YDS Publishing YouTube kanalında." · Whisper "…YEDESE Publishing…" (HV-17 ile uyumlu) | |
| HV-4 | evet | `grep -riE 'tam ?ders|full lesson'` senaryo, altyazi, METIN, aciklama*, `ortak/*.js`, sahne HTML/JS: 0. Yalnız `SPEC.md`/`RAPOR.md` yasak alıntısı (iç belge) | |
| HV-5 | evet | `grep -riE 'dakika|\bdk\b'` aynı yüzeyler: 0 | |
| HV-6 | evet | Sahne 3 kaydet kartı + `Kaydet` düğmesi (`koyu/03-…-17.65.png`) · açıklama ilk satırı "Sınav günü bakmak için kaydet. …" (3 dosya) | Kaydet sahnesinin kendi karesi kol a kopyası (HV-13) |
| HV-7 | kanıt yok | `04-…/k/…-23.95.png` kol a kopyası; kart x 60–960, y ≈ 622–1125 (≈ 900×503; ölçü 920×518'den %2 küçük, kabul) | İçerik doğru görünüyor ama kol b karesi yok |
| HV-8 | evet | Altı sorudan altısı evet: sınavda çıkar, öğrenci karıştırır (go/goes), tek cümle ("He, she, it: s gelir"), Türkçe köprü ("Kardeşim gider"), dersi izlemeden anlaşılır, sınav günü bakılır | |
| HV-9 | evet | `find simple-present-temel-s1b -name '*.mp4'` → 0 | |
| HV-10 | evet | 01/02 kol b kareleri: y 0–280 ve 1570–1920 boş (altyazı 1440–1500 aralığında) | 03/04 yalnız dolaylı (bayt aynı HTML) |
| HV-11 | evet | `zaman.json`: 4 sahne, toplam 24,33 sn (≤ 35; hedef 22–26) · `ffprobe` m4a 24,330000 | |
| HV-12 | **hayır** | İlk söz 1,00 sn (evet). Kanca cümlesi 1,00–**4,45** sn (`sureler.json` i=1 + `baslar`); standart §3 kanca 0–4 sn | Kol a da 4,12 (aşıyor). Üretici açık nokta 6 "kanca değişkeninin sonucu" diyor; ölçüt yine hayır |
| HV-13 | kanıt yok | `03-…/k/…-16.2.png` ve `…-17.65.png` kol a kopyası (19:23) | "2 sn aynı piksel" kol b'de ölçülmedi |
| HV-14 | kanıt yok | `04-…/k/…-20.9.png` kol a kopyası. Bu karede `@ydspublishing · YouTube` yok (yalnız `@ydspublishing`), 23,95'te var | Kol b karesi çekilince 20,9 yerine sahne ortası seçilmeli |
| HV-15 | evet | Giriş "Gerisi bizde." listede (§4); derste tek | |
| HV-16 | evet | "Sınavdan önce lazım olacak. Kaydet." listede; derste tek | |
| HV-17 | evet | `ses_metni` "YeDeSe Publishing"; Whisper "YEDESE Publishing"; ekran "YDS Publishing" | |
| HV-18 | evet | `aciklama{,-a,-b}.md` ilk satır sabit; Reels/TikTok blokları bağsız | |
| HV-19 | evet | Bütün `aciklama*.md` bağlarında `utm_campaign=ING-YDT-GR-02-0x-T` büyük harf (117 + 111 satır; küçük harfli bağ 0). `utm_content=s1b-a` / `s1b-b` | Ek bulgu 4: 02-04 s2/s2b `aciklama*.md` 91. satırda bayat DİKKAT notu "S1 küçük harf yazar" duruyor |
| HV-20 | evet | Kol b: `kapak.png` = `kapak-a.png` (kanca karesi: altyazı yok, kanal katmanı var, karakter var, ✗ var) + `aciklama-a/b.md`. Kapak B/C ve hikâye A/B kol a paketinde (AB §4) | Grup düzeyi toplam 3 / 2 / 2 sağlanıyor |
| HV-21 | kanıt yok | Kol b'de hikâye karesi yok (AB §4: kol a'da) | Kol a hikâye karelerine bu jüri bakmadı; kol a jürisi kapsar |
| HV-22 | kanıt yok | `araclar/cakisma-kapisi.mjs` bu makinede (`dijital-anlatim/araclar/`) yok; rapordaki "0 uyarı" üretici çıktısı | Mac'te ya da kapı betiğiyle jüri yeniden koşmalı |
| HV-23 | evet | `sentez.wav.rapor.json`: 10/10 parça benzerlik 1,00 (eşik 0,9) | |

## Madde tablosu — §2d A/B kolu

| Kimlik | Hüküm | Kanıt | Not |
|---|---|---|---|
| AB-1 | evet | `surumler.json`: kol a `s1` (`kol a, kanca, kopru`) + kol b `s1b` (`kol b, kanca, yanlis-cumle`); atama s1 → kanca | Grupta tam 2 kol |
| AB-2 | evet | `diff -rq`: 82 satır. Sınıflar (kendi sayımım üreticiyle tutuyor): senaryo/ses/zaman türevi, sahne 01/02 klasörleri, kapak A, açıklama utm, `surumler.json`, grup türevi çıkarımı (kol a'da kalan `kapak-b/c`, `hikaye*`, sahne 05–08), tutanak. Değer cümlesi sesi `cumle-2/3/4.wav` sha256 eşit (`bb9402db…`, `9cb210d9…`, `dd50c6bc…`). `kunye.js` farkı yalnız `KOK` yolu (`diff` tek satır) | `kunye.js` sınıf dışı ama içerik değil yol: kabul. Açıklama metni utm dışında kol a ile aynı (`diff`) |
| AB-3 | **hayır** | Değer sahnesi (02) iki kolda aynı değil: kol b `sahne-02.js` değişti (kanca izi 1–3: `Hata nerede?` kuyruğu, kırmızı ✗, "go" kartı devri), sahne 359 → 371 kare, değer cümlesi 5,00'te başlıyor (kol a 4,67). Kanal katmanı, çekirdek cümle (sha256) ve ses kadrosu aynı (evet) | Son hâl (kare 14,9 ↔ kol a 8,8 düzeni) aynı; fark kanca 02'ye taşınmış olmasından. Düzeltme: kancayı 4 sn'de sahne 01 içinde bitir |
| AB-4 | kanıt yok | Yayın takvimi yok | Şef maddesi |
| AB-5 | kanıt yok | Dosya tarafı evet (mp4 0, HV-9). API yanıtı (`mp4: null`) görülmedi | |
| AB-6 | evet | `surumler.json` s1b: `varyant {grup s1, kol b, degisken kanca, deger yanlis-cumle}`; açıklamalarda `utm_content=s1b-a/-b` | |
| AB-7 | kanıt yok | Sonuç tablosu yok | Şef maddesi (kazanan ilanı) |

## İki kolun yan yana kıyası (söz, ekran metni, kapak, açıklama)

| Öğe | Kol a | Kol b | Değişken mi? |
|---|---|---|---|
| Kanca sözü | (köprü) "GO mu, GOES mu?" kapağı; cümle 1 | "My brother go to school by bus. Hata nerede?" | evet |
| Kapak (A) | GO mu, GOES mu? + sarı hap | MY BROTHER / GO. + kırmızı ✗ | evet |
| Değer, kaydet, çağrı sözü | aynı sha256 | aynı sha256 | hayır (iyi) |
| Süre | 24,00 | 24,33 | kanca sonucu (+0,33) |
| Açıklama metni | — | utm dışında aynı | hayır (iyi) |
| Rozet | `YDT · BASIC` | `YDT · BASIC` | hayır (iki kolda aynı) |

## Değişkenle ilgisiz ek bulgular (kaldı sayılmadı; ana derse ve kol a'ya geri besleme)

1. **Kural cümlesi "s" ama gösterilen "-es".** Ses ve kaydet kartı "he, she, it: **s** gelir", sahne 02 `go-es` içinde `es`'i çember içine alıyor, `go` yanında `s` kırmızıyla çiziliyor. `go → goes` ekinin adı "s/es"; "s" tek başına yanıltır. Kol a ve ana derste de aynı (EK-5b nitelikli hayır). Öneri: "fiile s ya da es gelir" ya da kartta `-s / -es`.
2. **Rozet metni** `YDT · BASIC`; standart §9 `YDT · TEMEL` ister. Aynı çağrı karesinde ana ders kapağı `YDT · TEMEL`, kanal hapı `YDT · BASIC` diyor (iç tutarsızlık). İki kola birlikte düzeltilmeli.
3. **Açıklama dosyalarında kol a kimliği kalmış:** başlık "# simple-present-temel-s1 · açıklama metni", "Sürüm: A (`s1-aciklama-a`)"; kimlik `s1b-aciklama-a`. Ayrıca "Kapak: `kapak-c.png`", "Hikâye: `hikaye-a.png`", "`hikaye-b.png`" kol b paketinde olmayan dosyaları gösteriyor (kırık yol). Üretici açık nokta 3'ü yalnız "Sürüm" satırı için yazmış.
4. **Bayat uyarı:** `02-04-ydt-temel-s2` ve `s2b` `aciklama*.md` 91. satır "S1 `utm_campaign` küçük harf yazar" notu artık yanlış (bütün bağlar büyük harf).
5. **EK-11 kulak kararı açık:** TTS "My brother go" kasıtlı yanlış cümleyi doğru okudu (Whisper `go`, 1,00); Nadir kulağıyla onaylanmadı. Shorts kapağı kasıtlı yanlış İngilizce taşıyor; ✗ var ama küçük görünümde (168 px) ✗ yaklaşık 19 px — `kapak-168.png` kanıt dosyası yok (KS-6 için üretilmeli).
6. **Kol b sahne 03/04 `zamanlar.json` kayması** (+0,33 sn) ve `proje/` yeniden üretimi doğru, ama kareler tazelenmedi (kök neden 1).

## Kaldı maddeleri — düzeltme önerisi (tek cümle)

| Kimlik | Düzeltme |
|---|---|
| HV-1, 7, 13, 14 | Sahne 03 ve 04 için `qa-yerel.sh simple-present-temel-s1b 03-hyperframes-kaydet … --hazirla` ve 04 için aynısını kol b zamanıyla koştur; son kare, çağrı ortası (`@ydspublishing · YouTube` görünen an) ve kaydet karesi kol b'ye ait olsun. |
| HV-12 | "Hata nerede?" → "Hata?" ya da cümle 1'i hızlandır; kanca bitişi ≤ 4,00 sn. |
| AB-3 | Kanca bitişi 4 sn'ye inince 02'ye taşan kuyruk (✗ kayışı, kanca kartı sönmesi) kısalır; değer sahnesini kol a ile bayt eşitliğine yaklaştır ya da AB §3'e "kanca kuyruğu 02 başında kalabilir" notu ekle (şef kararı). |
| HV-21 | Şef kararı: kol a hikâye karelerinin jürisi kol a jürisinde; bu madde kol b için "geçersiz" ilan edilirse AB §4 ve `juri-olcutleri.md` §2c'ye yazılmalı. |
| HV-22 | Çakışma kapısını jüri makinesinde koştur (`araclar/cakisma-kapisi.mjs` srv21'de yok). |
| AB-4, AB-5, AB-7 | Şef: yayın takvimi, API yanıtı (`/api/kontrol/huni?oge=…` `mp4: null`), sonuç tablosu — yayın sonrası. |

## Ana derse geri besleme

- Ek bulgu 1 (s / es) ana derste de var; ana dersin kural cümlesi ve kartları "s/es" diye düzeltilmeli.
- Rozet `YDT · BASIC` → `YDT · TEMEL` yayma adımı (standart §9) iki kola ve ana derse birlikte uygulanmalı.
- Kanca süresi: kol a da 4,12 sn (> 4). Standart "kanca ≤ 4 sn" ile kol a'nın 4,12 sn'si için ya ses hızı ya da standart cümlesi güncellenmeli.

## Jüri notu

Bu hüküm bir DÜZELTME değil: üretim dosyalarına dokunulmadı. Teslim kapısı (§1g): HV-1, 7, 13, 14, 22 kanıt yok ve HV-12/AB-3 hayır iken
önizleme adresi Nadir'e GİTMEMELİ; düzeltme sonrası jüri yeniden koşar (§1b).
