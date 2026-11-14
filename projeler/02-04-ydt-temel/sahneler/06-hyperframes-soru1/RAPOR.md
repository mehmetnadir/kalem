# Sahne 06 — Soru anı 1 (HyperFrames, 613 kare, t_bas 93,35; cümle 6 öğrenci + 7 öğretmen) · 14.11

Tema: acik

| Alan | Durum |
|---|---|
| Kapı (`qa-yerel.sh … --hazirla`) | çıkış kodu **0** · `çakışma yok (81 örnek, 57243 kutu)` |
| Önizleme | `ONIZLE_YALNIZ=1 bash calistir.sh` tamam (komut 111, olay 45); render YOK |
| Üretim yolu | şef tasarımı `SPEC.md` → `agy-filo tek --rol kod` (gemini-3.8-flash-high, 344 sn) `uret.py` yazdı → şef okudu, 2 küçük Edit (docstring `yanılgı:` satırı, figür adı) |
| agy özeti | `/home/sef/.claude/canavar/agy-filo/20261114-221630/ozet.md` (1/1 başarılı; `eksik`/`SAHİPSİZ`/`bos-kosu` yok) |
| Dosyalar | `uret.py` (agy) · `SPEC.md` · `olay.py`, `calistir.sh`, `yardim.py` (01 sahnesinden kopya, KARE=613) · `olaylar.json` · `proje/index.html` |

## İçerik
- Kare 0: sahne 05'in iki kartı statik (sıkı düzen): *The train to İzmir / leaves at 7 pm today.* + TIMETABLE ·
  *I am going to the / movie theater tonight.* + ARRANGEMENT; *leaves* ve *am going* sarı altçizgili (05'in odakları).
- Soru anı 1: öğrenci başı (`ogrenci-bas.svg`, sol alt) + el balonu, soru sözcük sözcük (10 sözcük ≤ 12); *-ing* sarı altı;
  sarı nokta balonu sol karttaki *leaves*e bağlar. 0,67 sn duraklama (97,74 → 98,41) olaysız; cevap 2 sn içinde.
- Cevap: balon söner, baş kalır. Sağ: figür + `person ↳ plan ↳ am / is / are + V-ing`, sarı ok figür → *am going*.
  Sol: tren çizimi + `train ↳ timetable ↳ V1 / V-s`, sarı ok tren → *leaves*. Öğrenci 1 sn baş sallar.
  "özne genelde cansızdır": *The train* altı sarı, tren nabzı, uçak ve kitap simgesi.
- yanılgı: tarifeli gelecek planlanmış gelecekle karışır (BRIEF/taslak `yanılgı:` satırı 1). Kırmızı, yeşil, emoji yok; tek vurgu `RENK.vurgu`.
- Künye: `SIMPLE PRESENT vs PRESENT CONTINUOUS · YDT BASIC`, sağ üst `Question`, ajanda etkin Examples.

## Olay listesi (olay · kare · küresel sn · cümle sözcüğü)
| Olay | Kare · sn | Sözcük |
|---|---|---|
| baş çizimi | 13 · 93,78 | — (ilk 12 kare durgun) |
| balon | 15 · 93,85 | 6 · Hocam, |
| soru sözcükleri (ilki) | 17 · 93,90 | 6 · Hocam, (her sözcük kendi t0'ında) |
| sarı nokta + bağ → leaves | 38 · 94,62 | 6 · tren |
| -ing altı | 109 · 96,98 | 6 · -ing |
| balon söner, ARRANGEMENT nabzı | 152 · 98,41 | 7 · Planı |
| figür + person | 171 · 99,05 | 7 · kişi |
| ↳ plan | 179 · 99,33 | 7 · yapar: |
| ok figür → am going | 205 · 100,17 | 7 · ben, |
| ↳ am / is / are + V-ing | 243 · 101,45 | 7 · arkadaşım. |
| tren + train | 277 · 102,57 | 7 · Tren |
| ↳ timetable | 317 · 103,93 | 7 · tarifeye |
| ok tren → leaves | 334 · 104,49 | 7 · uyar. |
| öğrenci baş sallar (1 sn) | 348 · 104,95 | 7 · uyar. sonu |
| TIMETABLE nabzı | 356 · 105,21 | 7 · Tarife |
| ↳ V1 / V-s | 406 · 106,89 | 7 · geniş |
| The train altı | 485 · 109,53 | 7 · özne |
| tren nabzı | 544 · 111,49 | 7 · tren, |
| uçak simgesi | 566 · 112,21 | 7 · uçak, |
| kitap simgesi (son hareket yerel 19,97 ≤ 20,03) | 589 · 112,97 | 7 · ders. |

## Kapı (son çıktı)
```
06-hyperframes-soru1 | çakışma yok (81 örnek, 57243 kutu)
kapı çıkış kodu: 0
```

## Bakılan kareler (`k/`, `k/koyu/`)
| Kare | Bulgu |
|---|---|
| `k/06-hyperframes-soru1-97.6.png` | soru tam, -ing altı, nokta → leaves; taşma/binme yok |
| `k/06-hyperframes-soru1-106.2.png` | iki zincir, iki ok, tren, figür; oklar yazı kesmiyor |
| `k/06-hyperframes-soru1-113.3.png` | son hâl: The train altı, uçak + kitap; boş alan yalnız alt orta |
| `k/koyu/06-hyperframes-soru1-108.png` | koyu tema: kontrast iyi, vurgu turuncu-sarı |

Düzeltme turu: 1 (figür pozu). Denenen `standing-4/5/6` (düşünme pozu, kadın görünümlü; K22'ye ters) → `standing-1`e dönüldü.
Bayat deneme karesi `~/Silinecekler/2026-11-14-0204/06-hyperframes-soru1-deneme/` altına taşındı.

## Açık noktalar
1. BRIEF "figür işaret pozu" istiyor; Open Peeps setindeki 6 ayakta pozun hiçbirinde işaret eden kol yok (SVG kol ölçümü).
   Ok figürün başından çıkıyor. İşaret pozu için yeni figür kaynağı ya da çizilmiş çöp adam: Nadir kararı.
2. Figür `standing-1` (kıvırcık saç, şort, protez bacak). Erkek öğretmen sesine (K22) yakın, ama cinsiyeti belirsiz.
3. Alt orta (x 250–1600, y 780–1000) boş kalıyor; öğrenci başı sol altta küçük. Bilinçli: soru anı sonrası sakin alan.
4. agy özetinin "değişen" listesinde 02/04 sahne dosyaları da var. Bunlar paralel oturumların kendi koşuları
   (kendi SPEC.md'leri 22:15–22:16'da yazılmış); bu iş yalnız `06-hyperframes-soru1/uret.py` yazdı.
