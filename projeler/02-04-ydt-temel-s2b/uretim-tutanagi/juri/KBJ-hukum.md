# KBJ-0204S2 — çıktı jürisi hükmü · `02-04-ydt-temel-s2b` (A/B kol b) · 15.11.2026

**Jüri modeli:** Claude Sonnet 5.5 (`claude-sonnet-5-5`), oturum 15.11 ≈ 22:55–23:15.
**Üretici oturum modeli:** Claude Opus 5.5 (`claude-opus-5-5`; kaynak `uretim-tutanagi/KBC-RAPOR.md` tablo, "Üretici model"). **Model farklı:** §1e sağlandı.
Okuma kuralı: **evet** = ölçüt sağlandı · **hayır** ve **kanıt yok** = kaldı.

## Özet

| Bölüm | evet | hayır | kanıt yok |
|---|---|---|---|
| §2a Kısa video (HV-1…23) | 19 | 2 | 2 |
| §2d A/B kolu (AB-1…7) | 4 | 0 | 3 |
| Ek madde (AB-X1, bağımsızlık) | 0 | 1 | 0 |
| **Toplam** | **23** | **3** | **5** |

**Sonuç: KALDI.** Teslim kapısı (§1g, D-0338) kapalı kalır; önizleme adresi Nadir'e ve karta yazılmaz.
Not: AB-4, AB-5, AB-7 yayın öncesi şef maddesidir; paketin içinden kanıtlanamaz. Üretim düzeltmesi gerektiren kaldı maddeleri: HV-13, HV-17, HV-20/21, AB-X1.

## Zaman kapısı (§1b)

| Kayıt | Zaman |
|---|---|
| Paketin son içerik değişikliği (`surumler.json`; `uretim-tutanagi/` hariç) | 15.11 22:58:56 |
| Çakışma kapısı çıktısı (`kapi-cikti.txt`) | 15.11 23:00:11 |
| Bu hüküm | 15.11 ≈ 23:15 |

Hüküm içerik değişikliğinden sonra yazıldı. QA kareleri (`sahneler/*/k/`) içerik değil kanıttır; sayılmadı.

## Bakılan kanıt

| Tür | Dosya / ölçüm |
|---|---|
| Metin | `ortak/anlatim/senaryo.json`, `altyazi.json`, `sureler.json`, `sozcukler.json`, `sentez.wav.rapor.json` (Whisper `duyulan`), `zaman.json`, `surumler.json`, `aciklama-a.md`, `aciklama-b.md`, `aciklama.md`, `sahneler/08…/zamanlar.json`, `sahneler/03…/zamanlar.json` |
| Kare, açık (Read ile açıldı) | `uretim-tutanagi/kare/01-hyperframes-kapak-0.png`, `…/02-paperjs-ornek-10.png`; 08: 17,41 · 20,5 · 21,7 · 22,82; 03: 22,83 · 24 · 24,6 · 26,8 · 29,48 |
| Kare, koyu (Read ile açıldı) | 01 (0,9), 02 (14,9), 08 (22,82), 03 (29,48) |
| Kol a karşılaştırma (Read ile açıldı) | kol a `kapak-a.png`, `hikaye-a.png`, `hikaye-b.png`, 08 (22,7), 03 (26,5) |
| Ölçüm (kendim koştum) | `diff -rq` kol a ↔ kol b (82 satır); `sha256sum` cümle 1–4 wav; `ffprobe` m4a süresi (29,49 ↔ 29,41); PIL kart farkı (08); `grep` (Tam ders, dakika, dk, emoji, utm, mutlak yol); `find -name '*.mp4'`; `find -type l` |
| Yapılmadı | `cakisma-kapisi.mjs` yeniden koşulmadı (başsız tarayıcı; çıktı dosyasına güvenildi, zamanı kapıdan sonra yazılmamış); API yanıtı (jeton yok); kulakla dinleme; mp4; Whisper'ı yeniden koşma |

## §2a — Kısa video (huni v2)

