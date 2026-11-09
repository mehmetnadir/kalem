# Teslim kapısı — oynatıcı v2 (prototip 0.2, 09.11.2026)

Nadir 09.11: "oldukça güzel görünüyor" + 3 soru (cihaz yükü, görüntüde kaçan, basılı tutma 2×) + "duraklat ikonu ve
bitiş ekranı sorunlu". Bu sürüm: 2 simge kusuru + bitiş ekranı düzeltmesi + basılı tutma 2× (turbo.js) + yük ölçüm aracı.

Ekran görüntüleri: `araclar/oynatici-kare.mjs` (`--oynat 1` gerçek tık, `--basili <px>` bas-tut); scratchpad
`oynatici-kare/v2-*.png`: oynar 1440 · bitiş 1440 · turbo 1440 · turbo kilit 1440 · turbo 390 dokunma · bitiş dikey.
**DİKKAT:** çekim sırasında makine yükü çok yüksekti (load 280, başka oturumda swift derlemesi); kareler doğru, süreler değil.

| # | Madde | Sonuç | Kanıt |
|---|---|---|---|
| 1 | Görüntüye bakıldı (1440 + 390) | GEÇTİ | 7 PNG şef okudu. Düzeltilen: duraklat simgesi dolu kare çıkıyordu (`.ko-oynat svg path{fill}` + 2 px kontur çubuk arasını kapatıyordu → `[data-ik=oynat|dur]` kuralı, kontur yok, çubuk arası 3); "Tekrar izle" simgesi dolu leke oluyordu (aynı kural `.ko-buyuk`'teki kontur simgeyi de dolduruyordu); bitişte afiş başlığı sahne künyesine biniyordu (`.ko-bitti .ko-poster-ust` gizli, karartma .46); ses T'den 0,6 sn kısa bitince çubuk tam dolmuyordu (`bitir` t = T) |
| 2 | Emoji taraması | GEÇTİ | `emoji-tara.sh`: temiz (6 dosya) |
| 3 | Yapay görünüm | GEÇTİ | `impeccable detect ortak/oynatici`: 0 bulgu (regex kipi). 2× kapsülü: koyu cam zemin, sarı halka, kontur simge; gradyan/parlama yok |
| 4 | Hareket | GEÇTİ | Kapsül belirme 150 ms (`ko-belir`), halka dolumu 80 ms doğrusal; `prefers-reduced-motion` genel kuralı ikisini de sıfırlar |
| 5 | Erişilebilirlik | GEÇTİ (masaüstü) | Kapsül `button` + `aria-label` (2× hız / 2× kilitli, çıkmak için dokun); canlı bölge: "Hız 2×", "Hız 2× kilitlendi", "Hız 1×"; kilitliyken sıradan dokunuş duraklatmayı korur (turbo.js testi) |
| 6 | Metin | GEÇTİ | Türkçe: "sahneye basılı tut 2×, basılıyken aşağı sürükle: kilit" (sayfa notu) |
| 7 | Algılanan hız / cihaz yükü | ÖLÇÜLDÜ | `araclar/oynatici-olcum.mjs` (Performance.getMetrics + rAF + longtask + Network; cpu 1 / 4); sonuç tablosu defterde (dijital-anlatim `grammar-defter.md` 09.11) ve PRD §7 |
| 8 | Uygulama kipi | GEÇTİ | Kapsül 34 px yüksek, tepede ortada, sahne künyesiyle çakışmaz (1440 ve 390 görüntüde) |

Basılı tutma davranışı (Nadir tarifi: YouTube/Instagram): sahneye 500 ms bas-tut → 2×, kapsül "2× »"; basılıyken aşağı
sürükle → halka dolar (eşik = sahne boyu × 0,3, 48–96 px); dolunca kilit (sarı halka + kilit simgesi), parmak kalkınca da 2×
sürer; kilidi kapsüle dokunuş ya da hız menüsü çözer; video bitince çözülür. 12 px'ten çok kayma = kaydırma niyeti, iptal.
Etkinken `touchmove` engellenir (sayfa kaymaz); kilitliyken sıradan dokunuş duraklat / kontroller gibi davranır. Dokunmatik
orta düğmelerin üstünde bas-tut çalışmaz (düğme). Testler: `araclar/test/oynatici-turbo.test.mjs` (5 test, saf durum makinesi).

Açık (Nadir kararı, v1'den sürüyor): kontrol çubuğu sahne üstünde (künye alt satırı yalnız kontroller açıkken örtülür) mü,
altında mı. Afiş görseli yok. Gerçek iPhone'da bas-tut ve `-webkit-touch-callout` denenmedi.
