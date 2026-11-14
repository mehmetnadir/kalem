# P1 raporu — 02-04-ydt-temel · paket iskeleti + senaryo.json + BRIEF · 14.11.2026

Hazırlayan: Claude oturumu (srv21, istem C). Ses sentezi, ElevenLabs çağrısı, render, sahne kodu, commit YOK.

## 1. Özet

| Ölçü | Değer |
|---|---|
| Cümle (`senaryo.json`) | 18 (öğretmen 15, öğrenci 3: cümle 6, 12, 16) |
| Sözcük | 509 (taslak 511; fark: IPA kalkınca "T shirt" → "T-shirt", 2 yerde 1 sözcük) |
| Sahne | 14 (HyperFrames 7, Paper.js 2, Düz canvas 5; 02-03 ile aynı dağılım) |
| Soru anı | 2 (cümle 6, 12); yanlış cevap cümle 16 (mini soru içinde) |
| Süre | iddia yok; taslak tahmini 246 sn; sahne t değerleri sentez sonrası |

## 2. Yazılan dosyalar

| Dosya | İş |
|---|---|
| `ortak/{cizim,font,hf_tema.py,logo}` | sembolik bağ, hedef 02-03 ile aynı (`../../present-continuous/ortak/…`) |
| `ortak/{kalem-canvas.js,tema.sh,tema_damga.py}` | 02-03'ten kopya, değişiklik yok |
| `ortak/kunye.js` | 02-03'ten kopya + 2 satır: `KOK` → `/projeler/02-04-ydt-temel/ortak`, `ders` → `SIMPLE PRESENT vs PRESENT CONTINUOUS` (02-02 → 02-03 emsali aynı 2 satırı değiştirdi) |
| `ortak/anlatim/{kur,metin_uret,sozcuk_uret}.py` | 02-03'ten kopya, değişiklik yok |
| `ortak/anlatim/zaman_uret.py` | 02-03'ten kopya; `SAHNE` eşlemesi 02-04 planına göre (sahne 9–14 son cümleleri 10, 12, 13, 14, 17, 18; sahne 11 `11-canvas-tuzak-cevap`). Koşturulmadı; `py_compile` geçti (4/4 betik) |
| `ortak/anlatim/senaryo.json` | 18 cümle; şema 02-03 ile birebir (üst anahtarlar + cümle anahtarları `ses, parcalar, olaylar, metin` doğrulandı); `olaylar: []` (02-03 gibi); rakam 0, IPA 0 |
| `gorevler.json`, `yorumlar.json`, `harita-konum.json` | boş (`[]`, `[]`, `{}`); 02-03'te de boş. Anlam `ortak/onizle-sunucu.mjs` 198–336: görev listesi, yorum listesi, harita düğüm konumu `{x, y}` |
| `surumler.json` | 02-03 biçimi; `video` 02-04 kimliği, konu, 4 amaç, 5 can alıcı, etiket; tek sürüm `ana-yatay` (durum taslak, önizleme `/p/02-04-ydt-temel/onizle.html`) |
| `BRIEF.md` | §0 künye, §1 kaynak (sunucu yolları), görsel dil bağı, §2 iskelet, §3 sahne planı (14 satır: klasör, motor, cümle, içerik, olaylar), §4 ses hattı |
| `uretim-tutanagi/juri.md` | jüri özeti (02-03 biçimi) |
| `uretim-tutanagi/istem/A-girdi.md` | yalnız künye "Döküm" satırı: kapsam 00:00–03:14 eklendi |

## 3. Sahne planı özeti

`01 giriş (1 başı) → 02 kanca (1 sonu, 2) → 03–05 örnek 1–3 (3, 4, 5) → 06 soru anı 1 (6, 7) → 07 kural (8) → 08–09 karşıt çift today (9, 10)`
`→ 10 tuzak + soru anı 2 (11, 12) → 11 tuzak cevabı (13) → 12 özet (14) → 13 mini soru (15–17, fade) → 14 kapanış (18)`

## 4. Ses metni dönüşümü (ön bakış, `ses_metni()` yalnız okundu, sentez yok)

- tr `-ing` → `/ɪŋ/` (cümle 6, 11, 18) · tr `is` → `/ɪz/` (cümle 3, 17) · `T-shirt` → `T shirt` (cümle 3, 9). Taslaktaki ses metniyle aynı.
- *wear* (3), *live* (4), *today* / *Today* (9, 10): `ses-sozluk.json`'da yok → ham kalır (aşağıda açık nokta 1).

## 5. Açık noktalar

1. **IPA kaybı (wear, today, live).** İstem "ham sözcük, IPA yok" dedi; taslak ve dil jürisi tur 2 bu 3 sözcükte IPA kabul etmişti. Sözlükte olmadıkları için sentezde düz okunurlar. Dil jürisi koşulu geçerli: kulak denemesinde (3021) dinle; düz okunursa ayrı `en` parça ya da `ses-sozluk.json` girdisi (D altında, bu istemin yazma alanı dışı; sözlük bütün projeleri etkiler).
2. **Kural 7 yanlış pozitif (cümle 14).** "kalıcı durum ve tarifeli gelecek" → ses "ve, tarifeli" (tarifeli ASCII-yalnız Türkçe sözcük, `TR_ASCII`'de yok). Kısa duraklama doğar; taslakta da aynı. Kabul ya da `TR_ASCII`'ye ekleme kararı sentez öncesi.
3. **A-girdi.md satır 70 ve 111** hâlâ "04:30" der (slayt 3 gerekçesi, kapsam maddesi 20). İstem yalnız künyeyi istedi; dokunulmadı.
4. **Sahne 06 motoru.** Kurala göre figür Düz canvas'ın işi; 02-03 emsaliyle HyperFrames + SVG figür planlandı. P2'de taşımazsa klasör `06-canvas-soru1` olur; `zaman_uret.py` satırı birlikte değişir.
5. **HIZ_EN 0,9** 02-03 BRIEF'ten alındı; `el.py` varsayılanı 0,8 → sentezde `HIZ_EN=0.9` verilmeli.
6. **Henüz olmayan dosyalar:** `zaman.json`, `METIN.md` (surumler.json `senaryo` alanı bunu gösterir), `altyazi.json`; hepsi sentez sonrası üretilir (02-03 emsali).
7. Çözülemeyen alan yok. Kütüphaneci (`project-switch.md`, `sozlesme.md`) yazma alanı dışında kaldı; yapılmadı.
8. `py_compile` çıktısı `__pycache__` → `~/Silinecekler/2026-11-14-0204/anlatim-__pycache__` (silme yok). Yardımcı yazıcı betikler `/tmp/claude-0204/` (paket dışı, geçici).
