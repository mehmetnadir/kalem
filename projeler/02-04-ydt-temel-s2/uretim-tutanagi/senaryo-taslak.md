# 02-04-ydt-temel-s2 · Shorts senaryo taslağı (9:16, hedef 24–28 sn)

Durum: TASLAK (istem S2-A, 15.11.2026). Ses sentezi, sahne kodu ve render YOK.
Düzeltme (istem S2-C, 15.11): S2-B jüri maddeleri işlendi, madde → yapılan → kanıt `S2-duzeltme.md`. Cümle 2'de *today* parçası
kart 2'nin hemen ardına alındı ve yumuşatıldı (`geçebilir`); cümle 2 `Konuşma anı: şimdiki zaman.` ile biter. Ölçülen çapalar: `../BRIEF-S2.md`.
Kaynak ders: `../../02-04-ydt-temel/` (senaryo jüriden GEÇTİ, D-0204). Biçim emsali: `../../02-04-ydt-temel-s1/` (S1-B jürisi + S1-C düzeltmesi).
Kalıp: `dijital-anlatim/.claude/docs/dikey-senaryo-kalibi.md` §1, §4, §5; `huni-plan-1211.md` §4–§7.

## 1. Künye

| Alan | Değer |
|---|---|
| Kimlik | `02-04-ydt-temel-s2` (huni: ders başına 3 kısa; S2 = dersin 1. farkı) |
| Kod | `ING-YDT-GR-02-04-T-S2` (kalıp §7: yatay kod + `-S2`) |
| Konu | Simple Present ve Present Continuous: kullanım farkları · YDT · temel |
| Fark | genel durum ↔ konuşma anı; *today* iki zamanda da geçebilir (S2-C: jüri dil 2, yumuşatıldı) |
| Ana ders kaynağı | cümle 3 (Örnek 1, *wear*) ve cümle 9 (karşıt çift, *today*); sahne `03-paperjs-ornek1` ve `08-canvas-karsit1` |
| Can alıcı | `canAlici[0]` ilk sorusu "genel mi, şu an mı?" + `canAlici[3]` "today iki zamanda da geçer; farkı anlam yapar" (ana ders `surumler.json`); seste yumuşak biçimi `geçebilir` (S2-C) |
| Format | dikey 1080×1920, 30 fps, tema açık (K19) |
| Ses | öğretmen Atakan `gsJ9nrlXYbPztJxC4fwc` (ana ders `senaryo.json` → `sesler.ogretmen`), eleven_v4 |
| Figür | öğretmen, erkek (K22: figür sesle eşleşir); `kadro.ogretmen` = S1 kaydı (ShirtPantsWB / Smile / Short) |
| Soru anı | yok. Öğrenci sesi yok. |
| Künye | S1 ile aynı: `ortak/kunye.js` dikey v2 (ders adı 2 satır, rozet `YDT · BASIC`); renk açık tema `zemin #f7f3ea`, `murekkep #1b2440`, `vurguDolgu #ffe066`, `pilMetin #1b2440` (S1 `ortak/kunye.js` satır 11–12, kullanım 154–155) |
| Süre iddiası | ana ders `cikti.mp4` ffprobe 265,676 sn (15.11, bu istem) → sözle "dört buçuk dakika" (S1 ile aynı) |
| Kapanış kimliği | `@ydspublishing` (karar A 05.11). "kanal" sözü yok, QR yok. |

## 2. Senaryo

