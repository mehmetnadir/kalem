# simple-present-temel-s1 · Shorts senaryo taslağı — huni v2 (9:16, hedef 22–26 sn)

Durum: TASLAK (istem P0202-S1-A, 15.11.2026). Ses sentezi, sahne kodu ve render YOK.
Paketteki eski kısa (3 sahne, eski kanal kapanışı, 22,77 sn) yerinde duruyor; bu belge onun yerine geçecek v2 metnidir.
Bağlayıcı standart: `dijital-anlatim/.claude/docs/huni-v2-standart.md` (4 sahne: kanca → değer → kaydet → çağrı).
Kaynak ders: `../../simple-present-temel/` (`ortak/anlatim/senaryo.json`, `sozcukler.json`, `surumler.json`, `BRIEF.md`).
Biçim emsali: `../../02-04-ydt-temel-s2/uretim-tutanagi/` (yalnız dosya biçimi). Eski S1 metni: `../ortak/anlatim/senaryo.json`.
Ölçülmüş süre ikizleri: ana ders `sureler.json`, eski S1 `sureler.json`, `../../02-04-ydt-temel-s1/ortak/anlatim/sureler.json`.

## 1. Künye

| Alan | Değer |
|---|---|
| Kimlik | `02-02-ydt-temel-s1` (paket `simple-present-temel-s1`; eski `senaryo.json` → `meta.kimlik`) |
| Kod | `ING-YDT-GR-02-02-T-S1` (kalıp §7: yatay kod + `-S1`) |
| Konu | Simple Present · YDT · temel |
| Bilgi | gider = goes: he, she, it öznesinde fiile s gelir; I, you, we, they ile gelmez |
| Biçim | köprü cümle (standart §5): bir Türkçe söz (*gider*) → iki İngilizce karşılık (*go* / *goes*) |
| Ana ders kaynağı | cümle 4 (`My brother usually goes to school by bus.`) ve cümle 7 (üçüncü tekil kişi kuralı) |
| Can alıcı | `canAlici[0]` "gider = goes" + `canAlici[3]` "he, she, it fiile s alır; I, you, we, they almaz" (ana ders `surumler.json`) |
| Ses | öğretmen `gsJ9nrlXYbPztJxC4fwc` (ana ders `sesler.ogretmen`) · öğrenci `oPC5I9GKjMReiaM29gjY` (`kadro.ogrenci`: kadın, genç) |
| Figür | sahnede konuşan figür yok; değer sahnesinde kardeş figürü (kalem çizimi). Ana derste `kadro.ogretmen` yok (yalnız `sesler.ogretmen`) |
| Format | dikey 1080×1920, 30 fps, tema açık (K19); mp4 yok, sayfada önizleme (standart §1 kural 9) |
| Kanal katmanı | `ydspublishing` yazı logosu (≈ 48 px) + `@ydspublishing` (Lexend 700, 42 px); y 280–350, x 60; 0. kareden son kareye, animasyonsuz |
| Künye | y 360–450: `Simple Present` + rozet `YDT · BASIC` (standart §2) |
| Yasak sözler | standart §1 kural 4 (eski kapanış sözü) ve kural 5 (süre sözü) — seste, ekranda, altyazıda yok |

## 2. Senaryo

**TR** / **EN** = ses parçasının dili. Ses metninde ve ekranda rakam yok. Zamanlar tahmindir (§5); gerçek çapa sentezden sonra
`ortak/anlatim/sozcukler.json`'dan okunur.
İşaret: **[YENİ]** = ana derste yok, jüri bakacak · **[ESKİ S1]** = eski S1 parçasıyla birebir; ana derste yok, jüri bakacak ·
**[ANA]** = ana derste aynı tümce var · **[KALIP]** = standart §4 sabit sözü; ana derste yok, jüri bakacak.

