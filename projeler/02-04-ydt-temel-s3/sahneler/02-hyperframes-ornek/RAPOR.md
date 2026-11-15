# RAPOR — 02-04-ydt-temel-s3 · sahne 02-hyperframes-ornek (HyperFrames, DİKEY 1080×1920) · 15.11.2026

| Alan | Durum |
|---|---|
| Kapı (`qa-yerel.sh … 6.6,10.9,15.9 13.5 --hazirla`) | **çıkış 0** — `02-hyperframes-ornek \| çakışma yok (53 örnek, 30467 kutu)` |
| `uret.py` / `olay.py` | çıkış 0; `Y.kontrol` geçti (hareket 0,40–12,49 yerel); 86 komut, 34 ses olayı (18 cizgi) |
| Kare 0 = sahne 01 son karesi | kart 1 çerçevesi `kc0…kc3` yol verisi birebir aynı; satırlar 97 / 468, 566; `pm` x 428,8 ve `today.` x 529,1 (01 `devir.json`: 428,84 / 529,13); tren `translate(790 404) scale(0.5)` ilk yolu birebir; `font-kerning:none` 01 ile aynı. Tek fark çip (`Hook` → `Example`, sahne gereği) |
| Render | YOK (`ONIZLE_YALNIZ=1`; istem gereği) |
| Kod yolu | şef `SPEC.md` → `agy-filo tek --rol kod` (`uret.py`) → şef okudu + 4 küçük Edit |

## 1. Dosyalar

| Dosya | Kaynak |
|---|---|
| `calistir.sh` | 02-04-ydt-temel-dikey sahne 06 kopyası; `KARE=402` + açıklama (Edit). Homebrew PATH koşullu, `Y=$(yuk1)`, `ONIZLE_YALNIZ` satırı kalıpta |
| `yardim.py` | 02-04-ydt-temel-dikey sahne 06 birebir kopyası (sha256 b0fec691…) |
| `olay.py` | aynı kalıp; yalnız açıklama satırı |
| `uret.py` | agy (SPEC.md) + şef düzeltmeleri (§4) |
| `cizim/ogretmen.json` | S1 sahne 01 kopyası (sha256 5e508402…; `kadro.ogretmen`, K22); `cizim/KAYNAK.md` |
| `nesneler.json` | `[]` (S1 biçimi) |

## 2. Olay listesi (yerel = küresel − 3,00; çapa `sozcukler.json`)

