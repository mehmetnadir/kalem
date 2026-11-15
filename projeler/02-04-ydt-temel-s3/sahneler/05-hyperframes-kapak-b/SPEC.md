# SPEC v2 — 02-04-ydt-temel-s3 · sahne 05-hyperframes-kapak-b (kapak B, soru) · huni v2

Yazan: şef (15.11.2026, istem D-V2-S3). Şef kod yazmaz; bu belge tasarımı verir. Ajan tam kodu yazar.
K = `/home/sef/01dev/_worktrees/kalem-0204`. Paket P = `K/projeler/02-04-ydt-temel-s3/`. Sahne D = `P/sahneler/05-hyperframes-kapak-b/`.
Bağlayıcı: `/home/sef/01dev/dijital-anlatim/.claude/docs/huni-v2-standart.md` §2, §6 · `P/BRIEF-S3.md` "Kapak B ve C" (B satırı) ·
`/home/sef/01dev/dijital-anlatim/.claude/docs/kapak-standardi.md` (çıkartma kenarı, krem daire). v1 SPEC yedeği:
`~/Silinecekler/2026-11-15-huni-v2/02-04-ydt-temel-s3/sahneler-v1/05-hyperframes-kapak-b/SPEC.md`.

Kapak B = soru kapağı. Başlık soruyu sorar. Kart can alıcı öğeyi (`leaves`) gösterir. Cevap karede YOK. Ses yok. Durağan tek kare.

## 1. Dosyalar

| Dosya | Durum | İş |
|---|---|---|
| `D/uret.py` | VAR (v1) | **YENİDEN YAZILACAK** — mutlak yol `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s3/sahneler/05-hyperframes-kapak-b/uret.py` |
| `D/yardim.py` | VAR | DOKUNMA; yalnız `import yardim as Y` (`Y.RENK`, `Y.genislik`, `Y.font_css`, `Y.ZEMIN_CSS`, `Y.zemin_html`, `Y.font_kopyala`, `Y.LOGO_EN_BOY`, `Y.LOGO_KAYMA`) |
| `D/calistir.sh`, `D/olay.py`, `D/zamanlar.json` | VAR (şef) | DOKUNMA |
| `P/ortak/kapak/karakter.png` | VAR (896×1200 RGBA, şeffaf) | salt oku |
| `D/proje/assets/karakter.png`, `D/proje/index.html`, `D/nesneler.json` | uret.py koşunca yazar | ajan dosyayı elle yazmaz |

Başka dosyaya dokunma. Silme yok. Test, render, snapshot, `calistir.sh`, git YOK. `D/cizim/ogretmen.json` artık OKUNMAZ (öğretmen figürü kalkar).

## 2. Kalıp kaynakları (salt oku)

| Kalıp | Mutlak yol | Ne alınır |
|---|---|---|
| Başlangıç (aynı sahne, v1) | `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s3/sahneler/05-hyperframes-kapak-b/uret.py` | dosya düzeni; `zaman.json` + `zamanlar.json` doğrulaması (satır 21–33, AYNEN); `kutu_d`, `daire_d`, `tren_svg`, `saat_svg`, `soru_svg` (satır 87–187, 218–226, AYNEN); `kesisim` (satır 312–316); HTML kabuğu + tek `set` çizelgesi (satır 627–653); `__main__` düzeni (satır 659–679). **Kaldır:** `FIG` okuması (satır 53), `figur_svg`, `ok_svg`, `zc` çizgisi, v1 HUD (`kunye_svg` satır 241–254: üst logo 48–144 + rozet 216–288) |
| v2 kanal katmanı + rozet | `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s3/sahneler/01-hyperframes-kapak/uret.py` | `LOGO_W`, `LOGO_X` (satır 228–229); `KONU`, `ROZET`, `ROZET_W`, `KB_K` döngüsü, `ROZET_X` (satır 191–201); `_kunye_svg` (satır 664–684) — `ku_konu` metni YOK, yalnız `kanal` + `rz0` |
| Karakter çıkartması | `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel/sahneler/90-hyperframes-kapak/uret.py` | `ESIK = 64` (satır 37), `KENAR_GECIS = 3` (satır 38), `YUZ_PNG` (satır 42); kırıntı temizliği `gorsel_kopyala` (satır 270–279); `<img class="abs kenar">` (satır 282–287); 4 yönlü `drop-shadow` dizisi (satır 295–298). Satır 326–327 CSS'i ALINMAZ (`#root.tema-acik` yazar; bu sahnede yasak, §4.7) |

## 3. Okuma ve sabitler

