# V2-S3-C raporu — 02-04-ydt-temel-s3 huni v2 çevirisi · 15.11.2026

| Ölçüm | Değer |
|---|---|
| Ses kapısı (faster-whisper turbo, eşik 0,85) | 8 / 8 parça geçti, tohum 0. Cümle: 1 → 1,00 · 2 → 0,98 · 3 → 1,00 · 4 → 1,00 · 5 → 1,00 |
| Ses kimliği (son 4) | öğretmen `4fwc` (cümle 1, 3, 4) · öğrenci `9gjY` (cümle 2, 5). Kanıt: cümle 5 parça anahtarı önbellekte öğrenci kimliğiyle var, öğretmenle yok; `kadro`/`sesler.ogrenci` ana dersle zaten aynıydı |
| Anlatım | 28,31 sn (`anlatim.m4a` ffprobe 28.310000; imza `9ad2cfc2…`). ElevenLabs 138 karakter (≈ 0,68 TL), 4 / 8 parça önbellekten |
| Zaman çizelgesi | 01 kanca 0,00–3,00 (102) → 02 değer 3,00–15,99 (402) → 08 kaydet 15,99–21,33 (172) → 03 çağrı 21,33–28,31 (239); durağan 04–07 yerinde |
| Yasak söz taraması (`tam ders`, `dakika`) | senaryo, altyazı, METIN, açıklama ×3, BRIEF: 0 |

Değişen cümleler (cümle 1–3 aynı; wav md5 v1 ile eşit):
- 4 (öğretmen): `Bu, üç farktan yalnız biri.` + `Tam ders: Simple Present ve Present Continuous.` + `Üç farkın hepsi dört buçuk dakikada.`
  → `Bu, üç farktan yalnız biri.` + `Bir arkadaşına gönder; o da karıştırıyor.`
- 5 (öğrenci, yeni): `Bu sadece başlangıç.` + `Dersin tamamı YDS Publishing YouTube kanalında.` (Whisper: "Dersin tamamı YEDESE Publishing YouTube kanalında.")

Yazılanlar: `ortak/anlatim/` (senaryo, zaman_uret.py 2 satır, ses zinciri çıktıları; günlük `uretim-tutanagi/ses-sentez-v2.log`), `zaman.json`,
`BRIEF-S3.md`, `aciklama-a.md`, `aciklama-b.md`, `aciklama.md` (= A), `surumler.json` (yalnız `s3` adı → `S3 Shorts (28,31 sn)`),
`uretim-tutanagi/istem/sahne-v2/D-<klasör>.md` × 8 (01, 02, 03, 04, 05, 06, 07, 08). Yedek: `~/Silinecekler/2026-11-15-huni-v2/02-04-ydt-temel-s3/`
(+ v1 sahne kodu `sahneler-v1/`, 25 MB, sahne oturumlarının kararlı başvurusu).

Kanal katmanı çözümü: ortak künye tek yerden VERMİYOR (canvas `ortak/kunye.js` ve HyperFrames sahne başına `yardim.py`, 7 farklı kopya,
ikisi de v1 HUD). Seçim: değerler istemlere aynen yazıldı; S1 BRIEF değerleriyle eşit (logo resim x 53,2 / görünür 60, y 291–339; yazı
Lexend 700 42, x 263, taban 330; künye taban 420, rozet y 386–434). 8 istemde blok md5 aynı (`f89fe9ed`).

Açık noktalar:
1. Süre 28,31 sn: standart ≈ 22–26, S2-C hedefi 24–28; 30 sınırının altında, yeniden sentez yok. Kaydet + çağrı 12,3 sn (standart ≈ 10).
2. Seste "Bir arkadaşına gönder", ekranda `Kaydet` (standart §3 gereği). Kaydet kartı cümlesi `Tarife → leaves, plan → am going.` yeni ekran metni (kaynak `meta.kapak.canAlici`); jüriden geçmedi.
3. Hikâye B v2'de cevabı açık verir (v1 gizliydi; standart §6 kural özeti ister). Şef onaylasın.
4. Birleştirme geçişi (`--gecis BookFlip`) kanal katmanını da çevirir; standart "giriş/çıkış yok" der. mp4 takvimine kadar etkisiz. Altyazı cümle 4 ikinci parçası 21,41'e uzanır (sahne sınırı 21,33); 08 istemi 21,33'te keser.
5. Ana ders kapağı 18:35'te oluştu (1920×1080); 03 istemi kopyalar, yoksa durur. Kart 1 devri (01 → 02) sabit: taban 568 / 666. Söyleniş "YeDeSe Publishing" Nadir dinleyince kesinleşir (standart §4).
