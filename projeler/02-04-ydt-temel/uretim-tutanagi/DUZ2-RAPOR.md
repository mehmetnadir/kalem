# DUZ2-0204Y — `02-04-ydt-temel` (yatay ana ders) rozet düzeltmesi (15.11.2026)

Girdi: `uretim-hatti/raporlar/J2-OZET-1511.md` §4.1 TD-1 · `dijital-anlatim/.claude/docs/juri-olcutleri.md` HV-24.

| Ölçüm | Sonuç |
|---|---|
| Rozet metni | künye `YDT BASIC` → `YDT · TEMEL` (ekranda `SIMPLE PRESENT vs PRESENT CONTINUOUS · YDT · TEMEL`) |
| Değişen dosya (git) | 18: kaynak kod 9, üretilmiş `index.html` 7, belge 1 (`BRIEF.md`), `surumler.json` 1 |
| Yeni dosya | bu rapor + `uretim-tutanagi/duz2-kareler/` (38 kare, 2 kontak sayfası, 28 kapı çıktısı; 29 MB) |
| Yeniden üretilen sahne | 7 HyperFrames: 01, 06, 07, 10, 12, 13, 14 |
| Yeniden üretim gerekmeyen | 7 kanvas/Paper.js sahnesi (02, 03, 04, 05, 08, 09, 11): rozeti `ortak/kunye.js`'ten canlı okur · kapak 90: üretici zaten `YDT · TEMEL` |
| Kare | koyu 22, açık 16; 2 künye kontak sayfası + kapak; hepsine baktım |
| Çakışma kapısı | 14 sahne, her sahne çıkış kodu **0** (1.074 örnek, 235.347 kutu) |
| Son `grep BASIC` (üretim dosyaları) | **0** |
| Ses ve zaman | dokunulmadı (`zaman.json`, `ortak/anlatim/`, `olaylar.json` farksız; `olay.py` koşmadı) |
| `youtube.json`, `youtube-aciklama.md` | dokunulmadı (git farksız) |

## 1. Değişen dosyalar

Kaynak (rozet sabiti):

| Dosya | Değişiklik |
|---|---|
| `ortak/kunye.js:52` | `KUNYE.seviye`: `"YDT BASIC"` → `"YDT · TEMEL"` (kanvas ve Paper.js sahneleri `kunyeCiz` ile okur) |
| `sahneler/{01,06,07,10,12,13,14}-*/yardim.py:182` | `kunye_svg` künye metni `· YDT BASIC` → `· YDT · TEMEL` (7 dosya, aynı satır) |
| `sahneler/90-hyperframes-kapak/yardim.py:155` | `ROZET` sabiti (dikey HUD yardımcısı; yatay kapak `uret.py:32` kendi `ROZET = "YDT · TEMEL"` sabitini kullanır) |

Üretilmiş: `sahneler/{01,06,07,10,12,13,14}-*/proje/index.html`.

Belge: `BRIEF.md:71` künye satırı (sonraki üretim eski metni geri getirmesin diye).

Sürüm: `surumler.json` `revizyonlar` dizisine `ana-yatay` / `r1` satırı (alan düzeni `surum`, `no`, `tarih`, `degisiklik`,
`cikti`; dikey paket ve SP ana ile aynı).

`senaryo.json`: bu pakette `giris.rozetler` alanı yok (`grep rozet` 0). Sahne 01 rozet hapı taşımaz (01 RAPOR.md §60).

## 2. Yeniden üretim

