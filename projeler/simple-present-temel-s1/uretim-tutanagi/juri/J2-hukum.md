KARAR: KALDI (2 hayır, 4 kanıt yok)

# J2-0202S1 çıktı jürisi — `simple-present-temel-s1` (yayındaki kısa, kol a) · 15.11.2026 22:54

**Jüri modeli: Claude Sonnet 5.5.** Üretici oturum modeli: Claude Fable 5.2 (commit `bce68bd`, `e745ad1` ek satırı). İKİ MODEL FARKLI (§1e karşılandı).
Salt okuma: üretim dosyasına dokunulmadı. Tek yazılan dosya bu hüküm. Ölçüt kaynağı: `D/.claude/docs/juri-olcutleri.md` §1, §2a, §2c (+ §2b'den EK maddeleri).
K = `/home/sef/01dev/_worktrees/kalem-0204/projeler/simple-present-temel-s1`, ana ders = `../simple-present-temel`.

## Özet

| Sonuç | Sayı |
|---|---|
| evet (geçti) | 43 |
| hayır (kaldı) | 2 — KS-10, RZ |
| kanıt yok (kaldı) | 4 — EK-4, EK-8, EK-11, EK-12 |
| Toplam madde | 49 |

Bakılan çıktı: son `ortak/anlatim/senaryo.json` (22:32), `sureler.json`, `sozcukler.json`, `altyazi.json`, `zaman.json`, `surumler.json`, `aciklama.md`/`-a`/`-b`,
`sentez.wav.rapor.json` (Whisper), 8 sahne RAPOR'u, ve KARELER: sahne 01 (0 · 1,5 · 2,95 sn açık; 0,9 · 1,5 · 2,95 koyu) · sahne 02 (3,05 · 8,8 · 14,55 açık; 8,8 koyu) ·
sahne 03 (14,7 · 16,2 · 17,65 açık; 17,65 koyu) · sahne 04 (17,8 · 20,9 · 23,95 açık; 23,95 koyu) · `kapak-a/b/c.png` açık + koyu · `hikaye-a/b.png` açık + koyu ·
`ortak/kapak/ana-kapak.png` + `ana-kapak-koyu.png` · 168 px küçük görünüm (kısa kapaklar, hikâyeler ve ana kapak; jüri kendi indirdi, `/tmp/j2-s1/`, pakete yazılmadı).
Her kare Read ile açıldı.

## §1 Yapı ve zaman

| Kimlik | Hüküm | Kanıt | Not |
|---|---|---|---|
| 1a TAŞLAK DEĞİL ÇIKTI | evet | yukarıdaki kare ve dosya listesi | Taslak (`*-taslak.md`) hükme girmedi |
| 1b Jüri zamanı > paket son içerik zamanı | evet (J2 için) | paket son içerik `bce68bd` 22:38:38 · bu hüküm 22:53:57 | **Eski jüri BAYAT:** `juri/s1.dil.md` 19:01:35 ve `s1.kaynak-kural.md` 19:01:16, paketten 3 sa 37 dk eski; 22:38 düzeltmesini ve 22 maddeyi görmedi. Rozet ya da KS-10 düzeltilirse J2 de bayatlar, yeniden koşar |
| 1e Model farkı | evet | Fable 5.2 ↔ Sonnet 5.5 | Ortak kör nokta riski azaldı; Whisper ve dosya ölçümü modelden bağımsız |

## §2a Kısa video (HV)

| Kimlik | Hüküm | Kanıt | Not |
|---|---|---|---|
| HV-1 | evet | `kanca-0.png`, `deger-8.8.png`, `cagri-23.95.png`; ayrıca `kaydet-17.65`, koyu 4 kare | `ydspublishing` logo + `@ydspublishing` y ≈ 295–340, x = 60; 0. sn, orta, son karede var. Koyu temada da var |
| HV-2 | evet | `senaryo.json` cümle 4 `ses: ogrenci`; `sentez.wav.rapor.json` | Çağrı parçası öğrenci sesi (`oPC5I9GK…`). Ses tonunu ben duymadım; kayıt metinden |
| HV-3 | evet | `senaryo.json` cümle 4: "Dersin tamamı YDS Publishing YouTube kanalında." | Birebir |
| HV-4 | evet | metin taraması (senaryo, altyazı, açıklama, sahne HTML/JS, `ortak/*.js`) | "Tam ders" / "Full lesson" 0 sonuç |
| HV-5 | evet | aynı tarama | "dakika", "dk" 0 sonuç (yalnız `calistir.sh` yük yorumu ve `METIN.md` başlığında "sn") |
| HV-6 | evet | sahne 03; `aciklama-a/-b.md` ilk satır | Ayrı Kaydet sahnesi. İlk satır: "Sınav günü bakmak için kaydet. Dersin tamamı @ydspublishing YouTube kanalında." (YouTube, Reels, TikTok üçünde) |
| HV-7 | evet | `cagri-23.95.png` (açık + koyu) | Ana ders kapağı ≈ 900×505, y 622–1126. Standart ≈ 920×518; tolerans içinde |
| HV-8 | evet | senaryo | 6/6 evet: sınavda çıkar, en çok yanılır, tek cümleye sığar, Türkçe köprü ("Kardeşim gider"), dersi izlemeden anlaşılır, sınav günü bakılır |
| HV-9 | evet | `find . -name '*.mp4'` → 0 | Nadir sözü yok, mp4 yok |
| HV-10 | evet | 4 sahne için çakışma kapısı (RAPOR: 01 · 02 · 03 · 04 "çakışma yok", 0 uyarı) + göz | Üst 0–280 ve alt 1570–1920 bölgesinde yazı/çizim yok. Altyazı y 1420–1520 |
| HV-11 | evet | `zaman.json` | 4 sahne, 24,00 sn (hedef 22–26 içinde, sınır 35) |
| HV-12 | evet | `sureler.json`, `senaryo.json` `zaman.giris` | İlk söz 1,00 sn. Giriş sahnesi 3,0 sn. Not: kanca cümlesi 4,12 sn'de biter (4 sn eşiğinin 0,12 sn üstü); eşik sahne süresine bağlı okundu |
| HV-13 | evet | `kaydet-16.2.png` ↔ `kaydet-17.65.png` | Kart bölgesi piksel farkı yalnız zemin degradesi köşesi (bbox 0,0–20,19): kart sabit. Yer imi SVG (çizgi), emoji değil. "Kaydet" hapı var |
| HV-14 | evet | `cagri-20.9.png`, `cagri-23.95.png` | Kart konumu doğru. "Gerisi bizde." Fredoka 700. `@ydspublishing · YouTube` satırı son karede var (20,9 sn karede yalnız hap, "· YouTube" sonra gelir) |
| HV-15 | evet | s1 "Gerisi bizde." · s2 "Bitmedi, gel." · s3 "Bu sadece başlangıç." | Listeden; derste yinelenmiyor |
| HV-16 | evet | s1 "Sınavdan önce lazım olacak. Kaydet." · s2 "Bu kuralı kaybetme. Kaydet." · s3 "Bir arkadaşına gönder; o da karıştırıyor." | Listeden; yinelenmiyor |
| HV-17 | evet | `sentez.wav.rapor.json`: `ses_metni` "YeDeSe Publishing", duyulan "YEDESE Publishing", benzerlik 1,00 | Marka `ses-sozluk.json` `YDS → YeDeSe` kaydından. Whisper literal "YDS" duymaz; standart §9 bu bilinen sapmayı kabul eder |
| HV-18 | evet | `aciklama*.md` | İlk satır sabit. Reels bloğunda bağ yok (bağ yalnız "Profil bağlantısı" ayrı satırında) |
| HV-19 | evet (s1 için) | `utm_campaign=ING-YDT-GR-02-02-T` her 15 satırda; `utm_content=s1-a` (10), `s1-b` (5) | Büyük harf, `<sürüm>-<set>` biçimi tutarlı. 02-02 s2/s3 ve 02-04 s1/s2/s3 de `ING-…-T` (02-04 s2 `aciklama*.md` satır 91'deki küçük harf yalnız uyarı metni, bağ değil). Altı paketlik betik hâlâ yok |
| HV-20 | evet | `kapak-a/b/c.png`, `hikaye-a/b.png`, `aciklama-a/b.md` | Kapak 3: altyazı yok, kanal katmanı var, B karakterli. Hikâye 2. Açıklama 2 |
| HV-21 | evet | `hikaye-a.png`, `hikaye-b.png` (+ koyu) | Kanal katmanı + kural özeti + Kaydet var; y 1150–1380 boş zemin |
| HV-22 | evet | sahne RAPOR'ları: 01 6252 kutu, 02 1985 kutu, 03 1542 kutu, 04 3880 kutu, hepsi 0 uyarı; statik türevlerde (kapak, hikâye) kapı "sahne bulunamadı" (çıkış 2) | Statik 5 kareye göz bakışı yapıldı: taşma, çakışma yok |
| HV-23 | evet | `sentez.wav.rapor.json` | Çağrı parçası 1,00 (≥ 0,9). Not: `ses-sentez.log` "önbellek 2/9 parça, Whisper koşmadı"; hangi 2 parçanın önbellekten geldiği kayıtta yok |

## §2c Kapak ve hikâye karesi (KS)

| Kimlik | Hüküm | Kanıt | Not |
|---|---|---|---|
| KS-1 | evet | `file`: kapak-a/b/c, hikaye-a/b 1080×1920; ana-kapak(-koyu) 1920×1080 | Koyu karşılıklar `sahneler/*/k/koyu/` altında (kökte değil); açık kökte |
| KS-2 | evet | `ana-kapak.png` | Ana yazı sol, 2 satır Fredoka 700 (`GİDER` / `= GOES`); kenar boşluğu ≈ %5; sağ alt boş. Kısa kapakların (dikey) düzeni standartta tanımsız; huni §6 kuralları sağlanıyor |
| KS-3 | evet | `ana-kapak.png`, `-koyu.png`, `kapak-b.png` | Açık sarı `#fece00`/koyu yazı; koyu `#141414`; çıkartma kenarı krem |
| KS-4 | evet | ana kapak "GİDER = GOES"; kısa A "GO mu, GOES mu?"; B "FİİLE -S HANGİ ÖZNEYLE?"; C "HE GOES / I GO"; YouTube başlığı "Simple Present: s yalnız he, she, it ile" / B "My brother goes: s nereden geliyor?" | 2–4 sözcük; hiçbiri başlığı ya da öbür kapağı yinelemiyor. Not: kapak C iki biçimi birden gösterip merakı azaltıyor (kural cümlesi değil, örnek çifti) |
| KS-5 | evet | `ana/ortak/kapak/KAYNAK.json`: `nano-banana-2`, 1k, 0,04 USD | Görselde yazı, harf, rakam, logo yok (karakter, minibüs). Not: `K/ortak/kapak/` içinde `KAYNAK.json` yok; kaynak ana derste |
| KS-6 | evet | 168 px şeritler (kısa kapaklar, hikâyeler, ana kapak açık + koyu) | `GİDER = GOES`, `GO mu, GOES mu?`, `FİİLE -S HANGİ ÖZNEYLE?` okunur. `kapak-168.png` pakette yok; jüri kendi indirdi |
| KS-7 | evet | `GİDER`, `FİİLE`, `HANGİ`, `ÖZNEYLE`, `Hangisi doğru?` | Büyük İ, Ö ve küçük ğ doğru çiziliyor, yedek yazı tipine düşmüyor |
| KS-8 | evet | tüm kapak ve hikâye kareleri | Taşma yok; yazı karakterle binmiyor (B'de metin üstte, karakter altta) |
| KS-9 | evet | tüm kareler | Emoji yok. Yer imi, tik, ok SVG çizimi |
| KS-10 | **hayır** | `ana/ortak/kapak/KAYNAK.json` karakter tarifi: "genç **erkek**, iri kıvırcık saç…"; `senaryo.json` `kadro.ogrenci.cinsiyet: "kadin"` (saç `LongBangs`) | Çağrı sahnesi ve kapak B erkek karakteri gösteriyor; öğrenci sesi (`oPC5I9GK…`) ve kadro kadın. `S1-duzeltme.md` bunu "Nadir/şef kararı" diye açık bırakmıştı; 22 maddeli ölçüte göre kapanmadı |

## Ek: §2b ve yapı maddeleri (kısa jüri istemine bağlı)

| Kimlik | Hüküm | Kanıt | Not |
|---|---|---|---|
| RZ rozet metni | **hayır** | künye `YDT · BASIC` (`kanca-0`, `deger-8.8`, `kaydet`, `cagri`, 5 türev karesi, `senaryo.json` `giris.rozetler`) ↔ ana kapak `YDT · TEMEL`; huni standardı §4 ve §9 rozet metni `YDT · TEMEL` | Aynı karede iki farklı rozet (`cagri-23.95.png`: üstte BASIC, ana kapak kartında TEMEL). Standart §9 "YDT · BASIC taşıyan kısalar ilk dokunuşta düzeltilir" diyor. Düzeltme yeri: `ortak/kunye.js`, `senaryo.json` `giris.rozetler`, `kapak-taslak.md`, 8 sahne `uret.py` |
| EK-1 kısaltma okunuyor mu | evet | `sentez.wav.rapor.json` `ses_metni` | YDS → "YeDeSe" (kayıtlı marka). Konuşmada "YDT" yok |
| EK-2 emoji | evet | tüm 13+ kare + dosya taraması | 0 emoji |
| EK-3 kapsam matrisi | evet | aşağıdaki matris | Boş hücre yok. Not: koyu temada sahne 02 ve 04'ten yalnız 1'er kare var; sahne 02'nin 3,05 / 14,55 ve sahne 04'ün 17,8 / 20,9 sn koyu kareleri yok |
| EK-4 görsel jüri GEÇTİ olmadan adres gitti mi | **kanıt yok** | `surumler.json` `durum: "inceleme"`, `onizleme` adresi var | Önceki görsel jüri kaydı yok (eski jüri taslağa baktı); adresin Nadir'e ne zaman yazıldığı tutanakta yok. Bu hüküm ilk görsel jüri. Karar şefte |
| EK-5a üstü çizili cümle gerçekten hatalı mı | evet | sahne 02 koyu/açık kare, hikâye A/B | Üstü çizili yalnız `go` + çizili `s` ("gos", hatalı biçim). Doğru cümle çizili değil. Hikâye B'de doğru şık A) go yeşil tikli, B) goes gri; çizili yok |
| EK-5b her denklik ve kural bağımsız doğru mu | evet | senaryo, kapak, hikâye, açıklama | `Gider = goes`; he/she/it ile fiile s; I/you/we/they ile yok; `My parents go` doğru. "Türkçe geniş zaman eki = s" denkliği s1'de artık yok (22:38 düzeltmesi). **Ana derste hâlâ var, aşağıya bak.** Küçük kusur: ses "s gelir" derken ekran `go-es` yazıp `es`'i daire içine alıyor |
| EK-5c istisnasız ifade | evet | senaryo, başlık, kapak, açıklama | "her zaman / hep / always" yok. "s yalnız he, she, it ile" (YouTube başlığı A) doğru; kural cümlelerinde "gelir/yok" mutlak değil |
| EK-6 yazım ve şablon cümlesi | evet | `aciklama.md`, `-a`, `-b` | Yazım hatası, tamlama hatası, İ/I hatası yok. `{UZUN_VIDEO_URL}` ve `{PLATFORM_URL}` yer tutucuları yayın öncesi bilinen açık iş |
| EK-7 koyu temada okunuyor mu | evet | 12 koyu kare | Kontrast iyi; yeşil tik koyuda da okunur |
| EK-8 klişe listesi (kontak sayfası) | **kanıt yok** | pakette 18 maddelik klişe kontak sayfası yok (`kanca/k/ara/kontak-ucus.png` ve `kontak-karaoke.png` başka amaçlı) | Göz bakışında klişe işareti görmedim, ama kontak sayfası olmadan hüküm "evet" olmaz |
| EK-9 soru anı | evet | senaryo | Kısa ≤ 1: 1 soru, 7 sözcük (≤ 12) |
| EK-10 ses metni kuralları | evet | `sentez.wav.rapor.json` | `ve,` yok; tire yok; IPA yok (zamir listeleri EN parçaya alındı: `He, she, it` / `I, you, we, they`, Whisper 1,00) |
| EK-11 yeni telaffuz kulakla dinlendi mi | **kanıt yok** | `S1-duzeltme.md` son bölüm: "Kulak kararı zorunlu (Nadir)"; dinleme kaydı yok | `go mu, goes mu` Türkçe parçada, `YeDeSe Publishing` sözlükte. Whisper 1,00 kulak yerine geçmez |
| EK-12 ekran metni sesten önce gelmiyor mu | **kanıt yok** | RAPOR'larda "motor zaman kapısı" çıktısı yok | Gözlem: kanca başlığı `GO mu, GOES mu?` 0. sn'de tam ekranda (2,95 sn'de `go` kutusu görünür), sözcükler 2,52–3,80 sn'de söyleniyor. Soğuk açılış tasarımı gereği olabilir; standartta açık istisna yazılı değil. Şef karar verir |

### EK-3 kapsam matrisi

Kısa video yalnız dikey (1080×1920). "Yatay" yön yalnız çağrı sahnesindeki ana kapakta (1920×1080) geçer; o dosya açık + koyu bakıldı.

| Türev | Dikey açık | Dikey koyu | Not |
|---|---|---|---|
| Sahne 01 kanca | 0 · 1,5 · 2,95 | 0,9 · 1,5 · 2,95 | tam |
| Sahne 02 değer | 3,05 · 8,8 · 14,55 | 8,8 | koyu 1 kare |
| Sahne 03 kaydet | 14,7 · 16,2 · 17,65 | 17,65 | koyu 1 kare |
| Sahne 04 çağrı | 17,8 · 20,9 · 23,95 | 23,95 | koyu 1 kare |
| Kapak A / B / C | 3 | 3 | tam |
| Hikâye A / B | 2 | 2 | tam |
| Ana kapak (yatay) | 1 | 1 | tam |

## Kaldı maddeleri ve düzeltme önerisi

| Kimlik | Düzeltme (tek cümle) | Kim |
|---|---|---|
| RZ | Künye rozetini `YDT · TEMEL` yap (`ortak/kunye.js`, `senaryo.json` `giris.rozetler`, 5 türev ve 4 sahne yeniden çekilir). | şef → üretici |
| KS-10 | Karakteri `kadro.ogrenci` (kadın) ile uyumlu yeniden üret ya da `kadro.ogrenci` cinsiyetini ve sesini erkeğe çevir. | Şef/Nadir kararı |
| EK-4 | Önizleme adresini Nadir'e yazmadan önce bu hükmün GEÇTİ olmasını bekle; adres zaten gittiyse tutanağa zamanını yaz. | Şef |
| EK-8 | 18 maddelik klişe kontak sayfasını üret ve işaret sayısını yaz. | üretici |
| EK-11 | `go mu, goes mu` ve `YeDeSe Publishing` söylenişini Nadir'e dinlet, sonucu tutanağa yaz. | Nadir |
| EK-12 | Zaman kapısı çıktısını tutanağa koy ya da kancadaki başlığın 0. sn'de görünmesini soğuk açılış istisnası diye standarda yaz. | Şef |

## Ana ders geri beslemesi (`../simple-present-temel/`)

1. **Yanlış denklik hâlâ ses ve künyede:** `ortak/anlatim/senaryo.json` cümle 7 "Türkçedeki er eki gibi: git-er, go-es." ve `meta.canAlici[0]` "Türkçedeki geniş zaman eki = İngilizcedeki s: gider = goes". Türkçe geniş zaman eki bütün kişilerde (gider-im, gider-sin, gider) var; İngilizce `-s` yalnız üçüncü tekil kişide. Denklik kuralı yanlış öğretir. s1 bu cümleyi 22:38'de düzeltti, ana ders düzeltilmedi.
2. **"s gelir" ile `goes` tutarsız:** cümle 3, 4, 5 "Sonunda s harfi var" der; `goes` -es, `takes off` -s. Tek kural yerine "s ya da es" demek yeterli.
3. **`meta.amaclar` "Türkçe geniş zaman eki ile köprü"** s1 `senaryo.json` ve `surumler.json`'a da geçmiş; yukarıdaki denklikten türediği için birlikte gözden geçirilmeli.
4. **Cümle 3 "Doğa kanunu: hep böyledir."** doğa olayı için doğru, ama kural diye alınırsa mutlak ifade olur; kural cümlesi değil, bilgi cümlesi; EK-5c'yi tetiklemiyor, yine de aynı satırda "hep" duyulur.

## Pakete bakarken görülen ek not

`zaman.json` → `hikaye.cikti` hâlâ `hikaye.png` diyor; teslim `hikaye-a.png` + `hikaye.png` (aynı dosya, md5 aynı). Sahne RAPOR'u da bunu açık nokta olarak yazmış. Ölçüt dışı, bilgi.
