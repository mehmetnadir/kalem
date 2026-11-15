# RAPOR — simple-present-temel-s3 · sahne 07-hyperframes-kapak-c (huni v2) · 15.11.2026

| Ölçüm | Değer |
|---|---|
| `calistir.sh --tema acik` | çıkış 0 · `P/kapak-c.png` PNG 1080×1920 |
| `calistir.sh --tema koyu` | çıkış 0 · `k/koyu/kapak-c-koyu.png` PNG 1080×1920 |
| `uret.py` | `index.html yazıldı 7022` · `S=147` · SPEC §6 assert'leri geçti |
| Çakışma kapısı | çıkış 2 · `HATA sahne bulunamadı: 07-hyperframes-kapak-c` (beklenen: araç yalnız `zaman.json → sahneler[]` okur; karede gözle denetlendi) |
| Metin taraması (`tam ders`, `dakika`; html/js/py) | boş (grep çıkış 1) |
| Kanal katmanı (iki kare, piksel, eşik 60, satır zemini x 0–40 medyanı) | logo mürekkebi x 60–239, y 298–330 (resim 291–339) · `@ydspublishing` x 264–596, y 296–339 (taban 330); emsal 06 v2 ölçümüyle aynı |
| Künye (piksel) | x 60–512, y 386–433 |
| İçerik (piksel) | x 60–959, y 473–1299 |
| Boş bölgeler (piksel) | y 0–280: 0 · y 1385–1920: 0 · x 961–1080: 0 · x 40–59: 0 (iki tema) |

P = `K/projeler/simple-present-temel-s3/`. Tek kare: ilk = orta = son (çizelge 1,0 sn, yakalama 0,5 sn).

## Olay listesi
Durağan kare; ses, altyazı, çip, figür, karakter görseli yok. `olaylar.json` = `[]`.

| Olay | Kare / küresel sn | Cümle sözcüğü |
|---|---|---|
| kapak tam görünür (kanal, künye, başlık, kart 1, kart 2) | kare 0 → son (zaman çizelgesi dışı) | — (anlatımdan bağımsız) |

## Yerleşim (nesneler.json)
| Blok | x · y · w · h | İçerik |
|---|---|---|
| kanal | 60 · 280 · 542 · 70 | `Y.kunye_svg()` → `#kanal` (`#logoimg` + `@ydspublishing`) |
| kunye | 60 · 360 · 453 · 90 | `Simple Present` (Fredoka 700 34) + rozet `YDT · BASIC` |
| baslik | 60 · 470 · 900 · 278 | `DOES VARSA` / `FİİL YALIN`, Fredoka 700 147 (motor ölçtü), mürekkep, zemin renginde 10 px kontur, hap yok; tabanlar 576,6 / 741,2 |
| kart1 | 60 · 840 · 900 · 200 | soluk (`ikincil`): `He doesn't go` + `es` (tspan) + `.`, Fredoka 72; kırmızı çizgi yalnız `es` üstünde; sağda kırmızı kalem `✗` (SVG yol) |
| kart2 | 60 · 1100 · 900 · 200 | `He doesn't go.` Fredoka 72 mürekkep; sağda `✓` (SVG yol); `go` altında sarı el altçizgisi (tek sarı öğe) |

Aralar: başlık altı → kart 1: 92 px · kart 1 → kart 2: 60 px · yazı sonu → işaret: ≥ 217 px. Çiftler arası kesişim 0.
Renk sayımı (html): kırmızı 2 (`k1-cizik`, `k1-carpi`), vurgu 2 (künye rozeti, `k2-alt`); yeşil, emoji, `✗`/`✓` karakteri yok.

## Değişen dosyalar (hepsi sahne dizininde, klasör yeni)
- `calistir.sh`, `olay.py`, `zamanlar.json`: emsal `02-04-ydt-temel-s1/sahneler/06-hyperframes-kapak-c/` kopyası; Edit: başlık yorumu, paket adı
  yorumu, `uret.py`/`olay.py` ayrı satır (S3 s05 kalıbı; `a && b` zincirinde `set -e` hatayı yutar). Çıktı adı (`kapak-c.png`) aynı kaldı.
