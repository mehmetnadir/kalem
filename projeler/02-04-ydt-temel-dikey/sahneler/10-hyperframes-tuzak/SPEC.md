# SPEC — 02-04-ydt-temel-dikey · sahne 10-hyperframes-tuzak (HyperFrames, 1080×1920, 656 kare)

Kaynak: `projeler/02-04-ydt-temel-dikey/BRIEF-DIKEY.md` §2 + §3 satır 10. Yazan: şef (15.11.2026). Tasarım verir; tam kod yok.
K = `/home/sef/01dev/_worktrees/kalem-0204`. D = `K/projeler/02-04-ydt-temel-dikey/sahneler/10-hyperframes-tuzak/`.

## 1. Dosyalar

| Dosya | Durum | İş |
|---|---|---|
| `D/uret.py` | YOK | §4–§8'e göre YAZ (tek iş) |
| `D/yardim.py` | VAR (dikey 01 kopyası) | DOKUNMA; `W, H, u, RENK, genislik, Sahne, el_kutu, el_cizgi, balon_sol, altyazi_dilimleri, altyazi_svg, html, kontrol, ORTAK, LOGO_EN_BOY` buradan |
| `D/olay.py` | VAR (dikey 01 kopyası) | DOKUNMA; `s, _ = U.uret()` ve `U.Z["kare"]` ister |
| `D/calistir.sh` | VAR | DOKUNMA |

Başka dosyaya dokunma. Silme yok. Test, render, git yok. `ortak/`, BRIEF, yatay paket salt okunur.

## 2. Kalıp kaynakları (salt oku)

| Kalıp | Mutlak yol | Ne alınır |
|---|---|---|
| Aynı içerik, yatay | `K/projeler/02-04-ydt-temel/sahneler/10-hyperframes-tuzak/uret.py` | bütün kurgu: `T(i)`/`Q(i)`, `gen()`, `metin()`, fosfor + `w6z` pilMetin kopyası, TR satırı `trw` kırpması ve `ek_ayir` (TIRE_PAY 0,14 · TIRE_ARA 0,08 · KUTU_UST 0,64 · KUTU_ALT 0,36 · kayma 0,36 sn `power3.out` · renk te+0,20 · tire te+0,28), `bag` yolu + ok ucu, `?` `back.out(2)`, öğrenci başı (3 yol, `bas%d`), balon + sözcükler, sarı nokta çizgisi, `living` altçizgisi, `kart`/`bal_ids` grupları, `Y.html(..., bal_ids=..., gruplar=[("kartg", kart)])`. Yerleşim ondan ALINMAZ |
| Dikey iskelet | `K/projeler/02-04-ydt-temel-dikey/sahneler/01-hyperframes-giris/uret.py` | `PAKET`, `SAH`, `Z`, assert biçimi, altyazı aç/kapa, `uret()` → `(s, kun)`, `__main__` |
| Dikey HUD (HF) | `K/projeler/present-continuous-dikey/sahneler/06-hyperframes-form/yardim.py` `kunye_svg()` | ders adı + rozet + çip SVG kalıbı (dikey 02-04 sayıları §5) |
| HUD sayıları | `K/projeler/02-04-ydt-temel-dikey/ortak/kunye.js` `KUNYE` | ders 2 satır, rozet, çip, logo |

## 3. Zaman (tek kaynak: dosyadan oku, sabit yazma)

- `zaman.json` sahne: t_bas 162,33 · kare 656 · sure 656/30. Yerel sn = küresel − 162,33 (`s.S()`).
- `sozcukler.json`: `S11` = cümle 11 (30 sözcük), `S12` = cümle 12 (10 sözcük). Yatay assert'leri aynen (S11[5:12] I…family., S11[0,1,12,13,15,18,22,27], len(S12)==10, S12[5]=="living").
- Ekranda `İstanbul` (dosyada `Istanbul`); balonda `olmaz` küçük harf (dosyada `Olmaz`).

## 4. Yerleşim (px; içerik bandı 352–1392, altyazı 1400–1536, platform 1536+ BOŞ)

Kart TR satırlarını ÜSTE, EN satırlarını ALTA koyar. Gerekçe: `bag` *yor* → *live* yazı kesmeden aşağı iner (EN üstte olsa kol
"with" ve "Ailemle"yi keser). Kartın göreli ölçüleri (CY = kart üstü):

