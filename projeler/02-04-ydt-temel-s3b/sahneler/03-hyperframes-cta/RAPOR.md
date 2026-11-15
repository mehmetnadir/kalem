# Sahne 03 Çağrı (02-04-ydt-temel-s3, huni v2, HyperFrames DİKEY 1080×1920, 239 kare, t_bas 21,33; cümle 5 öğrenci) · 15.11.2026

Durum: yazıldı. `ONIZLE_YALNIZ=1` hazırlığı koşuldu (son koşu AÇIK tema). mp4 render yok. Kapı GEÇTİ (çakışma yok, çıkış kodu 0).
Tema: acik

| Dosya | Yazan | Değişiklik |
|---|---|---|
| `SPEC.md` | şef | v2 tasarımı: yerleşim, olay listesi, ekran metni, kabul ölçütü (v1 SPEC yedekte) |
| `uret.py` | agy-filo (`kod`, gemini-3.8-flash-high, 335 sn) + şef 1 satır | baştan yazıldı; v1 içeriği tamamen kalktı |
| `calistir.sh` | şef (Edit) | başlık, `KARE=239`, ana kapak kopyası `proje/assets/`, denetim kareleri |
| `yardim.py`, `olay.py`, `nesneler.json` | — | değişmedi (`yardim.py` künyesi/altyazısı kullanılmıyor) |
| üretilen | `uret.py` + `olay.py` | `proje/index.html`, `zamanlar.json` (`cagri_satir` 2), `olaylar.json` (5 olay) |

## Ana kapak kopyası
| Kaynak (ana ders, 1920×1080) | Hedef | `cmp` |
|---|---|---|
| `projeler/02-04-ydt-temel/kapak.png` (632.015 B) | `ortak/kapak/ana-kapak.png` | aynı |
| `projeler/02-04-ydt-temel/kapak-koyu.png` (634.425 B) | `ortak/kapak/ana-kapak-koyu.png` | aynı |
`cp -a` ile kopyalandı. `calistir.sh` ikisini `proje/assets/`e koyar; tema seçimi CSS ile (`.tema-acik #kapakA`).

## Yerleşim (px)
| Bölge | y | İçerik |
|---|---|---|
| Kanal (`#kunye > #kanal`) | 291–339 | logo `#logoimg` x 53,2 w 193,5 h 48 · `@ydspublishing` Lexend 700 42, x 263, taban 330; tween yok |
| Künye | 386–434 | konu Fredoka 700 34 (x 60, taban 420, son x 644,6) + rozet `YDT · BASIC` (x 664,6, w 203,6) |
| Giriş sözü | ≈ 490–582 | `Bu sadece başlangıç.` Fredoka 700 96, x 60, taban 560 (890,9 px) |
| Kapak kartı | 620–1126 | 900×506, x 60, rx 24, çerçeve `murekkep` 3 px; oynat düğmesi/çubuk/süre yok |
| Çağrı | 1160–1346 | hap `@ydspublishing` (x 60, w 580,4, h 104; Lexend 700 64) / `YouTube` (x 60, taban 1346). Tek satır 946,6 px > 900 → iki satır |
| Altyazı + karaoke | 1430–1529 | Lexend 500 44, orta x 510, 2 satır (taban 1462/1518); okunmamış sözcük `ikincil`, okunan `murekkep` |

## Olay listesi
| Olay | Küresel sn | Yerel kare | Sözcük |
|---|---|---|---|
| Kanal + künye tam | 21,33 | 0 | sahne başı |
| Kapak kartı girer (opaklık + ölçek 0,96→1, 0,40 sn) | 21,33 | 0 | sahne başı |
| `Bu` kinetik · ses `tik` 0,40 | 21,88 | 16 | `Bu` |
| `sadece` kinetik | 22,12 | 24 | `sadece` |
| `başlangıç.` kinetik · ses `tik` 0,45 | 22,68 | 40 | `başlangıç.` |
| Altyazı parça 0 / parça 1 | 21,83 / 23,74 | 15 / 72 | `Bu` / `Dersin` |
| Hap kalem çizgisi (0,30 sn) · ses `cizgi` 0,50 | 25,07 | 112 | `YDS` |
| Hap yazısı kalemle yazılır (→ 26,11) · ses `hisirti` 0,45 | 25,17 | 115 | `YDS` → `Publishing` |
| Hap dolgusu (0,15 sn) | 25,27 | 118 | `YDS` |
| `YouTube` kinetik · ses `tik` 0,50 | 26,19 | 146 | `YouTube` |
| Durgun kuyruk (tween yok) | 27,31 → son kare | 179 → 238 | `kanalında.` sonu |

