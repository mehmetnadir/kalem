# S3-SON RAPOR — huni dosyaları denetimi (15.11.2026)

## Dosya listesi

| Dosya | Durum | Not |
|---|---|---|
| `kapak-a.png` + `kapak.png` | ÜRETİLDİ | aynı dosya (`cmp` eşit), 1080×1920 |
| `kapak-b.png` | VAR | 1080×1920 |
| `kapak-c.png` | VAR | 1080×1920 |
| `hikaye-a.png` + `hikaye.png` | VAR | 1080×1920 |
| `hikaye-b.png` | VAR | 1080×1920 |
| `aciklama-a.md`, `aciklama-b.md`, `aciklama.md` | VAR | bu işte dokunulmadı |
| `sahneler/01-hyperframes-kapak/k/koyu/kapak-a-koyu.png` | ÜRETİLDİ | koyu tema, altyazısız, 1080×1920 |
| `uretim-tutanagi/huni-surumler.json` | GÜNCEL | 7 satır, hepsi `inceleme`, `dosya` adları kökle eşleşir |
| `uretim-tutanagi/kontak/s3-huni-yanyana.png` | ÜRETİLDİ | 1800×640 (5 × 360×640) |

`surumler.json` kısa video satırı `kimlik` zaten `s3`; değişiklik gerekmedi.

## Kapak A yöntemi
Sahne 01 `proje` kopyasında (`proje-ka`, `proje-ka-koyu`) yalnız CSS `#altyazi{display:none !important}` eklendi. Sahne kodu değişmedi.
Kare `hyperframes snapshot --at 1.97` ile alındı. Koyu kopyada `hf_tema.py ... koyu` koşuldu. Sahnenin `proje/` klasörüne dokunulmadı.

## Bakılan kareler (Read ile)
`kapak-a`, `kapak-b`, `kapak-c`, `hikaye-a`, `hikaye-b`, `s3-huni-yanyana`. Koyu `kapak-a-koyu.png` yalnız `file` ile ölçüldü; görsel bakış yok.

## Bulgular
- Altyazı bandı: hiçbir karede yok. Kapak A'da bant çıktı; `The train to İzmir` künye/kart satırıdır, altyazı değil.
- Başlık 2 satır: A `TARİFE` / `≠ PLAN`, B `NEDEN -ING` / `YOK?`, C `İKİ ÖRNEK` / `İKİ ZAMAN`. Rozet `YDT · BASIC` ve logo hepsinde yerinde.
- A, B, C belirgin farklı (öğretmen+saat+tren / soru işareti+tek kart / iki üst üste kart).
- Hikâye B'de cevap yok: yalnız A `TARİFE` / B `PLAN` seçenekleri.
- Taşma/kesik yazı yok.

## Kusurlar (sahne değiştirilmedi)
1. Bütün 5 karede alt ~400 px (y ≈ 1500–1920) boş. Shorts/Reels arayüz alanı için bilinçli olabilir; karar Nadir'de.
2. `kapak-b.png`: `NEDEN -ING` kenarlardan ≈ 65 px kalıyor, güvenli alanın sınırında.
3. `kapak-c.png`: `İKİ ZAMAN` sarı hapı sol-sağ ≈ 68 px kenar boşluğu; başlık bloğu A ve B'den daha sıkışık.
4. Hikâye A ve B: üst başlık ile rozet yan yana sıkışık (`PRESENT CONTINUOUS` ↔ rozet arası ≈ 25 px). Okunur, taşma yok.

## Açık noktalar
- Koyu tema B, C ve hikâye kareleri üretilmedi (istenmedi).
- `aciklama-*.md` içeriği bu işte denetlenmedi.
- Alt boşluk kararı (kusur 1) verilirse sahne 01, 04–07 yerleşimi ayrı işte değişir.