```
CY-34 ┌─ TRAP ─┐ Fredoka 700 96 vurgu, kenar çizgisinin ÜSTÜNDE ortalı (taban CY+33); çizgide boşluk
CY    ╞════════╧══════════════════════════════════════════╕  kart x 48–1032, kenar 4 px murekkep
CY+128│ (TR) Ailemle İstanbul'da            TR1 taban       │  hap x 88, metin XT; Fredoka 600 72 ikincil
CY+214│      yaşı-[yor]-um.                 TR2 taban       │  yor kutusu ky=TB2−46, kb=TB2+26 (≈CY+240)
      │    ?   ╲ bag (S eğrisi, ok ucu aşağı)  kanal CY+240–332│
CY+400│      I live in İstanbul             EN1 taban       │  Fredoka 700 72 murekkep, sözcük zamanlı
CY+486│      with my family.                EN2 taban       │
CY+544└────────────────────────────────────────────────────┘
```

| Ad | Değer | Not |
|---|---|---|
| KX, KW, CH | 48, 984, 544 | kart |
| CY0 → CY1 | 600 → 392 (fark −208) | 177,40 toplanma; CY1−34 = 358 ≥ 352 |
| TRAP | x 100, taban CY+33, Fredoka 700 96, `vurgu` | çizgi boşluğu [100−18, 100+w+18] |
| hap "TR" | x 88, y TB1−65, w = genislik(Lexend 700 "TR" 64)+40, h 84, rx 42; çizgi murekkep 4 | yazı Lexend 700 64 murekkep, ortalı, taban TB1 |
| XT | 88 + hap_w + 24 (≈ 239) | TR1, TR2, EN1, EN2 aynı sütun |
| TB1, TB2, EB1, EB2 | CY+128, CY+214, CY+400, CY+486 | taban |
| `?` | Fredoka 700 72 vurgu; sağ kenar = LXM−27, taban CY+318 | kolun SOLUNDA, ok ucundan ≥ 14 px |
| bag | M KXM,CY+248 C KXM,CY+292 LXM,CY+282 LXM,CY+326 + ok ucu M LXM−13,CY+306 L LXM,CY+326 L LXM+13,CY+306 | KXM = yor kutusu ortası, LXM = *live* ortası; murekkep 4 |
| fosfor | x live−0,10·72, y EB1−0,78·72, h 0,90·72, rx 10 | *live* altında |
| Balon | BX0 290, BY0 966, BY1 1276; BX1 = BX0+40+en geniş satır+40 (≈ 843) | aynalı `balon_sol`: kuyruk SAĞA, ucu (870, 1270) |
| Balon yazısı | Caveat 700 64 murekkep, x BX0+40, tabanlar BY0+76 / +168 / +260 (aralık 92) | 3 satır, sözcük sözcük |
| Öğrenci başı | `transform="translate(987.4 1217.5) scale(-0.505 0.505)"` (AYNA: yüz sola, balona bakar); çizgi 4,0 | kutu ≈ x 891–1009, y 1220–1380 (sahne 11 ile aynı yer) |
| Sarı nokta çizgisi (CY1 koordinatı) | M 800,BY0+1 L 800,YC+30 Q 800,YC 770,YC L KX1+16,YC Q KX1−14,YC KX1−14,YC−12; YC = CY1+kb_göreli+22 | sağ boşluktan (EN satırları ≤ 751) kanala girer, yor kutusunun altında biter; nokta (800, BY0+1) r 12 |
| `living` altı | x living−3 → living+w+3, y taban2+28 (0,44 em; g kuyruğunun altı), w 9, vurgu | |

Aynalı balon: `s.yol("bal", Y.balon_sol(BX0, BY0, BX1, BY1, BX0+BX1−870, 1270), ..., ek='transform="matrix(-1 0 0 1 %.2f 0)"' % (BX0+BX1))`.
Kart kenarı AÇIK yol: uret.py içinde `el_kutu`'ya benzer el çizimi; TRAP boşluğunun sağ ucundan başlar, saat yönünde döner, sol ucunda biter.

## 5. HUD (kare 0'dan tam, hareketsiz; `kunye_tam(bolum)` uret.py içinde, tek `<g id="kunye">`)