| Kimlik | Hüküm | Kanıt | Not |
|---|---|---|---|
| HV-1 | evet | 0 sn `kare/01-hyperframes-kapak-0.png`; orta `kare/02-paperjs-ornek-10.png`, `08…-20.5.png`; son `03…-29.48.png` | logo + `@ydspublishing` y ≈ 296–340, x = 60; koyu karelerde de var. Orta kare (sahne 02) kol a dizinindeki koddan çizilir (bkz. AB-X1) |
| HV-2 | evet | `senaryo.json` cümle 4 `ses: ogrenci` (`oPC5I9…gjY` = `kadro.ogrenci.ses`) | |
| HV-3 | evet | `senaryo.json` cümle 4: "Dersin tamamı YDS Publishing YouTube kanalında." birebir | Whisper "YEDESE Publishing" (bkz. HV-17) |
| HV-4 | evet | `grep -iE 'tam ders'` sahne `proje/index.html`, `ortak/*.js`, `ortak/anlatim/*.json`, açıklamalar: 0 | eşleşmeler yalnız `SPEC.md`, `RAPOR.md`, `uret.py` yasak listeleri (belge, çıktı değil) |
| HV-5 | evet | `grep -iE 'dakika\|\bdk\b'` aynı küme: çıktıda 0 | eşleşmeler yalnız belge ve üretici yorumları |
| HV-6 | evet | sahne 08 (17,41–22,83); `aciklama-a.md` ve `aciklama-b.md` ilk satır "Sınav günü bakmak için kaydet. …" | kaydet kalıbı §4 listesinden (`Ekran görüntüsü al, sınav günü bak.`). Ekranda ve seste "Kaydet" sözcüğü yok (bkz. HV-13) |
| HV-7 | evet | `03…-29.48.png`: ana ders kapağı x 60–960, y ≈ 627–1133 (900×506) | standart ≈ 920×518; sapma %2. Kart içinde `YDT · TEMEL`, künyede `YDT · BASIC` aynı karede (bkz. Ek bulgu E2) |
| HV-8 | evet | senaryo | sınavda çıkar · yanılınır · tek cümle · dersi izlemeden anlaşılır · sınav günü yeniden bakılır = 5 evet; Türkçe köprü yok (1 hayır) |
| HV-9 | evet | `find 02-04-ydt-temel-s2b -name '*.mp4'`: boş | |
| HV-10 | evet | 11 açık + 5 koyu kare: y < 295 yalnız zemin; içerik en çok y ≈ 1280; altyazı y 1420–1520; y ≥ 1570 boş | kutu ölçümü yok, göz denetimi; çakışma kapısı 4 sahnede 0 çakışma |
| HV-11 | evet | `zaman.json`: 4 sahne; `ffprobe` m4a 29,49 sn | kabul sınırı 35 altında; hedef 22–26 iki kolda aşıldı (KBC-RAPOR açık nokta 1) |
| HV-12 | evet | `sozcukler.json`: "Genel" t0 = 1,00 sn; kanca 0–2,84 sn | ilk söz tam 1,00: sınırda |
| HV-13 | **hayır** | `08…-20.5/21.7/22.82.png`; PIL kart farkı (x 60–960, y 560–1000): 20,5→21,2 = 0 px; 21,7→22,4 = 0 px; 22,4→22,82 = 0 px; 21,2→21,7 = 16.435 px (Today hapı dolu → çerçeve, 21,35) | Kart ≥ 2 sn sabit: evet (`zamanlar.json` `kart_giris` 17,96 → ilk değişim 21,35 = 2,99 sn; kol a ile kart pikseli aynı: 0 px). Ama yer imi SVG yok (yerine vizör SVG) ve "Kaydet" yazısı yok → madde açık metni sağlanmadı. Madde kapanış değişkenini öngörmüyor (bkz. düzeltme) |
| HV-14 | evet | `03…-24.6/29.48.png`: kart y 627–1133; giriş sözü Fredoka 700, 88 px; `@ydspublishing · YouTube` y ≈ 1170–1250 (29,48) | 26,8 sn karesinde YouTube sözcüğü henüz yok; seste 27,37'de geliyor (doğru) |
| HV-15 | evet | "Konu burada bitmiyor." ∈ §4 listesi; derste bir kez | |
| HV-16 | evet | "Ekran görüntüsü al, sınav günü bak." ∈ §4 listesi; derste bir kez | |
| HV-17 | **hayır** | `ses-sozluk.json` `"YDS": "YeDeSe"` ✓ (1 kayıt); `sentez.wav.rapor.json` son parça `duyulan` = "YEDESE Publishing" | Standart §4 "Whisper 'YDS Publishing' duyuyor mu" ister; hiçbir koşuda "YDS" duyulmuyor. Kol a ile aynı sapma; üretim hatası değil, ölçüt-standart çelişkisi |
| HV-18 | evet | `aciklama-a.md`, `aciklama-b.md` ilk satır sabit; Reels bloklarında adres yok ("Bağlantı profilde.") | |
| HV-19 | evet | `grep -rhoE 'utm_campaign=…' aciklama*.md`: gerçek bağlarda yalnız `ING-YDT-GR-02-04-T` (kol b 15 bağ) ve `ING-YDT-GR-02-02-T`; küçük harf yalnız "DİKKAT" notu içinde. `utm_content`: `s2b-a` ×10, `s2b-b` ×5 | AB §4 `<sürüm>-<set>` biçimi tutuyor. Bayat not için bkz. E4 |
| HV-20 | **kanıt yok** | kol b kökünde `kapak*.png`, `hikaye*.png` yok (7 dosya `~/Silinecekler/2026-11-15-kol-b/` altına taşındı); `aciklama-a/b.md` var (2) | AB §4: türev gruba ait, kol a'da. Kol a türevleri bakıldı (`kapak-a.png`, `hikaye-a/b.png`): kanal katmanı + `Kaydet` var. Ama bu paket için kare yok → kural gereği "kanıt yok" |
| HV-21 | **kanıt yok** | kol b'de hikâye karesi yok; kol a `hikaye-a.png` (kanal katmanı, kural kartı, yer imi + Kaydet, y 1150–1380 boş) ✓ | `hikaye-b.png`: kural özeti yok (soru kartı: "Hangisi doğru?", A/B şık); standart §6 "kural özeti" ister. Kol a hükmü için not (E7) |
| HV-22 | evet | `kapi-cikti.txt`: 01 (13 örnek) · 02 (60) · 08 (23) · 03 (28) — çakışma yok; `rc=0` | kendim koşmadım; kapı çıktısı son içerik değişikliğinden 75 sn sonra. Statik türev kol b'de yok: "ÖLÇEMEDİ" maddesi uygulanamaz |
| HV-23 | evet | `sentez.wav.rapor.json`: 10/10 parça `benzerlik` 1,00 | marka parçası ses metniyle 1,00; ekran metniyle 0,97 (huni-v2 §9) |

