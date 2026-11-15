#!/usr/bin/python3 -I
"""A/B kol b üretim (KBC), kol b jürisi (KBJ) ve var olan kısaların çıktı jürisi (J2) istemleri.

Kullanım: /usr/bin/python3 -I kbc-uret.py  → aynı dizine KBC-<kod>.md, KBJ-<kod>.md, J2-<kod>.md yazar.
Ölçütlerin tek otoritesi: dijital-anlatim/.claude/docs/juri-olcutleri.md (istem yalnız yolunu anar).
"""
from pathlib import Path

# kod, kol a paketi, ana ders paketi, değişken
KISALAR = [
    ("0204S1", "02-04-ydt-temel-s1", "02-04-ydt-temel", "kanca"),
    ("0204S2", "02-04-ydt-temel-s2", "02-04-ydt-temel", "kapanis"),
    ("0204S3", "02-04-ydt-temel-s3", "02-04-ydt-temel", "kanca"),
    ("0202S1", "simple-present-temel-s1", "simple-present-temel", "kanca"),
    ("0202S2", "simple-present-temel-s2", "simple-present-temel", "kapanis"),
    ("0202S3", "simple-present-temel-s3", "simple-present-temel", "kanca"),
]

BAS = """MAKİNE: Linux x86_64 (srv21), kullanıcı sef. K=`/home/sef/01dev/_worktrees/kalem-0204` (worktree), D=`/home/sef/01dev/dijital-anlatim`.
Python `/usr/bin/python3 -I`. Skill `~/.claude/skills/motion-grafik-ders/` (önce "Bağlayıcı standartlar" bölümünü oku).
SABİT KURALLAR: Yalnız isteneni yaz. Silme yok (`rm` yok; gerekirse `~/Silinecekler/2026-11-15-kol-b/` altına taşı). mp4 RENDER YOK.
git commit yok, alt ajan yok, agy-filo yok, ayna yüklemesi yok. Kanca atlama bayrağı oluşturma (`/tmp/conductor-*`, `~/.conductor/*`); sözleşme
kancası isterse `K/.claude/docs/sozlesme.md` dosyasına 1 satır ekle. Arka plan işi beklerken `pgrep -f` kullanma; komutu ön planda `timeout` ile
koştur. Jeton ya da anahtar değeri yazma, `.env` okuma (ses aracı kendi ortamını kendisi okur)."""

