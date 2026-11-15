# SPEC — sahne 04 Çağrı (simple-present-temel-s1, huni v2, HyperFrames DİKEY 1080×1920)

Şef yazdı (15.11). İstem: `uretim-tutanagi/istem/sahne-v2/D-04-hyperframes-cagri` (D-S1). Bağlayıcı: `D/.claude/docs/huni-v2-standart.md`.

## Kod yolu

Emsal `projeler/02-04-ydt-temel-s1/sahneler/03-hyperframes-cta/` RAPOR'u "huni v2" der → taban. Bu sahne emsalle aynı işi yapar.
Ölçüm (15.11): cümle 4 iki pakette aynı 8 sözcük (`Gerisi · bizde. · Dersin · tamamı · YDS · Publishing · YouTube · kanalında.`),
altyazı 2 parça, kare 218. Emsal `uret.py` zamanı `zaman.json` (klasör adı) ve `sozcukler.json` (cümle 4) çapasından okur;
sabit saniye yok. Bu yüzden yeni kod gerekmez:

| Dosya (mutlak yol) | Kaynak | Kurulum |
|---|---|---|
| `/home/sef/01dev/_worktrees/kalem-0204/projeler/simple-present-temel-s1/sahneler/04-hyperframes-cagri/uret.py` | emsal `03-hyperframes-cta/uret.py` (`cp -p`) | Edit: belge dizesi, `T_BAS` yorumu |
| `…/04-hyperframes-cagri/yardim.py` | aynı paket `03-hyperframes-kaydet/yardim.py` (`cp -p`; v2, `KONU = "Simple Present"`) | Edit: belge dizesi |
| `…/04-hyperframes-cagri/olay.py` | emsal (`cp -p`) | Edit: belge dizesi |
| `…/04-hyperframes-cagri/calistir.sh` | emsal (`cp -p`) | Edit: başlık, denetim karesi yorumu |

agy koşusu yok: yazılacak yeni kod satırı yok (istem: emsal `cp -p` + kısa Edit).

## Olay listesi (t_bas 17,74; yerel kare = round((t − 17,74) × 30))

| Olay | Küresel sn | Kare | Cümle 4 sözcüğü |
|---|---|---|---|
| ana kapak kartı girer (ölçek 0,94 → 1, 0,50 sn + saydamlık 0,25 sn) | 17,74–18,24 | 0–15 | sahne başı |
| `Gerisi` kinetik (y +24 → 0, 0,22 sn) | 18,29 | 16 | Gerisi |
| `bizde.` kinetik | 18,77 | 31 | bizde. |
| `@ydspublishing` sarı hap girer | 20,76 | 91 | YDS |
| `· YouTube` girer | 21,88 | 124 | YouTube |
| durgun kuyruk | 23,08 → 24,00 | 160 → 218 | kanalında. sonu |

Ses olayları: kare 12 vurus 0,6 · 16 tik 0,4 · 91 tik 0,6 · 124 tik 0,4.
`· YouTube` `YDS` çapasında değil, `YouTube` çapasında girer: BRIEF "ekran metni sesten önce gelmez" kuralı (emsal de böyle).

## Yerleşim

| Öğe | Yazı · boy | Konum |
|---|---|---|
| Kanal katmanı | logo + `@ydspublishing` Lexend 700 42 | BRIEF tablosu; `#kunye > #kanal`, `#logoimg`; opaklık 1, animasyon yok |
| Künye | `Simple Present` Fredoka 700 (≤ 34) + rozet `YDT · TEMEL` Lexend 700 26 | taban 420; hap 386–434, konu sonu + 20 |
| `Gerisi bizde.` | Fredoka 700 96 (900 px'e sığan en büyük, alt sınır 64) | x 60, taban 560 (≈ 489–560) |
| Ana kapak kartı | `assets/ana-kapak.png` / `ana-kapak-koyu.png` | x 60–960, y 620–1126 (900×506), köşe 24, `murekkep` kenar 4 px |
| `@ydspublishing` hap + `· YouTube` | Lexend 700 56 | hap x 60–…, y 1160–1240 (tek vurgu: dolgu `#f2a93b` → açık temada `vurguDolgu`, yazı `#1b1a17` → `pilMetin`) |
| Altyazı + karaoke | Lexend 500 44 | 1400–1550, en çok 2 satır, cümle 4 |

Tema: `hf_tema.py` `#logoimg` href'ini değiştirir; kapak için `uret.py` içindeki `MutationObserver` `#root.tema-acik` sınıfına göre
`#kapakimg` href'ini seçer. `calistir.sh` iki kapağı `proje/assets/`a kopyalar.

## Kurallar

- Ekran metni: `Gerisi bizde.`, `@ydspublishing`, `· YouTube`, künye, altyazı. Yasak: eski kapanış sözü, süre, saat, QR, oynat/izle düğmesi, YouTube logosu.
- Çip yok. 0–280 ve 1570–1920 boş. Sağ 960–1080 boş.
- Ana kapak dosyası yoksa `uret.py` `ana kapak bekliyor` ile durur.

## Kabul

1. `qa-yerel.sh simple-present-temel-s1 04-hyperframes-cagri 17.80,20.90,23.95 23.95 --hazirla` → 0.
2. `cakisma-kapisi.mjs … --sahne 04-hyperframes-cagri --port 41333 --sunucu 41022` → 0, 0 uyarı.
3. `grep -rniE 'tam[ ]ders|dak[i]ka'` (html/js/py) boş.
4. Kanal katmanı 4 karede aynı konumda (piksel ölçümü). Kartta `GİDER = GOES` ve karakter görünür.
