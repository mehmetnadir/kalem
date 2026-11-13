# Sahne 14 — Kapanış (HyperFrames, 323 kare, t_bas 272,42; cümle 19; son sahne, geçişsiz)

Durum: P2 yazıldı, önizleme hazırlığı (ONIZLE_YALNIZ=1, son koşu açık tema) tamam. Render, kapı ve sahne-kare YOK (12:40 şef notu; QA şeridi koşar).
Dosyalar: `uret.py` · `olay.py` · `yardim.py` · `calistir.sh` · `proje/index.html` · `olaylar.json` (12 olay).
Kalıp: ileri `12-canvas-kapanis` (SIGNAL → VERB, sonraki ders kartı), HyperFrames diliyle. İçerik süresi 293 kare = anlatım bitişi (281,69) + 0,5 sn (282,19).

## İçerik
- `SIGNAL` (Fredoka 150) + sarı alt çizgi; kalemle ok; `VERB` sarı + sarı halka.
- `believe → no -ing` notu (cümle 19 «believe gibi fiiller -ing almaz»; sahne 12 özet metniyle aynı ifade).
- Sonraki ders kartı: `Next lesson` · `GR-02-04` · `Simple Present vs Present Continuous` (konu-adlari.json); giriş süresi dışında (K23).
- Künye: `· YDT BASIC`, sağ üst `Next lesson`, ajanda etkin Trap.

## Olay ↔ sözcük t0 (küresel sn)
| Olay | Sözcük (cümle.i) | Sözcük t0 | Olay t | Sapma |
|---|---|---|---|---|
| SIGNAL (sinyal) | sinyal (19.3) | 274.17 | 274.17 | +0.00 |
| sarı alt çizgi (altını) | altını (19.5) | 275.13 | 275.13 | +0.00 |
| kalem oku (Sonra) | Sonra (19.7) | 276.17 | 276.17 | +0.00 |
| VERB (fiile) | fiile (19.8) | 276.57 | 276.57 | +0.00 |
| sarı halka (bak:) | bak: (19.9) | 276.93 | 276.93 | +0.00 |
| believe | believe (19.10) | 277.53 | 277.53 | +0.00 |
| ok (fiiller) | fiiller (19.12) | 278.25 | 278.25 | +0.00 |
| no -ing (-ing) | -ing (19.13) | 278.89 | 278.89 | +0.00 |
| no -ing belirteç (almaz.) | almaz. (19.14) | 279.29 | 279.29 | +0.00 |
| kart çizimi (Sonraki) | Sonraki (19.15) | 280.25 | 280.25 | +0.00 |
| GR-02-04 (derste) | derste (19.16) | 280.65 | 280.65 | +0.00 |
| kart başlığı + ok (görüşürüz.) | görüşürüz. (19.17) | 280.97 | 280.97 | +0.00 |

Kontrol: tüm komut zamanları ilk 12 kare ve son 12 kare dışında (ihlal yok); `node --check` JS tamam; kart başlığı genişlik doğrulaması (assert) geçti; kapı ve kare görüntüsü QA şeridine kaldı (`k/` boş).
Kare yolları: `k/` (QA şeridi dolduracak).

## QA 13.11
- Kapı: HyperFrames, ölçülmez. Kareler `k/14-hyperframes-kapanis-{273,276,279,281.5}.png`, koyu `k/koyu/`.
- Göz: SIGNAL → VERB, believe → no -ing, sonraki ders kartı (GR-02-04) sığıyor, künye doğru. Düzeltme yok. Kalan sorun yok.
- zaman eşitleme 13.11: yeniden kuruldu (t_bas 270,34, kare 333); kareler `k/14-hyperframes-kapanis-{272.5,274.9,276,279.2}.png`.
