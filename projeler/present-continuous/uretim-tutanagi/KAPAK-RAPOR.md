# KAPAK-RAPOR — present-continuous ana ders kapakları · 15.11.2026 (istem KAPAK-0201T)
| Dosya (`file`) | Boyut | Tema |
|---|---|---|
| `present-continuous/kapak.png` · `kapak-koyu.png` | 1920 × 1080 | açık · koyu |
| `present-continuous-dikey/kapak.png` · `kapak-koyu.png` | 1080 × 1920 | açık · koyu |
| `present-continuous/uretim-tutanagi/kapak-168.png` | 168 × 94 | açık (PIL LANCZOS) |
Yöntem: `simple-present-temel` üreticisinin kopyası (`sahneler/90-hyperframes-kapak/uret.py`, `yardim.py`, `calistir.sh`); dikey `calistir.sh` ana pakettekini `--duzen dikey` ile çağırır, görseller `present-continuous-dikey/ortak/kapak` göreli bağından. `bash calistir.sh --tema acik|koyu` → `hyperframes snapshot --at 0.5`. Sahne `zaman.json` listesinde yok; `zaman.json`, `surumler.json` değişmedi.
**Emsalden farklar.** (1) Metin `GİDİYORUM` · `= AM GOING` · `-yor → -ing` · `YDT · TEMEL`. (2) 9 harf sol %55'e sığsın diye yazı boyu 240 → 168 (yatay; vurgu kutusu x 1068), 190 → 160 (dikey). (3) Küçük boyda satır 1 ile kutu arası 21 px kalıyordu (kural 24): `k_ust = T1 + max(0,15·S, 0,02·S + 25)`. (4) Yatay: arka yumruk sağ alt süre bölgesine düşüyordu; karakter tam boy, tabanı y 975 (alttan taşmaz, krem kenar tabanı da çevirir), ölçek 0,84, yüz merkezi y ≈ 444, kronometre karakterin sol altında. (5) Dikey: kaynak satır 990'da düz kesik (arka yumruk üstü), ölçek 0,78, kronometre solda. (6) Görsel kopyasında 02-04 emsalinin kenar temizliği (alfa ≤ 64 + 3×3 açılış); kaynak PNG değişmedi.
| Kapı (§5) | Sonuç |
|---|---|
| 1. 4 PNG, boyut | GEÇTİ — `file`: 1920×1080 ×2, 1080×1920 ×2 |
| 2. 168 px | GEÇTİ — "GİDİYORUM = AM GOING" okunuyor, yüz seçiliyor; küçük satır zor (beklenen) |
| 3. Büyük İ glifi | GEÇTİ — `uret.py` her harfi Fredoka latin/latin-ext cmap'te arar (`assert`); İ noktası Fredoka biçiminde (yakın kesit, Read) |
| 4. Yazı ↔ görsel | GEÇTİ — alfa + kutu `assert` (pay 24 + kenar 10 px), 4 PNG göz denetimi |
| 4. Boş bölgeler | GEÇTİ — yatay sağ alt %15×%8 zemin dışı piksel 0/24.768; dikey üst ve alt %20 0/414.720 (iki tema; içerik y 400–1511) |
| Görsel | kırıntı yok (kaynakta yalnız gövdeye ≤ 7 px tek pikseller, kopyada temizlendi); yazı yok; kesik kenar yalnız dikeydeki bilinçli kesik |
**Açık kalan (şef/Nadir onayı):** (a) Yatay yazı boyu %15,6 (standart %18–24; 9 harf sol %55'e en çok ~168 px sığar). (b) Yatayda karakter tabanı alt kenardan 105 px yukarıda (emsal yatayda alttan taşar). (c) Dikeyde karakter ortanın 148 px sağında; ana yazı y 492'de başlar (bant 600; emsalle aynı). (d) Hız çizgileri krem kenarla leke gibi görünür, koyu temada belirgin (kenar yöntemi, görsel kusuru değil). İlk tur PNG'leri ve inceleme kesitleri `~/Silinecekler/2026-11-15-kapak/present-continuous-tur1/`; commit yok.
