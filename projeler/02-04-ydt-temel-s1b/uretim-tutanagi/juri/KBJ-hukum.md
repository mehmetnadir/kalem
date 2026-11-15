# KBJ-0204S1 jüri hükmü — 02-04-ydt-temel-s1b (A/B kol b, değişken `kanca`) · 15.11.2026 23:24

Jüri modeli: **Claude Sonnet 5.5** (`claude-sonnet-5-5`). Üretici modeli (KBC-RAPOR): Claude Opus 5.5. İki model FARKLI (§1e sağlandı); ikisi de Claude 5.5 ailesi, ortak kör nokta riski tam kapanmadı.
Jüri zamanı 23:24 > paketin son içerik değişikliği (`surumler.json` 23:10:25; kapak 23:09; açıklamalar 23:10) → §1b sağlandı.
Jüri hiçbir üretim dosyasını değiştirmedi; tek yazılan dosya bu hüküm dosyası.

## Özet

| Hüküm | Sayı |
|---|---|
| Evet (geçti) | 29 |
| Hayır (kaldı) | 7 |
| Kanıt yok (kaldı sayılır) | 4 |
| Toplam madde | 40 (HV 23 · AB 7 · EK 10) |

Kaldı (hayır): HV-19, HV-22, AB-3, EK-3, EK-5c, EK-6, EK-12.
Kanıt yok: HV-21 (tasarım gereği), AB-4 / AB-5 / AB-7 (yayın ve API aşaması, henüz ölçülemez).
**Teslim kapısı (§1g): GEÇMEDİ.** Önizleme adresi Nadir'e gitmemeli.

## Bakılan kanıt

| Kanıt | Durum |
|---|---|
| `senaryo.json`, `METIN.md`, `sureler.json`, `altyazi.json`, `sentez.wav.rapor.json` (Whisper), `ses-sentez.log`, `zaman.json`, `surumler.json`, `aciklama*.md` | okundu |
| Kareler (Read ile açıldı) | `kapak-a.png`; sahne 01 açık 0 ve 2,5; sahne 02 açık 2,5 · 6 · 14 · 16,13; sahne 08 açık 25,4; sahne 03 açık 31,7; koyu: `kapak-a-koyu`, sahne 02 (10), sahne 08, sahne 03; `kontak-kbc.png` (16 karo, son karo sahne 03 son kare) |
| `diff -rq` kol a ↔ kol b (kendim koştum) | 96 fark satırı; üreticinin 11 sınıfına uyuyor, sınıfsız satır yok |
| Metin taraması (`tam ders`, `dakika`, `dk`; html, js, json, md, py) | yalnız `BRIEF-S1.md:66` kural cümlesi (iç belge) |
| `find -iname '*.mp4'` | 0 dosya |
| Emoji taraması | karelerde yok; yalnız `SPEC.md` ASCII taslağı ve rapor işaretlerinde (✓ ✗ ✋), çıktıda değil |
| `utm_campaign` taraması (`projeler/*/aciklama*.md`) | s1, s1b doğru; **s2 ve s2b küçük harf** (bkz. HV-19) |

**Kare uyarısı:** `sahneler/03-hyperframes-cta/k/` altındaki 25.55 / 28.6 / 31.7 ve `…/k/koyu/…-31.7`, ayrıca `sahneler/08-hyperframes-kaydet/k/` altındaki
bütün kareler kol a'dan kalmadır (mtime 18:54 ve 19:20). 31,7 sn karesi kol b'nin süresinden (27,89 sn) sonradır. Bu karelere kol b kanıtı gibi bakmadım;
sahne klasörleri bayt bayt aynı olduğu için yalnız dolaylı destek saydım. Kol b'ye özgü yeni kare yalnız sahne 01, sahne 02 ve `kontak-kbc.png` son karosu.

## Madde tablosu — §2a kısa video (HV)