Konuşan her satırda öğretmen. **TR** / **EN** = ses parçasının dili. Ses metninde rakam yok.
Sözcük zamanları tahmindir (ana ders ve S1'in ölçülmüş parça ikizleri, §5). Gerçek çapa sentezden sonra `ortak/anlatim/sozcukler.json`'dan okunur.
İşaret: **[YENİ]** = ana derste yok, jüri bakacak · **[ANA]** = ana derste aynı tümce var · **[S1]** = S1 cümle 3 ile birebir.

| Sahne | Cümle | Konuşan | Ses metni (söylenen) | Ekran metni | Görsel fikir |
|---|---|---|---|---|---|
| 01 kapak (HyperFrames) 0,00–2,44 | 1 | öğretmen | **TR** Genel mi, şu an mı? **[ANA]** cümle 18'deki soru · ilk söz 1,00 | Kapak sürümü (A, B ya da C; `kapak-taslak.md`) 0. karede tam. Soru satırı yalnız altyazı bandında, sözcük zamanlı: `Genel mi,` (1,00) · `şu an mı?` (1,88) | İlk kare = kapak. Kalem hareketi yalnız kapağın tek vurgusunda 0,3–0,8 sn. Son 0,6 sn (≈ 1,84–2,44) uçuş: başlık üst bant ders adına, figür solar; soru satırı içerik bandının üstüne `Genel mi, şu an mı?` (Caveat) olarak kalemle yazılır ve sahne 02 boyunca soru başlığı olarak durur. |
| 02 örnek (Paper.js) 2,44–15,82 | 2 | öğretmen | **EN** She wears her coat in the winter. **[ANA]** | Kart 1: `She wears her coat` / `in the winter.` (Fredoka 64, karaoke; She 2,99 · wears 3,23 · coat 3,79 · winter 4,55) | Kart 1 içerik bandının üst yarısında. `coat` çapasında mont kalemle (ana ders `sahne-03.js` MONT dizisi). `in the winter` çapasında `odak` (sarı altçizgi). |
| | | | **TR** Genel durum: geniş zaman. **[ANA]** cümle 3'teki tümce | `GENERAL` (Caveat, 5,56 "Genel") · `Simple Present` (ince yazı, 6,60 "geniş") | Kart 1 altında `zaman_cizgisi`: uzun çizgi üstünde tekrar eden kısa kış bantları (küçük kar tanesi), now noktası bantların dışında → "her kış böyle" görseli. **[YENİ görsel]** ana ders sahne 03'te bu çizgi yok. |
| | | | **EN** She is wearing her pink T-shirt today. **[ANA]** | Kart 2: `She is wearing her` / `pink T-shirt today.` (karaoke; She 7,65 · is 7,87 · wearing 8,01 · T-shirt 8,87 · today 9,37) | Kart 2 kart 1'in altında, tek sütun. `T-shirt` çapasında pembe tişört kalemle (ana ders `sahne-03.js` TISORT dizisi). `today` çapasında `odak`. |
| | | | **TR** Today iki zamanda da geçebilir; farkı anlam yapar. **[YENİ]** `canAlici[3]`'ün yumuşak biçimi (S2-C, jüri dil 2 (c)); ana ders cümle 10'a yakın ("Today iki cümlede de var. Farkı anlam yapıyor") | ≈ 10,6 "Today": kart 2'deki `today` sarı daire (`isaret`) · ≈ 13,1 "anlam": `MEANING` (sarı hap) kart 2'nin sağında | `Simple Present` etiketine ok YOK, kart 1'e bağ YOK (S2-C, jüri kaynak 3 (b)): ekran *today* için geniş zaman iddiası taşımaz. "anlam" çapasında üst soru satırı `Genel mi, şu an mı?` mürekkep altçizgi alır: karar aracı budur. Bu anda tek sarı `MEANING`; `today` dairesi mürekkebe döner. |
| | | | **TR** Konuşma anı: şimdiki zaman. **[YENİ]** cümle 2 bununla biter (S2-C, jüri kaynak 2): cümle 3'teki "Bu" genel ↔ konuşma anı çiftine bağlanır | `RIGHT NOW` (Caveat, ≈ 14,1 "Konuşma") · `Present Continuous` (ince yazı, ≈ 15,2 "şimdiki") | `today` dairesinden `RIGHT NOW` etiketine tek ince kalem oku (yalnız Present Continuous'a bağ). Kart 2 altında `zaman_cizgisi`: today gün bandı, now noktası bandın içinde nabız (ana ders sahne 08 görseli). |
| 03 tam ders çağrısı (HyperFrames) 15,82–26,39 | 3 | öğretmen | **TR** Bu, üç farktan yalnız biri. **TR** Tam ders: Simple Present ve Present Continuous. **TR** Üç farkın hepsi dört buçuk dakikada. **[S1]** | S1 sahne 03 ile aynı sıra: `üç farktan biri` (üç 16,85) · `Tam ders:` (18,60) · bant `Simple Present` / `vs Present Continuous` (`vs` = "ve" çapası 20,60) · `üç farkın hepsi` (22,83) · saat + `dört buçuk dakikada` (dört 24,19) · `@ydspublishing` sarı hap (dolgu `#ffe066`, yazı `#1b2440`) son sözle (dakikada 24,67) | S1 yerleşimi aynen (Lexend / Caveat / Fredoka). Son 1,0 sn durgun kuyruk. Son karede mont ve tişört ikonu bandın iki yanında küçük → kapak karesine döngü (kalıp §1 kural 5). |

