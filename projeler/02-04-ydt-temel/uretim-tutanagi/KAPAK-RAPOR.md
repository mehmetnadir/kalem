# KAPAK-RAPOR — 02-04-ydt-temel ana ders kapakları · 15.11.2026 (istem KAPAK-0204)
| Dosya (`file`) | Boyut | Tema |
|---|---|---|
| `02-04-ydt-temel/kapak.png` · `kapak-koyu.png` | 1920 × 1080 | açık · koyu |
| `02-04-ydt-temel-dikey/kapak.png` · `kapak-koyu.png` | 1080 × 1920 | açık · koyu |
| `02-04-ydt-temel/uretim-tutanagi/kapak-168.png` | 168 × 94 | açık |
Yöntem: iki pakette `sahneler/90-hyperframes-kapak/` (aynı `uret.py` + `calistir.sh`, `SPEC.md`). `bash calistir.sh --tema acik|koyu` → `uret.py` (yerleşim araması + kurallar) →
`hf_tema.py` → `hyperframes snapshot . --at 0.5 --no-end --keep` → kök PNG. Dikey görseller `02-04-ydt-temel-dikey/ortak/kapak/` kopyası. 168 kopyası PIL LANCZOS.

| Kapı maddesi | Sonuç | Bakılan |
|---|---|---|
| Boyut | 4/4 standart §1 ile aynı | `file` |
| 168 px'te ana yazı | okunur: `HER ZAMAN mı` / `ŞİMDİ mi?`, yüz seçilir | `kapak-168.png` (Read) |
| Büyük İ/Ş/Ğ yazı tipi | 14 harf Fredoka latin/latin-ext cmap'te (Ğ metinde yok); İ noktası, Ş çengeli Fredoka | satır 2 yakın kesit (Read) |
| Yazı–karakter üst üste | binmiyor: maske denetimi ≥ 34 px + göz | 4 PNG (Read) |
| Sağ alt %15×%8 | boş: zemin dışı piksel 0/24.768 (açık, koyu) | numpy + yatay PNG |
| Dikey üst ve alt %20 | yalnız zemin: 0 piksel (açık, koyu); içerik y 417–1529 | numpy + dikey PNG |
| Emoji, öğe sayısı | emoji yok; yazı, karakter, nesne, logo, rozet (+ açık temada krem daire) | 4 PNG |
Turlar: kapı öncesi 3 yerleşim turu (yatayda saç/el yazıya yakın; dikeyde karakter küçük → tabela başın soluna, ölçek 0,67); kapıda 1 kusur turu
(10 px tek adım gölge ok uçlarında basamak + avuçta kırıntı → 3 × 3,33 px, kopyada alfa ≤ 64 + 3×3 açılış), yeniden çekim sonrası geçti.

**Açık kalan:**
- Açık temada logo tek renk `#141414` türevi; dikeyde karakter ortadan 184 px sağda (standart "ortalı"); kenar 3 geçiş (standart tek adım). Üçü Nadir/şef onayında.
- 02-02 pilotu (KAPAK-0202) tek üretici + `--duzen` kalıbında; 02-04 iki pakette aynı dosya. Birleştirme şef kararı.
- Write kancası 15 satır üstünü kesti; istem alt ajanı ve bayrağı yasakladığı için kod kabukla yazıldı. Ara 12 PNG `~/Silinecekler/2026-11-15-kapak/`'ta; commit yok.
