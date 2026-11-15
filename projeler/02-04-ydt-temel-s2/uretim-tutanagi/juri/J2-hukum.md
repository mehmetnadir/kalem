# J2-0204S2 — çıktı jürisi hükmü · `02-04-ydt-temel-s2` (kol a) · 15.11.2026

**Jüri modeli:** Claude Sonnet 5.5 (`claude-sonnet-5-5`), oturum 15.11 22:50–23:1x.
**Üretici oturum modeli:** bilinmiyor (`uretim-tutanagi/*.md` içinde model kaydı yok). Aynı model uyarısı: koyulamaz; üretici kaydı eklenince şef karşılaştırır (§1e açık).
Okuma kuralı: **evet** = ölçüt sağlandı. **hayır** ve **kanıt yok** = kaldı.

## Özet

| Bölüm | evet | hayır | kanıt yok |
|---|---|---|---|
| §2a Kısa video (HV-1…23) | 19 | 2 | 2 |
| §2c Kapak ve hikâye (KS-1…10) | 6 | 3 | 1 |
| Ek denetim (EK-*) | 10 | 0 | 3 |
| **Toplam** | **35** | **5** | **6** |

**Sonuç: KALDI.** Teslim kapısı (§1g, D-0338) kapalı kalır; önizleme adresi Nadir'e ve karta yazılmaz.

## Zaman kapısı (§1b)

| Kayıt | Zaman |
|---|---|
| Paketin son içerik değişikliği (`git log -1 -- projeler/02-04-ydt-temel-s2`, bc402eb) | 15.11 19:41:49 |
| PNG'lerin son yazımı (kapak/hikâye) | 18:58 – 19:26 |
| Eski jüri (`juri/s2.dil.md`, `s2.kaynak-kural.md`) | 12:22 – 12:24 |
| Bu hüküm | 15.11 ≈ 23:00 |

Eski jüri v2 çevirisinden (ses 18:25, sahneler 18:5x–19:32) ÖNCE koştu ve bayat. Bu hüküm son içerik değişikliğinden sonra yazıldı. Not: bu dosya paket içinde olduğu için `git log` zamanını yeniden ilerletir; kapı betiği `juri/` yolunu hariç tutmalı.

## Bakılan kanıt

| Tür | Dosya |
|---|---|
| Metin | `ortak/anlatim/senaryo.json`, `sureler.json`, `sozcukler.json`, `METIN.md`, `sentez.wav.rapor.json` (Whisper), `zaman.json`, `surumler.json`, `aciklama-a.md`, `aciklama-b.md`, `aciklama.md` |
| Kare, açık (Read ile açıldı) | `kapak-a|b|c.png`, `hikaye-a|b.png`; sahne 01 (0 ve 2,8 sn), 02 (2,84 · 10,1 · 17,35), 08 (17,41 · 20,1 · 20,72 · 22,27 · 22,7), 03 (22,75 · 29,35) |
| Kare, koyu (Read ile açıldı) | kapak A/B/C koyu, hikâye A/B koyu, sahne 02 (14,9), 08 (22,7), 03 (28,5) |
| Ölçüm | PIL ile kare farkı (08 kaydet kartı), piksel renk örneği, `md5sum`, `grep` (metin taraması) |
| Yapılmadı | `cakisma-kapisi.mjs` (başsız tarayıcı açar; `tarayici-kapisi` kuralı), kulakla dinleme, mp4 |

## §2a — Kısa video (huni v2)

