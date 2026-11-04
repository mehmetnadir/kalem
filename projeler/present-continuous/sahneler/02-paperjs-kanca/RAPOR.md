# Sahne 02 — Kanca (Paper.js, 385 kare, t_bas 3,00; 04.11 K23: 445 → 385, cümle 2 sonrası 60 kare öne, cümle 1 yazısı 0–0,4 sn hazır belirir)

## Yapılan
- `kalem-paper.js`: ortak modül (kalem darbesi geometrisi, SVG→darbe, sözcük belirme, alt çizgi, daire, ok, kutu, tik, parıltı, olay günlüğü). Sahne 03 de buradan import eder.
- `sahne-02.js` içerik, `sayfa.html` sürücü, `calistir.sh` hat. Künye `kunye.js`'ten (`Hook`, etkin 0), kare 0'dan sabit.
- Çıktı: `video.mp4` (ffprobe: 1920×1080, yuv420p, 30 fps, 385 kare), `olaylar.json`, `zamanlar.json`, `kontrol.png`, `k/*.png`.

## Zamanlama (BRIEF satırı → gerçek yerel kare)
| BRIEF | Beklenen | Gerçek |
|---|---|---|
| Bu / akşam / amcamlara / gidiyorum | 0 / 7 / 19 / 38 | 0 / 7 / 19 / 38 |
| Ev + yürüyen figür çizimi (7,2–8,8 sn) | 6–54 | 12–54 (geçiş altında boş kalsın diye 6 kare geç) |
| Hilal | ≈ 8,0 sn | 30–60 |
| gidiyorum sarı daire (9,39) | 72 | 72 |
| `-yor → şimdiki zaman` | 96 | 96 (`-yor`), 112 (`şimdiki zaman`) |
| Takvim (11,15) | 125 | 125 |
| `bu akşam → gelecek` | ≈ 139 | 139–157 |
| `I'm going to my uncle's tonight.` (12,50–) | 165 | 165 (altı sözcük 165–199) |
| `going` daire | ≈ 13,2–13,6 sn | 191 |
| `-yor ⇄ -ing` oku | 12,5–14,58 sn | 213 |
| El kutusu / saat + `6 min` (14,73) | 232 | 224 / 232 |
| form (16,97) · time expressions (17,65) · 6 uses (19,29) | 299 · 319 · 369 | 299 · 319 · 369 |
| Durgun son 12 kare | 433–444 | zaman 432'de donar (olay da yok) |

## Kontrol anları (`k/`)
8,5 sn = `k/0045.png` · 13,5 sn = `k/0195.png` · 19,5 sn = `k/0375.png` · son−13 = `k/0432.png`. `kontrol.png`: 0, 89, 178, 267, 356, 432.

## Sayılar
- Darbe: 43. Olay: 29 (cizgi 18, tik 7, parilti 4), aynı karede en çok 2, hepsi kare 0–373.
- Hareketsiz süre: figür nefesi (6 sn'de 1,00→1,012), saat ve hilal parıltısı 3 kez tekrarlar; olaysız en uzun aralık 2,1 sn.

## Görsel denetim bulguları (2 tur + 1 son)
1. Tur 1: figür ve gövde yolları görünmedi (`CompoundPath` çocuklarında dolgu yok, süzgeç attı). Süzgeç ebeveyn stilini okuyacak şekilde düzeltildi.
2. Tur 1: `gidiyorum` dairesi takvim ikonuna değiyordu, `going` dairesi komşu sözcüklere taşıyordu. Daire yarıçapı daraltıldı, takvim 24 px aşağı alındı ve 88 px yapıldı.
3. Son kontrol: çakışma yok, güvenli alan (56 px) içinde, künye tam, yazılar okunur. Sol altta büyük boş alan var (BRIEF yerleşimi sağ alt kutu istiyor).
4. Son 12 karede olay kaydı yazılmıyor (içerik durgun).

## Açık sorular
- `Bu` sözcüğü kare 0'da başlıyor (sözcük zamanı). BRIEF §1 geçişte tuval boş olsun der; çelişki var, zamanı seçtim. Geçiş altında ilk 4 karede "Bu" belirir.
- Caveat `->` oku yerine her ok kalemle çizildi (yazı tipinde ok glifi yok). Yön `ev` yönüne yürüyen figür: SVG figür önden bakıyor, kayma 70 px sağa.
- İngilizce cümle `y 520` yerine 570 (takvim notlarıyla çakışmasın diye 50 px aşağı).
- Figür yolları dolgu şekillerinin dış çizgisi: görünüm "röntgen" (örtülü parçalar da çizili). Peeps için en çok 60 darbe sınırında sade kaldı.

## Çalışmayan
Yok. `rm` yasağı nedeniyle `calistir.sh` geçici kareleri `~/Silinecekler/2026-11-04-kalem/` altına taşır.
