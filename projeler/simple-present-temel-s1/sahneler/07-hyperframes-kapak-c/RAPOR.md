# RAPOR — simple-present-temel-s1 · sahne 07-hyperframes-kapak-c (huni v2) · 15.11.2026

| Ölçüm | Değer |
|---|---|
| `calistir.sh --tema acik` | çıkış 0 · `P/kapak-c.png` PNG 1080×1920 (`file`: 8-bit RGB) |
| `calistir.sh --tema koyu` | çıkış 0 · `k/koyu/kapak-c-koyu.png` PNG 1080×1920 |
| `uret.py` | `index.html yazıldı 17330` · `S=190` · SPEC §6 assert'leri geçti |
| Çakışma kapısı | çıkış 2 · `HATA sahne bulunamadı: 07-hyperframes-kapak-c` (beklenen: araç yalnız `zaman.json → sahneler[]` okur; karede gözle ve pikselle denetlendi) |
| Metin taraması (`tam ders`, `dakika`; html/js/py) | boş (grep çıkış 1) |
| Kanal katmanı (iki kare, piksel, eşik 60) | logo mürekkebi x 60–239, y 298–330 (resim 291–339) · `@ydspublishing` x 264–596, y 296–339 (taban 330); 02-04 kapak C v2 ölçümüyle birebir |
| Künye (piksel) | yalnız rozet `YDT · BASIC`: x 60–263, y 386–433; konu adı yok |
| Boş bölgeler (piksel, eşik 60) | y 0–280: boş · y 1385–1920: boş · x 961–1080: boş · x 0–59: boş |
| İçerik (piksel) | başlık x 107–917, y 470–845 · otobüs + zemin x 68–951, y 1051–1361 |

`P` = `K/projeler/simple-present-temel-s1/`. Komutlar `PATH=~/.nvm/versions/node/v24.22.2/bin:$PATH` ile koştu.
**Not:** istem KURALLAR "calistir.sh yalnız ONIZLE_YALNIZ=1" der; Doğrula 1 ise PNG için tam koşu ister. Bu sahnenin `calistir.sh`'ı
mp4 üretmez (tek kare `hyperframes snapshot`). Doğrula 1 uygulandı; mp4 üretilmedi.

## Olay listesi
Durağan kare; ses, altyazı, çip yok. `olaylar.json` = `[]`. Çizelge 1,0 sn (HyperFrames en az), yakalama 0,5 sn; ilk = orta = son kare.
Küresel anlatım saniyesi yok (zaman çizelgesi dışı).

| Olay | Kare / sn | Cümle sözcüğü |
|---|---|---|
| kapak tam görünür (kanal, rozet x 60, başlık, `ES` hapı, otobüs, zemin çizgisi) | 0 / 0,00 → son | — (anlatımdan bağımsız) |

## Yerleşim (nesneler.json)
| Blok | x · y · w · h |
|---|---|
| kanal | 60 · 280 · 542 · 70 |
| kunye (yalnız rozet; `#rz0` x 60'a kaydı, `#ku-konu` gizli) | 60 · 360 · 204 · 90 |
| baslik (`HE GOES` / `I GO`, Fredoka 700 190; satır 2'deki `GO` satır 1'deki `GO` ile aynı x) | 102 · 470 · 816 · 403 |
| es-hap (`ES`, tek vurgu; açıkta `#ffe066` + `#1b2440`, koyuda `#f2a93b` + `#1b1a17`) | 670 · 470 · 248 · 194 |
| otobus (`coco/bus.svg`, kalem 4,4 px, ayna yok → sağa gider = okuma yönü) | 120 · 1053 · 780 · 303 |
| zc (zemin çizgisi) | 70 · 1358 · 880 · 4 |

Çiftler arası kesişim 0; başlık altı → otobüs üstü 180 px; otobüs tekerleği zemin çizgisinin 4 px üstünde. Başlık konturu yok
(02-04 kapak C açık noktası 2'deki soluk hale bu sahnede yok).

## Değişen dosyalar (hepsi bu sahne dizininde + paket kökü `kapak-c.png`)
- `SPEC.md`: şef yazdı.
- `calistir.sh`, `olay.py`, `zamanlar.json`: emsal `02-04-ydt-temel-s1/sahneler/06-hyperframes-kapak-c/` kopyası (`cp -p`); Edit: başlık yorumu, paket adı.
- `yardim.py`: aynı paketin `01-hyperframes-kanca/yardim.py` kopyası (`cp -p`; doğru `KONU`, v2 `kunye_svg()`, otobüs için `coco()`); Edit: docstring.
  Gerekçe: emsal `yardim.py`'de `KONU` = "Simple Present vs Present Continuous" ve `coco()` yok; kanca kopyası ikisini de taşır.
- `uret.py`: agy yazdı (SPEC). Şef baştan sona okudu; SPEC'e uyuyor. Düzeltme turu 1 (şef, Edit): GO–ES arası `a` 0,10·S → 0,14·S.
  Neden: karede hap `O`'ya 6 px kaldı (sıkışık); düzeltmeden sonra 14 px (satır y 566 ölçümü: `O` sonu x 655, hap başı x 669).
- Üretilenler: `nesneler.json`, `olaylar.json`, `proje/` (önizleme koyu temada son koşudan kaldı), `k/at-0.5s.png`, `k/koyu/*`, `P/kapak-c.png`.
- Silinen ya da taşınan dosya yok.

## Bakılan kareler
| Kare | Bulgu |
|---|---|
| `P/kapak-c.png` (= `k/at-0.5s.png`, açık; tek kare: ilk = orta = son) | taşma, kesik yazı, üst üste binme, boş kare YOK; 0–280 ve 1570–1920 boş; x 961+ boş; kanal + rozet tablodaki yerde; hap `#ffe066`, `ES` lacivert; otobüs sağa bakar |
| `k/koyu/kapak-c-koyu.png` (koyu, tek kare) | aynı yerleşim; kontrast iyi; hap `#f2a93b`, `ES` koyu; logo koyu tema dosyası |
| `/tmp/sp07-baslik-acik2.png` (başlık kırpığı, düzeltme sonrası) | `GO` ile hap arası boşluk okunur; iki `GO` alt alta hizalı |

## agy koşu özeti
`~/.claude/canavar/agy-filo/20261115-194731/ozet.md` — 1/1 başarılı · 188 sn · rol `kod` · gemini-3.8-flash-high · girdi 1.895.588 / çıktı 78.523 token.
Özetin "değişen" listesinde `06-hyperframes-kapak-b/*` ve `.claude/docs/sozlesme.md` da var: bunlar paralel oturumların işi; agy yalnız `uret.py` yazdığını bildirdi.

## Açık noktalar
1. Çakışma kapısı durağan kareleri ölçmez (çıkış 2). Denetim piksel ölçümü ve göz denetimiyle yapıldı.
2. Figür yok (taslak §5 ve kalıp §4 sapması; jüri madde saymadı). Karar şefte.
3. `SPEC.md` §4.2 "beklenen" sayıları `a = 0,10·S` ile hesaplandı (gb 808,1, x0 105,95); gerçek değerler yukarıdaki tabloda (gb 815,7, x0 102).
4. Platform arayüzü bölgeleri (üst 0–250, alt 1580+, sağ 960+) üçüncü taraf ölçümüdür; yayın öncesi gerçek ekranda doğrulanmadı (standart §2).