| Sahne | Konuşan | Ses metni (söylenen) | Ekran metni | Görsel fikir |
|---|---|---|---|---|
| 1 Kanca 0,00–4,35 | öğretmen | **TR** `Kardeşim gider: go mu, goes mu?` **[YENİ]** · ilk söz 1,00 | 0,00: kapak A tam (`kapak-taslak.md` §3; başlık `GO mu,` / `GOES mu?`) · altyazı sözcük zamanlı (`Kardeşim` 1,00 · `gider:` 1,64) · ≈ 2,45 (uçuş sonu): Caveat `Kardeşim gider:` (söylendikten sonra) · kart `go` (≈ 2,54 "go") · kart `goes` (≈ 3,42 "goes") · aralarında kalem `?` (≈ 3,90 "mu?") | İlk kare = kapak A: genç figür (`open-peeps/standing-2.svg`) + otobüs (`coco/bus.svg`); kalem hareketi yalnız başlıktaki `?` 0,3–0,8. Uçuş 1,90–2,45: başlık künyeye (`Simple Present`), figür ve otobüs küçülüp içerik bandının sağ üstüne. İki kart yan yana (x 60–960, Fredoka 700 ≥ 96): bir Türkçe söz, iki İngilizce aday |
| 2 Değer 4,35–15,78 | öğretmen | **EN** `My brother goes to school by bus.` **[ESKİ S1]** cümle 2 parça 1; ana ders cümle 4 parça 2'nin *usually*'siz biçimi | Kart: `My brother goes` / `to school by bus.` (Fredoka 700 ≥ 64, karaoke; `My` 4,90 · `goes` 5,54 · `bus.` 6,50) · kartın üstünde soluk Caveat `Kardeşim gider:` (ikincil renk; sahne 01'in son karesindeki konumdan başlar, sahne sonuna dek kalır; seslendirilmez, 1,00–1,64'te söylendi) **[JÜRİ K2]** | Kanca kartı `goes` cümledeki *goes*'a uçar (5,54) ve sarı alt çizgi alır. Kart `go` soluklaşır, sağ kenarda bekler (kaybolmaz). Otobüs kalemle çizilir 4,90–6,50 (ana ders sahne 04 otobüsü). Köprü çifti `Kardeşim gider` ↔ `My brother goes` değer ekranında birlikte görünür (EN büyük, TR soluk) |
| | | **EN** `He, she, it` + **TR** `ile fiile s gelir.` **[JÜRİ D1]** eski S1 cümle 2 parça 3'ün bölünmüş biçimi; kalıp 02-02-ydt-temel cümle 21 ve 52 (EN zamir öbeği + TR yüklem) | `My brother` altında Caveat `= he` ("He" çapası) · çipler `he` · `she` · `it` (EN parça sözcük çapaları) · `goes` → `go-es`, `es` sarı daire ("s" çapası) | `My brother` → `he` kalem oku: "kardeşim = he". Formül ana ders sahne 04 ile aynı (`he + go → go-es`); sarı belirteç en çok 2 (alt çizgi + daire) |
| | | **EN** `I, you, we, they` + **TR** `ile gelmez.` **[JÜRİ D1]** ana ders cümle 7 parça 3 tümcesinin bölünmüş biçimi | ikinci satır çipler `I` · `you` · `we` · `they` (EN parça sözcük çapaları) · soluk `go` kartı çiplerin yanına döner; `s` yerine kırmızı kalem çizgisi ("gelmez" çapası) | Son durum iki satır: `he · she · it → goes` / `I · you · we · they → go`. Kancanın iki kartı da yerini bulur: cevap "özneye bak". Kırmızı çizgi ana ders sahne 06 ile aynı (72,55–77,74) |
| 3 Kaydet 15,78–19,05 | öğretmen | **TR** `Sınavdan önce lazım olacak. Kaydet.` **[KALIP]** | 16,33 ("Sınavdan"): kural özeti kartı tek hareketle (≤ 0,45 sn): `He, she, it: s gelir;` / `I, you, we, they: s yok.` (Fredoka 700 ≥ 64; satır 21 · 24 karakter); 16,78'den sahne sonuna sabit (2,27 sn) · 18,45 ("Kaydet."): yer imi simgesi + `Kaydet` sarı hap kartın altında | Kart değer sahnesinde söyleneni yineler, yeni bilgi taşımaz (02-04-s1 emsali). Yer imi SVG yolu kalemle çizilir, emoji değil. Tek sarı öğe `Kaydet` hapı |
| 4 Çağrı 19,05–25,31 | **öğrenci** | **TR** `Gerisi bizde.` **TR** `Dersin tamamı YDS Publishing YouTube kanalında.` **[KALIP]** 02-04-ydt-temel-s1 cümle 4 ile birebir | 19,05: ana dersin kapağı 16:9 kart (`../simple-present-temel/kapak.png`; koyu temada `kapak-koyu.png`), 900×506, x 60–960, y 620–1126 · 19,60 ("Gerisi"): `Gerisi bizde.` Fredoka 700, kartın üstünde (y ≈ 470–590) · ≈ 22,07 ("YDS"): `@ydspublishing · YouTube` Lexend 700, kartın altında (y ≈ 1160–1240) · 24,31–25,31 durgun kuyruk | Kapak kartında `GİDER = GOES` ve karakter görünür (standart §1 kural 7). Konuşan figür yok: kapaktaki karakter erkek, öğrenci sesi kadın (K22). Ekranda yasak söz (standart §1 kural 4–5) yok |

