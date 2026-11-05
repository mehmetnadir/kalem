# Sahne 01 İLERİ DİKEY — Giriş (HyperFrames, 102 kare, 1080x1920) · Present Perfect

Tema: acik + koyu

BRIEF-DIKEY §0–§4: logo sol üst 387x96, ders adı 56 (taban 212), rozet 72/36, çip `Hook` 80/40, altyazı Lexend 500 44 (taban 1484),
platform bandı boş. Kapak: rozetler (y 360) → `PRESENT` / `PERFECT` 200 px (taban 612 / 800) → cümle 1 Caveat 80 iki satır
(taban 890 / 980, `Ago` kırmızı çizgi) → uçak (680x345) + saat (290) y 1040–1390 → 2,1–3,0 uçuş: başlık ders adına, rozet HUD'a,
cümle (450 / 540) sahne 02 yerine; çip son 0,25 sn.

## Kanıt
- iki tema 1080x1920 yuv420p 30 fps, 102 kare. olaylar.json 22 olay (kare 3–89).
- Kare denetimi (Read): k/60.png, k/87.png, k/89.png, telefon kontak k/telefon-01.png (360x640): HUD, başlık, altyazı okunuyor.
- Sayfa kapısı: `proje/index.html?canli=1&tema=acik`: konsol boş, `__timelines.main` var.

## Neden yeniden
1. `yok.` 87. karede kırpıktı (bkz. yatay) → 2,74 sn düzeltmesi; 89. karede tam.

## Sapma / açık
- Başlık 200 px (BRIEF 190–230); uçuş sonunda (87. kare) içerik bandı yalnız cümle 1 (sahne 02 başlangıcı).
- Editör `onizle.html?surum=dikey-tam` açılmıyor: dikey proje kökünde `surumler.json` yok, editör "Present Continuous" varsayılanına düşüyor,
  `window.EDITOR` tanımsız. Ortak/proje kökü dosyası; bu görevin kapsamı dışında, dokunulmadı.
