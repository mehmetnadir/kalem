# RAPOR v2 — 02-04-ydt-temel-s2 · sahne 06-hyperframes-kapak-c (Kapak C, karşıt çift; huni v2)

15.11.2026 · istem D-S2-V2 · srv21 (Linux x86_64). HyperFrames, 1080×1920, tek kare, ses yok, zaman çizelgesi dışı (`zaman.json` → `duragan`).
Tema: acik

| Öğe | Durum |
|---|---|
| Teslim | `P/kapak-c.png` (açık, 1080×1920) · `D/k/koyu/kapak-c-koyu.png` (koyu, 1080×1920) |
| Kod | `uret.py` agy yazdı (SPEC.md v2), şef baştan sona okudu; düzeltme gerekmedi · `yardim.py` = S2 sahne 01 v2 kopyası (şef) · `calistir.sh` şef Edit (v2 kalıbı: `GEN=1080; YUK=1920`, ffprobe boyut denetimi) |
| Boy | başlık S = 151 (bant yüksekliği sınırlar) · kart yazısı B = 72 (Fredoka 700) |
| `calistir.sh` | `ONIZLE_YALNIZ=1` rc 0 · `--tema acik` rc 0 · `--tema koyu` rc 0 |
| mp4 | YOK (tek kare yakalama; birleştirme yok) |

## Olay listesi

| Olay | Kare / küresel sn | Cümle sözcüğü |
|---|---|---|
| kare tam görünür (iki `set`, tween yok) | kare 0 · yakalama 0,5 sn · zaman çizelgesi dışı | yok (ses yok) · `olaylar.json` = `[]` |

## Yerleşim (nesneler.json; huni v2 §2)

| Blok | x, y, w, h |
|---|---|
| kanal (`<g id="kanal">`: logo `logoimg` x 53,15 y 291 h 48 w 193,5 + `@ydspublishing` Lexend 700 42 x 263 taban 330) | 60, 291, 542, 52 |
| kunye (konu `Simple Present vs Present Continuous` Fredoka 700 34, taban 420 + rozet `YDT · BASIC` y 386–434) | 60, 386, 808, 48 |
| baslik `AYNI FİİL,` / `İKİ ZAMAN` (mürekkep + zemin konturu, hapsız, x 60 sol hizalı) | 60, 460, 732, 340 |
| kart1 · `She wears her coat` / `in the winter.` · mont (sağ üst) | 60, 840, 900, 256 · mont 802, 868, 117, 140 |
| kart2 · `She is wearing her` / `pink T-shirt today.` · tişört (sağ üst) | 60, 1124, 900, 256 · tişört 790, 1159, 140, 126 |
| k2-alti (tek sarı: `is wearing` el altçizgisi) | 231, 1244, 337, 12 |

0–280 ve 1400–1920 yalnız zemin. İçerik x 60–960. Çip, sol alt logo, `Hook` çipi, figür, altyazı YOK. `today` ve `wears` vurgusuz.
v1 → v2: v1 HUD (logo y 48 h 96, rozet y 216) kalktı; kanal katmanı + künye `Y.kunye_svg()`; başlık 190 → 151 (bant 460–800);
kartlar x 48–1032 → 60–960, y 864–1344 → 840–1380 (h 232 → 256); ikon x 862 → 790.

## Kapı sonucu (son satırlar)

```
$ ONIZLE_YALNIZ=1 bash calistir.sh
index.html yazıldı 7876 · S=151 B=72 · olay 0 · önizleme hazır                 (rc 0)
$ bash calistir.sh --tema acik
png,1080,1920 · …/02-04-ydt-temel-s2/kapak-c.png                              (rc 0)
$ bash calistir.sh --tema koyu
png,1080,1920 · …/06-hyperframes-kapak-c/k/koyu/kapak-c-koyu.png               (rc 0)
$ node araclar/cakisma-kapisi.mjs 02-04-ydt-temel-s2 --sahne 06-hyperframes-kapak-c --port 41333 --sunucu 41022
HATA sahne bulunamadı: 06-hyperframes-kapak-c                                  (rc 2; beklenen: durağan sahne sahneler[] dışında)
$ grep -rniE "tam ders|dakika" … --exclude-dir=k
(boş, rc 1)
```

`uret.py` assert'leri geçti: yardim.py v2 değerleri (logo 291/48, kanal 263/330/42, konu 60/420, rozet 386/48/26, `ku-cip` yok),
bant sınırları, kesişim 0 (üst düzey + kart içi), başlık–künye ≥ 10, başlık–kart ≥ 20, satır ≤ 24 karakter, yazı ≥ 64, altçizgi iki satır arasında.
`index.html`'de `tl.to/from` 0 (yalnız iki `set`); `id="kanal"` 1 kez. qa-yerel koşulmadı (istem: sahnenin anlatım saniyesi yok).

## Bakılan kareler ve bulgu

| Kare | Bulgu |
|---|---|
| `P/kapak-c.png` (açık) = `k/at-0.5s.png` (md5 `50d0996d4d85…`) | temiz: kanal katmanı y 291–339 yerinde; taşma, kesik yazı, üst üste binme yok; virgül kuyruğu ile 2. satır İ noktaları çakışmaz; içerik x 960 içinde; 0–280 ve 1400–1920 boş |
| aynı, piksel ölçümü | `wearing` `g` kuyruğu alt 1234 → altçizgi 1244–1254 (ara 10 px) → 2. satır üst 1268 (ara 14 px) |
| `k/koyu/kapak-c-koyu.png` (koyu) | temiz; kanal katmanı (şeffaf logo + krem `@ydspublishing`) yerinde; rozet `#f2a93b`, altçizgi turuncu, mürekkep krem; kontrast yeterli |

Durağan kare: ilk = orta = son kare (tek kare, tween yok). Düzeltme turu: 0.

## agy koşu özeti

`/home/sef/.claude/canavar/agy-filo/20261115-190725` · rol `kod` · gemini-3.8-flash-high · başarılı · 198 sn · 1 tur.
Özetteki "değişen" listesi bütün çalışma ağacıdır (paralel oturumlar: S1 04/06, S2 04); agy'nin yazdığı: `uret.py` (+ kendi koşusunun
`proje/index.html`, `nesneler.json`).

## Açık noktalar

1. **Altçizgi rengi açık temada `#d9900f`** (hf_tema `stroke vurgu` dönüşümü; v1 ile aynı). İstemdeki `#ffe066` hap dolgusudur, yalnız `rect`'e geçer;
   ince çizgide `#ffe066` krem zeminde okunmaz.
2. **Çakışma kapısı durağan sahneyi ölçmüyor** (`sahne bulunamadı`, rc 2; araç sınırı, değiştirilmedi). Çakışma karede gözle ve `uret.py` kutu assert'leriyle denetlendi.
3. **Rozet dili** `YDT · BASIC` (paket + S1); standart örneği `YDT · TEMEL` (V2-C-RAPOR açık nokta 3; karar Nadir'de).
4. **Konu satırı 34 px** (`Y.konu_boyu()` üst sınır); rozet sağ kenarı 868 ≤ 960.
