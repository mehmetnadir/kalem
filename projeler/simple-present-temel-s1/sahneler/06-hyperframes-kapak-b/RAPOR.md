# RAPOR — simple-present-temel-s1 · sahne 06-hyperframes-kapak-b (huni v2; HyperFrames, 1080×1920, tek kare, ses yok) · 15.11.2026

Tema: acik

İstem: D-S1 06-hyperframes-kapak-b (P0202-S1-C, 15.11). Tasarım: `SPEC.md`. Paket yeni: eski sahne kodu ve yedek yok.

| Ölçüm | Değer |
|---|---|
| Çıktı (açık) | `P/kapak-b.png` 1080×1920 PNG · md5 `1181d8346804…` (= `k/at-0.5s.png`) |
| Çıktı (koyu) | `k/koyu/kapak-b-koyu.png` 1080×1920 PNG · md5 `d13a0521a8b7…` |
| Yerleşim | başlık Fredoka 700 S 106 (ana satırlar; yedek gerekmedi) · karakter ölçeği 0,425 · otobüs ölçeği 0,3746 (görünür en 360) |
| Kod | `uret.py` agy koşusu (1 tur) + 1 şef Edit (QA tur 1) · `yardim.py` kopya + `kunye_svg(konu, cerceve)` (şef, kısa Edit) · `calistir.sh` kopya + logo satırı |

Dosya kaynakları: `calistir.sh`, `olay.py`, `zamanlar.json` ← emsal `02-04-ydt-temel-s1/sahneler/05-hyperframes-kapak-b/` (`cp -p`);
`yardim.py` ← paketin `05-hyperframes-hikaye-a/yardim.py` (v2, `KONU` `Simple Present` doğru). `cizim/` yok (Tabler simgesi kullanılmadı).

## 1. Olay listesi

Durağan kare. Ses, anlatım, altyazı, çip yok. `olaylar.json` = `[]`. Zaman çizelgesi 1,0 sn; tek `set`; yakalama 0,5 sn. Küresel anlatım saniyesi yok.

| Öğe | Konum (px) | Renk açık / koyu |
|---|---|---|
| Zemin `#kb-zemin` | tam kare, düz (gren ve vinyeti örter) | `#fece00` / `#141414` |
| Kanal `#kanal` | logo resmi x 53,2, y 291–339 (görünür sol 60) · `@ydspublishing` Lexend 700 42, x 263, taban 330 | logo tek renk `#141414` / `yds-publishing-seffaf.svg` · yazı `#141414` / `#f3efe6` |
| Künye `#rz0` | yalnız rozet `YDT · BASIC`: hap x 60–263,6, y 386–434, 3 px çerçeve, Lexend 700 26; konu adı yok | çerçeve + yazı `#141414` / `#f3efe6` |
| Başlık `bs-1` | `FİİLE -S`, Fredoka 700 106, x 60, taban 656,4 | `#141414` / `#f3efe6` |
| Kutu `bk-kutu` + `bs-2` | kutu x 60–952,7, y 675,5–812,2, rx 10,6 · `HANGİ ÖZNEYLE?` x 77, taban 786,8 | kutu `#141414` + yazı `#f3efe6` / kutu `#fece00` + yazı `#141414` |
| Daire `#kb-daire` | merkez (740, 1150), r 220 → x 520–960, y 930–1370 | `#f3efe6` / yok (kapak-standardi: koyuda daire yok) |
| Otobüs `#nesne` | `ortak/kapak/nesne.png`, görünür x 205–565, y 1126–1272; parmak hizasında, sağa (karaktere) bakar | 10 px krem kenar (iki tema) |
| Karakter `#karakter` | `ortak/kapak/karakter.png`, görünür x 609–860, y 933–1368; baş ortası daire ortasında (x 740); sola işaret eder | 10 px krem kenar (iki tema) |

Başlık bloğu (558–812) 470–900 bandında dikey ortadadır. Tek vurgu satır 2 kutusu; sarı hap yok (zemin sarı).

## 2. Kapı sonuçları

