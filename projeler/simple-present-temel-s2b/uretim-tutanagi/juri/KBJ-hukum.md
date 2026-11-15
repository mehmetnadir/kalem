# KBJ-hukum — simple-present-temel-s2b (A/B kol b, değişken `kapanis`) çıktı jürisi · 15.11.2026 23:10

**Jüri modeli:** Claude Sonnet 5.5 (`claude-sonnet-5-5`). **Üretici:** Claude Opus 5.5 (`claude-opus-5-5`, KBC-RAPOR). İki model farklı; aile aynı (Claude 5). Ortak kör nokta riski (juri-olcutleri §1e) tam kapanmadı.
**Zaman (§1b):** paketin son içerik değişikliği 23:00:15 (`surumler.json`); bu jüri 23:08–23:10. Jüri içerikten yeni.
**Kanıt:** senaryo, `sentez.wav.rapor.json` (Whisper), `sureler.json`, `zaman.json`, `altyazi.json`, `aciklama*.md`, `surumler.json`, `diff -rq` (kendi koşum, 70 satır), kol b kareleri (01: 0 / 1,5 / 2,95 · 02: 3,05 / 7,45 / 11,8 · 03: 11,88 / 15,5 / 17,7 / 19,05 · 04: 19,08 / 20,1 / 21,4 / 25,7; koyu: 01 1,5 · 02 7,45 · 03 18,3 · 04 24,2), kol a türevleri (kapak a/b/c, hikâye a/b). Whisper'ı yeniden koşmadım: üretici raporu kullandım (ses kapısı çıktısı).

## Özet

| Küme | Evet | Hayır | Kanıt yok |
|---|---|---|---|
| §2a HV-1…23 | 22 | 1 (HV-13) | 0 |
| §2d AB-1…7 | 3 (AB-1, 2, 6) | 1 (AB-3) | 3 (AB-4, 5, 7) |
| Ek bulgu (§1c, dil + paket) | — | 4 | — |

