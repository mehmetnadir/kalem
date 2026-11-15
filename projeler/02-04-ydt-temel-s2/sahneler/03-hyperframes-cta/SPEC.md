# SPEC — 02-04-ydt-temel-s2 sahne 03 CTA (HyperFrames, DİKEY 1080×1920) · 15.11.2026

## 0. Görev
Yazılacak dosya (yalnız bu): `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s2/sahneler/03-hyperframes-cta/uret.py`
Başka dosyaya dokunma. Silme yok. Test, render, git yok.

Durum: `uret.py` S1 sahne 03 dosyasının kopyasıdır ve S2 verisiyle çalışır (zaman `zaman.json` + `sozcukler.json` cümle 3'ten
okunur; 18 sözcük assert'i geçer). Şef 2 satırı değiştirdi (docstring, `T_BAS` yorumu). **Senin işin yalnız §3'teki ikon değişimi:**
sol ikon ev → mont, sağ ikon bavul → tişört. Geri kalan her satır (metin, yerleşim, zaman, JS akışı) AYNEN kalır.

Örnek (kalıp kaynağı): `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s1/sahneler/03-hyperframes-cta/uret.py`
(S1; aynı yerleşim, ev + bavul). İkon verisi kaynağı:
`/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel/sahneler/12-hyperframes-ozet/uret.py`
- satır 45–58: `MONT` ve `TISORT` ızgara verisi (birebir al),
- satır 124–153: `ikon_yollari` içindeki `egri` dalı (Catmull-Rom → kübik, `uz *= 1.05`; satır 143–151).

## 1. Zaman (değişmez; bilgi için)
`T_BAS` 17.41, `KARE` 347, `SURE` 11.5667. Yerel sn = küresel − 17.41. Kare = round(yerel × 30).
Cümle 3 (i · sözcük · t0 küresel): 0 Bu, 17.96 · 1 üç 18.44 · 2 farktan 18.60 · 3 yalnız 19.16 · 4 biri. 19.64 · 5 Tam 20.19 ·
6 ders: 20.63 (t1 21.23) · 7 Simple 21.39 · 8 Present 21.63 · 9 ve 22.19 · 10 Present 22.67 · 11 Continuous. 23.35 · 12 Üç 24.42 ·
13 farkın 24.66 · 14 hepsi 25.14 · 15 dört 25.78 · 16 buçuk 26.02 · 17 dakikada. 26.26 (t1 27.06).

## 2. Olay listesi (kopyadaki `zamanlar.json` ile birebir; hepsi `T(i, …)` / `E(i, …)`'den)

| # | Olay | Sözcük çapası | Küresel sn · kare | Ses olayı |
|---|---|---|---|---|
| 1 | `üç` kinetik (satır A) | T(1,"üç") | 18.44 · 31 | tik 0.4 |
| 2 | `farktan` kinetik | T(2) | 18.60 · 36 | — |
| 3 | `üç` sarı altçizgi | T(1)+0.22 | 18.66 · 38 | cizgi 0.5 |
| 4 | `biri` kinetik | T(4) | 19.64 · 67 | — |
| 5 | `Tam ders:` Caveat yazımı | T(5) → E(6) | 20.19 · 83 (1.04 sn) | hisirti 0.45 |
| 6 | ders bandı girişi + `Simple` | T(7) | 21.39 · 119 | vurus 0.9 |
| 7 | `Present` (satır 1) | T(8) | 21.63 · 127 | — |
| 8 | `vs` (sesteki `ve`) | T(9,"ve") | 22.19 · 143 | tik 0.5 |
| 9 | `Present` (satır 2) | T(10) | 22.67 · 158 | — |
| 10 | `Continuous` | T(11) | 23.35 · 178 | — |
| 11 | `farktan` + `biri` çıkış | T(12,"üç") | 24.42 · 210 | tik 0.4 |
| 12 | `farkın` · `hepsi` kinetik | T(13) · T(14) | 24.66 · 218 / 25.14 · 232 | — |
| 13 | saat darbe + `dört` | T(15) | 25.78 · 251 | cizgi 0.5 |
| 14 | `buçuk` · `dakikada` | T(16) · T(17) | 26.02 · 258 / 26.26 · 266 | — |
| 15 | `@ydspublishing` hap girişi | T(17) | 26.26 · 266 | tik 0.6 |
| 16 | hap yazımı (clip) | T(17)+0.10 → E(17) | 26.36 · 268 | hisirti 0.5 |
| 17 | **mont** darbe (bandın solu) | E(17) | 27.06 · 290 (0.45 sn) | cizgi 0.45 |
| 18 | **tişört** darbe (bandın sağı) | E(17)+0.10 | 27.16 · 292 (0.45 sn) | cizgi 0.45 |

Hareket kare 306'da biter; 306–346 durgun kuyruk (anlatım 26.98'de biter). İlk ve son 12 kare durgun.

## 3. İkon değişimi (yapılacak iş)
1. `BAVUL` veri bloğunu sil, yerine `MONT` ve `TISORT` listelerini koy (kaynak satır 45–58, sayılar birebir).
   Tip ipucu `List[Dict[str, Any]]`. Yorum: `# Mont ve tişört ızgara verisi (02-04-ydt-temel sahne 12 / 07; mont 100x120, tişört 100x90)`.