| Kimlik | Hüküm | Kanıt | Not |
|---|---|---|---|
| HV-1 | evet | 0 sn: `sahneler/01…/k/…-0.png`; orta: `02…-10.1.png`, `08…-20.1.png`; son: `03…-29.35.png` | logo y ≈ 298–330, `@ydspublishing` y ≈ 295–340, x = 60; koyu karelerde de var |
| HV-2 | evet | `senaryo.json` cümle 4 `ses: ogrenci`; `sesler.ogrenci` = `oPC5I9GKjMReiaM29gjY` = ana ders `kadro.ogrenci.ses`; `sentez.wav.rapor.json` son 2 parça | |
| HV-3 | evet | `senaryo.json` cümle 4: "Dersin tamamı YDS Publishing YouTube kanalında." birebir | Whisper: "YEDESE Publishing" (marka okunuşu, bkz. HV-17) |
| HV-4 | evet | `grep -iE 'tam ders'` `ortak/*.js`, `ortak/anlatim/*.json`, sahne `index.html`, `uret.py`, açıklamalar: 0 | `BRIEF-S2.md` ve `sahneler/*/SPEC.md` yasağı adlandırır (belge, çıktı değil) |
| HV-5 | evet | `grep 'dakika'` aynı kümede: 0 | `calistir.sh` yorumlarında "1 dk yük" ve `04/uret.py` iddiası ("dk" yok kontrolü): yük ölçüsü, süre sözü değil |
| HV-6 | evet | sahne 08 (kare 20,1–22,7: "Kaydet" + yer imi); `aciklama-a.md` ilk satır "Sınav günü bakmak için kaydet. …" | |
| HV-7 | evet | `03…-29.35.png`: ana ders kapağı x 60–960, y ≈ 627–1133 (900×506) | standart ≈ 920×518; sapma %2, sağ sınır 960'ı aşmaz. Kart içinde `YDT · TEMEL`, künyede `YDT · BASIC` (bkz. KS-2) |
| HV-8 | evet | senaryo | sınavda çıkar · çok yanılınır · tek cümlelik kural · dersi izlemeden anlaşılır · sınav günü yeniden bakılır = 5 evet; Türkçe köprü yok (1 hayır) |
| HV-9 | evet | `find projeler/02-04-ydt-temel-s2 -name '*.mp4'`: boş | |
| HV-10 | evet | 11 açık + 8 koyu kare: üst boşluk y < 295; içerik en çok y ≈ 1380; altyazı y 1420–1520; y ≥ 1570 boş | kutu ölçümü yok, göz denetimi. Sahne 02 için 3 açık kare |
| HV-11 | evet | `zaman.json`: 4 sahne, 29,41 sn | kabul sınırı 35 sn altında; hedef 22–26 sn aşıldı (V2-C-RAPOR açık nokta 1) |
| HV-12 | evet | `sozcukler.json`: "Genel" t0 = 1,00 sn; kanca sahnesi 0–2,84 sn | ilk söz tam 1,00 sn: sınırda |
| HV-13 | **kanıt yok** | PIL kart farkı (x 60–960, y 560–1000): 20,1 → 20,72 sn = 0 px; 20,72 → 22,27 sn = 16.599 px; 22,27 → 22,7 sn = 16.479 px | Yer imi SVG ✓, "Kaydet" yazısı ✓. Ama "Today" hapı 22,27 sn'de solgun, 22,7 sn'de çerçeveli: kart 2 sn aynı piksel kalmıyor. 2 sn sabitliği gösteren kare çifti yok |
| HV-14 | evet | `03…-22.75`, `-29.35`: kart y 627–1133; "Bitmedi, gel." Fredoka 700; `@ydspublishing · YouTube` y ≈ 1170–1250 | |
| HV-15 | evet | "Bitmedi, gel." ∈ listesi; s1 "Gerisi bizde.", s3 "Bu sadece başlangıç." | derste yinelenmez |
| HV-16 | evet | "Bu kuralı kaybetme. Kaydet." ∈ listesi; s1 "Sınavdan önce lazım olacak.", s3 "Bir arkadaşına gönder; …" | |
| HV-17 | **hayır** | `araclar/iki-dilli/ses-sozluk.json:15` `"YDS": "YeDeSe"` ✓; ama Whisper `duyulan` = "YEDESE Publishing" | Standart §4 "Whisper 'YDS Publishing' duyuyor mu" beklenir; hiçbir koşuda "YDS" duyulmadı (§9 aynı sapmayı yazar). Karar şefte: kapıya "YEDESE ≡ YDS" eşlemesi ekle ya da §4'ü güncelle |
| HV-18 | evet | `aciklama-a.md` ilk satır sabit; Reels bloğunda adres yok ("Bağlantı profilde.") | |
| HV-19 | evet | `utm_campaign=ING-YDT-GR-02-04-T`: s1, s2, s3 açıklama dosyalarının hepsi büyük harf; `utm_content=s2-a` / `s2-b`; SP s2b `ING-YDT-GR-02-02-T` | 4 paket ölçüldü (6 değil). Küçük harf yalnız `s1/uretim-tutanagi/aciklama-taslak.md` içinde; s2 açıklamalarındaki "S1 küçük harf yazar" DİKKAT notu bayat (bkz. EK-6) |
| HV-20 | evet | kapak A: öğretmen figürü, B: öğrenci karakteri, C: karakter yok; hepsinde kanal katmanı, altyazı yok; hikâye 2; açıklama 2 | |
| HV-21 | **hayır** | `hikaye-a.png`: kanal + "Today iki zamanda…" + wears/is wearing + Kaydet, y 1150–1380 boş ✓. `hikaye-b.png`: kanal + "Hangisi doğru?" sorusu + Kaydet; kural özeti yok | A evet, B hayır. B'de yalnız "Genel mi, şu an mı?" ipucu var; S2-SON "cevap yok" bilinçli yazıyor. Karar şefte: B soru kartı ise §6'yı güncelle, değilse karta kural satırı ekle |
| HV-22 | **kanıt yok** | v2 çakışma kapısı çıktısı pakette yok; V2-C-RAPOR: durağan 04–07 "sahne bulunamadı" | Statik türevlerde G baktı: yazı–çizim binmesi yok. Video sahneleri için ölçüm eksik |
| HV-23 | evet | `sentez.wav.rapor.json`: 10/10 parça 1,00; çağrı parçası ekran metniyle 0,97 (V2-C-RAPOR) | ≥ 0,9 |

