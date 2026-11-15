# İstem P0202-S2-C raporu — simple-present-temel-s2 paket + ses + zaman + sahne istemleri + açıklama (huni v2) · 15.11.2026

| Ölçüm | Değer |
|---|---|
| Ses kapısı (el.py, faster-whisper turbo, eşik 0,85) | 8 / 8 parça; hepsi tohum 0, benzerlik 1,00 (aşağıda) |
| Ses kimliği | cümle 1–3 öğretmen `gsJ9…4fwc` · cümle 4 öğrenci `oPC5…9gjY` (`senaryo.json` `sesler`; ana ders kopyası) |
| ElevenLabs | 202 karakter (≈ 0,99 TL; tahminle aynı); cümle 4 önbellekten (Whisper önbelleği 2 / 8 parça), vekil `ses-sunucu.sh` |
| Anlatım | **25,73 sn** (`anlatim.m4a` ffprobe 25.730000; imza `e2dc3f179d4a39b6…`, `aac-96k-48000-mono`); hedef 22–28, eşik 32 aşılmadı |
| Zaman çizelgesi | 01 kanca 0,00–3,00 (102) · 02 değer 3,00–11,87 (278) · 03 kaydet 11,87–19,07 (228) · 04 çağrı 19,07–25,73 (230); `hikaye` (05) + `duragan[]` (06–08) |
| Metin taraması (kapı 3) | paket (`uretim-tutanagi/` hariç) temiz: yasak çağrı kalıbı ve süre sözü 0 eşleşme |
| Jüri | 5 / 5 madde işlendi + sahne istemi notu; `S2-duzeltme.md` |

## Ses kapısı — parça başına (`ortak/anlatim/sentez.wav.rapor.json`)

| Cümle · parça | Dil | Metin | Whisper duyduğu | Benzerlik |
|---|---|---|---|---|
| 1 · 1 | tr | Usually görünce hangi zaman? | Usually görünce hangi zaman? | 1,00 |
| 2 · 1 | en | My brother usually goes to school by bus. | aynı | 1,00 |
| 2 · 2 | tr | Alışkanlık işareti. | Alışkanlık işareti | 1,00 |
| 2 · 3 | tr | Şu an değil, her sabah yedide kalkarım gibi. | … her sabah 7'de kalkarım gibi. (sayı normalize) | 1,00 |
| 3 · 1 | en | Usually, always, every day: Simple Present. | Usually, always, every day, simple present. | 1,00 |
| 3 · 2 | tr | Bu kuralı kaybetme. Kaydet. | Bu kuralı kaybetme, kaydet. | 1,00 |
| 4 · 1 | tr | Bitmedi, gel. | Bitmedi, gel. (önbellek) | 1,00 |
| 4 · 2 | tr | Dersin tamamı YDS Publishing YouTube kanalında. | … YEDESE Publishing … (ses metni `YeDeSe`; önbellek) | 1,00 |

Cümle başları 1,00 · 3,95 · 12,42 · 19,62; bitişler 3,40 · 11,87 · 19,07 · 24,73 (`baslar.json`). Günlük: `ses-sentez.log`.

## Yazılanlar

| Dosya | İçerik |
|---|---|
| `ortak/` | bağlar `cizim`, `font`, `hf_tema.py`, `logo` → `../../present-continuous/ortak/` (emsal ile aynı) · kopya `kalem-canvas.js`, `tema.sh`, `tema_damga.py` · `kunye.js` (emsal v2 kopyası; 2 Edit: `KOK`, `KUNYE.konu` = `Simple Present`) |
| `ortak/kapak/` | `ana-kapak.png`, `ana-kapak-koyu.png` (← `simple-present-temel/kapak.png`, `kapak-koyu.png`, 1920×1080) · `karakter.png` (← ana ders `ortak/kapak/`) |
| `ortak/anlatim/` | `senaryo.json` (4 cümle / 8 parça; C3 parça 1 `en`) · kopya `sozcuk_uret.py`, `kur.py`, `metin_uret.py` · `zaman_uret.py` (2 Edit: 4 sahne temiz numara, `hikaye` + `duragan[]` sabiti) · zincir çıktıları: `sentez.wav` (+ rapor), `cumle-1..4.wav`, `sureler.json`, `sozcukler.json`, `baslar.json`, `anlatim.wav`, `anlatim.m4a` (+ imza), `altyazi.json` (8 parça), `METIN.md` |
| kök | `zaman.json` · `BRIEF-S2.md` · `aciklama-a.md`, `aciklama-b.md`, `aciklama.md` (= A, `cmp` eşit) · `surumler.json` (`video.kimlik` `02-02-ydt-temel`; 8 satır `s2`, `s2-kapak-a|b|c`, `s2-hikaye-a|b`, `s2-aciklama-a|b`; durum `inceleme`; ad `S2 Shorts (25,73 sn)`) · `gorevler.json` `[]`, `yorumlar.json` `[]`, `harita-konum.json` `{}` |
| `uretim-tutanagi/` | `S2-duzeltme.md` · taslaklara jüri düzeltmeleri (senaryo §2, §4, üst not, §5b ölçülen; kapak §1, §3, §5, §6, S2-C notu; hikâye §4, §5; açıklama §4; S2-A rapor §3 ek satırı) · `istem/sahne/D-01…D-08` (8 istem) · `ses-sentez.log` · bu rapor |

