# DUZ2-0204D — `02-04-ydt-temel-dikey` rozet düzeltmesi (15.11.2026)

Girdi: `uretim-hatti/raporlar/J2-OZET-1511.md` §3A (02-04-ydt-temel-dikey satırı), §4.1 TD-1 ·
`dijital-anlatim/.claude/docs/juri-olcutleri.md` HV-24.

| Ölçüm | Sonuç |
|---|---|
| Rozet metni | `YDT · BASIC` → `YDT · TEMEL` |
| Değişen dosya (git) | 22: kaynak kod 8, üretilmiş `index.html` 6, belge 7, `surumler.json` 1 |
| Yeniden üretilen sahne | 6 HyperFrames: 06, 07, 10, 12, 13, 14 |
| Yeniden üretim gerekmeyen | 7 kanvas/Paper.js sahnesi (02, 03, 04, 05, 08, 09, 11): rozeti `ortak/kunye.js`'ten canlı okur |
| Kare | koyu 19, açık 13; 2 kontak sayfası; hepsine bakıldı |
| Çakışma kapısı | 14 sahne, her sahne çıkış kodu **0** (1.074 örnek, 155.668 kutu) |
| Son `grep BASIC` (üretim dosyaları) | **0** |
| Yatay pakette geçiş | 24 satır / 24 dosya (üretim 16, belge 8); dokunulmadı |
| Ses ve zaman | dokunulmadı (`zaman.json`, `olaylar.json`, `ortak/anlatim/`, `_is/ses.wav` farksız; `olay.py` koşmadı) |

## 1. Değişen dosyalar

Kaynak (rozet sabiti):

