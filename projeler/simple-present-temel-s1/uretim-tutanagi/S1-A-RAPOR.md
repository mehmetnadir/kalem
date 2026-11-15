# S1-A raporu — simple-present-temel-s1 (02-02-ydt-temel-s1) · huni v2 taslak · 15.11.2026

| Dosya | İçerik | Durum |
|---|---|---|
| `senaryo-taslak.md` | 4 sahne (kanca → değer → kaydet → çağrı), 4 cümle / 7 parça, kaynak eşlemesi, ses notları, süre hesabı | TASLAK |
| `kapak-taslak.md` | 3 kapak: A `GO mu,` / `GOES mu?` · B `FİİLE -S` / `HANGİ ÖZNEYLE?` (karakterli; jüri K1) · C `HE GOES` / `I GO` | TASLAK |
| `hikaye-taslak.md` | 2 durağan kare: A kural özeti kartı + `Kaydet` · B "Hangisi doğru?" + `Kaydet` | TASLAK |
| `aciklama-taslak.md` | 2 set × (YouTube başlık + açıklama, Reels, TikTok); UTM `s1-a` / `s1-b` | TASLAK |
| `S1-A-RAPOR.md` | bu belge | — |

Ses sentezi, ElevenLabs çağrısı, sahne kodu, render, commit YOK. Pakette başka dosyaya dokunulmadı; eski kısa yerinde.

## 1. Senaryo özeti

```
Kanca (öğretmen)   Kardeşim gider: go mu, goes mu?
   → Değer (öğretmen)   My brother goes to school by bus.
                        Özne he, she ya da it olunca fiile s gelir.
                        I, you, we, they ile gelmez.
   → Kaydet (öğretmen)  Sınavdan önce lazım olacak. Kaydet.     [ekran: He, she, it: s gelir; / I, you, we, they: s yok.]
   → Çağrı (öğrenci)    Gerisi bizde. Dersin tamamı YDS Publishing YouTube kanalında.   [ekran: ana ders kapak.png + @ydspublishing · YouTube]
```

Ana dersin bir cümlesiyle birebir aynı cümle yok. Cümle 4 02-04-ydt-temel-s1 cümle 4 ile birebir: önbellek adayı (Whisper 1,00 · 1,00).
Jüri işaretli Türkçe: cümle 1 (yeni), cümle 2 parça 2 (eski S1, ana derste yok), cümle 3 ve 4 (standart kalıbı). Hikâye B kökü (EN, yeni).

## 2. Süre tahmini

| Sahne | Ölçülmüş ikiz | Tahmin |
|---|---|---|
| 1 Kanca | sözcük toplamı (eski S1 `Kardeşim`, `goes`; ana ders `gider`; duraklamalar) 3,35 sn | 0,00–4,35 |
| 2 Değer | eski S1 parça 2,16 + 4,64; ana ders cümle 7 alt dilimi 3,68; parça arası 0,25 + 0,15 | 4,35–15,78 |
| 3 Kaydet | 02-04-s1 cümle 3 parça 2: 2,72 sn | 15,78–19,05 |
| 4 Çağrı | 02-04-s1 cümle 4: 4,71 sn + kuyruk 1,00 | 19,05–25,31 |

Hesap: ilk söz 1,00 + 3,35 + 0,55 + (2,16 + 0,25 + 4,64 + 0,15 + 3,68) + 0,55 + 2,72 + 0,55 + 4,71 + 1,00 = **25,31 sn** (hedef 22–26).
Kötü durum (S2 sapma payları: cümle 1 +%28, ikizi alt dilim olan parça +%10, metni birebir ikizli parçalar +%5, önbellek 0):
+1,79 sn → **≈ 27,1 sn** (28 sınırına pay ≈ 0,9 sn). Aşarsa B planı (ilk söz 0,50, kuyruk 0,44) −1,06 sn; metin değişmez.

## 3. Standart §5 ölçütleri (6 sorudan en az 4 "evet")

