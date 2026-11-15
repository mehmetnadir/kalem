# SPEC — 02-04-ydt-temel-s3 sahne 03 CTA (HyperFrames, DİKEY 1080×1920) · 15.11.2026

## 0. Görev
Yazılacak dosya (yalnız bu): `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s3/sahneler/03-hyperframes-cta/uret.py`
Başka dosyaya dokunma. Silme yok. Test, render, git yok.

Bu dosya şu an S1 örneğinin birebir kopyasıdır:
`/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s1/sahneler/03-hyperframes-cta/uret.py` (S1 SPEC'i aynı dizinde `SPEC.md`).
İş: kopyayı yerinde DÜZENLE (baştan yazma). Yerleşim, kinetik sözcükler, bant, saat, hap, altyazı, künye, JS işlevleri
(`ac`, `darbe`, `darbeCok`, `yaz`, altyazı döngüsü) olduğu gibi kalır. Değişen yalnız: cümle numarası ve ikonlar (ev → tren, bavul → bilet).

Neden: S3 sahne 03 sesi S1 sahne 03 sesiyle aynı dosya (md5 `80e56127…`). Sözcük çapaları S1 − 4,00 sn. Göreli zamanlar aynı kalır;
küresel zaman `zaman.json` (t_bas 15,99) ve `sozcukler.json` cümle 4'ten okunur. Sabit saniye yazma.

## 1. Zaman ve cümle (satır numaraları kopyadaki yerlerdir)
1. Satır 1–2 docstring: `02-04-ydt-temel-s1` → `02-04-ydt-temel-s3`; `Cümle 3` → `Cümle 4`.
2. Satır 16 yorum `# 19.99` → `# 15.99`.
3. Satır 21: `if w["cumle"] == 3` → `if w["cumle"] == 4`.
4. Satır 31 ve 40 docstring: `Cümle 3` → `Cümle 4`.
5. `BEKLENEN_SOZLER` aynı kalır (cümle 4 sözcük sırası S1 cümle 3 ile aynı: 0 Bu, 16.54 · 1 üç 17.02 · 5 Tam 18.77 · 7 Simple 19.97 ·
   9 ve 20.77 · 12 Üç 23.00 · 15 dört 24.36 · 17 dakikada. 24.84 (t1 25.64)).

## 2. İkon verisi (ev ve bavul yerine tren ve bilet)
Kaynak (kalıp, birebir al): `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel/sahneler/07-hyperframes-kural/uret.py`
satır 79–105: `_kutu(x, y, w, h, ince=False)`, `TREN` listesi, `_bilet()` işlevi, `BILET = _bilet()`.
Bunlar ana ders sahne 05 `trenParcalari` / `biletParcalari` sadeleştirmesidir; S3 kapak A aynı çizimi kullanır (döngü tutarlılığı).

1. Satır 59–67 `BAVUL` bloğunu sil; yerine yukarıdaki 4 öğeyi koy. Yeni işlevlere type hint ekle
   (`_kutu(...) -> Dict[str, Any]`, `_bilet() -> List[Dict[str, Any]]`, `TREN: List[Dict[str, Any]]`, `BILET: List[Dict[str, Any]]`).
   Koordinatları değiştirme. Yorum satırı: `# Tren ve bilet ikonu (02-04-ydt-temel sahne 07; kaynak sahne 05 trenParcalari/biletParcalari)`.
2. `_kutusu`, `_daire_yolu`, `ikon_yollari` aynı kalır (S1'deki `ikon_yollari(parcalar, mx0, my0, en, boy)` imzası).

## 3. Yerleşim sabitleri (satır 146–152 `# İkonlar` bloğu)
`EV_*` ve `BAVUL_*` sabitlerini sil; yerine:

| Sabit | Değer | Anlam |
|---|---|---|
| `TREN_CX` | 84.0 | sol şerit merkezi (x 48–120; banda 12 px boşluk) |
| `BILET_CX` | 996.0 | sağ şerit merkezi (x 960–1032) |
| `IKON_EN` | 72.0 | ikon kutusu genişliği (tren ve bilet geniş: genişlik bağlar) |
| `IKON_KALIN` | 4.0 | ana çizgi kalınlığı (görünür px) |
| `IKON_INCE` | 2.6 | `ince` parça kalınlığı |

Dikey konum `uret()` içinde `bant_boy`'dan hesaplanır (sabit px değil): her ikon kendi bant satırının hizasında durur.
- `tren_cy = P1_Y - 0.36 * bant_boy` (≈ 731; satır 1 `Simple Present` hizası — tarife = Simple Present).
- `bilet_cy = P2_Y - 0.36 * bant_boy` (≈ 823; satır 2 `vs Present Continuous` hizası — plan = Present Continuous).

## 4. `uret()` bölüm 4 (satır 214–227) yeniden
Başlık yorumu `# 4. İkonlar: Tren (sol, satır 1) ve Bilet (sağ, satır 2)`. Ev (`Y.tabler("home")`, `ev_s`, `ev_x`, `ev_y`) kodunu sil.
- `tren_yollar = ikon_yollari(TREN, TREN_CX, tren_cy, IKON_EN, IKON_EN)`; `tren_ids = ["tren_0", …]`;
  `tren_svg` = her parça `<path id="tren_{i}" d="{d}" stroke-width="{IKON_INCE if ince else IKON_KALIN}" style="opacity:0"/>`
  (S1 `bavul_svg` kalıbının aynısı).
- `bilet_yollar`, `bilet_ids`, `bilet_svg`: aynı kalıp, `BILET`, `BILET_CX`, `bilet_cy`, id öneki `bilet_`.
- Denetim (`assert`): iki ikonun ölçekli kutusu (`_kutusu` × ölçek, merkez etrafında) x'te şeride sığar
  (tren 48 ≤ x0, x1 ≤ BANT_X − 8; bilet BANT_X + BANT_W + 8 ≤ x0, x1 ≤ 1032) ve y'de bandın içinde kalır
  (BANT_Y ≤ y0, y1 ≤ BANT_Y + BANT_H). Ölçek `ikon_yollari` ile aynı formül: `min(boy/gh, en/gw)`.

## 5. Zamanlar, veri, SVG, JS
1. `zamanlar` sözlüğü: `"ev_darbe"` → `"tren_darbe"`, `"bavul_darbe"` → `"bilet_darbe"` (değerler aynı:
   `[y_sn(E(17, "dakikada")), 0.45]` ve `[y_sn(E(17, "dakikada") + 0.10), 0.45]`). `olaylar` listesi aynı (11 satır).
2. `veri`: `"ev_ids"` → `"tren_ids": tren_ids`, `"bavul_ids"` → `"bilet_ids": bilet_ids`.
3. HTML (satır 368–378): iki `<g>` bloğu yerine:
   `<!-- İkon Sol: Tren (satır 1 hizası) -->` + `<g id="tren" fill="none" stroke="{R['murekkep']}" stroke-linecap="round" stroke-linejoin="round">{tren_svg}</g>`
   `<!-- İkon Sağ: Bilet (satır 2 hizası) -->` + aynı kalıpta `<g id="bilet" …>{bilet_svg}</g>`. İç `transform` grubu YOK (yollar sahne koordinatında).
4. JS (satır 475–476): `darbeCok(V.tren_ids, Z.tren_darbe[0], Z.tren_darbe[1]);` ve `darbeCok(V.bilet_ids, Z.bilet_darbe[0], Z.bilet_darbe[1]);`.

## 6. Olay listesi (S3 küresel; yerel = küresel − 15,99; kare = round(yerel × 30); hepsi `T`/`E` çapasından)

| Olay | Çapa | Küresel sn | Yerel · kare | Ses olayı |
|---|---|---|---|---|
| `üç` kinetik + altçizgi | T(1,"üç") | 17.02 | 1.03 · 31 | tik 0.4 · cizgi 0.5 (+0.22) |
| `farktan` · `biri` | T(2) · T(4) | 17.18 · 18.22 | 1.19 · 36 · 2.23 · 67 | — |
| `Tam ders:` yazımı | T(5,"tam") → E(6) | 18.77–19.81 | 2.78 · 83 | hisirti 0.45 |
| bant + `Simple` · `Present` | T(7) · T(8) | 19.97 · 20.21 | 3.98 · 119 · 4.22 · 127 | vurus 0.9 |
| `vs` (sesteki `ve`) | T(9,"ve") | 20.77 | 4.78 · 143 | tik 0.5 |
| `Present` · `Continuous` | T(10) · T(11) | 21.25 · 21.93 | 5.26 · 158 · 5.94 · 178 | — |
| `farktan biri` çıkışı → `farkın` · `hepsi` | T(12) · T(13) · T(14) | 23.00 · 23.24 · 23.72 | 7.01 · 210 … | tik 0.4 |
| saat darbesi + `dört` · `buçuk` · `dakikada` | T(15) · T(16) · T(17) | 24.36 · 24.60 · 24.84 | 8.37 · 251 … | cizgi 0.5 |
| hap girişi · `@ydspublishing` yazımı | T(17) · T(17)+0.10 → E(17) | 24.84 · 24.94–25.64 | 8.85 · 266 · 8.95 | tik 0.6 · hisirti 0.5 |
| tren darbesi (sol) | E(17,"dakikada") | 25.64 | 9.65 · 290 | cizgi 0.45 |
| bilet darbesi (sağ) | E(17)+0.10 | 25.74 | 9.75 · 293 | cizgi 0.45 |

Hareket yerel 10.20'de (kare 306) biter; kare 306–346 durgun son düzen.

## 7. Kurallar
- Ekran metni değişmez: `üç farktan biri`, `üç farkın hepsi`, `Tam ders:`, `Simple Present`, `vs Present Continuous`, `dört buçuk dakikada`,
  `@ydspublishing`. "kanal", "6 dk", QR, emoji yok.
- Renk: yalnız `R` (`Y.RENK` koyu değerleri); ikonlar `R['murekkep']`. `#ffe066` / `#1b2440` sabit yazma (tema dönüştürür).
- `id="t2"`, `id="rz1"`, `id="ku-nokta"` kullanma. Bütün id'ler tekil.
- Python: girinti 4, satır ≤ 120, yeni işlevde type hint.

## 8. Kabul ölçütü (şef doğrular)
1. `cd <sahne> && /usr/bin/python3 uret.py` çıkış 0; `proje/index.html` ve `zamanlar.json` yazılır.
2. `zamanlar.json`: `t_bas` 15.99, `kare` 347; bütün yerel değerler S1 `zamanlar.json` ile aynı (yalnız `ev_darbe`/`bavul_darbe` adları
   `tren_darbe`/`bilet_darbe` oldu); `olaylar` 11 satır.
3. `grep -n "ev_\|bavul\|BAVUL\|EV_\|home\|cumle\"\] == 3" uret.py` boş döner.
4. `index.html`: `id="tren"`, `id="bilet"`, `tren_0`, `bilet_0` var; `id="ev"`, `id="bavul"` yok.
5. Şef koşturur: `bash araclar/qa-yerel.sh 02-04-ydt-temel-s3 03-hyperframes-cta 18.7,23.0,26.4 25.8 --hazirla` → kapı çıkış kodu 0.
