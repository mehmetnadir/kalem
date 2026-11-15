# RAPOR — 02-04-ydt-temel-s2 · sahne 06-hyperframes-kapak-c (Kapak C, karşıt çift)

15.11.2026 · istem D-S2 · srv21 (Linux x86_64). HyperFrames, 1080×1920, tek kare, ses yok, zaman çizelgesi dışı (`zaman.json` → `duragan`).
Tema: açık (teslim) + koyu.

| Öğe | Durum |
|---|---|
| Teslim | `P/kapak-c.png` (açık, 1080×1920) · `D/k/koyu/kapak-c-koyu.png` (koyu, 1080×1920) |
| Kod | `uret.py` agy yazdı (SPEC.md); şef 1 küçük düzeltme yaptı (QA 1) |
| Boy | başlık S = 190 · kart yazısı B = 72 (Fredoka 700) |
| `calistir.sh` | `ONIZLE_YALNIZ=1` rc 0 · `--tema acik` rc 0 · `--tema koyu` rc 0 |
| mp4 | YOK (tek kare yakalama; birleştirme yok) |

## Olay listesi

| Olay | Kare / küresel sn | Cümle sözcüğü |
|---|---|---|
| kare tam görünür (iki `set`, hareket yok) | kare 0 · yakalama 0,5 sn · zaman çizelgesi dışı | yok (ses yok) · `olaylar.json` = `[]` |

## Yerleşim (nesneler.json)

| Blok | x, y, w, h |
|---|---|
| hud (logo 48/48 h 96 · rozet `YDT · BASIC` 48/216 h 72) | 48, 0, 984, 288 |
| baslik `AYNI FİİL,` / `İKİ ZAMAN` (mürekkep + kontur, hapsız) | 77, 340, 926, 424 |
| kart1 · `She wears her coat` / `in the winter.` · mont (sağ üst) | 48, 864, 984, 232 · mont 874, 892, 117, 140 |
| kart2 · `She is wearing her` / `pink T-shirt today.` · tişört (sağ üst) | 48, 1112, 984, 232 · tişört 862, 1147, 140, 126 |
| k2-alti (tek sarı: `is wearing` el altçizgisi) | 219, 1220, 337, 12 |

Satır kırılımı ana ders `sahne-03.js` `SAT` ile aynı. Mont ve tişört `sahne-03.js` `MONT` / `TISORT` darbe dizilerinden (birebir, px'e ölçek).
`today` ve `wears` vurgusuz. Figür yok. 1344–1536 ve 1536–1920 boş.

## Kapı sonucu (son satırlar)

```
$ ONIZLE_YALNIZ=1 bash calistir.sh
index.html yazıldı 7581 · S=190 B=72 · olay 0 · önizleme hazır          (rc 0)
$ bash calistir.sh --tema acik
png,1080,1920 · …/02-04-ydt-temel-s2/kapak-c.png                       (rc 0)
$ bash calistir.sh --tema koyu
png,1080,1920 · …/06-hyperframes-kapak-c/k/koyu/kapak-c-koyu.png        (rc 0)
```

`uret.py` assert'leri geçti: bant sınırları, kesişim 0 (üst düzey + kart içi), başlık–HUD ≥ 40, başlık–kart ≥ 48, satır ≤ 24 karakter,
yazı ≥ 64, altçizgi iki satır arasında. qa-yerel, çakışma kapısı ve sahne-kare koşulmadı (istem: durağan sahne `sahneler[]` dışında).

## Bakılan kareler ve bulgu

| Kare | Bulgu |
|---|---|
| `k/at-0.5s.png` = `P/kapak-c.png` (açık) tur 1 | temiz; `wearing` `g` kuyruğu ile altçizgi arası ≈ 7 px (sıkışık) → QA 1 |
| aynı, tur 2 (QA 1 sonrası) | temiz: taşma, kesik yazı, üst üste binme yok; kuyruk–altçizgi ≈ 10 px, altçizgi–alt satır ≈ 12 px; İ noktaları ve virgül çakışmaz |
| `k/koyu/kapak-c-koyu.png` (koyu) tur 2 | temiz; rozet `#f2a93b`, altçizgi turuncu, mürekkep krem; kontrast yeterli |

QA 1 (şef Edit, 3 sayı): kart satır tabanları üst + 86 / 182 → 84 / 184 (satır aralığı 100); altçizgi `0,36·B` → `0,40·B`
(sözleşme kuralı: taban + max(0,28 em, kuyruk + 13)). SPEC.md aynı değerlere güncellendi.

## agy koşu özeti

`/home/sef/.claude/canavar/agy-filo/20261115-124930` · rol `kod` · gemini-3.8-flash-high · başarılı · 168 sn · 1 tur.
Özetteki "değişen" listesi bütün çalışma ağacıdır (paralel oturumlar); agy'nin yazdığı: `uret.py` (+ kendi koşusunun `proje/index.html`,
`nesneler.json`).

## Açık noktalar

1. **Logo yeri:** istem ve BRIEF-S2 "logo sol alt y ≈ 1478" der; BRIEF-DIKEY §0 (Nadir bulgusu) "logo HUD sol üst 96 px, alt bantta logo yok"
   der. S1 kapak A/B/C ve hikâye kareleri Nadir bulgusunu uyguladı. Bu kare de logoyu HUD sol üste koydu (seri tutarlılığı). Sol alt
   istenirse yalnız `kunye_svg()` logo y değeri değişir. BRIEF-S2 / `kapak-taslak.md` satırı güncellenmeli (yazma kapsamı dışı).
2. **Çip:** istem genel kuralı `KUNYE.cipler["06-hyperframes-kapak-c"]` (`Hook`) der; BRIEF-S2 C sütunu HUD'da yalnız rozet ister ve S1
   kapak C'de çip yok. Çip konmadı.
3. **Altçizgi rengi açık temada `#d9900f`** (hf_tema `stroke vurgu` dönüşümü; S1 hikâye odak çizgisiyle aynı). Hap dolgusu `#ffe066` yalnız
   `rect` için geçerli.
4. Ekran metni taraması: `index.html`'de "kanal", QR, süre yok; `uret.py`'de 140 karakteri aşan satır yok (awk ölçümü).
