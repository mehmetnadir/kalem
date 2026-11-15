# YV-DUZ-SP — `simple-present-temel` (+ `-dikey`) yayın verisi düzeltmeleri · 16.11.2026

> Girdi: `uretim-hatti/raporlar/YV-DUZ-1511.md` §7 (madde 1–5), §5; `DUZ2-RAPOR.md` (cümle 7 yeni, ders 96,47 sn).
> Makine srv21. Ses, render, sahne, senaryo, zaman, kapak dosyalarına dokunulmadı. Silinen dosya yok.
> Eski hâller: `uretim-tutanagi/yv-duz-sp-once/` (yatay: `youtube.json`, `youtube-aciklama.md`, `surumler.json`;
> dikey: `../simple-present-temel-dikey/uretim-tutanagi/yv-duz-sp-once/`).

## 1. Özet

| Madde | Durum | Değişen dosya |
|---|---|---|
| §7.1 "Bölümler:" satırı | uygulandı | `youtube-aciklama.md` (yatay + dikey) |
| §7.2 açıklama satır 1 | uygulandı | `youtube-aciklama.md` (yatay + dikey) |
| §7.3 mutlak ifade / denklik | yayın verisinde uygulandı; seste ve ekranda açık iş (§4) | `youtube.json`, `youtube-aciklama.md` (yatay + dikey), `surumler.json` `canAlici[2]` |
| §7.4 zaman | ölçüldü, kayan değer yok | — |
| §7.5 kopya sınırı | değişiklik gerekmedi (rapor hükmü) | — |
| Düzeltme notu | yazıldı | `surumler.json` `revizyonlar[]` `ana-yatay r1-yv`, `dikey-tam r1-yv` |

## 2. Önce → sonra

| # | Yer | Önce | Sonra |
|---|---|---|---|
| 1 | açıklama, damga bloğu üstü | (başlık yok) | `Bölümler:` |
| 2 | açıklama satır 1 | `Simple Present'ı üç örnekle öğren: doğa kanunu, alışkanlık, tarife ve fiile gelen s (he, she, it).` | `Simple Present'ı üç örnekle öğren: doğa kanunu, alışkanlık ve tarife; fiile gelen s (he, she, it) de derste.` |
| 3a | `youtube.json` `bolumler[2].ad` + açıklama 00:28 satırı | `Alışkanlık: usually, always, every day` | `Alışkanlık: My brother usually goes to school` |
| 3b | `surumler.json` `video.canAlici[2]` | `usually, always, every day = tekrar eden iş sinyali` | `usually, always, every day çoğu zaman alışkanlığı işaret eder; zamanı tek başına belirlemez (always öteki zamanlarla da gelir)` |
| 3c | `surumler.json` `video.canAlici[0]` | (DUZ2 düzeltmişti) `Geniş zaman eki Türkçede her kişide gelir (giderim, gider); İngilizcede s yalnız he, she, it ile gelir (I go, he goes)` | değişmedi; yeni cümle 7 ile aynı iddia |

Gerekçeler:
- 3a: bölüm adı üç zarfı "alışkanlık" tanımı gibi sıralıyordu (jüri notu: always öteki zamanlarla da gelir). Yeni ad öteki iki örnek
  bölümünün kalıbını izler (`Doğa kanunu: The sun rises in the east`, `Tarife ve program: Our plane takes off`) ve sahne 04'ün örnek cümlesini taşır.
- 3b: `=` mutlak denklik kurar. Yeni metin derste söylenen "alışkanlık işareti"ni korur, zamanı tek başına belirlemediğini ekler.
- Dikey paket: `youtube.json` yatayla bayt eşit (`cmp`); `youtube-aciklama.md` yalnız `utm_content=dikey-tam` satırında farklı.

Taranan, değişmeyen metinler (denklik ve mutlak kod yok): başlık `Simple Present | YDT İngilizce` · 13 etiket · sabit yorum ·
gönderi g1 (`Neden "he goes" ama "I go" diyoruz? …` — yeni cümle 7 ile uyumlu) · `canAlici[1]`, `[3]`, `[4]`.
Tarama: `grep -niE "always, usually|usually, always|= *tekrar|eki *=|er eki|Kod:"` dört yayın dosyasında → 0 satır.

## 3. Zaman (ders 96,47 sn, `zaman.json`)

| Bölüm | `t` | Sahne başı | Süre | Damga |
|---|---|---|---|---|
| 1 Geniş zamandan köprü | 0 | 01 (0,00) | 15,45 | 00:00 |
| 2 Doğa kanunu | 15,45 | 03 (15,45) | 12,24 | 00:15 |
| 3 Alışkanlık | 27,69 | 04 (27,69) | 15,67 | 00:28 |
| 4 Tarife ve program | 43,36 | 05 (43,36) | 17,11 | 00:43 |
| 5 Neden hep s? | 60,47 | 06 (60,47) | 36,00 | 01:00 |