Yöntem: her sahnede `uret.py` → `ortak/hf_tema.py proje/index.html acik` (calistir.sh'ın önizleme yolu; render yok).
Depodaki `index.html` dosyaları açık temada (`class="tema-acik"`), kapak `index.html` koyu temada.

1. Belirlenimcilik: kaynak değişmeden önce 7 sahne yeniden üretildi → `git diff` **0** satır.
2. Kaynak düzeldi, 7 sahne yeniden üretildi. `index.html` farkı sahne başına tek belirteç:

| Değer | Önce | Sonra |
|---|---|---|
| `#ku-sev` metni | `· YDT BASIC` | `· YDT · TEMEL` |

Yatay künyede genişlik ölçümü yok (`dx="14"` sabit); başka değer değişmedi.

3. Kapak: `uret.py` + `hf_tema.py koyu` → `index.html` farkı **0**. `kapak.png` ve `kapak-koyu.png` (15.11 18:56) yeniden
   çekilmedi; ikisinde de rozet `YDT · TEMEL`.

## 3. Kareler (kendi bakışım)

Araç: `araclar/sahne-kare.mjs` (önizleme sunucusu 127.0.0.1:41022 = bu worktree, başsız Chrome 41333).
Sunucu doğrulaması: `curl /projeler/02-04-ydt-temel/ortak/kunye.js` → `seviye: "YDT · TEMEL"`.

| Kontak sayfası | Kare |
|---|---|
| `uretim-tutanagi/duz2-kareler/kontak-kunye-koyu.png` | `duz2-kareler/koyu/` 22 kare (üst 110 px şerit) |
| `uretim-tutanagi/duz2-kareler/kontak-kunye-acik.png` | `duz2-kareler/acik/` 16 kare (üst 110 px şerit) |

Kare adları `<sahne>-<t>.png` (t = anlatım saniyesi): 01-hyperframes-giris-2.7 · 02-paperjs-kanca-12 / 16.9 / 19.5 ·
03-paperjs-ornek1-32 · 04-canvas-ornek2-56 · 05-canvas-ornek3-81 · 06-hyperframes-soru1-93.7 / 103 ·
07-hyperframes-kural-113.7 / 122 · 08-canvas-karsit1-138 · 09-canvas-karsit2-154 · 10-hyperframes-tuzak-162.7 / 173 ·
11-canvas-tuzak-cevap-194 · 12-hyperframes-ozet-205.6 / 213 · 13-hyperframes-mini-soru-220.6 / 236 ·
14-hyperframes-kapanis-251.6 / 258 (açık temada HyperFrames sahnelerinde yalnız ikinci zaman).

Bakış sonucu:

- Künye ders yazısı görünen her karede rozet `· YDT · TEMEL`; İngilizce seviye adı yok.
- 01 (2,7 sn) ve 02 (12 sn) karelerinde ders yazısı yok: tasarım gereği. 01'de `ku-ders` gizli; 02'de başlık 16,67 sn'de
  künyeye iner (02 RAPOR.md §80). 02 iniş sonrası (16,9 ve 19,5 sn) rozet doğru.
- Rozet ders adının sağında, aynı taban çizgisinde; sağ üst bölüm adına (en uzun: `Example 1 / 3`, `Trap · answer`)
  uzak, taşma ve çakışma yok.
- Karede tek rozet metni var (HV-24 "aynı karede iki rozet" koşulu sağlanır).
- İki temada okunur (koyu: `#c9c2b3` ikincil metin; açık: `#5a6275`).
- Kapak (`kapak.png`, `kapak-koyu.png`): sol alt hap `YDT · TEMEL`.

## 4. Çakışma kapısı

Komut (sahne başına, ön planda, `timeout 280`): `node araclar/cakisma-kapisi.mjs 02-04-ydt-temel --sahne <s> --json
uretim-tutanagi/duz2-kareler/cakisma/<s>.json --port 41333 --sunucu 41022`.

| Sahne | Çıkış | Örnek | Kutu |
|---|---|---|---|
| 01-hyperframes-giris | 0 | 13 | 79 |
| 02-paperjs-kanca | 0 | 70 | 1.725 |
| 03-paperjs-ornek1 | 0 | 96 | 7.091 |
| 04-canvas-ornek2 | 0 | 101 | 2.106 |
| 05-canvas-ornek3 | 0 | 99 | 1.981 |
| 06-hyperframes-soru1 | 0 | 81 | 57.243 |
| 07-hyperframes-kural | 0 | 69 | 43.884 |
| 08-canvas-karsit1 | 0 | 61 | 676 |
| 09-canvas-karsit2 | 0 | 69 | 1.972 |
| 10-hyperframes-tuzak | 0 | 87 | 32.229 |
| 11-canvas-tuzak-cevap | 0 | 87 | 1.650 |
| 12-hyperframes-ozet | 0 | 61 | 39.009 |
| 13-hyperframes-mini-soru | 0 | 125 | 39.812 |
| 14-hyperframes-kapanis | 0 | 55 | 5.890 |

Her sahne: "çakışma yok". Çıktılar: `duz2-kareler/cakisma/<sahne>.{json,log}`.

## 5. Son `grep` çıktısı

```
$ grep -rnI "BASIC" projeler/02-04-ydt-temel --exclude='*RAPOR.md' --exclude-dir=uretim-tutanagi | wc -l
0
$ grep -rlI "BASIC" projeler/02-04-ydt-temel
projeler/02-04-ydt-temel/sahneler/06-hyperframes-soru1/RAPOR.md
projeler/02-04-ydt-temel/sahneler/01-hyperframes-giris/RAPOR.md
projeler/02-04-ydt-temel/sahneler/13-hyperframes-mini-soru/RAPOR.md
projeler/02-04-ydt-temel/sahneler/14-hyperframes-kapanis/RAPOR.md
projeler/02-04-ydt-temel/uretim-tutanagi/senaryo-taslak.md
projeler/02-04-ydt-temel/uretim-tutanagi/YV-RAPOR.md
projeler/02-04-ydt-temel/uretim-tutanagi/juri/YVJ-hukum.md
projeler/02-04-ydt-temel/uretim-tutanagi/DUZ2-RAPOR.md
```

Kalan 7 dosya tarihî kayıttır (sahne ajanı raporu, senaryo taslağı, YV raporu, jüri hükmü); o günkü durumu anlatır, üretim
girdisi değildir. `DUZ2-RAPOR.md` bu rapordur (eski metni alıntılar). Tarihî kayıtlara dokunmadım.
Üretim dosyalarında (kod, `index.html`, `kunye.js`, `surumler.json`, BRIEF) geçiş 0.

Huni kapısı (`dijital-anlatim/araclar/huni-kapi.mjs projeler/02-04-ydt-temel`): HV-24 **ÖLÇÜLEMEDİ** — "rozet kaynağı
bulunamadı". Neden: kapı rozeti `kunye.js` içinde `rozet:` anahtarında ya da `senaryo.json` `giris.rozetler`'de arar;
yatay künye `seviye:` anahtarını kullanır. Aynı ölçümün `BASIC` taraması sorun bulmadı (bulsaydı sonuç KALDI olurdu).

## 6. Açık kalanlar (bu istemin kapsamı dışı)

- **mp4 yeniden derlenmedi** (kural: render yok). `cikti.mp4`, `cikti-koyu.mp4`, `_is/` parçaları, sahne `video*.mp4`,
  sahne `kontrol.png`, `k/` kareleri ve kök `kontrol.png`, `kontrol-koyu.png` eski rozeti taşır. Yayından önce şef derlemesi
  gerekir.
- **Dersler arası biçim farkı:** SP ana (`simple-present-temel`) yatay künyesi `· YDT TEMEL` (noktasız), kapak ve rozet
  hapı `YDT · TEMEL`. Bu pakette künye HV-24 metniyle birebir `· YDT · TEMEL` oldu. Tek biçim için şef kararı gerekir
  (değişiklik `kunye.js` + 7 `yardim.py` içinde tek belirteç).
- **HV-24 kapı ölçülebilirliği:** huni kapısı yatay künyenin `seviye:` alanını okumuyor (§5). Kapı `dijital-anlatim`
  deposunda; bu istemin yazma kapsamı dışında.
- `uretim-tutanagi/duz2-kareler/` 29 MB (38 tam kare PNG); şef commit'e almak istemezse `Silinecekler/` altına taşınır.
- git commit atılmadı (şef atar).
