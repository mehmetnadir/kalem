# DUZ2-SPANA — `simple-present-temel-dikey` düzeltmeleri · 15.11.2026

> Girdi: `uretim-hatti/raporlar/J2-OZET-1511.md` §3A ("SP-dikey: A1 rozet; A2 dikey kapak"), §4.1 TD-1, TD-2, TD-3.
> Ses, senaryo, altyazı ve kapak görseli ana paketle ortaktır: `ortak/anlatim` → `../../simple-present-temel/ortak/anlatim`,
> `ortak/kapak` → `../../simple-present-temel/ortak/kapak` (simge bağı). Ayrıntı ve cümle 7 gerekçesi:
> `../simple-present-temel/uretim-tutanagi/DUZ2-RAPOR.md`. Render yok, silme yok.

## 1. Düzeltme tablosu

| # | Kusur | Dosya | Önce → sonra | Kanıt |
|---|---|---|---|---|
| A1 | Rozet (TD-1) | `ortak/kunye.js` `KUNYE.rozet` (02–05 künye hapı) | `YDT · BASIC` → `YDT · TEMEL` | kare 02–05 |
| A1 | Rozet | `sahneler/01-hyperframes-giris/yardim.py` `ROZETLER` | `YDT · TEMEL`, `GRAMMAR` | kare 01 |
| A1 | Rozet | `sahneler/06-hyperframes-form/yardim.py` (hap genişliği + metin) | `YDT · TEMEL` | kare 06 |
| A1 | Rozet | `BRIEF-DIKEY.md` satır 57 | `YDT · TEMEL` | grep |
| A1 | Rozet | `senaryo.json` `giris.rozetler` | ana paketle ortak dosya | ana rapor |
| A2 | Dikey kapak (TD-2) | `kapak.png`, `kapak-koyu.png` | erkek karakter → kadın öğrenci | §3 |
| A2 | Karakter dosyası | `ortak/kapak/karakter.png` (bağ) | kopya gerekmedi; bağ yeni dosyayı gösterir | sha256 eşit |
| A3 | Ekran kartı (TD-3) | `sahneler/06-hyperframes-form/uret.py` | `Türkçe: git-er = go-es` → `giderim · gider │ I go · he goes` | kare 06 |
| A3 | Zaman | `sahneler/06-hyperframes-form/zamanlar.json` | cümle 7 anahtarları yeni sözcük zamanlarından; `kare` 1020 → 1110 | betik denetimi |
| A3 | Zaman | `zaman.json` sahne 6 | `t_son` 93,47 → 96,47; `kare` 1020 → 1110; `icerik_kare` 990 → 1080 | dosya |
| A3 | Zaman | `sahneler/06-hyperframes-form/calistir.sh` | `KARE=1020` → `KARE=1110` | dosya |
| A3 | Altyazı | sahne 06 altyazı dilimleri | ortak `altyazi.json` + `sozcukler.json` (yeni parça 2 satıra bölündü) | kare 06 |

`youtube.json`, `youtube-aciklama.md`: denklik ifadesi yok; bölüm anları ve bildirim (43,91) cümle 7'den önce. Değişiklik gerekmedi.
Bu paketin `surumler.json` dosyası yok; sürüm kaydı ana paketin `surumler.json` `revizyonlar[]` → `dikey-tam r1`.

## 2. Ses (ortak dosya)

| Dosya | Yol (ana / dikey) | sha256 |
|---|---|---|
| `anlatim.wav` | `../simple-present-temel/ortak/anlatim/` = `ortak/anlatim/` | `db210a861e29…` (iki yolda eşit) |
| `anlatim.m4a` | aynı | `bba1167a69ab…` (iki yolda eşit) |
| `karakter.png` | `../simple-present-temel/ortak/kapak/` = `ortak/kapak/` | `5a902b401816…` (iki yolda eşit) |

Yeniden sentez yok (dikey için). Cümle 7: 26,74 → 29,70 sn; ders 93,47 → 96,47 sn; Whisper en düşük 0,96 (ana rapor §3).

## 3. Kapak