- `PAKET = AD.parent.parent`. `zaman.json` → `duragan` içinde `klasor == AD.name` TEK kayıt; `kare == 1`, `cikti == "kapak-b.png"`;
  `sahneler[]` içinde `AD.name` YOK (v1 satır 22–28 aynen). `zamanlar.json`: `sure` 1,0 · `kare` 1 · `fps` 30 (v1 satır 30–33).
- Anlatım, sözcük, altyazı dosyası OKUNMAZ. `#altyazi` öğesi YOK (standart §6: kapakta altyazı yok).
- Renk yalnız `Y.RENK` anahtarlarıyla: `zemin #1b1a17`, `murekkep #f3efe6`, `ikincil #c9c2b3`, `vurgu #f2a93b`. Başka hex YOK.
- Bant sabitleri: `ICERIK_SOL 60 · ICERIK_SAG 960 · ICERIK_UST 460 · ICERIK_ALT 1380 · UST_BOS 280 · MERKEZ_X 510`.

## 4. Yerleşim (px; y = yazı tabanı; açık tema görünümü)

```
y    0 ┌──────────────────────────────────────────┬────┐
       │ (boş zemin)                               │    │
   291 │ [logo 193,5×48] @ydspublishing            │    │ kanal katmanı, kimlik kanal (kunye içinde)
   386 │                          (YDT · BASIC)     │    │ yalnız rozet, kapak A son konumu (x ≈ 664,6)
   591 │ NEDEN -ING                                │    │ Fredoka 700 S (≈164), merkez x 510, kontur
   617 │       (    YOK?    )                      │    │ sarı hap y 617–781, merkez x 510
   874 │  ◯saat       ?(sarı)    ┌karakter───┐     │    │ karakter: görünür üst 820, sağ 948 (+10 kenar)
  1018 │ ┌──────┐┌──┐  duman    │ krem daire│     │    │ (açık temada arkasında krem daire)
  1176 │ ══════════════ ray      └───────────┘     │    │ karakter alt ≈ 1227 (+10 kenar)
  1254 │ ┌──────────────────────────┐              │    │
  1341 │ │ The train leaves …       │              │    │ kart: Fredoka 700 72; leaves altında sarı altçizgi
  1378 │ └──────────────────────────┘              │    │
  1380 ├──────────────────────────────────────────┤    │ 1380–1920 BOŞ (altyazı yok)
       └──────────────────────────────────────────┴────┘ x 960–1080 içerik yok
```

### 4.1 Kanal katmanı + rozet — `<g id="kunye">` (01 `_kunye_svg` kalıbı)
- `<g id="kanal">`: `<image id="logoimg" href="assets/logo.svg" x=LOGO_X y="291" width=LOGO_W height="48"/>` +
  `<text id="kanal-ad" x="263" y="330" font-family="Lexend" font-weight="700" font-size="42" fill=murekkep>@ydspublishing</text>`.
  `LOGO_W = 48 · Y.LOGO_EN_BOY` (≈ 193,49), `LOGO_X = 60 − Y.LOGO_KAYMA · LOGO_W` (≈ 53,15). Opaklık 1; animasyon YOK.
- `<g id="rz0">`: `KONU = "Simple Present vs Present Continuous"` YALNIZ ölçü içindir, ekrana YAZILMAZ. `ROZET = "YDT · BASIC"`,
  `ROZET_W = genislik("Lexend", 700, ROZET, 26) + 40`. `KB_K` = 34'ten 28'e inen ilk boy: `60 + genislik("Fredoka", 700, KONU, k) + 20 + ROZET_W ≤ 960`.
  `ROZET_X = 60 + genislik("Fredoka", 700, KONU, KB_K) + 20` (beklenen KB_K 34, ROZET_X ≈ 664,6, ROZET_W ≈ 203,6).
  `<rect x=ROZET_X y="386" width=ROZET_W height="48" rx="24" fill=vurgu/>` + `<text x=ROZET_X+ROZET_W/2 y="419.4" text-anchor="middle"
  font-family="Lexend" font-weight="700" font-size="26" fill=zemin>YDT · BASIC</text>`.
- Grup: `<g id="kunye">{kanal}{rz0}</g>`. Konu metni, çip, ikinci rozet YOK.

