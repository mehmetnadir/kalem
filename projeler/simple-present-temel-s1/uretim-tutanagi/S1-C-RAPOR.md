# S1-C raporu — simple-present-temel-s1 (02-02-ydt-temel-s1) huni v2 paketi · 15.11.2026

| Ölçüm | Değer |
|---|---|
| Eski kısa | `uretim-tutanagi/` dışındaki her şey `~/Silinecekler/2026-11-15-huni-v2/simple-present-temel-s1-eski/` altına taşındı (`mv`): `BRIEF-S1.md`, `RAPOR.md`, `ortak/`, `sahneler/` (01–03), `surumler.json`, `zaman.json`, `gorevler.json`, `yorumlar.json`, `harita-konum.json` |
| Jüri | 6 madde: 5 uygulandı (D1, D3, D4, K1, K2), 1 uygulanmadı (D2 öneri satırı, K2 ile çelişir) → `S1-duzeltme.md` |
| Ses kapısı (el.py, faster-whisper turbo, eşik 0,85) | 9 / 9 parça; cümle 1 → 1,00 · 2 → 1,00 (5 parça: 1,00 · 1,00 · 1,00 · 1,00 · 1,00) · 3 → 1,00 · 4 → 1,00 (2 parça: 1,00 · 1,00) |
| Ses kimliği | cümle 1–3 öğretmen `gsJ9nrlXYbPztJxC4fwc` · cümle 4 öğrenci `oPC5I9GKjMReiaM29gjY` (ana ders `sesler` + `kadro.ogrenci`, kopya) |
| Marka adı | Whisper "YEDESE Publishing" duydu; kıyas metni (sözlük `YDS` → `YeDeSe`) 1,00 |
| Önbellek | cümle 4 ücretsiz: 02-04-ydt-temel-s1 cümle 4 ile aynı anahtar (`cumle-4.wav` 415.466 bayt, emsalle birebir; kapı önbelleği 2 / 9) |
| Anlatım | **24,00 sn** (`anlatim.m4a` ffprobe 24.000000; imza `6391ee92…`); ElevenLabs 155 karakter (≈ 0,76 TL). Hedef 22–28 sn: içinde |
| Zaman çizelgesi | 01 kanca 0,00–3,00 (102) · 02 değer 3,00–14,63 (361) · 03 kaydet 14,63–17,74 (105) · 04 çağrı 17,74–24,00 (218); `hikaye` = 05, `duragan[]` = 06, 07, 08 |
| Cümle başları | 1,00 · 4,67 · 15,18 · 18,29; son söz 23,00 (+ 1,0 kuyruk) |

Yazılanlar (hepsi `K/projeler/simple-present-temel-s1/` altında; ek: `K/.claude/docs/sozlesme.md` 1 satır):

| Dosya | İçerik |
|---|---|
| `ortak/` | emsal bağları (`cizim`, `font`, `hf_tema.py`, `logo` → `../../present-continuous/ortak/`) · `kalem-canvas.js`, `tema.sh`, `tema_damga.py` (emsal kopyası) · `kunye.js` (emsal v2 kopyası; 2 Edit: `KOK`, `KUNYE.konu` `Simple Present`) |
| `ortak/kapak/` | `ana-kapak.png`, `ana-kapak-koyu.png` (ana ders `kapak.png`, `kapak-koyu.png`; 1920×1080) · `karakter.png` · `nesne.png` (kapak B taslağı ister) |
| `ortak/anlatim/` | `senaryo.json` (emsal şeması; 4 cümle, 9 parça; rakam yok) · `sozcuk_uret.py`, `kur.py`, `metin_uret.py` (emsal kopyası) · `zaman_uret.py` (2 Edit: 4 sahne + `hikaye`/`duragan[]` sabit) · ses zinciri çıktıları (`cumle-1..4.wav`, `sentez.wav` + rapor, `sureler`, `sozcukler`, `baslar`, `anlatim.wav/.m4a/.imza`, `altyazi.json`, `METIN.md`) |
| kök | `zaman.json` · `surumler.json` (8 satır, `video.kimlik` `02-02-ydt-temel`, durum `inceleme`, `s1` = "S1 Shorts (24,00 sn)") · `BRIEF-S1.md` · `aciklama-a.md`, `aciklama-b.md`, `aciklama.md` (= A) · `gorevler.json`, `yorumlar.json`, `harita-konum.json` (boş) |
| `uretim-tutanagi/` | `S1-duzeltme.md` · `istem/sahne/D-*.md` × 8 · `ses-sentez.log` · bu rapor · taslak düzeltmeleri (`senaryo-`, `kapak-`, `hikaye-`, `aciklama-taslak.md`, `S1-A-RAPOR.md`) |

