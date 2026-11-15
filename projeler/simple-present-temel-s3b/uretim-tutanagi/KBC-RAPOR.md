# KBC-RAPOR — simple-present-temel-s3b (A/B kol b, değişken `kanca`) · 15.11.2026 (istem KBC-0202S3)

| Ölçüm | Kol a (`simple-present-temel-s3`) | Kol b (`simple-present-temel-s3b`) |
|---|---|---|
| Değer (`varyant.deger`) | `yanlis-cumle` (EN `He doesn't goes.` + TR `Hata nerede?`) | `soru` (TR `Olumsuzda s nereye gider?`) |
| Kanca karesi | `BU CÜMLE` / `YANLIŞ` + kart `He doesn't goes.` | `S NEREYE` / `GİDER?` + kart `He goes.` |
| Toplam süre | 25,08 sn | 24,43 sn (`anlatim.m4a` ffprobe 24.430000; taslak tahmini 24,67) |
| Kanca sahnesi | 0,00–3,89 (129 kare) | 0,00–3,24 (109 kare) |
| İlk söz | 1,00 sn | 1,00 sn |
| Yeni sentez | — | 1 cümle · 1 parça · 25 karakter (≈ 0,12 TL) |
| Whisper en düşük | 0,93 | 0,93 (parça 3·1, önbellek; yeni parça 1,00) |
| `diff -rq` satırı | — | 74 (bu rapor dahil); beklenmeyen 0 |
| Çakışma kapısı | — | çıkış 0 (4 sahne, çakışma yok) |
| Üretici model | — | Claude Opus 5.5 (`claude-opus-5-5`); jüri başka modelle koşmalı (juri-olcutleri §1e) |

## 1. Değişen dosyalar (kol b)

