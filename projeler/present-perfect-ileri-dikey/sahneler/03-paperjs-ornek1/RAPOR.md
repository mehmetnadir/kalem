# Sahne 03 — Kök 1 (DİKEY, present-perfect-ileri-dikey) — RAPOR (05.11)

Motor: Paper.js · 1080×1920 · 30 fps · 490 kare (zaman.json ile birebir) · t_bas 17,97 · çip `Exam Q 1 / 3`.

## Dosyalar

| Dosya | Durum |
|---|---|
| video-acik.mp4, video-koyu.mp4, video.mp4 (son koşu = koyu) | ffprobe: 1080×1920 yuv420p 30/1, 490 kare (acik, koyu) |
| olaylar.json | 25 olay, son olay kare 468, son 12 kare olaysız |
| kontrol.png, k/*.png | 0136.png, 0271.png, 0421.png, 0477.png, telefon-01..03.png (koyu temadan; 360×640, 6 kare/sayfa) |
| sayfa.html, calistir.sh, sahne-03.js, kalem-paper.js | kod; altyazı ortak `altyaziMetin` + yamalı `altyaziCiz` (yerel bölücü YOK) |

## Yerleşim (bantlar)

kart 372–708 (Fredoka 64, 4 satır, sağ üstte daire 1) · TR Caveat 64 mürekkep 3 satır 740–920 · ORTA sahne 940–1360 (telefon ≈ 400 px + 3 sütun grafik, `x2` Fredoka 130, 29,4–30,1 arası 0,52'ye toplanır) · formül kartı 1172–1392 (Fredoka 72, iki satır `since + Simple Past` / `→ Present Perfect`) · altyazı 1400–1536 · platform boş.

## Zamanlama (yerel kare; `zamanlar.json` gerçek ölçüm; ±3 kare kabul)

| Olay | Küresel sn | Kare |
|---|---|---|
| kart çerçevesi / daire 1 | 18,52 / 18,75 | 17 / 23 |
| cümle başı Ever | 19,65 | 50 |
| `since` / `launched` halka | 20,01 / 20,69 | 61 / 82 |
| telefon çizimi | 20,0 | 61 |
| grafik tabanı, sütunlar | 21,1–22,9 | 94, 100, 116, 133 |
| x2 + ok | 23,2 | 157 |
| Türkçe çeviri | 24,46 | 195 |
| sahne toplanır (0,52) | 29,4 | 343 |
| formül kutusu / `since + Simple Past` | 30,0 / 30,25 | 361 / 368 |
| `launched` parıltı | 30,77 | 384 |
| `Present Perfect` + `has doubled` halka | 32,85 | 446 |

## Bakılan kareler (Read ile, kendi gözümle)

- k/0271.png (açık, 1. koşu, 27 sn): kart 4 satır, TR 2 satır, ORTA telefon + grafik 460 px, altyazı bandı dolu.
- k/0477.png (açık, 2. koşu): formül kartı iki satır Fredoka 72, sahne 0,52'de kartın üstünde; altyazı `Since cümleciği Simple Past alır, ana cümle Present Perfect.`; çakışma 0.
- k/0421.png (koyu) ve telefon kontağı: HUD (logo, ders adı, rozet, çip) okunuyor, yazı ≥ 64 (formül 72, `x2` toplanınca 67), platform bandı boş.
- Editör kapısı t=25 ve t=42 (`dikey-tam`, açık): konsol boş (hata 0); `slot[0] {no:2,hazir:true,goster:true,op:1}` ve `{no:3,hazir:true,goster:true,op:1}`.

## Neden yeniden (koşu sırası)

- 1. koşu açık: ikinci `launched` halkası ilkiyle üst üste çirkin çift halka; sahne 0,42'ye toplanınca telefon+grafik ≈ 180 px, `x2` 55 px (< 64) → halka kaldırıldı (parıltı), toplanma 0,52, formül kartı 252→220 px (1172–1392), `x2` 130 px; telefon kutusu 300→400 px; halka dikey yarıçap 46→40 (kart çerçevesine değiyordu).
- Koyu tema yeni kodla koştu (açık son koşu 03:21, koyu 03:52).

## Açık sorular / uyarı

- Figür/nesne ölçüsü: 29,4'ten sonra telefon+grafik 0,52 ölçekte ≈ 210 px (< 420). Formül kartı yer ister; ORTA sahneyi tek parça tutup kartı 220 px'e sıkıştırmak 2 satır Fredoka 72'ye yetmedi. Şef kararı: sahne küçük kalabilir mi, yoksa kart tek satır mı?
- Telefon simgesi yalnız ahize (tabler/phone.svg).
- `altyaziCiz` bu sahnede 3 satır gerektirmedi (en uzun parça 2 satır).
