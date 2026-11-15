# KAPAK-RAPOR — 02-03-ydt-temel ana ders kapakları · 15.11.2026 (istem KAPAK-0203T, yalnız yatay)
| Dosya (`file`) | Boyut | Tema |
|---|---|---|
| `02-03-ydt-temel/kapak.png` · `kapak-koyu.png` | 1920 × 1080 | açık · koyu |
| `02-03-ydt-temel/uretim-tutanagi/kapak-168.png` | 168 × 94 | açık (PIL LANCZOS) |
Yöntem: `sahneler/90-hyperframes-kapak/` = 02-04 emsalinin kopyası (`SPEC.md`). `bash calistir.sh --tema acik|koyu` → `uret.py` → `hf_tema.py` → `hyperframes snapshot . --at 0.5`.
Emsalden farklar: metin + görsel + yüz ölçüsü (465, 480); `S1 ≤ S2` (ÖNCE vurgu satırından büyük olmaz); sütun daraltma araması (32 px; SİNYALE BAK kutusu saça 34 px yer açar); görsel üst kenarı %5 payında (kural eklendi). Sonuç: karakter 0,99, S1 = S2 = 144.

| Kapı maddesi | Sonuç | Bakılan |
|---|---|---|
| Boyut | 2/2 standart §1 ile aynı | `file` |
| 168 px'te ana yazı | okunur: `ÖNCE` / `SİNYALE BAK`, büyüteçli yüz ve lamba seçilir | `kapak-168.png` + koyu 168 kopyası (Read) |
| Büyük İ/Ö Fredoka | 11 harf cmap'te (İ latin-ext, öteki latin); İ noktası Fredoka biçiminde (Ş, Ğ metinde yok) | glif denetimi + satır 2 yakın kesit (Read) |
| Yazı–karakter üst üste | binmiyor: maske kuralı ≥ 34 px (kenar dahil) + göz | 2 PNG (Read) |
| Sağ alt %15×%8 | boş: zemin dışı piksel 0 / 24.768 (açık, koyu) | numpy |
| Kenar, kırıntı, beklenmeyen yazı | yok: saç, el, büyüteç, lamba kenarı düzgün; görselde yazı yok | kenar kesitleri (Read) |
Turlar: 1. çekimde saç üstü kenardan 44 px (standart %5 = 54) → kural eklendi, 2. çekim geçti. Ara 2 PNG `~/Silinecekler/2026-11-15-kapak/`.

**Açık kalan:** `BAK`'taki B tek iç boşluklu görünür; Fredoka 700'ün kendi glifi (2 kontur), hata değil. Lamba başın sağında, karakterden ≈ 130 px ayrık (emsal tabelası gibi). Dikey paket bu istemde yok; commit yok.
