# 07-hyperframes-hikaye-b — RAPOR (15.11, istem D-S3; mp4 yok)
Tema: acik + koyu (iki kare)

| Alan | Değer |
|---|---|
| Motor | HyperFrames · 1080×1920 · tek kare, durağan, ses yok · zaman çizelgesi dışı (`zaman.json` → `duragan`, `sahneler[]` dışında) |
| Çıktı | açık `../../hikaye-b.png` (paket kökü) · koyu `k/koyu/hikaye-b-koyu.png` · ikisi `png,1080,1920` (ffprobe) |
| Dosyalar | `uret.py` (agy yazdı, SPEC.md'den) · `SPEC.md` · `calistir.sh`, `olay.py`, `zamanlar.json`, `yardim.py` (S1 sahne 07 kopyası; başlık satırları uyarlandı) · `nesneler.json`, `olaylar.json` (üretilir) |
| Kaynak | BRIEF-S3 "Hikâye karesi B" · `uretim-tutanagi/hikaye-taslak.md` §3 (S3-C) · `S3-duzeltme.md` madde 2 · ana ders `05-canvas-ornek3/sahne.js` `trenParcalari` / `saatParcalari` · `13-hyperframes-mini-soru` şık kalıbı |
| Kapı | `uret.py` iç kuralları (SPEC §6) geçti · `ONIZLE_YALNIZ=1` rc 0 · `--tema acik` rc 0 · `--tema koyu` rc 0 · qa-yerel koşulmadı (istem gereği: sahne `sahneler[]` dışında) |

## Ekran metni ve olay listesi
Ses ve olay yok (`olaylar.json` = `[]`). Kare 1, yakalama 0,5 sn. Öğeler (y = yazı tabanı, px):

| Öğe | Metin | Ölçü | Konum |
|---|---|---|---|
| HUD | `SIMPLE PRESENT vs` / `PRESENT CONTINUOUS` · rozet `YDT · BASIC` · çip `Full lesson` (`KUNYE.cipler["07-hyperframes-hikaye-b"]`, kunye.js'ten okunur) | 56 / 36 / 40 | 0–288 |
| Soru | `Tarife mi, plan mı?` | Fredoka 700 96, mürekkep | taban 448 (376–472) |
| Cümle kartı | tren (ölçek 1,2) + saat (r 96, akrep 7, yelkovan 12, rakamsız) · `The train to İzmir` / `leaves at 7 pm today.` | Fredoka 700 64; vurgu yok | çerçeve 512–1014 |
| Şıklar | `A` `TARİFE` · `B` `PLAN` (yan yana, harf rozeti mürekkep çerçeve) | Fredoka 700 72 (harf 64) | 1054–1274 |
| Çağrı | `Cevap tam derste:` / `profildeki bağlantı` · `@ydspublishing` hap | Caveat 700 72 · Fredoka 700 64 | 1364–1520 |
| Platform | boş | — | 1536–1920 |

İçerik bandı doluluğu: (1274 − 376) / 1040 = %86,3. Satır en uzun `leaves at 7 pm today.` = 21 karakter.

## Bakılan kareler ve bulgu
| Kare | Bulgu |
|---|---|
| `../../hikaye-b.png` (açık) | taşma yok · kesik yazı yok · üst üste binme yok · kontrast iyi · hap dolgu `#ffe066`, yazı `#1b2440` (piksel ölçümü) · 1290–1350 ve 1540–1920 yalnız zemin + vinyet (parlaklık 217–241) |
| `k/koyu/hikaye-b-koyu.png` (koyu) | aynı yerleşim · hap `#f2a93b` · 1540–1920 parlaklık 16–25 (boş) |

Cevap karede yok; doğru şık yeşil değil; iki şık aynı biçim. Sarı öğe yalnız rozet, çip, `@ydspublishing` hapı. `İzmir` noktalı İ,
`7 pm` rakamla. "kanal", QR, süre, emoji, kırmızı, yeşil yok. Düzeltme turu gerekmedi (0 / 4).

## agy koşu özeti
`agy-filo tek --rol kod` · gemini-3.8-flash-high · başarılı · 326 sn · özet `~/.claude/canavar/agy-filo/20261115-124453/ozet.md`.
Şef okuması: kod SPEC'e uyuyor, Edit gerekmedi. agy özetindeki "değişen" listesi (S2 03-cta, sozlesme.md) eş-oturum izidir;
SPEC'ten sonra ana ders, S1, dikey paket, S3 `ortak/`, `zaman.json`, `BRIEF-S3.md` içinde değişen dosya yok (`find -newer SPEC.md`).

## Açık noktalar
1. Logo: BRIEF-S3 hikâye B tablosu çağrı bandında "logo sol alt" der. BRIEF-DIKEY §0 "alt bantta logo yok" der; S1 hikâye B de logoyu
   yalnız HUD'da taşır. Logo HUD'da kaldı; alt bantta Caveat + hap ile yer de yok.
2. Bantlar: BRIEF tablosu soruyu 300–420'ye koyar; içerik bandı alt sınırı 352 olduğundan soru 376–472'ye, kart ve şıklar aşağı kaydı
   (sıra aynı, 1344 üstünde biter). BRIEF'teki "1190–1300 boş" satırı doluluk kuralı (≥ %85) için şık kutusuyla kullanıldı.
3. Çip: kunye.js bu sahneye `Full lesson` verir (S1 hikâye B'de `Quiz`). Değişiklik ortak dosyada; istenirse `ortak/kunye.js` sahibi düzeltir.
