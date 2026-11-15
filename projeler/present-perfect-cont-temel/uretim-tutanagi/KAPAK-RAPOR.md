# KAPAK-RAPOR — present-perfect-cont-temel ana ders kapakları · 15.11.2026 (istem KAPAK-0209T)
| Dosya (`file`) | Boyut | Tema |
|---|---|---|
| `present-perfect-cont-temel/kapak.png` · `kapak-koyu.png` | 1920 × 1080 | açık · koyu |
| `present-perfect-cont-temel-dikey/kapak.png` · `kapak-koyu.png` | 1080 × 1920 | açık · koyu |
| `present-perfect-cont-temel/uretim-tutanagi/kapak-168.png` | 168 × 94 | açık (PIL LANCZOS) |
Yöntem: emsal `simple-present-temel/sahneler/90-hyperframes-kapak/` (`uret.py`, `yardim.py`, `calistir.sh`) kopyası; dikey `calistir.sh` ana betiği `SAHNE=` ile çağırır, görsel `-dikey/ortak/kapak` göreli bağından. Metin şef kararı: `İKİ SAATTİR` · kutu `= HAVE BEEN` · `-dir … -yor` → `have been -ing` · `YDT · TEMEL`.
Emsalden farklar: (1) metin uzun → S 240 → 160 (yatay), 190 → 146 (dikey); satır 1–kutu aralığı `max(0,15·S, 0,02·S + 25)` (S < 185'te PAY 24 px altına düşüyordu). (2) Karakter masa ve kitapla tam (kesik yok, `alt_kesik` kapalı): yatayda ölçek 0,95, masa altı y 970; dikeyde 0,655, sağa yaslı. (3) Saat küçük, karakterin yanında: yatay masanın solunda (0,28), dikey dirseğin solunda (0,30). (4) Kopyada kırıntı temizliği eklendi (emsal 02-04 yöntemi: alfa ≤ 64 + 3×3 açılış; kaynak PNG değişmedi).

| Kapı (§5) | Sonuç | Bakılan |
|---|---|---|
| 4 PNG, boyut | 4/4 standart §1 ile aynı | `file` |
| 168 px ana yazı | okunur (`İKİ SAATTİR` / `= HAVE BEEN`), yüz seçilir; küçük satır okunmaz (beklenen) | `kapak-168.png` + koyu kopyası (Read) |
| İ/Ş/Ğ Fredoka | İ Fredoka latin-ext (yuvarlak nokta); `…` ve `·` Lexend latin; her harf `assert` | satır 1 yakın kesit (Read) |
| Yazı–görsel binmez | `denetle()` assert (pay 24 + kenar 10 px) geçti; göz denetimi temiz | 4 PNG (Read) |
| Sağ alt %15×%8 | zemin dışı piksel 0 / 25.056 (açık, koyu) | numpy |
| Dikey üst/alt %20 | 0 / 414.720 her bölge, iki tema; içerik y 400–1527 | numpy |
| Emoji, öğe | emoji yok; yazı, karakter, nesne, logo, rozet (+ açık temada krem daire) | 4 PNG |
Turlar: 2 çekim. 1. turda çıkartma kenarında basamak vardı (kaynakta gövde dışı 1–2 piksellik kırıntı: karakter 127, saat 105; alfa ikili 0/255); temizlikten sonra kenar düz.
**Açık kalan:** (a) Kaynak `karakter.png`/`nesne.png` kırıntılı (arka plan temizleyici artığı); kaynak düzeltilmedi, kopyada süzüldü. (b) Fredoka 700 `B` sol üst çentikli; yazı tipi tasarımı (PIL ile aynı), hata değil. (c) Yatayda yazı bloğu ortadan ≈ 50 px yukarıda (saç kenarı kutuyu sınırlar); dikeyde karakter ortadan ≈ 200 px sağda (standart "ortalı"; emsal de sağda). (d) Ara kareler `~/Silinecekler/2026-11-15-kapak/`; commit yok.
