# İstem DUZ-{KOD} — `{PAKET}` (ve `{PAKET}-dikey`): düzeltme turu · kapsam `{KAPSAM}` · 16.11.2026

uretici_model satırı: raporun İLK satırı `uretici_model: <model>` olmak zorunda.

MAKİNE: Linux x86_64 (srv21), kullanıcı sef. K=`/home/sef/01dev/_worktrees/kalem-0204` (worktree), D=`/home/sef/01dev/dijital-anlatim`.
SABİT KURALLAR: silme yok (`rm` yok; eski dosya `/home/sef/Silinecekler/2026-11-16-duz-{KOD}/` altına taşınır). git commit yok (şef atar).
Alt ajan yok, agy-filo yok. `.env`, `*.key` okuma; anahtar ya da jeton yazdırma. Kanca atlama bayrağı oluşturma (bir kapı yazmayı engellerse
dur, sebebi ve hazır metnin yolunu raporla). Arka plan işi beklerken `pgrep -f` kullanma; komutu ön planda `timeout` ile koştur. Türkçe karakter tam.
Yalnız şu iki pakete yaz: `K/projeler/{PAKET}`, `K/projeler/{PAKET}-dikey` (dikey paket yoksa yalnız ilki).
Kısalara (`{PAKET}-s1` …), öteki derslere ve `K/ortak/` altına dokunma.

## YASAK ve SERBEST
- YASAK: mp4 üretimi, `ffmpeg`, `hyperframes render`; yeni görsel üretimi (imagen yok); `K/ortak/` altına yazma; `rm`.
- SERBEST: PNG kare çekimi (`ortak/yakala.py` render'sız; HyperFrames paketinde `hyperframes snapshot`); metin ve ses dosyası düzenleme.
  Ses yeniden sentezi `D/araclar/iki-dilli/el.py` ile yapılır (aynı anda en çok 2 `el.py`; "yuva bekleniyor" olağandır; ön planda `timeout 1500`).

## Girdi
- Son DJ hükmü: `{HUKUM_YOLU}`. Hükümdeki her `hayır` satırı (kalın `**hayır**` dahil) bir iştir. `evet`, `kanıt yok`, `uygulanmaz` satırlarına dokunma.
- Ölçütler (D/.claude/docs): `juri-olcutleri.md` §1, §2b, §2c, §2f; `kapak-standardi.md`; `youtube-yayin-verisi-sozlesme.md` §2.
- Skill: `~/.claude/skills/motion-grafik-ders/SKILL.md` ("Bağlayıcı standartlar" tablosu).

## Kapsam: `{KAPSAM}`
Bu tur yalnız aşağıdaki tabloda kapsamına düşen dosya kalıplarına yazar. `hepsi` = dört satırın birleşimi. Kapsam dışı maddeyi
`kapanmadı` işaretle, sahibini yaz; dokunma.

| Kapsam | Dokunabileceği dosya kalıpları (iki pakette) |
|---|---|
| `cumle-ses` | `senaryo.json` (cümle + `meta.canAlici`), `METIN.md`, `BRIEF.md`, `altyazi.json`, `sozcukler.json`, `sureler.json`, `zaman.json`, `surumler.json`, ses dosyaları (yalnız değişen cümle; öteki sha256 aynı kalır), karaoke ve altyazı zamanları |
| `sahne-kare` | `sahneler/*/sahne-*.js`, `sahneler/*/kalem-*.js`, `sahneler/*/uret.py`, `proje/index.html`, paketin kendi `ortak/kunye.js`, `sahneler/*/k/*.png` (kareler EN SON çekilir) |
| `kapak-yayin` | paketin kapak üreticisi ve kapak PNG'leri (yatay + dikey, açık + koyu, 168 px), `youtube.json`, `youtube-aciklama.md`, `surumler.json` düzeltme notu |
| `hepsi` | yukarıdakilerin tümü |

## Kurallar
1. **Render gerektiren madde kapatılmaz** (sınıf a): mp4, bayat `k/` karesi, bayat `zamanlar.json` yan ürünü. Etiketi `render sonrası`; kare çekimiyle
   çözülebilen kısmı (yalnız PNG) çek, mp4'e dokunma.
2. **Ölçüt kararı.** "Ölçüt kararı bekliyor" ya da "Ş belirler" yalnız `D/.claude/docs/juri-olcutleri.md` ilgili satırında "Ş kararı" YOKSA yazılabilir.
   Satırda "Ş kararı" varsa karar uygulanır; maddeyi o karara göre düzelt.
3. Yeni cümle jürinin karşı örneğine dayanır: karşı örneği yeni cümleye kendin uygula. Kapsam sözcüğü (`çoğu zaman`, `durum anlamında`) yeterliyse
   cümleyi yeniden kurma. Mutlak kural ve birebir Türkçe–İngilizce denklik kalmaz. Aynı ifadeyi taşıyan her yer düzelir.
4. Sınıf tanımı (rapor tablosunda): **a** render gerektirir · **b** düzeltilebilir, bu turda yapıldı ya da yapılabilir · **c** ölçüt belirsiz ya da çelişkili ·
   **d** kaynak ya da veri sorunu (karakter cinsiyeti, görsel alfa kusuru, ortak künye) · **e** ölçüm aracı eksik (kare matrisi, `hyperframes check`).
5. KARELER EN SON çekilir: kaynak kareden sonra değişirse o sahnenin kareleri yeniden çekilir (KR-1).
6. `surumler.json` sürüm kaydına düzeltme notu ekle (`degisiklik` ≤ 500 karakter, `no` = `r<sayı>`); ayrıntı rapora.

## İş listesi
{IS_LISTESI}

## Rapor (ZORUNLU biçim)
Dosya: `K/projeler/{PAKET}/uretim-tutanagi/DUZ-RAPOR.md` (var olan metni silme; sona `## Tur DUZ-{KOD}` bölümü ekle). İlk satır `uretici_model: <model>`.
Rapor, hükümdeki HER `hayır` kimliği için bir satırlık şu tabloyu taşır. Tablo eksikse rapor yarım sayılır.

| kimlik | kapandı / kapanmadı | sınıf a–e | sahip | kanıt (dosya:satır ya da kare yolu) |
|---|---|---|---|---|

Tablonun altında: yeni cümle ve önce → sonra farkları, değişen dosyalar, yeniden sentezlenen cümle sayısı, Whisper en düşük (eşik ≥ 0,85),
yeniden çekilen kareler, tutarlılık kapısı (`python3 K/uretim-hatti/betikler/yv-tutarlilik.py --kilitli {PAKET},{PAKET}-dikey` çıkış kodu).
Son mesajın en çok 12 satır: kapandı / kapanmadı sayıları, sınıf dağılımı, düzeltemediğin madde ve sebebi, rapor yolu.