| Dosya | Değişiklik |
|---|---|
| `ortak/kunye.js` | `KUNYE.rozet` (kanvas sahneleri ve sahne 07 bunu okur) |
| `sahneler/06-hyperframes-soru1/uret.py` | genişlik ölçümü + metin (2 yer) |
| `sahneler/07-hyperframes-kural/uret.py` | `assert ROZET == "YDT · TEMEL"` (rozeti `kunye.js`'ten okur) |
| `sahneler/10-hyperframes-tuzak/uret.py` | genişlik + metin + `rw_hud` (3 yer) |
| `sahneler/12-hyperframes-ozet/yardim.py` | genişlik + metin (2 yer) |
| `sahneler/13-hyperframes-mini-soru/uret.py` | genişlik + metin (2 yer) |
| `sahneler/14-hyperframes-kapanis/yardim.py` | genişlik + metin (2 yer) |
| `sahneler/90-hyperframes-kapak/yardim.py` | `ROZET` sabiti (kapak `uret.py` zaten `YDT · TEMEL`; `kapak.png`, `kapak-koyu.png` doğru) |

Üretilmiş: `sahneler/{06,07,10,12,13,14}-*/proje/index.html`.

Belge (spec; sonraki üretim eski metni geri getirmesin diye): `BRIEF-DIKEY.md` (satır 57, 70, 71: ölçülen rozet kutusu
281 → 287 px), `sahneler/{06,07,10,12,13,14}-*/SPEC.md` (metin; 06, 12, 14'te genişlik tahmini ≈ 282 → ≈ 288).

Sürüm: `surumler.json` `revizyonlar` dizisine `dikey-tam` / `r2` satırı (alan düzeni: `surum`, `no`, `tarih`,
`degisiklik`, `cikti`; diğer paketlerle aynı).

Yeni: `uretim-tutanagi/duz2-kareler/` (kareler, kontak sayfaları, kapı çıktıları), bu rapor.

`senaryo.json`: bu pakette yok (`find` 0 sonuç); dikey paket yatayın sesini kullanır.

## 2. Yeniden üretim

Yöntem: her sahnede `uret.py` → `ortak/hf_tema.py proje/index.html koyu` (calistir.sh'ın önizleme yolu; render yok).

1. Belirlenimcilik ölçümü: kaynak değişmeden önce 6 sahne yeniden üretildi → `git diff` **0** satır.
2. Kaynak düzeltildi, 6 sahne yeniden üretildi. `index.html` farkı sahne başına yalnız 3 değer:

| Değer | Önce | Sonra |
|---|---|---|
| rozet metni | `YDT · BASIC` | `YDT · TEMEL` |
| hap `rect width` | 282.48 | 288.02 |
| metin merkezi `x` | 811.09 | 813.87 |

3. Açık tema karesi için `index.html` geçici olarak `acik` temaya çevrildi, kare alındı, sonra `uret.py` + `koyu` ile geri
   üretildi; son fark yine yalnız yukarıdaki 3 değer.

Rozet kutusu: HyperFrames x 667,85, w 288,02 · kanvas (başsız tarayıcı `__kalemKutu`) 668,216,287,72. Sağ kenar ≈ 956 px;
içerik sınırı 1032 px. Çip y 48–128, rozet y 216–288: dikey örtüşme yok.

## 3. Kareler (kendi bakışım)

Araç: `araclar/sahne-kare.mjs` (önizleme sunucusu 127.0.0.1:41022 = bu worktree, başsız Chrome 41333).

| Kontak sayfası | Kare |
|---|---|
| `uretim-tutanagi/duz2-kareler/kontak-hud-koyu.png` | `duz2-kareler/koyu/` 19 kare: 13 sahne, HyperFrames'te kare 0 + sahne ortası |
| `uretim-tutanagi/duz2-kareler/kontak-hud-acik.png` | `duz2-kareler/acik/` 13 kare: 13 sahne, sahne ortası |

Kare adları `<sahne>-<t>.png` (t = anlatım saniyesi): 02-paperjs-kanca-19.5 · 03-paperjs-ornek1-32 · 04-canvas-ornek2-56 ·
05-canvas-ornek3-81 · 06-hyperframes-soru1-93.4 / 103 · 07-hyperframes-kural-113.4 / 122 · 08-canvas-karsit1-138 ·
09-canvas-karsit2-154 · 10-hyperframes-tuzak-162.4 / 173 · 11-canvas-tuzak-cevap-194 · 12-hyperframes-ozet-205.4 / 213 ·
13-hyperframes-mini-soru-220.4 / 236 · 14-hyperframes-kapanis-251.3 / 258 (açık temada yalnız ikinci zaman).

Bakış sonucu (32 karenin hepsi):

- Rozet metni her karede `YDT · TEMEL`; İngilizce seviye adı yok.
- Metin hapın içinde ortalı; taşma yok.
- Rozet ders adı 2. satırının sağında; ders adıyla, çiple ve logoyla çakışma yok.
- Karede tek rozet metni var (HV-24 "aynı karede iki rozet" koşulu sağlanır).
- İki temada okunur (koyu: `#f2a93b` hap, koyu metin; açık: `#ffe066` hap, lacivert metin).
- Kapak (`kapak.png`, `kapak-koyu.png`): rozet `YDT · TEMEL` (15.11 18:58 üretimi; değişiklik gerekmedi).

## 4. Çakışma kapısı

Komut (sahne başına, ön planda): `node araclar/cakisma-kapisi.mjs 02-04-ydt-temel-dikey --sahne <s> --json
uretim-tutanagi/duz2-kareler/cakisma/<s>.json --port 41333 --sunucu 41022` (sıklık 4/sn, pay 4 px).

| Sahne | Çıkış | Örnek | Kutu |
|---|---|---|---|
| 01-hyperframes-giris | 0 | 13 | 88 |
| 02-paperjs-kanca | 0 | 70 | 1.951 |
| 03-paperjs-ornek1 | 0 | 96 | 5.434 |
| 04-canvas-ornek2 | 0 | 101 | 1.633 |
| 05-canvas-ornek3 | 0 | 99 | 1.571 |
| 06-hyperframes-soru1 | 0 | 81 | 35.067 |
| 07-hyperframes-kural | 0 | 69 | 16.053 |
| 08-canvas-karsit1 | 0 | 61 | 660 |
| 09-canvas-karsit2 | 0 | 69 | 1.448 |
| 10-hyperframes-tuzak | 0 | 87 | 19.608 |
| 11-canvas-tuzak-cevap | 0 | 87 | 1.508 |
| 12-hyperframes-ozet | 0 | 61 | 27.482 |
| 13-hyperframes-mini-soru | 0 | 125 | 35.555 |
| 14-hyperframes-kapanis | 0 | 55 | 7.610 |

Her sahne: "çakışma yok", hata 0, uyarı 0. Çıktılar: `duz2-kareler/cakisma/<sahne>.{json,log}`.

## 5. Yatay paket `projeler/02-04-ydt-temel` (yalnız rapor, dokunulmadı)

`grep -rnI "BASIC" projeler/02-04-ydt-temel` → 24 satır, 24 dosya. Yatay biçim noktasız `YDT BASIC` (künye
`seviye` alanı, tek satır künye).

| Tür | Dosya | Sayı |
|---|---|---|
| Üretim | `ortak/kunye.js:52` (`seviye: "YDT BASIC"`) | 1 |
| Üretim | `sahneler/{01,06,07,10,12,13,14}-*/yardim.py:182` (`· YDT BASIC`) | 7 |
| Üretim | `sahneler/90-hyperframes-kapak/yardim.py:155` (`ROZET = "YDT · BASIC"`) | 1 |
| Üretim (türetilmiş) | `sahneler/{01,06,07,10,12,13,14}-*/proje/index.html:32` | 7 |
| Belge | `BRIEF.md:71`, `uretim-tutanagi/senaryo-taslak.md:81`, `uretim-tutanagi/YV-RAPOR.md:112`, `uretim-tutanagi/juri/YVJ-hukum.md:24`, `sahneler/{01,06,13,14}-*/RAPOR.md` | 8 |

Üretim dosyası toplamı 16. Ana ders düzeltmesi ayrı istemin işidir (J2 §3A ana ders satırı).

## 6. Son `grep` çıktısı (dikey paket)

```
$ grep -rnI "BASIC" projeler/02-04-ydt-temel-dikey --exclude='*RAPOR.md' | wc -l
0
$ grep -rlI "BASIC" projeler/02-04-ydt-temel-dikey
projeler/02-04-ydt-temel-dikey/sahneler/14-hyperframes-kapanis/RAPOR.md
projeler/02-04-ydt-temel-dikey/sahneler/10-hyperframes-tuzak/RAPOR.md
projeler/02-04-ydt-temel-dikey/sahneler/06-hyperframes-soru1/RAPOR.md
projeler/02-04-ydt-temel-dikey/uretim-tutanagi/DUZ2-RAPOR.md
projeler/02-04-ydt-temel-dikey/sahneler/07-hyperframes-kural/RAPOR.md
projeler/02-04-ydt-temel-dikey/sahneler/02-paperjs-kanca/RAPOR.md
```

Kalan dosyalar raporlardır: 5 sahne `RAPOR.md` dosyası sahne ajanlarının tarihî üretim raporudur (o günkü kareyi anlatır;
satır başına 1 geçiş: 14:17, 10:11, 06:14, 07:16, 02:29), `DUZ2-RAPOR.md` bu rapordur (eski metni alıntılar). Üretim
girdisi değildir; tarihî raporlara dokunulmadı.
Üretim dosyalarında (kod, `index.html`, `kunye.js`, `surumler.json`, BRIEF, SPEC) geçiş 0.

## 7. Açık kalanlar (bu istemin kapsamı dışı)

- **mp4 yeniden derlenmedi** (kural: render yok). `cikti.mp4`, `cikti-koyu.mp4`, `_is/govde*.mp4`, `_is/gecis*.mp4`,
  sahne `video*.mp4`, sahne `kontrol.png` ve `k/` kareleri eski rozeti taşır. Yayından önce şef derlemesi gerekir.
- `uretim-tutanagi/duz2-kareler/` 21 MB (32 tam kare PNG); şef commit'e almak istemezse `Silinecekler/` altına taşınır.
- git commit atılmadı (şef atar).
