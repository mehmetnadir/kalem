# İstem YT-1 — YouTube sürümü ortak parçaları: giriş sahnesi, çıkış sahnesi, sessiz bildirim kartı + tarayıcı önizlemesi · 15.11.2026

MAKİNE: Linux x86_64 (srv21), kullanıcı sef. K=`/home/sef/01dev/_worktrees/kalem-0204` (worktree), D=`/home/sef/01dev/dijital-anlatim`.
Python `/usr/bin/python3 -I`. Skill `~/.claude/skills/motion-grafik-ders/`.
KURALLAR: Yalnız isteneni yaz. Silme yok (`rm` yok; gerekirse `~/Silinecekler/2026-11-15-youtube/` altına taşı). mp4 RENDER YOK (kare ve ses üretilir,
video dosyası üretilmez). git commit yok, alt ajan yok, agy-filo yok, ayna yüklemesi yok. Yazma YALNIZ `K/ortak/youtube/` altında (dizini aç); ders
paketlerine, `araclar/` ve `ortak/oynatici/` altına dokunma. Kanca atlama bayrağı oluşturma (`/tmp/conductor-*`, `~/.conductor/*`); sözleşme kancası
isterse `K/.claude/docs/sozlesme.md` dosyasına 1–2 satır ekle. Arka plan işi beklerken `pgrep -f` kullanma; komutu ön planda `timeout` ile koştur.
Jeton ya da anahtar değeri yazma, `.env` okuma (ses aracı kendi ortamını kendisi okur).

## Amaç
YouTube'da yayınlanacak derslerin mp4'üne, render SONRASI birleştirmeyle eklenecek üç ortak parça. Parçalar bütün derslerde aynıdır; bir kez üretilir.
BAĞLAYICI standart: `D/.claude/docs/youtube-surumu-standart.md` (önce `git -C D pull --ff-only` dene; olmazsa var olan kopyayı oku; dosya yoksa DUR ve raporla).
Envanter (hat bugün nasıl çalışıyor): `D/.claude/docs/arastirma/1511/youtube-surumu-envanter.md`.

## Okuma (emsal)
1. Yeni kuşak ders: `K/projeler/02-04-ydt-temel/` — `sahneler/01-hyperframes-giris/` (logo girişi, yazı tipleri, tema değişkenleri, `calistir.sh`,
   `uret.py`, `yardim.py`), `sahneler/14-hyperframes-kapanis/`, `ortak/` (kunye.js, logo, font, tema), `zaman.json` (1920×1080, 30 fps), `BRIEF.md`.
2. Ses: ana dersin `ortak/anlatim/senaryo.json` `kadro` / `sesler` (öğrenci sesi kimliği), ses zinciri betikleri ve
   `D/araclar/iki-dilli/el.py`, `ses-sozluk.json` (`YDS` → `YeDeSe`). Huni kısasında aynı sesle çağrı emsali:
   `K/projeler/02-04-ydt-temel-s1/uretim-tutanagi/V2-C-RAPOR.md` (ses kapısı ve önbellek).
3. Ev stili: emoji yok; simge SVG; açık tema varsayılan, koyu tema eş; ham renk yok (dersin tema değişkenleri).

## Yaz (hepsi `K/ortak/youtube/` altında)
1. `giris/` — HyperFrames sahnesi, 1920×1080, 30 fps, süre ≤ 3,0 sn. Ekran: `ydspublishing` yazı logosu + `@ydspublishing`; sade, tek hareket (logo
   yerine oturur). Ses (ÖĞRENCİ sesi): "YDS Publishing'e hoş geldin." İlk söz ≤ 1,0 sn'de başlar; söz 3,0 sn'den önce biter (bitmiyorsa sahne süresini
   söze göre ayarla ve raporla). Açık + koyu tema.