Yazılmayan (istem kuralı): sahne kodu, render, mp4, git commit, alt ajan, silme, `huni-surumler.json` (Huni v2 ile kalktı). Kovan kaydı yazılmadı
(yazma kapsamı paket dizini). Sözleşme kancası bu oturumda satır istemedi.

## Açık noktalar

1. **Kapak C başlığı (şef onayı):** dil 3 ve kaynak 1a önerileri birbirini ihlal eder; birleşik metin `ÜÇ İFADE,` / `TEK İŞARET` (satır 2 kaynak
   önerisi aynen, satır 1 ana dersin "zaman ifadeleri" terimi). Başka metin istenirse yalnız `07` istemi ve kapak taslağı değişir.
2. **Hikâye B (şef):** kural özeti `usually = alışkanlık` eklendi (kaynak 2 b); soru kolaylaşır. Diğer yol standart §6'ya istisna (kaynak 2 a);
   belge `D/` altında, yazma kapsamı dışı. Emsal v2 hikâye B de kural özeti taşır.
3. **Karakter A → C (istem uyumu):** istem "karakter kapak B ya da C'de" der; taslak A'ya koymuştu. `karakter.png`'nin sola işaret eden duruşu
   C'deki karta işaret eder; A'da kalem figürü (`kadro.ogrenci`). Kapak B taslaktaki gibi (öğrenci başı + balon).
4. **Kapak A künyesi emsalden farklı:** künye (`Simple Present` + rozet) 0. kareden sabit (kapak taslağı §2, üç kapak aynı künye); başlık künye
   satırının sağ boş bölümüne uçup söner (D-01). Emsalde konu adı uçuşla geliyordu.
5. **Ana ders yönü (Nadir; kaynak jürisi şefe not):** son sahne kapağı ve "dersin tamamı" prototip `simple-present-temel`e bağlı; uzun ders
   `02-02-ydt-temel` YouTube'a çıkarsa kapak (`GİDER = GOES`) ve örnek uyuşmaz. S1 ve S3 aynı durumda.
6. **`utm_campaign` biçimi iki pakette farklı:** bu paket `ING-YDT-GR-02-02-T` (huni-plan §6, jüri geçti); emsal `02-04-ydt-temel-s1`
   küçük harf `ing-ydt-gr-02-04-t` (S1 jüri maddesi, Nadir kararı bekliyor). Tek biçim seçilince açıklamalarda yalnız bu alan değişir.
7. **Kod tabanı boşlukları:** emsalde kaydet sahnesi YOK (`08-hyperframes-kaydet`, 19:10) → D-03 yapı örneği emsal `03-hyperframes-cta`;
   emsal `07-hyperframes-hikaye-b` v1 (kanal katmanı yok) → D-08 kanal kalıbı emsal `04`, boşluklu kök `02-04-ydt-temel-s2/07`.
8. **Çakışma kapısı portu:** 8 istem emsal değerini taşır (`--port 41333 --sunucu 41022`); sahne oturumları paralel koşarsa port çakışabilir.
   Durağan kareler (05–08) kapıyla ölçülmez (çıkış 2 beklenir); gözle denetim.
9. **Bilgi:** sözcük `t1` cümle sonunu ≤ 0,08 sn aşar (`zaman?` 3,48 > 3,40; `gibi.` 11,95 > sahne sınırı 11,87; `Kaydet.` 19,15 > 19,07);
   altyazı taşır, sahne sınırı değişmez. Söyleniş "YeDeSe Publishing" Nadir kulağıyla kesinleşir (standart §4).
10. `zaman.json` `hikaye.cikti` = `hikaye-a.png` (emsalde `hikaye.png`); `hikaye.png` kopyasını 05 oturumu üretir. Bu alanı okuyan araç yok
    (`araclar/` taraması); birleştirme yalnız `sahneler[]` okur.
