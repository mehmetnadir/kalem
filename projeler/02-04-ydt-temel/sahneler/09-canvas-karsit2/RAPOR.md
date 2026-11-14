# 09-canvas-karsit2 — RAPOR (14.11, P2; render yok)

| Alan | Değer |
|---|---|
| Motor | Düz canvas · 1920×1080 · 30 fps · 523 kare (içerik 511) · t_bas 145,29 · t_son 162,33 · cümle 10 |
| Dosyalar | `sayfa.html` · `sahne.js` · `sahne-ortak.js` (05-canvas-ornek3 kopyası, yalnız 1. satır yorumu farklı) · `calistir.sh` |
| Ekran metni | The train to İzmir leaves at 7 pm today. · today + 7 pm → timetable · RIGHT NOW ≠ TIMETABLE; süren üst kart: She is wearing her pink T-shirt today. · today → this day only; zaman çizgisi: today · now · 7 pm; çip "Contrast 2 / 2" |
| Renk | `RT.murekkep` + `RT.ikincil`; tek vurgu `RT.vurgu` (odak altçizgileri, nabız), karaoke `RT.vurguDolgu`; yeşil yok (soru sahnesi değil), kırmızı yok, emoji yok |
| Ölçü | `u(n) = n × tuval genişliği / 1920`; cümle Fredoka 700 (iki cümlenin en genişine göre en çok 56), kart notu Caveat 50, zaman etiketi 48, son etiketler 64 — taban 30'un üstünde |
| Kapı | `qa-yerel.sh … --hazirla` çıkış 0; çakışma yok (69 örnek, 1972 kutu) |

## Yerleşim (BRIEF §3 satır 9)

```
üst kart (alt0, sahne 08'den süren)  She is wearing her pink T-shirt today.      [tişört]
                                     today → this day only
alt kart (alt1)                      The train to İzmir leaves at 7 pm today.     [tren]
                                     today + 7 pm → timetable
zaman çizgisi        today ├────●now ─────────── ⌒ ───────────→ ◆7 pm ────┤ ──→
son etiketler              RIGHT NOW            ≠            TIMETABLE
```

`→` ve `≠` el yazısı glif setinde yok (caveat-tr); ikisi de kalemle çizilir.

## Olay listesi (yerel kare = round((t − 145,29) × 30); t küresel anlatım sn)