| Dosya | Değişiklik |
|---|---|
| paket (tamamı) | kol a'nın `cp -a` kopyası, `uretim-tutanagi/` hariç; 423 ↔ 423 dosya; bayt farkı 0; git dışı 211 varlık sha256 eşit (`kopya-denetim.txt`) |
| `ortak/{cizim,font,logo,hf_tema.py}`, `ortak/logo/yds-publishing-koyu-zemin.svg` | simge bağı → gerçek kopya (bağlar Silinecekler'de); paket içinde bağ 0 |
| `ortak/anlatim/senaryo.json` | cümle 1 (`parcalar` + `metin`); `giris.satir1/2` ve `meta.kapak.satir1/2` → `S NEREYE` / `GİDER?` (`kapak-taslak.md` §4; s1b emsali). Kadro, sesler, cümle 2–4, `meta.kimlik` aynı |
| `ortak/anlatim/` türevleri | `cumle-1.wav`, `sentez.wav` (+ rapor), `anlatim.wav`, `anlatim.m4a` (+ imza), `sozcukler.json`, `sureler.json`, `baslar.json`, `altyazi.json`, `METIN.md` |
| `zaman.json` | 4 sahnenin `t_bas` / `t_son` değeri −0,65; sahne 01 `kare` 129 → 109, `icerik_kare` 117 → 97; 02–04 kare sayısı aynı |
| `sahneler/01-hyperframes-kanca/` | `uret.py` (söz, başlık, kapak kartı, `doesn't` girişi, `es` çizgisi, zaman), `zamanlar.json`, `olay.py` (+ şapka `cizgi` olayı), `calistir.sh` (`KARE=109`), `proje/index.html`, `olaylar.json`, `devir.json` (yalnız `t`), `RAPOR.md`, `SPEC.md` (üstte kol b notu), `k/`, `proje-ka/`, `proje-ka-koyu/` (kol a kareleri Silinecekler'de) |
| kök `kapak-a.png` = `kapak.png` | yeni kanca karesi (t 0,90, altyazısız; md5 `a7b1535b…`); koyu `sahneler/01-hyperframes-kanca/k/koyu/kapak-a-koyu.png` |
| kök `kapak-b.png`, `kapak-c.png`, `hikaye.png`, `hikaye-a.png`, `hikaye-b.png` | `~/Silinecekler/2026-11-15-kol-b/simple-present-temel-s3b/grup-turevleri/` (grup türevi; kol a'dakiyle bayt aynı) |
| `surumler.json` | 4 satır: `s3b` (kısa, `varyant`, önizleme `/p/simple-present-temel-s3b/onizle.html`, ad `S3b Shorts (24,43 sn)`), `s3b-kapak-a`, `s3b-aciklama-a`, `s3b-aciklama-b` |
| `aciklama.md`, `aciklama-a.md`, `aciklama-b.md` | yalnız `utm_content`: `s3-a` → `s3b-a`, `s3-b` → `s3b-b` (adresler, üst bilgi satırı, UTM tablosu); `aciklama.md` = A (`cmp` eşit) |
| kol a `surumler.json` | yalnız `s3` satırına `varyant: {"grup": "s3", "kol": "a", "degisken": "kanca", "deger": "yanlis-cumle"}` (`git diff` 7 ekleme, 1 silme: `"ana-yatay"` satırına virgül) |

Kol b `varyant`: `{"grup": "s3", "kol": "b", "degisken": "kanca", "deger": "soru"}`. İki JSON `json.load` ile ayrıştı; `deger` `[a-z0-9-]`;
`dosya` alanlarının hepsi pakette var. Değişmeyen: `BRIEF-S3.md`, sahne 02–08, `ortak/` (anlatım dışı), `gorevler.json`, `yorumlar.json`, `harita-konum.json`.

## 2. Ses tablosu (`sentez.wav.rapor.json`; tohum hepsi 0; günlük `ses-sentez.log`, el.py rc 0, kapı önbelleği 7 / 8)

| Cümle | Konuşan (ses …son 4) | Parçalar | Kaynak | `cumle-N.wav` sha256 kol a | kol b | Whisper (parça) |
|---|---|---|---|---|---|---|
| 1 | öğretmen …4fwc | TR `Olumsuzda s nereye gider?` | **yeni** | `132a1a3113c2` | `5ff705528f78` | 1,00 (duyulan `Olumsuzda S nereye gider?`) |
| 2 | öğretmen …4fwc | TR `Olumsuzda ve soruda does girer, s ona geçer.` · TR `Fiile s gelmez.` · EN `He doesn't go. Does she go?` | önbellek | `6cbf7b4efbd3` | `6cbf7b4efbd3` | 0,96 (`döz`) · 1,00 · 1,00 |
| 3 | öğretmen …4fwc | TR `Does varsa fiil yalın.` · TR `Bir arkadaşına gönder; o da karıştırıyor.` | önbellek | `569e61237aa4` | `569e61237aa4` | 0,93 (`Döz`) · 1,00 |
| 4 | öğrenci …9gjY | TR `Bu sadece başlangıç.` · TR `Dersin tamamı YDS Publishing YouTube kanalında.` | önbellek | `6a9927c66d00` | `6a9927c66d00` | 1,00 · 1,00 (ses metni `YeDeSe`, sözlük `ses-sozluk.json` `kisaltma.YDS`; duyulan `YEDESE Publishing`) |

Cümle 1 yeni sesinde İngilizce sözcük yok; `s` Whisper'da `S` (harf adı). Öteki 7 parçanın Whisper değeri kapı önbelleğinden gelir (kol a ile aynı).

## 3. Süreler (sn)

| Öğe | Kol a | Kol b |
|---|---|---|
| Toplam | 25,08 | 24,43 (hedef 22–26; sınır 35) |
| Cümle başları 1 · 2 · 3 · 4 | 1,00 · 4,44 · 13,39 · 18,65 | 1,00 · 3,79 · 12,74 · 18,00 |
| Cümle 1 süresi | 2,89 | 2,24 (taslak tahmini 2,48) |
| Sahne 01 kanca | 0,00–3,89 | 0,00–3,24 |
| Sahne 02 değer | 3,89–12,84 (281 kare) | 3,24–12,19 (281 kare) |
| Sahne 03 kaydet | 12,84–18,10 (170 kare) | 12,19–17,45 (170 kare) |
| Sahne 04 çağrı | 18,10–25,08 (239 kare) | 17,45–24,43 (239 kare) |
| Kanca sözcükleri | He 1,00 · doesn't 1,32 · goes. 1,72 · Hata 2,69 · nerede? 3,09 | Olumsuzda 1,00–1,72 · s 2,04–2,20 · nereye 2,28–2,60 · gider? 2,68–3,32 |
| Kırmızı `?` · çıkış başı | 2,69 · 3,39 | 2,28 · 2,73 |

## 4. Tek değişken kanıtı (`diff -rq simple-present-temel-s3 simple-present-temel-s3b`; satır listesi `diff-rq.txt`)

| Sınıf | Satır | İçerik |
|---|---|---|
| değişen sahne `01-hyperframes-kanca` | 34 | `uret.py`, `zamanlar.json`, `olay.py`, `calistir.sh`, `olaylar.json`, `devir.json`, `proje/index.html`, `RAPOR.md`, `SPEC.md`, `__pycache__`; `k/` 16, `proje-ka[-koyu]/` 8 |
| senaryo | 1 | `ortak/anlatim/senaryo.json` |
| yeni ses | 6 | `cumle-1.wav`, `sentez.wav`, `sentez.wav.rapor.json`, `anlatim.wav`, `anlatim.m4a`, `anlatim.m4a.imza` |
| zaman ve söz türevleri | 6 | `sozcukler.json`, `sureler.json`, `baslar.json`, `altyazi.json`, `METIN.md`, kök `zaman.json` |
| `surumler.json` | 1 | kol b satırları + `varyant` |
| açıklamada `utm_content` | 3 | `aciklama.md`, `aciklama-a.md`, `aciklama-b.md` |
| kapak A (kanca karesi) | 2 | `kapak-a.png`, `kapak.png` |
| çıkarılan grup türevleri | 5 | `Only in` kol a: `kapak-b.png`, `kapak-c.png`, `hikaye.png`, `hikaye-a.png`, `hikaye-b.png` |
| `uretim-tutanagi/` | 16 | iki kolun ayrı tutanağı (bu rapor dahil) |
| **Beklenmeyen** | **0** | — |

Satırları düzenli ifade kurallarıyla bir betik sınıfladı (kurallar `diff-rq.txt` başlıklarında). Sahne 02–08 ve `ortak/` (anlatım dışı) satır vermedi:
bayt aynı. Sahne 02/04 karesi iki kolda aynı yerel anda bayt aynı (02: kol a 8,40 ↔ kol b 7,75; 04: 25,07 ↔ 24,42, `cmp`).

## 5. Kapı ve kareler

```
node araclar/cakisma-kapisi.mjs simple-present-temel-s3b --port 41333 --sunucu 41022   → çıkış 0
01-hyperframes-kanca | çakışma yok (14 örnek, 781 kutu)
02-paperjs-deger | çakışma yok (37 örnek, 667 kutu)
03-hyperframes-kaydet | çakışma yok (22 örnek, 3125 kutu)
04-hyperframes-cagri | çakışma yok (29 örnek, 4974 kutu)
```
İlk koşu sahne 01'de 1 uyarı verdi (0,50 sn, yarım çizilmiş hap çerçevesi × `GİDER?` kutusu, 22×13 px, kutu sağ üst köşesi). Sebep: İ noktası
tek `<text>` kutusunu köşeye dek yükseltir. `GİDER?` aynı konumda iki parça (`Gİ` + `DER?`) yazıldı; mürekkep aynı. Kayıt `kapi-cikti.txt`.

| Sahne | Açık kareler (küresel sn) | Koyu | Gözle bakış (Read) |
|---|---|---|---|
| 01 | 0 (ilk) · 0,90 (kapak) · 1,15 · 1,40 · 1,65 · 2,12 · 2,50 · 2,80 · 3,00 · 3,23 (son) | 2,12 | taşma, çakışma, okunmayan yazı yok; şapka tabanın altında, `doesn't` soldan sağa açılıyor, `es` çizgisi `goes` altında, `?` kart köşesinde; çıkışta kart y 480 |
| kapak A | `kapak-a.png` (açık), `k/koyu/kapak-a-koyu.png`, 168 px küçük görünüm | koyu | altyazı, şapka, `?` yok; başlık 168 px'te okunuyor; İ noktası hap içinde |
| 02 · 04 | 7,75 (orta) · 24,42 (video son karesi) | — | kol a karesiyle bayt aynı; son karede ana ders kapağı ve `@ydspublishing · YouTube` |

- Kanal katmanı: ilk (0), orta (7,75), son (24,42) karede mürekkep kutusu x 107–595 (Paper.js sahnesi 598), y 296–339; kol a'nın aynı karelerinde aynı.
- Son kare (sahne 01, 3,24 ↔ kol a 3,90): kanal, künye, içerik, boş bantlar 0 piksel farklı; kart bölgesinde `es` glif kenarında 183 piksel
  (en çok 60/255, kenar yumuşatma); altyazı bölgesi farklı (beklenen).
- Yüzey taraması (`Tam ders`, `dakika`, `dk`: senaryo, altyazı, METIN, açıklama, `surumler.json`, sahne HTML/JS, `ortak/*.js`) boş. Emoji 0. mp4 0.
- Kareler: `sahneler/01-hyperframes-kanca/k/` ve `~/qa-kare/simple-present-temel-s3b/` (`kanal-a/`, `kanal-b/`).

## 6. Açık noktalar

1. **Kulak kararı (EK-11):** `gider?` yükselen tonla mı, `s` "se" diye mi duyuluyor? Whisper `S` yazdı (1,00); kulakla dinlenmedi.
2. **Kanca sonu yakınsaması (BK-RAPOR açık nokta 1):** taslak uygulandı. 1,62–3,24 arasında kol b kartı kol a kartıdır (`He doesn't goes.`), 2,28'de kırmızı `?` gelir.
3. **`?` bekleme süresi:** `?` çizimi 2,72'de biter, çıkış 2,73'te başlar (kol a'da `?` 0,26 sn tam duruyordu). Sebep: ölçülmüş söz taslaktan kısa çıktı (2,24 ↔ 2,48).
4. **Taslaktan sapma:** sözcük kayması 1,00–1,30, `doesn't` açılması 1,30–1,62 (taslak 1,00–1,40 ve 1,20–1,60); açılan sözcük kayan `He` ile kesişmesin.
   Çıkış C0 = 2,7333: `gider?` sözcük sonu (3,32) ses bitişini (3,24) aşar; çıkış içerik sonuna (kare 97) bağlandı.
5. **`GİDER?` iki parça:** kapı ölçümünden doğan yazım (`Gİ` + `DER?`); görüntü tek yazıyla aynı. Jüri bakacak.
6. **Kayma tam kare değil:** 0,65 sn = 19,5 kare. Sahne 02–04 görüntüsü sese göre kol a'da +0,010 sn, kol b'de −0,007 sn kayar (yarım kare içinde).
7. **`BRIEF-S3.md`** kol a kanca tarifini taşır; tek değişken kuralı için bayt aynı tutuldu. Kol b kanca tarifi: `sahneler/01-hyperframes-kanca/RAPOR.md`, `senaryo-taslak.md`.
8. **Açıklama üst bilgisi:** `s3-aciklama-a/b` sürüm adları ve `kapak-b.png`, `kapak-c.png`, `hikaye-*.png` gönderimleri kaldı (istem: YALNIZ `utm_content`).
   Bu dosyalar gruba aittir, kol a paketindedir.
9. **Mutlak yol:** değişmeyen sahne 02 (`sayfa.html`, `sahne-02.js`, `kalem-paper.js`) ve `ortak/kunye.js` `KOK` kol a'yı `/projeler/simple-present-temel-s3/`
   yoluyla yükler (s2b ile aynı). Yerel zaman tutarlı (veri ve `tBas` kol a'dan, oynatıcı `tbas` kol b'den); kol a panelde yoksa kol b sahne 02 kırılır.
10. **Rozet `YDT · BASIC`:** standart §9 `YDT · TEMEL` der; tek değişken için iki kolda birlikte düzeltilmeli.
11. **Jüri koşmadı:** D-0338 teslim kapısı için görsel + dil jürisi başka modelle koşmalı. Kovan kaydı yazılmadı (yazma alanı paket dizini).
    Sözleşme kancası için `K/.claude/docs/sozlesme.md` dosyasına 1 satır eklendi.