## §2d — A/B kolu

| Kimlik | Hüküm | Kanıt | Not |
|---|---|---|---|
| AB-1 | evet | `surumler.json` kol b: `varyant {grup s2, kol b, degisken kapanis, deger ekran-goruntusu}`; kol a: `{s2, a, kapanis, kaydet}`; `ls projeler` grup s2'de yalnız `…-s2` ve `…-s2b` | atama tablosu s2 → kapanış ✓ |
| AB-2 | evet | `diff -rq 02-04-ydt-temel-s2 02-04-ydt-temel-s2b` = 82 satır (üretici 81) | +1 = kol a `uretim-tutanagi/juri/` (başka oturum, üretimden sonra). Her satır beklenen sınıfta: kapanış sahneleri 08+03 (üretici, çalıştırıcı, `proje/index.html`, zaman/olay, QA kareleri), zaman-ses türevi, `cumle-3/4.wav`, `senaryo.json` (cümle 3 parça 2, cümle 4 parça 1), `surumler.json`, `utm` ×3, grup türevi (kapak ×4, hikâye ×3), `uretim-tutanagi/`. Sahne 01, 02, 04–07 ve `ortak/` (anlatım dışı) için fark yok. Not: sahne 08 görseli yer imi → vizör: "kaydet kalıbı" (AB §3) içinde sayıldı |
| AB-3 | evet | `sha256sum` `cumle-1.wav` 0b0dafd59a98 = 0b0dafd59a98; `cumle-2.wav` 1d805b981216 = 1d805b981216; `sahneler/01`, `02`, `ortak/kunye.js` kol a ile bayt aynı; kadro/ses kimlikleri aynı (`senaryo.json`) | Çekirdek cümle: metin aynı, ses kimliği aynı, süre aynı (3,52 sn); wav sha256 farklı (`cumle-4.wav` b192db36b66b → 8f69da650730; komşu parça değişti, yeniden sentez). Baytsal "aynı" değil; kabul: Whisper 1,00 |
| AB-4 | **kanıt yok** | yayın takvimi yok; iki paket `durum: inceleme` | Şef maddesi; yayın öncesi |
| AB-5 | **kanıt yok** | pakette mp4 yok (`find`); API yanıtı alınmadı (jeton yok) | Dosya düzeyinde ✓; kuralın kanıtı API yanıtıdır |
| AB-6 | evet | `surumler.json` `s2b` satırı `varyant` ✓; `utm_content=s2b-a` / `s2b-b` ✓ (15 bağ) | |
| AB-7 | **kanıt yok** | sonuç tablosu yok; ölçüm başlamadı | Yayın sonrası şef maddesi |
| AB-X1 (ek) | **hayır** | `sahneler/02-paperjs-ornek/sayfa.html:7`, `sahne-02.js:4–5`, `kalem-paper.js:11–12`, `ortak/kunye.js:8` (`KOK`): hepsi `/projeler/02-04-ydt-temel-s2/…` | AB §4 "kol b KOPYADIR, bağ yok". Sahne 02 (değer sahnesi) ve `ortak/` (font, logo) kol a'dan yüklenir. Kol a değişirse kol b sessizce değişir (tek değişken bozulur); kol a taşınır/arşivlenirse kol b kırılır. KBC-RAPOR açık nokta 2 bunu biliyor ("bayt aynılığı için değiştirmedim") |

