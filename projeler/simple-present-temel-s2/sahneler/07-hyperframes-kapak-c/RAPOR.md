# RAPOR — simple-present-temel-s2 · 07-hyperframes-kapak-c (huni v2, durağan kare) · 15.11.2026

| Konu | Sonuç |
|---|---|
| Çıktı (açık) | paket kökü `kapak-c.png` · 1080×1920 PNG · `calistir.sh --tema acik` rc 0 |
| Çıktı (koyu) | `k/koyu/kapak-c-koyu.png` · 1080×1920 PNG · `calistir.sh --tema koyu` rc 0 |
| Başlık | `ÜÇ İFADE,` / `TEK İŞARET` · Fredoka 700 · S = 143 (y 462–799; boyu 460–800 bandı sınırlar, genişlik 774 px) |
| Karakter ölçeği | s = 0,465 · görünür x 672,7–948, y 833–1309 · parmak ucu y ≈ 1122 (kartın `every day` satırı) |
| Çakışma kapısı | çıkış 2 `HATA sahne bulunamadı` (beklenen; araç yalnız `sahneler[]` okur) |
| Metin taraması | boş (grep rc 1) |
| Kanal katmanı | iki karede de görünür; konum ve boy tabloyla aynı (ölçüm aşağıda) |
| Kod yolu | `SPEC.md` (şef) → `uret.py` (agy-filo `kod`, gemini-3.8-flash-high, 236 sn) → şef okuması + 1 küçük Edit |

## Öğe listesi (`nesneler.json` sırası)

| Öğe | Kutu (x, y, w, h) | Not |
|---|---|---|
| kanal | 60, 280, 542, 70 | `Y.kunye_svg()` → `#kanal` (`#logoimg` + `#kanal-yazi` `@ydspublishing` Lexend 700 42) |
| kunye | 60, 360, 453, 90 | `Simple Present` Fredoka 700 34 + rozet `YDT · BASIC` |
| baslik | 117, 462, 786, 337 | 2 satır, mürekkep, hapsız, zemin konturu 12 (`paint-order:stroke fill`) |
| kart | 62, 830, 536, 320 | kâğıt `rect` (`#f3efe6`, opaklık 0,06) + elle çizilmiş kalem kenarı (03-kaydet kalıbı); `usually` · `always` · `every day` Fredoka 72 |
| takvim | 490, 856, 68, 76 | Tabler `calendar`, ölçek 4; "1" çizgisi çıkarıldı (QA tur 1) |
| ok | 294, 1159, 56, 97 | kalem oku, mürekkep 5 px |
| hap | 60, 1268, 600, 104 | `Simple Present` Fredoka 80; karenin tek sarı vurgusu (açık `#ffe066` / `#1b2440`) |
| karakter | 663, 823, 295, 496 | `ortak/kapak/karakter.png` → `proje/assets/karakter.png`; `<img class="abs kenar">`, krem `#f3efe6` kenar 10 px (3 × 4 yön `drop-shadow`) |

## Kapı sonuçları (son satırlar)

```
$ bash calistir.sh --tema acik          → rc_acik=0 · index.html yazıldı 7859 · S=143 · s=0.465 · png,1080,1920
$ bash calistir.sh --tema koyu          → rc_koyu=0 · index.html yazıldı 7859 · S=143 · s=0.465 · png,1080,1920
$ node araclar/cakisma-kapisi.mjs simple-present-temel-s2 --sahne 07-hyperframes-kapak-c --port 41333 --sunucu 41022
HATA sahne bulunamadı: 07-hyperframes-kapak-c
rc_kapi=2
$ grep -rniE 'tam ders|dakika' …/07-hyperframes-kapak-c/ --include=*.html --include=*.js --include=*.py
(boş) rc_grep=1
```

Piksel ölçümü (zemin = satır başına sol kenar x 0–40 medyanı, eşik RGB farkı > 60; sözleşme kalıbı):

| Bölge | Açık | Koyu |
|---|---|---|
| üst 0–280 | boş | boş |
| kanal 280–352 | x 60–596, y 296–339 (logo x 60–239, yazı x 264–596) | aynı |
| künye 352–458 | x 60–512, y 386–433 | x 60–513, y 386–433 |
| içerik 458–1390 | x 59–948, y 468–1371 | x 59–957, y 468–1371 (krem kenar) |
| alt 1390–1920 | boş | boş |
| sağ 960–1080 | boş | boş |

## Bakılan kareler ve bulgu

QA kareleri: açık `k/at-0.5s.png` = paket kökü `kapak-c.png` (tek kare: ilk = orta = son) · koyu `k/koyu/at-0.5s.png` = `k/koyu/kapak-c-koyu.png`.
Read ile bakıldı (iki tur):

| Tur | Bulgu | İş |
|---|---|---|
| 1 | Taşma, kesik yazı, üst üste binme yok; Ü, Ç, İ, Ş doğru glif; bantlar boş; kanal + künye yerinde; koyu temada krem kenar ceketi zeminden ayırır. Tabler takvimin içindeki çizgi "1" rakamı gibi okunur (kapak kuralı: rakam yok) | `uret.py` `kart_svg`: `M11 15`, `M12 15` yolları süzüldü (+ yol sayısı assert'i 4) |
| 2 | Takvim kırpıntısı (iki tema) rakamsız; ölçek ve yerleşim değişmedi (S 143, s 0,465) | — |

## agy koşu özeti

`/home/sef/.claude/canavar/agy-filo/20261115-194608` (1/1 başarılı, 236 sn, gemini-3.8-flash-high; girdi 2,56 M, çıktı 110,8 K token).
Şef okuması: SPEC'e uyuyor (glif sınırı BoundsPen ile, S ve s araması, maske şartları, §6 assert'leri, `#root.tema-acik` yok, yasak söz listesi yok).

## Açık noktalar

1. Karakterin saçı sarıdır (görselin kendi paleti, kapak-standardi stil cümlesi). Karenin tek sarı vurgu ÖĞESİ haptır; emsal 05'te de aynı (sarı kazak + sarı hap).
2. Koyu temada künye rozeti ile hap aynı turuncudur (`#f2a93b`); künye bütün sahnelerde aynı, emsal davranışı.
3. Başlık `font-kerning:none` (emsal kalıbı): `İFADE` içinde İ–F arası hafif geniş görünür. Nadir bakışına.
4. Karakter ölçeği 0,465 (görünür ≈ 275 × 476 px). Daha büyük ölçek ya başlığa (üst) ya hapa (alt sol) değer; parmak kartın içinde kalır.
5. agy özeti "değişen 70" dosya sayar: liste paralel oturumların dosyalarını da içerir (`simple-present-temel-s1/…`, `.claude/docs/sozlesme.md`).
   Bu sahne dizininde agy'nin yazdığı tek kod dosyası `uret.py`; diğer yeni dosyalar `uret.py` çıktısıdır (`proje/`, `nesneler.json`).
6. Çakışma kapısı durağan kareyi ölçmez (çıkış 2); denetim göz + piksel ölçümüyle yapıldı.
