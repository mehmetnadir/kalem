# S3-C raporu — simple-present-temel-s3 paket + ses + zaman + sahne istemleri + açıklama · 15.11.2026 (istem P0202-S3-C)

| Ölçüm | Değer |
|---|---|
| Jüri | 11 / 11 madde işlendi (dil 4 + kaynak 7; iki çift aynı sorun) + 1 ek (madde 10, yazı tabanı) → `S3-duzeltme.md` |
| Ses kapısı (el.py, faster-whisper large-v3-turbo int8, eşik 0,85) | 9 / 9 parça geçti; en düşük 0,93 |
| Çağrı (öğrenci sesi, standart §7 kapı 4 ≥ 0,9) | 1,00 · 1,00; cümle 4 önbellekten (`cumle-4.wav` md5 `bf5e747e…` = `02-04-ydt-temel-s3/ortak/anlatim/cumle-5.wav`) |
| Anlatım | **25,08 sn** (`anlatim.m4a` ffprobe 25.080000; imza `8f8c1b83…`, `aac-96k-48000-mono`); hedef 22–28 içinde, 32 sınırının altında |
| ElevenLabs | 180 karakter (≈ 0,88 TL), cümle 1–3; vekil `ses-sunucu.sh`; günlük `ses-sentez.log` |
| Zaman çizelgesi | 01 0,00–3,89 (129) · 02 3,89–12,84 (281) · 03 12,84–18,10 (170) · 04 18,10–25,08 (239); `hikaye` (05) + `duragan[]` (06–08) |
| Metin taraması (standart §7 kapı 3) | `senaryo.json`, `altyazi.json`, `METIN.md`, `aciklama*.md`, `surumler.json`: `tam ders` / `dakika` 0 sonuç. Sahne kodu yok |

## 1. Ses kapısı — parça başına benzerlik

| Cümle | Konuşan | Parça | Duyulan (Whisper) | Benzerlik |
|---|---|---|---|---|
| 1 | öğretmen | EN `He doesn't goes.` | He doesn't goes. | 1,00 |
| 1 | öğretmen | TR `Hata nerede?` | Hata nerede? | 1,00 |
| 2 | öğretmen | TR `Olumsuzda ve soruda does girer, s ona geçer.` | Olumsuzda ve soruda döz girer, S ona geçer. | 0,96 |
| 2 | öğretmen | TR `Fiile s gelmez.` | Fiile S gelmez. | 1,00 |
| 2 | öğretmen | EN `He doesn't go. Does she go?` | He doesn't go. Does she go? | 1,00 |
| 3 | öğretmen | TR `Does varsa fiil yalın.` | Döz varsa fiil yalın. | 0,93 |
| 3 | öğretmen | TR `Bir arkadaşına gönder; o da karıştırıyor.` | Bir arkadaşına gönder. O da karıştırıyor. | 1,00 |
| 4 | öğrenci | TR `Bu sadece başlangıç.` | Bu sadece başlangıç. | 1,00 |
| 4 | öğrenci | TR `Dersin tamamı YDS Publishing YouTube kanalında.` (ses metni `YeDeSe`) | Dersin tamamı YEDESE Publishing YouTube kanalında. | 1,00 |

Cümle başına en düşük: 1 → 1,00 · 2 → 0,96 · 3 → 0,93 · 4 → 1,00. Yanlış cümle riski (taslak B planı 4) gerçekleşmedi: Whisper `goes` yazdı.
`does` TR parçada sözlükten `/dʌz/` okundu, Whisper "döz" yazdı (kıyas metni ekran metnidir; 0,93–0,96).

## 2. Yazılanlar