| Öğe | id | Değer |
|---|---|---|
| ders satır 1 / 2 | `ku-ders1`, `ku-ders2` | `SIMPLE PRESENT vs` / `PRESENT CONTINUOUS`, Fredoka 700 56, `#f3efe6`, x 48, taban 212 / 276 |
| rozet | `ku-rozet` | rect x RX = 48 + genislik(Fredoka 700 "PRESENT CONTINUOUS" 56) + 24, y 216, w = genislik(Lexend 700 "YDT · TEMEL" 36)+56, h 72, rx 36, fill `#f2a93b`; yazı Lexend 700 36 `#1b1a17`, ortalı, taban 265 |
| çip | `ku-bolum` | `Trap`: yardim.kunye_svg içindeki rect + text ile aynı (x = 1032 − cw, y 48, h 80, rx 40, çizgi 4 `#f2a93b`, Lexend 700 40, taban 102) |
| logo | `#logoimg` | `Y.html` logo = (48, 48, 96·Y.LOGO_EN_BOY, 96) |

ID yasağı: `t1`, `t2`, `rz1`, `ku-nokta` (hf_tema özel kuralı). `ku-` öneki yalnız HUD'da.

## 6. Olay listesi (küresel sn; kare = yerel sn × 30)

| # | Olay | sn | Sözcük | Ses |
|---|---|---|---|---|
| 1 | TRAP yazı açılır (0,3 sn) + kart kenarı çizilir (t+0,1, 0,7 sn) + `kartg` ölçek 0,93→1 (0,9 sn `power3.out`, köken kart ortası) | 162,88 | Tuzak. S11[0] | tik 0,45 · cizgi 0,7 |
| 2 | hap çizgisi (0,3 sn) + "TR" yazısı (0,2 sn) | 163,84 | Türkçe S11[1] | tik 0,35 |
| 3 | EN sözcükleri, satır 1 I·live·in·İstanbul, satır 2 with·my·family. (0,18 sn; family. 0,3) | 166,09–167,53 | S11[5..11] | tik (I, İstanbul, family.) 0,5 |
| 4 | TR1 `Ailemle İstanbul'da` (0,45 sn) | 168,66 | S11[12] | tik 0,45 |
| 5 | TR2 `yaşıyorum.` bitişik, kırpma açılır (0,4 sn; genişlik = son hâl + 24) | 169,54 | S11[13] | tik 0,45 |
| 6 | `ek_ayir`: yor + um kayar, kutu büyür; yor yazısı te+0,20'de pilMetin; tireler te+0,28 | 171,30 | yor S11[15] | cizgi 0,55 |
| 7 | `bag` tek yol (kol + ok ucu), 0,6 sn | 172,74 | Yor S11[18] | cizgi 0,55 |
| 8 | `?` (sarı) ölçek 0,4→1, 0,3 sn `back.out(2)` | 174,26 | akla S11[22] | tik 0,55 |
| 9 | fosfor genişler (0,35 sn `power2.out`); live pilMetin kopyası t+0,3 | 176,26 | -ing S11[27] | cizgi 0,5 |
| 10 | `kartg` y −208 (0,35 sn `power3.out`) | 177,40 | cümle 11 sonu | — |
| 11 | baş 3 yol (Q(0)−0,20 + 0,05·i, 0,32 sn) · balon t+0,10 (0,55 sn) | 177,65 | Hocam, S12[0] | cizgi 0,55 ×3 · cizgi 0,7 |
| 12 | balon sözcükleri (0,12 sn; mı? 0,25) — satır 1 Hocam,·Türkçesi · satır 2 yaşıyorum.·I·am·living · satır 3 in·İstanbul·olmaz·mı? | 177,85–183,39 | S12[0..9] | tik (Hocam,, I) |
| 13 | sarı nokta (ölçek 0,3→1, 0,25 sn) + çizgi (0,45 sn, w 9); AYNI ANDA `?` sarı → ikincil kopya | 179,37 | yaşıyorum. S12[2] | cizgi 0,45 |
| 14 | `living` sarı altı (0,35 sn); AYNI ANDA nokta + çizgi → ikincil kopya (w 6) | 181,36 (S12[5]+0,3) | living | cizgi 0,45 |
| 15 | durgun; son 12 kare geçiş altında | 183,64–183,79+ | — | — |

