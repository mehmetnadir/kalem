# SPEC — sahne 05 hikâye karesi A (kural kartı), huni v2 · simple-present-temel-s1 · 15.11.2026

Durağan kare: HyperFrames DİKEY 1080×1920, tek kare, ses yok, altyazı yok, çip yok; zaman çizelgesi dışı (`zaman.json → hikaye`).
Bağlayıcı: `D/.claude/docs/huni-v2-standart.md` §1–§2, §6; paket `BRIEF-S1.md` "Kanal katmanı" + "Hikâye kareleri";
`uretim-tutanagi/hikaye-taslak.md` §3–§4.

## 1. Yazılacak dosya (agy)

| Dosya | Durum |
|---|---|
| `/home/sef/01dev/_worktrees/kalem-0204/projeler/simple-present-temel-s1/sahneler/05-hyperframes-hikaye-a/uret.py` | YENİ (agy yazar; başka dosyaya dokunma) |
| `…/05-hyperframes-hikaye-a/yardim.py` | VAR (aynı paket `03-hyperframes-kaydet/yardim.py` v2 kopyası; DEĞİŞTİRME) |
| `…/05-hyperframes-hikaye-a/calistir.sh`, `olay.py`, `zamanlar.json` | VAR (emsal kopyası; DEĞİŞTİRME) |

`uret.py` çıktısı (çalışınca): `proje/index.html`, `proje/assets/fonts/*` (Y.font_kopyala), `nesneler.json`.

## 2. Emsal kod (kalıp buradan)

| Emsal | Mutlak yol | Alınacak kalıp |
|---|---|---|
| E1 | `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s1/sahneler/04-hyperframes-hikaye/uret.py` | Dosyanın iskeleti birebir: başlık, `zaman.json`/`zamanlar.json` okuma ve assert'leri (satır 18–28; `hikaye.klasor == AD.name`), `kaydet_svg()` (satır 144–158), `blok_kutulari` / `kesisim` / `kurallari_dogrula` deseni (satır 161–270), `uret()` HTML şablonu (satır 285–313: font_css, ZEMIN_CSS, `#root` data-*, zemin_html, `<svg id="sahne">`, paused GSAP timeline 0 ve `Z['sure']`), `__main__` (satır 319–339: font kopyala, index.html yaz, nesneler.json yaz). `ek_svg`, `kart_svg`, `ozet_svg`, `BAVUL` ALINMAZ. |
| E2 | `/home/sef/01dev/_worktrees/kalem-0204/projeler/simple-present-temel-s1/sahneler/01-hyperframes-kanca/yardim.py` satır 148–244 | coco yükleyicisi: `_coco_alt_yollar`, `_donusum`, `coco` işlevlerini **birebir** `uret.py` içine kopyala (bölüm başlığı `# ---- coco (Inkscape) SVG: kalem darbesi yolları (01-kanca yardim.py kopyası) ----`). Tek değişiklik: `ORTAK` yerine `Y.ORTAK`. `re` ve `math` import et. |
| E3 | `/home/sef/01dev/_worktrees/kalem-0204/projeler/simple-present-temel-s1/sahneler/01-hyperframes-kanca/SPEC.md` satır 138 | otobüs grubu: `<g id="otobus" transform="translate(2·cx 0) scale(-1 1)">` (ön yüz sola), her yol `fill="none"` stroke murekkep, round cap/join |