Bildirim `t` 43,91, `sure` 3,0: cümle 5 başı (`sozcukler.json` ilk sözcük 43,91). 30 sn sonrası ilk cümle başı (cümle 4 28,24'te başlar).
Bitiş 46,91 ≤ 96,47 − 20 = 76,47. Cümle başları HEAD ile aynı (cümle 1–7: 1,0 · 3,31 · 16,0 · 28,24 · 43,91 · 61,02 · 65,73).
Sonuç: kayan değer yok, hiçbir `t` değişmedi. Açıklama damga bloğu `bolumler` ile aynı (kapı `damga: 0`).
Dikey `zaman.json` sahne başları yatayla aynı (0 · 3 · 15,45 · 27,69 · 43,36 · 60,47; son 96,47).

## 4. Dersin sesinde ve ekranında kalan açık iş (dokunulmadı; senaryo, ses, sahne yazma alanı dışı)

| Yer | Zaman | Kalan ifade | Önerilen doğru cümle |
|---|---|---|---|
| Ses, cümle 7 parça 7 (`senaryo.json`, `METIN.md`, `altyazi.json` satır 207) | 90,55–95,51 | `Kod: always, usually, every day, Simple Present.` | `Always, usually, every day çoğu zaman Simple Present ile gelir; ama tek başına zamanı belirlemez.` |
| Ekran, sahne 06 formül kartı (`06-hyperframes-form/uret.py` satır 318–336; dikey `uret.py` satır 392+) | ≈ 90,55'ten sona | `always ✓ usually ✓ every day ✓ → Simple Present` | kart cümleyle birlikte değişir; ör. ok yerine "çoğu zaman" etiketi ya da kartın kaldırılması |
| `senaryo.json` `meta.canAlici[2]` | — | `usually, always, every day = tekrar eden iş sinyali` | `surumler.json` `canAlici[2]` ile eşitlenmeli (şimdi 2. öğe farklı; 0, 1, 3, 4 eşit) |
| Ses, cümle 4 (`altyazi.json` satır 95) | 35,53–39,05 | `Usually, always, every day: alışkanlık işareti.` | mutlak kod değil (alışkanlık bağlamında örnekle gelir); değişiklik önerilmez |
| Kapak metni `GİDER = GOES` (`kancaKapak`, `surumler.json` `surumler[].kapak`) | — | çeviri eşlemesi (o gider = he goes); ek denkliği iddia etmez | kapak yazma alanı dışı; jüri yeniden bakabilir |

Not: cümle 7 parça 7 değişirse ders süresi ve sahne 06 zamanı yeniden ölçülür; bölüm 5 ve bildirim cümle 7'den önce olduğu için
`youtube.json` zamanları etkilenmez (son 20 sn sınırı yeni süreyle yeniden bakılır).

## 5. Kapı

```
$ /usr/bin/python3 -I uretim-hatti/betikler/yv-tutarlilik.py --kilitli 02-04-ydt-temel-dikey
yv-tutarlilik: 12 ders, 11 dikey eş
  simple-present-temel               başlık  30 kr · açıklama  690 B · etiket 162 · bölüm  5 · süre 96.47 sn
  simple-present-temel-dikey         başlık  30 kr · açıklama  690 B · etiket 162 · bölüm  5 · süre 96.47 sn
[TAMAM] sinir: 0
[TAMAM] zaman: 0
[TAMAM] damga: 0
[TAMAM] kanal-etiketi: 0
[TAMAM] emoji: 0
[TAMAM] baslik: 0
[TAMAM] liste: 0
[TAMAM] etiket-yazim: 0
[TAMAM] kopya: 0
[TAMAM] dikey: 0
[bilgi] 02-03-ydt-temel: başlık 71 karakter (hedef ≤ 60)
[bilgi] present-continuous-ileri: başlık 66 karakter (hedef ≤ 60)
[bilgi] present-perfect-cont-ileri: başlık 73 karakter (hedef ≤ 60)
[bilgi] simple-present-ileri: başlık 62 karakter (hedef ≤ 60)
toplam sorun: 0 · kilitli pakette: 0
çıkış 0
```

`--kilitli` olmadan da çıkış 0 (önceki koşudaki 2 `[kilitli] damga` satırı kalktı).

## 6. Açık kalanlar (şef)

- §4 tablosu: cümle 7 parça 7 sesi + sahne 06 formül kartı + `meta.canAlici[2]` eşitlemesi (DUZ3 türü iş; ses sentezi gerekir).
- YVJ jürisi yeni ses (96,47 sn) üzerinde yeniden koşmalı (§7.4).
- `.claude/docs/sozlesme.md`: istem yazma alanı dışında; satır yazılmadı.

---
Son Güncelleme: 16.11.2026 — ilk sürüm (YV-DUZ-SP).