### 4.2 Başlık — `<g id="baslik">`
- Satır 1 `NEDEN -ING` (elle büyük harf; `I` = Latin U+0049; `text-transform` YOK). Satır 2 `YOK?` sarı hapta. İki satır aynı boy S.
- Boy: `g1_100 = genislik("Fredoka", 700, "NEDEN -ING", 100)`, `g2_100 = genislik(…, "YOK?", 100)`.
  `S = floor(min(170, 900·100/g1_100, 900·100/(g2_100 + 60)))`. S ile yeniden ölç; `g1 > 900` ya da `g2 + 0,60·S > 900` ise S'i 1'er azalt
  (v1 satır 66–69 kalıbı). Beklenen S = 164.
- Konum (merkez x 510):
  - `T1 = 476 + 0,70·S` (≈ 590,8); `x1 = 510 − g1/2` (≈ 61,7); assert `x1 ≥ 60`.
  - Hap: `p = 0,30·S`; `hap_x = 510 − g2/2 − p`; `hap_w = g2 + 2p`; `hap_y = T1 + 0,16·S` (≈ 617,0); `hap_h = S`; `rx = S/2`.
  - `T2 = hap_y + 0,85·S` (≈ 756,4); `x2 = 510 − g2/2`.
- `<text id="bs-1">`: x1, T1, Fredoka 700 S, `fill` murekkep, `stroke` zemin, `stroke-width` 12, `stroke-linejoin="round"`,
  `style="font-kerning:none;paint-order:stroke fill"`, `xml:space="preserve"` (v1 satır 270–274 aynen).
- `<rect id="bk-hap">` önce, `<text id="bs-2">` sonra: x2, T2, Fredoka 700 S, `fill` zemin, KONTURSUZ, `style="font-kerning:none"`.
- Başlıkta başka renk, altçizgi, ikinci hap YOK.

### 4.3 Sol sütun — `<g id="eskiz" fill="none" stroke=murekkep stroke-linecap="round" stroke-linejoin="round">`
İçerik yalnız `tren_svg(TX0, TY0, K_TREN)` + `saat_svg(SC, SR)` (v1 işlevleri aynen). `zc`, figür, kalem oku YOK.

| Öğe | Değer |
|---|---|
| tren | `K_TREN = 1.05` · `TX0 = 64 + 10·K_TREN + 2` (= 76,5) · `TY0 = 1010` · `RAY_Y = TY0 + 158·K_TREN` (≈ 1175,9). Lokomotif sağda |
| saat | `SC = (TX0 + 87,5·K_TREN, 934)` · `SR = 56`. Akrep 7'de, yelkovan 12'de, ikisi de murekkep. Rakam YOK |

### 4.4 Soru işareti — `soru_svg(SX0, SY0, SH)` (eskiz DIŞINDA, v1 işlevi aynen)
`SH = 112` · `SY0 = 880` · `SCX = TX0 + 237,5·K_TREN` (kabin üstü) · `SX0 = SCX − 0,31·SH`. `stroke` vurgu.

### 4.5 Kart — `kart_svg` (eskiz DIŞINDA; v1 satır 229–238 kalıbı, YENİ koordinatlar)
- Metin `The train leaves …` (sonda boşluk + U+2026). `KB = 72`. `metin_w = genislik("Fredoka", 700, metin, 72)`; `KW = metin_w + 80` (≈ 688,6).
- `<rect id="kart" x="62" y="1256" width=KW height="120" rx="28" fill="none" stroke=murekkep stroke-width="4"/>` (dış kenar 60–KW+64, 1254–1378).
- `<text id="kart-yazi" x="102" y="1341">` Fredoka 700 72, `fill` murekkep, kontursuz, `style="font-kerning:none"`, `xml:space="preserve"`.
- Altçizgi (`leaves`): `LX = 102 + genislik(…, "The train ", 72)`, `LW = genislik(…, "leaves", 72)`.
  `<path id="alti" d="M{LX−4} 1358 Q{LX+LW/2} 1364 {LX+LW+4} 1355" fill="none" stroke=vurgu stroke-width="10" stroke-linecap="round"/>`.
- Kartta başka vurgu YOK.

### 4.6 Karakter görseli — HTML `<img id="karakter">` (svg DIŞINDA)
- `karakter_hazirla(hedef: Path) -> tuple[int, int, int, int]`: `PAKET/ortak/kapak/karakter.png` aç; boyut (896, 1200) ve RGBA assert.
  90-kapak `gorsel_kopyala` kırıntı temizliği (alfa ≤ 64 → 0; 3×3 Min sonra Max süzgeci; alfa ile çarp). Temiz alfanın `getbbox()` kutusu
  `(bx0, by0, bx1, by1)` (beklenen ≈ 21, 173, 878, 1112). Kutuya kırp; `D/proje/assets/karakter.png` olarak kaydet. Kaynak dosya DEĞİŞMEZ.
