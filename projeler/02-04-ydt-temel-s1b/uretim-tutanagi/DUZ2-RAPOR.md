# DUZ2-0204S1 raporu — 02-04-ydt-temel-s1b (A/B kol b, değişken `kanca`) · J2 A düzeltmeleri + KBJ gerçek hataları · 15.11.2026

Yazan: üretici oturumu (fa49db46), model Claude Opus 5.5 (`claude-opus-5-5`). İstem DUZ2-0204S1. Girdi: `juri/KBJ-hukum.md`, `KBC-RAPOR.md`,
kol a raporu `../../02-04-ydt-temel-s1/uretim-tutanagi/DUZ2-RAPOR.md` (düzeltme ayrıntısı ve A3 metin gerekçesi orada). Ses sentezi, mp4,
commit, alt ajan YOK. Silinen dosya yok; taşınanlar `~/Silinecekler/2026-11-15-duz2-0204S1/` (`LISTE.md`).

| Ölçüm | Değer |
|---|---|
| Düzeltilen kusur | A1 (TD-1) · A3 (kart) · KBJ HV-22 · KBJ EK-3 · KBJ EK-6 · AB-8 (önbellek yolu) |
| Yeniden sentez | 0 cümle (değişken cümle 1 de değişmedi) |
| Süre | 27,89 sn (`anlatim.m4a` ffprobe 27,890000; ≤ 35 ✓, hedef 22–26 ✗) |
| Whisper en düşük | 0,96 (cümle 2 `I am living with my uncle.`, kol a ile aynı ses) |
| Çakışma kapısı | çıkış **0** (4 sahne, 0 uyarı; KBC'deki 4,50 sn `-um. × yor çip 1` uyarısı kalktı) |
| AB-8 taraması | 0 satır |
| AB-9 | cümle 2, 3, 4 sha256 kol a ile eş; cümle 1 değişken |
| `diff -rq` | §4: beklenmeyen 0 |

## 1. Düzeltmeler

| # | Kusur | Dosya | Önce → sonra | Kanıt |
|---|---|---|---|---|
| 1 | A1 / TD-1 | `ortak/anlatim/senaryo.json` `giris.rozetler`, `ortak/kunye.js`, `BRIEF-S1.md`, 7 × `yardim.py`, 7 × `SPEC.md` | `YDT · BASIC` → `YDT · TEMEL` (kol a ile aynı satırlar) | `cmp` kol a ↔ kol b: 7 `yardim.py` eş; bütün kol b karelerinde `YDT · TEMEL` |
| 2 | A3 kaydet kartı | `sahneler/08-hyperframes-kaydet/uret.py` (kol a dosyası `cp -p`, `cmp` eş) | 2 satır → `Live, work fiillerinde:` / `kalıcıysa geniş zaman,` / `geçiciyse şimdiki zaman.` | `k/08-…-21.54.png`, `k/koyu/08-…-21.54.png`; kol a 25,4 sn karesiyle fark 0 px |
| 3 | A3 grup türev kaynakları (kol b PNG üretmez) | `sahneler/04-…/uret.py`, `07-…/uret.py`, `SPEC.md`; `proje/index.html` (`ONIZLE_YALNIZ=1 calistir.sh --tema acik`) | kol a ile aynı | 04–07 `proje/index.html` kol a ile `cmp` eş |
| 4 | KBJ HV-22 (`-um. × yor çip 1`, 4,50 sn) | `sahneler/02-paperjs-ornek/kalem-paper.js` (`sonKay`), `sahne-02.js` (`SON_KAY = 24`) | sönme kayması 36 → 24 px (kol a ile aynı satırlar) | kapı çıkış 0 (§3); `sahne-02.js` kol a ↔ kol b fark satırı 44 = HEAD'deki 44 (düzeltme iki kolda aynı) |
| 5 | KBJ EK-3 (kol a'dan kopya kareler) | `sahneler/*/k/` | 08 ve 03 kareleri kol a'nın 18:54 / 19:20 kopyasıydı; 04–07 `k/` kol a QA kareleri | eski 45 kare `~/Silinecekler/…/eski-kare/02-04-ydt-temel-s1b/` altına taşındı; 4 sahnenin açık + koyu kareleri ve kapak A kol b'den yeniden çekildi (§3) |
| 6 | KBJ EK-6 (açıklama başlık notları) | `aciklama.md`, `aciklama-a.md`, `aciklama-b.md` | başlık `02-04-ydt-temel-s1` → `02-04-ydt-temel-s1b (A/B kol b, değişken kanca)`; `31,75 sn` → `27,89 sn`; `Sürüm: A (s1-aciklama-a)` → `s1b-aciklama-a`, B aynı; kaynak satırı kol a tutanağını gösterir; `kapak-b.png`, `hikaye*.png` atıfları "kol a paketinde (huni A/B §4)" | `diff` önce/sonra: 3 dosyada yalnız başlık notu ve atıf satırları; platform blokları ve `utm` değişmedi |
| 7 | AB-8 (kol a yolu) | `sahneler/04–07/proje/.hyperframes/video-state.json` (git dışı snapshot önbelleği) | kol a mutlak yolu taşıyordu (14 satır) | önbellek `~/Silinecekler/…/proje-hyperframes/` altına taşındı; AB-8 taraması 0 satır |
| 8 | Kimlik | `ortak/anlatim/senaryo.json` `meta.kimlik` | `02-04-ydt-temel-s1` → `02-04-ydt-temel-s1b` | `json.load` geçti; okuyan araç `VM.kod`'u önce okur (`ortak/editor/onizle.js:913`) |
| 9 | Tema damgası | `sahneler/05|06-…/RAPOR.md` | kol a koşusu `Tema: acik` satırı ekledi | kol a dosyası `cp -p`; iki kol eş |

## 2. Süre, ilk söz, Whisper (ses değişmedi)

| Ölçü | Kol b | Kol a | Sınır | Durum |
|---|---|---|---|---|
| Toplam süre | 27,89 sn | 31,75 sn | ≤ 35 (hedef 22–26) | sınır içinde; hedef iki kolda aşılır |
| İlk söz | 0,50 sn | 1,00 sn | ≤ 1 | ✓ |
| Kanca cümlesi bitişi (sözcük t1) | 2,58 sn | 6,44 sn | kanca ≤ 4 | kol b ✓; kol a aşar |
| Whisper en düşük | 0,96 | 0,96 | ≥ 0,90 | ✓ |

| Cümle | Kol b metni | sha256 (a / b) | Whisper (parça) |
|---|---|---|---|
| 1 (değişken) | Bu iki yaşıyorum aynı mı? | `35974df2f7f2` / `2f914435214e` | 1,00 |
| 2 | İngilizcede ikisi ayrılır. … Şimdilik: geçici durum, şimdiki zaman. | `a363311cf849` = | 1,00 · 1,00 · 1,00 · **0,96** · 1,00 |
| 3 | Bu, üç farktan yalnız biri. Sınavdan önce lazım olacak. Kaydet. | `0c3ba8612d3b` = | 1,00 · 1,00 |
| 4 (öğrenci) | Gerisi bizde. Dersin tamamı YDS Publishing YouTube kanalında. | `dd50c6bcd452` = | 1,00 · 1,00 |

## 3. Kareler, AB-3 ölçümü, kapı

Yöntem kol a ile aynı (`ONIZLE_YALNIZ=1 calistir.sh --tema koyu|acik` + `sahne-kare.mjs --port 41333 --sunucu 41022`; kapak A `proje-ka`
+ `hyperframes snapshot --at 1.75`). Kol b türevleri: yalnız kapak A (AB §4).

| Sahne / türev | Açık | Koyu |
|---|---|---|
| 01 kanca (değişken) | `k/01-…-0 · 0.9 · 1.3 · 1.75 · 2.2 · 2.45.png` | `k/koyu/…-1.75 · 2.2.png` |
| Kapak A | `kapak-a.png` = `kapak.png` (md5 `bf26cabd7f0b`), `k/ka-acik/at-1.75s.png` | `k/koyu/kapak-a-koyu.png` |
| 02 değer | `k/02-…-2.55 · 4.5 · 6 · 7.64 · 10 · 11.14 · 14 · 16.04.png` | `k/koyu/…-7.64 · 11.14.png` |
| 08 kaydet | `k/08-…-16.19 · 17.34 · 18.89 · 19.54 · 21.54.png` | `k/koyu/…-21.54.png` |
| 03 çağrı | `k/03-…-21.69 · 24.74 · 27.85.png` | `k/koyu/…-27.85.png` |

Göz denetimi (kontak `kontak-DUZ2-1.png`, `kontak-DUZ2-2.png`): taşma, çakışma, okunmayan yazı yok; rozet `YDT · TEMEL`; altyazı tek bantta;
0–280 ve 1570–1920 boş; kanal katmanı her karede y 291–339. Kapak A'da 4 yazı satırı (KBC açık noktası 5) değişmedi.

AB-3 (değişken dışı sahneler aynı içerik, aynı göreli an): kol b t ↔ kol a t + 3,86 sn, eşik 24/255, piksel sayısı.

| Çift (a ↔ b) | Tam kare | Altyazı bandı dışı | Kanal 280–350 |
|---|---|---|---|
| 02: 11,5 ↔ 7,64 · 15 ↔ 11,14 · 19,9 ↔ 16,04 · 13,86 ↔ 10 | 0 · 0 · 0 · 0 | 0 | 0 |
| 02: 9,86 ↔ 6 (kare hizalı 5,9667) | 77 (38) | 77 (38) | 0 |
| 02: 17,86 ↔ 14 (kare hizalı 13,9667) | 236 (0) | 236 (0) | 0 |
| 08: 20,05 · 21,2 · 22,75 · 23,4 · 25,4 ↔ 16,19 · 17,34 · 18,89 · 19,54 · 21,54 | 0 (5 çift) | 0 | 0 |
| 03: 25,55 · 28,6 · 31,7 ↔ 21,69 · 24,74 · 27,85 | 0 (3 çift) | 0 | 0 |
| koyu: 02 (2 çift), 08, 03 | 0 (4 çift) | 0 | 0 |

Kalan 38 px (x 205–220, y 580–587): `bag 1` okunun çizim başı kol a'da kare 194 (6,48 × 30 = 194,4), kol b'de kare 94 (3,12 × 30 = 93,6);
iki kol olay karesini ayrı yuvarlar (1 kare). Sahne 02 kodu bayt eşit değil (kol b `T_BAS 2.5`, `KARE 421`, kol b yolları, cümle 1 kuyruğu
kanca sahnesinde); içerik eşitliği yukarıdaki piksel ölçümüyle kanıtlanır.

HV-13: kart dikdörtgeni (x 61–959, y 601–979) 18,89 ↔ 21,54 sn → 0 px.

Çakışma kapısı (`kapi-cikti-DUZ2.txt`, JSON `cakisma-DUZ2.json`):

```
$ node araclar/cakisma-kapisi.mjs 02-04-ydt-temel-s1b --port 41333 --sunucu 41022 --json …/cakisma-DUZ2.json
01-hyperframes-kapak | çakışma yok (11 örnek, 2674 kutu)
02-paperjs-ornek | çakışma yok (56 örnek, 3106 kutu)
08-hyperframes-kaydet | çakışma yok (23 örnek, 2800 kutu)
03-hyperframes-cta | çakışma yok (26 örnek, 3880 kutu)
çıkış kodu: 0
```

AB-8 taraması:

```
$ grep -rn "02-04-ydt-temel-s1/" K/projeler/02-04-ydt-temel-s1b --include=*.js --include=*.html --include=*.json --include=*.py
(çıktı yok — 0 satır; surumler.json `varyant` alanı da bu deseni taşımaz)
ortak/kunye.js:6  export const KOK = "/projeler/02-04-ydt-temel-s1b/ortak";
```

## 4. Diff sınıflaması (`diff -rq K/projeler/02-04-ydt-temel-s1 K/projeler/02-04-ydt-temel-s1b`)

Kural tabanlı sınıflayıcı her satırı bir sınıfa bağlar; tam liste `diff-siniflama-DUZ2.txt`.

| Sınıf | Satır | Durum | Gerekçe |
|---|---|---|---|
| D1 değişken sahne 01 (kod, `proje`, `proje-ka`, QA kareleri, `__pycache__`) | 32 | beklenen | değişken `kanca` |
| D2 kapak A (`kapak-a.png` = `kapak.png`) | 2 | beklenen | A kapağı = kanca karesi (AB §4) |
| D3 `ortak/anlatim/cumle-1.wav` | 1 | beklenen | değişken cümle |
| D4 `ortak/anlatim/senaryo.json` | 1 | beklenen | cümle 1 + `meta.kimlik` s1b |
| D5 ses ve zaman türevleri (`zaman.json`, anlatım türevleri, `sozcuk_uret.py`, 08/03 `zamanlar.json`) | 14 | beklenen | cümle 1 süresi; 08/03 `zamanlar.json` yalnız küresel `t_bas`/`kuresel` (yerel zamanlar ve `proje/index.html` eş) |
| G1 sahne 02 (`sahne-02.js`, `kalem-paper.js`, `sayfa.html`, `calistir.sh`, `SPEC.md`, `RAPOR.md`) | 6 | gerekçeli | baş kırpımı (KBC); içerik eşitliği §3 piksel ölçümü; DUZ2 düzeltmesi iki kolda aynı |
| G2 `ortak/kunye.js` | 1 | gerekçeli | `KOK` kol b yolu (AB-8 bunu ister) |
| Q1 sahne 02/08/03 QA kareleri | 40 | beklenen | her kol kendi zaman çizelgesiyle çekildi (git dışı) |
| T1 grup türevleri yalnız kol a (kök `kapak-b/c`, `hikaye*`, 04–07 `k/` ve `.hyperframes`) | 21 | beklenen | AB §4: türevler gruba aittir |
| S1 `surumler.json` | 1 | beklenen | `varyant`, kol b sürüm satırları, `revizyonlar` r1 |
| S2 `aciklama*.md` | 3 | beklenen | `utm_content=s1b-*` + kol b başlık notları (EK-6) |
| U1 `uretim-tutanagi/` | 32 | beklenen | kola özgü tutanak |
| P1 `__pycache__` (sahne 01 dışı) | 9 | beklenen | derleme önbelleği (git dışı) |
| **Toplam** | **163** | **beklenmeyen 0** | sınıfsız satır 0 |

Değişmeyen (bayt eş): 04–07 kaynakları ve `proje/index.html`, 08/03 `proje/index.html`, `uret.py`, `yardim.py`, `BRIEF-S1.md`, `ortak/` (kunye.js dışı).

## 5. Düzeltilmeyen maddeler (KBJ)

| KBJ maddesi | İşaret | Sebep |
|---|---|---|
| HV-19 (s2, s2b küçük harf) | ölçüt | J2-OZET B2: yayın bağları büyük harf; s2/s2b bu paketin dışı |
| HV-21 (kol b'de hikâye yok) | ölçüt | `juri-olcutleri.md` HV-21 "A/B kol b'de uygulanmaz" |
| HV-20 (kol b türevleri) | ölçüt | HV-20 "A/B kol b'de uygulanmaz"; yalnız kapak A |
| HV-17 (YEDESE) | ölçüt | J2-OZET B1; KBJ zaten "evet" dedi |
| AB-4, AB-5, AB-7 | ölçüt (yayın sonrası) | `juri-olcutleri.md` §2d: üretim jürisinde uygulanmaz |
| EK-12 (başlık sesten önce) | ölçüt | `juri-olcutleri.md` EK-12 istisnası: kanca sahnesi başlığı ilk sözden önce görünebilir |
| AB-3 bayt eşitliği (sahne 02 kodu) | ölçüt / gerekçeli | baş kırpımı: kol b sahne 02 kancanın kuyruğunu taşımaz; içerik eşitliği §3 piksel ölçümüyle; bayt eşitliği için `T_BAS`/yol parametre dosyasına taşınmalı (şef kararı, A sınıfı değil) |
| EK-5c "Hep orada" | gerçek hata saymadım | kural cümlesi değil, örneğin durumunu anlatır ("Şimdilik" karşıtı); J2-OZET T1 EK-5c = G; değiştirmek iki kolda değer sesini değiştirir. Şef kararı |
| Süre farkı −3,86 sn (kol b lehine yanlılık) | bilgi | değişkenin doğal sonucu (KBC §6.2); kıyas okunurken not düşülür |
| Süre hedefi 22–26 | — | ses yeniden yazılmadı |
| `senaryo.json` `giris.satir2` (`= İKİ ZAMAN`) | — | okuyan araç yok; kol b kanca başlığı sahne 01 `uret.py` içinde (KBC §6.6) |

## 6. Değiştirilen dosyalar

Git'te izlenen: `BRIEF-S1.md`, `aciklama.md`, `aciklama-a.md`, `aciklama-b.md`, `ortak/anlatim/senaryo.json`, `ortak/kunye.js`, `surumler.json`
(`revizyonlar` r1), `sahneler/01-hyperframes-kapak/{yardim.py,SPEC.md,proje/index.html,proje-ka/index.html}`,
`sahneler/02-paperjs-ornek/{kalem-paper.js,sahne-02.js,SPEC.md}`, `sahneler/03-hyperframes-cta/{yardim.py,SPEC.md,proje/index.html,zamanlar.json}`,
`sahneler/04–07/{uret.py (04, 07),yardim.py,SPEC.md,nesneler.json,proje/index.html,RAPOR.md (05, 06)}`,
`sahneler/08-hyperframes-kaydet/{uret.py,yardim.py,SPEC.md,proje/index.html,zamanlar.json}`; yeni: `uretim-tutanagi/{DUZ2-RAPOR.md,
kapi-cikti-DUZ2.txt,cakisma-DUZ2.json,diff-siniflama-DUZ2.txt,kontak-DUZ2-1.png,kontak-DUZ2-2.png}`.
Git dışı: `kapak-a.png`, `kapak.png`, `sahneler/*/k/` kareleri.
