# Sahne 04 Çağrı — huni v2 (simple-present-temel-s3, HyperFrames DİKEY 1080×1920, 239 kare, t_bas 18,10; cümle 4 öğrenci)

| Kapı | Sonuç |
|---|---|
| Ana kapak (standart §7 madde 5) | `ortak/kapak/ana-kapak.png` md5 `b51ced1b…` · `ana-kapak-koyu.png` md5 `7b56e671…` (ana ders `kapak*.png` ile aynı) |
| `ONIZLE_YALNIZ=1 bash calistir.sh --tema acik` | çıkış 0 · `olay 4` · `önizleme hazır` |
| `qa-yerel.sh … 18.15,21.60,25.00 25.00 --hazirla` | çıkış 0 · `04-hyperframes-cagri \| çakışma yok (29 örnek, 4974 kutu)` · `kapı çıkış kodu: 0` |
| `cakisma-kapisi.mjs --sahne 04-hyperframes-cagri` | çıkış 0 · `çakışma yok (29 örnek, 4974 kutu)` · 0 uyarı |
| `grep -rniE 'tam ders\|dakika'` (html/js/py) | boş (grep çıkış 1) |
| Kanal katmanı (piksel ölçümü, 4 kare: 18,15 · 21,60 · 25,00 · koyu 25,00) | 4 karede aynı: logo mürekkebi x 60–239, y 298–330 (resim kutusu 53,2–246,7 × 291–339) · `@ydspublishing` x 264–595, y 296–339 (taban 330) |
| Boş bölgeler (piksel ölçümü, 4 kare) | 0–280: 0 piksel · 1570–1920: 0 piksel · sağ 963–1080 (y 280–1570): 0 piksel |

Durum: yazıldı, önizleme hazır (son hazırlık AÇIK tema). Render yok. Commit yok.

## Dosyalar
- `SPEC.md` (şef) → `uret.py` (agy, tek koşu; şef baştan sona okudu, düzeltme gerekmedi).
- Kopya + Edit (emsal `02-04-ydt-temel-s1/sahneler/03-hyperframes-cta/`): `yardim.py` (docstring + `KONU = "Simple Present"`),
  `olay.py` (docstring), `calistir.sh` (başlık, `KARE=239`, `uret.py`/`olay.py` iki ayrı satır, denetim kareleri), `nesneler.json`.
- Üretilen: `proje/index.html`, `zamanlar.json`, `olaylar.json` (4 ses olayı), `k/*.png`.