- Ölçek: `SK = 520 / 1200` (dosya kutusu yüksekliği 520; görünür yükseklik ≈ 406). `KW_K = (bx1 − bx0)·SK`, `KH_K = (by1 − by0)·SK`.
- Konum: `KX = 948 − KW_K` (görünür sağ 948; kenarla 958 ≤ 960), `KY = 820`.
- `<img id="karakter" class="abs kenar" src="assets/karakter.png" alt="" style="left:{KX:.1f}px;top:{KY:.1f}px;width:{KW_K:.1f}px;height:{KH_K:.1f}px">`.
- Çıkartma kenarı: CSS `.kenar{filter: …}` — 90-kapak satır 295–298 kalıbı: `KENAR_PX = 10`, `KENAR_GECIS = 3`, adım `10/3` px,
  4 yön × 3 geçiş = 12 `drop-shadow(dx dy 0 #f3efe6)`. Renk yalnız `<style>` içinde.

### 4.7 Krem daire — `<div id="daire">` (yalnız açık tema)
- Merkez yüz ortası: `DX = KX + (461 − bx0)·SK`, `DY = KY + (470 − by0)·SK` (90-kapak `YUZ_PNG`).
- `DR = min(0,36·KH_K, DY − (baslik_alt + 16), 960 − DX)`; `baslik_alt = hap_y + hap_h`.
- `<div id="daire" class="abs" style="left:{DX−DR:.1f}px;top:{DY−DR:.1f}px;width:{2·DR:.1f}px;height:{2·DR:.1f}px"></div>`.
- CSS: `#daire{display:none;border-radius:50%;background:#f3efe6;}` · `.tema-acik #daire{display:block;}`.
  **DİKKAT:** `#root.tema-acik` dizgisi uret.py çıktısında YASAK: `ortak/hf_tema.py` onu "tema CSS'i var" sayar, açık tema koyu çıkar
  (sözleşme satır 75, 79). Assert: `"#root.tema-acik" not in html`.
  `<circle>` KULLANMA (hf_tema `[fill="#f3efe6"]` kuralı açık temada daireyi laciverte çevirir).

### 4.8 HTML sırası ve tema
- `#root` içinde sıra: `Y.zemin_html()` → `#daire` → `#karakter` → `<svg id="sahne">` (`{kunye}{baslik}{eskiz}{soru}{kart}`).
- `<style>`: `Y.font_css()`, `Y.ZEMIN_CSS` (DEĞİŞTİRME; hf_tema bu metni arar), `#sahne{position:absolute;left:0;top:0;}`, `.kenar{…}`, daire kuralları.
- SVG renkleri öznitelik, küçük harf hex. hf_tema açık temada: `rect fill vurgu → #ffe066` (rozet, hap) · `text fill zemin → #1b2440`
  (rozet yazısı, `YOK?`) · `stroke vurgu → #d9900f` (`?`, altçizgi) · `murekkep → #1b2440` · `stroke zemin → zemin` (başlık konturu).
- id `t2`, `ku-nokta`, `rz1`, `altyazi` KULLANMA.
- Çizelge: v1 satır 644–653 aynen (tek `set`, hareket yok).

## 5. Bloklar ve kurallar (uret.py içinde `assert`)

### 5.1 Blok kutuları (`nesneler.json` sırası, 13 blok)
| Ad | Kutu (x, y, w, h) |
|---|---|
| `kanal` | (LOGO_X, 291, 263 + genislik("Lexend", 700, "@ydspublishing", 42) − LOGO_X, 48) |
| `rozet` | (ROZET_X, 386, ROZET_W, 48) |
| `baslik` | x `min(x1 − 6, hap_x)` → `max(x1 + g1 + 6, hap_x + hap_w)`; y `T1 − 0,70·S − 6` → `hap_y + hap_h` |
| `bk-hap` | (hap_x, hap_y, hap_w, hap_h) |
| `saat` | `SC ± (1,02·SR + 2,5)` |
| `soru` | (SX0 − 6, SY0 − 6, 0,62·SH + 12, 0,92·SH + 14) |
| `duman` | v1 satır 374–380 formülü (yeni K_TREN, TX0, TY0) |
| `tren` | v1 satır 382–388 formülü |
| `kart` | (60, 1254, KW + 4, 124) |
| `kart-yazi` | (102, 1341 − 0,75·72, metin_w, 72) |
| `alti` | (LX − 9, 1350, LW + 18, 19) |
| `karakter` | (KX − 10, KY − 10, KW_K + 20, KH_K + 20) — çıkartma kenarı dahil |
| `daire` | (DX − DR, DY − DR, 2·DR, 2·DR) |