| Kimlik | Hüküm | Kanıt | Not |
|---|---|---|---|
| HV-1 | evet | kapak-a, sahne 02 (2,5 · 6 · 14 · 16,13), sahne 08, kontak son karo | logo + `@ydspublishing` her karede y ≈ 295–340, x = 60; 0. sn, orta, son kare tamam |
| HV-2 | evet | `senaryo.json` cümle 4 `ses: ogrenci` (`…9gjY`) | |
| HV-3 | evet | `senaryo.json:93,97` "Dersin tamamı YDS Publishing YouTube kanalında."; Whisper 1,00 | ses birebir; ekranda çekirdek cümle yazılı değil, `@ydspublishing · YouTube` var |
| HV-4 | evet | metin taraması | `ortak/*.js` dahil taranmış; yalnız `BRIEF-S1.md` kural cümlesi |
| HV-5 | evet | metin taraması | süre sözü yok |
| HV-6 | evet | sahne 08 (kare 25,4); `aciklama*.md` satır 1 | |
| HV-7 | evet | kontak son karo; kol a mirası kare 31,7 | kart ≈ 900×503, y 622–1125 (hedef ≈ 920×518, y 620–1140; %2 sapma) |
| HV-8 | evet | `senaryo.json` | 6 sorunun 6'sı evet (çıkar, en çok yanılınan, tek cümle, Türkçe köprü, izlemeden anlaşılır, sınav günü bakılır) |
| HV-9 | evet | `find` 0 | |
| HV-10 | evet | bütün kol b kareleri | y 0–280 ve 1570–1920 boş; altyazı y ≈ 1470 |
| HV-11 | evet | `zaman.json` | 4 sahne; 27,89 sn ≤ 35. Hedef 22–26 sn aşıldı (standart kabul sınırı içinde) |
| HV-12 | evet | `sureler.json`, `METIN.md` | ilk söz 0,50 sn; kanca sözü 2,00 sn, sahne 2,50 sn |
| HV-13 | evet | kare 25,4 (kol a mirası); `08/zamanlar.json` | kart girişi 0,55–1,00 sn, kuyruk 5,5 sn → kart ≥ 2 sn sabit; yer imi SVG; "Kaydet" var. Kol b'ye özgü kare yok (EK-3) |
| HV-14 | evet | kontak son karo; kare 31,7 | kart konumu doğru, "Gerisi bizde." Fredoka, `@ydspublishing · YouTube` satırı var |
| HV-15 | evet | s1 "Gerisi bizde." · s2 "Bitmedi, gel." · s3 "Bu sadece başlangıç." | listeden, derste yinelenmiyor |
| HV-16 | evet | s1 "Sınavdan önce lazım olacak. Kaydet." · s2 "Bu kuralı kaybetme. Kaydet." | listeden; s1 ile s2 farklı. s3 kalıbını taramadım (bu paketin kapsamı dışı) |
| HV-17 | evet | `sentez.wav.rapor.json` cümle 4: Whisper "YEDESE Publishing", 1,00; ekranda "YDS Publishing" | `ses-sozluk.json` dosyasını açmadım; rapor `YDS` → `YeDeSe` diyor |
| HV-18 | evet | `aciklama*.md` | ilk satır sabit; Reels ve TikTok'ta bağ yok ("profildeki bağlantı") |
| HV-19 | **hayır** | `grep` `utm_campaign` | bu paket (s1b) ve s1 doğru: `ING-YDT-GR-02-04-T`, `utm_content=s1b-a/-b`. **`02-04-ydt-temel-s2` ve `s2b` `aciklama.md`, `-a`, `-b` dosyalarında `ing-ydt-gr-02-04-t` (küçük harf, 6 yer)**; 02-02 paketleri büyük harf. Altı paket birlikte tutarsız |
| HV-20 | evet | `surumler.json`; AB §4 | kol b 1 kapak (A = kanca karesi, karakterli: öğretmen figürü) + 2 açıklama; kapak B/C ve hikâye grupta (s1) |
| HV-21 | kanıt yok | kol b'de hikâye karesi yok | AB §4 hikâyeyi gruba bırakır; kol a jürisi bakar. Jüri kuralı gereği kaldı sayılır, şef onaylasın |
| HV-22 | **hayır** | `kapi-cikti.txt` | "çıkış kodu 0" ama `02-paperjs-ornek \| 4.50–4.50 sn \| -um. × yor çip 1 \| 72x11 px \| uyari`: 1 uyarı. Ölçüt "0 uyarı". Üretici "kol a'dan miras" diyor (kol a 8,37–8,43 sn, 72x12 px); miras olması uyarıyı kapatmaz |
| HV-23 | evet | `sentez.wav.rapor.json` | en düşük 0,96 (cümle 2 `I'm living` duyuldu, önbellek); yeni cümle 1,00; çağrı 1,00 |

## Madde tablosu — §2d A/B kolu (AB)

