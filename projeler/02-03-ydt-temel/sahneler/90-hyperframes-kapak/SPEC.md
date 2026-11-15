# SPEC — sahne 90-hyperframes-kapak · ana ders kapağı (02-03-ydt-temel, yalnız yatay, durağan tek kare)

Standart: `dijital-anlatim/.claude/docs/kapak-standardi.md` v1. İstem KAPAK-0203T (15.11.2026). `zaman.json` `sahneler[]` dışı; ses ve mp4 yok.
Emsal kopyası: `02-04-ydt-temel/sahneler/90-hyperframes-kapak/` (`uret.py`, `calistir.sh`, `yardim.py` aynı yöntem; dikey paket bu istemde yok).

| Dosya | İş |
|---|---|
| `uret.py` | emsal kopyası; biçim paket adından (`-dikey` → 1080×1920, öteki 1920×1080). `proje/index.html`, `proje/assets/` (logo-acik/koyu.svg, temizlenmiş karakter/nesne PNG), `nesneler.json` yazar |
| `calistir.sh` | emsalle birebir; `--tema acik|koyu` → paket kökü `kapak.png` / `kapak-koyu.png`; eski kök PNG `~/Silinecekler/<tarih>-kapak/` altına |
| `yardim.py` | kalıp kopyası; yalnız `genislik`, `font_css`, `font_kopyala`, `LOGO_EN_BOY` kullanılır |

- Metin (şef kararı): `ÖNCE` · vurgu kutusu `SİNYALE BAK` · Lexend `now · usually · these days` · çizgi rozet `YDT · TEMEL`.
- Görsel: `ortak/kapak/karakter.png` (büyüteçli genç, yüz ortası dosyada 465, 480) + `nesne.png` (trafik lambası, karakter boyunun 0,34'ü, başın sağında).
- Renk, logo, çıkartma kenarı (10 px, 3 geçiş × 3,33 px), görsel kopyası temizliği (alfa ≤ 64 + 3×3 açılış): emsalle aynı.
- Emsalden farklar (yerleşim): (1) `S1 = min(S1, S2)` — kısa satır 1 vurgu satırından büyük olmaz. (2) Arama döngüsüne sütun daraltma `kis`
  (0–200 px, adım 8): uzun vurgu kutusu sol %55'i doldurunca karakterin saçına 34 px yer açar. Sıra: karakter ölçeği ↓ → daraltma ↑ → yazı yukarı.
  (3) Kural: görselin çıkartma kenarı üstten %5 payın altında (standart §2 "kenardan %5"; emsalde yalnız `y > 0`).
- Sonuç (15.11): karakter ölçeği 0,99, daraltma 32 px, S1 = S2 = 144, yazı bloğu ortada (oynatma 0), daire r 345.
- Kurallar (`dogrula`): emsalle aynı + madde (3).
- Kullanım: `bash calistir.sh --tema acik` ve `--tema koyu`. `ONIZLE_YALNIZ=1 bash calistir.sh` yalnız `proje/index.html`.
