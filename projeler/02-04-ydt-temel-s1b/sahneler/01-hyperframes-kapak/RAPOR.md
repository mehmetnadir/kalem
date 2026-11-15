# Sahne 01 · kanca kol b (02-04-ydt-temel-s1b; HyperFrames DİKEY 1080×1920, 87 kare, 0,00–2,50 sn + 12 kare geçiş payı)

| Ölçüm | Değer |
|---|---|
| Durum | yazıldı (istem KBC-0204S1, 15.11.2026, srv21). Önizleme hazırlığı `ONIZLE_YALNIZ=1`. mp4 yok, commit yok |
| Değişken | kanca: kol a `kopru` → kol b `soru` ("Bu iki yaşıyorum aynı mı?") |
| Çakışma kapısı | çıkış 0 · `01-hyperframes-kapak \| çakışma yok (11 örnek, 2674 kutu)` |
| Kapak A | `kapak-a.png` = `kapak.png` (md5 `5c996114…`), `k/koyu/kapak-a-koyu.png` (`7552886e…`); t 1,75; altyazısız |
| Ana rapor | `../../uretim-tutanagi/KBC-RAPOR.md` (ses, süre, fark sınıflaması, kapı) |

## Olay listesi (küresel sn = yerel sn; çapa `sozcukler.json` cümle 1)
| Olay | sn | Çapa |
|---|---|---|
| kapak tam: kanal, rozet x 60, `YAŞIYORUM` / `AYNI MI?` hap (B 152), ev, figür 280 + bavul, yer çizgisi | 0,00 | söz öncesi |
| `YOR` altına sarı altçizgi (`cizgi`) | 0,30–0,80 | söz öncesi |
| altyazı `Bu iki yaşıyorum aynı mı?` | 0,45 → | Bu − 0,05 |
| satır 1 `İstanbul'da yaşı-yor-um.` kırpma (`hisirti`) | 0,50–0,80 | Bu |
| satır 2 `Amcamla yaşı-yor-um.` kırpma (`hisirti`) | 0,74–1,04 | iki |
| iki `yor` kutusu soldan sağa (`tik` × 2) | 1,06–1,26 · 1,21–1,41 | yaşıyorum |
| KAPAK KARESİ | 1,75 | — |
| başlık solar 0,18 · çizim solar 0,40 · rozet x 60 → 665 0,35 | 1,86 → | aynı |
| satırlar kutularıyla 920 / 1040 → 560 / 680 (`parilti`) | 1,92–2,42 | aynı + 0,06 |
| konu adı açılır (`tik` kare 71) | 2,18–2,41 | aynı + 0,32 |
| durgun = sahne 02 kare 0 hâli; son 12 kare geçiş altında | 2,42–2,90 | → sahne 02 |

`uret.py` denetimleri: başlık/hap sınırları, satır–hap ≥ 24, satır 2–figür ≥ 24, satır 2–ev ≥ 24, kutu bandı, zaman sırası
(satır 2 < kutu < kapak_t < aynı), hareket ≤ 2,50, kayma örneklemesi (başlık görünürken satır 1 hapın altında; konu görünürken rozet sağda).

## Bakılan kareler
| Kare | Bulgu |
|---|---|
| k/0, 0.9, 1.3, 1.75, 2.2, 2.5 · k/koyu/1.75, 2.2 · k/ka-acik, k/ka-koyu | taşma, kesik yazı, okunmaz kontrast YOK; 0–280 ve 1570–1920 boş; kanal katmanı her karede aynı yer |
| 2,5 (sahne 01) ↔ 2,5 (sahne 02) | fark kol a 01→02 ek yeriyle aynı düzeyde (satır bandı 5.567 ↔ kol a 5.591 piksel; HF ↔ canvas yazı işlemesi) |

Kol a sürümü (v2 kapak raporu): `02-04-ydt-temel-s1/sahneler/01-hyperframes-kapak/RAPOR.md`.