## §2c — Kapak ve hikâye karesi

| Kimlik | Hüküm | Kanıt | Not |
|---|---|---|---|
| KS-1 | evet | `file`: kapak-a/b/c, hikaye-a/b = 1080×1920; koyu karşılıkları `sahneler/*/k/koyu/` altında 5/5 var, 1080×1920 | Ölçüt 1920×1080 yatay + 4 PNG ders kapağı içindir; kısa dikey. Koyu PNG paket köküne kopyalanmadı, yalnız sahne `k/` klasöründe |
| KS-2 | **hayır** | 5 kapak/hikâye karesinde ve bütün sahne karelerinde rozet `YDT · BASIC`; ana kapak kartı `YDT · TEMEL` | Standart rozeti `YDT · TEMEL` yazar (kapak §2; huni §9 "BASIC taşıyan 6 kısa düzeltilir"). Aynı karede iki rozet metni çelişir (`03…-29.35`). Düzen huni v2 §2'ye uyuyor; kapak §2'nin dikey "orta bant" düzeni kısa için geçerli değil: ölçüt–standart çelişkisi şefe |
| KS-3 | **hayır** | piksel: zemin radyal krem gradyan (222,218,210 → 235,231,223); yazı (27,36,64) | Ölçüt `#fece00` / `#141414`; koyu zemin ≈ `#1b1a17`. Kısa kapak rengi huni v2 §6'da tanımsız; bütün huni seti aynı şablonu kullanıyor. Sonuç: ölçüt ile uygulama ayrışır; şef biri seçer. Çıkartma kenarı B'de krem ✓ |
| KS-4 | **hayır** | kapak B "TODAY VARSA HANGİ ZAMAN?" = `aciklama-b.md` YouTube başlığı "Today varsa hangi zaman?" | Birebir yineleme. A ("GENEL ≠ ŞU AN", 3 sözcük) ve C ("AYNI FİİL, İKİ ZAMAN", 4 sözcük) başlıkla örtüşmüyor |
| KS-5 | evet | `ortak/kapak/karakter.png` md5 `3d846e4b…` = ana ders dosyası; ana ders `KAYNAK.json`: `nano-banana-2`, 1k, 0,04 USD; görselde yazı/harf/logo yok (`today`, `?` HTML/SVG) | s2 paketinde kendi `KAYNAK.json` yok; izlenebilirlik md5 ile |
| KS-6 | **kanıt yok** | `kapak-168.png` yok | Göz notu: ana yazı 90+ px; 168 px genişlikte ≈ 14+ px; okunur görünür. Dosya üretilip Read ile bakılmadı |
| KS-7 | evet | A "ŞU", B "HANGİ", C "FİİL", "İKİ": büyük Ş, İ doğru çizildi | Ğ yok |
| KS-8 | evet | A, B, C kareleri | B'de "HANGİ ZAMAN?" sağ kenarı x ≈ 958: platform sağ bölgesinin (960) hemen önünde |
| KS-9 | evet | 3 kapak + 2 hikâye, açık + koyu | emoji yok |
| KS-10 | evet | kapak B: genç kadın, uzun kâkül, yuvarlak gözlük = `kadro.ogrenci` (kadın, LongBangs, GlassRound); kapak A: öğretmen figürü (erkek, kısa saç) | |