Renkler yalnız `Y.RENK` değerleriyle yazılır (koyu palet hex'i; `ortak/hf_tema.py` açık temaya çevirir): metin `R["murekkep"]`,
soluk `R["ikincil"]`, hap dolgusu `R["vurgu"]` (rect), hap yazısı `R["zemin"]` (text → `pilMetin`). Başka hex YAZMA. Yeşil ve kırmızı YOK.

## 3. Olay listesi (tek kare)

| Olay | Kare / sn | Cümle sözcüğü |
|---|---|---|
| bütün öğeler görünür (aşağıdaki 7 blok) | kare 0 (yakalama 0,5 sn; çizelge 1,0 sn) | — (anlatım yok; kural özeti BRIEF-S1 girişi) |

Animasyon yok. Zaman çizelgesi E1 ile aynı (`tl.set` 0 ve `Z['sure']`).

## 4. Yerleşim (px; tek sütun, x 60'tan sola hizalı)

| Blok (`ad`) | id | y bandı | İçerik ve ölçü |
|---|---|---|---|
| `kanal` | `kanal` (Y.kunye_svg içinde) | 291–339 | E1 ile aynı kutu: x 53,2, w = 263 + genişlik(Lexend 700 `@ydspublishing` 42) − 53,2, h 48 |
| `kunye` | `kunye` | 386–434 | E1 ile aynı: x 60, w = rz_x + rz_w − 60 (`Y.rozet_konumlari()[0]`), h 48 |
| `ozet` | `ozet` > `ozet1`, `ozet2` | 470–650 | `He, she, it: s gelir;` taban 536 · `I, you, we, they: s yok.` taban 620; Fredoka 700 64, murekkep, x 60. Kutu: y = 536 − 0,75·64, alt = 620 + 0,25·64, w = iki satırın büyük genişliği |
| `satir1` | `satir1` > `s1-ozne`, `s1-ok`, `s1-go`, `s1-es`, `s1-cizgi` | 690–800 | taban 770, Fredoka 700 72, murekkep. `s1-ozne` `he · she · it` x 60 · `s1-ok` kalem oku x OK_X…OK_X+72 · `s1-go` `go` x FIIL_X · `s1-es` `es` x FIIL_X + genişlik(`go`) · `s1-cizgi` `es` altı kalın mürekkep alt çizgi: `<line>` y 786, x `es` başı + 2 → `es` sonu − 2, stroke murekkep 8, linecap round |
| `satir2` | `satir2` > `s2-ozne`, `s2-ok`, `s2-go`, `s2-yuva` | 820–930 | taban 900, Fredoka 700 72, murekkep. `s2-ozne` `I · you · we · they` x 60 · `s2-ok` x OK_X · `s2-go` `go` x FIIL_X · `s2-yuva` soluk boş yuva: `<rect>` x = FIIL_X + genişlik(`go`), y 846, w = genişlik(`es` 72), h 60, rx 12, fill none, stroke `R["ikincil"]` 4, `stroke-dasharray="10 8"` (satır 1'deki `es`'in tam altında) |
| `ornek` | `ornek` > `ornek-yazi`, `otobus` | 950–1030 | `My brother = he` Caveat 700 64, `R["ikincil"]`, x 60, taban 1008 · otobüs `BUS = coco("bus", BUS_KUTU)`, BUS_KUTU = [470, 956, 220, 70]; E3 aynası (cx = BUS_KUTU x + w/2 = 580); yollar stroke murekkep, stroke-width 2.6, fill none, linecap/linejoin round |
| `kaydet` | `kaydet` > `kaydet-imi`, `kaydet-hap`, `kaydet-yazi` | 1050–1140 | E1 `kaydet_svg()` aynısı, y +2: imi `translate(39 1046) scale(4)` · hap rect x 128, y 1050, w = genişlik(Fredoka 700 `Kaydet` 64) + 80, h 88, rx 44, fill `R["vurgu"]` · yazı taban 1116, ortalı, fill `R["zemin"]` |

Sabitler: `OK_X = 60 + genişlik(Fredoka 700 "I · you · we · they" 72) + 24` (yuvarla, ≈ 616); `FIIL_X = OK_X + 72 + 24` (≈ 712).
Böylece iki satırda ok ve fiil aynı sütundadır; satır 2'nin yuvası satır 1'in `es`'inin altına düşer.

Kalem oku (`s1-ok`, `s2-ok`; `→` glifi Fredoka'da YOK, metin olarak YAZMA): bir `<path>`, `fill="none"`, stroke murekkep 7,
linecap/linejoin round. y_orta = taban − 26. `d = "M OK_X y_orta L OK_X+72 y_orta M OK_X+52 y_orta−16 L OK_X+72 y_orta L OK_X+52 y_orta+16"`.

Blok kutuları (`blok_kutulari`, kesişim ve boşluk denetimi için):

| Blok | x | y | w | h |
|---|---|---|---|---|
| ozet | 60 | 536 − 48 = 488 | max genişlik | 620 + 16 − 488 = 148 |
| satir1 | 60 | 770 − 54 = 716 | FIIL_X + genişlik(`goes` 72) − 60 | 790 − 716 = 74 |
| satir2 | 60 | 846 | FIIL_X + genişlik(`go`) + genişlik(`es`) − 60 | 900 + 18 − 846 = 72 |
| ornek | 60 | 956 | BUS_KUTU x + w − 60 | 1030 − 956 = 74 |
| kaydet | 60 | 1050 | 128 + hap_w − 60 | 88 |

1150–1380 boş zemin (bağ çıkartması elle konur): bu bantta HİÇBİR öğe, kutu ya da çerçeve yok. 1400–1920 boş. 0–280 boş.

## 5. Ekran metni (satır ≤ 24 karakter)

`He, she, it: s gelir;` (21) · `I, you, we, they: s yok.` (24) · `he · she · it` + `goes` · `I · you · we · they` + `go` ·
`My brother = he` (15) · `Kaydet` (6). Künye ve kanal Y.kunye_svg()'den gelir (`Simple Present`, `YDT · BASIC`, `@ydspublishing`).
Yasak sözler kodda literal olarak bile YAZILMAZ (dış grep kapısı tarar; E1'in kural 8 notunu aynen koru).

## 6. Kurallar (`kurallari_dogrula` assert'leri)

1. İçerik blokları (ozet, satir1, satir2, ornek, kaydet): x ≥ 60, x + w ≤ 960, y ≥ 460, y + h ≤ 1140.
2. kanal ve kunye: y ≥ 280, y + h ≤ 450.
3. Bütün blok çiftlerinin kesişim alanı 0 (7 blok).
4. Dikey boşluk ≥ 16: kunye→ozet, ozet→satir1, satir1→satir2, satir2→ornek, ornek→kaydet.
5. Otobüs: `coco` yollarının bütün koordinatları BUS_KUTU içinde (aynadan sonra da: x' = 2·580 − x); en az 5 yol.
   Yazı ile otobüs arası: 60 + genişlik(Caveat 700 `My brother = he` 64) + 24 ≤ BUS_KUTU x.
6. Yazı boyları: içerik yazılarının hepsi ≥ 64 (64, 72, Caveat 64, hap 64).
7. Ekran satırları ≤ 24 karakter (§5 listesi; künye ve kanal hariç).
8. Yasak söz denetimi dış grep kapısında (E1 notu).
9. HTML'de `id="kanal"` ve `id="logoimg"` tam 1 kez. Şu id'ler var: `ozet1`, `ozet2`, `s1-es`, `s1-cizgi`, `s1-ok`, `s2-ok`,
   `s2-yuva`, `ornek-yazi`, `otobus`, `kaydet-imi`, `kaydet-hap`. Şunlar YOK: `ku-cip`, `cg1`, `hap-kutu`, `ust`, `alt`, `altyazi`.
10. Sarı (`R["vurgu"]`) yalnız `kaydet-hap` rect'inde ve künye rozetinde: HTML'de `R["vurgu"]` değeri tam 2 kez geçer.
11. HTML'de `→` karakteri YOK; `R["kirmizi"]` değeri YOK (uret.py'nin kendi HTML dizgesinde, tema öncesi).

## 7. Kabul ölçütü

- `/usr/bin/python3 uret.py` rc 0; çıktı `index.html yazıldı <n>`; `nesneler.json` 7 blok (kanal, kunye, ozet, satir1, satir2, ornek, kaydet).
- Tip ipucu bütün işlevlerde (`-> str`, `list[dict[str, float]]` …); girinti 4 boşluk (E1 ile aynı); satır ≤ 120 karakter.
- Şef koşturur: `ONIZLE_YALNIZ=1 bash calistir.sh`, sonra `calistir.sh --tema acik|koyu` → 1080×1920 PNG; kareye bakar.
- agy: test, render, git YOK; yalnız `uret.py` yazılır ve bir kez `/usr/bin/python3 uret.py` ile koşturulabilir.
