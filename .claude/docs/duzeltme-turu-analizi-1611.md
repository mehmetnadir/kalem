# Düzeltme turu analizi — neden "hayır" listesi küçülmüyor (16.11.2026)

> Kaynak: srv21 salt okuma. 11 ders (dikey eşleri aynı hükümde), 18 DJ hükmü, 10 DUZ3 + 10 DUZ3B + 5 KNT oturum kaydı.
> Ölçüt kaynağı: `dijital-anlatim/.claude/docs/juri-olcutleri.md`. Madde kimlikleri hükümlerin ilk sütunundan alındı.

## 0. Ana bulgu

Döngü dönmüyor çünkü düzeltici zaten çoğu maddeyi **istemiyle yasaklanmış** durumda. Tablo:

```
jüri "hayır" → DUZ3B istemi: yalnız cümle/ekran metni/rozet/altyazı satırı
             → öteki maddeler "ölçüt kararı", "motor işi", "KNT işi", "render yasak" → dokunma
             → KNT oturumu (kanıt) 5/5 limitte 0 turda öldü
             → render yok → bir sonraki jüri aynı maddeleri yine "hayır" yazar
```

İkinci bulgu: iki hüküm arasında **düzeltme turu çalışmamış** olan çiftler "kalıcı" görünür (aşağıda §2).
Üçüncü bulgu: kanıt dosyaları (`kanit/`) eklendikçe jüri daha çok "hayır" yazıyor; bu gerileme değil, görünürlüktür.

## 1. Özet tablo

"Satır" = hükümdeki `hayır` içeren tablo satırı (cümle ve kart satırları dahil). "Kimlik" = yalnız ölçüt kimlikli hayır sayısı.
"Kalıcı" = en az 2 hükümde kalan kimlik. Maliyet = `total_cost_usd`.

| Ders | Hüküm | Hayır satırı ilk → son | Kalıcı kimlik | Düzeltici (DUZ3 / DUZ3B) | Maliyet |
|---|---|---|---|---|---|
| present-continuous | 2 | 7 → 9 | DK-2, EK-3, EK-6, ST-1, ST-2 (5) | Opus / çıktı yok (çalışıyor) | 19,74 $ |
| present-continuous-ileri | 3 | 11 → 15 → 15 | DK-1, DK-2, EK-3, EK-5c, KS-10, ST-1, KS-6, DK-3, EK-12, ST-2 (10) | Opus / Sonnet | 18,12 + 0,84 $ |
| simple-present-temel | 1 | 10 | — | Opus (json boş) / yok | ? |
| simple-present-ileri | 2 | 9 → 11 | DK-1, DK-2, EK-1, EK-3, ST-1, KS-6 (6) | Opus / Sonnet (rapor var, json yok) | 15,37 $ + ? |
| 02-03-ydt-temel | 1 | 18 | — | Opus / çıktı yok | 12,14 $ |
| 02-04-ydt-temel | 3 | 6 → 2 → 9 | HV-24, EK-5b (2) | Opus / Sonnet | 18,99 + 2,43 $ |
| present-perfect-temel | 1 | 7 | — | Opus / Opus (limit hatası) | 14,50 + 3,94 $ |
| present-perfect-ileri | 2 | 10 → 20 | EK-3, EK-5b, EK-5c, KS-10, ST-1, YV-6 (6) | Opus / limit hatası | 17,54 $ |
| present-perfect-cont-temel | 1 | 6 | — | Opus / limit hatası | 15,79 $ |
| present-perfect-cont-ileri | 1 | 13 | — | Opus / limit hatası | 14,79 $ |
| simple-past-temel | 1 | 6 | — | Opus (DUZ3-0210T) / çıktı yok | 25,36 $ |

Toplam: DUZ3 10 json'lu oturum 172,34 $ (ortalama 17,23 $, 79–239 tur). DUZ3B Sonnet 2 oturum 3,27 $ (ortalama 1,64 $).
Not: 02-03 ve simple-past-temel için DUZ3B, 0201T, 0202I, 0210T için json henüz yok; sunucuda 9 `claude -p` süreci çalışıyor.

## 2. Hükümler arası geçiş — düzeltme gerçekten araya girdi mi?