Sahne sınırı = sonraki cümle başı − 0,55; son sahne = son söz + 1,0 sn (S1 kuralı). Ekran metni sesten önce gelmez; kapak başlığı istisnadır
(kalıp §4–§5: başlık 0. karede tam; S1 emsali). Hikâye karesi zaman çizelgesi dışında (`hikaye-taslak.md`).

## 3. Kaynak eşlemesi

| Parça | Ana derste | Ses önbelleği |
|---|---|---|
| Cümle 1 `Genel mi, şu an mı?` | cümle 18 içinde aynı tümce ("… Genel mi, şu an mı? Kalıcı mı, …") | yok: komşu parça değişir |
| `She wears her coat in the winter.` | cümle 3 parça 2 | yok: komşu parça değişir |
| `Genel durum: geniş zaman.` | cümle 3 parça 3 içinde aynı tümce | yok |
| `She is wearing her pink T-shirt today.` | cümle 3 parça 4 ve cümle 9 parça 2 | yok |
| `Konuşma anı: şimdiki zaman.` | yok. Yakın: cümle 9 "konuşma anında olan durum, şimdiki zaman"; cümle 14 "Konuşma anı, … şimdiki zaman" | yok |
| `Today iki zamanda da geçebilir; farkı anlam yapar.` | yok. Metin `surumler.json` `canAlici[3]`'ün yumuşak biçimi (S2-C); yakın: cümle 10 | yok |
| Cümle 3 (3 parça) | yok (S1 metni; S1-B jürisi + S1-C düzeltmesi 3) | VAR: S1 cümle 3 ile birebir |

**Ana dersin bir cümlesiyle birebir aynı cümle yok.** EN parçalar ana dersle aynıdır, ama önbellek anahtarı aynı cümlenin önceki ve sonraki
parçalarını da içerir (`dijital-anlatim/araclar/iki-dilli/el.py` satır 88 ve 140–142: `[metin, dil, onceki, sonraki, ses, model, tohum]`).
S1'de de aynı oldu: `I live in Istanbul.` ana dersle aynıydı ama ücretlendi (S1-C 257 karakter = cümle 2 + 3 karakter toplamı).
Cümle 3 S1 cümle 3 ile birebir aynıdır: üç parça, aynı komşular, aynı ses ve model → S1 önbelleğinden gelir (srv21 `~/.local/share/elevenlabs-onbellek`,
168 kayıt). S1 Whisper kapısı: 1,00 · 1,00 · 0,90 (`../../02-04-ydt-temel-s1/uretim-tutanagi/S1-C-RAPOR.md` §2).

## 4. Ses metni notları (`ses-tasarimi.md`, S1 §3 ile aynı)

- Sözcük *wear* TR parçada tek başına geçmez. Gerekçe: ana derste "Fiil aynı: wear." Whisper'da "Where" duyuldu (benzerlik 0,95; ana ders `sentez.wav.rapor.json`).
- *today* TR parçada geçer (cümle 2 parça 4; S2-C sentezinde "Today, iki zamanda da geçebilir." duyuldu, benzerlik 1,00). Emsal: ana ders cümle 9 ve 10'da TR parçadaki *today* "Today" duyuldu (benzerlik 1,00). Dil jürisi koşulu
  (ana ders `juri.md`): sentezde *today* kulakla dinlenir; düz okunursa cümle yeniden kurulur.
- EN parçalar tam cümledir; tek sözcüklük EN parça yok (13.11 KULAK). `T-shirt` sese `T shirt` gider (`ses_metni`, ana dersle aynı).
- TR parçada `-ing`, `yor`, kısaltma ve rakam yok. Hitap (sen/siz) yok (S1 karar 5).
- `@ydspublishing` sesle okunmaz; yalnız ekranda.
- Cümle 3'teki "ve": `ses_metni.py` Kural 7 sese `ve,` uygular; S1'de Whisper 1,00 geçti. Önbellekten geldiği için yeni denetim gerekmez.
- Maliyet (tahmin): yeni parçalar 188 karakter (cümle 1 + 2). S1 oranıyla (257 karakter ≈ 1,26 TL) ≈ 0,92 TL. Cümle 3 ücretsiz.

