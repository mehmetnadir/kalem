#!/usr/bin/python3 -I
"""YouTube yayın verisi adımı (YV) ve jürisi (YVJ) istemleri — ders başına bir çift.

Kullanım: /usr/bin/python3 -I yv-uret.py  → aynı dizine YV-<kod>.md, YVJ-<kod>.md yazar.
Sözleşme: dijital-anlatim/.claude/docs/youtube-yayin-verisi-sozlesme.md · ölçüt: juri-olcutleri.md §2f.
"""
from pathlib import Path

# kod, ders paketi
DERSLER = [
    ("0204T", "02-04-ydt-temel"),
    ("0202T", "simple-present-temel"),
    ("0201T", "present-continuous"),
    ("0201I", "present-continuous-ileri"),
    ("0202I", "simple-present-ileri"),
    ("0203T", "02-03-ydt-temel"),
    ("0206T", "present-perfect-temel"),
    ("0206I", "present-perfect-ileri"),
    ("0209T", "present-perfect-cont-temel"),
    ("0209I", "present-perfect-cont-ileri"),
    ("0210T", "simple-past-temel"),
    ("0210I", "simple-past-ileri"),
]

BAS = """MAKİNE: Linux x86_64 (srv21), kullanıcı sef. K=`/home/sef/01dev/_worktrees/kalem-0204` (worktree), D=`/home/sef/01dev/dijital-anlatim`.
Python `/usr/bin/python3 -I`. Skill `~/.claude/skills/motion-grafik-ders/` (önce "Bağlayıcı standartlar" bölümünü oku).
SABİT KURALLAR: Yalnız isteneni yaz. Silme yok (`rm` yok). mp4 RENDER YOK, ses sentezi yok, sahne kodu yok. git commit yok, alt ajan yok,
agy-filo yok, ayna yüklemesi yok. Kanca atlama bayrağı oluşturma (`/tmp/conductor-*`, `~/.conductor/*`); sözleşme kancası isterse
`K/.claude/docs/sozlesme.md` dosyasına 1 satır ekle. Arka plan işi beklerken `pgrep -f` kullanma. Jeton ya da anahtar değeri yazma, `.env` okuma."""

YV = """# İstem YV-{kod} — `{paket}`: YouTube yayın verisi (başlık, açıklama, bölümler, etiket, liste, gönderi, bildirim anları) · 15.11.2026

{bas}
YAZMA ALANI: `K/projeler/{paket}/youtube.json`, `K/projeler/{paket}/youtube-aciklama.md`, `K/projeler/{paket}/uretim-tutanagi/YV-RAPOR.md`
ve dersin uzun dikey paketi varsa (`K/projeler/{paket}-dikey/` ya da `surumler.json` içinde adı geçen dikey paket; yoksa "dikey paket yok" yaz)
onun içinde aynı iki dosya. Başka dosyaya dokunma.

## Amaç
Nadir (15.11): "Ürettiğimiz tüm derslerin YouTube'da etiketlenmesi için API'ye her türlü bilgiyi vermemiz gerekiyor. Takvim uygulaması YouTube'a
listeler, etiketler, shortlar, gönderiler paylaşırken bunları kullanabilmeli." Bütün dersler YouTube'a AÇIK tema ile yüklenir (uzun yatay + uzun
dikey). Panel bu dosyaları okur ve takvim uygulamasına API ile verir. Sen bu dersin verisini yazarsın.

## Okuma
1. BAĞLAYICI: `D/.claude/docs/youtube-yayin-verisi-sozlesme.md` (tamamı), `D/.claude/docs/youtube-surumu-standart.md` §3 (bildirim kuralları),
   `D/.claude/docs/juri-olcutleri.md` §1 ve §2f (jüri bu maddelere bakacak), `D/.claude/docs/huni-v2-standart.md` (açıklama dili ve utm kuralı).
2. Ders: `K/projeler/{paket}/` → `ortak/anlatim/senaryo.json` (başlık, cümleler), `zaman.json` (sahneler, `bolum`, süreler), cümle başları dosyası,
   `ortak/anlatim/altyazi.json`, `surumler.json` (`video.etiketler`, sürümler), `ortak/kunye*`. Kısaları: `K/projeler/{paket}-s1` … (başlık ve
   açıklama dili emsali; bağlantı tabanı ve utm biçimi oradan).
3. Katalog: `D/varlik/grammar/katalog.json` (ünite adı, konu sırası, önceki ve sonraki ders).

## Yaz
1. `youtube.json` (JSON'u yazdıktan sonra ayrıştırarak doğrula):
   - `baslik`: ≤ 100 karakter; kalıp `<Konu> | <kitle> İngilizce` (kitle künyeden: YDT). Konu adı dersin gerçek konusu; abartı yok.
   - `etiketler`: `surumler.json` etiketleri + eksikse konu adı, zaman adları, kitle, "İngilizce", "gramer"; toplam ≤ 500 karakter; yineleme yok.
   - `bolumler`: `[{{"t": <sn>, "ad": "…"}}]`; ilk `t` 0; en az 3 bölüm; her bölüm ≥ 10 sn (kısa sahneyi öncekiyle birleştir); `t` sahne başlangıcı
     (`zaman.json`). `ad` İZLEYİCİ dilinde ve içeriği söyler ("Aynı fiil, iki zaman: wear"); iç ad ("Örnek 1", "Karşıt çift 1") YASAK; ≤ 40 karakter.
   - `sabitYorum`: tek cümle (kaydet teşviki + bölüm damgalarına işaret).
   - `gonderiler`: en az 1 `{{"kimlik": "g1", "metin": "…", "gorsel": "<dersin açık tema kapak dosyası; surumler.json'daki adıyla>"}}`; metin 2–3 kısa
     cümle, bir soru ile başlar, emoji yok. Yeni görsel ÜRETME.
   - `liste`: `{{"ad": "<Ünite> · <kitle> <seviye>", "sira": <katalog sırası>, "onceki": "<öğe kimliği ya da null>", "sonraki": "<…>"}}`.
   - `bildirimler`: `[{{"t": <ders zamanı sn>, "sure": 3.0}}]`; ders < 4 dk ise 1 (≈ %30), ≥ 4 dk ise 2 (≈ %30 ve ≈ %70); her biri bir CÜMLE
     SINIRINDA (cümle başları dosyasından; söz ortasında değil); ilk 30 sn ve son 20 sn içinde olamaz. `"giris": true, "cikis": true`.
   - `aciklamaDosya`: `"youtube-aciklama.md"`.
2. `youtube-aciklama.md` (≤ 5.000 bayt; düz metin, YouTube açıklamasına aynen yapışır): ilk satır değer cümlesi (ders ne kazandırır; mutlak kural yok)
   · kaydet satırı · bölüm damgaları (`MM:SS Ad`, `youtube.json` ile birebir; not satırı: "giriş klibi eklenirse damgalar kayar, araç düzeltir" YAZMA,
   bu rapora girer) · sıradaki ders adı · bağlantı (kısaların açıklamasındaki taban adres; `utm_source=youtube&utm_medium=video&utm_campaign=<ders
   kodu, kısalardaki yazımla>&utm_content=ana-yatay`) · son satır etiketler (`#…`, en çok 5). Kısaltma ve yazım denetimi yap.
3. Dikey paket varsa: aynı `baslik`, `etiketler`, `sabitYorum`, `gonderiler`, `liste`; `bolumler` ve `bildirimler` dikey paketin KENDİ `zaman.json`
   dosyasından; açıklamada `utm_content=dikey-tam`.
4. Öz denetim (`YV-RAPOR.md`): `juri-olcutleri.md` §2f her madde için evet/hayır + kanıt (karakter ve bayt sayımları komut çıktısıyla); bölüm tablosu
   (iç ad → izleyici adı → süre); bildirim anlarının hangi cümle sınırına denk geldiği; dilbilgisi iddiası içeren her cümle için "kesin / jüri
   bakacak"; açık noktalar; üretici modelin adı.

Son mesajın en çok 10 satır: başlık, bölüm sayısı, etiket karakter toplamı, açıklama baytı, bildirim anları, dikey paket var mı, emin olmadığın nokta.
"""