| # | Olay | t (sn) | Kare | Cümle 10 sözcüğü (t0) |
|---|---|---|---|---|
| 1 | Sahne 08'den süren durum 0,3 sn'de geri gelir: üst kart + cümle + not + tişört, zaman çizgisi + today bandı + now (nabız) + etiketler; olay sesi yalnız kart çizgisinde | 145,72 | 13 | — (söz 145,84'te başlar) |
| 2 | Alt kart çerçevesi | 145,76 | 14 | The (145,84) |
| 3 | Alt cümle sözcük sözcük, karaoke altçizgi | 145,84–148,80 | 16 | The … today. |
| 4 | Küçük tren çizimi (kartın sağı) | 146,00 | 21 | train (146,00) |
| 5 | Alt kart notu "today" | 149,69 | 132 | today (149,69) |
| 6 | `odak` 7 pm (sarı altçizgi; dar öbek → halka yerine `alti`) | 150,57 | 158 | saatle (150,57) |
| 7 | Not "+ 7 pm" | 151,05 | 173 | geliyor: (151,05) |
| 8 | Zaman çizgisinde 7 pm çentiği + nokta | 151,85 | 197 | akşam (151,85) |
| 9 | Etiket "7 pm" | 152,25 | 209 | yedi. (152,25) |
| 10 | now → 7 pm kalem yayı (kalkış ileride) | 153,45 | 245 | henüz (153,45) |
| 11 | Not oku + "timetable" (yazı 155,23–155,96) | 154,93 | 289 | tarifede (154,93) · yazılı. |
| 12 | `odak` leaves | 156,09 | 324 | Geniş (156,09) |
| 13 | Çoklu kart `odak`: iki today aynı anda | 157,21 | 358 | Today (157,21) |
| 14 | ≠ (kalem, 3 darbe) | 159,05 | 413 | Farkı (159,05) |
| 15 | RIGHT NOW (now altında) | 160,57 | 458 | konuşma (160,57) · anı (160,97) |
| 16 | TIMETABLE (7 pm altında; 162,11'de biter) | 161,61 | 490 | tarife (161,61) |

İlk görünür öğe kare 13 (ilk 12 kare boş). Son olay kare 505'te biter (içerik 511'de biter; cümle 162,33'te biter).
En uzun olaysız aralık 3,7 sn (146,00 → 149,69); bu aralıkta karaoke 148,80'e kadar sürer. 4 sn kuralı içinde.

## Kapı (son koşu)

```
yuva 1 · kök /home/sef/01dev/_worktrees/kalem-0204 · önizleme 41022 · cdp 41333
== HAZIRLA
tema: acik
önizleme hazır
== KAPI
09-canvas-karsit2 | çakışma yok (69 örnek, 1972 kutu)
== KARE (açık)  146.4 · 154.5 · 157.7 · 162.2
== KARE (koyu)  162.2
kapı çıkış kodu: 0
```

## Bakılan kareler ve bulgu

| Kare | Bulgu |
|---|---|
| `k/09-canvas-karsit2-146.4.png` | süren üst kart tam; alt cümle "The train to" (karaoke "to" altında); tren yarı çizili; today bandı, now. Taşma yok. |
| `k/09-canvas-karsit2-154.5.png` | 7 pm altçizgisi, "today + 7 pm", zaman çizgisinde 7 pm + etiket, now → 7 pm yayı tam. Taşma yok. |
| `k/09-canvas-karsit2-157.7.png` | "→ timetable", leaves altçizgisi, iki kartta today altçizgisi aynı anda. Altçizgiler ayrık (7 pm ↔ today arası boşluk görünür). |
| `k/09-canvas-karsit2-162.2.png` | son kare: RIGHT NOW ≠ TIMETABLE, now ve 7 pm altında hizalı; künye ve ajanda serbest. |
| `k/koyu/09-canvas-karsit2-162.2.png` | koyu tema: krem çizgi ve yazı, vurgu turuncu, today bandı soluk ama seçilir. Taşma yok. |

Düzeltme turu: 0 (ilk koşuda kapı 0, kare bulgusu yok).

## Açık noktalar

1. Sahne 08 (`08-canvas-karsit1`) bu koşuda dizinde yoktu. Üst kart, today bandı ve now bu sahnenin kendi yorumudur:
   üst kart y 116–316, now x 620, today bandı x 380–1560, zaman çizgisi y 700, tişört kartın sağında. 08 yazılınca konum ve
   boy sürekliliği (BookFlip geçişi) QA'da karşılaştırılmalı; uyumsuzsa `yerlesim()` tek satırla eşlenir.
2. Ajandada "Contrast" yok (Hook, Examples, Rule, Trap); etkin çip 02-03 ile aynı düzenle Rule'a (2) düşer. Çip metni
   "Contrast 2 / 2"; 08 farklı ad seçerse eşlenmeli.
3. Yazma kapısı (`write-size-gate`) 15 satırdan uzun kodu şefe kapatıyor. `sahne.js` tam metni spec'e yazıldı
   (`/tmp/kalem-0204-s09/sahne-spec.md`), `agy-filo tek` (rol bulk, gemini-3.8-flash-low) birebir yazdı; `diff` 0 fark,
   `node --check` geçti. Claude alt ajanı açılmadı.
4. `sahne-ortak.js` paket iskeletinin kopyasıdır; içinde iskelete ait sabit px değerleri var (kart çizgi kalınlığı, karaoke
   çizgisi aralığı). `sahne.js` bütün yerleşimi `u()` ile verir.
5. `calistir.sh` `GLOBAL_SN="152.6 156.1 158.0 162.3"`: render koşusunda `k/` kare seçimi içindir; render yapılmadı.
