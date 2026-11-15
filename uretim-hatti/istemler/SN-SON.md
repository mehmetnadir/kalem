# İstem S{N}-SON — 02-04-ydt-temel-s{N} huni dosyaları tamamlama denetimi · 15.11.2026

BAĞLAYICI STANDART: üretimden önce `D/.claude/docs/` altından oku — `huni-v2-standart.md` (kısa), `kapak-standardi.md` (kapak, hikâye), `youtube-surumu-standart.md` (YouTube sürümü), `huni-ab-sozlesme.md` (A/B kolu). Bu istemdeki eski (v1) söz bunlarla çelişirse standart geçer. mp4 yalnız Nadir'in açık sözüyle. D=`/home/sef/01dev/dijital-anlatim`.

MAKİNE: Linux x86_64 (srv21), kullanıcı sef. K=`/home/sef/01dev/_worktrees/kalem-0204`. Node `~/.nvm/versions/node/v24.22.2/bin`.
KURALLAR: Yazma yalnız `K/projeler/02-04-ydt-temel-s{N}/` altında. Sahne kodunu (animasyon, yerleşim) değiştirme. Silme yok
(eskiyi `~/Silinecekler/2026-11-15-0204/` altına taşı). mp4 render YOK. git commit yok. Alt ajan yok. Bayrak dosyası oluşturma;
durma kancası sözleşme isterse `K/.claude/docs/sozlesme.md` dosyasına 1 satır ekle.

Sahne oturumları bitti (7 sahne). Bu iş paket kökündeki huni dosyalarını tamamlar ve denetler. Emsal: `K/projeler/02-04-ydt-temel-s1/`
(`uretim-tutanagi/S1-VAR-RAPOR.md` son bölüm: kapak A altyazısız çekim yöntemi — sahne `proje` kopyasında altyazı katmanı CSS ile
gizlenir, `hyperframes snapshot --at <sn>` ile kare alınır).

## Paket kökünde olması gerekenler (hepsi 1080×1920 PNG ya da md)
`kapak-a.png` + `kapak.png` (aynı dosya) · `kapak-b.png` · `kapak-c.png` · `hikaye-a.png` + `hikaye.png` (aynı) · `hikaye-b.png` ·
`aciklama-a.md` · `aciklama-b.md` · `aciklama.md`.

## Yap
1. Eksik olanı üret. Kapak A: `01-hyperframes-kapak` sahnesinin kapak karesi (BRIEF-S{N}'deki kare; S1'de 1,97 sn) ALTYAZISIZ, açık
   tema → paket kökü; koyu tema → `sahneler/01-hyperframes-kapak/k/koyu/kapak-a-koyu.png`. Var olan `kapak-a.png` altyazı bandı
   taşıyorsa aynı yöntemle yeniden çek. B, C ve hikâye kareleri sahne 04–07 çıktısıdır; kökte yoksa sahnenin kendi akışıyla üret.
   Var olan aracı kullan; yeni uzun betik yazma (15+ satır kod kapısı). Piksel boyama/kırpma yok.
2. Her PNG'ye Read ile BAK: altyazı bandı yok, taşma/kesik yazı yok, başlık 2 satır, künye ve rozet yerinde, A/B/C gerçekten farklı,
   hikâye B'de cevap yok. `file` ile 1080×1920. Kusur varsa sahneyi DEĞİŞTİRME; raporla (hangi kare, ne kusur).
3. `uretim-tutanagi/huni-surumler.json`: 7 satır (`s{N}-kapak-a|b|c`, `s{N}-hikaye-a|b`, `s{N}-aciklama-a|b`), `dosya` alanları kökteki
   adlarla eşleşsin, durum `inceleme`. `surumler.json` kısa video satırı `kimlik` = `s{N}`.
4. Yan yana kontak: `uretim-tutanagi/kontak/s{N}-huni-yanyana.png` (kapak A, B, C, hikâye A, B; 360×640 parçalar, ffmpeg hstack).
5. `uretim-tutanagi/S{N}-SON-RAPOR.md`: dosya listesi (var/üretildi), bakılan kareler, kusurlar, açık noktalar.

Son mesajın en çok 8 satır.
