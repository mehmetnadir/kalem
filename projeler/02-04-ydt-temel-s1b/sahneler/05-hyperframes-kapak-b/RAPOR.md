# RAPOR — 02-04-ydt-temel-s1 · sahne 05-hyperframes-kapak-b (huni v2) · 15.11.2026

Tema: acik

İstem: `uretim-tutanagi/istem/sahne-v2/D-05-hyperframes-kapak-b.md`. Tasarım: `SPEC.md` (v2). Eski RAPOR yoktu.

| Ölçüm | Değer |
|---|---|
| Çıktı (açık) | `P/kapak-b.png` 1080×1920 PNG · md5 `f6ae6fcb…` |
| Çıktı (koyu) | `k/koyu/kapak-b-koyu.png` 1080×1920 PNG · md5 `c5327984…` |
| Yerleşim | başlık S 142 · karakter ölçeği 0,49 · balon x 523–960 · balon yazısı Caveat 74 |
| Yedek | `~/Silinecekler/2026-11-15-huni-v2/02-04-ydt-temel-s1/sahneler/05-hyperframes-kapak-b/` (v1 SPEC, uret.py, yardim.py, calistir.sh, json, k/, proje/index.html) |
| Kod | `yardim.py` (agy koşusu 1) · `uret.py` (agy koşusu 2 + 4 şef Edit) |

## 1. Olay listesi

Durağan kare. Ses, anlatım, altyazı ve çip yok. `olaylar.json` = `[]`. Zaman çizelgesi 1,0 sn; tek `set`; yakalama 0,5 sn.

| Öğe | Konum (px) | Kaynak |
|---|---|---|
| Kanal katmanı `#kanal` | logo resmi x 53,2, y 291–339 (görünür sol 60) · `@ydspublishing` Lexend 700 42, x 263, taban 330 | `yardim.py kunye_svg()` (sahne 01 v2 bloğu birebir) |
| Künye | konu Fredoka 700 34, x 60, taban 420 · rozet `YDT · BASIC` hap x 665–868, y 386–434 | aynı |
| Başlık | `YAŞI[YOR]UM` / `NASIL DENİR?`, Fredoka 700 142, orta x 510, kutu y 480–625; satır 2 tabanı 781 | v1 algoritması, genişlik 888 |
| Karakter | `ortak/kapak/karakter.png`, kenar dahil x 62–501, y 900–1380; 10 px krem kenar (`drop-shadow` 3 × 4 yön) | 90 kapak kalıbı |
| Düşünce izi | 3 daire r 8 / 12 / 16, baştan (406, 967) iki balonun arasına (502, 1027) | maske denetimli |
| Balon 1 | x 523–960, y 862–1006; ev ikonu + `I live?` Caveat 74 | |
| Balon 2 | x 523–960, y 1026–1170; bavul ikonu + `I am living?` Caveat 74 | |

## 2. Kapı sonuçları

| Kapı | Komut | Sonuç |
|---|---|---|
| 1 Render | `calistir.sh --tema acik` / `--tema koyu` | rc 0 / rc 0 · `file`: 1080 x 1920 PNG (ikisi de); kök PNG = `k/at-0.5s.png` (cmp aynı) |
| 2 Çakışma | `node araclar/cakisma-kapisi.mjs 02-04-ydt-temel-s1 --sahne 05-hyperframes-kapak-b --port 41333 --sunucu 41022` | `HATA sahne bulunamadı: 05-hyperframes-kapak-b` · çıkış 2 (beklenen; araç yalnız `sahneler[]` okur). Çakışma gözle ve `uret.py` assert'leriyle denetlendi |
| 3 Metin | `grep -rniE 'tam ders\|dakika' … --include=*.html --include=*.js --include=*.py` | boş (rc 1) |
| 4 Kanal | kare ölçümü (mürekkep pikseli, iki tema) | logo x 60–239, y 298–330 · yazı x 265–596, y 296–339 · kanal bandı 280–350 içinde |

Ek bant ölçümü (iki tema, mürekkep pikseli): 0–280 boş · 1381–1920 boş · x 961–1080 boş · künye y 386–433 · içerik x 60–959, y 480–1378.
`uret.py` assert'leri: bütün bloklar kendi bandında; başlık / balon / iz / kanal / künye kesişimi 0; karakter maskesi balonlara ve ize
kenar + pay kadar uzak; görünen metinde yasak söz ve emoji yok; HTML'de yalnız `Y.RENK` renkleri; `id="kanal"`, `id="logoimg"` tek.

## 3. Bakılan kareler ve bulgu

Kareler: açık `P/kapak-b.png` (tek kare: ilk = orta = son), koyu `k/koyu/kapak-b-koyu.png`. 3 düzeltme turu:

| Tur | Bulgu | Düzeltme (şef Edit) |
|---|---|---|
| 0 | balon çizgisinin dış kenarı x 962 (agy 2 px tolerans koymuştu) | `BL_X1` 958, tolerans 0 |
| 1 | `I am living?` soru işareti balon kenarına ≈ 11 px (Caveat glifi ilerleme genişliğini aşıyor) | sağ pay `PAD_SAG` 40 → ölçek 0,52 → 0,49, yazı 72 → 74 |
| 2 | koyu temada krem kenarın yumuşatması x 58'e taşıyor | karakter 2 px sağa |
| 3 | metin taraması `uret.py`'nin kendi yasak listesine takıldı | liste sözcükleri parçalı yazıldı (koruma aynı) |

Son karelerde taşma, kesik yazı, üst üste binme, okunmaz kontrast ve boş kare yok. Tek vurgu `YOR` kutusu; kırmızı, yeşil, emoji, QR, süre sözü yok.

## 4. agy koşuları

| Koşu | Özet | Sonuç |
|---|---|---|
| 1 yardim.py | `~/.claude/canavar/agy-filo/20261115-190521` | başarılı, 68 sn; diff: künye bloğu sahne 01 ile birebir, kalan satırlar aynı |
| 2 uret.py | `~/.claude/canavar/agy-filo/20261115-190526` | başarılı, 426 sn; **ISRAF** uyarısı (girdi 5,14 M > tavan 5 M); 4 küçük şef Edit |

## 5. Açık noktalar

1. Açık temada krem kenar (`#f3efe6`) zemine (`#f7f3ea`) çok yakın, görünmez; standart §2'deki krem daire de aynı sebeple konmadı. Koyu temada kenar belirgin.
2. Koyu temada `YOR` kutusu ve rozet paketin koyu `vurguDolgu` rengini (`#f2a93b`, turuncuya yakın) alır; öteki sahnelerle aynı, değiştirilmedi.
3. Sağ alt (x 525–960, y 1180–1380) boş zemin kalır: balonlar baş hizasında, karakterin sağ avucu balon 2'nin altına yakın.
4. Paket dışı not: sahne 07 (`07-hyperframes-hikaye-b`) hâlâ "Cevap tam derste:" taşıyor (başka istemin işi; dokunulmadı).
5. agy koşu özetlerindeki "değişen" listesinde başka oturumların dosyaları görünür (04-hikaye, s2, s3); bu sahnenin ajanları yalnız hedef dosyayı yazdı.
