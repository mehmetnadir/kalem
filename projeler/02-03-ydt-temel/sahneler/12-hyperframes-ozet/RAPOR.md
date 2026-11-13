# Sahne 12 · ara özet (HyperFrames, 487 kare, 226,45–242,28 sn; cümle 15)

Durum: P2 yazıldı, `ONIZLE_YALNIZ=1` hazırlığı koşuldu (koyu, sonra açık; son koşu AÇIK). Render yok. Kapı ve `sahne-kare` koşulmadı (şef EK); `k/` boş.
Tema: acik.

## İçerik
`ozet` 3 madde, sahne 07 ile aynı görsel dil (kalemle bant, sarı belirteç, kalem oku, soluk küçük kart), kademeli:
1. `NOW · THESE DAYS / NOWADAYS` → `usually -ing` + `(temporary, changing)`
2. `USUALLY / GENERAL` → `V1`
3. `believe, have:` `no -ing`
Her madde sağdaki küçük karta okla bağlanır; söylenince kart çerçevesi sarıya döner (1: kural kartı sinyalleri, 2: USUALLY · GENERAL, 3: TRAP kartı + `believe` sarı daire). Bölüm perdesi yok; sonda ince geçiş çizgisi (241,84 sn). Künye: sağ üst `Recap`, ajanda etkin yok (özet ajandada değil). Hareket 0,55–15,77 sn (ilk/son 12 kare durgun; `Y.kontrol` geçti).

## Olay ↔ sözcük (cümle 15; küresel sn)
| Olay | Sözcük (i) | Sözcük t0 | Olay sn | Sapma |
|---|---|---|---|---|
| bantlar + küçük kartlar çizilir | Özet. (0) | 227,00 | 227,00–227,65 | 0,00 |
| madde 1 oku→kart + `NOW` + belirteç | Now, (1) | 228,04 | 228,04 / 228,14 | 0,00 / 0,10 |
| `· THESE DAYS` + belirteç | these (2) | 228,68 | 228,68 / 228,78 | 0,00 / 0,10 |
| `/ NOWADAYS` + belirteç | nowadays (5) | 229,96 | 229,96 / 230,06 | 0,00 / 0,10 |
| ok + `usually -ing` | şimdiki (6) | 231,00 | 231,00 / 231,14 | 0,00 / 0,14 |
| `(temporary,` | geçici (9) | 232,60 | 232,60 | 0,00 |
| `changing)` | değişen (12) | 233,40 | 233,40 | 0,00 |
| madde 2 `USUALLY` + belirteç | Usually (14) | 234,68 | 234,68 / 234,78 | 0,00 / 0,10 |
| `/ GENERAL` + belirteç | genel (16) | 235,80 | 235,80 / 235,90 | 0,00 / 0,10 |
| ok + `V1` | geniş (18) | 236,76 | 236,76 / 236,90 | 0,00 / 0,14 |
| madde 3 `believe,` + kart oku | Believe (20) | 237,88 | 237,88 | 0,00 |
| `have:` | have (22) | 239,08 | 239,08 | 0,00 |
| `no -ing` | -ing (28) | 241,32 | 241,32 | 0,00 |
| geçiş çizgisi | yok. (29) | 241,84 | 241,84–242,22 | 0,00 |

## Kapı
Koşulmadı (EK). Yerinde kontroller: madde sağ uçları bant içinde (assert; bant sağ kenarı 1156) · kart yazıları kart içinde (assert) · yazı tabanı ≥ 30 px (kart 30, madde 48, not 40) · `node --check` JS tamam.

## Açık notlar
- Karttaki ok glifi yok (Fredoka `→` taşımıyor): oklar çizim. Küçük kartlarda yalnız sinyal / TRAP cümlesi gösterilir.
- Taslak ekranındaki `(temporary, changing)` parantezi BRIEF'te yok, taslakta var: taslağı izledim.

Dosyalar: `uret.py`, `olay.py`, `calistir.sh`, `yardim.py`, `proje/index.html`, `olaylar.json`.
Kare yolları: yok (EK).

## QA 13.11
- Kapı: HyperFrames, ölçülmez. Kareler `k/12-hyperframes-ozet-{227,232,237,242}.png`, koyu `k/koyu/`.
- Göz: sol üç özet kartı ve sağ üç küçük kart oklarla bağlı. Sağ alttaki TRAP mini kartında believe halkası We ve this'e değiyor (küçük yazı); okunur, düzeltilmedi. Kalan sorun: sol alt boş çizgi (özet sonunda dolmuyorsa amaçsız olabilir).
- QA 13.11 ek: TRAP mini kartındaki believe halkası el altçizgisine çevrildi; sol alttaki çizgi geçiş çizgisi, `yok.` sözcüğünde 140→1750 px tam çiziliyor (`k/12-hyperframes-ozet-242.2.png`), amaçlı, kaldırılmadı. Önceki "kalan sorun" notu geçersiz.
- zaman eşitleme 13.11: yeniden kuruldu (t_bas 224,85, kare 477); kareler `k/12-hyperframes-ozet-{226.8,228.8,233.4,236.5,240.2}.png`. Sözcük-işaret uyumu uret.py'de sözcük t0'ından.
