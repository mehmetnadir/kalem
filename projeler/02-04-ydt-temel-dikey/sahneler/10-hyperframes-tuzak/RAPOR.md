# Sahne 10 · tuzak + soru anı 2 — DİKEY (HyperFrames, 1080×1920, 656 kare, 162,33–183,79 sn; cümle 11–12)

Tema: koyu

Durum: yazıldı (istem D-dikey, 15.11.2026, srv21). Önizleme hazırlığı `ONIZLE_YALNIZ=1`. Render yok, commit yok.
Kod yolu: şef `SPEC.md` yazdı → `agy-filo tek --rol kod` `uret.py`'yi yazdı → şef okudu, 1 küçük düzeltme (Edit) → `qa-yerel.sh` 2 tur.

| Ölçüt | Sonuç |
|---|---|
| Kapı (`qa-yerel.sh`) | çıkış 0 · çakışma yok (87 örnek, 19.608 kutu) |
| HUD | logo 48,48 387×96 · ders 2 satır (Fredoka 56, taban 212/276) · rozet `YDT · BASIC` · çip `Trap`; kare 0'dan tam |
| Altyazı | cümle 11 + 12 → 7 dilim, aynı anda tek dilim, bant 1400–1536 |
| Sarı belirteç | aynı anda en çok 3 (kutu · `?` · fosfor → nokta çizgisi · altçizgi; eskisi ikincil) |
| Ses olayı | 20 (`olaylar.json`; tik 10, cizgi 10), hepsi kare < 644 |
| Hareket | 0,55–21,31 sn yerel (ilk ve son 12 kare durgun, `Y.kontrol`) |

## Yerleşim (SPEC.md §4)

```
358  TRAP (Fredoka 96 sarı, kart kenarındaki boşlukta)
392  ┌ kart (toplanmış; ilk hâli 600–1144, bant ortası)                    ┐
     │ (TR) Ailemle İstanbul'da        ikincil Fredoka 600 72               │
     │      yaşı-[yor]-um.             ek_ayir, kutu vurguDolgu             │
     │   ?  ↙ bag (dikey gövde, ok ucu live'da)    ┐ sarı nokta çizgisi     │
     │      I [live] in İstanbul       Fredoka 700 72, live fosfor          │
     │      with my family.                        │                        │
936  └─────────────────────────────────────────────┼────────────────────────┘
966  balon (x 290–843) Caveat 64, 3 satır ●────────┘           baş (aynalı)
1276 └ kuyruk sağa → (870, 1270)                         x 891–1009, y 1220–1380
1400 altyazı · 1536+ platform bandı BOŞ
```

## Olay listesi (kare = sahne içi, sn = küresel)

| Olay | Kare | sn | Sözcük |
|---|---|---|---|
| TRAP + kart kenarı (açık yol, TRAP boşluklu) + `kartg` 0,93→1 | 16–43 | 162,88–163,78 | Tuzak. (11/0) |
| hap `TR` (çizgi + yazı) | 45 | 163,84 | Türkçe (11/1) |
| EN: I · live · in · İstanbul / with · my · family. | 113–165 | 166,09–167,83 | 11/5–11 |
| TR1 `Ailemle İstanbul'da` | 190 | 168,66 | Türkçesi (11/12) |
| TR2 `yaşıyorum.` bitişik | 216 | 169,54 | yaşıyorum. (11/13) |
| `ek_ayir` → `yaşı-yor-um.` (renk +0,20, tire +0,28) | 269–282 | 171,30–171,73 | yor (11/15) |
| `bag` yor → live (S eğrisi + dikey gövde + ok ucu) | 312–330 | 172,74–173,34 | Yor (11/18) |
| sarı `?` (kolun solunda) | 358 | 174,26 | akla (11/22) |
| *live* fosfor + pilMetin | 418–428 | 176,26–176,61 | -ing (11/27) |
| kart yukarı toplanır (y −208) | 452–462 | 177,40–177,75 | cümle 11 sonu |
| öğrenci başı (3 yol) + balon | 460–478 | 177,65–178,30 | Hocam, (12/0) − 0,20 |
| balon sözcükleri (3 satır) | 466–639 | 177,85–183,64 | 12/0–9 |
| sarı nokta + çizgi → *yor*; `?` ikincil | 511–524 | 179,37–179,82 | yaşıyorum. (12/2) |
| *living* sarı altı; nokta çizgisi ikincil | 571–581 | 181,36–181,71 | living (12/5) + 0,3 |

