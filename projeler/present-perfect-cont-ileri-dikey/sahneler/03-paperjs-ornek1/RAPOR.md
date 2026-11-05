# Sahne 03 — Örnek 1 (Paper.js, dikey 1080x1920, ileri)

Tema: acik + koyu (ikisi de koşuldu; `video-acik.mp4`, `video-koyu.mp4`, `video.mp4` = son koşu koyu).

| Kalem | Değer |
|---|---|
| Kare sayısı | 505 (zaman.json ile birebir; ffprobe acik ve koyu: 505 kare, yuv420p, 30 fps, 1080x1920) |
| Olay sayısı | 27 (`olaylar.json`, en büyük kare 479, son 12 kare durgun) |
| Editör kapısı | dikey-tam t=24 ve t=40: konsol boş (hata 0); eval slot {no:2|3, hazir:true, goster:true} |
| Denetim kareleri | k/0203, 0323, 0443, 0492 + k/telefon-01..03 (360x640 kontak, bakıldı) |

Neden yeniden: (1) 1. koşuda HUD ve sözcükler başka projeden geldi (ppci-dikey/02 kalem-paper.js present-perfect-cont-temel-dikey kunye.js'ini içe aktarıyordu; kendi kopyamda yola çevirdim) (2) ilk düzende sahne grubu 0,6'ya küçülüyordu; figür 420 altına inerdi → iki sütun düzeni: figür 430 px baştan sona, TR sağ sütun, formül kartı altta. Figür 420 altına inmiyor. Açık soru: ppci-dikey/02-paperjs-kanca/kalem-paper.js satır 4 hâlâ present-perfect-cont-temel-dikey (başka ajanın dosyası, dokunulmadı).
