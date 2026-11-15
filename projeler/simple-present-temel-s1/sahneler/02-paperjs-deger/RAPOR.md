# 02-paperjs-deger — RAPOR (15.11, istem D-S1, huni v2; render yok)

| Ölçüm | Değer |
|---|---|
| Motor | Paper.js · 1080×1920 · 30 fps · 361 kare · t_bas 3,00 · t_son 14,63 (`zaman.json` ile aynı) |
| `qa-yerel.sh … 3.05,8.80,14.55 8.80 --hazirla` | çıkış 0 (2 tur) |
| `cakisma-kapisi.mjs … --sahne 02-paperjs-deger --port 41333 --sunucu 41022` | çıkış 0 · "çakışma yok (48 örnek, 1985 kutu)" · "uyar" geçen satır 0 |
| Metin taraması (`tam[ ]ders\|dak[i]ka`, html/js/py) | boş (grep çıkış 1) |
| Kanal katmanı (3 açık + 1 koyu karede piksel ölçümü) | 4 / 4 karede yerinde, konum aynı |
| `node --check` (`.mjs` kopyası) | geçti |

## Yapım

| Adım | Kim | Çıktı |
|---|---|---|
| Kopya + kurulum | şef (`cp -p` + kısa Edit) | `kalem-paper.js` (yalnız 2 import yolu + baş yorum), `sayfa.html` (import yolu, 361 kare), `calistir.sh` (N 361, klasör, paket, `GLOBAL_SN`, taşıma dizini `~/Silinecekler/2026-11-15-huni-v2/simple-present-temel-s1`), `nesneler.json` (`[]`). Kaynak: `../../../02-04-ydt-temel-s1/sahneler/02-paperjs-ornek/` (RAPOR "huni v2" diyor → v2 taban) |
| Tasarım + spec | şef | `SPEC.md` (sabit tablosu, kare sabitleri, 26 olay, ölçekli kaplar §4, bekçiler §5) |
| `sahne-02.js` | agy-filo `tek --rol kod` (gemini-3.8-flash-high, 234 sn, 1 tur, başarılı) | 535 satır · özet `/home/sef/.claude/canavar/agy-filo/20261115-193236/ozet.md` |
| İnceleme | şef | dosya baştan sona okundu; SPEC'e uyuyor; 2 hata bulundu (aşağıda) |
| Şef Edit (inceleme) | şef | (1) `lerp` kalem-paper.js'ten dışa aktarılmıyor (yalnız `kis`, `yumus`, `cikis`) → modül bağlama hatası verirdi; `node --check` yakalamaz. `lerp` `S`'den alındı, kullanılmayan `cikis` importu kalktı. (2) 3 `svgCiz` çağrısında `await` yoktu → eklendi |
| Şef Edit (kare turu 1) | şef | `es` dairesi tireye değdi (13.11 QA kuralı). `DX_ES` tire + 12 → tire + 20, tire x `go` sonu + 6 → + 4, daire payı 12 → 10. SPEC aynı değerlerle güncellendi |

agy özetinin "değişen" listesindeki `.claude/docs/sozlesme.md`, `02-04-ydt-temel-s2|s3/…/08-hyperframes-kaydet/*` paralel oturumların
işidir (filo düzeyi git farkı). Bu koşuda agy yalnız `sahne-02.js` yazdı; sözleşme dosyası agy bitişinden sonra (19:37) değişti.

## Yerleşim (son durum, 14,55 karesi)

```
 505–582  Kardeşim gider:   (Caveat 72, x 60, soluk ikincil)
 620–859  ┌ My brother go-(es)          ┐  EN kart, Fredoka 72; goes alt çizgi (sarı) + es daire (sarı)
          └ to school by bus.   [otobüs]┘  otobüs 726–946 × 730–815
 900–965  ↓ = he                            ok kart sol payından iner (x ≈ 85–106)
1035–1122 he · she · it → goes
1185–1292 I · you · we · they → [go s̶]      go kartı 0,6 ölçek, x 720–945; s yuvası soluk + kırmızı çizgi
```

## Olay ↔ sözcük (yerel kare = round((t − 3,00) × 30); zaman `sozcukler.json`'dan `al()` ile)