| Yerel | Küresel çapa | Olay |
|---|---|---|
| 0 | — | Kare 0: kart 1 (`The train to İzmir` / `leaves at 7`), tren köşede, künye, altyazı dilimi 0 |
| 0,40 · 0,52 | `p.m.` 3,00 · `today.` 3,40 | `pm`, `today.` (ilk 12 kare geçiş altında; `pm` 0,40'a kayar) |
| 0,52–1,45 | `today.` | zaman çizgisi: eksen + ok, now noktası + `now`, `7 pm` çentiği + `7 pm`, now → `7 pm` kalem oku, `7 pm` sarı daire (`isaret`), `gelecek · V-s` |
| 1,15–2,93 | `I` 4,45 … `tonight.` 5,93 | kart 2 çerçevesi; `I am going to the` / `movie theater tonight.` sözcük sözcük; bilet `movie` 5,29'da |
| 2,93–3,40 | `tonight.` 5,93 | `tonight` noktası + `tonight` + `gelecek · am + V-ing` |
| 3,50 · 3,58 | `Hocam,` − 0,50 / − 0,42 | zaman çizgisi söner; kart 2 −124 px yukarı (kartlar üstte toplanır) |
| 3,90–7,33 | `Hocam,` 7,00 … `yok?` 10,33 | öğrenci başı (`ogrenci-bas.svg`), balon, soru sözcük sözcük (Fredoka 600 64, 3 satır) |
| 6,72 · 6,86 | `Neden` 9,72 | sarı nokta balon üstünde → sarı bağ kart 1 `leaves` altına |
| 7,76–8,51 | 10,76–11,51 | DURAKLAMA (olay yok) |
| 8,51 | `Planı` 11,51 | balon + baş söner; öğretmen (react-peeps `ShirtPantsWB/Short/Smile`) kalemle 8,55–9,05 |
| 9,07 · 9,47 | `bir` 12,07 | sarı ok öğretmenin elinden `am going` sütununa (kart 2 altı); `am going` sarı altçizgi |
| 9,31 · 9,51 | `kişi` · `yapar.` | `person` → (kalem oku) `plan` |
| 10,43 | `Tren` 13,43 | önceki sarılar griye döner; sarı bağ trenden `leaves` altına |
| 10,53 · 10,83 | `Tren` · `tarifeye` 13,83 | kart 1 altında `train` → `timetable` |
| 12,19 | `geniş` 15,19 | tren bağı griye döner; `leaves` sarı altçizgi (odak). Son durgun 12,49–13,40 |

Aynı anda tek sarı öğe kümesi: `7 pm` dairesi (1,10–3,75) → bağ `cn` (6,72–8,86) → ok + `am going` (9,07–10,68) → tren bağı (10,43–12,44) → `leaves` (12,19–).

## 3. Kapı sonucu (son satırlar)

```
== KAPI
02-hyperframes-ornek | çakışma yok (53 örnek, 30467 kutu)
== KARE (açık) 6.6 · 10.9 · 15.9      == KARE (koyu) 13.5
kapı çıkış kodu: 0
```

## 4. Bakılan kareler ve bulgu

| Kare | Bulgu | Sonuç |
|---|---|---|
| `k/kare0/02-hyperframes-ornek-3.png` ↔ `../01-hyperframes-kapak/k/01-hyperframes-kapak-2.95.png` | ilk koşuda kare 0'da altyazı yoktu: GSAP `seek(0)` 0. sn `set`'ini uygulamıyor | DÜZELTİLDİ: 0'da açık dilim baştan görünür yazılır; yeniden yakalandı, eşit |
| `k/koyu/…-13.5.png` | ilk koşuda tren bağının ok ucu gövdeden önce `leaves` altında belirdi: Chrome kesik deseni her alt yolda (M) baştan başlar | DÜZELTİLDİ: oklar tek kontur (`ok_tek`, `ok1`, `tok`); 4,0 · 9,95 · 12,2 · 13,5 karelerinde ok ucu gövdeyle geliyor |
| `k/…-6.6.png` | iki kart + zaman çizgisi; etiketler arası ≥ 40 px; taşma, kesik yazı yok | geçti |
| `k/…-10.9.png` (duraklama) | balon kart sütununun altında, sarı bağ `tonight.`'ın 16 px sağından geçer; 1536 altı boş | geçti |
| `k/…-15.9.png` | son düzen: `leaves` sarı, griler, iki etiket, öğretmen; altyazı bantta | geçti |
| `k/koyu/…-13.5.png` | koyu temada kontrast okunur; sarı geçiş anında (10,43–10,68) eski sarı söner, yeni bağ çizilir | geçti |
| kabul 3 (index.html) | `Izmir`, `seven`, `p.m.`, `→` 0; `#ffe066` / `#1b2440` yalnız `hf_tema` CSS'inde | geçti |

Şef düzeltmeleri (uret.py): `krm` y 862 → 867 (sözleşme: `g` kuyruklu sözcükte taban + 0,48 × boy) · `ok_tek` tek konturlu ok ·
`#icerik text{font-kerning:none}` (sahne 01 ve ölçümle aynı) · 0'da açık altyazı dilimi.

## 5. agy koşu özeti

`/home/sef/.claude/canavar/agy-filo/20261115-130026/ozet.md` — rol kod, gemini-3.8-flash-high, başarılı, 402 sn; girdi 2.664.606 / çıktı 192.617 token.
Özetteki "değişen" listesi bütün çalışma ağacını tarar (paralel oturumların dosyaları); agy yalnız `uret.py`'yi yazdı (mtime 13:06).

## 6. Açık noktalar

1. "Kartlar üstte küçülür" ölçekle yapılmadı: kart yazısı 64 px tabanın altına inerdi (BRIEF-DIKEY §0). Zaman çizgisi söner, kart 2 −124 px kayar.
2. Karaoke: alt bantta düz altyazı (Lexend 44); okunan sözcük vurgusu kartta sözcük sözcük yazımla verilir. Sarı karaoke altçizgisi
   eklenmedi (aynı anda tek sarı kuralı, `7 pm` dairesiyle çakışırdı). Nadir sarı altçizgi isterse `7 pm` dairesi 4,45'te söner.
3. Öğretmen figüründe işaret eden kol yok (kit pozu bileti tutan el); işaret, elden çıkan sarı kalem okuyla verilir (sözleşme satır 42 kalıbı).
4. Teacher oku `am going` sözcüğüne değil, kart 2'nin altına (sözcüğün sütununa) iner; kart içinde satırlar arası şerit yok (aralık 98).
   Sözcüğü `am going` sarı altçizgisi işaretler (ana ders sahne 06 kalıbı).
5. Faz C'de sağ alt (x 650–1032, y 1100–1390) boş kalır; içerik bandı dikeyde 368–1390 kullanılır.
6. `ses` olayları (34) `olaylar.json`'da; efekt sesi birleştirmede (`birlestir.py --efekt`) — bu turda koşulmadı.