Üretici ana paketteki `sahneler/90-hyperframes-kapak/uret.py --duzen dikey` (tek kaynak). Yeni değerler: karakter s 0,64, sol 320,
kesim satır 1000 (kutu x 415–828, y 930–1516); daire merkezi 625 → 650. Assert'ler iki temada geçti (üst/alt %20 boş, yazı payı,
minibüs payı).

| Kapak | Dosya | Boyut | sha256 (ilk 12) |
|---|---|---|---|
| Dikey açık | `kapak.png` | 1080×1920 | `1fe5eba99fc9` |
| Dikey koyu | `kapak-koyu.png` | 1080×1920 | `d5885c390e09` |

Çekim: `bash sahneler/90-hyperframes-kapak/calistir.sh --tema koyu|acik` → rc 0 ×2; ham kare `sahneler/90-hyperframes-kapak/k/at-0.5s.png`,
`k/koyu/at-0.5s.png`. Read ile bakıldı: karakter metne doğru sol üstü gösterir, üst ve alt %20 yalnız zemin, rozet `YDT · TEMEL`,
taşma ve binme yok.

## 4. Kareler (kendim baktım)

Komut: `node araclar/sahne-kare.mjs simple-present-temel-dikey <sahne> <t,…> <dizin> --tema acik --port 41333 --sunucu 41022`;
dizin `sahneler/<sahne>/k/duz2/` (git dışı).

| Sahne | Anlar (sn) | Gözlem |
|---|---|---|
| 01 giriş | 1,2 · 2,0 · 2,9 | haplar `YDT · TEMEL` + `GRAMMAR` |
| 02–05 | 9,0 · 22,0 · 41,5 · 52,0 | künye hapı `YDT · TEMEL` |
| 06 soru + form | 66,6 · 76,4 · 83,5 · 85,7 · 86,6 · 88,0 · 89,9 · 93,0 · 95,8 · 96,4; koyu 96,4 (`k/duz2/koyu/`) | kart satırı y 1222 (≈ 794 / 984 px), `does` kartı ile `always` satırı arasında; yeni altyazı 2 satır; "Next lesson" ile çakışma yok; koyuda okunur |

Önceki kare: `~/is/uretim-0204/duz2-spana/once/simple-present-temel-dikey/06-hyperframes-form-92.4.png`.

## 5. Kapılar

```
$ grep -rIl "BASIC" projeler/simple-present-temel-dikey      → 0 dosya

$ node araclar/cakisma-kapisi.mjs simple-present-temel-dikey --port 41333 --sunucu 41022 --json …/kapi-dikey.json
01, 03: çakışma yok · 02: yalnız uyarı · 04: every day / go / -es × otobus · 05: tomorrow × ucak ·
06: ok0/ok2 × row0–2 (66,47), d_v × kir, f0–f2 × fu0–fu2 (91,72 / 92,72 / 93,72)        → çıkış 1
```

Taban (sahne 06 HEAD `index.html` + `olaylar.json` geçici olarak yerine konup ölçüldü, geri yüklendi, `cmp` eşit): çıkış 1, aynı
5 hata (ok × row, d_v × kir). Yeni sürümde ek görünen `f0–f2 × fu0–fu2` değişmeyen `always · usually · every day` alt çizgileridir;
zaman kayınca örnekleme anı açılış animasyonuna denk geldi (tek örnek, sonra yok). Yeni kart öğelerinde (`tr1`, `tr2`, `tra*`, `ayr`,
`en1`, `en2`, `ena`) hata 0. 04 ve 05 hataları değişmeyen sahne içeriğindedir.

## 6. Açık kalanlar

| Madde | Sebep |
|---|---|
| Çakışma kapısı çıkış 1 | eski tasarımdaki hatalar (yukarıda); kapsam dışı |
| EK-11 kulak dinlemesi | Nadir'in işi |
| mp4 bayat | render yasak |
| `GRAMMAR` rozeti İngilizce | istem kapsamı yalnız `BASIC` |

---
Son Güncelleme: 16.11.2026 (DUZ2-SPANA oturumu).
