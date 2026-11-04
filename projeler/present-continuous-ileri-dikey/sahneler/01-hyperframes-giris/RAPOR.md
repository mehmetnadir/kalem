# Sahne 01 İLERİ DİKEY — Giriş (HyperFrames, 102 kare, 1080x1920)

Tema: koyu

BRIEF-DIKEY §0–§4 ile sıfırdan düzen: logo sol üst 387x96 (y 48), ders adı 56 (taban 212), rozet 72/36 (y 236), çip `Hook` 80/40,
altyazı SVG metni Lexend 500 44 (taban 1484, band 1400–1536), platform bandı boş. Kapak: rozetler (y 372) → başlık 156 px 2 satır
→ cümle 1 Caveat 80 iki satır (taban 930/1020) → standing-3 (485 px) + telefon (240 px) → 2,1–3,0 uçuş: başlık ders adına, 1. rozet HUD rozetine,
cümle (taban 450/540) sahne 02 yerine; figür solar; çip son 0,25 sn.

## Kanıt
- video-acik.mp4 + video-koyu.mp4: 1080x1920 yuv420p 30 fps, 102 kare. olaylar.json 52 olay.
- Kare denetimi (Read): k/60.png, k/87.png, kontrol.png; telefon kontak k/telefon-01.png (360x640): HUD, başlık, altyazı okunuyor.
- Editör kapısı: `onizle.html?surum=dikey-tam&tema=acik&t=1.5` ve `t=8`: konsol hatası 0; slot `hazir:true, goster:true`.

## Neden yeniden
1. İlk koşu: cümle kırpması satır başı x'i iki kez çıkarıyordu (`-i`, `düş` kesik) → genişlik formülü düzeltildi.
2. Figür/telefon x kaydırıldı (telefon 8→10 ölçek); son sözcük kırpması 2,96 sn ile sınırlandı.

## Sapma / açık
- Kapak başlığı 156 px (BRIEF 190–230): `CONTINUOUS` 190 px'te 1175 px, 984 px içerik genişliğine sığmaz; 156 px'te 964 px.
- Uçuştan sonra (3,0–3,71 sn) içerik bandı yalnız cümle 1 ile dolu (alt yarı boş); BRIEF §4 sahne 02 başlangıcını böyle tarif ediyor.
