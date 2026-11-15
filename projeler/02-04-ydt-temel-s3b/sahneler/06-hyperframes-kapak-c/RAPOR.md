# RAPOR — 02-04-ydt-temel-s3 · sahne 06-hyperframes-kapak-c (kapak C, karşıt çift) · huni v2 · 15.11.2026

Tema: acik (önizleme `proje/index.html` açık temada bırakıldı; iki tema da yakalandı)

| Ölçüm | Değer |
|---|---|
| `calistir.sh --tema acik` | çıkış 0 · `P/kapak-c.png` PNG 1080×1920 (ffprobe) |
| `calistir.sh --tema koyu` | çıkış 0 · `k/koyu/kapak-c-koyu.png` PNG 1080×1920 (ffprobe) |
| `uret.py` | `index.html yazıldı 26124` · `S=170` · SPEC §6 assert'leri geçti |
| Çakışma kapısı | çıkış 2 · `HATA sahne bulunamadı: 06-hyperframes-kapak-c` (araç sınırı: yalnız `zaman.json` → `sahneler[]` okur; araç değiştirilmedi) |
| Metin taraması (`tam ders`, `dakika`, `proje/`) | boş (grep çıkış 1) |
| Kanal katmanı (piksel, iki kare) | logo mürekkebi x 60–239, y 298–330 (resim y 291–339) · `@ydspublishing` x 264/265–595, y 296–339 (taban 330); S1 kapak C v2 ölçümüyle aynı |
| Boş bölgeler (piksel kenar testi, eşik 40) | y 0–280: 0 · y 1400–1920: 0 · x 961–1080: 0 · x 0–59: 0 |
| İçerik (piksel) | x 62–960 (zemin çizgisi ucu 958 + 3 px test kayması), y 466–1338 |

Eski çıktılar: `~/Silinecekler/2026-11-15-huni-v2/02-04-ydt-temel-s3/kapak-c.png` · v1 sahne kodu `…/sahneler-v1/06-hyperframes-kapak-c/`.

## Öğe listesi (nesneler.json)
| Öğe | x · y · w · h | Yazı boyu |
|---|---|---|
| kanal (logo 193,5×48 + `@ydspublishing`) | 60 · 280 · 542 · 70 | Lexend 700 42 |
| rozet `YDT · BASIC` (kapak A konumu; konu adı yok) | 665 · 386 · 204 · 48 | Lexend 700 26 |
| baslik `İKİ ÖRNEK` / `İKİ ZAMAN` (kontur dahil) | 88 · 460 · 845 · 388 | Fredoka 700 170 |
| bk-kutu (`İKİ ZAMAN` sarı kutu) | 88 · 644 · 845 · 204 | — |
| kart-1 (el kutusu ±4) | 60 · 892 · 785 · 208 | — |
| ik-tren | 84 · 953 · 105 · 86 | — |
| m-1 `The train leaves …` | 209 · 968 · 609 · 72 | Fredoka 700 72 |
| hap-leaves (tek kart vurgusu) | 520 · 960 · 231 · 75 | — |
| kart-2 (el kutusu ±4) | 60 · 1128 · 785 · 208 | — |
| ik-bilet | 84 · 1212 · 105 · 41 | — |
| m-2 `I am going …` (vurgusuz) | 209 · 1204 · 400 · 72 | Fredoka 700 72 |
| fig (öğretmen, `kadro.ogretmen`) | 865 · 1052 · 87 · 280 | — |

Bantlar: 0–280 boş · 280–350 kanal · 360–450 rozet · 460–848 başlık · 896–1332 kartlar + figür (zemin çizgisi y 1332, x 853–956) ·
1400–1920 boş. Çiftler arası kesişim 0; rozet altı → başlık üstü 26 px; başlık altı → kart 1 47 px; kart arası 36 px; kart sağı (+4) → figür 20 px.
Sarı kutu x 88–932 (v1'de 68–1012 idi; S3-SON kusur 3 kapandı).

## Olay listesi
| Olay | Kare / sn | Cümle sözcüğü |
|---|---|---|
| kapak tam görünür | 0 / 0,00 → son (çizelge 1,0 sn, yakalama 0,5 sn; ilk = orta = son kare) | — (anlatımdan bağımsız) |

`olaylar.json` = `[]`. Ses, altyazı, karaoke, çip yok.

## Bakılan kareler
| Kare | Bulgu |
|---|---|
| `P/kapak-c.png` (açık) | taşma, kesik yazı, üst üste binme yok; kanal + rozet kapak A ile aynı yerde; sarı kutu `#ffe066`, yazı lacivert; 0–280 ve 1400–1920 boş; x 960 sağı boş; altyazı yok |
| `k/koyu/kapak-c-koyu.png` | aynı yerleşim; kontrast iyi; kutu ve hap `#f2a93b`, yazıları koyu; logo şeffaf sürüm |

Düzeltme turu: 0.

## Değişen dosyalar
- `SPEC.md` v2 (şef). `uret.py` (agy yazdı; şef baştan sona okudu, SPEC'e uyuyor, düzeltme gerekmedi).
- Üretilen: `nesneler.json`, `olaylar.json`, `proje/index.html`, `k/at-0.5s.png`, `k/koyu/*`, `P/kapak-c.png`.
- `yardim.py`, `calistir.sh`, `olay.py`, `zamanlar.json`, `cizim/` değişmedi (kanal katmanı `uret.py` içinde, sahne 01 kalıbıyla).

## agy koşu özeti
`~/.claude/canavar/agy-filo/20261115-191352/ozet.md` — 1/1 başarılı · 290 sn · rol `kod` · gemini-3.8-flash-high · girdi 1.820.565 / çıktı 155.222 token.
Özetin "değişen" listesinde `.claude/docs/sozlesme.md` ve `02-03-ydt-temel` dosyaları da var: bunlar paralel oturumların işi; agy yalnız `uret.py` yazdığını bildirdi.

## Açık noktalar
1. Çakışma kapısı durağan kareleri ölçmez (çıkış 2). Denetim piksel ölçümü ve göz denetimiyle yapıldı.
2. Başlık S = 170 (üst sınır); başlık bandı 460–848 oldu, BRIEF'teki "≈ 460–800"den 48 px uzun. Kartlar buna göre 896'dan başlar; içerik bandı (1380) aşılmadı.
3. Kart genişliği figür yüzünden 777 px; ikon kutusu 105 px (bilet ikonu 105×41, küçük ama okunur).
4. Platform arayüzü bölgeleri (üst 0–250, alt 1580+, sağ 960+) üçüncü taraf ölçümüdür; gerçek ekranda doğrulanmadı (standart §2).
