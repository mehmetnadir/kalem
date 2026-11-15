# Sahne 06 · kapak C — karşıt çift (HyperFrames, 1080×1920, tek kare, ses yok, zaman çizelgesi dışı)

Tema: acik

Durum: yazıldı ve iki temada yakalandı (15.11.2026, istem D-S3). mp4 yok. `zaman.json` → `duragan` kaydı (kare 1, `kapak-c.png`); `sahneler[]` dışında.
Çıktı: `../../kapak-c.png` (açık, paket kökü) · `k/koyu/kapak-c-koyu.png` (koyu) · `k/at-0.5s.png` (açık ham kare).

## Olay listesi
Ses ve hareket yok: `olaylar.json` = `[]`, çizelge 1,0 sn, yakalama 0,5 sn (`zamanlar.json`). Küresel saniye yok (anlatıma bağlı değil).
Öğeler (y px, `nesneler.json` ile aynı):

| Öğe | Yer | Değer |
|---|---|---|
| HUD | 0–288 | logo sol üst (48, 48, 387×96) · rozet `YDT · BASIC` (48, 216, h 72); çip yok, ders adı yok, altyazı yok |
| Başlık | 358–786 | `İKİ ÖRNEK` (mürekkep, kontur 12) / `İKİ ZAMAN` sarı kutuda (dolgu `vurgu` → açıkta `#ffe066`, yazı → `#1b2440`); Fredoka 700 S = 190 (üst sınır), blok 944 px ≤ 952 |
| Kart 1 | 884–1084, x 64–880 | lokomotif ikonu (131×108) · `The train leaves …` Fredoka 700 72; **`leaves` sarı hapta (tek kart vurgusu)** |
| Kart 2 | 1124–1324, x 64–880 | sinema bileti ikonu (131×51) · `I am going …` Fredoka 700 72; vurgusuz |
| Figür | 984–1324, x 911–1016 | öğretmen (`kadro.ogretmen` ShirtPantsWB / Smile / Short), 340 px, kısa zemin çizgisi 1324 |
| Boş | 1344–1920 | öğe yok |

Can alıcı `canAlici[1]` (tarifeli gelecek V-s → `leaves`) + `[2]` (planlanmış gelecek am + V-ing → `am going`): iki kart (S3-duzeltme madde 5).
Eski başlık `İKİSİ DE` / `GELECEK` kullanılmadı (madde 1). `İKİ` Türkçe İ, elle büyük harf; `text-transform` yok.

## Kapı sonucu
qa-yerel, çakışma kapısı ve sahne-kare koşulmadı (istem: sahne `sahneler[]` dışında, anlatım zamanı yok). Kapı = `uret.py` assert'leri
(kesişim 0, aralar, bant sınırı ≤ 1344, içerik bandı üstü ≥ 352, kart eşitliği, hap boşluğu, renk kümesi 4 hex, yasak metin) + yakalama + `ffprobe`.

```
$ ONIZLE_YALNIZ=1 bash calistir.sh            → index.html yazıldı 25994 · S=190 · olay 0 · önizleme hazır (rc 0)
$ bash calistir.sh --tema koyu                → png,1080,1920 · …/k/koyu/kapak-c-koyu.png (rc 0)
$ bash calistir.sh --tema acik                → png,1080,1920 · …/02-04-ydt-temel-s3/kapak-c.png (rc 0)
```
Son koşu açık tema: `proje/index.html` açık temada kalır.

## Bakılan kareler
| Kare | Tur | Bulgu |
|---|---|---|
| `../../kapak-c.png` (açık) | 1 | taşma, kesik yazı, binme yok; İ noktaları sarı kutunun içinde; başlık üstü 344 (kontur 338) içerik bandı üstü 352'yi 14 px aşıyor → düzeltildi |
| `k/koyu/kapak-c-koyu.png` | 1 | aynı yerleşim; turuncu kutu üstünde koyu yazı okunur; çizgiler açık renkte |
| `../../kapak-c.png` (açık) | 2 | başlık 358–786, kontur dahil 352; kartlara ara 98; 1344 altı boş; kontrast iyi |
| `k/koyu/kapak-c-koyu.png` | 2 | aynı; sorun yok |

Düzeltme turu: 1 (şef Edit: `T1 = 358 + 0,93·S`, assert `başlık üstü − 6 ≥ 352`; SPEC.md §4.2 güncellendi).

## agy koşusu
`agy-filo tek --rol kod` · gemini-3.8-flash-high · 258 sn · başarılı · özet `/home/sef/.claude/canavar/agy-filo/20261115-124819/ozet.md`.
Şef `uret.py`'yi baştan sona okudu: SPEC'e uyuyor; büyük düzeltme gerekmedi.

## Açık noktalar
1. **Logo yeri.** İstem ve BRIEF-S3 "logo sol alt (y ≈ 1478)" der; aynı istem "1344–1920 boş" der. BRIEF-DIKEY §0 (Nadir bulgusu):
   "logo HUD sol üst, alt bantta logo yok". S1 kapak C aynı çelişkiyi logo sol üst ile çözdü (S1 `kapak-taslak.md` §5–§6 HUD satırı).
   Bu kare de logo sol üstte. Alta almak geri alınabilir: `kunye_svg()` logo y.
2. **Tren = yalnız lokomotif.** Yandan tam tren (oran ≈ 2,46 : 1) 816 px karta 72 px cümleyle birlikte ≈ 131 × 53 px'e iner.
   Lokomotif + duman (oran ≈ 1,2 : 1) aynı genişlikte 108 px yükseklik verir. Kapak A ve sahne 02 tam treni kullanırsa ikon farklı görünür.
3. Kart 2 metni 640 px'te biter; kartlar "aynı boy" kuralıyla eşit, sağda boşluk kalır.
4. Sarı dolgu 3 yerde: rozet, başlık kutusu, `leaves` hapı (BRIEF-S3 tarifi). Kart içindeki tek vurgu `leaves`.
5. agy spec'e karşın `uret.py`'yi bir kez koştu (yalnız `proje/index.html` + `nesneler.json`; render yok). Sonraki şef koşuları üstüne yazdı.
6. agy özetindeki "değişen" listesi paralel oturum dosyalarını gösterir (S2 sahneleri, `sozlesme.md`); bu sahne onlara dokunmadı.
7. `hyperframes check` koşulmadı (istem kapısı yakalama + göz).
8. `ortak/__pycache__/hf_tema.cpython-310.pyc` 12:51:43'te oluştu (agy koşusu sırasında; şef koşuları 12:52'den sonra). Kaynağı
   kesin değil (agy ya da paralel oturum); önbellek dosyası, zararsız. Dokunulmadı.

Dosyalar: `uret.py` (agy), `SPEC.md` (şef), `yardim.py` + `calistir.sh` + `olay.py` + `zamanlar.json` + `cizim/ogretmen.json` (S1 kapak C kopyası), `cizim/KAYNAK.md`.
