# S3-A raporu — simple-present-temel-s3 · 15.11.2026 (istem P0202-S3-A)

| Dosya | İçerik | Durum |
|---|---|---|
| `senaryo-taslak.md` | 4 sahne (kanca → değer → kaydet → çağrı), 4 cümle, 9 parça; kaynak eşlemesi; süre tahmini; B planı | TASLAK |
| `kapak-taslak.md` | 3 kapak: A kanca karesi (karakterli), B soru, C kural kartı + karşıt çift | TASLAK |
| `hikaye-taslak.md` | 2 hikâye karesi: A kural özeti + Kaydet, B "Hangisi doğru?" + Kaydet | TASLAK |
| `aciklama-taslak.md` | 2 set × 3 platform (YouTube, Instagram, TikTok) + UTM tablosu | TASLAK |
| `S3-A-RAPOR.md` | bu rapor | — |

Ses sentezi, ElevenLabs çağrısı, render, sahne kodu, git commit ve alt ajan YOK. Yazma yalnız bu dizinde.
Metin taraması (standart §7 kapı 3): bu dizinde standart §1 kural 4 sözü ve süre sözü yok (grep, 15.11).

## 1. Süre tahmini

Tahmin **25,48 sn** (hedef 22–26; tavan 28). Hesap:

```
ilk söz 1,00
+ cümle 1: EN 1,50 + 0,25 + TR 1,04                     = 2,79  → 3,79
+ 0,55 + cümle 2: TR 3,84 + 0,15 + TR 2,20 + 0,25 + EN 2,72 = 9,16  → 13,50
+ 0,55 + cümle 3: TR 1,74 + 0,15 + TR 2,56               = 4,45  → 18,50
+ 0,55 + cümle 4: öğrenci 5,43                           = 5,43  → 24,48
+ kuyruk 1,00                                                    → 25,48
```

| Parça türü | sn | Kaynak |
|---|---|---|
| Ölçülmüş, birebir | 3,84 + 5,43 = 9,27 | ana ders cümle 7 parça 4; 02-04 S3 cümle 5 (önbellek) |
| Ölçülmüş ikiz (aynı metin, başka komşu) | 2,56 | 02-04 S3 cümle 4 parça 2 |
| Yakın ikizden türetilmiş | 1,50 + 1,04 + 2,20 + 2,72 = 7,46 | ana ders cümle 4 ve 7 sözcük zamanları |
| Hece hızından | 1,74 | ana ders TR ortalaması 4,03 hece/sn |
| Boşluk + ilk söz + kuyruk | 4,45 | `el.py` 0,25 / 0,15; cümle arası 0,55; ilk söz 1,00; kuyruk 1,00 |

En kötü durum: ölçülmemiş 9,20 sn %11 uzun çıkarsa (S1 sapması) → **26,49 sn**; 28 sn içinde (pay 1,51 sn). B planı `senaryo-taslak.md` §5.

## 2. Standart §5 ölçütleri

| # | Soru | Cevap | Dayanak |
|---|---|---|---|
| 1 | Sınavda çıkar mı? | evet | yardımcı fiil + yalın fiil yapısı dil sınavı gramer sorularının tabanı; öğe paketi `02-02-ydt-temel` amaç 4 bunu "doesn't eats tuzağı" diye adlandırır. Kendi soru sayımımız yok |
| 2 | Öğrenci en çok burada mı yanılır? | evet | öğe paketi amaç 4 ve `canAlici[1]` tuzak olarak tanımlar. Kendi hata verimiz yok (ölçülmedi) |
| 3 | Kural tek cümleye sığar mı? | evet | `Does varsa fiil yalın.` (4 sözcük) |
| 4 | Türkçe köprüyle gösterilir mi? | hayır | yalnız soluk TR çeviri var (`O gitmez.`, `O gider mi?`). Ana dersteki köprü (git-er = go-es) olumlu cümle içindir; olumsuz ve soruya yapı köprüsü kurmadım |
| 5 | Dersi izlemeden anlaşılır mı? | evet | kanca + kural + iki doğru örnek + özet kısa içinde. Ön koşul: he/she/it ile fiile s gelir bilgisi (S1 verir; S3 söylemez) |
| 6 | Sınav günü yeniden bakılır mı? | evet | kural kartı (sahne 3), kapak C, hikâye A |

Sonuç: **5 / 6 evet** (eşik 4).

## 3. Sürümler arası fark

