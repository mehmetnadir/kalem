# İstem S1-KAPAK-A — 02-04-ydt-temel-s1 kapak A altyazısız yeniden çekim · 15.11.2026

BAĞLAYICI STANDART: üretimden önce `D/.claude/docs/` altından oku — `huni-v2-standart.md` (kısa), `kapak-standardi.md` (kapak, hikâye), `youtube-surumu-standart.md` (YouTube sürümü), `huni-ab-sozlesme.md` (A/B kolu). Bu istemdeki eski (v1) söz bunlarla çelişirse standart geçer. mp4 yalnız Nadir'in açık sözüyle. D=`/home/sef/01dev/dijital-anlatim`.

MAKİNE: Linux x86_64 (srv21), kullanıcı sef. K=`/home/sef/01dev/_worktrees/kalem-0204`. Node `~/.nvm/versions/node/v24.22.2/bin`.
KURALLAR: Yazma yalnız `K/projeler/02-04-ydt-temel-s1/` altında. Sahne kodunu (animasyon, yerleşim) değiştirme. Silme yok
(eskiyi `~/Silinecekler/2026-11-15-0204/` altına taşı). mp4 render YOK. git commit yok. Alt ajan yok. Bayrak dosyası oluşturma;
durma kancası sözleşme isterse `K/.claude/docs/sozlesme.md` dosyasına 1 satır ekle.

## Sorun (şef kareye baktı)
`kapak-a.png` ve `kapak.png` (ikisi aynı; kaynak `sahneler/01-hyperframes-kapak/k/01-hyperframes-kapak-1.97.png`) karede ALTYAZI
bandı var: "İstanbul'da yaşıyorum. Amcamla yaşıyorum. Türkçede ikisi de yaşıyorum." Kapak görseli altyazı taşımaz
(kapak B ve C'de yok; sahne 05/06 kalıbı). Künye, rozet, başlık, çizim aynen kalır.

## Yap
1. Sahne 01'in 1,97. saniye karesini (kare 59, 30 fps) altyazı katmanı GİZLİ olarak 1080×1920 yeniden çek: açık tema →
   paket kökü `kapak-a.png` ve `kapak.png`; koyu tema → `sahneler/01-hyperframes-kapak/k/koyu/kapak-a-koyu.png`.
   Yol: sahne 05/06'nın kare çekme yöntemi (onların `calistir.sh` / `uret.py` akışına bak) ya da QA aracının (`araclar/qa-yerel.sh`)
   kare çekimi + altyazı öğesini gizleyen seçenek/CSS. Var olan aracı kullan; yeni uzun betik yazma (15+ satır kod kapısı).
   Altyazıyı piksel boyayarak ya da kırparak silme.
2. Eski `kapak-a.png` ve `kapak.png` dosyalarını Silinecekler'e taşı, yenilerini yaz.
3. Doğrula: iki yeni PNG'ye Read ile bak (altyazı yok, başka hiçbir şey değişmedi, taşma yok); `file` ile 1080×1920.
4. `uretim-tutanagi/S1-VAR-RAPOR.md` sonuna 3 satır ekle: ne değişti, hangi yöntem, bakılan kareler.

Son mesajın en çok 6 satır.
