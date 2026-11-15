# İstem V2-S1-C — 02-04-ydt-temel-s1 huni v2 çevirisi: senaryo + ses + zaman + sahne istemleri + açıklama · 15.11.2026

Ortam ve kurallar: `~/is/uretim-0204/S2-C.md` dosyasının ilk iki bölümü (MAKİNE, KURALLAR) AYNEN geçerli; önce onu oku. Ek kurallar:
yazma yalnız `K/projeler/02-04-ydt-temel-s1/` altında · sahne kodu yazma (sahneleri sonraki oturumlar yapar) · mp4 render yok · git commit yok ·
kanca atlama bayrağı oluşturma (`/tmp/conductor-*`, `~/.conductor/*`); sözleşme kancası isterse `K/.claude/docs/sozlesme.md` dosyasına 1–2 satır ekle ·
silme yok · `.env` okuma, API anahtarı yazma.

## Oku
1. `/home/sef/01dev/dijital-anlatim/.claude/docs/huni-v2-standart.md` (tamamı; BAĞLAYICI — bu paketi o standarda çeviriyorsun).
2. Paket: `BRIEF-S1.md`, `ortak/anlatim/senaryo.json`, `zaman.json`, `surumler.json`, `aciklama-a.md`, `aciklama-b.md`,
   `uretim-tutanagi/istem/sahne/*.md`, `uretim-tutanagi/S1-C-RAPOR.md` (varsa).
3. Ana ders: `K/projeler/02-04-ydt-temel/ortak/anlatim/senaryo.json` (yalnız `kadro` ve `sesler`: öğrenci ses kaydı buradan).

## Önce yedek
`ortak/anlatim/`, `zaman.json`, `surumler.json`, `BRIEF-S1.md`, `aciklama*.md` ve paket kökü PNG'lerini
`~/Silinecekler/2026-11-15-huni-v2/02-04-ydt-temel-s1/` altına KOPYALA (`cp -a`; taşıma değil). Sonra yerinde düzenle.

## Adımlar
1. `senaryo.json`: kanca ve değer cümlelerinin metni korunur. Son cümle (çağrı) ikiye ayrılır ve yeniden yazılır:
   - kaydet cümlesi, ses `ogretmen`: eski son cümlenin değer taşıyan ilk parçası kalabilir (ör. "Bu, üç farktan yalnız biri."),
     ardından kaydet kalıbı: `Sınavdan önce lazım olacak. Kaydet.`
   - çağrı cümlesi, ses `ogrenci`: `Gerisi bizde. Dersin tamamı YDS Publishing YouTube kanalında.`
   `kadro` ve `sesler` alanına öğrenciyi ana dersteki kayıttan ekle (ses kimliğini elle yazma, kopyala). "Tam ders" sözü ve süre sözü
   ("dakika") hiçbir cümlede kalmaz. Ham sözcük kuralı (rakam yok) sürer.
2. Ses: `cd K && bash araclar/ses-sunucu.sh 02-04-ydt-temel-s1`; sonra paketin ses betikleri (sözcük zamanı, kur, altyazı, METIN).
   Çağrı parçası öğrenci sesiyle çıkmalı (rapora ses kimliğinin son 4 hanesi). Whisper kapısında marka adı "YDS Publishing" bekleniyor;
   `D/araclar/iki-dilli/ses-sozluk.json` kısaltma kaydı ("YDS" → "YeDeSe") söylenişi verir. Kapı geçmezse dur ve raporla
   (aynı cümle 2 kez düşerse yeniden deneme yok).
3. `zaman.json`: zaman çizelgesi 4 sahne, sıra: `01-hyperframes-kapak` (kanca) → `02-…-ornek` (değer) → `08-hyperframes-kaydet` (YENİ) →
   `03-hyperframes-cta` (çağrı). Süreler yeni anlatımdan. Durağan kareler (`04`, `05`, `06`, `07`) listede bugünkü yerinde kalır.