## Ek denetim (jüri talebindeki özel aramalar)

| Kimlik | Hüküm | Kanıt | Not |
|---|---|---|---|
| EK-1 | evet | `ses-sozluk.json`: `YDS → YeDeSe`; anlatımda YDT yok | Marka adı harf harf okunuyor; D-0340 Nadir onayı var. Ölçüt metnine "marka istisnası" yazılmalı |
| EK-2 | evet | 21 açık/koyu kare | emoji yok |
| EK-3 | evet | tema × sahne: 01 (açık 0 / 2,8; koyu 0,9), 02 (açık 3; koyu 14,9), 08 (açık 5; koyu 22,7), 03 (açık 2; koyu 28,5); türev 5 × 2 tema = 10/10 | boş hücre yok. Yatay yön: kısa dikey, uygulanmaz |
| EK-5a | evet | hiçbir karede üstü çizili ya da "yanlış" işaretli cümle yok; hikâye B'de A şıkkı çizili değil | T-s1 hikâye B hatası tekrarlanmadı |
| EK-5b | evet | bağımsız doğrulama: "She wears her coat in the winter." (alışkanlık, Simple Present ✓) · "She is wearing her pink T-shirt today." (Present Continuous ✓) · "Today iki zamanda da geçebilir; farkı anlam yapar." ✓ · hikâye B: "Look! She ___ her pink T-shirt today." → **is wearing** ✓, `wears` yanlış ✓ ("Look!" konuşma anı) | Ana ders kapağı "HER ZAMAN mi ŞİMDİ mi? · I live · I am living": `I am living` geçici durum, "şimdi" ile tam örtüşmez; hata değil, ana derse geri besleme |
| EK-5c | evet | metin taraması `her zaman|hep|always`: açıklama/senaryo/sahne metinlerinde 0; ana kapak "HER ZAMAN mi" soru, kural değil | "iki zamanda da geçebilir" mutlak değil |
| EK-6 | evet | `aciklama-a.md`, `aciklama-b.md`: yazım, tamlama, İ/ı, noktalama hatası yok; "konusunda püf nokta" doğru | Sabit cümle hatası yok. Bakım kusuru: §4 "S1 küçük harf yazar" DİKKAT notu bayat (s1 dosyaları büyük harf) |
| EK-7 | evet | koyu: 5 türev + sahne 02, 08, 03 | okunur |
| EK-8 | **kanıt yok** | `uretim-tutanagi/kontak/s2-huni-yanyana.png` 13:27'de üretilmiş (v2'den önce), v2 kontak sayfası yok | klişe işaret sayımı yapılamaz |
| EK-9 | evet | anlatımda tek soru: "Genel mi, şu an mı?" (5 sözcük); hikâye B sorusu 8 sözcük | kısa ≤ 1 ✓ |
| EK-10 | evet | `T shirt` (tire), `YeDeSe`, şık harfi yok, `ve,` yok | |
| EK-11 | **kanıt yok** | dinleme kaydı yok | `T shirt` ve öğrenci sesiyle "Bitmedi, gel." kulakla dinlenmedi; marka D-0340 dinlendi |
| EK-12 | **kanıt yok** | motor zaman kapısı çıktısı pakette yok | Örnek karelerde ekran metni sesle uyumlu (02 @10,1 / @14,9; 08 @20,1) |