Zaman çizelgesi (`ls -l` + DJ dosya adı SS:DD): DUZ3 01:35–02:34, DJ'ler 00:19–02:30, DUZ3B 12:13–12:43, DJ'ler 12:04–12:37.

| Çift | Araya düzeltme girdi mi | Sonuç |
|---|---|---|
| present-continuous 02:09 → 12:09 | Hayır (DUZ3 02:01 bitti, DUZ3B yok) | Aynı durum yeniden yargılandı: 7 → 9 |
| present-continuous-ileri 01:42 → 12:05 | Hayır | 11 → 15 (jüri `kanit/` dosyalarıyla DK-3, ST-2, EK-12, B3, B4 ekledi) |
| simple-present-ileri 01:52 → 12:10 | Hayır (DUZ3B 12:43'te yazdı) | 9 → 11; EK-1 hükümde "YeDeTe" okunuyor, T2-1 raporu 12:43 tarihli |
| present-perfect-ileri 02:30 → 12:10 | Hayır (DUZ3B limitte öldü) | 10 → 20 (jüri yüzey listesini genişletti: kapak, kart, `canAlici`, açıklama) |
| **02-04-ydt-temel 00:19 → 01:48** | **Evet (Opus DUZ3)** | **5 → 1 kimlik: DK-2, EK-5b, EK-5c, KS-4 kapandı; HV-24 kaldı (mp4)** |
| **present-continuous-ileri 12:05 → 12:37** | **Evet (Sonnet DUZ3B)** | **15 → 15: kapanan 3 (EK-5c ilk hâli, KS-6, B4); yeni 3 (hepsi "düşük")** |

Sonuç: dört çiftte hayır sayısı **arttı** ve araya düzeltme girmedi. Gerçek düzeltme içeren yalnız 2 çift var; ikisinde de kapsamdaki maddeler kapandı.
İstemdeki "15 maddeden 1" gözlemi: Sonnet kapsamdaki 3 maddeyi kapattı, jüri 3 düşük bulguyu yeni yazdı, 12 madde istem gereği hiç denenmedi.

## 3. Kalıcı maddelerin sınıfı

Sayım: son hükümde o kimliği taşıyan ders sayısı (11 dersten).

| Sınıf | Maddeler (ders sayısı) | Kanıt |
|---|---|---|
| (a) Render gerektiriyor | HV-24 mp4 (02-04, present-perfect-temel); EK-12 bayat `zamanlar.json` (3); bayat `k/` kareleri KR-1/B3 (3) | 02-04 DJ 12:12: "`cikti.mp4` 15.11 00:09 ... `YDT BASIC`"; present-continuous-ileri DUZ3-RAPOR T2: "`zamanlar.json` (kare 50; son render eski sözle). Render yasak" |
| (b) Düzeltilebilir, düzeltici atladı | DK-2 altyazı/kart satırı ≤ 24 kr (9); EK-1 (1); EK-6 "bugünlerde" (2) | DK-2 ölçütü açık (`juri-olcutleri.md` satır 62 "satır ≤ 24 karakter"). Sonnet: "Jüri 'altyazı sınırını Ş belirlesin' dedi; ölçüt kararı bekliyor". Opus 02-04 aynı maddeyi 24 kr'ye indirdi. EK-6: present-continuous DUZ3-RAPOR satır 158 "ses değişmesin diye dokunulmadı" |
| (c) Yanlış pozitif / ölçüt belirsiz ya da çelişkili | ST-1 kırmızı ✗ (8); ST-2 rozet 26 px < 30 (8); KS-4 2–4 / 2–5 sözcük (2); KS-2 %55 sınırı (4) | ST-1 ölçütü: "kırmızı ✗ ikinci vurgu sayılır" ile "kasıtlı yanlış işareti mürekkep ya da soluk tondadır" aynı satırda; jüri her hükümde "Ş istisna yazsın". ST-2: ölçüt "yazı tabanı 30" ama "rozet için 26 bilgi satırı" der; DJ 12:05 "Ş kararı: rozet için kısa-kuralı". 02-04 DUZ3: "KS-4'te standart 2–4, istem 2–5; karar senin" |
| (d) Kaynak / veri sorunu | KS-10 karakter cinsiyeti (4); B2 kapakta beyaz üçgen (1); DK-1 dikey karaoke (4) | KS-10: `KAYNAK.json` "genç erkek, iri kıvırcık saç" ↔ `kadro.ogrenci` `cinsiyet kadin`; istem "yeni görsel yasak". B2: `karakter.png` alfa kusuru. DK-1: `kunye.js:188–202 altyaziCiz` tek renk `R.murekkep`; DUZ3B-0201I "Altyazı oynatıcı mekanizması; motor işi". 53 `kunye.js` kopyası, 53 ayrı md5 |
| (e) Ölçüm aracı eksik | EK-3 koyu-tema matrisi (10); DK-3 `hyperframes check` (6); EK-12 zaman kapısı (3) | EK-3 hükmü: "KANIT.md EK-7 `olculemedi`; 11 hücre karesiz". DK-3: "Paper.js sahneleri (02–05) kapsam dışı". EK-12: "Ölçülemeyen 5 sahne (zamanlar.json biçimi tanınmadı)". KNT oturumları (kanıt üretimi): 5 kayıt, hepsi `0 tur, "You've hit your weekly limit · resets Nov 21, 2am"` (02:34–02:35) |

Ek notlar:
- DK-3 `#ku-bolum` kontrastı (1,93:1), ST-2 künye 20/24 px, DK-1 `altyaziCiz` aynı ortak künye şablonundan geliyor (`kunye.js:52`: `bolumYazi: 24, ajandaYazi: 20`). Her paket kendi kopyasını taşıdığı için 53 yerde ayrı düzeltme gerekir. Düzeltici `K/ortak/` altına dokunamaz.
- EK-5b/EK-5c (8 + 4 ders) gerçek içerik hatasıdır; düzeltici bunları kapatıyor (02-04: 5 → 1, pc-ileri `-ing almaz` → `durum anlamında`). Jüri yeni yüzey buldukça yeni satır çıkıyor (present-perfect-ileri 10 → 20 satır: `canAlici`, `youtube-aciklama.md`, kapak).
- Jüri modeli düzeltici modelle aynı (pc-ileri hükmü satır 2: "ortak kör nokta riski"). Bu kör noktayı ölçmedim.

## 4. Model karşılaştırması

| Ölçü | Opus 5.5 (DUZ3, 10 oturum) | Sonnet 5.5 (DUZ3B, 2 oturum) |
|---|---|---|
| Ortalama maliyet | 17,23 $ | 1,64 $ |
| Ortalama tur | 175 | 55 |
| Kapsam | cümle + ses + sahne + kapak + yayın verisi (geniş) | tek ekran metni + 2 küçük dosya (dar) |
| Kapanan madde | 02-04: 4 / 5 kimlik | pc-ileri: 3 / 15 satır; kapsamdaki 3 / 3 |
| Maliyet / kapanan madde | ≈ 4,7 $ (02-04) | ≈ 0,28 $ (pc-ileri) |

Kanıt düzeyi: **n = 2 çift, farklı dersler, farklı kapsam**. Model üstünlüğü söylenemez. Söylenebilen: kapsam dar olunca Sonnet ucuz ve temiz kapatıyor; Opus işi geniş yaptığı için pahalı.
Çıkış durumu: 4 DUZ3B oturumu (0206I, 0206T, 0209I, 0209T) ve 5 KNT haftalık limit hatasıyla öldü (modelUsage boş; yalnız 0206T 43 tur sonra, 3,94 $). Limit Opus'a mı özel, doğrulanmadı: Sonnet oturumları aynı saatlerde çalıştı (çıkarım).

## 5. Öneriler

1. **Ölçüt kararlarını kapat (c).** `juri-olcutleri.md` satır 62 (DK-2 altyazı da 24 mü), 65 (ST-1 kasıtlı ✗/çizgi tonu), 66 (ST-2 rozet ≥ 26), 89 (KS-4), 95 (KS-10 hangisi doğru). Her satıra "Karar: …, 16.11" yaz; jüri "Ş bekliyor" yazamaz. Etki: ST-1 (8), ST-2 (8), KS-4/KS-2 (6), KS-10 (4) = yaklaşık 26 ders-madde belirsizlikten çıkar.
2. **DUZ3B istemine zorunlu durum tablosu.** `uretim-hatti/istemler/DUZ3B-*` şablonuna: her `hayır` kimliği için satır `kimlik | kapandı / kapanmadı | sınıf a–e | sahip | kanıt`. "Ölçüt kararı bekliyor" yalnız öneri 1'de karar yoksa geçerli sayılır. Etki: (b) sınıfı DK-2 (9), EK-6 (2), EK-1 görünür ve kapanır.
3. **Tek "kare + matris" betiği, model yok.** `araclar/kare-denetim.mjs` / `qa-yerel.sh` sahne × yön × tema matrisini kendisi çeksin ve `kanit/KANIT.md` EK-3/EK-7/EK-8'i yazsın (kare çekimi serbest). Betik KNT oturumunun yerini alır; limit riski 0. Etki: EK-3 (10 ders), KR-1/B3 (3).
4. **Künye şablonunu bir kez düzelt, paketlere yay (d, e).** `kunye.js` ortak çekirdeğini ayrı dosya yap (`ders`/`seviye` sabitleri paket kopyasında kalsın): `ajandaYazi`/`bolumYazi` ≥ 30, `#ku-bolum` rengi ≥ 3:1, `altyaziCiz` sözcük başına dolum. Etki: DK-1 (4), DK-3 (künye kaynaklı, en az 4), ST-2 (8).
5. **Render sonrası tek tur (a).** mp4, `k/` kareleri, `zamanlar.json` yan ürünleri, `kapak` PNG insanın açık sözüyle tek toplu render edilir; ardından jüri. Düzeltici render beklemez, "render sonrası" etiketi koyar. Etki: HV-24 (2), EK-12 (3), KR-1/B3 (3).
6. **Jüri hükmüne kalıcılık tablosu.** Hükmün sonuna: `kimlik | önceki hükümde? | arada düzeltme turu var mı | sınıf`. Araya tur girmediyse hükmün başına "aynı durum yeniden yargılandı" yaz ve hayır sayısını gerileme sayma. Etki: §2'deki 4 çiftte sahte "15 → 15" okuması biter; gereksiz jüri koşusu azalır.
7. **Jüri satırına hazır düzeltme cümlesi.** EK-5b/EK-5c hükmünde karşı örnek + önerilen kapsam sözcüğü (`çoğu zaman`, `durum anlamında`) zorunlu; düzeltici uygular ya da karşı gerekçe yazar. Kanıt: present-perfect-ileri c1 ("Ago varsa, fiil Simple Past.") iki hükümde mutlak bulundu; pc-ileri `-ing almaz` kapsam sözcüğü eklenince kapandı. Etki: EK-5b (8), EK-5c (4).
8. **Düzeltmeyi Sonnet'e, geniş kapsamlı DUZ3'ü bölerek ver; kota önce ölç.** DUZ3'ün 10 oturumu 172 $ tuttu; kapsamı 3 işe böl (cümle+ses / sahne+kare / kapak+yayın). 600 derste 10 $ yerine ≈ 2 $ hedefi. 3 derste A/B koş (Sonnet ↔ Opus, aynı jüri), sonra karar ver. Limit hatasıyla ölen DUZ3B/KNT oturumlarını `SendMessage` ile sürdür, sıfırdan doğurma.

## 6. Kanıt düzeyi notu

| Ölçüldü (sunucu dosyası) | Yorum |
|---|---|
| Hükümlerdeki `hayır` kimlikleri (grep, 18 hüküm) | Kimlik sayımı doğru; "satır" sayımı cümle satırlarını da içerir, kaba |
| DUZ3/DUZ3B/KNT `.json` maliyet, tur, hata | Doğru; 6 json boş (çalışıyor ya da yazılmadı), maliyet bilinmiyor |
| DUZ3 / DUZ3B rapor mtime ↔ DJ dosya adı saati | Sıra çıkarımı; jüri hangi dosya sürümünü okudu, kontrol edilmedi |
| Sınıf ataması (a–e) | Yorum; her sınıf için en az 1 alıntı var, ders başına tek tek doğrulanmadı |
| Model karşılaştırması | n = 2, kapsam farklı; yön göstergesi, sonuç değil |
| Limitin Opus'a özel olduğu | Çıkarım, doğrulanmadı |
| `ortak/kunye.js` şablon kaynağı | 53 dosya, 53 ayrı md5; ortak çekirdek var mı, açılıp farkı alınmadı |
