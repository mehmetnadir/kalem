# Sahne 04 Çağrı — huni v2 (simple-present-temel-s1, HyperFrames DİKEY 1080×1920, 218 kare, t_bas 17,74; cümle 4 öğrenci)

| Kapı | Sonuç |
|---|---|
| `qa-yerel.sh simple-present-temel-s1 04-hyperframes-cagri 17.80,20.90,23.95 23.95 --hazirla` | çıkış 0 · `04-hyperframes-cagri \| çakışma yok (26 örnek, 3880 kutu)` · `kapı çıkış kodu: 0` |
| `cakisma-kapisi.mjs … --sahne 04-hyperframes-cagri --port 41333 --sunucu 41022` | çıkış 0 · `04-hyperframes-cagri \| çakışma yok (26 örnek, 3880 kutu)` · 0 uyarı |
| `grep -rniE 'tam[ ]ders\|dak[i]ka'` (html/js/py) | boş (grep çıkış 1) |
| Kanal katmanı (piksel ölçümü, 4 kare) | 4 karede aynı: logo mürekkebi x 60–239 (koyu 61–239), y 298–330 (resim kutusu 53,2–246,7 × 291–339) · `@ydspublishing` x 265–595, y 296–339 (taban 330) · künye x 60–512, y 386–433 |
| Boş bölgeler (piksel ölçümü, 4 kare) | 0–280 boş · 1570–1920 boş · sağ 963–1080 (y 280–1570) içerik yok · içerik 490–1239 · altyazı 1421–1511 |

Durum: yazıldı, önizleme hazır (`ONIZLE_YALNIZ=1`, son hazırlık AÇIK tema). Render yok. Commit yok.

## Dosyalar
- `SPEC.md` (şef): tasarım, olay listesi, kod yolu.
- `uret.py`, `olay.py`, `calistir.sh`: emsal `projeler/02-04-ydt-temel-s1/sahneler/03-hyperframes-cta/` (RAPOR "huni v2") `cp -p` kopyası; Edit yalnız belge dizesi ve yorumlar (paket adı, sahne no, t_bas 17,74, denetim karesi küresel saniyeleri).
- `yardim.py`: aynı paketin `03-hyperframes-kaydet/yardim.py` (v2, `KONU = "Simple Present"`) `cp -p` kopyası; Edit yalnız belge dizesi.
- Gerekçe: cümle 4 iki pakette aynı 8 sözcük (`Gerisi 18,29 · bizde. 18,77 · Dersin 19,48 · tamamı 20,04 · YDS 20,76 · Publishing 21,44 · YouTube 21,88 · kanalında. 22,28–23,08`), altyazı 2 parça, kare 218. Emsal `uret.py` zamanı `zaman.json` (klasör adı) ve `sozcukler.json` çapasından okur (`T(i, bas)` assert'li); sabit saniye yok.
- Üretilen: `proje/index.html`, `zamanlar.json`, `olaylar.json` (4 ses olayı), `k/*.png`, `k/koyu/*.png`.
- Ana kapak: `ortak/kapak/ana-kapak.png`, `ana-kapak-koyu.png` var (1920×1080); `calistir.sh` ikisini `proje/assets/`a kopyalar.

## Olay listesi (yerel kare = round((t − 17,74) × 30))
| Olay | Kare · yerel (küresel) | Cümle 4 sözcüğü |
|---|---|---|
| ana kapak kartı girer (ölçek 0,94→1 0,50 sn + saydamlık 0,25 sn) | 0 · 0,00 (17,74) → 18,24 | sahne başı |
| `Gerisi` kinetik | 16 · 0,55 (18,29) | Gerisi |
| `bizde.` kinetik | 31 · 1,03 (18,77) | bizde. |
| `@ydspublishing` sarı hapı girer | 91 · 3,02 (20,76) | YDS |
| `· YouTube` girer | 124 · 4,14 (21,88) | YouTube |
| durgun kuyruk | 160 · 5,34 (23,08) → 218 | kanalında. sonu |

Ses olayları (`olaylar.json`): kare 12 vurus 0,6 · 16 tik 0,4 · 91 tik 0,6 · 124 tik 0,4.
Altyazı: yalnız cümle 4 (2 parça); karaoke çizgisi her sözcüğün t0'ında 0,15 sn'de çizilir, sonraki sözcükte söner.

## Yerleşim
| Öğe | Yazı · boy | Konum |
|---|---|---|
| Kanal | logo + `@ydspublishing` Lexend 700 42 | BRIEF tablosu; `#kunye > #kanal` (`#logoimg`), opaklık 1, animasyon yok |
| Künye | `Simple Present` Fredoka 700 34 + rozet `YDT · BASIC` Lexend 700 26 | taban 420; hap 386–434 |
| `Gerisi bizde.` | Fredoka 700 96 | x 60, taban 560 (ölçüm y 490–560) |
| Ana kapak kartı | 16:9 | x 60–960, y 620–1126, köşe 24, `murekkep` kenar 4 px |
| `@ydspublishing` hapı + `· YouTube` | Lexend 700 56 | hap x 60–568, y 1160–1240 (tek vurgu; açık temada `vurguDolgu` / `pilMetin`); `· YouTube` x 586 (mürekkep 588–856), taban 1220 |
| Altyazı + karaoke | Lexend 500 44 | 1400–1550, orta x 510, en çok 2 satır |

## Bakılan kareler
| Kare | Bulgu |
|---|---|
| `k/04-hyperframes-cagri-17.8.png` | kanal + künye tam; kart girişte (yarı saydam, küçük ölçek). Taşma yok. |
| `k/04-hyperframes-cagri-20.9.png` | `Gerisi bizde.`, kart, sarı hap; altyazı 2 satır x 81–936, `YDS` altında karaoke çizgisi. `· YouTube` henüz yok (sözcük 21,88). |
| `k/04-hyperframes-cagri-23.95.png` | son kare: bütün öğeler tam; altyazı kapalı (kuyruk). Kartta `GİDER = GOES` başlığı ve karakter görünür. Üst üste binme yok. |
| `k/koyu/04-hyperframes-cagri-23.95.png` | koyu zemin; koyu kapak (`ana-kapak-koyu.png`) yüklendi; hap ve rozet koyu vurgu dolgusu; kontrast okunur. |

## agy koşu özeti
- agy koşusu yok. Yazılacak yeni kod satırı çıkmadı: emsal v2 kodu bu sahnenin verisiyle birebir çalışır (istem: emsal `cp -p` + kısa Edit).

## Açık noktalar
- `· YouTube` `YDS` çapasında değil, `YouTube` çapasında (21,88) girer. İstem "`@ydspublishing · YouTube` … `YDS` çapasında" der; BRIEF "ekran metni sesten önce gelmez" kuralı ve emsal bu ayrımı ister. Karar şefte.
- Ana kapakta rozet `YDT · TEMEL`, künyede `YDT · BASIC` (BRIEF değeri). Aynı karede iki seviye adı görünür (emsal 02-04-s1 s03 ile aynı açık nokta).
- Sahne başında (kare 0–7) kart henüz saydam; geçiş (`gecis_kare`) bu aralığı örter. mp4 birleştirmede bakılmalı.
- `K/.claude/docs/sozlesme.md` dosyasına 1 satır eklendi (çağrı sahnesi kod yolu).