| Kapı | Komut | Sonuç |
|---|---|---|
| 1 Render | `calistir.sh --tema acik` / `--tema koyu` | rc 0 / rc 0 · `png,1080,1920` (ikisi) · `file`: `PNG image data, 1080 x 1920` |
| 1 İlk = orta = son | `hyperframes snapshot . --at 0,0.5,0.966` (açık, `k/qa/`) | üç kare md5 `1181d8346804…`, teslim PNG ile aynı |
| 1 Önizleme | `ONIZLE_YALNIZ=1 calistir.sh --tema acik` | rc 0 · `olay 0` · `önizleme hazır` (son hazırlık açık tema) |
| 2 Çakışma | `node araclar/cakisma-kapisi.mjs simple-present-temel-s1 --sahne 06-hyperframes-kapak-b --port 41333 --sunucu 41022` | `HATA sahne bulunamadı: 06-hyperframes-kapak-b` · çıkış 2 (beklenen: araç yalnız `zaman.json → sahneler[]` okur). Çakışma `uret.py` assert'leriyle ve karede gözle denetlendi |
| 3 Metin | `grep -rniE 'tam[ ]ders\|dak[i]ka' … --include=*.html --include=*.js --include=*.py` | boş (grep çıkış 1) |
| 4 Kanal | kare ölçümü (zeminden ayrışan piksel, iki tema) | logo x 60–239, y 298–330 · yazı x 264–595, y 296–339 · ikisi 280–350 bandında; iki temada aynı |

Bant ölçümü (iki tema): 0–280 boş · 1381–1920 boş · x 961–1080 boş · x 0–59 boş · künye x 60–263, y 386–433 · başlık x 60–952, y 558–812 ·
813–919 boş · görsel x 193–959 (koyu 193–868), y 920–1377.
`uret.py` assert'leri: bloklar kendi bandında; kanal / künye / başlık / daire / otobüs / karakter kesişimi 0; otobüs maskesi karaktere
2 × kenar + 4 px uzak; Fredoka 700 cmap'inde `İ`, `Ö` var; görünen metinde yasak söz, `ALIR`, `ÖZNE` (YLE'siz) ve emoji yok;
HTML'de yalnız `#1b1a17`, `#f3efe6`, `#fece00`, `#141414`; `id="kanal"`, `id="logoimg"` tek; `ku-konu` yok.

## 3. Bakılan kareler ve bulgu

Kareler: açık `P/kapak-b.png` (tek kare: ilk = orta = son), koyu `k/koyu/kapak-b-koyu.png`. 1 düzeltme turu:

| Tur | Bulgu | Düzeltme (şef Edit, `uret.py` 2 satır) |
|---|---|---|
| 0 | saçın krem kenarı karede y 917'ye uzanıyor (görsel bandı 920): kenar + yumuşak alfa maskeden 13 px taşıyor | görünür üst 930 → 933, yükseklik 440 → 436 (ölçek 0,429 → 0,425); sonuç üst 920, alt 1377 |

Son karelerde taşma, kesik yazı, üst üste binme, okunmaz kontrast ve boş kare yok. Kırmızı, yeşil, emoji, QR, süre sözü, eski kapanış sözü yok.
Açık tema ana kapakla aynı aile (sarı zemin, siyah yazı ve logo, siyah kutuda krem satır, krem daire); koyu tema `kapak-koyu.png` ailesi.

## 4. agy koşusu

| Koşu | Özet | Sonuç |
|---|---|---|
| 1 uret.py | `~/.claude/canavar/agy-filo/20261115-195002` | başarılı, 268 sn, gemini-3.8-flash-high; girdi 2,37 M (önbellek 2,15 M), çıktı 142 K. Şef okudu: SPEC'e uygun, düzeltme gerekmedi; QA turu 1 şef Edit |

Koşu özetindeki "değişen" listesinde `.claude/docs/sozlesme.md` görünür; bu oturumun ajanı yalnız `uret.py` yazdı (öteki satır başka oturumun izi).

## 5. Açık noktalar

1. Karakter küçük kalır (görünür 252×435): istem görsel bandını 920–1380 verir. Başlık bloğu 254 px; görsel bandı başlığın altından
   (≈ 850) başlarsa karakter ≈ %20 büyür. Karar şefte.
2. Logo tek renk sahnede kurulur: `calistir.sh` açık temada lacivert logonun dolgularını (`#fece00`, `#13204D`, `#231f20`) `#141414` yapar.
   Canlı önizlemede (`?canli=1`) hf_tema betiği logoyu standart lacivert/şeffaf dosyaya çevirir; render etkilenmez.
3. Karakter erkek, videonun çağrı sesi kadın (`kadro.ogrenci`); kapak-taslak §4 DİKKAT satırıyla aynı, karar Nadir/şefte.
4. `yardim.py` kopyasına `kunye_svg(konu=False, cerceve=True)` eklendi (öntanım davranışı aynı). Sahne 07 kapak C de yalnız rozet ister;
   çerçeveli hap orada da gerekirse aynı iki parametre kullanılabilir.