2. `cikis/` — HyperFrames sahnesi, 1920×1080, 30 fps, süre 20,0 sn. Sol yarı: söz satırı (Fredoka 700) + logo + `@ydspublishing`. SAĞ YARI (x ≥ 960)
   BOŞ kalır: yalnız zemin (YouTube bitiş ekranı ögeleri oraya gelir). Ses (ÖĞRENCİ sesi), 0,5 sn'de başlar: "Faydalı olduysa abone ol. Sıradaki ders
   ekranda." Sözden sonra ekran sabit kalır (hareketli grafik yok). Açık + koyu tema.
3. `bildirim/` — SESSİZ kart: "Beğen · Abone ol". İki simge elle çizilmiş SVG (beğen işareti, abone düğmesi biçimi); emoji yok, YouTube logosu yok.
   Çıktı: şeffaf zeminli `bildirim-acik.png` ve `bildirim-koyu.png` (RGBA; kart ≈ 520×140 px, 1920×1080 kareye göre). Giriş/çıkış hareketi birleştirme
   aracında `fade` ile verilecek; burada yalnız durağan kart.
4. Yer ölçümü: bildirim kartının derste hiçbir öğeyle çakışmayacağı yeri ÖLÇ. İki dersin var olan karelerinden en az 8 kare al
   (`K/projeler/02-04-ydt-temel/sahneler/*/k/*.png` yeni kuşak, `K/projeler/simple-present-temel/sahneler/*/k/*.png` eski kuşak; 1920×1080 olanlar):
   künye, bölüm çipi, altyazı ve sahne içeriğinin kapladığı kutuları çıkar; bütün karelerde boş kalan en büyük köşe bölgesini bul (aday sıra: sağ üst,
   sol alt, sol üst; sağ alt YASAK — YouTube filigranı). Sonucu `bildirim/yer.json` (`{"x":…, "y":…, "w":…, "h":…, "kose":"…"}`) ve ölçüm tablosuyla yaz.
   Kartı bu yere bindirilmiş 4 örnek kare üret (`bildirim/ornek-*.png`: 2 ders × açık/koyu ya da eldeki tema).
5. Ses: iki cümleyi dersin ses zinciriyle sentezle (öğrenci sesi; önbellek anahtarı kuralına uy), Whisper kapısı ≥ 0,90; dosyalar `giris/ses/` ve
   `cikis/ses/`. Süreleri ölç (sn, 2 ondalık).
6. Kareler: `giris/` için 0,0 · 1,0 · son kare; `cikis/` için 0,5 · 4,0 · 19,9 sn; açık + koyu (`k/` ve `k/koyu/`). Çıkış karelerinde x ≥ 960 bölgesinde
   zemin dışı piksel sayısını ölç (0 olmalı).
7. `onizle.html` — tek dosya, tarayıcıda açılınca sırayla oynatır: giriş sahnesi (sesiyle) → 6 sn örnek ders karesi (durağan görüntü; 2. saniyede
   bildirim kartı belirir, 3 sn kalır, kaybolur) → çıkış sahnesi (sesiyle). Üstte "Açık / Koyu" düğmesi ve "Baştan" düğmesi. Dış ağ isteği yok; yollar
   göreli (`./giris/…`). Bu sayfa Nadir'in önizlemesi içindir.
8. `RAPOR.md` — dosya listesi; süre ve ses ölçümleri; Whisper benzerlikleri; yer ölçümü tablosu ve seçilen köşe; kapı maddeleri (standart §5: ilk söz
   ≤ 1 sn, sağ yarı boş, kart çakışmıyor); standarttan sapma varsa gerekçesi; birleştirme aracının (sonraki iş) bu parçalardan beklediği girdi
   (dosya adı, boyut, süre) tablo olarak.

Kareleri Read ile kendin gör; "çalışıyor" demeden önce logo, yazı ve kartın okunduğunu, taşma olmadığını doğrula.
Son mesajın en çok 12 satır: süreler, Whisper, seçilen köşe ve ölçüsü, sapmalar, önizleme dosyasının yolu.