| # | Olay | Kare | Sözcük (küresel sn) | Konum |
|---|---|---|---|---|
| 1–3 | `Kardeşim gider:` · kart `go` · küçük figür + otobüs (sahne 01'den hazır) | 0 | — | TR x 60 taban 560 · kart 62–438 × 620–819 · figür/otobüs x 700–956, y 460–600 |
| 4 | kart `goes` (kutu 8, yazı 12) | 8 / 12 | 1:4 goes (3,40) | 582–958 × 620–819, Fredoka 120 |
| 5 | kalem `?` | 24 | 1:5 mu? (3,80) | x ≈ 484–536, taban 760 |
| 6 | kanca satırı aşağı kayar (+260) | 36–46 | 1:5 sonu (4,20) | 880–1080 |
| 7 | EN kart kutusu | 46–60 | 2:0 My (4,67) | 62–958 × 620–859 |
| 8–9 | TR soluk Caveat'e döner · figür + küçük otobüs solar | 50–60 / 50–62 | 2:0 My | |
| 10 | büyük otobüs kalemle | 50–96 | 2:0 My → 2:6 bus. (6,19) | 726–946 × 730–815 (ayna, sola gider) |
| 11, 14 | EN cümle + karaoke | 50–96 | 2:0–6 (4,67–6,19) | taban 712 / 804, x 110 |
| 12–13 | `goes` kartı uçar, cümledeki *goes* olur | 61–70 | 2:2 goes (5,23) | `goX` ≈ 496, ölçek 120 → 72 |
| 15 | `goes` sarı alt çizgi (kalıcı) | 72 | 2:2 | y ≈ 734 |
| 16 | kart `go` soluk (0,4), sağ kenarda bekler | 70–82 | 2:2 | 729–955 × 889–1009 |
| 5′ | `?` söner | 61–69 | 2:2 | |
| 17–18 | `My brother` → ok · Caveat `= he` | 122 / 126 | 2:7 He, (7,08) | `= he` x 118, taban 950 |
| 19 | satır A `he` · `she` · `it` | 122 / 139 / 154 | 2:7–9 (7,08–8,12) | taban 1100, x 84 |
| 20–21 | `goes` → `go-es`, `es` sarı daire | 188–194 / 196 | 2:12 s (9,25) | daire x ≈ 610–706 |
| 22 | satır A ok + `goes` | 197 / 203 | 2:13 gelir. (9,57) | ok 443–507, goes 527–678 |
| 23 | satır B `I` · `you` · `we` · `they` | 229 / 253 / 274 / 296 | 2:14–17 (10,62–12,86) | taban 1250 |
| 24–25 | `go` kartı satır B yanına döner (alfa 1) · satır B oku | 318–328 | 2:19 gelmez. (13,59) | kart 720–945 × 1172–1292 |
| 26 | `s` yuvası (soluk) + kırmızı kalem çizgisi | 328 / 331 | 2:19 | kart içinde, `go`'nun sağında |

Sarı belirteç: karaoke (geçici) + `goes` alt çizgisi + `es` dairesi. Kırmızı yalnız #26. Yeşil yok. İçerik yazısı en küçük 72 px.

## Kapı (tur 2, son satırlar)

```
== HAZIRLA
tema: acik
önizleme hazır
== KAPI
02-paperjs-deger | çakışma yok (48 örnek, 1985 kutu)
== KARE (açık)
"png":"/home/sef/qa-kare/simple-present-temel-s1/02-paperjs-deger/02-paperjs-deger-3.05.png"
"png":"/home/sef/qa-kare/simple-present-temel-s1/02-paperjs-deger/02-paperjs-deger-8.8.png"
"png":"/home/sef/qa-kare/simple-present-temel-s1/02-paperjs-deger/02-paperjs-deger-14.55.png"
== KARE (koyu)
"png":"/home/sef/qa-kare/simple-present-temel-s1/02-paperjs-deger/koyu/02-paperjs-deger-8.8.png"
kapı çıkış kodu: 0
```

## Kanal katmanı ve bantlar (karede ölçüm; eşik: x 0–40 satır medyanından sapma)

| Kare | 0–280 | Kanal (280–352) | Künye (352–455) | İçerik (455–1395) | Altyazı | 1565–1920 | x 961–1080 |
|---|---|---|---|---|---|---|---|
| 3,05 açık | boş | x 61–598, y 296–339 | x 60–509, y 386–433 | x 62–956, y 459–818 | x 151–871, y 1449–1494 | boş | boş |
| 8,80 açık | boş | x 61–598, y 296–339 | x 60–509, y 386–433 | x 62–957, y 512–1101 | x 366–654 | boş | boş |
| 14,55 açık | boş | x 61–598, y 296–339 | x 60–509, y 386–433 | x 62–957, y 512–1290 | x 398–622 | boş | boş |
| 8,80 koyu | boş | x 61–598, y 296–339 | x 60–510, y 386–433 | x 62–957, y 512–1101 | x 366–654 | boş | boş |

Kanal: logo görünür sol kenar 61 (SVG iç boşluğu), `@ydspublishing` sağ ucu 598, taban 330 (kuyruk 339) — emsal 02-04-s1 ölçümüyle aynı.

## Bakılan kareler (Read ile)

| Kare | Bulgu |
|---|---|
| `k/02-paperjs-deger-3.05.png` | kare 0 durumu: `Kardeşim gider:` (mürekkep), kart `go`, sağ üstte küçük figür + otobüs; altyazı 1 satır; taşma yok |
| `k/02-paperjs-deger-8.8.png` | EN kart + otobüs, soluk TR üstte, `goes` sarı alt çizgili, ok + `= he`, satır A, `go` kartı soluk sağda; üst üste binme yok |
| `k/02-paperjs-deger-14.55.png` | son durum: iki satır + EN kart + soluk TR; `go-es` dairesi tireye değmiyor (tur 1'de değiyordu, düzeltildi); kırmızı çizgi `s` yuvasında |
| `k/koyu/02-paperjs-deger-8.8.png` | koyu tema: krem yazı, soluk `go` kartı gri, turuncu vurgu; okunur |
| ek (`/tmp/olc-0202/ara/`: 4,40 · 5,20 · 5,32 · 5,60 · 9,50 · 13,68) | kayma, uçuş, iniş, bekleme, `go-es` ayrılması, dönüş; uçuşta (61–70) `goes` kartı otobüsün ve 2. satırın üstünden 9 kare geçer (hareket, kabul) |

## Açık noktalar

1. **Sahne 01 eşleşmesi:** sahne 01 henüz yok. Kare 0 sabitleri D-01 istemiyle ortak: `Kardeşim gider:` Caveat 72, x 60, taban 560 · kart
   `go` x 60–440, y 620–820 (el çizimi kutu `ikincil`, Fredoka 120, orta x 250, taban 750) · figür kutu [700, 460, 60, 140] · küçük otobüs
   kutu [770, 530, 190, 70], `ayna` (SVG doğal yönü sağa). Sahne 01 bu değerlerden saparsa sahne 02 sabitleri güncellenmeli.
2. **Kanca satırı kayması (4,20–4,53, +260 px):** istemde yok; EN kartın kanca kartlarıyla çakışmadan TR satırının hemen altına
   yazılması için eklendi (köprü çifti bitişik). Şef/Nadir isterse kaldırılabilir (o zaman EN kart 860 altına iner, son durumda 600–850 boş kalır).
3. **`?` söner (5,03–5,30):** istem `?` için son durum vermiyor; soru cevaplanınca söner. "Hiçbir öğe kaybolmaz" son durum öğeleri için uygulandı.
4. **Kapı ölçek kapları:** `go`/`goes` kartları ölçekli kapta (`data` kart); çakışma kapısı kart kuralıyla bunları uçuşta saymaz.
   Kart içi yazılar (`go`, `s` yuvası) kapıya ayrı kutu olarak girmez; denetim karede gözle yapıldı.
5. **`go` kartı `s` yuvasıyla:** `go` + soluk `s` kart içinde sağa kayık (sol pay ≈ 70, sağ ≈ 33 px); sabit, okunur.
6. Birleştirme ve mp4 yapılmadı (istem; standart §1 kural 9).