### 5.2 Kurallar
1. Bant: her blok `y ≥ 280`, alt `≤ 1380`, sağ `≤ 960`; `kanal` dışındaki her blok `x ≥ 60` (`kanal` resim kutusu 53,15'ten başlar).
   `baslik` ve sahne blokları (`saat, soru, duman, tren, kart, karakter, daire`) `y ≥ 460`. 0–280 ve 1380–1920 arasında öğe YOK.
2. Kesişim 0: `kanal, rozet, baslik, saat, soru, duman, tren, kart, karakter` çiftleri (yalnız `duman–tren` hariç).
   `daire` bunların hepsiyle 0, yalnız `karakter` hariç. Kapsama: `bk-hap ⊂ baslik`; `kart-yazi ⊂ kart`; `alti ⊂ kart`.
3. Boşluk: kanal alt → rozet üst ≥ 40 · rozet alt → başlık üst ≥ 24 · başlık alt → karakter üst ≥ 24 · başlık alt → `saat`, `soru`,
   `duman` üst ≥ 48 · saat alt ve soru alt → tren üst ≥ 16 · tren alt → kart üst ≥ 20 · karakter alt → kart üst ≥ 16 ·
   karakter sol − max(tren sağ, duman sağ) ≥ 24 · soru sağ → duman sol ≥ 24 · saat sağ → soru sol ≥ 24 · `DR ≥ 100`.
4. Yazı boyu: S ≥ 64, KB = 72 (kanal 42 ve rozet 26 standart §2 ölçüsü, kapsam dışı). Başlık 2 satır, 3 sözcük. Her satır ≤ 24 karakter:
   `@ydspublishing`, `YDT · BASIC`, `NEDEN -ING`, `YOK?`, `The train leaves …`. Başlıkta `İ` YOK; `-ING` içinde U+0049 VAR.
5. Zorunlu (html içinde): `id="kunye"`, `id="kanal"`, `@ydspublishing`, `assets/logo.svg`, `id="karakter"`, `assets/karakter.png`,
   `id="daire"`, `drop-shadow`. `id="kanal"` öğesi `id="kunye"` grubunun içinde.
6. Yasak (html küçük harfe çevrilip aranır): `tam ders`, `dakika`, `qr`, `izle`, `tarife`, `timetable`, `6 dk`, `simple present`,
   `text-transform`, `math.random`, `date.now`, `new date`, `opacity:0`, `<circle`, `altyazi`. `id="t2"`, `id="ku-nokta"`, `id="rz1"` YOK.
   (v1 listesindeki `kanal` sözcüğü ÇIKAR: kanal katmanı artık zorunlu.) 6 haneli hex kümesi ⊆ {`#1b1a17`, `#f3efe6`, `#c9c2b3`, `#f2a93b`}.
   Yeşil, kırmızı, gradyan (zemin vinyeti hariç), emoji YOK. try/catch YOK.
7. Python: bütün işlevlerde tür ipuçları. `/usr/bin/python3 uret.py` stdout: `index.html yazıldı <bayt>` ve
   `S=<S> KW=<KW> KB_K=<KB_K> karakter=<KX>,<KY>,<KW_K>,<KH_K> daire r=<DR>`. Hata yoksa çıkış 0.

## 6. Olay listesi (durağan kare)

| Olay | Kare / sn | Cümle · sözcük |
|---|---|---|
| bütün öğeler tam görünür (tek `set`) | kare 0; yakalama 0,5 sn (`zamanlar.json` `yakala_sn`) | yok (ses yok, zaman çizelgesi dışı) |

`olaylar.json` boş liste (`olay.py`). Ekran metni: `@ydspublishing` · `YDT · BASIC` · `NEDEN -ING` · `YOK?` · `The train leaves …`. Başka metin YOK.

## 7. Kabul (şef koşturur, ajan koşturmaz)
`/usr/bin/python3 D/uret.py` çıkış 0 · `bash calistir.sh --tema acik` → `P/kapak-b.png` · `bash calistir.sh --tema koyu` →
`D/k/koyu/kapak-b-koyu.png`; ikisi 1080×1920. Kanal katmanı x 60, y 291–339 görünür. Taşma, kesik yazı, üst üste binme yok.
Karakter ile kart ayrık; karakter sağ kenarı (kenar dahil) ≤ 960; 0–280 ve 1380–1920 boş.