| Dosya | İçerik |
|---|---|
| `uretim-tutanagi/{senaryo,kapak,hikaye,aciklama}-taslak.md` | jüri düzeltmeleri; önceki hâl `~/Silinecekler/2026-11-15-0204/simple-present-temel-s3-taslak-onceki/` |
| `uretim-tutanagi/S3-duzeltme.md` | madde → yapılan → kanıt; ayrılan yer; şef kararları |
| `ortak/` | bağlar `cizim`, `font`, `logo`, `hf_tema.py` (emsal ile aynı hedef); `kalem-canvas.js`, `tema.sh`, `tema_damga.py` (emsal kopyası); `kunye.js` (emsal v2 kopyası; `KOK` bu paket, konu `Simple Present`, rozet `YDT · BASIC`) |
| `ortak/kapak/` | `ana-kapak.png`, `ana-kapak-koyu.png` (← `simple-present-temel/kapak.png`, `kapak-koyu.png`, 1920×1080), `karakter.png` (← ana `ortak/kapak/karakter.png`) |
| `ortak/anlatim/senaryo.json` | emsal şeması; 4 cümle (3 öğretmen + 1 öğrenci); `sesler` ve `kadro` ana paketten birebir (`kadro` yalnız `ogrenci`); `meta.kimlik` `02-02-ydt-temel-s3`; `meta.kapak.canAlici` boş |
| `ortak/anlatim/*.py` | emsal kopyası; `zaman_uret.py` 1 Edit (4 sahne temiz numara, `duragan[]` sabit, `GIRIS_SN 4,0`); `metin_uret.py` başlık satırı (sed) |
| ses zinciri çıktıları | `sentez.wav` (+ rapor), `cumle-1…4.wav`, `sureler.json`, `sozcukler.json` (41 sözcük), `baslar.json`, `anlatim.wav`, `anlatim.m4a` (+ imza), `altyazi.json` (9 parça), `METIN.md` |
| `zaman.json` | 1080×1920, 30 fps, `gecis_kare` 12, 4 sahne + `hikaye` + `duragan[]` |
| `gorevler.json`, `yorumlar.json`, `harita-konum.json` | emsal ile aynı boş değer |
| `BRIEF-S3.md` | çıktı, kaynaklar, yerleşim, kanal katmanı tablosu (emsalden aynen), sahne tablosu, sahne içeriği (ölçülmüş çapalar), kapak ve hikâye tarifi, çalıştırma |
| `aciklama-a.md`, `aciklama-b.md`, `aciklama.md` (= A, `cmp` aynı) | YouTube / Instagram / TikTok; yer tutucular `{UZUN_VIDEO_URL}`, koşullu `{PLATFORM_URL}` |
| `surumler.json` | `video` = ana paket `video` (`kimlik` `02-02-ydt-temel`); 8 satır `s3`, `s3-kapak-a|b|c`, `s3-hikaye-a|b`, `s3-aciklama-a|b`; durum `inceleme`; ad `S3 Shorts (25,08 sn)`; anahtar sırası emsalle aynı (assert) |
| `uretim-tutanagi/istem/sahne/D-*.md` × 8 | 01 kanca (+ kapak A), 02 değer, 03 kaydet, 04 çağrı, 05 hikâye A, 06 kapak B, 07 kapak C, 08 hikâye B; her istemde kanca bayrağı yasağı + sözleşme satırı, çakışma kapısı, QA kareleri (KÜRESEL sn), koyu tema |
| `K/.claude/docs/sozlesme.md` | 1 satır (yeni kısada `duragan[]`, `GIRIS_SN`, önbellek) |

## 3. Açık noktalar

1. **Rozet.** İstem "Rozet emsaldeki gibi" → `YDT · BASIC`. Standart §2 ve iki jüri `YDT · TEMEL` der. Seri kararı şefte.
2. **canAlici.** Ana `canAlici` listesinde S3'ün maddesi yok; `meta.kapak.canAlici` boş. Şef ana listeye cümle 7 parça 4'ü eklerse alan onu alır.
3. **Karakter yeri.** İstem "karakter kapak B ya da C'de" der; jüriden geçen taslak karakteri A'ya (kanca karesi = sahne 01) koyar, B ve C
   figürsüzdür. Taslak uygulandı (standart §6 "en az biri" A ile karşılanır). Şef isterse D-06 ya da D-07'ye taşınır.
4. **BRIEF adı.** İstem adım 2 ve 6 `BRIEF-S2.md` der; paket S3 olduğu için `BRIEF-S3.md` yazıldı (emsal `02-04-ydt-temel-s3/BRIEF-S3.md` kalıbı).
5. **Kanca süresi.** Sahne 01 0,00–3,89 (emsalde K23 gereği 3,00). Standart §3 "kanca 0–4 sn" esas alındı; cümle 1 tamamen sahne 01'de.
6. **Hikâye B.** Kural özeti karta girdi (jüri kaynak 4 (a)); soru kuraldan çözülür. Jüri bunu "kaydetmeye değer" diye önerdi; etkileşim etkisi ölçülmedi.
7. **`utm_campaign` harfi.** S3 büyük harf `ING-YDT-GR-02-02-T` (taslak, S2 ile aynı, jüri geçti); emsal 02-04-ydt-temel-s1 küçük harf. Seri kararı şefte.
8. **Söyleniş.** "YeDeSe Publishing" ve TR içinde `does` (/dʌz/) Nadir kulağıyla kesinleşir (standart §4).
9. **Emsal kaydet sahnesi.** `02-04-ydt-temel-s1/sahneler/08-hyperframes-kaydet/` bu koşuda yoktu; D-03 yedek taban olarak `03-hyperframes-cta` yazar.
10. **Kanca kartı genişliği.** `He doesn't goes.` Fredoka 80 taslaktaki x 60–640'a sığmaz (≈ 700 px); D-01 kartı yazıya göre açar, karakter kalan alana sığar.
11. **Ana kapak kopyaları git'e girer.** Kök `kapak.png` `.gitignore`'da; `ortak/kapak/*.png` değil (emsal ile aynı durum). Commit şefte.