**Sonuç: KALDI.** Kalan: HV-13, AB-3, ek bulgu E1 (mutlak denklik), E2 (kol a'ya mutlak yol). Teslim kapısı (D-0338) açılmaz.

## §2a — Kısa video

| Kimlik | Hüküm | Kanıt | Not |
|---|---|---|---|
| HV-1 | evet | kare 0,0 / 7,45 / 17,7 / 25,7: logo + `@ydspublishing` y ≈ 295–340, x = 60 | giriş/çıkış animasyonu yok |
| HV-2 | evet | `senaryo.json` cümle 4 `ogrenci` (…9gjY); rapor 4·1 ve 4·2 Whisper 1,00 | |
| HV-3 | evet | senaryo cümle 4 parça 2; `altyazi.json`; kare 21,4 | Whisper `YEDESE Publishing` duyar, ses metni `YeDeSe` (benzerlik 1,00) |
| HV-4 | evet | tarama (`tam ders`): senaryo, altyazı, METIN, açıklama ×3, sahne HTML/JS/PY, `ortak/*.js`, `surumler.json` boş | yalnız `SPEC.md`/`RAPOR.md` yasak cümlesini anar; çıktı değil |
| HV-5 | evet | tarama (`dakika`, `\bdk\b`) aynı yüzeylerde boş | |
| HV-6 | evet | sahne 3 ayrı (11,87–19,07); açıklama ilk satırı "Sınav günü bakmak için kaydet…" | teşvik video-açıklama arasında uyuşmuyor, bkz. E3 |
| HV-7 | evet | kare 20,1 / 21,4 / 25,7: kart x 60–960, y 622–1125 (≈ 900×503) | `ana-kapak.png` sha256 `e2bbf46da46b` = `simple-present-temel/kapak.png`; koyu `df33df751ea0` eşit |
| HV-8 | evet | sınavda çıkar ✓ · tuzak ✓ · tek cümle ✓ · Türkçe köprü ✓ · izlemeden anlaşılır ✓ · yeniden bakılır ✓ | 6/6 biçim olarak; içerik doğruluğu E1'de kaldı |
| HV-9 | evet | `find … -name '*.mp4'` boş | |
| HV-10 | evet | altyazı y 1420–1520; üst kutu y ≥ 280; çakışma kapısı çıkış 0 | |
| HV-11 | evet | 4 sahne; 25,73 sn (`zaman.json`) | hedef 22–26 içinde |
| HV-12 | evet | `baslar.json` ilk söz 1,00; sahne 01 = 3,0 sn | sınırda: ≤ 1 sn eşit |
| **HV-13** | **hayır** | kare 17,7 / 19,05 / koyu 18,3: yer imi simgesi yok (4 köşe çerçeve), "Kaydet" yazısı yok ("Ekran görüntüsü al") | Değişkenin kendisi; ama §3 tablosu "yer imi SVG + Kaydet" ister, §4 listesi `Ekran görüntüsü al…` kalıbına izin verir: standart kendi içinde çelişiyor. Kart 17,7 ↔ 19,05 piksel aynı (maks fark 15 ≤ 16); 2 sn sabitliği kare ölçümüyle yalnız 1,35 sn doğrulandı, kalanı `zamanlar.json` (3,29 sn) beyanı |
| HV-14 | evet | kare 21,4: giriş Fredoka 700 (HTML `font-weight:700`), kart y 622–1125, `@ydspublishing · YouTube` 25,7 | |
| HV-15 | evet | "Konu burada bitmiyor." listede (§4); derste tek kez | |
| HV-16 | evet | "Ekran görüntüsü al, sınav günü bak." listede (§4); tek kez | |
| HV-17 | evet | `ses-sozluk.json` `YDS → YeDeSe`; rapor 4·2 ses_metni `YeDeSe`, benzerlik 1,00 | |
| HV-18 | evet | `aciklama.md`/`-a`/`-b` ilk satır sabit; Reels bloklarında bağ yok | |
| HV-19 | evet | `utm_campaign=ING-YDT-GR-02-02-T` SP paketlerinde tek biçim (s1 24, s1b 15, s2/s2b 39, s3 24); `utm_content` `s2b-a` / `s2b-b` | s3b'de açıklama henüz yok (ölçülemedi). Başka ders: `02-04-ydt-temel-s2/aciklama*.md` küçük harf `ing-ydt-gr-02-04-t` ×4 → o paket için hayır |
| HV-20 | evet | kol b'de yok (AB §4: grup türevi kol a'da). Kol a: kapak a/b/c altyazısız, kanal katmanı var, a ve c karakterli; hikâye 2; açıklama 2 | kapak-c karakteri erkek (afro) ↔ `kadro.ogrenci` kadın: KS-10 grup işidir, bu jürinin kapsamı dışı, E4'e yazıldı |
| HV-21 | evet | hikâye-a, hikâye-b: kanal katmanı + özet + Kaydet; y 1150–1380 boş | koyu hikâye karesine bakılmadı |
| HV-22 | evet | `kapi.log`: 4 sahne "çakışma yok", çıkış 0 | kol b'de statik türev yok |
| HV-23 | evet | çağrı parçaları 1,00 / 1,00 | en düşük 0,92 (2·3, kol a ile aynı wav, `7'de`) eşik üstü |

## §2d — A/B kolu

| Kimlik | Hüküm | Kanıt | Not |
|---|---|---|---|
| AB-1 | evet | kol a `s2` `varyant` `kol:a, degisken:kapanis, deger:kaydet`; kol b `s2b`; grupta 2 kol; s2 → `kapanis` | |
| AB-2 | evet | `diff -rq` 70 satır; sınıf: aciklama 3 · grup türevi 7 · `ortak/anlatim` 12 · sahne 03/04 30 (kod 7 + `k/` 23) · `surumler` 1 · tutanak 17. Sahne 01, 02 ve `ortak/` kalanı fark vermedi. Beklenmeyen 0 | üreticinin sınıflaması doğru; 3·1 ve 4·2 yeniden sentezi AB-3'te |
| **AB-3** | **hayır** | `cumle-3.wav` `9142f8fe5573` → `3fa5c40623a7`, `cumle-4.wav` `b192db36b66b` → `4201e1dfc0f9`; parça 3·1 (kural özeti, metin aynı) ve 4·2 (çekirdek, metin aynı) yeniden sentez; 3·1 süresi 4,08 → 4,00 | `cumle-1/2.wav` aynı (değer sahnesi ✓), kadro aynı, kanal katmanı kareleri aynı. Çekirdek cümle ve kural özetinin sesi sha256 düzeyinde aynı değil; AB §2 "sha256" ister |
| AB-4 | kanıt yok | yayın takvimi pakette yok | Şef maddesi |
| AB-5 | kanıt yok | API sorgusu koşmadı (jeton yok); pakette `mp4` yok, `surumler.json`'da `mp4` alanı yok | Şef/API |
| AB-6 | evet | `surumler.json` kol b: `varyant{grup:s2,kol:b,degisken:kapanis,deger:ekran-goruntusu}` (`[a-z0-9-]`); `utm_content` `s2b-a` / `s2b-b` | |
| AB-7 | kanıt yok | kazanan ilanı yok, ölçüm yok | Şef; yayın sonrası |