YVJ = """# İstem YVJ-{kod} — `{paket}` YouTube yayın verisi ÇIKTI jürisi · 15.11.2026

{bas}
YAZMA ALANI: yalnız `K/projeler/{paket}/uretim-tutanagi/juri/YVJ-hukum.md` (dizini aç).

## Jüri kuralları (`D/.claude/docs/juri-olcutleri.md` §1 bağlayıcıdır)
- Sen JÜRİSİN: hiçbir üretim dosyasını DEĞİŞTİRME. ÇIKTIYA bak: `youtube.json`, `youtube-aciklama.md` (ve dikey paketteki eşleri), dersin
  `senaryo.json`, `zaman.json`, cümle başları, katalog.
- Sayıları KENDİN ölç (karakter, bayt, süre farkları; salt okuma komutları); üreticinin raporuna güvenme.
- "Kaynağa uygun" ile "doğru" ayrı: başlık, açıklama, bölüm adı, sabit yorum ve gönderi metnindeki her dilbilgisi iddiasını bağımsız doğrula
  (mutlak kural, yanlış denklik, doğru cümleyi yanlış gösterme yok). Bölüm adı o bölümde gerçekten anlatılanı mı söylüyor: senaryodan denetle.
- Her madde: kimlik | hüküm (evet / hayır / kanıt yok) | kanıt | not. "Hayır" ve "kanıt yok" = kaldı. Kendi model adını ilk satıra yaz; üretici
  modelle aynıysa büyük harfle bildir.

## İş
`juri-olcutleri.md` §2f (YV-1 … YV-9) BÜTÜN maddelerine ve `youtube-surumu-standart.md` §3 bildirim kurallarına (sayı, zaman, cümle sınırı, ilk 30 sn /
son 20 sn) hüküm ver. Hüküm dosyası: özet, madde tablosu, kaldı maddeleri için düzeltme önerisi (tek cümle; önerilen yeni metinle).

Son mesajın en çok 10 satır: geçti / kaldı / kanıt yok sayıları, kaldı maddeleri (kimlik + tek cümle), jüri modeli ↔ üretici modeli.
"""

hedef = Path(__file__).resolve().parent
for kod, paket in DERSLER:
    (hedef / f"YV-{kod}.md").write_text(YV.format(kod=kod, paket=paket, bas=BAS), encoding="utf-8")
    (hedef / f"YVJ-{kod}.md").write_text(YVJ.format(kod=kod, paket=paket, bas=BAS), encoding="utf-8")
print(len(DERSLER) * 2, "istem:", hedef)