## Kaldı maddeleri ve düzeltme önerisi

| Kimlik | Tek cümle öneri |
|---|---|
| HV-13 | 08 sahnesinde "Today" hapı animasyonunu kartın 2 sn sabit penceresinden sonraya al ya da 20,2 / 21,2 / 22,2 sn kare üçlüsüyle sabitliği kanıtla. |
| HV-17 | Whisper kapısına "YEDESE = YDS" eşlemesi ekle ya da huni v2 §4'teki "YDS Publishing duyulur" beklentisini "YEDESE Publishing" olarak güncelle (şef kararı). |
| HV-21 | `hikaye-b.png` karesine tek satır kural özeti ekle ya da huni v2 §6'ya "B kol soru kartı olabilir" istisnasını yaz. |
| HV-22 | `cakisma-kapisi.mjs` v2 sahneleri için `ortak-tarayici ws` ile koşulsun; çıktı `uretim-tutanagi/kontak/` altına yazılsın. |
| KS-2 | Rozet metnini `YDT · TEMEL` yap (künye + kapak + hikâye + 8 sahne); ana kapak kartıyla çelişki bitsin; kapak §2 dikey düzenine kısa için istisna yaz. |
| KS-3 | Kısa kapak renk şablonunu (krem gradyan, lacivert yazı) kapak standardına kayda geçir ya da `#fece00` ölçütünü ders kapağına daralt. |
| KS-4 | Kapak B ana yazısını YouTube başlığından ayır ("TODAY VARSA…" ya da başlık değişsin, biri). |
| KS-6 | `kapak-a|b|c` için 168 px küçük görünüm üret ve Read ile bak. |
| EK-8 | v2 karelerinden yeni kontak sayfası üret, klişe işaretlerini say. |
| EK-11 | "T shirt" ve öğrenci çağrısını Nadir dinlesin; kayda yaz. |
| EK-12 | Motor zaman kapısını çalıştır, çıktıyı tutanağa koy. |

## Ana derse geri besleme (`02-04-ydt-temel`)

1. Ana ders kapağı `HER ZAMAN mi ŞİMDİ mi?` ve `I am living` geçici durumu gösterir; "şimdi" sözü konuşma anı anlamına kayar. Kapağı "KALICI mı GEÇİCİ mi?" ile hizalamak öneri; hata değil.
2. Ana kapak kartı `YDT · TEMEL` taşıyor; ders içi künye `YDT · BASIC`. Aynı rozet düzeltmesi ana derste de geçerli.
3. Hat bayrağı: `huni-v2-standart.md` §4 "Whisper YDS Publishing duyar" beklentisi ölçümle çelişiyor; aynı sorun s1, s3 ve 02-02 kısalarında da çıkar.
4. `juri-olcutleri.md` KS-2/KS-3 ders kapağı içindir; kısa kapak ölçütü yok. Kısa kapak için ayrı satırlar eklenmeli.