## Kapı sonucu (son koşu)

```
== KAPI
10-hyperframes-tuzak | çakışma yok (87 örnek, 19608 kutu)
== KARE (açık)  174.8 · 177.2 · 183.7
== KARE (koyu)  183.7
kapı çıkış kodu: 0
```
Komut: `bash araclar/qa-yerel.sh 02-04-ydt-temel-dikey 10-hyperframes-tuzak 174.8,177.2,183.7 183.7 --hazirla`

## Bakılan kareler ve bulgu

| Tur | Kare | Bulgu | Düzeltme |
|---|---|---|---|
| 1 | k/174.8, 177.2 | `bag` ok ucu tik (✓) gibi okunuyor; uç *live*'dan 27 px uzak | eğri CY+296'dan dikey gövdeyle iner, uç CY+332 (fosfor üstünden 12 px); assert eklendi |
| 1 | k/183.7, k/koyu/183.7 | taşma, kesik yazı, binme yok; koyu temada kutu/fosfor üstü yazı koyu, okunur; platform bandı boş | — |
| 2 | k/177.2 | ok net aşağı, ucu *live*'da; `?` kanattan ≥ 12 px | — |
| 2 | k/ara/163.3, 171.45, 173.1, 177.55, 178.15, 179.7 (`kontak-ara.png`) | kart kenarı çizimi, ek_ayir ara hâli, bag, toplanma, balon çizimi, sarı nokta çizgisi (sağ boşluktan kanala) temiz; 179,7'de `?` ikincil | — |

## agy koşusu

`~/.claude/canavar/agy-filo/20261115-123133` — 1/1 başarılı, 238 sn, gemini-3.8-flash-high. Özetteki "değişen" listesi paralel
oturumun 06 dosyalarını da gösterir (sözleşme notu); bu sahneyle ilgisi yok.

## Açık noktalar

1. **TR satırları üstte, EN altta.** BRIEF EN'i önce sayar ama konum yazmaz. EN üstte olunca *yor* → *live* kolu "with" ve "Ailemle"yi
   keser (ölçüm: live x 273–394, with x 239–382). EN sözcükleri yine söylendiği anda alt satırlarda belirir.
2. **Ölçüler BRIEF'ten sapar** (BRIEF §2.10 "y yaklaşık"): kart 600–1144 → 392–936 (BRIEF 600–1040 → 380–820; 4 satır + 92 px kanal + TRAP
   kenarı); balon 966–1276, baş sağ altta 1220–1380 (BRIEF "balon + baş 860–1380").
3. **Öğrenci başı aynalı** (yüz sola, balona bakar). Sahne 11 başı aynı yere koyar (x 870–1030, y 1220–1380); 11 aynalamazsa geçişte
   baş yön değiştirir. Sahne 11 yazarı `scale(-s s)` kullanmalı.
4. Yaklaş evresinde (162,88–177,40) bandın üstü (352–566) ve altı (1144–1392) boştur; BRIEF "kart önce bant ortasında". Boş kart çerçevesi
   yok (kart 3,2 sn içinde dolmaya başlar). Doluluk sahne sonunda 358–1380 (%98).
5. `TRAP` etiketi sarı yazıdır (bölüm etiketi, stil §2); belirteç sayısına katılmadı. `yaklas` çevre karartması yok (yatay emsal).

Dosyalar: `SPEC.md`, `uret.py` (agy + 1 şef düzeltmesi), `olay.py` + `yardim.py` (dikey 01 kopyası), `calistir.sh` (01 kalıbı, KARE 656),
`proje/index.html`, `olaylar.json`, `k/` (3 açık + 1 koyu + 6 ara + kontak), `RAPOR.md`.