Altyazı: `Y.altyazi_dilimleri([11, 12])` → `alt{i}`; görünür aralık [max(0, L(t0)−0,05), min(L(t1)+0,35, L(sonraki t0)−0,05)); son dilim sahne sonuna kadar.
Aynı anda tek dilim. `Y.altyazi_svg(...)` `__main__`te `ek=` ile geçer.

## 7. Renk ve kurallar

- Koyu hex yaz, hf_tema çevirir: murekkep `#f3efe6`, ikincil `#c9c2b3`, vurgu `#f2a93b` (rect/circle dolgusu → vurguDolgu), dolgu üstü yazı `#1b1a17` (→ pilMetin).
- TR satırları ikincil (72 px), EN murekkep, tireler ikincil, bag murekkep, hap murekkep.
- Aynı anda en çok 3 sarı belirteç: kutu · `?` · fosfor (176,26) → 179,37 `?` ikincil, çizgi sarı → 181,36 çizgi ikincil, altçizgi sarı.
- Renk değişimi = iki kopya + `s.set` opaklık (yatay `w6z` gibi). `attr: {fill}` ara değer tween'i YASAK (CSS eşleşmesi bozulur).
- Kırmızı, yeşil, emoji, gradyan, gölge yok. En küçük içerik yazısı 64 (balon, hap); HUD 36/40/56.
- `uret()` tam 2 değer döndürür: `(s, kun)`; grup kümeleri `s.kart` (set) ve `s.bal` (liste) özniteliğinde. `kart` = trap, kr, trp, trl,
  tra, trw, en5–en11, en6z, fos, bag, qm, qmi. `bal` = bas, bal, bw0–bw9, bg, bgd, bgi, bgdi, ml.
- `Y.kontrol(s, Z["kare"])` (ilk=True). Python girinti 4, satır ≤ 140. Çalıştırma `/usr/bin/python3 uret.py` (fontTools; `-I` yok).

## 8. Assert'ler (uret.py içinde; ihlalde dur)

1. Her metin satırının sağ ucu ≤ 992 (kart içi); balon BX1 ≤ 850 ve 800 ≤ BX1 − 40.
2. CY1 − 34 ≥ 352; CY0 + CH ≤ 1392; CY1 + CH + 24 ≤ BY0; BY1 ≤ 1392; baş altı 1380 ≤ 1392.
3. kanal: (CY+332) − kb ≥ 80; `?` üstü (taban − 0,74·72) − (TB2 + 0,27·72) ≥ 20; (EB1 − 0,74·72) − `?` tabanı ≥ 20; `?` sağ ucu ≤ LXM − 25.
4. fosfor sol ucu > "I" sağ ucu + 6 ve fosfor sağ ucu < "in" sol ucu − 6; ok ucu (CY+326) ≤ fosfor üstü − 12.
5. sarı nokta çizgisi: 800 − max(EN1, EN2 sağ ucu) ≥ 40; YC − kb ≥ 18; (CY1+332) − YC ≥ 40; KX1 + 16 > KXM + 40.
6. `living` altı + 5 ≤ taban3 − 0,72·64 − 6 (satır 3); balon sözcük satırları BX1 − 40 içinde.
7. Ders ve rozet 984 içinde, rozet sağ ucu < çip sol ucu (HUD satır ayrı ama yazı kutuları çakışmaz).

## 9. Kabul

1. `cd D && /usr/bin/python3 uret.py && /usr/bin/python3 olay.py` çıkış 0; `olaylar.json` ≈ 20 olay, hepsi kare < 644.
2. `proje/index.html`: `data-width="1080" data-height="1920"`, `#kunye` içinde ku-ders1, ku-ders2, ku-rozet, ku-bolum; `#kartg`, `#balg`, `alt0…`.
3. `cd K && bash araclar/qa-yerel.sh 02-04-ydt-temel-dikey 10-hyperframes-tuzak 174.8,177.2,183.7 183.7 --hazirla` çıkış 0 (şef koşar).
4. Kareler: taşma, kesik yazı, üst üste binme, okunmaz kontrast, boş kare, platform bandında öğe YOK; altyazı bandında metin.
