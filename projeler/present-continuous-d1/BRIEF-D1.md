# Present Continuous D1 — "-yor = -ing" dikey parça (YDT temel, 9:16)

Amaç: ana projedeki (`../present-continuous/BRIEF.md`) kalem görsel dilini dikey parçada göstermek.
Çıktı `cikti.mp4` (1080×1920, 30 fps, 54,33 sn) + `kontrol.png`. Ses hazır: `ortak/anlatim/anlatim.wav` (53,33 sn; yeniden sentez yok).
Kod: `ING-YDT-GR-02-01-T-D1`. Cümle başları (sn): 1,00 · 2,27 · 9,68 · 16,97 · 27,42 · 34,94 · 45,90.

## 0. Kaynak
| Öğe | Yol |
|---|---|
| Ses + süreler | `ortak/anlatim/{cumle-1..7.wav, sureler.json, anlatim.wav}` (kaynak `~/01dev/dijital-anlatim/pilot/grammar-tenses-01-dikey-d1/ses/`) |
| Sözcük zamanları | `ortak/anlatim/sozcukler.json` = `sozcuk_uret.py` (sureler.json + cümle başları; Whisper yok) |
| Senaryo (yalnız başvuru) | `ortak/anlatim/senaryo.json` |
| Sembolik bağ (ana proje) | `ortak/{cizim,font,logo}` |

## 1. Teknik çerçeve
`zaman.json`: genişlik 1080, yükseklik 1920, fps 30, `gecis_kare` 12, tema açık. `kare = round((t_son − t_bas)×30) + 12`
(son sahne +30 kare kuyruk). Yerel f ↔ küresel `t_bas + f/30`; ilk 12 ve son 12 kare geçiş altında durgun.
Kareler yakala.py'ye `1080 1920` verilerek alınır; HyperFrames `data-width 1080 data-height 1920`.

| # | Klasör | Motor | Kare | Küresel sn | Anlatım |
|---|---|---|---|---|---|
| 1 | 01-hyperframes-giris | HyperFrames | 102 | 0,00–3,40 | cümle 1 |
| 2 | 02-paperjs-kanca | Paper.js | 431 | 3,00–17,37 | cümle 2 (sonu) + 3 |
| 3 | 03-canvas-ek | düz canvas | 551 | 16,97–35,34 | cümle 4 + 5 |
| 4 | 04-hyperframes-form | HyperFrames | 582 | 34,94–54,33 | cümle 6 + 7 |

## 2. Stil
Ana BRIEF §2 aynen (açık palet, Fredoka/Caveat/Lexend, kalem darbesi, ses olayları). Dikey fark: içerik yazısı ≥ 50 px;
Caveat not 56–110, Fredoka cümle 64–140.

## 3. Künye (dikey HUD)
| Öğe | Konum |
|---|---|
| Ders adı `PRESENT CONTINUOUS` | x 48, taban 104, Fredoka 700 36 |
| Rozet `YDT · BASIC` | x 48, y 136–182, hap |
| "Şu an" çipi (`Hook` · `Examples` · `Form`) | sağ üst, x 1032'ye yaslı, y 62–110 |
| Logo | x 48, y 1464–1512 (yükseklik 48) |
| Platform bandı | y 1536–1920 BOŞ |

## 4. Bantlar
HUD 0–288 · içerik 288–1344 · altyazı 1344–1536 (kullanılmaz) · logo 1440–1536 sol · platform 1536–1920 boş.

## 4a. Sahne sözleşmeleri
| Sahne | Hareket |
|---|---|
| 01 | rozet `YDT · BASIC` + `GRAMMAR` (0,3–0,9); başlık `-YOR` / `= -ING` 230 px kalemle (0,65–1,45); `Gidiyorum.` 1,0 sn; figür (standing-3) + ev (home); 2,0–3,0 başlık künyeye uçar |
| 02 | `Bu akşam amcamlara gidiyorum.` sözcük zamanlı, `gidiyorum` sarı daire; `-yor → şimdiki zaman` + saat; figür ev yönünde yürür; 9,9 kutu, 11,53'ten `I am going to my uncle's tonight.`, `going` daire; 14,02 `aynı plan` + `-yor ⇄ -ing` |
| 03 | `fiil + -ing`; `go → go-ing`; `gidi-yor-um → go-ing` halkalar + `= iş sürüyor`; 29,11 `runn-ing` / `koşu-yor` + figür; kutuda `ek değişmez: -ing -yor` |
| 04 | `be` + `I am / He is / We are` sözcük zamanlı, `now` ayracı, `be + V-ing` kutusu, `in progress →`; 45,5 hepsi sol üste küçülür; 47,17 `-yor = -ing` (Fredoka 140, bant merkezi); `Gidiyorum.` / `I am going.`; 1 sn kuyruk |

## 6. Olaylar
Ana BRIEF §6: `cizgi` her darbe; `tik`, `vurus`, `parilti`; birlestir `--efekt hisirti` yalnız `cizgi` çalar.

## 7. Kabul
Ana BRIEF §7 + `cikti.mp4` 53–55 sn, `kontrol.png` incelemesi, editör 200
(`/p/present-continuous-d1/onizle.html?surum=d1`).