## Kapı ve QA
`bash araclar/qa-yerel.sh 02-04-ydt-temel-s3 03-hyperframes-cta 21.33,24.82,28.28 27.0 --hazirla` (2. koşu, düzeltme sonrası):
```
== KAPI
03-hyperframes-cta | çakışma yok (29 örnek, 5038 kutu)
== KARE (açık)  21.33 · 24.82 · 28.28
== KARE (koyu)  27
kapı çıkış kodu: 0
```
Metin taraması `grep -rniE "tam ders|dakika" …/03-hyperframes-cta/proje` → sonuç yok (rc 1).

## Kanal katmanı ölçümü (PIL, mürekkep kutusu)
| Kare | Logo (x0, y0, x1, y1) | `@ydspublishing` |
|---|---|---|
| açık 21,33 | 61, 298, 240, 331 | 265, 296, 596, 340 |
| açık 24,82 | 61, 298, 240, 331 | 265, 296, 596, 340 |
| açık 28,28 | 61, 298, 240, 331 | 265, 296, 596, 340 |
| koyu 27,00 | 60, 298, 240, 331 | 264, 296, 596, 340 |
Görünür sol kenar x 60; resim kutusu y 291–339. Dört karede de aynı konum. y 0–280, 1570–1920 ve x 962–1080: dört karede boş.

## Bakılan kareler ve bulgu
| Kare | Bulgu |
|---|---|
| açık 21,33 | yalnız kanal + künye (kapak girişi 0. karede başlar); zemin açık |
| açık 24,82 | kapak (açık), giriş sözü, altyazı 2 satır: `Dersin tamamı` okunmuş, kalanı soluk |
| açık 28,28 | kapak, giriş sözü, sarı hap + `YouTube`; altyazı yok (27,74'te kapandı); son kare = tam düzen |
| koyu 27,00 | koyu kapak (`kapakK`), hap, `YouTube`, altyazı tam okunmuş |
Taşma, kesik yazı, üst üste binme yok. Kontrast iki temada yeterli.

Düzeltme turu 1 (şef, Edit): ilk koşuda açık karelerin zemini koyu kaldı. Sebep: kapak CSS'indeki `#root.tema-acik` dizgesi
`ortak/hf_tema.py` içindeki "tema CSS'i zaten var" denetimini (`"#root.tema-acik" not in html`) tetikledi, değişken CSS'i eklenmedi.
Seçici `.tema-acik #kapakA` yapıldı; 2. koşuda dört kare doğru.

## agy koşusu
Özet: `/home/sef/.claude/canavar/agy-filo/20261115-184909` (1/1 başarılı, 335 sn). agy-filo "değişen 87" listesi başka oturumun
`projeler/02-04-ydt-temel-dikey/` dosyalarını da sayar (aynı worktree'de eş zamanlı iş); bu sahne dışında dosyaya dokunmadım.

## Açık noktalar
- `k/` içinde v1 QA kareleri duruyor (`18.7`, `23`, `26.4`, `koyu/25.8`); silme yasağı yüzünden yerinde. Yedekleri
  `~/Silinecekler/2026-11-15-huni-v2/02-04-ydt-temel-s3/sahneler-v1/03-hyperframes-cta/k/` altında; taşıma kararı şefte.
- Ana kapak görseli sarı; kapakla `@ydspublishing` hapı aynı karede iki sarı alan (kapak dosyanın kendisi, vurgu kuralı dışı).
- Açık temada hap çizgisi `vurgu` `#d9900f`, dolgu `#ffe066`: hapın koyu sarı kenarı kalır (koyu temada çizgi ve dolgu aynı renk).
- Kare 0'da kapak opaklığı 0 (giriş 0,00–0,40 sn); sahne geçişi (BookFlip, 12 kare) bu aralığı örter.
