# S2-SON — huni dosyaları denetimi · 15.11.2026

## Dosyalar (paket kökü)

| Dosya | Durum | Not |
|---|---|---|
| `kapak-a.png` + `kapak.png` | üretildi | Sahne 01 `k/…-0.9.png` (t 0,9 sn, açık tema), altyazısız; iki dosya aynı (md5) |
| `kapak-b.png`, `kapak-c.png` | var | 1080×1920 |
| `hikaye-a.png` + `hikaye.png` | var | aynı dosya (md5) |
| `hikaye-b.png` | var | 1080×1920 |
| `aciklama-a.md`, `aciklama-b.md`, `aciklama.md` | var | içerik değişmedi |
| `sahneler/01-hyperframes-kapak/k/koyu/kapak-a-koyu.png` | üretildi | koyu tema 0,9 sn karesinin kopyası (Read ile bakılmadı) |
| `uretim-tutanagi/kontak/s2-huni-yanyana.png` | üretildi | 5 parça, 1800×640 |

`huni-surumler.json`: 7 satır, dosya adları eşleşir, hepsi `inceleme`. `surumler.json` kısa video `kimlik` = `s2` (zaten öyleydi).

## Bakılan kareler (Read)
kapak-a (sahne 01 karesi), kapak-b, kapak-c, hikaye-a, hikaye-b, yan yana kontak. `file`: 5 PNG + kapak-a/kapak 1080×1920.

## Denetim
- Altyazı bandı: hiçbir karede yok.
- Taşma/kesik yazı: yok. Başlıklar kapak A 2 satır (GENEL / ≠ ŞU AN), B 2 satır, C 2 satır.
- Künye (logo sol üst, YDT · BASIC rozeti) hepsinde yerinde; hikâyelerde `Full lesson` çipi ve ders adı var.
- A/B/C farklı: A figür+mont+tişört, B takvim+soru işareti, C iki örnek cümle.
- Hikâye B'de cevap ve sarı vurgu yok.

## Kusur / not
1. Bütün karelerde içerik y ≈ 1500'de biter; alt %20 boş (Shorts arayüz bölgesi için bilinçli olabilir, Nadir bakar).
2. Hikâye A'da ders adı ile `YDT · BASIC` rozeti aynı satırda, boşluk dar ama çakışma yok.
3. Kapak A'da `Genel` ile `≠ ŞU AN` hapı sol/sağ hizası kapak B/C'den farklı (A ortalı, C sola hizalı); tür farkı, kusur sayılmadı.

## Açık noktalar
- Koyu tema PNG'si kopya olarak alındı; gözle bakılmadı.
- PNG'ler `.gitignore` altında; commit gerekirse `git add -f`.
- Tutanak/test kimliği (TT-…) üretilmedi; bu iş yalnız dosya tamamlama.