| Kimlik | Hüküm | Kanıt | Not |
|---|---|---|---|
| AB-1 | evet | `surumler.json` `varyant {grup s1, kol b, degisken kanca, deger soru}` | s1 → `kanca` atamaya uygun; kol a satırı `kol: a, kopru` |
| AB-2 | evet | kendi `diff -rq` çıktım (96 satır) | görünür fark yalnız kanca (sahne 01, cümle 1, süre kayması, kapak A, utm). Sahne 02 ve `kunye.js` farkları kanca kırpımının sonucu; bayt eşitliği için AB-3'e bak |
| AB-3 | **hayır** | `diff -rq`: sahne 02 (`sahne-02.js`, `kalem-paper.js`, `sayfa.html`, `calistir.sh`, `SPEC.md`, `RAPOR.md`), `ortak/kunye.js` | ölçüt "sha256 aynı". Değer sahnesi (sahne 02) kodu farklı: `T_BAS 3.0 → 2.5`, `KARE 522 → 421`, kol a yolları, cümle 1 çapaları. `kunye.js` (kanal katmanı) `KOK` yolu farklı. Çekirdek cümle ve ses kadrosu aynı (cümle 2–4 sha256 eşit). İçerik eşdeğerliği yalnız üreticinin 6 örnek ölçümüne dayanıyor; ben yeniden ölçmedim |
| AB-4 | kanıt yok | yayın takvimi yok | Ş maddesi; yayın öncesi |
| AB-5 | kanıt yok | API çağrılmadı | dosya düzeyinde: `.mp4` 0, `surumler.json`'da mp4 alanı yok |
| AB-6 | evet | `surumler.json`; `aciklama-a.md`, `-b.md` | `varyant` var; `utm_content=s1b-a` ve `s1b-b` |
| AB-7 | kanıt yok | kazanan ilanı yok | Ş maddesi; ölçüm başlamadı |

## Madde tablosu — ilgili EK maddeleri

| Kimlik | Hüküm | Kanıt | Not |
|---|---|---|---|
| EK-1 | evet | `METIN.md`, `senaryo.json` | seste `YDT` yok; marka `YeDeSe` okunuyor |
| EK-2 | evet | bütün kol b kareleri | emoji yok; yer imi SVG |
| EK-3 | **hayır** | `…/03-hyperframes-cta/k/`, `…/08-hyperframes-kaydet/k/` | kol b'ye özgü kare eksik: sahne 08 açık + koyu, sahne 03 koyu. KBC-RAPOR "sahne 03 son kare 27,85" diyor; o kare yalnız kontak karosunda var, ayrı dosya yok. Hikâye ve kapak B/C hücreleri kol b'de yok (AB §4) |
| EK-5a | evet | sahne 01 ve 02 kareleri | üstü çizili ya da "yanlış" işaretli cümle yok |
| EK-5b | evet | bağımsız dilbilgisi denetimi | "I live in Istanbul." kalıcı durum, geniş zaman ✓. "I am living with my uncle." geçici durum, şimdiki zaman ✓. "Kalıcıysa geniş zaman, geçiciyse şimdiki zaman." yön gösterici kural; "üç farktan biri" çerçevesiyle kabul. Kanca cevabı ("ikisi ayrılır") doğru |
| EK-5c | **hayır** | `senaryo.json` cümle 2 "Hep orada: kalıcı durum, geniş zaman."; kare 14 ve 16,13 ekranda "Hep orada." | "hep" istisnasız söylem; geniş zaman kalıcı durumda "hep orada" demek değildir (`I live in Istanbul` bugün de yaşıyor demektir, ömür boyu değil). Kol a ile aynı cümle, yani ana dersteki kısa da aynı hatayı taşıyor |
| EK-6 | **hayır** | `aciklama.md:1,5`, `aciklama-a.md:4-6,48`, `aciklama-b.md:4-5,50` | kol b başlık notları kol a künyesini taşıyor ("02-04-ydt-temel-s1", "Shorts … 31,75 sn" oysa 27,89; "Sürüm: A (`s1-aciklama-a`)"). Kırık atıf: `aciklama.md` `hikaye.png`; `aciklama-a.md` `hikaye-a.png`; `aciklama-b.md` `kapak-b.png`, `hikaye-b.png`. Bu dosyalar `s1b` içinde yok (grupta, `s1`). Yazım hatası ve tamlama hatası bulunmadı ("konusunun püf noktası" doğru) |
| EK-7 | evet | `kapak-a-koyu.png`; sahne 01 koyu; sahne 02 koyu (10); sahne 08 koyu; sahne 03 koyu | koyuda okunuyor; son ikisi kol a mirası |
| EK-9 | evet | `senaryo.json` | tek soru, 5 sözcük ("Bu iki yaşıyorum aynı mı?"); kısa ≤ 1 |
| EK-12 | **hayır** | kare 0 ve kontak ilk karo; `METIN.md` cümle 1 sözcük zamanları | `YAŞIYORUM / AYNI MI?` 0. karede ekranda; ses 0,50'de başlar, "aynı mı" 1,86–2,22 sn'de söylenir → ekran sesten önce. Motor zaman kapısı çıktısı yok (`kapi-cikti.txt` yalnız çakışma kapısı). Soğuk açılış (K23) için başlığın 0. sn'de durması savunulabilir; ölçüt metni istisna tanımıyor |

