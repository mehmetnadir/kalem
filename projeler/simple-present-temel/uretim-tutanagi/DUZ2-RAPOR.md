# DUZ2-SPANA — `simple-present-temel` ana ders düzeltmeleri · 15.11.2026

> Girdi: `uretim-hatti/raporlar/J2-OZET-1511.md` §3A "Ana derste aynı hata" (A1, A2, A3), §4.1 TD-1, TD-2, TD-3.
> Makine srv21 (Linux x86_64). Render yok, mp4 yok, alt ajan yok. Silinen dosya yok: eski dosyalar
> `~/Silinecekler/2026-11-15-duz2-SPANA/` altında (`~/Silinecekler/LISTE.md` satırları yazıldı).
> Dikey paketin raporu: `../simple-present-temel-dikey/uretim-tutanagi/DUZ2-RAPOR.md`.

## 1. Düzeltme tablosu

| # | Kusur | Dosya | Önce → sonra | Kanıt |
|---|---|---|---|---|
| A1 | Rozet (TD-1) | `ortak/anlatim/senaryo.json` `giris.rozetler[0]` | `YDT · BASIC` → `YDT · TEMEL` | §6 grep |
| A1 | Rozet | `ortak/kunye.js` `KUNYE.seviye` (02–05 künyesi) | `YDT BASIC` → `YDT TEMEL` | kare 02–05 |
| A1 | Rozet | `sahneler/01-hyperframes-giris/{uret.py, yardim.py, nesneler.json}` | rozet hapı + künye `· YDT TEMEL` | kare 01 |
| A1 | Rozet | `sahneler/06-hyperframes-form/yardim.py` | künye `· YDT TEMEL` | kare 06 |
| A1 | Rozet | `sahneler/90-hyperframes-kapak/yardim.py` `ROZET` (kullanılmayan sabit) | `YDT · TEMEL` | grep |
| A1 | Rozet | `BRIEF.md` satır 95, 109 | `YDT TEMEL`, `YDT · TEMEL` | grep |
| A2 | Karakter erkek (TD-2, K22, KS-10) | `ortak/kapak/karakter.png` | erkek, iri kıvırcık saç → kadın öğrenci, uzun kâkül, yuvarlak gözlük | sha256 `5a902b40…` |
| A2 | Karakter kaydı | `ortak/kapak/KAYNAK.json` `gorseller[0]` | `uretim_id` d97e66af… → f312969e…; tarif, referans | dosya |
| A2 | Kapak yerleşimi | `sahneler/90-hyperframes-kapak/uret.py` `yatay()`, `dikey()` | §4 tablosu | assert + kare |
| A2 | Kapak | `kapak.png`, `kapak-koyu.png`, `uretim-tutanagi/kapak-168.png` | yeni karakterle yeniden çekildi | §4 |
| A3 | Yanlış denklik (TD-3) | `ortak/anlatim/senaryo.json` cümle 7 parça 6 + `metin` | §2 | Whisper 1,00 |
| A3 | Yanlış denklik | `senaryo.json` `meta.canAlici[0]` | §2 | dosya |
| A3 | Yanlış denklik | `surumler.json` `video.canAlici[0]` | `meta.canAlici` ile aynı metin | assert eşit |
| A3 | Ses | `ortak/anlatim/{anlatim.wav, anlatim.m4a, cumle-1…7.wav}` (git dışı) | yalnız cümle 7 yeni | §3 |
| A3 | Zaman zinciri | `sureler.json`, `sozcukler.json`, `altyazi.json`, `METIN.md`, `zaman.json` | yalnız cümle 7 ve sahne 06 | §3 |
| A3 | Ekran kartı | `sahneler/06-hyperframes-form/{uret.py, zamanlar.json, calistir.sh}` | `Türkçe: -er eki` / `git-er = go-es` → 2×2 kart | kare 06 |
| — | Sürüm kaydı | `surumler.json` `revizyonlar[]` | `ana-yatay r1`, `dikey-tam r1` eklendi | dosya |

`youtube.json` ve `youtube-aciklama.md`: denklik ifadesi yok (grep 0). Bölüm anları 0 · 15,45 · 27,69 · 43,36 · 60,47 ve bildirim 43,91;
hepsi cümle 7'nin başından (65,73) önce. Değişiklik gerekmedi.