## 5. Süre (tahmin; gerçek süre sentez sonrası `zaman.json`)

Yöntem: her parça için ana dersin ya da S1'in ölçülmüş ikizi (aynı ses, aynı model). Parça arası: EN'li geçişte 0,25 sn, TR → TR 0,15 sn
(`el.py`). Cümle arası 0,55 sn. İlk söz 1,00 (S1 `zaman.giris.ilkSoz`).

| Cümle / parça | Sözcük | Ölçülmüş ikiz | sn | Başlar | Biter |
|---|---|---|---|---|---|
| 1 `Genel mi, şu an mı?` | 5 | ana ders cümle 18: 2,96–4,40 | 1,44 | 1,00 | 2,44 |
| 2 EN `She wears …` | 7 | ana ders cümle 3 parça 2: 3,45–5,77 | 2,32 | 2,99 | 5,31 |
| 2 TR `Genel durum: geniş zaman.` | 4 | ana ders cümle 3: 9,54–11,38 | 1,84 | 5,56 | 7,40 |
| 2 EN `She is wearing …` | 7 | ana ders cümle 3 parça 4: 11,63–14,35 | 2,72 | 7,65 | 10,37 |
| 2 TR `Konuşma anı: şimdiki zaman.` | 4 | cümle 14 "Konuşma anı," 0,96 + "şimdiki zaman." 0,76 + iki nokta duraklaması 0,23 | 1,95 | 10,62 | 12,57 |
| 2 TR `Today iki zamanda da geçer; …` | 8 | cümle 10 "Today iki cümlede de var." 1,68 + duraklama 0,16 + "Farkı anlam yapıyor:" 1,44 içinde "yapıyor" 0,76 yerine "yapar" ≈ 0,58 | 3,10 | 12,72 | 15,82 |
| 3 (S1 birebir) | 18 | S1 `sureler.json` cümle 3 | 9,02 | 16,37 | 25,39 |
| kuyruk | | | 1,00 | 25,39 | 26,39 |

**Ölçülen (S2-C, 15.11):** `anlatim.m4a` 27,98 sn. Cümle 1 1,00–2,84 (1,84; tahmin 1,44) · cümle 2 3,39–17,41 (14,02; S2-C sırası ve
`geçebilir` ile tahmin ≈ 13,03) · cümle 3 17,96–26,98 (9,02, önbellek) · kuyruk 1,0. Sahneler 01 0,00–2,84 · 02 2,84–17,41 · 03 17,41–27,98.
28 sn içinde; B planı gerekmedi. Aşağıdaki tablo S2-A tahminidir (eski parça sırasıyla).

Toplam tahmin **26,39 sn** (hedef 24–28). Üst sınır: S1'de cümle 2 tahmini %11 kısa çıktı (11,8 → 13,08). Yeni parçalara +%11 eklenince
toplam **27,86 sn**; 28 sn içinde kalır (pay 0,14 sn). Cümle 3 ölçülmüş olduğu için sapma taşımaz.

Sahne süreleri (tahmin): 01 = 2,44 sn (K23 giriş ≤ 3 sn) · 02 = 13,38 sn · 03 = 10,57 sn.
Kalıp §5 hedefi: can alıcı 0–5 sn → 1,00–2,44 · örnek 5–18 sn → 2,99–15,82 · çağrı 18–25 sn → 16,37–25,39.
İlk 10 sn'de 3 hareket türü: kinetik başlık ve uçuş (01), kalem çizimi (mont, tişört, `zaman_cizgisi`), karaoke (02).

**B planı (yalnız ölçülen toplam 28 sn'yi aşarsa; metin değişmez, jüri gerekmez):** 1) ilk söz 1,00 → 0,50 (kalıp §5 "ilk söz 0. sn"
izin verir; kapak hareketi 0,0–0,4) = −0,50 sn · 2) kuyruk 1,00 → 0,44 (S1-C açık nokta 1 seçeneği) = −0,56 sn.
