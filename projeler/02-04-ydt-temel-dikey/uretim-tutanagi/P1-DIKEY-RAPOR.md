# P1-dikey raporu — 02-04-ydt-temel-dikey · 15.11.2026

| Alan | Durum |
|---|---|
| İskelet | tamam (simple-present-temel-dikey yapısı) |
| zaman.json | 14 sahne, yatayla aynı t_bas/t_son/kare/gecis; 1080×1920 |
| BRIEF-DIKEY.md | §0 bulgular · §1 teknik · §2 bantlar/HUD/ortak kurallar · §3 14 satır · §4 kabul |
| Sahne istemi | 14 (`istem/sahne/D-<klasör>.md`), yer tutucu kalmadı |
| Ses / render / sahne kodu / commit | YOK (istem gereği) |
| Motor değişikliği | YOK |

## Yazılan dosyalar

| Dosya | Nasıl |
|---|---|
| `ortak/anlatim` → `../../02-04-ydt-temel/ortak/anlatim` | sembolik bağ (aynı ses) |
| `ortak/{cizim,font,hf_tema.py,logo}` → `../../present-continuous/ortak/…` | sembolik bağ (simple-present-temel-dikey ile aynı hedef) |
| `ortak/kalem-canvas.js`, `ortak/tema.sh`, `ortak/tema_damga.py` | simple-present-temel-dikey kopyası, değişiklik yok (proje yolu taşımıyorlar) |
| `ortak/kunye.js` | simple-present-temel-dikey kopyası (dikey v2) + 02-04 uyarlaması, aşağıda |
| `gorevler.json` `[]` · `yorumlar.json` `[]` · `harita-konum.json` `{}` | simple-present-temel-dikey anlamıyla boş; eski içerik yok |
| `surumler.json` | present-continuous-dikey biçimi; `video` bloğu yatay 02-04'ten; tek sürüm `dikey-tam`; `revizyonlar: []` |
| `zaman.json` | yatay kopyası; yalnız `genislik` 1080, `yukseklik` 1920 (sahneler dizisi birebir eşit, ölçüldü) |
| `BRIEF-DIKEY.md` | şef |
| `uretim-tutanagi/istem/D-dikey-sablon.md` | `~/is/uretim-0204/D-dikey-sablon.md` kopyası |
| `uretim-tutanagi/istem/sahne/D-*.md` × 14 | şablon + BRIEF §3 satırı (tek kaynak: BRIEF tablosundan üretildi) |
| `uretim-tutanagi/SPEC-altyazi-dilim.md` | `altyaziDilimle` tasarımı (agy'ye verildi) |
| `sahneler/` | boş dizin; sahne dizinlerini sahne istemleri açar |

## kunye.js uyarlaması

| Değişiklik | Sebep | Kanıt |
|---|---|---|
| `KOK` → `/projeler/02-04-ydt-temel-dikey/ortak` | paket yolu | — |
| `ders` 2 satır: `SIMPLE PRESENT vs` / `PRESENT CONTINUOUS` (`dersSatir` 64), rozet 2. satırın sağında (`rozetY` 216, `rozetAra` 24, `dersDuzen()`) | tek satır 56 px'te 1119 px; 984 px'e sığmaz, 56 px kuralı küçültmeye izin vermez | başsız tarayıcı kutuları: logo 48,48,387,96 · ders 48,156,596,126 · rozet 668,216,281,72 · çip 684,48,348,80; iki temada kare bakıldı, çakışma yok |
| `KUNYE.cipler` (14 sahne → çip) + `KUNYE.ajanda` (yatay liste) | dikey HUD ajanda çizmez; çip sahnenin kendi bölümünü yazar (yatay 06/08/09 ajanda açığı) | çip metinleri yatay sahne kodundan |
| `altyaziDilimle()` + `kunyeHazirla` sözcük zamanını okur | 13 altyazı parçası 2 satıra sığmaz (en uzun 226 karakter); eski kod 3. satırı taşırıp sözcük sırasını bozuyordu | önce: cümle 8 karesinde taşma + karışık sıra; sonra: 47 parça → 64 dilim, t 105 / 120 / 128,5 karelerinde 2 satır, bant içinde |

`altyaziDilimle` 15+ satır: yazma kapısı şefe kapattı → `agy-filo tek --rol kod` (gemini-3.8-flash-high, 198 sn, başarılı),
özet `/home/sef/.claude/canavar/agy-filo/20261115-113703/ozet.md`. Şef işlevi baştan sona okudu: spec'e uyar. `node --check` geçti.
Özetin "değişen" listesindeki `02-04-ydt-temel-s1/uretim-tutanagi/juri/*` dosyaları paralel S1 oturumunundur; bu iş yazmadı.

## Sahne planı özeti

| No | Klasör | Motor | Küresel sn | Dikey ana fikir |
|---|---|---|---|---|
| 1 | 01-hyperframes-giris | HyperFrames | 0,00–3,00 | soğuk açılış, 3 Türkçe satır 128 px, *yor* kutusu; ders adı yok |
| 2 | 02-paperjs-kanca | Paper.js | 3,00–20,22 | TR satırlar şeride; iki tek satır kart; etiketler HUD'un iki ders satırına uçar; MEANING |
| 3 | 03-paperjs-ornek1 | Paper.js | 20,22–43,85 | kart A + mont → şerit; kart B + tişört; GENERAL / RIGHT NOW |
| 4 | 04-canvas-ornek2 | Düz canvas | 43,85–68,84 | `live` + kart A + ev + uzun bant → şerit; kart B + bavul + kısa bant |
| 5 | 05-canvas-ornek3 | Düz canvas | 68,84–93,35 | sabit alt zaman çizgisi; tren/saat → şerit; bilet; TIMETABLE / ARRANGEMENT |
| 6 | 06-hyperframes-soru1 | HyperFrames | 93,35–113,37 | soru balonu; iki cevap satırı (figür → am going, tren → leaves) |
| 7 | 07-hyperframes-kural | HyperFrames | 113,37–130,40 | 3 çift satır söylenince; ad satırı; MEANING FIRST |
| 8 | 08-canvas-karsit1 | Düz canvas | 130,40–145,29 | today kartı + büyük zaman çizgisi; 08–09 ortak ölçüler |
| 9 | 09-canvas-karsit2 | Düz canvas | 145,29–162,33 | 08 kartı şeride; tren kartı; 7 pm; RIGHT NOW ≠ TIMETABLE |
| 10 | 10-hyperframes-tuzak | HyperFrames | 162,33–183,79 | TRAP kartı ortada → yukarı; soru balonu 2 |
| 11 | 11-canvas-tuzak-cevap | Düz canvas | 183,79–205,30 | iki tek satır kart + iki zaman çizgisi; ≠ meaning |
| 12 | 12-hyperframes-ozet | HyperFrames | 205,30–220,33 | 3 madde bloğu söylenince; MEANING FIRST |
| 13 | 13-hyperframes-mini-soru | HyperFrames | 220,33–251,27 | kök kartı, 5 şık, öğrenci balonu, doğru B vurgu dolgusu |
| 14 | 14-hyperframes-kapanis | HyperFrames | 251,27–264,64 | MEANING FIRST, 3 soru, sonraki ders kartı |

Dağılım: HyperFrames 7 · Paper.js 2 · düz canvas 5 (yatayla aynı). `{ORNEK}`: present-continuous-dikey (tek kaynak paket,
durum `hazir`); HF giriş → `01-hyperframes-giris`, öteki HF → `06-hyperframes-form` (balon + tablo), Paper → 02/03,
canvas → 04 (04, 08, 11) ve 05 (05, 09).

## Doğrulama

```
zaman.json            → 1080 1920 14
istem/sahne | wc -l   → 14
readlink ortak/anlatim → ../../02-04-ydt-temel/ortak/anlatim
node --check kunye.js → çıkış 0
```

## Açık noktalar

1. **Ders adı 2 satır** şef kararıdır (56 px kuralı + 984 px). Nadir tek satır isterse tek yol 48 px (959 px), kural dışı.
2. **Altyazı dilimi** açgözlüdür; cümle ortasından da keser (ör. `… Tarife ya da` / `program varsa …`). Cümle sınırı önceliği
   istenirse `altyaziDilimle` tek yerde değişir. HyperFrames sahneleri aynı kuralı Python'da ayrıca uygular (iki uygulama).
3. **"En çok 1 örnek kart"** şöyle uygulandı: çok satırlı kart + büyük çizimde ekranda 1 kart, öncekisi üst şeride küçülür.
   02 ve 11'deki tek satırlık karşıt çift iki kart üst üste (BRIEF §2.5 istisna). Uymazsa 02/11 satırı değişir.
4. **07 kural tablosu** 2 hücreli satırlar kullanır; anlatım "soldakiler / sağdakiler" der. Sayfa düzeni tek sütundur.
5. **Şablon çelişkisi:** istem şablonu "doğru şık yeşil" der; yatay BRIEF ve 13.11 QA "ham yeşil yok" der. §3 satır 13 bunu açıkça yazar.
6. **14 çipi** `Next lesson`, kart başlığıyla aynı (yatay 14 açık noktası 5). Yatayla tutarlı bırakıldı.
7. **Nesne boyu:** 04 bavul, 05 bilet, 03 tişört 400–420 px sınırında; sahne ajanı ölçer, gerekirse kart satırını sıkıştırır.
8. **surumler.json** `senaryo: null`, `tarih` yatay kaydıyla aynı (`02-04-ydt-temel/surumler.json` `dikey-tam`); present-continuous-dikey
   `METIN.md` yazıyordu. Editörde kaynak gerekirse tek alan değişir.
9. Sözleşme (`K/.claude/docs/sozlesme.md`) güncellenmedi: yazma kapsamı paketle sınırlı. Eklenmeye değer: dikey 02-04 künye
   (2 satır ders, çip haritası), altyazı dilimi.
10. Paket git'te izlenmiyor (yeni dizin); commit yok.