4. `BRIEF-S1.md`: sahne tablosu ve yerleşim standart §2–§3'e göre güncellenir (kısa; eski satırlar değişir, yeni belge yazma).
5. Sahne istemleri `uretim-tutanagi/istem/sahne-v2/D-<klasör>.md` × 8 (eski `istem/sahne/` yerinde kalır; şablon ve biçim oradan):
   - `01`, `02`: içerik aynı; yerleşim standart §2'ye çekilir (üst 0–280 ve alt 1570–1920 boş; künye 360–450; içerik 460–1380;
     altyazı 1400–1550); kanal katmanı eklenir (§1 kural 1: yazı logosu + `@ydspublishing`, y 280–350, x 60, kalıcı).
   - `08-hyperframes-kaydet` (yeni): kural özeti kartı tek cümle + yer imi simgesi (SVG, emoji değil) + "Kaydet"; kart 2 sn sabit.
   - `03-hyperframes-cta` (çağrı, yeniden): ana dersin kapağı 16:9 kart (≈ 920×518, y ≈ 620–1140) + giriş sözü `Gerisi bizde.` (Fredoka 700) +
     `@ydspublishing · YouTube`. Kapak dosyası: sahne oturumu `K/projeler/02-04-ydt-temel/kapak.png` ve `kapak-koyu.png` dosyalarını
     pakete `ortak/kapak/ana-kapak.png`, `ana-kapak-koyu.png` olarak KOPYALAR (tema uyumlu kullanır); kaynak dosya yoksa sahne oturumu
     DURUR ve "ana kapak bekliyor" yazar. "Tam ders", süre, "izle" düğmesi taklidi yok.
   - `04`, `07` (hikâye A, B): standart §6 — kanal katmanı + kural özeti + "Kaydet"; iki sürüm birbirinden farklı düzen.
   - `05`, `06` (kapak B, C): kanal katmanı; altyazı yok; en az biri karakter görseli taşır
     (`K/projeler/02-04-ydt-temel/ortak/kapak/karakter.png` kopyası → `ortak/kapak/karakter.png`; krem çıkartma kenarı).
   - Kapak A (`kapak-a.png` + `kapak.png`): `01` sahnesinin kanca karesi, altyazı katmanı gizli (S1-KAPAK-A yöntemi:
     `uretim-tutanagi/S1-VAR-RAPOR.md` ya da s1 paketindeki rapor).
   Kanal katmanı: bütün sahnelerde AYNI piksel konumu ve boyu. Paketin ortak künye mekanizması (`ortak/kunye.js` ya da HyperFrames künye
   parçası) tek yerden veriyorsa oradan çöz ve istemlere "künye ortak dosyadan gelir, elle yazma" satırını koy; vermiyorsa istemlere aynı
   değerleri yaz (x, y, yükseklik, yazı boyu). Hangisini seçtiğini rapora yaz.
   Her isteme: QA kareleri ilk kare, orta, son kare (qa-yerel t değerleri KÜRESEL anlatım saniyesi) + koyu tema; "kanca atlama bayrağı
   oluşturma; sözleşme kancası isterse K/.claude/docs/sozlesme.md dosyasına 1–2 satır ekle"; çakışma kapısı komutu
   (`node araclar/cakisma-kapisi.mjs 02-04-ydt-temel-s1 --sahne <klasör> --port 41333 --sunucu 41022`).
6. `aciklama-a.md`, `aciklama-b.md`, `aciklama.md`: ilk satır standart §4; "Tam ders" ve süre sözleri çıkar; gerisi korunur.
7. `surumler.json`: yalnız `s1` satırının adındaki süre ölçülen yeni süreyle güncellenir; öteki satırlara dokunma.
8. `uretim-tutanagi/V2-C-RAPOR.md` (en çok 30 satır): değişen cümleler (eski → yeni), ses kapısı (cümle başına benzerlik, ses kimliği son 4),
   anlatım süresi, zaman çizelgesi, kanal katmanı çözümü, sahne istem listesi, açık noktalar.

Son mesajın en çok 10 satır.
