# RAPOR v2 — 02-04-ydt-temel-s3 · 07-hyperframes-hikaye-b (hikâye B, soru + cevap) · huni v2 · 15.11.2026

Tema: acik + koyu (iki tema çekildi)

| Kalem | Sonuç |
|---|---|
| Çıktı | `P/hikaye-b.png` (açık) · `D/k/koyu/hikaye-b-koyu.png` (koyu) · ikisi `png 1080×1920` (ffprobe; `calistir.sh` boyut denetimi rc 0) |
| Kod | `uret.py` agy yazdı (SPEC v2) · şef 3 küçük düzeltme (§Düzeltme turları) · `calistir.sh` şef: başlık, boyut denetimi (çıkış 3), `uret.py` / `olay.py` ayrı satır |
| İç kurallar | `uret.py` assert'leri geçti: bantlar, kesişim 0, dikey boşluk ≥ 10, kart içi ve şık içi paylar, yazı ≥ 64, satır ≤ 24, yasak dizgi, emoji yok, `#root.tema-acik` yok · `S_SORU=96` · nesneler.json 12 kayıt |
| Çakışma kapısı | çıkış 2 (ölçülemedi; araç sınırı, sahne `sahneler[]` dışında) |
| Metin taraması | `grep -rniE "tam ders\|dakika" …/proje` → sonuç yok (rc 1) |
| Kanal katmanı | açık + koyu: logo ve `@ydspublishing` görünür, sol kenar x 60, y 291–339 içinde |

## Öğe listesi

| Öğe | Kimlik | y bandı | Yazı boyu |
|---|---|---|---|
| Kanal: logo (tema logosu) | `#kunye > #kanal > #logoimg` | 291–339 (resim x 53,15, w 193,49) | — |
| Kanal: `@ydspublishing` | `#kanal-yazi` | taban 330 | Lexend 700 42 |
| Künye konu `Simple Present vs Present Continuous` | `#ku-konu` | taban 420 | Fredoka 700 34 |
| Rozet `YDT · BASIC` (sarı hap) | `#rz0` | 386–434 | Lexend 700 26 |
| Soru `Tarife mi, plan mı?` | `#soru` | 462–553 (taban 532) | Fredoka 700 96 |
| Cümle kartı çerçevesi | `#kart-crv` | 580–760, x 60–960 | — |
| `The train to İzmir` | `#kart-s1` | taban 655 | Fredoka 700 64 |
| `leaves at 7 pm today.` + `leaves` sarı altçizgi | `#kart-s2`, `#alti` | taban 730 · altçizgi 733–751 | Fredoka 700 64 |
| Tren (sağ üst) + saat (kollar yedide, rakamsız) | `#kart-tren`, `#kart-saat` | 594–656 · 676–749 | — |
| Şık A `A` `TARİFE` (yeşil çerçeve + kalem ✓) | `#sA` | 779–901, x 60–498 | harf 64 · yazı Fredoka 700 72 |
| Şık B `B` `PLAN` (soluk, opaklık 0,4) | `#sB` | 780–900, x 522–960 | harf 64 · yazı Fredoka 700 72 |
| Kural özeti `Tren tarifeye uyar:` / `geniş zaman.` | `#kural` | 920–1059 (taban 970 / 1043) | Lexend 500 64 / Lexend 700 64 |
| Yer imi simgesi (SVG yol) + `Kaydet` | `#kaydet-imi`, `#kaydet-yazi` | 1072–1137 (taban 1122) | Fredoka 700 64 |
| Bağ çıkartması yeri | — | 1150–1380 boş zemin | — |
| Alt boş | — | 1400–1920 boş; altyazı yok | — |