Metin taraması (standart §7 kapı 3): paket içinde yasak kapanış sözü ve süre sözü yok; yalnız salt okunur jüri kaydı (`juri/s1.kaynak-kural.md` satır 50, 65)
kuralı alıntılar. İstemlerdeki tarama komutu desen olarak yazıldı (`tam[ ]ders|dak[i]ka`).

## Açık noktalar

1. **Jüri D2 ↔ K2 çelişkisi.** D2 değer kartına söylenmeyen `Kardeşim okula` / `otobüsle gider.` ister; K2 bunu yasaklar. K2 yolu uygulandı
   (`Kardeşim gider:` soluk sürer). D2 satırı da eklensin mi: şef kararı.
2. **`go` / `goes` okunuşu (kulak).** Whisper 1,00 (`Kardeşim gider. Go mu, goes mu?`), ama Whisper dilbilgisini düzeltebilir (jüri dil açık 3).
   Nadir dinlemeli. "go-es" duyulursa B planı: TR `Kardeşim gider:` + EN `Go or goes?` (yeniden sentez gerekir).
3. **Kanca 0–4,12.** Cümle 1 4,12'de biter (standart 0–4 sn; +0,12). Sahne 01 3,00'te biter (taslak klasör eşlemesi, K23); `goes` ve `mu?` 02'de.
   Aynı dersin S3'ü `GIRIS_SN 4,0` seçti (`sozlesme.md`); S1 taslağa bağlı kaldı.
4. **Kaydet sahnesi dar.** 14,63–17,74 (3,11 sn): kart sabit 15,63–17,74 (2,11 sn ≥ 2); `Kaydet.` 17,10 → sahne sonu 0,64 sn (emsal 0,60).
5. **Rozet `YDT · BASIC`.** İstem "emsaldeki gibi"; standart §2 örneği ve taslaklar `YDT · TEMEL` idi (taslaklar BASIC'e çekildi).
6. **Karakter ↔ kadro.** `karakter.png` erkek, `kadro.ogrenci` kadın (jüri kaynak açık 5); kapak B ve çağrı kartı ana dersin görselini taşır. Nadir/şef.
7. **Kapak C figürsüz** (taslak §5 sapması; jüri madde saymadı). Karar şefte.
8. **Kırmızı.** Ana ders BRIEF kırmızıya izin verir (satır 159, `s` çizgisi); emsal 02-04 "kırmızı yok" der. İstemler kırmızıyı yalnız sahne 02'deki `s` çizgisine bağladı.
9. **Emsal sahneleri henüz v1** (19:1x: `02-04-ydt-temel-s1/sahneler/08-hyperframes-kaydet/` yok). İstemler: emsal `RAPOR.md` "huni v2" diyorsa v2 taban,
   demiyorsa yapı v1'den, v2 yerleşimi istemden. Sahne 01 ve 02 eşleşmesi için sabitler iki istemde aynı (`Kardeşim gider:` taban 560, kart satırı y 620–820).
10. **Durağan kareler** (05–08) çakışma kapısıyla ölçülemez (çıkış 2 beklenir); istemlerde gözle denetim.
11. **Adlandırma.** İstem gövdesindeki `BRIEF-S2.md` ve `kimlik s2` S1 için `BRIEF-S1.md` ve `s1` yazıldı (huni v2 bölümü `s<N>` kalıbı; emsal adı).
12. **Açıklama:** `https://ydspublishing.com/grammar/02-02-ydt-temel` canlılığı ölçülmedi; `{UZUN_VIDEO_URL}` ana ders yüklenince dolar; `{PLATFORM_URL}` koşullu.
13. Git: eski kısanın izlenen dosyaları taşındığı için `git status`'ta silinmiş görünür; commit yok.