KBC = """# İstem KBC-{kod} — `{paket}b`: A/B deneme kolu paketi (ses + zaman + değişen sahneler + kapı) · değişken: {degisken} · 15.11.2026

{bas}
YAZMA ALANI: `K/projeler/{paket}b/` (tamamı) ve `K/projeler/{paket}/surumler.json` içinde YALNIZ kısa satırına `varyant` alanı eklemek.

## Amaç
Kısa videoda A/B testi: aynı konunun iki kolu yayınlanır. Kol a = var olan `{paket}`. Sen kol b paketini (`{paket}b`) taslaktan ÜRETİRSİN.
İki kol arasında TEK değişken değişir (`{degisken}`); gerisi bayt düzeyinde aynıdır. Fark kanıtı bu işin kabul ölçütüdür.

## Okuma
1. BAĞLAYICI: `D/.claude/docs/huni-ab-sozlesme.md` (tamamı), `D/.claude/docs/huni-v2-standart.md`, `D/.claude/docs/juri-olcutleri.md` (§1, §2a, §2d:
   jüri bu maddelere bakacak; üretirken sen de bak).
2. Taslak (onaylı): `K/projeler/{paket}b/uretim-tutanagi/` → `senaryo-taslak.md`, `kol-b.json`, `kapak-taslak.md` (varsa), `BK-RAPOR.md`.
3. Yöntem emsali (ses önbelleği, Whisper kapısı, zaman, sahne QA, kanal katmanı): `K/uretim-hatti/istemler/V2-S1-C.md` ve kol a'nın
   `K/projeler/{paket}/uretim-tutanagi/` içindeki C aşaması raporu. Ana ders: `K/projeler/{ders}/`.

## Adımlar
1. Paket = kol a'nın KOPYASI. Simge bağı KULLANMA (panel yüklemesi bağı reddeder; sözleşme §4 bu yönde düzeltildi). `cp -a` ile kol a içeriğini
   `{paket}b/` altına kopyala; `uretim-tutanagi/` HARİÇ (kol b'nin kendi tutanağı kalır). Git dışı varlıklar (wav, m4a, `gsap.min.js`, yazı tipi,
   png) da kopyalanır. Kopyadan sonra iki pakette dosya sayısını ve git dışı varlıkların sha256 eşitliğini raporla.
2. `ortak/anlatim/senaryo.json`: yalnız taslaktaki değişen cümleler. Başka cümle, kadro, ses kimliği değişmez.
3. Ses: yalnız YENİ cümleler sentezlenir (dersin ses zinciri, önbellek anahtarı kuralı). Değişmeyen cümlelerin ses dosyası kol a ile aynı sha256
   olmalı (tablo yaz). Whisper benzerliği ≥ 0,90. İlk söz ≤ 1,0 sn. Marka söylenişi sözlükten ("YeDeSe").
4. `zaman.json` ve türevleri (cümle başları, altyazı, süreler) yeniden üret. Toplam süre ≤ 35 sn (hedef 22–26).
5. Yalnız `kol-b.json` `degisen_sahneler` listesindeki sahneler yeniden üretilir (yeni söz ve yeni süreye göre). Değişken `kanca` ise A kapağı
   (`kapak-a.png`) da yeniden üretilir (kanca karesi). Değişmeyen sahne klasörlerinin `proje/` içeriği kol a ile bayt bayt aynı kalır.
   Kanal katmanı her karede aynı pikselde. Emoji yok; simge SVG. "Tam ders" ve süre sözü hiçbir yüzeyde yok.
6. `surumler.json` (kol b): kısa sürüm kimliği `s<N>b`; `varyant: {{"grup": "s<N>", "kol": "b", "degisken": "{degisken}", "deger": "<değer>"}}`.
   `deger` yalnız `[a-z0-9-]`: kanca için `soru` | `yanlis-cumle` | `kopru`; kapanış için `ekran-goruntusu`. Değişken `kanca` ise kapak A satırı
   `s<N>b-kapak-a`; öteki türev satırları (kapak B/C, hikâye) gruba aittir, kol b'de yinelenmez (satırları ve kopyalanmış dosyalarını çıkar:
   dosyaları `~/Silinecekler/2026-11-15-kol-b/{paket}b/` altına taşı). Açıklama dosyaları kol b'de kalır; içlerinde YALNIZ `utm_content` değişir
   (`s<N>b-a`, `s<N>b-b`). Kol a `surumler.json` kısa satırına `varyant: {{"grup": "s<N>", "kol": "a", "degisken": "{degisken}", "deger":
   "<kol a değeri>"}}` ekle (kanca: `kol-b.json` `kol_a_deger`; kapanış: `kaydet`); kol a'da başka hiçbir şeye dokunma. İki JSON'u ayrıştırarak doğrula.
7. Tek değişken kanıtı: `diff -rq K/projeler/{paket} K/projeler/{paket}b` çıktısının HER satırını sınıfla. Beklenen: değişen sahne klasörleri, senaryo ve
   zaman türevleri, yeni ses dosyaları, `surumler.json`, açıklamalarda utm, kapak A (kanca ise), çıkarılan grup türevleri, `uretim-tutanagi/`.
   Bunların dışındaki her fark HATADIR: düzelt ya da raporda "açık" diye yaz.
8. Kapı: `node araclar/cakisma-kapisi.mjs {paket}b --port 41333 --sunucu 41022` (meşgulse boş port seç) çıkış 0. QA kareleri: değişen her sahneden
   en az 2 an + ilk kare + son kare; emsaldeki temalarla. Kareleri Read ile kendin gör: taşma, çakışma, okunmayan yazı, kanal katmanı.
9. `uretim-tutanagi/KBC-RAPOR.md`: değişen dosyalar; ses tablosu (cümle, kaynak önbellek/yeni, sha256 kısaltması, Whisper); süreler (kol a ↔ kol b);
   diff sınıflama tablosu; kapı çıktısı; üretici modelin adı (jüri farklı modelle koşacak); açık noktalar.

"Çalışıyor" demeden önce kareye bak. Son mesajın en çok 12 satır: değer (a → b), süre (a → b), yeni sentezlenen cümle sayısı, Whisper en düşük,
diff'te beklenmeyen fark sayısı, kapı çıkış kodu, açık nokta.
"""