Renk: tek sarı içerik öğesi `leaves` altçizgisi (+ künye rozeti, standart parça). Yeşil yalnız şık A çerçevesi ve ✓
(açıkta `#167a4a`, koyuda `#3a9a6a`; sahne CSS'i `.tema-acik #sahne .dogru`). Kırmızı yok, emoji yok. `İzmir` noktalı, `7 pm` rakamla.

## Kanal katmanı ölçümü (PNG piksel taraması, mürekkep/doygun piksel kutusu)

| Tema | Logo görünür kutu (x0, y0, x1, y1) | Yazı görünür kutu | 0–280 | x 962+ | y 1146+ | İçerik kutusu |
|---|---|---|---|---|---|---|
| açık | 60, 298, 239, 330 | 265, 296, 596, 339 | boş | boş | boş | x 60–959, y 462–1136 |
| koyu | 60, 298, 239, 330 | 265, 296, 596, 339 | boş | boş | boş | x 60–959, y 462–1136 |

## Kapı (son satırlar, aynen)

```
$ node araclar/cakisma-kapisi.mjs 02-04-ydt-temel-s3 --sahne 07-hyperframes-hikaye-b --port 41333 --sunucu 41022
HATA sahne bulunamadı: 07-hyperframes-hikaye-b
çıkış=2
```

## Bakılan kareler ve bulgu

Tek kare (ilk = orta = son): `P/hikaye-b.png` (açık), `D/k/koyu/hikaye-b-koyu.png` (koyu). Read ile açıldı.
- Taşma, kesik yazı, üst üste binme yok. Kontrast iki temada yeterli; soluk şık B okunur ama geri planda.
- 0–280 boş; içerik x 960'ı aşmaz; 1150–1920 boş; altyazı yok.
- v1 öğeleri (üst logo 48–144, 2 satır ders adı, `Full lesson` çipi, büyük tren, Caveat çağrı satırı, alt `@ydspublishing` hapı) yok.

## Düzeltme turları (2 / 4)

1. Açık kare koyu çıktı (rc 0, boyut doğru). Sebep: SPEC'teki yerel kural `#root.tema-acik .dogru` → `hf_tema.py` bu dizgiyi görünce
   dosyayı "çevrilmiş" sayıp renk değişkenlerini eklemedi. Düzeltme: seçici `.tema-acik #sahne .dogru` + assert; SPEC §3/§8 güncellendi;
   ders `K/.claude/docs/sozlesme.md` son satırına yazıldı.
2. Şık A'nın 6 px çerçevesi dış kenarı x 59'a taşıyordu (piksel ölçümü). Düzeltme: rect x 63, w 432 (dış 60–498), blok `sA` x 60, kural 1 x ≥ 60.
- Ek (önleyici, sözleşme satır 91): `calistir.sh`'te `uret.py && olay.py` tek satırdaydı; `set -e` uret.py hatasını yutup eski
  `index.html`'i yakalatabilirdi → iki ayrı satır.

## agy koşusu

`~/.claude/canavar/agy-filo/20261115-191627/ozet.md` — rol `kod`, gemini-3.8-flash-high, 202 sn, başarılı, tek dosya `uret.py`.
Şef okuması: kod SPEC'e uyuyor; iç öğe kutuları (tren, saat, alti, tik) sabit sayı olarak yazılmış, PNG ölçümüyle tutarlı.

## Açık noktalar

- agy özetinin "değişen" listesinde `.claude/docs/sozlesme.md` ve `02-03-ydt-temel/sahneler/90-hyperframes-kapak/*` görünür. agy dökümünde
  (`tek.d1.out`) bu yollar yok; dosyalar agy bittikten sonra (19:20, 19:21) değişti → eş zamanlı başka oturumun işi.
- Ana derste (13-hyperframes-mini-soru) "ham yeşil yok" kararı var (13.11 QA); bu karede yeşil, istem ve standart gereği kullanıldı.
- `Kaydet` satırı ile `geniş zaman.` arası 13 px (bantlar 920–1060 ve 1070–1140 sabit); göze sıkışık gelirse kural özeti 1 satıra
  (`Tarife: geniş zaman.`) indirilebilir.
- Çakışma kapısı bu sahneyi ölçmez (çıkış 2); yerine `uret.py` iç kuralları + piksel taraması.
