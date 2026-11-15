# RAPOR — 02-04-ydt-temel-s1 · sahne 06-hyperframes-kapak-c (huni v2) · 15.11.2026

| Ölçüm | Değer |
|---|---|
| `calistir.sh --tema acik` | çıkış 0 · `P/kapak-c.png` PNG 1080×1920 |
| `calistir.sh --tema koyu` | çıkış 0 · `k/koyu/kapak-c-koyu.png` PNG 1080×1920 |
| `uret.py` | `index.html yazıldı 23463` · `S=160` · §6 assert'leri geçti |
| Çakışma kapısı | çıkış 2 · `HATA sahne bulunamadı: 06-hyperframes-kapak-c` (beklenen: araç yalnız `sahneler[]` okur; karede gözle denetlendi) |
| Metin taraması (`tam ders`, `dakika`) | boş (grep çıkış 1) |
| Kanal katmanı (iki kare, piksel) | logo mürekkebi x 60–239, y 298–330 (resim 291–339) · `@ydspublishing` x 264–596, y 296–339 (taban 330); sahne 01 v2 ölçümüyle aynı |
| Boş bölgeler (piksel, eşik 60) | y 0–280: 0 · y 1385–1920: 0 · x 961–1080: 0 · x 0–59: 0 |
| Künye / içerik (piksel) | künye x 60–867, y 386–433 · içerik x 68–951, y 478–1361 |
| Eski çıktı yedeği | `~/Silinecekler/2026-11-15-huni-v2/02-04-ydt-temel-s1/kapak-c.png` (önceden), sahne v1 dosyaları `…/sahneler/06-hyperframes-kapak-c/` |

## Olay listesi
Durağan kare; ses, altyazı, çip yok. `olaylar.json` = `[]`. Çizelge 1,0 sn (HyperFrames en az), yakalama 0,5 sn; ilk = orta = son kare.

| Olay | Kare / sn | Cümle sözcüğü |
|---|---|---|
| kapak tam görünür (kanal, künye, başlık, kutu, ev, figür, bavul, etiketler) | 0 / 0,00 → son | — (anlatımdan bağımsız) |

## Yerleşim (nesneler.json)
| Blok | x · y · w · h |
|---|---|
| kanal | 60 · 280 · 542 · 70 |
| kunye | 60 · 360 · 808 · 90 |
| baslik (`I LIVE` / `I AM LIVING`, Fredoka 700 160) | 72 · 470 · 876 · 309 |
| bk-kutu (`AM LIVING`, tek vurgu) | 135 · 616 · 813 · 163 |
| et-kalici (Caveat 700 88) | 139 · 984 · 153 · 92 |
| et-gecici (Caveat 700 88) | 730 · 1056 · 159 · 92 |
| ev | 80 · 1090 · 270 · 270 |
| fig (öğretmen, eli boş) | 436 · 880 · 149 · 480 |
| bavul | 744 · 1162 · 132 · 198 |

Zemin çizgisi y 1360, x 70–950. Çiftler arası kesişim 0; başlık altı → figür üstü 101 px; ev–fig 86 px, fig–bavul 160 px; etiket → ikon 13,6 px.

## Değişen dosyalar
- `SPEC.md` v2 (şef). v1 yedeği Silinecekler'de.
- `yardim.py`: sahne 01 v2 `yardim.py` kopyası (`cp`, yalnız 1. satır docstring farklı). `kunye_svg()` argümansız: `<g id="kunye">` → `#kanal`
  (`#logoimg` + `#kanal-yazi`), `#ku-konu`, `#rz0`; `HUD` v2 bantları (kenar 60, sagSinir 960, icerikBas 460, icerikSon 1380, altyaziSon 1550).
  Gerekçe: aynı dönüşüm sahne 01'de yazıldı ve doğrulandı; ikinci kez yazdırılmadı.
- `uret.py`: agy yazdı (SPEC §3). Şef baştan sona okudu; SPEC'e uyuyor, düzeltme gerekmedi.
- `nesneler.json`, `proje/index.html` (önizleme açık temada bırakıldı), `k/at-0.5s.png`, `k/koyu/*`, `P/kapak-c.png`.
- `calistir.sh`, `olay.py`, `zamanlar.json`, `cizim/` değişmedi.

## Bakılan kareler
| Kare | Bulgu |
|---|---|
| `P/kapak-c.png` (= `k/at-0.5s.png`, açık) | taşma, kesik yazı, üst üste binme, boş kare YOK; 0–280 ve 1570–1920 boş; x 961+ boş; kanal katmanı + künye tablodaki yerde; sarı kutu `#ffe066`, yazı lacivert |
| `k/koyu/kapak-c-koyu.png` | aynı yerleşim; kontrast iyi; kutu `#f2a93b`, `AM LIVING` koyu |
| `/tmp/kapakc/baslik-acik.png` (başlık kırpığı, açık) | `I LIVE` ve `I` çevresinde açık temada çok soluk zemin renkli kontur halesi (vinyet zemini kontur renginden biraz koyu); okunurluğu bozmaz, sahne 01 ile aynı kalıp |

Düzeltme turu: 0.

## agy koşu özeti
`~/.claude/canavar/agy-filo/20261115-190354/ozet.md` — 1/1 başarılı · 187 sn · rol `kod` · gemini-3.8-flash-high · girdi 1.081.481 / çıktı 101.973 token.
Özetin "değişen" listesinde 04, 05 ve s2 sahne dosyaları da var: bunlar paralel oturumların işi; agy yalnız `uret.py` yazdığını bildirdi.

## Açık noktalar
1. Çakışma kapısı durağan kareleri ölçmez (çıkış 2). Denetim piksel ölçümü ve göz denetimiyle yapıldı.
2. Açık temada başlık konturunun soluk halesi (yukarıda). İstenirse açık temada kontur kaldırılır; bu iş `hf_tema.py` (ortak) ya da sahne CSS'i ister.
3. Platform arayüzü bölgeleri (üst 0–250, alt 1580+, sağ 960+) üçüncü taraf ölçümüdür; yayın öncesi gerçek ekranda doğrulanmadı (standart §2).
