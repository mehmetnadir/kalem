# Sahne 07 · kural kartı (HyperFrames, 667 kare, 87,78–109,61 sn; cümle 8)

Durum: P2 yazıldı, `ONIZLE_YALNIZ=1` hazırlığı koşuldu (koyu, sonra açık; son koşu AÇIK). Render yok. Kapı ve `sahne-kare` koşulmadı (şef EK); `k/` boş.
Tema: acik.

## İçerik
Üç bant (`tanim`, kalemle), söylendiği anda kademeli:
1. `NOW` → `am / is / are + V-ing` (bant çerçevesi ve sonuç sarı)
2. `THESE DAYS · NOWADAYS · PLAN` → `usually V-ing` + `(temporary / changing)` (soluk)
3. `USUALLY · GENERAL` → `V1 / V-s` (soluk)
Sağda üç örnek kartı küçük hâlde (We are leaving… / Our company… / It is getting harder…). Satır 2'nin üç sinyali (`THESE DAYS`, `NOWADAYS`, `PLAN`) söylenince bant sağ kenarından kendi örnek kartına ince çizgi gider; karttaki sinyal (`at 9`, `these days`, `nowadays`) sarı belirteç alır. "Önce sinyal sözcüğünü ara": bütün sinyal belirteçleri 108,25 sn'de kalınlaşır. Okla gösterim hepsi çizim (Fredoka'da → glifi yok).
Künye: sağ üst `Rule`, ajanda Rule etkin. Hareket 0,50–20,77 sn aralığında (ilk 12 ve son 12 kare durgun; `Y.kontrol` geçti).

## Olay ↔ sözcük (cümle 8; küresel sn)
| Olay | Sözcük (i) | Sözcük t0 | Olay sn | Sapma |
|---|---|---|---|---|
| Bant 1–3 çerçeveleri çizilir | Karar kartı. (0) | 88,33 | 88,33–88,73 | 0,00 |
| `NOW` + sarı belirteç | now (4) | 90,73 | 90,73 / 90,83 | 0,00 |
| ok + `am / is / are + V-ing` | şimdiki zaman (8) | 92,81 | 92,81 / 92,95 | 0,00 / 0,14 |
| `THESE DAYS` + belirteç + çizgi → örnek 2 | These days (10) | 94,09 | 94,09 / 94,19 | 0,00 / 0,10 |
| `· NOWADAYS` + belirteç + çizgi → örnek 3 | nowadays (13) | 95,37 | 95,37 / 95,47 | 0,00 / 0,10 |
| ok + `usually V-ing` | genellikle (14) | 96,25 | 96,25 / 96,37 | 0,00 / 0,12 |
| `(temporary` | geçici (18) | 98,49 | 98,49 | 0,00 |
| `/ changing)` | değişen (21) | 99,37 | 99,37 | 0,00 |
| `· PLAN` + belirteç + çizgi → örnek 1 | Planlı (23) | 100,57 | 100,57 / 100,67 | 0,00 / 0,10 |
| `USUALLY` + belirteç | Usually (29) | 103,21 | 103,21 / 103,31 | 0,00 / 0,10 |
| `· GENERAL` + belirteç | genel (34) | 105,45 | 105,45 / 105,55 | 0,00 / 0,10 |
| ok + `V1 / V-s` | geniş zaman (36) | 106,41 | 106,41 / 106,55 | 0,00 / 0,14 |
| bütün belirteçler kalınlaşır | sinyal (40) | 108,25 | 108,25 | 0,00 |
Örnek kartları 88,28–88,67 sn'de (söz öncesi, süs; önceki sahnelerin kartları).

## Kapı
Koşulmadı (EK). Yerinde kontroller: satır sağ uçları bant içinde (en geniş 999 px, bant sağ kenarı 1156) · kartlar çakışmıyor (y 286–374, 496–624, 726–854) · yazı tabanı ≥ 30 px (kart 30, sonuç 52, sinyal 56) · `node --check` JS tamam.

## Açık notlar
- Bant 2 / 3 sonuç metni soluk (IKN) kasıtlı: taslak "satır 1 sarı, satır 2–3 ikincil". Açık temada sarı metin (`#d9900f`) kontrastı düşük; sahne 12 de aynı dili kullanır.
- `PLAN` satırı: "Planlı gelecek" söylenince (100,57) eklenir; satır 2'nin sonucu (`usually V-ing`) ondan önce gelir (söz sırası böyle).

Dosyalar: `uret.py`, `olay.py`, `calistir.sh`, `yardim.py`, `proje/index.html`, `olaylar.json`.
Kare yolları: yok (EK).

## QA 13.11
- Kapı: HyperFrames, ölçülmez. Kareler `k/07-hyperframes-kural-{89,95,102,109}.png`, koyu `k/koyu/`.
- Göz: üç kural kartı (NOW / THESE DAYS·NOWADAYS·PLAN / USUALLY·GENERAL) ve sağda üç örnek kartı + bağ çizgileri taşmıyor. 102 sn karesinde 3. kart henüz boş (söz sırası; 109 sn karesinde dolu). Düzeltme yok. Kalan sorun yok.
- QA 13.11 ek: 3. kart "Usually" sözcüğünde (103,21 sn, `T(29)`) beliriyor; 102 sn karesinde boş olması doğru, düzeltme gerekmedi.
- zaman eşitleme 13.11: yeniden kuruldu (sunucu --hazirla). 3. kart "Usually" (103,21 sn) sözcüğünde beliriyor: 102,95 karesinde boş, 103,45 karesinde "USUALLY" yazılı (`k/07-hyperframes-kural-{102.95,103.45}.png`). Sözcük-işaret uyumu doğru.
