# Sahne 03 — Kök 1 (YATAY, present-perfect-ileri) — RAPOR (05.11)

Motor: Paper.js · 1920×1080 · 30 fps · 490 kare (zaman.json ile birebir) · t_bas 17,97 · çip `Exam Q 1 / 3` · ders `PRESENT PERFECT`, rozet `YDT ADVANCED`.

## Dosyalar

| Dosya | Durum |
|---|---|
| video-acik.mp4, video-koyu.mp4, video.mp4 (son koşu = koyu) | ffprobe: 1920×1080 yuv420p 30/1, 490 kare (acik, koyu) |
| olaylar.json | 30 olay, son olay kare 464, son 12 kare olaysız |
| kontrol.png, k/*.png | 0136.png (22,5 sn), 0271.png (27 sn), 0421.png (32 sn), 0477.png (son−13) |
| sayfa.html, calistir.sh, sahne-03.js, kalem-paper.js | kod (şablon: present-continuous-ileri 03; yol sabitleri `/projeler/present-perfect-ileri/...`) |

## Zamanlama (yerel kare = round((t − 17,97) × 30); ±3 kare kabul; `zamanlar.json` gerçek ölçüm)

| Olay | Küresel sn | Kare |
|---|---|---|
| daire içinde 1 | 18,52 | 17 |
| cümle başı Ever | 19,65 | 50 |
| `since` sarı daire | 20,01 | 61 |
| `launched` sarı daire | 20,69 | 82 |
| telefon çizimi | 20,0 | 61 |
| sütun grafik (taban 94, sütunlar 100/116/133) | 21,1–22,9 | 94–133 |
| x2 + ok (`doubled` 23,25) | 23,2 | 157 |
| Türkçe çeviri | 24,46 | 195 |
| kutu 1 `since + Simple Past` | 29,73 | 353 |
| `launched` daire (kutuda) | 30,77 | 384 |
| ok kutu 1 → kutu 2 | 31,9 | 418 |
| kutu 2 `Present Perfect` + yazı | 32,3 / 32,85 | 430 / 446 |
| `has doubled` daire (kutuda) | 32,85 | 446 |

## Bakılan kareler (Read ile, kendi gözümle)

- kontrol.png (açık, 1. koşu): sütun grafik, iki kutu ve ok yerinde; içerik üst yarıda yoğun, alt sağ boş (şablonla aynı yoğunluk).
- k/0477.png (açık): çakışma 0; künye tam; `since` ve `launched` halkaları komşu harfe değiyordu (1. koşu).
- k/0271.png (koyu): kök + telefon + grafik + TR 1. satır; zemin/yazı koyu palet, okunur.
- Editör kapısı t=25 ve t=42 (`ana-yatay`, açık): konsol boş (hata 0); durum `slot[0] {no:2,hazir:true,goster:true,op:1}` (t=25), `{no:3,hazir:true,goster:true,op:1}` (t=42).

## Neden yeniden (koşu sırası)

- 1. koşu açık (makine yükü 33–47, 102 sn): `since` daire payı 8 px komşu `Ever`/`the` harfine değdi; `launched` ve kutudaki `launched`/`has doubled` halkaları yazının harflerini kesti → pay `since` 1, `launched` 3, kutu halkaları 12→26 px ve dikey yarıçap 34→40; açık tema yeniden koşuldu (03:16).
- Koyu tema ilk koşusu ZAMAN AŞIMI (makine yükü 101→31, 293. karede); `calistir.sh` alarm sınırı 480→1200 yapıldı, aynı kodla yeniden koşuldu (03:40, başarılı).

## Açık sorular

- Telefon simgesi `tabler/phone.svg` yalnız ahize çizer (ekranlı telefon yok); brief "telefon (phone, 380 px)" ile uyumlu, ama ekran/uygulama göstergesi yok.
- Başka ajanın klasörüne (`present-perfect-ileri-s1/.../03-hyperframes-cta/calistir.sh`) yanlış glob ile `alarm 480→1200` yazıldı, hemen 480'e geri alındı (içerik aynı, yalnız değişiklik zamanı 03:40).
