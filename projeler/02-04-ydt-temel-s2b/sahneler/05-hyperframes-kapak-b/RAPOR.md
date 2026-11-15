# Sahne 05 — Kapak B (soru) · 02-04-ydt-temel-s2 · huni v2 · HyperFrames DİKEY 1080×1920 · tek kare, ses yok · 15.11.2026

Tema: acik

Teslim açık tema, koyu kopya. İstem: D-S2-V2. v1 (SPEC, RAPOR, uret.py, kareler) yedeği:
`~/Silinecekler/2026-11-15-huni-v2/02-04-ydt-temel-s2/sahneler/05-hyperframes-kapak-b/` (`cp -a`, kopya).

| Alan | Durum |
|---|---|
| Teslim | `P/kapak-b.png` (açık, 1080×1920, md5 `e3f4ea3b…`) · `k/koyu/kapak-b-koyu.png` (koyu, 1080×1920, md5 `8c2582a9…`) |
| Önizleme | `ONIZLE_YALNIZ=1 bash calistir.sh` → "önizleme hazır", rc 0 (`S=125 TT=76 KS=0.56 r=147 X0=58.2 Y0=747.3`) |
| Tek kare | `bash calistir.sh --tema acik` rc 0 · `--tema koyu` rc 0; ffprobe `1080,1920` (iki dosya) |
| Çakışma kapısı | `node araclar/cakisma-kapisi.mjs 02-04-ydt-temel-s2 --sahne 05-hyperframes-kapak-b --port 41333 --sunucu 41022` → `HATA sahne bulunamadı: 05-hyperframes-kapak-b`, çıkış 2 (beklenen: araç yalnız `sahneler[]` okur). Çakışma uret.py assert'leri + karede gözle denetlendi |
| Metin taraması | `grep -rniE "tam ders\|dakika" … --exclude-dir=k` → boş (rc 1) |
| Üretim yolu | şef `SPEC.md` (v2) → `agy-filo tek --rol kod` (gemini-3.8-flash-high, 304 sn) `uret.py` yazdı → şef baştan sona okudu, SPEC'e uyuyor |
| agy özeti | `/home/sef/.claude/canavar/agy-filo/20261115-190904/ozet.md` (1/1 başarılı; "değişen 61" bütün ağacı tarar, paralel oturumların dosyaları) |
| Şef düzeltmeleri (Edit) | 1) `var tl` (örtük global) · 2) takvim yazısı TT 89 → 76 ve x = 590 − 0,09·TT (1. tur karesi: `y` sağ kenara ≈ 12 px, kuyruk alt kenara ≈ 10 px) · 3) yasak listesi düzenli ifade (`tam\s+ders`, `dak[iı]ka`): tarama uret.py'nin kendi listesine takılıyordu |
| Düzeltme turu | 1 / 4 (takvim yazısı) |
| Dosyalar | `uret.py` (agy + 3 küçük Edit) · `SPEC.md` (şef) · `yardim.py` (şef Edit: `HUD`, `konu_boyu`, `rozet_konumu`, `kunye_svg` v2; çip ve v1 ders adı kalktı) · `calistir.sh` (şef Edit: `karakter.png` kopyası; `uret.py` ve `olay.py` ayrı satır, sözleşme 15.11 `set -e` tuzağı; ardından iki tema yeniden koştu, md5 aynı) · `nesneler.json`, `olaylar.json`, `proje/` (üretilen) |

## Olay listesi
Durağan kare; olay yok (`olaylar.json` = `[]`). Çizelge 1,0 sn, yakalama 0,5 sn (`zamanlar.json`). Ses, sözcük zamanı, altyazı yok.
GSAP zaman çizelgesi yalnız `#baslik`'e iki `set` (opaklık 1) yazar; `#kanal` hiçbir tween'e girmez.

