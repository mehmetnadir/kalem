# İstem C — 02-04-ydt-temel paket iskeleti + senaryo.json + BRIEF (P1) · 14.11.2026

MAKİNE: Linux x86_64 (srv21), kullanıcı sef. K=`/home/sef/01dev/_worktrees/kalem-0204` (git worktree, dal `sunucu/02-04-ydt-temel`),
D=`/home/sef/01dev/dijital-anlatim`. Python `/usr/bin/python3 -I`. Skill `~/.claude/skills/motion-grafik-ders/`.
KURALLAR: Yalnız isteneni yaz. Silme yok (`~/Silinecekler/2026-11-14-0204/` altına taşı). Ses sentezi yok, ElevenLabs çağrısı yok,
render yok, sahne kodu yok (sahneler sonraki adım). git commit yok. Alt ajan açma. Yazma yalnız `K/projeler/02-04-ydt-temel/` altında.

Girdi (jüriden geçti): `K/projeler/02-04-ydt-temel/uretim-tutanagi/senaryo-taslak.md` + jüri dosyaları `uretim-tutanagi/juri/`.
Örnek paket (aynı hattın önceki dersi, birebir yapı): `K/projeler/02-03-ydt-temel/`.

## Adımlar

1. İskelet: `projeler/02-04-ydt-temel/` 02-03 ile aynı yapıda.
   - `ortak/` içindeki sembolik bağları aynı hedeflerle kur (`cizim`, `font`, `hf_tema.py`, `logo` → `../../present-continuous/ortak/…`).
   - `ortak/{kalem-canvas.js,kunye.js,tema.sh,tema_damga.py}` 02-03'ten kopyala.
   - `ortak/anlatim/` içine 02-03'ün yalnız `.py` betiklerini kopyala (veri dosyası, wav, m4a, json kopyalama).
   - `gorevler.json`, `surumler.json`, `yorumlar.json`, `harita-konum.json`: 02-03'teki anlamlarını oku, 02-04 kimliğiyle uyarla;
     02-03'e özgü içerik (yorum, görev geçmişi) taşıma. Anlamını çözemediğin alan varsa boş bırak ve raporla.
2. `ortak/anlatim/senaryo.json`: 02-03'ün `senaryo.json` şemasıyla birebir (ders, baslik, duzen "konu", seviye, kitle, sesler, cumleler[]{ses,
   parcalar:[[tr|en|sus, metin]…], olaylar varsa aynı biçimde}). Taslağın ses metnini kullan; ham sözcük yaz (IPA yazma; `ses_metni()`
   dönüşümü sentezde yapılır). Rakam yazma, sözcükle yaz. Öğrenci cümleleri `ses: "ogrenci"`.
   Doğrula: `/usr/bin/python3 -I -c "import json;d=json.load(open('…/senaryo.json'));print(len(d['cumleler']))"`.
3. `BRIEF.md`: 02-03 BRIEF'in bölüm yapısıyla — §0 künye, §1 kaynak (sunucu yolları: pptx `D/varlik/grammar/kaynak-pptx/YEDEK/Tenses/unit-1_sunum-3 uygun.pptx`,
   döküm `D/varlik/grammar/transkript-whisper/863572960.md`, taslak + jüri `uretim-tutanagi/`), görsel dil bağı, sahne planı tablosu
   (sahne no, klasör adı `NN-<motor>-<ad>`, motor HyperFrames / Paper.js / canvas, kapsadığı cümle numaraları, içerik, olaylar).
   Motor dağılımı ve sahne sayısı 02-03'e yakın olsun; sahne süreleri sentezden sonra hesaplanır (t değerleri "sentez sonrası").
4. `ortak/anlatim/zaman_uret.py` (ve sahne planını tutan başka betik varsa) içindeki sahne ↔ cümle eşlemesini 02-04 sahne planına
   göre güncelle. Betiği koşturma (girdisi sentezden sonra oluşur); yalnız `/usr/bin/python3 -I -m py_compile` ile derle.
5. `uretim-tutanagi/P1-RAPOR.md`: ne yazıldı, cümle sayısı, sahne planı özeti, uyarlanan dosyalar, açık noktalar.

6. `uretim-tutanagi/istem/A-girdi.md` künyesindeki döküm kapsamını jüri kararıyla eşitle (kaynak jürisi tur 1 madde 1: 00:00–03:14); başka satıra dokunma.

7. `uretim-tutanagi/juri.md`: 02-03'teki `juri.md` biçiminde kısa jüri özeti (tur 1: kaynak DÜZELT 2, kural GEÇTİ, dil DÜZELT 4+; tur 2: kaynak GEÇTİ, dil GEÇTİ; dosya bağları; dil jürisi koşulu: ses denemesinde wear, today, live dinlenir).

Son mesajın en çok 15 satır: cümle sayısı, sahne sayısı, yazılan dosyalar, açık noktalar.
