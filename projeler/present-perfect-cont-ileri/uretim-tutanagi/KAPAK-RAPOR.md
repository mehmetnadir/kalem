# KAPAK-RAPOR — present-perfect-cont-ileri ana ders kapakları · 15.11.2026 (istem KAPAK-0209I)
| Dosya (`file`) | Boyut | Tema |
|---|---|---|
| `present-perfect-cont-ileri/kapak.png` · `kapak-koyu.png` | 1920 × 1080 | açık · koyu |
| `present-perfect-cont-ileri-dikey/kapak.png` · `kapak-koyu.png` | 1080 × 1920 | açık · koyu |
| `present-perfect-cont-ileri/uretim-tutanagi/kapak-168.png` | 168 × 94 | açık |
Yöntem: emsal `simple-present-temel/sahneler/90-hyperframes-kapak/` kopyası (`uret.py --tema --duzen`, `yardim.py`, `calistir.sh`). Dikey sahnenin `calistir.sh` dosyası ana üreticiyi `--duzen dikey` ile çağırır; görsel `-dikey/ortak/kapak` göreli bağından gelir. `zaman.json` ve `surumler.json` değişmedi.
Emsalden farklar: (1) metin `SÜREÇ mi` / vurgu `SONUÇ mu?` / Lexend `have been doing · have done` / rozet `YDT · İLERİ`; küçük satır tek metin (ok yok). (2) Satır ve kutu sınırı mürekkepten hesaplanır (Ü noktası, Ç çengeli, g kuyruğu); satır arası 0,16 S. (3) Yazı boyu S: yatay 160, dikey 164 (emsal 240 / 190); `SONUÇ mu?` kutusu sol %55'e ve kaldırılan elin 34 px soluna sığar. (4) Karakter ölçeği yatay 1,00 (emsal 1,05); dikey 0,62, png satır 900'de düz kesik (iki el dahil). (5) Kum saati küçük (yatay 99 × 187, dikey 108 × 204), karakterin solunda. (6) Görsel kopyasına 02-04 yöntemi: alfa ≤ 64 + 3 × 3 açılış.
| Kapı (§5) | Sonuç | Bakılan |
|---|---|---|
| 1. 4 PNG, boyut | GEÇTİ: 1920 × 1080 ×2, 1080 × 1920 ×2 | `file` |
| 2. 168 px küçük görünüm | GEÇTİ: `SÜREÇ mi` / `SONUÇ mu?` okunur, yüz seçilir; küçük satır okunmaz (emsalde de) | `kapak-168.png` + koyu kopyası (Read) |
| 3. Glif İ/Ş/Ğ | GEÇTİ: her harf Fredoka / Lexend latin + latin-ext cmap `assert`; Ü, Ç Fredoka biçiminde; rozet İ Lexend | yakın kesit (Read) |
| 4. Yazı ↔ karakter | GEÇTİ: yazı–görsel ≥ 34 px, yazı–yazı ≥ 24 px, daire–yazı ≥ 24 px (`assert`) + göz | 4 PNG (Read) |
| 4. Sağ alt %15 × %8 | GEÇTİ: zemin dışı piksel 0 / 24.768 (açık, koyu) | numpy |
| 4. Dikey üst ve alt %20 | GEÇTİ: 0 / 414.720 her bölge, iki tema | numpy |
| 5. Emoji, kırıntı, kesik kenar | GEÇTİ: emoji yok; görselde yazı yok; ilk koyu karede el ve saç çevresinde benek (kaynakta ana şekil dışı tek pikseller) vardı, 6. madde ile 1 turda giderildi | yakın kesit (Read) |
Açık kalan: (a) Yazı boyu emsalden küçük: vurgu kutusu 190 px = kapağın %17,6'sı (standart %18–24); metin uzunluğu ve sol %55 sınırı yüzünden. Şef onayı gerekir. (b) Write kancası 15 satır üstü `.py` düzenlemesini kesti; düzenleme küçük parçalara bölündü. Yoklama importu emsal `__pycache__/uret.cpython-310.pyc` dosyasını yeniden derledi (kaynak değişmedi). (c) Ara kareler ve kesitler `~/Silinecekler/2026-11-15-kapak/`; commit yok.
