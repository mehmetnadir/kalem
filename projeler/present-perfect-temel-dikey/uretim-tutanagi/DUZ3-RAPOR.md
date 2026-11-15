# DUZ3-0206T — `present-perfect-temel-dikey` (dikey tam ders) içerik düzeltmesi · 16.11.2026

> Ana rapor: `../present-perfect-temel/uretim-tutanagi/DUZ3-RAPOR.md` (cümle tablosu, Whisper, gerekçeler). Bu dosya yalnız dikey pakete
> özgü olanı yazar. Render yok, mp4 yok, commit yok.

## 1. Ses ve ortak dosyalar

| Dosya | Durum |
|---|---|
| `ortak/anlatim` | ana pakete sembolik bağ (değişmedi) → `anlatim.wav` sha256 iki yolda eşit `d2d68143c965`; `sureler.json`, `sozcukler.json`, `altyazi.json`, `METIN.md` aynı dosya. Yeniden sentez yok |
| `surumler.json` | ana pakete sembolik bağ → `canAlici[4]` ve r2 revizyonları (ana-yatay, dikey-tam) tek yazımla iki pakette |
| `zaman.json` | 04: kare 564, 34,16–52,56 · 05: kare 482, 52,56–68,23 · 06: kare 939, 68,23–98,53 (ana ile aynı kare ve zaman; genişlik/yükseklik ve `gecis` alanları dikeyin) |
| `youtube.json` | ana ile bayt bayt aynı (bölüm 4 52,56, bölüm 5 68,23; bildirim 34,71 değişmedi) |
| `youtube-aciklama.md` | damga 00:53 ve 01:08; ana ile fark yalnız `utm_content=dikey-tam` |

## 2. Sahneler (dikey)

| Sahne | Ne değişti | Neden |
|---|---|---|
| 01 giriş | `yardim.py` `ROZET = "YDT · TEMEL"` (kapak hapı + künye hapı), `uret.py` yorum → `proje/index.html` (`olaylar.json` aynı çıktı) | HV-24 |
| 02–05 künye | `ortak/kunye.js` `rozet: "YDT · TEMEL"` | HV-24 |
| 04 örnek 2 | 26 sabit c4 yeni ses zamanlarına (ana ile aynı eşleme), KARE 564; 2. nota (750, fUst − 22) → (770, fUst − 6), 3. nota fUst + 2 → + 14 | c4 yeni ses; çakışma kapısı hatası (§4) |
| 05 örnek 3 | 36 sabit c5 yeni ses zamanlarına, TBAS 52,56, KARE 482; etiketler `never · ever · just` → tek `never` (ortalı; boşluk hesabı `24 * (boslar.length - 1)`) | c5 yeni metin |
| 06 soru + form | `zamanlar.json` ana ile aynı dosya içeriği; notlar `geçmiş` → `şimdiye bağlanıyor`; tablo `SINYAL_SATIRLARI` (sol iki parça, sağ iki parça, her biri kendi sözcüğünde; evre 5'te hepsi söner); kod kartı `geçmişten → şimdiye` (ok "köprü"de, aralık + 24 / + 112); `yardim.py` künye hapı `YDT · TEMEL`; altyazı parçaları `altyazi.json`'dan otomatik | c7 yeni metin + HV-24 |
| `calistir.sh` 04, 05, 06 | kare sayısı ve denetim anları (06: `(t − 68,23) × 30`) | yeni süre |
| `BRIEF-DIKEY.md` | kare sayıları, rozet, 05 ve 06 satırları | belge yeni duruma |

## 3. Kareler (kendim baktım; `sahneler/<sahne>/k/duz3/`, git dışı; koyu `k/duz3/koyu/`)

`node araclar/sahne-kare.mjs present-perfect-temel-dikey <sahne> <t,…> <dizin> --tema acik --port 41333 --sunucu 41022`, sahne sahne.

| Sahne | Anlar (sn) | Gözlem |
|---|---|---|
| 01 | 1,2 · 2,9 | rozet hapı `YDT · TEMEL` + `GRAMMAR`; künye hapı `YDT · TEMEL` |
| 04 | 41 · 46 · 48,6 · 51,7 | altyazı `For süreyi söyler.`, `Bu kez has, çünkü özne üçüncü tekil kişi.`; notalar TR satırına ve `başladı,` yazısına değmez (düzeltme sonrası) |
| 05 | 56,2 · 60,3 · 63,9 · 67,9 | tek `never` etiketi ortada, ok `now` noktasına; altyazı `Burada never, hayatın bugüne kadarki kısmını kapsar.` 2 satır |
| 06 | 70,5 · 74,5 · 75,6 · 79 · 83,6 · 87,7 · 91,6 · 95 · 97,4 · 98,4 | `geçmiş` / `→ şimdiye bağlanıyor` ortalı; tablo satırları 2 satırlı (sol / ok + sağ), `süre · başlangıç` ve `az önce · çoktan` kutu içinde (x ≤ 1020); kod kartı `geçmişten → şimdiye` kart içinde; altyazı c7 parçaları |
| 06 koyu | 91,6 | tablo koyu zeminde okunur |

## 4. Çakışma kapısı

```
$ node araclar/cakisma-kapisi.mjs present-perfect-temel-dikey --sahne <s> --port 41333 --sunucu 41022 --json ~/is/duz3-0206T/kapi-dikey-<s>.json
01 0 · 02 0 · 03 0 · 05 0 · 06 0
04 ilk koşu: çıkış 1 — "Kardeşim beş yıldır gitar çalıyor." × nota, kesişim 34×12 px (x 750; 2. notanın salınımı "gitar"ın g kuyruğuna biniyor;
   konumlar bu işten önce de aynıydı, önceden var olan kusur)
   2. nota (750, fUst + 2) denemesi: "başladı," × nota 19×6 px → (770, fUst − 6): çıkış 0 (75 örnek, 1577 kutu)
→ son durum 6 / 6 çıkış 0
```

## 5. Açık kalanlar

Ana raporun §9'u dikey için de geçerlidir (EK-11 dinleme, mp4 ve canvas `olaylar.json` render adımında, yet kapsamı, kapak jürisi). Dikey ≈ 102 sn
(3 + 98,53 + ≈ 1) → Shorts sınırı (≤ 180 sn) içinde kalır; YVJ Not 1 (dikey damga bloğu) şef kararı olarak açık.

---
Son Güncelleme: 16.11.2026 (DUZ3-0206T oturumu).