| Türev | Sürüm | Fark |
|---|---|---|
| Kapak | A `BU CÜMLE` / `YANLIŞ` | yanlış cümleyi gösterir, karakter işaret eder; nedeni videoya bırakır; videonun ilk karesi |
| Kapak | B `GOES mu,` / `GO mu?` | iki şık sorar, vurgu yalnız `?`; figür yok |
| Kapak | C `DOES VARSA` / `FİİL YALIN` | kuralı ve karşıt çifti verir; kaydedilecek kapak; figür yok |
| Hikâye | A | kural + bir yanlış, iki doğru satır + Kaydet; alt bant boş |
| Hikâye | B | soru tuzağı tek kökte, iki şık + ipucu + Kaydet; cevap karede yok |
| Açıklama | A | kuralla açılır; YANLIŞ → DOĞRU çiftleri; kapak C ile koşut |
| Açıklama | B | soruyla açılır; yalnız doğru cümleler + neden; kapak B ile koşut |

Üç kapak da ana kapak metnini (`GİDER = GOES`) yinelemez. Bütün türevlerde ilk satır, kanal katmanı ve UTM şeması ortaktır.

## 4. Açık noktalar

1. **canAlici kaynağı.** Ana paket `simple-present-temel/surumler.json` listesinde does maddesi yok; taslak en yakın `[3]`'ü kullanır.
   Öğe paketi `projeler/02-02-ydt-temel/` (aynı kimlik, ayrı senaryo, jüri GEÇTİ) `canAlici[1]` S3 ile birebir örtüşür. Aynı kimliği
   iki paket taşır; hangisinin listesi esas: şef kararı.
2. **Rozet.** Standart §2 ve kapak-standardi `YDT · TEMEL` der; ana ders künyesi `YDT · BASIC` (ana BRIEF §0 madde 5: İngilizce derste
   şablonda Türkçe yok). Taslak bağlayıcı standarda uyar; seri tutarlılığı için şef bakar.
3. **Ana ders kapağı.** `simple-present-temel/kapak.png` bu worktree'de yok (kök PNG git'e girmez, ayna ile gelir). Dosya gelmezse
   standart §7 kapı 5 gereği kısa "bekliyor" kalır. Kaynak sahne `sahneler/90-hyperframes-kapak/` var.
4. **Whisper ve yanlış cümle.** `He doesn't goes.` parçasında Whisper "go" yazabilir; benzerlik 0,9 altına düşebilir. Kulak kararı
   gerekir; düşerse B planı 4 (kanca TR olur, metin değişir, jüri).
5. **Karakter ↔ kadro.** `karakter.png` genç erkek; ana `kadro.ogrenci` kadın (çağrı sesi kadın). Kapak-standardi §4 "karakter kadro
   tanımına uyar" der. Taslak karakteri konuşan öğrenci gibi göstermez (çağrı sahnesinde figür yok). Ayrıca ana `senaryo.json` `kadro`
   yalnız öğrenciyi taşır; öğretmen sesi `sesler.ogretmen` alanında (istem "kadro: öğretmen + öğrenci" der).
6. **Marka okunuşu.** `ses-sozluk.json`'da marka kaydı yok; yalnız `YDS` → `YeDeSe` kısaltması var (02-04'te Whisper 1,00). Standart §4
   "kayıt yoksa eklenir" der; dosya bu istemin yazma kapsamı dışında.
7. **Önbellek doğrulanmadı.** Cümle 4'ün önbellekten geleceği metin, sıra ve ses eşitliğine dayanır. Anahtarın öbür alanları
   (`SES_AKTIF`, `MODEL`, `HIZ_EK`) sentez anında görülür; srv21 önbellek dizininde kayıt aranmadı.
8. **Yineleme denetimi.** Çağrı girişi `Bu sadece başlangıç.` ve kaydet kalıbı 02-04 S3 ile aynı (başka ders; standart yalnız aynı
   derste yinelemeyi yasaklar). `simple-present-temel` S1 ve S2'nin v2 sürümü yok; onlar başka giriş ve kalıp seçmeli.
9. **Hitap.** Kaydet kalıbı "gönder" der; emsal S1 karar 5 (hitap yok) ile çelişir. Standart §4 kalıbı esas alındı.
10. **Ana kapak kartı genişliği.** Standart §3 kartı ≈ 920×518 der; ortalı yerleşimde sağ uç x ≈ 1000'e çıkar ve §2 içerik sınırını
    (x 960) 40 px aşar. Kontak sayfasında bakılır; gerekirse 900×506.
11. **Kanca kapak istisnası.** Kapak A başlığı ve kartı 0. karede tamdır, ses 1,00'da başlar. Emsal istisnası uygulandı
    (`kapak-taslak.md` §3 DİKKAT).

Sonraki adım: jüri (dil + kaynak-kural) bu dizindeki dört taslağı okur; [YENİ] işaretli 3 Türkçe ve 2 İngilizce parça önce bakılır.