2. `ikon_yollari`'na `egri` dalını ekle: `kapali` eklemesinden ve `uz` hesabından SONRA, `if p.get("egri") and len(q) >= 3:` ise
   kaynak satır 143–151'deki Catmull-Rom yolu (`d += " C…"`, `uz *= 1.05`), değilse mevcut `M … L …` yolu. İmza ve tip ipuçları aynı kalır.
3. Sabitler: `EV_CX/EV_CY/EV_BOY` → `MONT_CX = 84.0`, `MONT_CY = 778.0`, `MONT_BOY = 72.0`;
   `BAVUL_CX/BAVUL_CY/BAVUL_BOY` → `TISORT_CX = 996.0`, `TISORT_CY = 778.0`, `TISORT_BOY = 72.0`.
4. `uret()` bölüm 4: `Y.tabler("home")` ev bloğunu kaldır. Mont ve tişört, bavul bloğu kalıbıyla:
   `mont_yollar = ikon_yollari(MONT, MONT_CX, MONT_CY, MONT_BOY, MONT_BOY)`, `mont_ids = ["mont_0", …]`,
   `<path id="mont_{i}" d="…" stroke-width="{3.0 if ince else 4.4}" style="opacity:0"/>`; tişört aynı (`tisort_{i}`).
5. SVG: `<g id="ev">…</g>` (iç `translate/scale` grubu dahil) yerine `<g id="mont" fill="none" stroke="{R['murekkep']}"
   stroke-linecap="round" stroke-linejoin="round">{mont_svg}</g>`; `<g id="bavul">` yerine aynı biçimde `<g id="tisort">`.
   Yorumlar: `İkon Sol: Mont`, `İkon Sağ: Tişört`.
6. Adlar: `veri` içinde `ev_ids` → `mont_ids`, `bavul_ids` → `tisort_ids`; `zamanlar` içinde `ev_darbe` → `mont_darbe`,
   `bavul_darbe` → `tisort_darbe` (değerler aynı: `[y_sn(E(17,"dakikada")), 0.45]`, `[y_sn(E(17,"dakikada") + 0.10), 0.45]`);
   JS sonunda `darbeCok(V.mont_ids, Z.mont_darbe[0], Z.mont_darbe[1]); darbeCok(V.tisort_ids, Z.tisort_darbe[0], Z.tisort_darbe[1]);`.
7. Dosyada `ev`, `bavul`, `home` adı kalmaz (değişken, id, yorum). `olaylar` listesi 11 satır, aynı kalır.

## 4. Yerleşim (değişmez; px, 1080×1920, kenar 48, içerik 352–1392, altyazı 1400–1536, 1536 altı boş)

| Satır | Öğe | Yazı · boy | Konum |
|---|---|---|---|
| A | `üç farktan biri` → `üç farkın hepsi` (`üç` yerinde, sarı altçizgi) | Lexend 700 · 72 | taban 452 |
| B | `Tam ders:` | Caveat 700 · 96 | taban 620 |
| Bant | `Simple Present` / `vs Present Continuous`, dolgu `R["vurgu"]`, yazı `R["zemin"]` | Fredoka 700 · 74 | 660–896, x 132–948 |
| İkon | mont (sol, kutu 72, merkez 84/778, ≈ 56×72) · tişört (sağ, merkez 996/778, ≈ 72×60) | çizgi 4,4 / ince 3,0, `R["murekkep"]` | bant dışı, 12 px boşluk |
| E | saat + `dört buçuk dakikada` | Lexend 700 · 72 | taban 1066 |
| F | `@ydspublishing` hapı (dolgu `R["vurgu"]`, yazı `R["zemin"]`) | Fredoka 700 · 64 | 1200–1312 |

Künye `Y.kunye_svg("Full lesson")` (= `KUNYE.cipler["03-hyperframes-cta"]`), altyazı `Y.altyazi_svg(T_BAS, SURE, ALT)`.

## 5. Kurallar
- Ekran metni yalnız: `üç farktan biri`, `üç farkın hepsi`, `Tam ders:`, `Simple Present`, `vs Present Continuous`, `dört buçuk dakikada`,
  `@ydspublishing`. "kanal", QR, "6 dk", emoji YOK.
- Yalnız `Y.RENK` koyu değerleri yazılır; `#ffe066` / `#1b2440` sabit yazılmaz (tema dönüşümünü `hf_tema.py` yapar). Vurgu renginde yazı yok.
  Yeşil, kırmızı, gradyan, gölge yok. `id="t2"`, `rz1`, `ku-nokta` kullanma; id'ler tekil.
- Python: type hint, girinti 4, satır ≤ 120.

## 6. Kabul ölçütü (şef doğrular)
1. `cd <sahne> && /usr/bin/python3 uret.py` çıkış 0; `proje/index.html` + `zamanlar.json` yazılır.
2. `zamanlar.json`: `mont_darbe` [9.65, 0.45], `tisort_darbe` [9.75, 0.45]; `olaylar` 11 satır; `ev_darbe`/`bavul_darbe` yok.
3. `index.html`: `id="mont"`, `id="tisort"`, `mont_0…mont_7`, `tisort_0…tisort_3`; `home`, `bavul`, `kanal`, `6 dk` dizileri yok.
4. Mont yolları `C` komutu içerir (egri parçaları: yaka ve ön kesim).
5. `bash araclar/qa-yerel.sh 02-04-ydt-temel-s2 03-hyperframes-cta 20.0,24.2,27.9 27.0 --hazirla` → çıkış 0 (şef koşturur).
