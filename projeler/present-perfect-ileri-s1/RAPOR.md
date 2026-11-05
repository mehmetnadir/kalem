# present-perfect-ileri-s1 — S1 Shorts üretim raporu (05.11)

| Çıktı | Kare | Süre |
|---|---|---|
| cikti.mp4 (acik) | 693 | 23,1 sn |
| cikti-koyu.mp4 (koyu) | 693 | 23,1 sn |
| sahne 01 / 02 / 03 | 102 / 383 / 232 | zaman.json ile birebir (iki tema) |

102 + 383 + 232 − 2 × 12 = 693 (birlestir.py aynı sayıyı yazdı; ffprobe 693).

- Kod: spi şablonundan kopya. Değişen: `sahneler/*/{uret.py,olay.py,zamanlar.json,yardim.py,calistir.sh}`,
  `02-paperjs-ornek/{sahne-02.js,kalem-paper.js,sayfa.html}`, `nesneler.json` (3 sahne, boş şablon).
- Sahne 01: `AGO VARSA` / `SIMPLE PAST` (160 px, 984 px'e sığdı), satır 1 `Ago gördün mü,` + satır 2 `Present Perfect`
  (uçuş sonrası yazılır), figür standing-2 (440 px) + saat. Çip kapakta yok.
- Sahne 02: Faz A `elenir.` + `Bu sınav tuzağına düşme.`; Faz B EN kart (ago sarı alt çizgi) + TR + ev/figür(480)/takvim;
  Faz C `Ago var, yani` / `Simple Past` sarı daire / `Has moved` kırmızı çarpı (14,50) / `yanlış olurdu.`
  `kalem-paper.js`: yerel `altyaziSec` yok (kunye.js `altyaziMetin/altyaziCiz`); `?canli=1` iken `POST /log` atılmaz.
- Sahne 03: `Tam ders:` · `Present / Perfect` bandı · saat + `6 dakika` · `Tam ders kanalda · 6 dk` hapı.
- `ortak/kunye.js`: ders `PRESENT PERFECT`, rozet `YDT · ADVANCED` / `GRAMMAR` — doğru, dokunulmadı.
- Editör kapısı (surum=shorts, tema=acik): konsol hatası 0. `EDITOR.durum()`: t 1,9 slot 0 `hazir:true, goster:true` ·
  t 8 slot 1 `hazir:true, goster:true` · t 18 slot 2 `hazir:true, goster:true`. Ekran: `k/editor-t1.9.png`, `editor-t8.png`, `editor-t18.png`.
- Baktığım kareler: 01 `k/59.png`, `k/93.png` · 02 telefon kontağı `k/telefon-02.png` (acik), `k/telefon-koyu-02.png` ·
  03 `k/telefon-03.png` · koyu 3 sahne `k/telefon-koyu-01.png` · birleşik koyu `../k/birlesik-koyu.png`.
- Ağ: ilk açılışta 3 × 404 = eksik `nesneler.json` (3 sahne); eklendi, konsol 0.

## Sapmalar / açık sorular
- BRIEF-S1 `ago` için "kırmızı alt çizgi" der; görev metni "kırmızı yalnız tuzak çarpısında" der. Çelişki: `ago` altı SARI, kırmızı yalnız `Has moved` çarpısı.
- BRIEF-S1.md "altyazı bandı YOK" ve "§4" bölümü içermiyor (eski kopya); görev metnine göre altyazı bandı dolu (`altyazi.json`).
- Editör saati 664 kare, paket 693 (spi'de de aynı tür fark).
- Ses 23,60 sn, video 23,1 sn (şablonla aynı davranış).

## Neden yeniden
Yeniden koşu yok; 6 koşu da ilk denemede geçti (alarm 1200). Yalnız editör kapısında `nesneler.json` eklenip kapı tekrarlandı.