JURI_ORTAK = """## Jüri kuralları (D/.claude/docs/juri-olcutleri.md §1 bağlayıcıdır)
- Sen JÜRİSİN, üretici değilsin: hiçbir üretim dosyasını DEĞİŞTİRME. Tek yazacağın dosya hüküm dosyası.
- TASLAĞA değil ÇIKTIYA bak: son `ortak/anlatim/senaryo.json`, ses dökümü (Whisper metni: ses kapısı çıktıları; yoksa "kanıt yok" yaz),
  `zaman.json`, `surumler.json`, açıklama dosyaları (`aciklama*.md`), sahne HTML'leri ve KARELER (png). Her kareyi Read ile aç. Kare eksikse
  (kip, tema, kapak, hikâye) "kanıt yok → kaldı" yaz; var saymak yasak.
- "Kaynağa uygun" ile "doğru" ayrı: dilbilgisi iddiasını kendi bilginle bağımsız doğrula. Ana derste aynı hata varsa onu da yaz.
- Mutlak kural, yanlış denklik, doğru cümleyi yanlış diye gösterme, yazım hatası, kısaltma okunuşu, utm biçimi: açıkça ara.
- Her madde: kimlik | hüküm (evet / hayır / kanıt yok) | kanıt (dosya:satır ya da kare adı) | not. Kaçamak hüküm yok. "Hayır" ve "kanıt yok" = kaldı.
- Üretici oturumun modeli raporda yazılıdır (yoksa "bilinmiyor" yaz); kendi model adını hüküm dosyasının başına yaz. İkisi aynıysa bunu ilk
  satırda büyük harfle bildir."""

KBJ = """# İstem KBJ-{kod} — `{paket}b` (A/B kol b) çıktı jürisi · 15.11.2026

{bas}
YAZMA ALANI: yalnız `K/projeler/{paket}b/uretim-tutanagi/juri/KBJ-hukum-<GGAA-SSDD>.md` (ad şimdiki zamandan: `date +%d%m-%H%M`; dizini aç).
Var olan `KBJ-hukum*.md` dosyalarına DOKUNMA (juri-olcutleri §1b: önceki hüküm kalır, en son hüküm sayılır).

{juri}

## İş
0. Deterministik kapı (ÖNCE): `export PATH=$HOME/.nvm/versions/node/v24.22.2/bin:$PATH; node D/araclar/huni-kapi.mjs K/projeler/{paket}b --kol-a K/projeler/{paket}` koş; çıktının tamamını hüküm dosyasına `## Deterministik kapı` başlığıyla koy. Kapının KALDI dediği madde kaldıdır (kanıtı doğrula, yanlışsa `kapı hatası` diye yaz). GEÇTİ dediğini yeniden ölçme. ÖLÇÜLEMEDİ ve kapının kapsamadığı maddeleri kendin ölç.
   Düzeltme turu raporu varsa oku: `uretim-tutanagi/DUZ2-RAPOR.md`.
1. Oku: `D/.claude/docs/juri-olcutleri.md` (tamamı), `D/.claude/docs/huni-ab-sozlesme.md`, `D/.claude/docs/huni-v2-standart.md`.
2. Paket: `K/projeler/{paket}b/` (kol b) ve `K/projeler/{paket}/` (kol a); üretim raporu `uretim-tutanagi/KBC-RAPOR.md`.
3. §2a (kısa video) BÜTÜN maddelerine ve §2d (A/B kolu) BÜTÜN maddelerine hüküm ver. Tek değişken için `diff -rq` çıktısını KENDİN koştur ve
   üreticinin sınıflamasını denetle (salt okuma komutu).
4. İki kolu yan yana kıyasla: değişken dışında söz, ekran metni, kapak, açıklama farkı var mı?
5. Hüküm dosyası: özet (geçti / kaldı sayısı), madde tablosu, kaldı maddeleri için düzeltme önerisi (tek cümle), ana derse geri besleme.

Son mesajın en çok 10 satır: geçti / kaldı / kanıt yok sayıları, kaldı maddeleri (kimlik + tek cümle), jüri modeli ↔ üretici modeli.
"""

