# PRESENT PERFECT İLERİ yatay · sahne 05 Kök 3 / tuzak (düz canvas) — RAPOR (05.11.2026)

Tema: acik + koyu (ikisi de koşuldu; `video-acik.mp4` + `video-koyu.mp4`; `video.mp4` = son koşu).

## Yapılan
- `sahne.js` (BRIEF §4 sahne 05): daire `3` (51,82) · kırmızı `TUZAK` (53,00) · cümle Fredoka 56, 3 satır 4/5/3 sözcük, sözcük zamanlı ·
  `two hours ago` kırmızı alt çizgi (55,09) · `hasn't landed yet.` sarı daire (56,61) · sağ: kalkış eğrisi + uçak 440 px + saat + `2 saat` ·
  TR çeviri Caveat 48 (58,30) · zaman çizgisi: `took off`, `finished` ayracı, `now` (60,30), kesik oklu `unfinished` ·
  kırmızı etiket `ago → Simple Past` (61,65 / 64,05) · sarı etiket `yet → Present Perfect` (65,48 / 67,64). Kırmızı yalnız tuzak (TUZAK, ago).
- `sahne-ortak.js` = ppi 04 kopyası (`?canli=1` iken `POST /log` atılmaz), `sayfa.html`, `nesneler.json`, `calistir.sh` (alarm 1500).

## Sayılar
- Kare 532 (ffprobe yuv420p 1920x1080 30 fps, ikisi de tema). `olaylar.json` 33 olay (cizgi 15, tik 15, parilti 2, vurus 1), son olay kare 505 < 532, aynı karede en çok 1.
- İlk çizim karesi 17 (ilk 12 kare boş). Zamanlama (yerel kare = round((t − 51,25) × 30)): 3 → 17 · TUZAK 53 · ago çizgisi 115 · daire 161 · TR 212 · ago etiketi 312 · yet etiketi 427.

## Kapılar
- Editör (başsız, ortak-tarayıcı): `ana-yatay&tema=acik&t=55` → `{"t":55,...,"slot":[{"no":4,"hazir":true,"goster":true,"op":1},...]}`; konsolda hata satırı yok.
- Baktığım kareler (Read): `k/0158.png`, `k/0278.png`, `k/0458.png`, `k/0519.png`, `kontrol.png` (koyu). Çakışma 0, künye tam, yazı okunur.

## Neden yeniden
- Tur 1 → 2: sarı daire kırmızı alt çizgiye ve `hasn't` harflerine değiyordu, `finished`/`unfinished` yazıları etiket kutusuna yapışıktı →
  satır aralığı 80 → 96, daire boyu/pay (ry 46, pay 40), çizelge ve kutular aşağı alındı.
- Tur 1'in ilk koşusu sistem sinyaliyle kesildi (çıkış 144, yük 50); aynı koşu yeniden başlatıldı.

## Açık sorular
- Tabler `plane.svg` tek yol: uçak tek darbe çiziliyor (olay az).
- Geçici kareler `~/Silinecekler/2026-11-05-kalem-ppi/` altında (LISTE.md).