## Ek bulgu (§1c: kaynak ≠ doğru; paket bağımsızlığı)

| # | Madde | Hüküm | Kanıt | Not |
|---|---|---|---|---|
| E1 | EK-5b + EK-5c: "Usually, always, every day: Simple Present." istisnasız denklik | **hayır** | senaryo cümle 3 parça 1; kare 17,7 / 19,05 kartı; kol a kapak-c "TEK İŞARET", kapak-b "ALWAYS VARSA HANGİ ZAMAN?", hikâye-a aynı kart | `always` ve `usually` Present Continuous ve geçmişle de gelir ("He is always complaining.", "She always came late."). Açıklama "çoğunlukla" der, ses ve ekran demez. Juri-olcutleri §4 hata 5 ("always için istisnasız kural") yinelendi. Her iki kolda ve ana derste aynı |
| E2 | Kol b kol a'dan bağımsız mı (AB §4 "kopya, bağ yok") | **hayır** | `ortak/kunye.js` `KOK="/projeler/simple-present-temel-s2/ortak"`; `sahne-02.js`, `kalem-paper.js`, `sayfa.html` aynı yol | Kol a panelden kalkar ya da `ortak/` değişirse kol b bozulur; tek değişken kanıtını da o yol bozar. KBC açık nokta 4 doğrulandı |
| E3 | Video ↔ açıklama uyumu | not | sahne 03 "Ekran görüntüsü al"; açıklama ilk satırı "…kaydet" | Kol b'nin kaydetme ölçüsü aleyhine eğilir (KBC nokta 7); karar şefte |
| E4 | Küçük kusurlar | not | açıklama başlıkları `s2-aciklama-a/b`, "Eşleşen kapak: kapak-a.png" (kol b'de dosya yok); rozet `YDT · BASIC` (üst bant) ↔ `YDT · TEMEL` (kart); kapak-c karakteri erkek ↔ `kadro.ogrenci` kadın; `{UZUN_VIDEO_URL}` boş | Standart §9: rozet iki kolda birlikte düzelir |

Doğru bulunanlar: "Kardeşim genellikle okula otobüsle gider." (yazım, çeviri) ✓ · "Şu an" üstü çizili ✓ (cümle "Şu an değil" diyor) · "Her sabah yedide kalkarım" geniş zaman ✓ · `My brother usually goes…` ✓ · hikâye-b şıkları (`goes` doğru, `is going` yanlış) ✓. Emoji 0 (kol b kareleri, açıklama, senaryo).

## Kaldı maddeleri için düzeltme önerisi

| Kimlik | Düzeltme (tek cümle) |
|---|---|
| HV-13 | Standartta "kaydet" sahnesi için `Ekran görüntüsü al` kalıbına yer imi yerine çerçeve simgesini yazın (ya da §3'ü kalıba göre genişletin); kodda değişiklik gerekmez. |
| AB-3 | Çekirdek cümle (4·2) ve kural özeti (3·1) parça wav'larını kol a'dan kopyalayıp `kur.py`'de sabitleyin; olmuyorsa AB §2'yi "sha256 yerine metin eşit + Whisper ≥ 0,9 + süre farkı ≤ 0,1 sn" diye yazın. |
| E1 | Cümleyi "Usually, always, every day: genellikle Simple Present." yapın; ses, kart, kapak-c ("TEK İŞARET"), kapak-b ve hikâye-a ikisinde birlikte değişir. |
| E2 | `KOK` ve sahne 02 yollarını kol b yoluna çevirin; tek değişken farkı için `ortak/` bayt eşitliğini yeniden denetleyin. |

## Ana derse geri besleme

- Ana dersin `canAlici` satırı "Türkçedeki geniş zaman eki = İngilizcedeki s: gider = goes" yanlış denklik taşır (juri-olcutleri §4 hata 4). Kapakta "GİDER = GOES" kelime çevirisi olarak kalır; `canAlici` metnini düzeltin.
- E1 ana derste de geçerlidir: "usually, always, every day = tekrar eden iş sinyali" mutlak okunmasın; "genellikle" ekleyin.
- Rozet `YDT · BASIC` → `YDT · TEMEL` (standart §9 açık işi).