- `yardim.py`: emsal 06 v2 kopyası; Edit: docstring + `KONU = "Simple Present"` (`KONU_PARCA` kalktı, kullanılmıyordu). Kanal/künye değerleri değişmedi.
- `SPEC.md` (şef), `uret.py` (agy yazdı; şef baştan sona okudu).
- Üretilen: `nesneler.json`, `olaylar.json`, `proje/` (önizleme açık temada bırakıldı), `k/at-0.5s.png`, `k/koyu/*`, `P/kapak-c.png`.
- Sahne dışı tek satır: `K/.claude/docs/sozlesme.md` sonuna 1 satır eklendi (istemdeki tek istisna).

## Şef düzeltmeleri (agy çıktısı üstüne, Edit)
1. `assert S == 147` kaldırıldı: boy motor ölçer (SPEC §4.2); sabit eşitlik yazı tipi değişince yanlış alarm verir.
2. QA tur 1: `es` çizgisinin sol ucu `x_es + 2` → `x_es + 4` (yuvarlak uç `o`ya 1–2 px değiyordu; Fredoka 72'de `o` ve `e` bitişik). SPEC'e de işlendi.
Düzeltme turu: 1 (en çok 4).

## Bakılan kareler
| Kare | Bulgu |
|---|---|
| `P/kapak-c.png` (= `k/at-0.5s.png`, açık) | taşma, kesik yazı, üst üste binme, boş kare YOK; 0–280 ve 1400–1920 boş; x 960+ boş; kanal + künye tablodaki yerde; altçizgi `#d9900f` (açıkta `--vurgu`), çizgi `g` kuyruğuna değmiyor |
| `k/koyu/kapak-c-koyu.png` | aynı yerleşim; başlık krem, kart 1 `#c9c2b3`, kart 2 `#f3efe6`; altçizgi `#f2a93b`; kontrast iyi |
| `/tmp/kapakc-s3/cizik2.png` (açık, `goes` büyütme) | kırmızı çizgi `e`nin sol kenarından `s`nin sağ kenarına; `.`ya değmiyor |
| `/tmp/kapakc-s3/alt.png` (açık, `go.` büyütme) | altçizgi `go` altında, kuyrukla arası ≈ 4 px |

## agy koşu özeti
`~/.claude/canavar/agy-filo/20261115-194825/ozet.md` — 1/1 başarılı · 160 sn · rol `kod` · gemini-3.8-flash-high · girdi 1.817.672 / çıktı 77.896 token.
Özetin "değişen" listesinde `simple-present-temel-s1` dosyaları ve `sozlesme.md` de var: bunlar paralel oturumların işi; agy yalnız `uret.py` yazdığını bildirdi
(sözleşme satırını şef agy'den sonra ekledi).

## Açık noktalar
1. Çakışma kapısı durağan kareleri ölçmez (çıkış 2). Denetim piksel ölçümü ve göz denetimiyle yapıldı.
2. İstemin "y 1150–1380 boş zemin mi" denetimi hikâye karesi kuralıdır (standart §6). Kapak C kartı BRIEF'e göre 1100–1300'de; bu bölge bilerek dolu.
3. Koyu temada kart 1'in solukluğu (`ikincil` `#c9c2b3` ↔ `#f3efe6`) açık temadakinden az. Paket içi hikâye A ile aynı renk kuralı; istenirse kart 1'e ek opaklık verilir.
4. Açık temada başlık konturunun soluk halesi (emsal 06 ile aynı kalıp; vinyet zemini kontur renginden biraz koyu). Okunurluğu bozmaz.
5. Platform arayüzü bölgeleri (üst 0–250, alt 1580+, sağ 960+) üçüncü taraf ölçümüdür; yayın öncesi gerçek ekranda doğrulanmadı (standart §2).