## Kolları yan yana (adım 4)

| Eksen | Kol a | Kol b | Fark |
|---|---|---|---|
| Kanca (sahne 01) | "Genel mi, şu an mı?" | aynı | yok |
| Değer (sahne 02) | 2 örnek, kural cümlesi | aynı | yok (kod kol a'dan, bkz. AB-X1) |
| Kaydet kalıbı | "Bu kuralı kaybetme. Kaydet." + yer imi | "Ekran görüntüsü al, sınav günü bak." + vizör | **değişken** |
| Çağrı girişi | "Bitmedi, gel." | "Konu burada bitmiyor." | **değişken** |
| Çekirdek cümle, ses kadrosu | aynı | aynı | yok (wav yeniden sentez) |
| Kanal katmanı, künye, kapak kartı | aynı | aynı | yok |
| Açıklama gövdesi (A/B setleri) | `s2-…` | `s2b-…` | yalnız `utm_content` ✓ |
| Kapak ×3, hikâye ×2 | kol a'da | pakette yok | AB §4 gereği |
| Süre | 29,41 sn | 29,49 sn | +0,08 |

Değişken dışında söz, ekran metni, kapak veya açıklama farkı **yok**. Tek çelişki: iki kolun açıklaması "Sınav günü bakmak için kaydet." diyor; kol b videosu "kaydet" demiyor (E5).

## Ek bulgular (madde dışı; üretici ya da şef kararı)

| # | Bulgu | Kanıt | Önem |
|---|---|---|---|
| E1 | Ekran metni sesten önce: sahne 08 `Ekran görüntüsü` iki sözcük birden 20,27'de çıkar; `görüntüsü` seste 20,71'de başlar (0,44 sn erken). `08…-20.5.png` karesi kanıt | `zamanlar.json` `vizor_ciz` 20,27; `sozcukler.json` | düşük (EK-12 benzeri) |
| E2 | Rozet `YDT · BASIC` (huni-v2 §9: "ilk dokunuşta düzeltilir"); aynı karede kart içi `YDT · TEMEL`. 7 sahnenin hepsinde BASIC | `03…-29.48.png`; `grep BASIC` | orta (kol a ile ortak) |
| E3 | `aciklama*.md` başlık ve üst bilgi kol a'dan kopya: "02-04-ydt-temel-s2", "29,41 sn", "Sürüm: A (`s2-aciklama-a`)" | `aciklama-a.md` satır 1–5 | düşük (yayın metni değil, dosya üstbilgisi) |
| E4 | "DİKKAT: S1 `utm_campaign` küçük harf yazar" notu bayat: gerçek bağlarda küçük harf yok | `grep` (HV-19) | düşük |
| E5 | Açıklama videonun söylediğiyle çelişir (video "Ekran görüntüsü al"; açıklama "kaydet"); ayrıca ekran görüntüsü platform kaydetme sayacına yazılmaz (ölçü yanlılığı) | `aciklama-a.md` satır 29; KBC-RAPOR açık nokta 5 | orta (A/B yorumu) |
| E6 | Kol b açıklamaları `kapak-a.png`, `kapak-b.png`, `hikaye-a/b.png` dosyalarına atıf yapar; kol b'de yok → API'de kol b için kapak/hikâye adresi boş kalır | `aciklama-a.md` "Kapak: `kapak-a.png`" | düşük |
| E7 | Kol a `hikaye-b.png` kural özeti taşımıyor (soru kartı), standart §6 ister; kol a jürisi bakmalı | `02-04-ydt-temel-s2/hikaye-b.png` | düşük (kol a) |
| E8 | Dil: "She is wearing … today" için "Konuşma anı: şimdiki zaman" etiketi gevşek (today = bu gün / geçici durum; tam şu an olmayabilir). Dilbilgisi hatası değil; EK-5b geçer. Mutlak kural yok (EK-5c), üstü çizili cümle yok (EK-5a), yazım hatası yok, `Today` açıklama cümleleri doğru | `senaryo.json` cümle 2 | bilgi |

## Düzeltme önerisi (kaldı maddeleri, tek cümle)

| Kimlik | Öneri |
|---|---|
| HV-13 | Standart §3'e "kapanış kolu `ekran-goruntusu` ise yer imi yerine vizör, 'Kaydet' yazısı yerine kalıp metni" istisnasını yaz (şef kararı), ya da kol b kartına yer imi + "Kaydet" etiketi ekle. |
| HV-17 | `huni-v2-standart.md` §4 ve `juri-olcutleri.md` HV-17'ye "Whisper 'YEDESE Publishing' ≡ YDS Publishing" eşlemesini yaz (kol a ile ortak). |
| HV-20, HV-21 | `juri-olcutleri.md` HV-20/21'e "kol b: türev grup düzeyinde kol a'da; kol a karesi sayılır" notunu yaz, ya da kol b'ye türev kopyala (AB §4 buna karşı). |
| AB-4, AB-5, AB-7 | Yayın takvimi, API yanıtı (`mp4: null`) ve sonuç tablosu yayın öncesi/sonrası şef işi; paket jürisinde "uygulanamaz" sınıfı aç. |
| AB-X1 | Sahne 02 ve `ortak/kunye.js` içindeki `/projeler/02-04-ydt-temel-s2/` yollarını `-s2b` yap (kopya bayt aynılığı bozulur, sözleşme değişken sayımı güncellensin) ya da kök-bağıl yola çevir; sonra `diff -rq` yeniden koş. |

## Ana derse (kol a / ana yatay) geri besleme

- Rozet `YDT · BASIC` → `YDT · TEMEL` (huni-v2 §9 açık iş; 7 sahne + kol a + öteki 11 ders).
- Whisper marka eşlemesini (HV-17) kapı betiğine al; her jüri aynı "hayır"ı yeniden bulmasın.
- `hikaye-b.png` kural özeti (HV-21) kol a jürisi kapatsın.
- Süre 29,4 sn: hedef 22–26 iki kolda aşılıyor; kısaltma iki kola birlikte yapılmalı (KBC-RAPOR açık nokta 1).
- Sahne 02 ve 03'te karaoke vurgusu karelerde görünmüyor (sahne 08'de alt çizgi var); DK-1 kısa için de geçerliyse bakılmalı.
- Açıklama başlığındaki süre ve kimlik alanları şablondan üretilsin (E3).

---
Üretici model: Claude Opus 5.5 · Jüri model: Claude Sonnet 5.5 · Hüküm: KALDI (3 hayır, 5 kanıt yok, 23 evet).
