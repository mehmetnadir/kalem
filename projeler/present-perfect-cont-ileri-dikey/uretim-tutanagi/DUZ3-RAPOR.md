# DUZ3-0209I — `present-perfect-cont-ileri-dikey` dikey tam ders düzeltmesi · 16.11.2026

> Ana rapor: `../../present-perfect-cont-ileri/uretim-tutanagi/DUZ3-RAPOR.md` (cümle tablosu, Whisper, gerekçeler orada).
> Bu rapor dikey pakete özgü işleri yazar. Render yok, mp4 yok, alt ajan yok.

## 1. Ses

`ortak/anlatim` dizini ana paketin anlatımına bağdır (`-> ../../present-perfect-cont-ileri/ortak/anlatim`). Ses yeniden sentezlenmedi,
kopya gerekmedi: `anlatim.wav` sha256 iki yoldan da `164e00d44df2` (aynı dosya). `sozcukler.json`, `altyazi.json`, `METIN.md` da ortaktır.

| Ölçü | Önce | Sonra |
|---|---|---|
| Ders süresi | 85,93 sn | 92,89 sn |
| `zaman.json` 03 / 04 / 05 / 06 | 505 · 478 · 392 · 752 kare | 553 · 478 · 428 · 877 kare (t sınırları ana paketle aynı: 17,25 · 35,28 · 50,80 · 64,67 · 92,89) |

## 2. Sahneler

| Sahne | Ne değişti | Neden |
|---|---|---|
| 01 giriş | `uret.py`, `yardim.py`: rozet `YDT · İLERİ` → `proje/index.html` | HV-24 |
| 02–05 künye rozeti | `ortak/kunye.js` `rozet: "YDT · İLERİ"` | HV-24 |
| 03 örnek 1 | p1–p4 sabitleri yeni sese eşlendi (ana raporla aynı betik); formül kartı 2. satır `→ have been + V-ing` → `hâlâ sürüyor: have been + V-ing` (Caveat 64 sarı + Fredoka 72; sağ uç ≈ 1009, kart 1032). Eski "→" since + past simple'dan sonra hep have been gelir diye okunuyordu. Tik sığmadığı için kaldırıldı; parıltı kaldı | c3 yeni metin |
| 04 örnek 2 | `kayma: -1.6`; `sahne-ortak.js` altyazı satırı `zm(...) - this.kayma` (altyazı küresel yeni çerçevede; kardeş derste bulunan aynı hata) | c3 +1,60 sn |
| 05 örnek 3 | TBAS 50,80, kare 428; not 3 satır `durum fiili:` / `genellikle` / `-ing yok` (Caveat 64, x 730, satırlar ky+180/250/320, sağ uç 963); eski `-ing yok` anlatımsızdı, şimdi sözcük pencereli | c5 yeni metin |
| 06 soru + form | `dn` `durum anlatır, süreç değil` (Caveat 72); tablo iskeleti `S(T(6, 1)) + 0,19` / `S(T(6, 3)) + 0,03` (eski sabit 63,5 / 63,9); dizinler +3; oklar `okuyorum → süreç`, `bitirdim → sonuç`; kod `süreç → been + -ing ✓` / `sonuç, durum → have + V3 ✓` (Fredoka 72, ok 20 + 52 + 20 px, sağ uç ≈ 1008); çip toplanma `tk − 0,6` = 84,73 | c7 yeni metin |
| `BRIEF-DIKEY.md` | kare listesi, rozet, 03 ve 06 satırları, biçim tablosundaki `-yor = -ing` örneği `have been + V-ing` oldu | belge |

Kareler (kendim baktım; `node araclar/sahne-kare.mjs present-perfect-cont-ileri-dikey <sahne> <t,…> <dizin> --tema acik --port 41333 --sunucu 41022`,
dizin `sahneler/<sahne>/k/duz3/`, git dışı; kontak sayfaları `~/is/duz3-0209I/d0*.png`):

| Sahne | Anlar (sn) | Gözlem |
|---|---|---|
| 01 | 1,2 · 2,9 | hap `YDT · İLERİ`; altyazı `Süreç mi, sonuç mu?` |
| 02 | 9,0 · 16,5 | rozet `YDT · İLERİ`; altyazı 2 satır |
| 03 | 22,6 · 28,6 · 31,9 · 33,6 · 35,25 | `hâlâ sürüyor:` sesle yazılır; 2. satır karta sığar; altyazı c3 p5 2 satır |
| 04 | 36,0 · 38,2 · 43,0 · 47,5 · 50,7 | altyazı konuşulan cümlede (36,0 `İkinci örnek.`, 47,5 `Süreç, been reading …`) → kayma düzeltmesi doğru |
| 05 | 51,6 · 54,4 · 57,6 · 60,4 · 62,5 · 63,6 · 64,6 | 3 satırlık not know-ing'e ve Present Perfect kutusuna değmez (tam boy kırpım baktım) |
| 06 | 66,6 · 70,0 · 72,4 · 76,0 · 79,6 · 82,6 · 84,4 · 85,5 · 87,3 · 89,6 · 91,0 · 92,3 · 92,85 | oklar etiket satırının sağında; kod tikleri kartın içinde; altyazı c7 p5 (80 karakter) 2 satır |

## 3. Kapak

Değişmedi (ana rapor §5). `ortak/kapak` ana pakete bağdır.

## 4. Yayın verisi

`youtube.json` ana paketle bayt bayt aynı (`cmp` eşit); `youtube-aciklama.md` farkı yalnız `utm_content=dikey-tam`. Zaman farkı ana rapor §6.

## 5. Çakışma kapısı

```
$ node araclar/cakisma-kapisi.mjs present-perfect-cont-ileri-dikey --port 41333 --sunucu 41022 --json ~/is/duz3-0209I/kapi-dikey.json
04: çakışma yok
01: cg:path0 × cg:text0 (giriş uçuşu) hata
02: form/2 traps × time clues uyarı
03: cizgi × the / timetable, / students (kök alt çizgisi × kök sözcükleri, 20,25–35,25) 3 hata
05: okul × İlkokuldan / beri birbirimizi / tanıyoruz. (58,80 tek örnek, figürlerin sola alta toplanma anı) 3 hata;
    beri birbirimizi × İlkokuldan / tanıyoruz. (TR 60 px satır aralığı) uyarı
06: hb0/hb1/hb2 × s1, s1:path0 (have been knowing × kırmızı üstü çizgi) 6 hata
→ çıkış 1
```

İlk koşuda yeni not satırları (05) 5 px kutu payıyla 3 uyarı verdi; satır aralığı 65 → 70 px yapıldı, sahne 05 yeniden ölçüldü
(`--sahne 05-canvas-ornek3`, `kapi-dikey-05.json`): yeni öğelerden uyarı 0. Kalan hataların hepsi bu işte geometrisi değişmeyen öğelerdedir;
05'teki toplanma anı yerel karede eskisiyle aynı yerde (231 → 233. kare). HEAD için taban ölçümü koşulmadı (ana rapor §7).

---
Son Güncelleme: 16.11.2026 (DUZ3-0209I oturumu).