| Öğe | Yer (px) | Not |
|---|---|---|
| kanal katmanı `#kanal` | logo x 53,2 y 291 w 193,5 h 48 · `@ydspublishing` Lexend 700 42, x 263, taban 330 | `#kunye` içinde; HF kutu adı `kunye:kanal`; karede ölçüm (koyu) x 60–595, y 290–342 |
| künye | konu Fredoka 700 34, x 60, taban 420 · rozet `YDT · BASIC` hap x 664,6 w 203,6, y 386–434, Lexend 700 26 | rozet sağ kenar 868 ≤ 960 |
| başlık `TODAY VARSA` / `HANGİ ZAMAN?` | Fredoka 700 S 125, sola yaslı x 60, taban 598,75 / 756,25 | mürekkep, hapsız; `İ` noktalı; ölçülen mürekkep sağ kenarı x 958 |
| kapak görseli `<img id="karakter">` | ölçek 0,56; görünür x 70–550, y 844–1370; blok (kenar dahil) x 60–560, y 834–1380 | 10 px krem kenar: 3 geçiş × 4 yön `drop-shadow`, `#f3efe6` |
| krem daire `#daire` | merkez (316,4 · 1010,5), r 147 | yalnız açık tema (`.tema-acik #daire`); `fill` özniteliği yok |
| takvim yaprağı | sayfa 200 × 200, x 490–690, y 870–1070, +4°; blok x 480–699, y 839–1080 | Tabler `calendar` ilk 4 yol, mürekkep 6 px kalem çizgisi |
| `today` | Caveat 700 76, takvim gövdesinde ortalı | küçük harf, mürekkep |
| `?` | Tabler `question-mark`, q 23, x 740–950, y 900–1248 | TEK vurgu (`stroke` vurgu → açıkta `#d9900f`) |
| 0–280 · 1380–1920 | boş | piksel ölçümü: 0–280 ve 1385–1920 içerik yok |

## Bakılan kareler ve bulgu
| Kare | Bakılan | Bulgu |
|---|---|---|
| `P/kapak-b.png` (açık; = `k/at-0.5s.png`) | taşma, kesik yazı, üst üste binme, kontrast, boş kare, bantlar, x > 960 | sorun yok. Kanal katmanı + künye yerinde; başlık iki satır aynı boy; takvim–baş ≈ 45 px, takvim–`?` ≈ 41 px |
| `k/koyu/kapak-b-koyu.png` (koyu) | aynı | sorun yok; krem kenar koyu zeminde belirgin, daire yok |
| takvim yakın kırpım (x 470–720, y 830–1090), iki tema, 2 tur | `today` kenar payı | 1. tur sıkışık (`y` kenara ≈ 12 px) → 2. tur ortalı, alt pay ≈ 19 px |
| piksel ölçümü (yüksek geçiren süzgeç + ham fark) | 0–280, 1385–1920, x > 960 | 0–280 boş · 1385–1920 boş · başlık mürekkebi x 958'de biter |

Durağan kare: ilk = orta = son (tek kare). qa-yerel koşulmadı (sahne `zaman.json` → `duragan`; küresel anlatım saniyesi yok).

## Açık noktalar
1. **Krem daire açık temada seçilmez:** kapak-standardi'nin krem dairesi sarı zemin içindir; bu paketin açık zemini `#f7f3ea`, daire `#f3efe6`
   (fark ≈ 4/255). Daire istem gereği çizildi; göze görünmez. Karar: daireyi kaldırmak ya da başka ton (şef/Nadir).
2. **Tek vurgu:** `?` tek çizilen vurgu; kapak görselinin sarı kazağı da sarı alan taşır (görselin kendisi; kapak-standardi paleti).
3. **Çakışma kapısı görseli ölçmez:** araç durağan sahneyi bulamaz (çıkış 2); bulsa da `hf-kutu` yalnız `#sahne` SVG'sini tarar, `<img id="karakter">` dışarıda.
   Karakter çakışması uret.py'de alfa maskesiyle (`bos_mu`, pay 26 px) denetlenir.
4. **"Elinde takvim":** görselde iki avuç açık; takvim sağ avucun üstünde, başın yanında durur ("yanında" seçeneği). Elle tutma için yeni görsel gerekir.
5. `cizim/ogretmen-dusunen.json` artık okunmuyor; silme yok kuralı gereği dizinde duruyor. `__pycache__/` da duruyor.
6. Rozet `YDT · BASIC` (paket + S1 ile aynı); standart örneği `YDT · TEMEL` (V2-C açık nokta 3, Nadir kararı).
