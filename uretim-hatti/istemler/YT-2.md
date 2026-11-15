# İstem YT-2 — YouTube sürümü DİKEY parçaları (1080×1920): giriş, çıkış, kısa çıkış, bildirim kartı yeri + önizleme · 15.11.2026

MAKİNE: Linux x86_64 (srv21), kullanıcı sef. K=`/home/sef/01dev/_worktrees/kalem-0204` (worktree), D=`/home/sef/01dev/dijital-anlatim`.
Python `/usr/bin/python3 -I`. Skill `~/.claude/skills/motion-grafik-ders/`.
KURALLAR: Yalnız isteneni yaz. Silme yok (`rm` yok; gerekirse `~/Silinecekler/2026-11-15-youtube-dikey/` altına taşı). mp4 RENDER YOK (kare ve ses
üretilir, video dosyası üretilmez). git commit yok, alt ajan yok, agy-filo yok, ayna yüklemesi yok. Yazma YALNIZ `K/ortak/youtube/dikey/` altında
(dizini aç); yatay parçalara (`K/ortak/youtube/giris`, `cikis`, `bildirim`), ders paketlerine, `araclar/` ve `ortak/oynatici/` altına dokunma. Kanca
atlama bayrağı oluşturma. Arka plan işi beklerken `pgrep -f` kullanma; komutu ön planda `timeout` ile koştur. Jeton ya da anahtar değeri yazma, `.env`
okuma (ses aracı kendi ortamını kendisi okur).

## Amaç
Karar D-0341: bütün dersler YouTube'a açık temayla, yatay VE uzun dikey (9:16) olarak yüklenir. Yatay parçalar hazır (YT-1). Bu iş aynı parçaların
dikey sürümünü üretir. Bağlayıcı standart: `D/.claude/docs/youtube-surumu-standart.md`. Emsal ve ölçümler: `K/ortak/youtube/RAPOR.md` (YT-1 çıktısı;
dosya düzeni, ses dosyaları, kapı maddeleri), `K/ortak/youtube/giris/`, `cikis/`, `bildirim/`.
Dikey ders emsali: `K/projeler/02-04-ydt-temel-dikey/` ve `K/projeler/simple-present-temel-dikey/` (güvenli alan: üst %15 künye, içerik %15–70,
altyazı %70–80, alt %20 boş; `D/.claude/docs/huni-v2-standart.md` §2 yerleşim tablosu).

## Yaz (hepsi `K/ortak/youtube/dikey/` altında)
1. `giris/` — yatay girişle aynı sahne, 1080×1920, 30 fps, aynı süre (3,00 sn). Ses yatayla AYNI dosyadır: kopyala (sha256 eşit), yeniden
   sentezleme. Logo ve `@ydspublishing` içerik bölgesinde (y %15–70), ortalı. Açık + koyu tema.
2. `cikis/` — 1080×1920, 20,0 sn; dersin YouTube süresi 180 sn'den UZUN olduğu durum içindir (YouTube bunu olağan video sayar, bitiş ekranı vardır).
   Üst yarı (y < 960): söz satırı + logo + `@ydspublishing`. ALT YARI (y ≥ 960) BOŞ kalır: yalnız zemin (bitiş ekranı ögeleri oraya gelir). Ses yatay
   çıkışla AYNI dosya (kopya, sha256 eşit). Açık + koyu.
3. `cikis-kisa/` — 1080×1920, süre ≤ 4,0 sn; dersin YouTube süresi 180 sn ve ALTINDA olduğu durum içindir (YouTube bunu Shorts sayar; bitiş ekranı
   yoktur, 20 sn boş çıkış izleyiciyi kaçırır). Ekran: söz satırı + logo + `@ydspublishing`, içerik bölgesinde. Ses (ÖĞRENCİ sesi): "Faydalı olduysa
   abone ol." Bu cümle yatay çıkışta ayrı parça olarak sentezlendiyse önbellekten al; değilse dersin ses zinciriyle sentezle (Whisper ≥ 0,90).
   Söz 0,3 sn'de başlar. Açık + koyu.
4. `bildirim/` — kart görseli yatayla AYNI dosyalardır (kopyalama; `yer.json` yalnız yeri taşır). Dikey derste kartın hiçbir öğeyle çakışmayacağı
   yeri ÖLÇ: iki dikey dersin var olan karelerinden en az 8 kare (`…-dikey/sahneler/*/k/*.png`, 1080×1920 olanlar) al; künye, bölüm çipi, altyazı ve
   sahne içeriği kutularını çıkar; bütün karelerde boş kalan bölgeyi bul. YASAK bölgeler: alt %20 (Shorts arayüzü: başlık, kanal, ses), sağ kenar
   x ≥ 900 şeridi y %45–80 arası (Shorts düğmeleri). Aday sıra: künyenin hemen altı (sol), altyazının üstü (sol). Sonuç `bildirim/yer.json`
   (`{"x":…, "y":…, "w":…, "h":…, "kose":"…", "olcek":…}`; kart 1080 genişliğe sığmıyorsa ölçeği yaz) + ölçüm tablosu + kart bindirilmiş 4 örnek kare.
5. Kareler: `giris/` 0,0 · 1,0 · son; `cikis/` 0,5 · 4,0 · 19,9; `cikis-kisa/` 0,3 · son; açık + koyu. `cikis/` karelerinde y ≥ 960 bölgesinde zemin
   dışı piksel sayısını ölç (0 olmalı).
6. `onizle.html` — tek dosya; dikey çerçevede (9:16, ekrana sığar) sırayla oynatır: giriş → 6 sn örnek dikey ders karesi (2. saniyede bildirim kartı,
   3 sn) → çıkış. Üstte "Açık / Koyu", "Uzun çıkış / Kısa çıkış" ve "Baştan" düğmeleri. Dış ağ isteği yok; yollar göreli.
7. `RAPOR.md` — dosya listesi; süre ve ses ölçümleri (sha256 eşitlikleri); yer ölçümü tablosu; kapı maddeleri (ilk söz ≤ 1 sn, uzun çıkışta alt yarı
   boş, kart çakışmıyor ve yasak bölgelere girmiyor); standarttan sapma varsa gerekçesi; birleştirme aracının beklediği girdi tablosu (dosya, boyut,
   süre) ve seçim kuralı (YouTube süresi ≤ 180 sn → `cikis-kisa`, değilse `cikis`).

Kareleri Read ile kendin gör; "çalışıyor" demeden önce logo, yazı ve kartın okunduğunu, taşma olmadığını doğrula.
Son mesajın en çok 12 satır: süreler, sha256 eşitlikleri, kısa çıkış sesi (önbellek mi sentez mi, Whisper), seçilen bildirim yeri, sapmalar,
önizleme dosyasının yolu.
