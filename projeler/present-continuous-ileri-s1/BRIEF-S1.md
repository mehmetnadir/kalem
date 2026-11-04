# S1 Shorts — "I AM KNOWING = YANLIŞ" (present-continuous-ileri-s1, YDT İLERİ)

Çıktı: `cikti.mp4` (1080×1920, 30 fps, 23.76 sn, anlatım 23.76 sn hazır) + `kapak.png` + `kontrol.png`.
Ana BRIEF biçimi dikeye uyarlandı; stil, kalem darbesi, olay sesi kuralları `../present-continuous/BRIEF.md` ile aynı; dikey v2 ölçekleri
`../present-continuous-dikey/BRIEF-DIKEY.md` §2–§3 (HUD, ders adı 56, rozet 36, ≥ 64 px yazı). Kaynaklar: ses `ortak/anlatim/`
(cümle başları 1,00 · 6,93 · 16,37; toplam 23.76), senaryo `ortak/anlatim/senaryo.json`
(kaynak: `dijital-anlatim/pilot/grammar-tenses-01-ileri-s1/`). `ortak/kunye.js` dikey v2 tabanlıdır (tek rozet `YDT · ADVANCED`;
`GRAMMAR` rozeti yok); çip sağ üst `Trap`.

Kapak başlığı (2 satır, 4 sözcük): `I AM KNOWING` / `= YANLIŞ`. Can alıcı: "I am knowing diyemezsin; know -ing almaz."

## Dikey yerleşim (px) — dikey v2 bantları
| Bant | y | İçerik |
|---|---|---|
| HUD | 0–320 | logo sol üst (96 px), ders adı (56), rozet `YDT · ADVANCED` (72), çip sağ üst |
| İçerik | 352–1392 | kapak / örnek / CTA |
| Altyazı | 1400–1536 | konuşulan parça (`ortak/anlatim/altyazi.json`, 7 parça), Lexend 500 44 |
| Platform | 1536–1920 | BOŞ |

## Sahneler (zaman.json ile birebir)
| # | Klasör | Motor | Küresel sn | Kare |
|---|---|---|---|---|
| 01 | 01-hyperframes-kapak | HyperFrames | 0.00–3.00 | 102 |
| 02 | 02-paperjs-ornek | Paper.js | 3.00–15.82 | 397 |
| 03 | 03-hyperframes-cta | HyperFrames | 15.82–23.76 | 268 |

Sahne sınırı = bir sonraki cümle başı − 0,55; son sahne = son söz + 1,0 sn.

## Sahne içeriği (tablodaki sn KÜRESELDİR; yerel kare = round((t − t_bas) × 30))
| sn | Hareket |
|---|---|
| 0,65–1,45 | Kapak: başlık `I AM KNOWING` (190 px) kalemle; `= YANLIŞ` (sarı) |
| 1,00–6,38 | Cümle 1 sözcük zamanlı ekranda: `Biliyorum` (1,00) · `I am knowing` (1,81–2,13; kırmızı çarpı çizilir 2,86'da `diyemezsin.`) · `YDT tam burada tuzak kurar.` (4,14–5,90) |
| 2,0–3,0 | Uçuş: başlık → çip/ders adı, cümleler yukarı, figür (standing-3) solar |
| 6,93–10,45 | Sahne 02: kart `I know the answer, but I am not telling anyone.` Fredoka 64 sözcük zamanlı (`know` 7,25 sarı daire; `am not telling` 8,81–9,29 daire); ORTA: figür (sitting-4) + telefon (phone) 460 px |
| 10,70–12,62 | Caveat 64: `Cevabı biliyorum ama kimseye söylemiyorum.` |
| 13,78–15,82 | `Bilmek durumdur,` (13,78) → `know` üstüne `-ing` yazılıp kalemle çizilir (`-ing almaz.` 15,06) |
| 16,37–22,76 | Sahne 03 (CTA): `Tam ders:` (16,37) · `Present Continuous` bant (17,49) · `ileri seviye` (18,97) · saat (clock) + `6 dakika` (20,01–20,21) · `Tam ders kanalda · 6 dk` (21,00–22,32) · 1 sn durgun kuyruk |

## Çalıştırma
Her sahne `calistir.sh --tema acik`; sonra paket kökünden
`python3 birlestir.py projeler/present-continuous-ileri-s1 --tema acik --gecis BookFlip --efekt hisirti`.