## Yerleşim
| Öğe | Yazı · boy | Konum |
|---|---|---|
| Kanal | logo + `@ydspublishing` Lexend 700 42 | BRIEF-S3 tablosu; `#kunye > #kanal`, opaklık 1, animasyon yok |
| Künye | konu `Simple Present` Fredoka 700 34 + rozet `YDT · BASIC` Lexend 700 26 | taban 420; hap 386–434 |
| `Bu sadece başlangıç.` | Fredoka 700 96 (900 px'e sığan en büyük; 891 px) | x 60–951, taban 560 (mürekkep y 490–≈583) |
| Ana kapak kartı | 16:9 900×506 | x 60–960, y 620–1126, köşe 24, mürekkep kenar 4 px kalemle çizilir |
| `@ydspublishing` hapı + `· YouTube` | Lexend 700 56 | hap x 60–568, y 1180–1260 (tek vurgu); `· YouTube` x 586–871, taban 1240 |
| Konuşma balonu altyazı + karaoke | Lexend 500 44 | balon x 122 (kuyruk ucu 64), y 1404–1546; sarma 760 px; okunan sözcük altında vurgu çizgisi |

## Olay listesi (yerel sn = küresel − 18,10; zaman `sozcukler.json` cümle 4 çapasından, `T(i, bas)` assert'li)
| Olay | Kare · yerel (küresel) | Cümle 4 sözcüğü |
|---|---|---|
| `Bu` kinetik (y +24→0, 0,22 sn `back.out(1.6)`) | 16 · 0,55 (18,65) | Bu |
| `sadece` kinetik | 24 · 0,79 (18,89) | sadece |
| `başlangıç.` kinetik | 40 · 1,35 (19,45) | başlangıç. |
| kart çerçevesi kalemle çizilir (0,40 sn `sine.inOut`) | 74 · 2,46 (20,56) | Dersin |
| kapak görseli belirir (0,30 sn), sonra sabit | 74 · 2,46 (20,56) | Dersin |
| `@ydspublishing` hapı girer (ölçek 0,9→1, 0,30 sn) | 112 · 3,74 (21,84) | YDS |
| `· YouTube` girer (x −12→0, 0,30 sn) | 146 · 4,86 (22,96) | YouTube |
| durgun kuyruk | 182 · 6,06 (24,16) → 239 | kanalında. sonu |

Ses olayları (`olaylar.json`): kare 16 tik 0,4 · 74 cizgi 0,5 · 112 tik 0,6 · 146 tik 0,4.
Altyazı balonu: yalnız cümle 4; `al0` 0,50–2,41 (`Bu sadece başlangıç.`), `al1` 2,41–6,41 (`Dersin tamamı YDS Publishing` /
`YouTube kanalında.`). Balon grupla açılır/kapanır; karaoke çizgisi her sözcüğün t0'ında 0,15 sn'de çizilir.

## Bakılan kareler
| Kare | Bulgu |
|---|---|
| `k/04-hyperframes-cagri-18.15.png` | yalnız kanal + künye; içerik bandı boş (ilk söz 18,65). Taşma yok. |
| `k/04-hyperframes-cagri-19.6.png` (ek) | başlık tam; balon tek satır, `başlangıç` altında karaoke. |
| `k/04-hyperframes-cagri-20.68.png` (ek) | kart çerçevesi üst kenarda çiziliyor, kapak görseli yarı saydam; balon 2 satır, `Dersin` karaoke. |
| `k/04-hyperframes-cagri-21.6.png` | kart tam (çerçeve kapalı); hap henüz yok; `tamamı` karaoke. Üst üste binme yok. |
| `k/04-hyperframes-cagri-22.png` (ek) | hap girdi; `YDS` karaoke; `· YouTube` henüz yok. |
| `k/04-hyperframes-cagri-25.png` | son kare: bütün öğeler tam; balon kapalı (kuyruk). |
| `k/koyu/04-hyperframes-cagri-25.png` | koyu zemin, koyu kapak (`ana-kapak-koyu.png`) yüklendi; hap ve rozet koyu vurgu dolgusu; kontrast okunur. |

## agy koşu özeti
- uret.py: `/home/sef/.claude/canavar/agy-filo/20261115-193426` (gemini-3.8-flash-high, başarılı, 250 sn).
- Not: özetin "değişen" listesinde `.claude/docs/sozlesme.md` ve `02-04-ydt-temel-s3/sahneler/08-hyperframes-kaydet/*` var; o dosyalar
  aynı çalışma ağacındaki paralel oturumlarındır (konu 02-04-s3 kaydet sahnesi), bu koşu yazmadı.

## Açık noktalar
- Sahne başında (kare 0–16) içerik bandı boş; ilk söz 18,65'te. Geçiş (`gecis_kare` 12) kare 0–11'i örter; kare 12–16 (0,13 sn) yalnız kanal + künye görünür.
- Ana kapakta rozet `YDT · TEMEL`, künyede `YDT · BASIC` (BRIEF değeri). Aynı karede iki farklı seviye adı görünür; karar şefte (emsal S1 ile aynı nokta).
- İstemde `kanalında.` 23,36–24,08 yazar; `sozcukler.json` t1 24,16 verir. Kuyruk veriden (24,16) başlar; sahne sonu `zaman.json` (239 kare) değişmedi.
- Balon geometrisi BRIEF'te yok: x 122, h 142, sarma 760 şef seçimi (ana ders s06 balon yolu).
- Cümle 3 parçası (`Bir arkadaşına gönder; …`) 18,18'de biter (sahne başından 0,08 sn sonra); bu sahne yalnız cümle 4 altyazısını gösterir (emsal ile aynı).
- `k/` içinde istem dışı 3 ek kare (19,6 · 20,68 · 22) durur: çerçeve çizimi ve balon geçişi için çekildi.