## 2. Cümle 7

| | Metin (parça 6) |
|---|---|
| Eski | `Türkçedeki er eki gibi: git-er, go-es.` |
| Yeni | `Türkçede geniş zaman eki her kişide gelir, İngilizcede s yalnız üçüncü tekil kişide.` |
| `canAlici[0]` eski | `Türkçedeki geniş zaman eki = İngilizcedeki s: gider = goes` |
| `canAlici[0]` yeni | `Geniş zaman eki Türkçede her kişide gelir (giderim, gider); İngilizcede s yalnız he, she, it ile gelir (I go, he goes)` |

Gerekçe (istemdeki örnek yerine bu cümle):
1. İstem örneği (`He, she, it özneyse fiile s gelir: go, goes.`) doğrudur. Ama aynı cümlenin parça 3'ü bunu zaten söyler
   ("Fiile s gelir. I, you, we, they ile gelmez."). Örnek yeni bilgi taşımaz.
2. Dersin amacı 4 "Türkçe geniş zaman eki ile köprü"dür. Yeni cümle köprüyü korur ve yanlış denkliği doğru karşıtlığa çevirir:
   Türkçe ek her kişide gelir (gid-er-im, gid-er), İngilizce `-s` yalnız üçüncü tekil kişide gelir. J2 özetinin hata tanımıyla aynı.
3. Terim cümlenin başıyla aynıdır ("üçüncü tekil kişi"). Ses parçasında İngilizce sözcük yok; Whisper Türkçe kipte 1,00.

Ekran kartı (sahne 06, x 1090–1468, y 545–690): TR satırı `giderim · gider` (Caveat 60, soluk, iki `er` sarı + alt çizgi),
EN satırı `I go · he goes` (Caveat 72, mürekkep, yalnız `es` sarı + alt çizgi). Sütun 1 = 1. kişi, sütun 2 = 3. tekil (DK-2: EN büyük, TR soluk).
Açılış: `giderim` "eki" (85,36) · `gider` "her" (85,60) · `er` çizgileri "kişide" (85,84 / 86,04) · `I go` "İngilizcede" (86,92) ·
`he goes` "üçüncü" (88,80) · `es` çizgisi "tekil" (89,20).

## 3. Ses ve süre