Sahne sınırı = sonraki cümle başı − 0,55; son sahne = son söz + 1,0 sn (emsal). Ekran metni sesten önce gelmez. İstisna yalnız kapak A
başlığıdır (0. kare; kalıp §4–§5, S2 emsali). Kural özeti kartı ve kapak kartı daha önce söyleneni gösterir.
Altyazı bandı (y 1400–1550, en çok 2 satır) bütün söylenenleri sözcük zamanlı taşır; kapak ve hikâye PNG'lerinde altyazı yok.

Klasör eşlemesi (istem P0202-S1-C huni v2 temiz numara; gerçek sınırlar `zaman.json`): `01-hyperframes-kanca` 0,00–3,00 (K23 giriş ≤ 3 sn;
kart `go` 01'in son karesinde, `goes` 02'de, 02-04-s1 emsali) · `02-paperjs-deger` · `03-hyperframes-kaydet` · `04-hyperframes-cagri`.

## 3. Kaynak eşlemesi

| Parça | Ana derste | Eski S1 | Ses önbelleği |
|---|---|---|---|
| 1 `Kardeşim gider: go mu, goes mu?` | yok | yok (eski cümle 1 `Gider, İngilizcede goes olur: …`) | yok: yeni metin |
| 2 EN `My brother goes to school by bus.` | cümle 4 parça 2, *usually*'li | cümle 2 parça 1, birebir | yok: sonraki parça değişir |
| 2 EN `He, she, it` + TR `ile fiile s gelir.` (jüri D1) | yok; yakın: cümle 7 parça 1–3 | cümle 2 parça 3'ün bölünmüşü | yok: parça metni farklı |
| 2 EN `I, you, we, they` + TR `ile gelmez.` (jüri D1) | cümle 7 parça 3 içinde (`Fiile s gelir. I, you, we, they ile gelmez.`) | yok | yok: parça metni farklı |
| 3 `Sınavdan önce lazım olacak. Kaydet.` | yok (standart §4) | yok | yok: 02-04-s1'de aynı metnin önceki parçası var (`Bu, üç farktan yalnız biri.`) |
| 4 `Gerisi bizde.` + `Dersin tamamı …` | yok (standart §4) | yok | VAR (aday): 02-04-ydt-temel-s1 cümle 4 ile birebir, iki parça, aynı öğrenci sesi |

**Ana dersin bir cümlesiyle birebir aynı cümle yok.** Önbellek anahtarı aynı cümlenin önceki ve sonraki parçalarını da içerir
(`dijital-anlatim/araclar/iki-dilli/el.py` satır 88 ve 138–142: `[ses_metni, dil, onceki, sonraki, ses, model, tohum]`).
Cümle 4'ün iki parçası, komşuları, sesi ve metni 02-04-s1 ile aynıdır. Model ve tohum aynıysa ses srv21 önbelleğinden gelir.
02-04-s1 Whisper sonucu: `Gerisi bizde.` 1,00 · `Dersin tamamı YDS Publishing YouTube kanalında.` 1,00 (ses metni `YeDeSe Publishing`).

## 4. Ses metni notları

- Cümle 1 TR parçada *go* ve *goes* geçer. Emsal: ana ders cümle 4 TR parçası `Fiil goes.`; eski S1 cümle 1 `İngilizcede goes olur`.
  Sentezde iki sözcük kulakla dinlenir. Düz Türkçe okunursa (ör. "gö") cümle yeniden kurulur; tek sözcüklük EN parça açılmaz (13.11 KULAK).
- Cümle 2'de zamir listeleri EN parçadadır (`He, she, it` · `I, you, we, they`; jüri D1). Ölçülmüş risk: TR parçadaki `/aɪ/` v4'te
  Türkçe "A" okunur ve Whisper kapısı bunu 0,99 ile geçirir (`02-03-ydt-temel` rapor satır 364–366); `it` sözlükte yoktur (Türkçe
  sözcük). EN parça bu iki riski kaldırır; emsal 02-02-ydt-temel cümle 21 ve 52 (duyulan aynı, 1,00). Kulak kararı yine zorunlu.