| # | Soru | Yanıt | Dayanak |
|---|---|---|---|
| 1 | Sınavda çıkar mı? | evet | özne–fiil uyumu boşluk doldurma ve cümle tamamlamada fiil biçimini belirler; YDT soru sayımı ölçülmedi |
| 2 | Öğrenci en çok burada mı yanılır? | evet (ölçülmedi) | ana derste öğrencinin tek sorusu bu ("Neden hep s?", cümle 6); `canAlici[0]` ve `[3]` aynı noktayı taşır |
| 3 | Kural tek cümleye sığar mı? | evet | `He, she, it: s gelir; I, you, we, they: s yok.` (2 satır, 21 · 24 karakter) |
| 4 | Türkçe köprüyle gösterilir mi? | evet | `Kardeşim gider` → `My brother goes`; bir Türkçe söz, iki İngilizce aday (`go` / `goes`) |
| 5 | Dersi izlemeden anlaşılır mı? | evet | örnek + kural kısa içinde tam; do / does ve olumsuz biçim gerekmez |
| 6 | Sınav günü yeniden bakılır mı? | evet | kaydet kartı ve hikâye A aynı tek cümleyi taşır |

Sonuç: **6 / 6 evet** (1 ve 2 gözleme dayalı; ölçüm yok).

## 4. Sürümler arası fark

| Tür | A | B | C |
|---|---|---|---|
| Kapak | videonun sorusu, ilk kare, kâğıt zemin, kalem figür + otobüs | başka soru (fiile -s hangi özneyle?), sarı zemin, karakter + otobüs | cevap çifti (`HE GOES` / `I GO`), kâğıt zemin, figürsüz |
| Hikâye | kural kartı (videodaki örnek, he tarafı) | soru–cevap (yeni kök, they tarafı; doğru şık yeşil) | — |
| Açıklama | doğrudan: köprü + kural; kapak C ile eşleşir | soru ile açılır; kapak B ile eşleşir | — |

## 5. Açık noktalar

1. **Kaydet sahnesinin sesi.** Standart §3 ses sütunu yalnız kaydet kalıbını söyler; taslak kural özetini ekranda (kart) verir, seste
   vermez. İstem "kural özeti tek cümle + kalıp" diyor; seste de istenirse +2,5–3,7 sn → tahmin ≈ 28 sn, hedef aşılır. Karar şefte.
2. **Kanca 4,35 sn** (standart 0–4 sn; +0,35). B planındaki ilk söz 0,50 bunu kapatır.
3. **Okunuş riski:** cümle 1'de `go` / `goes` TR parçada (kulak kararı). Cümle 2'deki zamir listeleri jüri D1 ile EN parçaya alındı
   (`He, she, it` · `I, you, we, they`); ölçülmüş risk TR `/aɪ/` → "A" kalktı. Ses kapısı sonucu `S1-C-RAPOR.md`.
4. **Kapak C figürsüz** (kalıp §4 "figür + nesne" sapması; S2 C ile aynı). Karar şefte.
5. **Karakter ve kadro uyuşmazlığı:** `karakter.png` erkek (kıvırcık, gözlüklü); `kadro.ogrenci` kadın (uzun perçem, yuvarlak gözlük);
   ana derste `kadro.ogretmen` yok. Karakter kapak B'de ve ana kapakta kalır; videoda konuşan figür olarak kullanılmaz (K22).
   Kapak standardı §4 "karakter dersin kadro tanımına uyar" maddesiyle çelişir. Nadir/şef kararı.
6. **`usually`'siz örnek:** ana ders cümle 4 `usually`'li; kısa eski S1'in `usually`'siz biçimini kullanır (tek fikir; *usually* sinyal
   sözcük kısasına kalır). Jüri bakacak.
7. **Hikâye B yeni kök:** `My parents ____ to work by bus.` ana derste yok; jüri bakacak.
8. **Adresler:** `platform_url` canlılığı ölçülmedi; `{UZUN_VIDEO_URL}` ana ders yüklenince dolar.
9. **Paketteki eski kısa** (`ortak/anlatim/senaryo.json`, `BRIEF-S1.md`, sahneler 01–03; rozet `YDT · BASIC` + `GRAMMAR`) v2'ye ayrı istemle
   çevrilir. Ana dersin `kapak.png` / `kapak-koyu.png` dosyaları var (standart §7 kapı 5 karşılanır).
10. **Söz kalıbı tüketimi:** bu kısa `Gerisi bizde.` ve `Sınavdan önce lazım olacak. Kaydet.` kullanır. Aynı dersin S2 ve S3'ü başka giriş
    ve başka kaydet kalıbı seçer (standart §4).
