# 04-canvas-ornek2 — RAPOR (14.11, P2; render yok)

Motor: Düz canvas · 1920×1080 · 30 fps · 762 kare (içerik 750) · t_bas 43,85 · t_son 68,84 · cümle 4.
BRIEF §3 satır 4: `kart` sol/sag, `cizim` (ev, bavul), `zaman_cizgisi` (uzun bant / kısa aralık bandı, now iki bandın içinde),
`odak` (*live*, *am living*). Ekran metni: senaryo-taslak satır 4 (I live in İstanbul with my family. · My parents are out of
town, so I am living with my uncle. · PERMANENT / TEMPORARY). Çip: Example 2 / 3.

## DURUM: BLOKLU — sahne.js yazılamadı

| Dosya | Durum |
|---|---|
| `calistir.sh` | yazıldı; `bash -n` geçti; `ONIZLE_YALNIZ=1 bash calistir.sh --tema acik` → "önizleme hazır", rc 0 |
| `sayfa.html` | 02-03 örneğinin aynısı (canvas + `./sahne.js`) |
| `sahne-ortak.js` | 02-03 örneğinin kopyası; yalnız 3 yol 02-03 → 02-04 (`sed`, içerik değişmedi) |
| `sahne.js` | YAZILMADI: `write-size-gate.sh` 15+ satır kod dosyasını blokluyor (106 satır). Kapının yolu delegasyon (agy); istem "alt ajan açma" diyor. Bypass bayrağını Claude oluşturamıyor. |
| QA (`qa-yerel.sh`) | KOŞULMADI (sahne.js yok) |

## Planlanan olaylar (sahne.js taslağı oturumda hazır; yerel kare = round((t − 43,85) × 30))

| Cümle:sözcük | t0 (sn) | Kare | Olay |
|---|---|---|---|
| 4:0 İkinci | 44,40 | 17 | daire içinde 2 |
| 4:2 Kancadaki | 45,76 | 57 | sol kart çerçevesi |
| 4:4 live. | 47,20 | 101 | `live` (Fredoka 72) + sarı altçizgi (47,55) |
| 4:5–11 I … family. | 48,09–49,61 | 127–173 | sol cümle sözcük sözcük (Fredoka 56, 4+3), karaoke altçizgi |
| 4:12 Ailemle | 50,82 | 209 | ev çizimi (tabler home, sol kart sağ alt) |
| 4:15 Orada | 52,90 | 272 | sol zaman ekseni + now noktası (53,15) |
| 4:16 hep | 53,30 | 284 | uzun bant (kalıcı), now bandın içinde |
| 4:18 Kalıcı | 54,58 | 322 | PERMANENT (Caveat, kalem yazar, 54,58–55,54) |
| 4:20 geniş | 55,54 | 351 | `odak` *live* sarı altçizgi |
| 4:22 My (−0,35) | 56,64 | 384 | sağ kart çerçevesi |
| 4:22–34 My … uncle. | 56,99–59,95 | 394–483 | sağ cümle sözcük sözcük (6+7) |
| 4:37 dışında, | 62,28 | 553 | bavul çizimi (kendi SVG'miz, sağ kart sağ alt) |
| 4:42 Bu | 65,00 | 635 | sağ zaman ekseni + now noktası (65,25) |
| 4:44 şimdilik. | 65,60 | 653 | kısa aralık bandı + iki uç çizgisi (66,00) |
| 4:45 Geçici | 66,84 | 690 | TEMPORARY (Caveat, 66,84–67,88) |
| 4:47 şimdiki | 67,88 | 721 | `odak` *am living* sarı altçizgi (68,28'de biter) |

## Açık noktalar

- Karar: sahne.js için kapı bypass'ı (Nadir) ya da agy delegasyonu izni.
- Kanca arızası (srv21): `write-size-gate.sh` bayrak yaşını `stat -f %m` ile ölçer (macOS sözdizimi). GNU stat'ta bu komut
  dosya sistemi bilgisi basar, rc 1 verir (ölçüldü). Bayrak varken aritmetik hata → kanca çıkış 1 (bloklamaz), bayrak
  silinmez → tek kullanımlık değil, kalıcı açık kalır (çıkarım; uçtan uca denenmedi).
- QA zamanları (anlatım saniyesi; `sahne-kare.mjs` t_bas…t_son bekler): açık 56.2,63.5,68.6 · koyu 68.6.