- `s` harfi TR parçada tek başına geçer: ana ders ve eski S1 ile aynı ("fiile s gelir").
- EN parça tam cümledir (cümle 2 parça 1). TR parçada `-ing`, rakam ve kısaltma yok. "YDT" söylenmez.
- Hitap (sen/siz) yok. `Kaydet.` standart §4 kalıbının emir kipidir.
- `@ydspublishing` sesle okunmaz; yalnız ekranda. Marka söylenişi `ses-sozluk.json` kaydından gelir (02-04-s1 ile aynı).
- Maliyet (tahmin): yeni parçalar 170 karakter (cümle 1: 31 · cümle 2: 33 + 43 + 28 · cümle 3: 35). S2 oranıyla
  (257 karakter ≈ 1,26 TL) ≈ 0,83 TL. Cümle 4 önbellekten gelirse ücretsiz.

## 5. Süre (tahmin; gerçek süre sentez sonrası `zaman.json`)

Yöntem: her parça için aynı sesin ölçülmüş ikizi. Parça arası: EN'li geçişte 0,25 sn, TR → TR 0,15 sn (`el.py` satır 137).
Cümle arası 0,55 sn. İlk söz 1,00 (eski S1 `zaman.giris.ilkSoz`).

| Cümle / parça | Sözcük | Ölçülmüş ikiz | sn | Başlar | Biter |
|---|---|---|---|---|---|
| 1 `Kardeşim gider: go mu, goes mu?` | 6 | sözcük toplamı: `Kardeşim` 0,56 (eski S1) + `gider:` ≈ 0,60 (ana ders 0,48 · eski S1 sonda 0,85) + iki nokta 0,30 (ana ders `deriz:` 0,20 · eski S1 `Gider,` 0,40) + `go mu,` ≈ 0,55 + virgül 0,25 + `goes` 0,40 (eski S1) + `mu?` ≈ 0,45 + sözcük araları 0,24 | 3,35 | 1,00 | 4,35 |
| 2 EN `My brother goes …` | 7 | eski S1 cümle 2 parça 1 | 2,16 | 4,90 | 7,06 |
| 2 EN `He, she, it` + TR `ile fiile s gelir.` (jüri D1) | 7 | 02-02-ydt-temel `He, she, it` 1,44 + 0,25 + `ile se gelir.` 1,08 | 2,77 | 7,31 | 10,08 |
| 2 EN `I, you, we, they` + TR `ile gelmez.` (jüri D1) | 6 | 02-02-ydt-temel `I, you, we, they` 2,16 + 0,25 + ≈ 0,80 | 3,21 | 10,33 | 13,54 |

Jüri D1 bölünmesinden sonra değer cümlesi ≈ 2,2 sn kısalır (jüri ≈ 1,8); aşağıdaki sahne sınırları eski tahmindir, gerçek değerler
sentezden sonra `zaman.json` ve `S1-C-RAPOR.md`'de.
| 3 `Sınavdan önce lazım olacak. Kaydet.` | 5 | 02-04-s1 cümle 3 parça 2 | 2,72 | 16,33 | 19,05 |
| 4 `Gerisi bizde.` + `Dersin tamamı …` | 8 | 02-04-s1 cümle 4 (1,04 + 0,15 + 3,52) | 4,71 | 19,60 | 24,31 |
| kuyruk | | | 1,00 | 24,31 | 25,31 |

Toplam tahmin **25,31 sn** (hedef 22–26; 28 sınırına pay 2,69 sn).

Kötü durum: S2'de tahmin kısa çıktı (cümle 1: 1,44 → 1,84, %28; cümle 2: 13,03 → 14,02, %8). Aynı payı burada uygula: cümle 1 +%28
(+0,94) · cümle 2 son parça +%10 (+0,37; ikiz bir alt dilim) · metni birebir ikizli parçalar +%5 (+0,48) · cümle 4 önbellek, 0.
Kötü durum toplamı **≈ 27,1 sn**; 28 sn içinde kalır (pay ≈ 0,9 sn).

Standart §3 hedefiyle karşılaştırma:

| Sahne | Standart | Tahmin |
|---|---|---|
| 1 Kanca | 0–4 sn | 0,00–4,35 |
| 2 Değer | 4–15 sn | 4,35–15,78 |
| 3 Kaydet | 15–18 sn; kart ≥ 2 sn sabit | 15,78–19,05; kart 2,27 sn sabit |
| 4 Çağrı | 18–25 sn | 19,05–25,31 |

İlk 10 sn'de 3 hareket türü: kinetik başlık ve uçuş (1), kalem çizimi (otobüs, `= he` oku), karaoke (2).

**B planı (yalnız ölçülen toplam 28 sn'yi aşarsa; metin değişmez, jüri gerekmez):** 1) ilk söz 1,00 → 0,50 (−0,50 sn; kalıp §5
"ilk söz 0. sn" izin verir) · 2) kuyruk 1,00 → 0,44 (−0,56 sn). S2 emsali.