J2 = """# İstem J2-{kod} — `{paket}` (yayındaki kısa, kol a) ÇIKTI jürisi · 15.11.2026

{bas}
YAZMA ALANI: yalnız `K/projeler/{paket}/uretim-tutanagi/juri/J2-hukum-<GGAA-SSDD>.md` (ad şimdiki zamandan: `date +%d%m-%H%M`; dizini aç).
Var olan `J2-hukum*.md` dosyalarına DOKUNMA (juri-olcutleri §1b: önceki hüküm kalır, en son hüküm sayılır).

Neden: 15.11 denetimi eski jürinin taslağa baktığını, v2 çevirisinden sonra yeniden koşmadığını ve 22 kurala hiç bakmadığını buldu. Bu koşu
yayındaki paketi yeni ölçütlerle baştan denetler.

{juri}

## İş
0. Deterministik kapı (ÖNCE): `export PATH=$HOME/.nvm/versions/node/v24.22.2/bin:$PATH; node D/araclar/huni-kapi.mjs K/projeler/{paket}` koş; çıktının tamamını hüküm dosyasına `## Deterministik kapı` başlığıyla koy. Kapının KALDI dediği madde kaldıdır (kanıtı doğrula, yanlışsa `kapı hatası` diye yaz). GEÇTİ dediğini yeniden ölçme. ÖLÇÜLEMEDİ ve kapının kapsamadığı maddeleri kendin ölç.
   Düzeltme turu raporu varsa oku: `uretim-tutanagi/DUZ2-RAPOR.md`.
1. Oku: `D/.claude/docs/juri-olcutleri.md` (tamamı), `D/.claude/docs/huni-v2-standart.md`, `D/.claude/docs/kapak-standardi.md`.
2. Paket: `K/projeler/{paket}/`; ana ders `K/projeler/{ders}/` (yalnız kıyas için).
3. §2a (kısa video) ve §2c (kapak ve hikâye karesi) BÜTÜN maddelerine hüküm ver. Kapak A/B/C ve hikâye A/B karelerinin her birini aç.
4. Paketin son içerik değişikliği zamanını (`git log -1 --format=%cI -- projeler/{paket}`) ve eski jüri dosyalarının zamanını yaz.
5. Hüküm dosyası: özet, madde tablosu, kaldı maddeleri için düzeltme önerisi (tek cümle), ana derse geri besleme.

Son mesajın en çok 10 satır: geçti / kaldı / kanıt yok sayıları, kaldı maddeleri (kimlik + tek cümle), jüri modeli.
"""

hedef = Path(__file__).resolve().parent
for kod, paket, ders, degisken in KISALAR:
    ortak = dict(kod=kod, paket=paket, ders=ders, degisken=degisken, bas=BAS, juri=JURI_ORTAK)
    (hedef / f"KBC-{kod}.md").write_text(KBC.format(**ortak), encoding="utf-8")
    (hedef / f"KBJ-{kod}.md").write_text(KBJ.format(**ortak), encoding="utf-8")
    (hedef / f"J2-{kod}.md").write_text(J2.format(**ortak), encoding="utf-8")
    # 2. tur (düzeltme sonrası) aynı içerik, ayrı ad: durum dosyaları ilk turla karışmaz
    (hedef / f"KBJ3-{kod}.md").write_text(KBJ.format(**ortak), encoding="utf-8")
    (hedef / f"J3-{kod}.md").write_text(J2.format(**ortak), encoding="utf-8")
print(len(KISALAR) * 3, "istem:", hedef)