Yöntem (öteki cümlelerin sesi değişmez):
1. Sunucu önbelleğinde (`~/.local/share/elevenlabs-onbellek`) bu dersin hiçbir parçası yoktu (ağsız anahtar benzetimi: 0 / 30; ses
   Mac'te üretilmiş). `el.py` bütün senaryoyla koşsaydı 7 cümlenin hepsi yeniden sentezlenirdi.
2. Bu yüzden `el.py` yalnız cümle 7'yi taşıyan geçici senaryoyla koştu: `HIZ_EN=0.8 bash araclar/ses-sunucu.sh --kok <geçici kök>
   simple-present-temel` (vekil, eleven_v4, öğretmen sesi). 298 karakter (≈ 1,46 TL), rc 0, 7 / 7 parça kapıdan geçti.
3. `HIZ_EN` 0,8: ana derste `My brother usually goes to school by bus.` 2,96 sn; aynı cümle `-s2` kısasında (0,9) 2,64 sn; oran 1,12 ≈ 0,9 / 0,8.
4. Cümle 1–6 wav'ı eski `anlatim.wav`'dan örnek-eşit kesildi (`[başlangıç_N, başlangıç_N+1)`, 48 kHz), cümle 7 = yeni `cumle-1.wav`.
   `kur.py` → `anlatim.wav`; `ses-paketle.py --yaz` → `anlatim.m4a`.
5. Kanıt: 0–65,73 sn PCM sha256 eski = yeni = `b0f44270cc91e764…`. `sozcukler.json` cümle 1–6: 113 sözcük eşit.
   `sureler.json` cümle 1–6 eşit (fark satır 693'ten başlar).

| Ölçü | Önce | Sonra |
|---|---|---|
| Cümle 7 süresi | 26,74 sn | 29,70 sn (+2,96) |
| Cümle 7 sözcük | 45 | 52 |
| Konuşma sonu | 92,47 | 95,43 |
| Ders süresi (`zaman.json` son `t_son`, `anlatim.wav`) | 93,47 sn | 96,47 sn |
| Sahne 06 kare / içerik kare | 1020 / 990 | 1110 / 1080 (`calistir.sh` `KARE=1110`) |
| `anlatim.wav` sha256 | `7a0ed8c4…` | `db210a86…` |
| `anlatim.m4a` sha256 | — (sunucuda yoktu) | `bba1167a…` |

Whisper (faster-whisper large-v3-turbo int8, eşik 0,85; rapor `uretim-tutanagi/DUZ2-cumle7-sentez.rapor.json`):

| Parça | Dil | Metin | Duyulan | Benzerlik |
|---|---|---|---|---|
| 1 | tr | Çünkü özne üçüncü tekil kişi: | Çünkü özne üçüncü tekil kişi. | 1,00 |
| 2 | en | he, she, it. | He, she, it. | 1,00 |
| 3 | tr | Fiile s gelir. I, you, we, they ile gelmez. | (aynı) | 1,00 |
| 4 | tr | Olumsuzda ve soruda does girer, s ona geçer. | Olumsuzda ve soruda döz girer, S 10'a geçer. | **0,96** (en düşük) |
| 5 | en | He does not go. Does he go? | (aynı) | 1,00 |
| 6 | tr | Türkçede geniş zaman eki her kişide gelir, İngilizcede s yalnız üçüncü tekil kişide. | Türkçe'de … İngilizce'de S … kişide. | 1,00 |
| 7 | tr | Kod: always, usually, every day, Simple Present. | COD. Always. Usually. Every day. Simple Present. | 0,98 |

Sahne 06 `zamanlar.json`: cümle 7'deki 29 anahtar yeni `sozcukler.json`'dan; betik denetimi "hata yok" (ana ve dikey).

## 4. Karakter ve kapak

Yeni görsel 1024×1024 (eski 896×1200), kol yukarıda. Eski yerleşimle el "= GOES" kutusuna, gövde süre rozeti bölgesine giriyordu.
Yeni değerler `uret.py`'nin kendi assert'leriyle bulundu (taşma, 34 px yazı payı, boş bölge, minibüs payı):

| Düzen | Önce | Sonra | Sınır |
|---|---|---|---|
| Yatay karakter | s 1,05 · sol 880 | s 0,95 · sol 854 · üst 117,25 (kutu x 995–1607, y 198–1090) | el x ≥ 988; gövde x < 1614 |
| Yatay minibüs | kutu x 640 | kutu x 610, y 842 (aynı boy) | karaktere 22 px pay |
| Dikey karakter | s 0,64 · sol 323 | s 0,64 · sol 320 · kesim satır 1000 (kutu x 415–828, y 930–1516) | alt %20 boş |
| Dikey daire | merkez 625 | merkez 650 | yazıya ≥ 24 px |

İşaret yönü: sol üst (metne doğru). Yatayda parmak "= GOES" kutusunu gösterir, kutudan ≈ 45 px uzakta.

| Kapak | Dosya | Boyut | sha256 (ilk 12) |
|---|---|---|---|
| Yatay açık | `kapak.png` | 1920×1080 | `7f714514f0c1` |
| Yatay koyu | `kapak-koyu.png` | 1920×1080 | `7e948a3b7ae4` |
| Küçük görünüm | `uretim-tutanagi/kapak-168.png` | 168×94 | "GİDER = GOES" ve yüz okunuyor |
| Dikey açık / koyu | `../simple-present-temel-dikey/kapak.png`, `kapak-koyu.png` | 1080×1920 | `1fe5eba99fc9` / `d5885c390e09` |

Çekim: `bash sahneler/90-hyperframes-kapak/calistir.sh --tema koyu|acik` (yalnız `hyperframes snapshot`), rc 0 ×4; ham kareler
`sahneler/90-hyperframes-kapak/k/at-0.5s.png`, `k/koyu/at-0.5s.png`. Read ile bakıldı: taşma yok, yazı–karakter binmesi yok,
sağ alt boş, rozet `YDT · TEMEL`, büyük İ doğru, emoji yok.

## 5. Kareler (kendim baktım)

Komut: `node araclar/sahne-kare.mjs simple-present-temel <sahne> <t,…> <dizin> --tema acik --port 41333 --sunucu 41022`.
Dizin: `sahneler/<sahne>/k/duz2/` (git dışı).

| Sahne | Anlar (sn) | Gözlem |
|---|---|---|
| 01 giriş | 1,2 · 2,0 · 2,9 | hap `YDT · TEMEL` + `GRAMMAR`; taşma yok |
| 02 kanca | 9,0 | künye `SIMPLE PRESENT · YDT TEMEL` |
| 03 örnek 1 | 22,0 | künye aynı |
| 04 örnek 2 | 41,5 | künye aynı |
| 05 örnek 3 | 52,0 | künye aynı |
| 06 soru + form | 66,6 · 76,4 · 83,5 · 85,7 · 86,6 · 88,0 · 89,9 · 93,0 · 95,8 · 96,4; koyu 96,4 (`k/duz2/koyu/`) | kart açılış sırası doğru; "3. tekil kişi" yazısına 90 px; formül kartıyla çakışma yok; koyuda okunur |

Önceki kare (kusurlu kart): `~/is/uretim-0204/duz2-spana/once/simple-present-temel/06-hyperframes-form-92.4.png`.

## 6. Kapılar

```
$ grep -rIl "BASIC" projeler/simple-present-temel projeler/simple-present-temel-dikey
projeler/simple-present-temel/sahneler/01-hyperframes-giris/RAPOR.md     (sahne tutanağı)
projeler/simple-present-temel/uretim-tutanagi/YV-RAPOR.md               (tutanak)
→ üretim dosyalarında 0

$ node araclar/cakisma-kapisi.mjs simple-present-temel --port 41333 --sunucu 41022 --json …/kapi-ana.json
01, 02, 03, 04: çakışma yok · 05: tomorrow × ucak (47,86–49,11) · 06: ok0/ok1/ok2 × row1/row2 (66,47), d_go × kir,
d_s × kir2 (75,22), sdup × sok, dnot × sok        → çıkış 1 (9 hata, 7 uyarı)
```

Taban (aynı araç, sahne 06'nın HEAD `index.html` + `olaylar.json`'u geçici olarak yerine konup ölçüldü, sonra geri yüklendi;
`cmp` eşit): çıkış 1, aynı 7 hata (ok × row, d_go × kir, sdup × sok, dnot × sok). Yeni sürümde ek görünen `d_s × kir2`
kasıtlı kırmızı X'in ikinci çizgisidir; zaman 0,32 sn kayınca 0,25 sn örnekleme anı çizim anına denk geldi. Yeni kart öğelerinde
(`tr1`, `tr2`, `tra*`, `en1`, `en2`, `ena`) hata 0; yalnız aynı sözcüğün renk dilimleri arasında 3 uyarı. 05'teki hata değişmeyen
sahne içeriğindedir. Kapı çıkışı 0 değil: eski tasarım kusurları bu düzeltmenin kapsamı dışında.

`python3 -m py_compile`: 06 ve 90 `uret.py` derlendi. Kapak assert'leri iki temada geçti.

## 7. Düzeltemediklerim / açık kalanlar

| Madde | Sebep |
|---|---|
| EK-11 kulak dinlemesi (cümle 7 yeni ses) | Nadir'in işi; Whisper süzgeçtir, kulak kararı onu aşar |
| Çakışma kapısı çıkış 1 | eski tasarımdaki 9 hata (yukarıda); bu oturumun kapsamı dışı |
| `GRAMMAR` rozeti İngilizce | istem yalnız `BASIC` → `TEMEL` istedi |
| Parça 4 "Olumsuzda ve soruda does girer" | ana derste he/she/it bağlamından hemen sonra gelir; J2 ana ders satırında yok, dokunulmadı |
| mp4'ler bayat | render yasak; Nadir isterse `calistir.sh` (06 için `KARE=1110` güncel) |
| `sahneler/01-hyperframes-giris/RAPOR.md`, `YV-RAPOR.md` | tutanak; eski durumu kaydeder |
| HF `index.html` dosyaları artık açık tema varsayılan | son çekim açık (D-0341, DUZ-1 kalıbı); canlı önizleme tema mesajıyla koyuya geçer (koyu kare alındı) |
| `.claude/docs/sozlesme.md`, Kovan | istem yazmayı iki paketle sınırladı |

---
Son Güncelleme: 16.11.2026 (DUZ2-SPANA oturumu).
