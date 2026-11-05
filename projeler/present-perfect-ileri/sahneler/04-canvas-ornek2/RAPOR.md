# Sahne 04 — Kök 2 (YATAY, present-perfect-ileri) — RAPOR (05.11)

Motor: düz canvas · 1920×1080 · 30 fps · 533 kare (zaman.json ile birebir) · t_bas 33,89 · içerik kare 521 · çip `Exam Q 2 / 3`.

## Dosyalar

| Dosya | Durum |
|---|---|
| video-acik.mp4, video-koyu.mp4, video.mp4 (son koşu = koyu) | ffprobe: 1920×1080 yuv420p 30/1, 533 kare (acik, koyu) |
| olaylar.json | 30 olay, son olay kare 504, son 12 kare olaysız |
| kontrol.png, k/*.png | 0123.png (38 sn), 0273.png (43 sn), 0423.png (48 sn), 0520.png (son−13) |
| sayfa.html, calistir.sh, sahne.js, sahne-ortak.js | kod (şablon: present-continuous-ileri 04; `kunyeCiz` etkin = 2 → ajanda `Exam`) |

## Zamanlama (kod tablosu; canvas motoru zaman logu üretmez. Kare = round((t − 33,89) × 30); sözcük zamanları `sozcukler.json`)

| Olay | Küresel sn | Kare |
|---|---|---|
| daire içinde 2 | 34,44 | 17 |
| cümle başı Selim (3 satır 5/4/5 sözcük) | 35,57 | 50 |
| `for thirty years` sarı daire | 37,13 | 97 |
| figür (sitting-5) çizimi | 36,0 | 63 |
| dizüstü (coco/laptop) çizimi | 37,8 | 117 |
| Türkçe çeviri 2 satır | 40,70 / 43,22 | 204 / 280 |
| takvim şeridi, ayraç `30 years`, `1995`, `now` | 41,0–44,2 | 213–309 |
| `has worked` sarı daire | 46,3 | 372 |
| kutu `for + süre` | 47,17 | 398 |
| kutu `since + başlangıç` | 50,29 | 492 |
| ok + `since 1995` | 50,4 / 50,55 | 495 / 500 |

## Bakılan kareler (Read ile, kendi gözümle)

- kontrol.png (açık, 1. koşu): sağ sütunda figür + dizüstü, sağ altta takvim şeridi, sol altta iki kutu; çakışma 0.
- k/0520.png (açık, 2. koşu): tüm öğeler, `since 1995` tam yazılı; künye tam.
- k/0273.png, k/0423.png (koyu): palet koyu, yazı okunur.
- Editör kapısı t=42 (`ana-yatay`, açık): konsol boş (hata 0); `slot[0] {no:3,hazir:true,goster:true,op:1}`.

## Neden yeniden (koşu sırası)

- 1. koşu açık (331 sn, makine yükü): `since 1995` etiketi son içerik karesinde (520) yarım yazılıydı (reveal 0,4 sn, 50,85'te başlıyordu) → 50,55'e çekildi; `has worked` / `for thirty years` halkaları iki satırı birbirine değiyordu → dikey yarıçap 42→38; `tabler/device-laptop.svg` yalnız boş ekran çiziyordu → `coco/laptop.svg`, kutu 390×340.
- Açık 2. koşu ve koyu koşu aynı kodla (koyu 03:34, başarılı).

## Açık sorular

- Figür `open-peeps/sitting-5` çömelmiş poz; dizüstüyle etkileşim yok (yalnız yan yana). Başka oturan figür gerekirse sitting-1/2/4/6/7 seçilebilir.
- `calistir.sh` alarm sınırı 480→1200 yapıldı (makine yükü 31–101); sahne 04 aynı sınırla başarıyla bitti.
