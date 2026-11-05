# PRESENT PERFECT İLERİ dikey · sahne 05 Kök 3 / tuzak (düz canvas, 1080x1920) — RAPOR (05.11.2026)

Tema: acik + koyu (ikisi de koşuldu; `video-acik.mp4` + `video-koyu.mp4`; `video.mp4` = son koşu).

## Yapılan
- Sıfırdan 9:16 (`sahne.js`): kart 984 px (içinde rozet `3`, kırmızı `TUZAK`, cümle Fredoka 64, 3 satır, `two hours ago` kırmızı alt çizgi, `hasn't landed yet.` sarı daire) →
  TR Caveat 64 (2 satır, mürekkep) → ORTA: solda saat + `2 saat` + zaman çizgisi (`took off`, `now`, `finished` / `unfinished`),
  sağda uçak (kutu 450 px) kalkış eğrisi + zemin → alt: iki yığılı etiket Fredoka 64 `ago → Simple Past` (kırmızı) / `yet → Present Perfect` (sarı).
  İçerik bandı 372–1390 dolu; altyazı bandı `altyazi.json` (sahne-ortak `altyaziCiz`, 05.11 yamalı); platform bandı boş.
- `sahne-ortak.js` = ppi-dikey 04 kopyası (`?canli=1` iken `POST /log` yok), `sayfa.html`, `nesneler.json`, `calistir.sh` (alarm 1500, telefon kontağı).

## Sayılar
- Kare 532 (ffprobe yuv420p 1080x1920 30 fps, ikisi de tema). `olaylar.json` 32 olay (cizgi 16, tik 13, parilti 2, vurus 1), son olay kare 505 < 532.
- Zamanlama (yerel kare): `3` 17 · TUZAK 53 · ago çizgisi 115 · daire 161 · TR 212 · ago etiketi 312 · yet etiketi 427.

## Kapılar
- Editör: `dikey-tam&tema=acik&t=55` → `slot no 4 hazir:true goster:true op:1`; konsol hata satırı yok.
- Baktığım kareler (Read): `k/0158.png`, `k/0278.png`, `k/0458.png`, `k/0519.png`, `kontrol.png`, `k/telefon-02.png` (360x640 kontak, koyu). HUD okunur, bant dolu, ≥ 64 px yazı, çakışma 0.

## Neden yeniden
- Tur 1 → 2: daire kırmızı alt çizgiye değiyordu, iki etiket kutusu birbirine yapışıktı, uçak zemin çizgisi etiketle çakışıyordu →
  satır aralığı 76 → 86 (ry 36), kart 306 px, uçak/zaman çizgisi yukarı, etiketler 1240 / 1320 (h 70).

## Açık sorular / sapma
- Uçak kutusu 450 px, çizim ≈ 370x340 (BRIEF "480"; 372–1392 bandına 4 satır + iki etiket sığdırmak için).
- Etiket yazısı 64 px (BRIEF 72): iki satır yığılı kutu bandın alt payına ancak böyle sığdı.
- Geçici kareler `~/Silinecekler/2026-11-05-kalem-ppi/` altında.