## Kol a ↔ kol b yan yana

| Boyut | Kol a (`kopru`) | Kol b (`soru`) | Hüküm |
|---|---|---|---|
| Kanca sözü | "Türkçede yaşıyorum tek sözcük…" (5,36 sn) | "Bu iki yaşıyorum aynı mı?" (2,00 sn) | tek değişken |
| Değer, kaydet, çağrı sözü | cümle 2–4 | aynı (sha256 eşit) | aynı |
| Kapak A | köprü karesi | `YAŞIYORUM / AYNI MI?` | değişkenin parçası |
| Açıklama gövdesi | A + B seti | A + B seti, yalnız `utm_content` farklı | aynı (başlık notları bayat, EK-6) |
| Süre | 31,75 sn | 27,89 sn | fark −3,86 sn: kancanın kısalmasının doğal sonucu; "ortalama izlenen yüzde" kıyasında bu sapma kol b lehine yanlılık katar. Sonuç okunurken not düşülmeli |
| Kanal katmanı, künye, rozet | aynı | aynı | aynı |

Söz, ekran metni, kapak ve açıklama farkı: kanca dışında değişiklik yok. Tek istisna süre kayması ve `Hep orada` gibi iki kolda ortak kusurlar.

## Kaldı maddeleri için düzeltme önerisi (tek cümle)

| Kimlik | Öneri | Kim |
|---|---|---|
| HV-19 | `02-04-ydt-temel-s2` ve `s2b` `aciklama*.md` dosyalarında `utm_campaign` değerini `ING-YDT-GR-02-04-T` yap (6 yer), sonra bütün paketlerde `grep` ile doğrula. | Üretici; jüri bu paketin dışına yazmaz |
| HV-22 | Sahne 02'de `yor` çipini `-um.` sözcüğünden uzaklaştır (kol a ile birlikte), kapıyı `--sikilik 30` ile yeniden koş, 0 uyarıyı kanıtla. | Üretici (iki kola birlikte) |
| AB-3 | Ya AB-3 ölçütüne "içerik eşdeğerliği piksel ölçümüyle kanıtlanır" kabulü ekle (şef kararı) ya da sahne 02'yi kol a ile aynı bayt kodla çalıştırıp `T_BAS`'ı parametre dosyasından ver. | Şef |
| EK-3 | Kol b için sahne 08 (açık + koyu) ve sahne 03 (koyu) kare yakala, `k/` altındaki kol a karelerini kol b adlarıyla ayır (silme yok, `~/Silinecekler/` altına taşı). | Üretici |
| EK-5c | Cümle 2'de "Hep orada: kalıcı durum" yerine "Orada, kalıcı durum" (ekranda "Hep orada." → "Orada.") yaz; kol a ve kol b'ye birlikte uygula, sesi yeniden sentezle. | Üretici (iki kola birlikte) |
| EK-6 | Kol b `aciklama*.md` başlık notlarını `s1b` künyesine ve 27,89 sn'ye çevir; `hikaye*.png` ve `kapak-b.png` atıflarını `../02-04-ydt-temel-s1/` yoluna yönelt ya da "grup dosyası" diye yaz. | Üretici |
| EK-12 | Ya başlık satırlarını ilk söz anında (0,5 sn) getir ya da `juri-olcutleri.md` EK-12'ye "soğuk açılış başlığı 0. sn'de durabilir" istisnasını yaz. | Şef |
| HV-21 | Kol b'de hikâye karesi yok; AB §4 bunu kabul ediyorsa `juri-olcutleri.md` HV-20/21'e "kol b kapak A hariç grupta" notu ekle. | Şef |

## Ana derse geri besleme

1. `Hep orada: kalıcı durum, geniş zaman.` ana derste de varsa aynı düzeltme gerekir (EK-5c); ana dersin `senaryo.json` metnini ara.
2. Ana ders kapağı `HER ZAMAN mı ŞİMDİ mi?` soru olarak kalır (iddia değil), ama "her zaman" sözü EK-5c taramasında tetiklenir; ana derste kapak metni gözden geçirilsin.
3. `YDT · BASIC` (üst rozet) ile `YDT · TEMEL` (ana kapak kartı) aynı karede yan yana: huni v2 §9 açık işi hâlâ açık; her iki kolda ve ana derste birlikte `YDT · TEMEL` yap.
4. Sahne 02'deki `yor` çipi / `-um.` kesişimi kol a ile ortak; ana ders sahnesi de aynı çipi kullanıyorsa orada da ölç.
5. Sahne klasörlerindeki `k/` kare dizini paket kopyalanırken eski paketin karelerini taşıyor; kopya betiği `k/` dizinini boş açmalı (jüri yanlış kareye güvenir).
