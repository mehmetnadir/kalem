# İstem P1-dikey — 02-04-ydt-temel-dikey paket iskeleti + BRIEF-DIKEY + sahne istemleri · 15.11.2026

MAKİNE: Linux x86_64 (srv21), kullanıcı sef. K=`/home/sef/01dev/_worktrees/kalem-0204` (git worktree, dal `sunucu/02-04-ydt-temel`),
D=`/home/sef/01dev/dijital-anlatim`. Python `/usr/bin/python3 -I`. Node `~/.nvm/versions/node/v24.22.2/bin`.
Skill `~/.claude/skills/motion-grafik-ders/`.
KURALLAR: Yalnız isteneni yaz. Silme yok (`~/Silinecekler/2026-11-15-0204/` altına taşı). Ses sentezi yok, render yok, sahne kodu
yok (sahneler sonraki adım). git commit yok. Yazma yalnız `K/projeler/02-04-ydt-temel-dikey/` altında.
Nadir 15.11: "bu video için burada görünenlerin hepsini istiyorum" → dikey 9:16 tam ders (açık + koyu) üretilecek.

## Kural kaynağı (önce oku)
1. Nadir 04.11 ONAYLI: dikey = yatayla AYNI anlatım ve AYNI ses; sahne düzeni dikey için SIFIRDAN tasarlanır; döndürülmüş ya da
   responsive yatay YASAK. Tek kaynak: `K/projeler/present-continuous-dikey/BRIEF-DIKEY.md` §0 (Nadir'in dikey bulguları), §2–§3 (HUD,
   bantlar, ölçek). Bunlar düzeltilmiş olmalı.
2. Yapı örneği (en yakın): `K/projeler/simple-present-temel-dikey/` (BRIEF-DIKEY.md, zaman.json, ortak/, sahneler/). Yerleşim/ölçek
   oradan değil, present-continuous-dikey BRIEF'inden alınır.
3. Yatay ders (içerik kaynağı): `K/projeler/02-04-ydt-temel/` — BRIEF.md (14 sahnelik plan), zaman.json, ortak/anlatim/
   (senaryo.json, sozcukler.json, baslar.json, altyazi.json, METIN.md), uretim-tutanagi/senaryo-taslak.md, sahneler/*/RAPOR.md.
4. `D/.claude/docs/dikey-senaryo-kalibi.md` §3 (9:16 yerleşim, yazı tabanı 50 mantıksal px, satır ≤ 24 karakter, tek sütun).

## Adımlar
1. İskelet `projeler/02-04-ydt-temel-dikey/`, simple-present-temel-dikey ile aynı yapı:
   - `ortak/anlatim` → `../../02-04-ydt-temel/ortak/anlatim` sembolik bağ (aynı ses). `ortak/{cizim,font,hf_tema.py,logo}` bağları
     simple-present-temel-dikey ile aynı hedeflere. `ortak/{kalem-canvas.js,kunye.js,tema.sh,tema_damga.py}` simple-present-temel-dikey'den
     kopya (dikey v2 künye). Künye verisi (ders adı, rozet, ajanda/çip) 02-04'e uyarlanır: ders adı ve ajanda
     `K/projeler/02-04-ydt-temel/ortak/kunye.js` içinden okunur. Yatayda ajandada "Question" ve "Contrast" yoktu (sahne 06, 08, 09 raporu);
     dikey künyede bölüm çipi sahnenin kendi bölümünü göstersin.
   - `gorevler.json`, `yorumlar.json`, `harita-konum.json`: simple-present-temel-dikey'deki anlamıyla, 02-04-dikey kimliğiyle; eski içerik taşınmaz.
   - `surumler.json`: `K/projeler/present-continuous-dikey/surumler.json` biçiminde. `video.kimlik` = `02-04-ydt-temel`; tek sürüm
     `kimlik: "dikey-tam"`, `tur: "dikey"`, `ad: "Dikey tam ders (9:16, aynı ses)"`, `seviye: "temel"`, `kaynak: "ana-yatay"`,
     `durum: "uretimde"`, `onizleme: "/p/02-04-ydt-temel-dikey/onizle.html"`, `proje: "02-04-ydt-temel-dikey"`. Revizyon yok.
2. `zaman.json`: yatay `02-04-ydt-temel/zaman.json` ile AYNI sahneler, AYNI t_bas/t_son/kare/gecis; `genislik` 1080, `yukseklik` 1920.
   Klasör adları yatayla aynı (`01-hyperframes-giris` …); motor dikeyde daha uygun değilse aynı kalsın, değiştirirsen gerekçesini yaz.
3. `BRIEF-DIKEY.md`: simple-present-temel-dikey BRIEF-DIKEY biçiminde. §0 bulgular (present-continuous-dikey §0'a bağ), §1 teknik çerçeve
   (yollar, kare ↔ küresel saniye, `ortak/yakala.py … 1080 1920`, HyperFrames kökü `data-width="1080" data-height="1920"`), §2 bantlar ve
   HUD, §3 sahne planı tablosu: 14 satır (no, klasör, motor, küresel sn, kare, dikeyde ekranda NE var — yatay BRIEF ve raporlardan, tek sütun,
   en çok 1 örnek kart; altyazı + karaoke alt bantta, sessiz izleme varsayılır). Yatay raporlarındaki açık noktaları dikeyde tekrar etme
   (boş çerçeve 9+ sn bekletme yok; figür işaret pozu yoksa ok figürün eline/yanına; ajanda çipi doğru bölüm).
4. Sahne istemleri: `uretim-tutanagi/istem/sahne/D-<klasör>.md` × 14. Şablon `uretim-tutanagi/istem/D-dikey-sablon.md` (bu istemle
   birlikte sunucuya kondu: `~/is/uretim-0204/D-dikey-sablon.md`; önce paket içine kopyala). Yer tutucuları doldur: {SAHNE} klasör,
   {NO} sıra, {SATIR} BRIEF-DIKEY §3 satırının metni, {CUMLE} kapsadığı cümle numaraları, {TBAS}/{TSON} küresel saniye,
   {YATAY} yatay sahne yolu, {ORNEK} aynı motorlu dikey örnek sahne yolu (simple-present-temel-dikey ya da present-continuous-dikey içinden;
   motor eşleşmesi yoksa en yakını).
5. `uretim-tutanagi/P1-DIKEY-RAPOR.md`: yazılan dosyalar, sahne planı özeti, motor değişiklikleri, açık noktalar.

Doğrula: `python3 -I -c "import json;z=json.load(open('…/zaman.json'));print(z['genislik'],z['yukseklik'],len(z['sahneler']))"` → `1080 1920 14`;
`ls uretim-tutanagi/istem/sahne | wc -l` → 14; `readlink ortak/anlatim`.

Son mesajın en çok 12 satır: sahne sayısı, motor dağılımı, yazılan dosyalar, açık noktalar.
