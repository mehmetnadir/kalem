# İstem D-S2 — 02-04-ydt-temel-s2 sahne 04-hyperframes-hikaye · 15.11.2026

MAKİNE: Linux x86_64 (srv21), kullanıcı sef. K=`/home/sef/01dev/_worktrees/kalem-0204` (git worktree, dal `sunucu/02-04-ydt-temel`).
Node `~/.nvm/versions/node/v24.22.2/bin`. Python `/usr/bin/python3 -I`. Skill `~/.claude/skills/motion-grafik-ders/`.
KURALLAR: Yalnız bu sahnenin dizinine yaz: `K/projeler/02-04-ydt-temel-s2/sahneler/04-hyperframes-hikaye/`. İstisna: `calistir.sh --tema acik` paket köküne yalnız `hikaye-a.png` ve kopyası `hikaye.png` yazar (tek kare PNG; sahnenin teslimi budur). Başka sahneye, `ortak/`a,
`BRIEF-S2.md`'ye, `zaman.json`'a, ana derse (`02-04-ydt-temel`), S1 paketine (`02-04-ydt-temel-s1`) ve dikey pakete dokunma (eksik
görürsen raporla). Silme yok (`~/Silinecekler/2026-11-15-0204/` altına taşı). mp4 render YOK: `calistir.sh`'ı yalnız `ONIZLE_YALNIZ=1`
ile koş. git commit yok. Claude alt ajanı açma.
Kanca atlama bayrağı OLUŞTURMA (/tmp/conductor-*, ~/.conductor/*). Durdurma kancası sözleşme satırı isterse K/.claude/docs/sozlesme.md
dosyasına 1–2 satır EKLE (tek istisna).

## Kod yolu (kapı ve doktrin)
Kod yazma kapısı 15 satırdan uzun kod dosyasını sana kapatır; bayrak açmaya çalışma. Yol: tasarımı sahne dizininde `SPEC.md` olarak
yaz (yazılacak dosyanın mutlak yolu, örnek sahnenin mutlak yolu ve oradan alınacak kalıp, olay listesi olay · kare/küresel sn · cümle
sözcüğü, yerleşim, ekran metni, kurallar, kabul ölçütü; tam kod YAZMA). Sonra
`agy-filo tek --rol kod --cwd /home/sef/01dev/_worktrees/kalem-0204 --zaman 25m -p "<SPEC.md mutlak yolunu oku ve uygula. Yalnız <dosya
mutlak yolu> dosyasını yaz. Başka dosyaya dokunma. Silme yok. Test, render, git yok.>"`. Kodu agy yazar; sen baştan sona okur, spec'e
uyuyor mu bakarsın, küçük düzeltmeyi Edit ile yaparsın, büyük düzeltmeyi agy'ye geri verirsin (en çok 2 tur). Tam kodu kendin yazıp
agy'ye birebir kopyalatmak YASAK (kapıyı vekille dolanmaktır). Örnek sahne dosyasını kopyalayıp küçük Edit'le uyarlamak serbest.
Kısa dosyalar (`calistir.sh`, `sayfa.html`) Edit ile yazılabilir.

## Okuma
1. Skill `SKILL.md`, `references/kalem-hatti.md`, `stil-anayasasi.md`, `hareket-sozlugu.md`, `kliseler.md`.
2. Paket: `K/projeler/02-04-ydt-temel-s2/BRIEF-S2.md` (giriş, "Sahneler" tablosunda 4. satır: — | 04-hyperframes-hikaye | HyperFrames | zaman çizelgesi dışı | 1 | hikaye-a.png (+ hikaye.png); "Kapak" ve "Hikâye"
   bölümleri), `zaman.json` (`hikaye` alanı; zaman çizelgesi dışı),
   `ortak/anlatim/senaryo.json` (`giris`, `meta.kapak`, `kadro`; ses yok, sözcük zamanı gerekmez), `uretim-tutanagi/S2-duzeltme.md`,
   `K/projeler/present-continuous-dikey/BRIEF-DIKEY.md` §0 ve §2–§3 (Nadir'in dikey bulguları, HUD ölçüleri).
3. İçerik kaynağı (ana ders yatay; içerik ve olay sırası; yerleşim DEĞİL): `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel/sahneler/12-hyperframes-ozet/` (özet kart dili) ve kart görseli için sahne 02 tarifi (BRIEF-S2 3,39–17,41 satırları) (kod + RAPOR.md).
4. Dikey örnek (aynı ders, aynı motor; dosya yapısı, `calistir.sh` kalıbı, 1080×1920 kurulum, `ONIZLE_YALNIZ` satırı): `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-s1/sahneler/04-hyperframes-hikaye/`.

## Yaz
`sahneler/04-hyperframes-hikaye/` içinde örnekle aynı dosya yapısı. Kurallar: tek sütun, kenar 48, içerik bandı 352–1392 (BRIEF-DIKEY §2); yazı tabanı
≥ 64 mantıksal px; satır ≤ 24 karakter; tek vurgu sarı (temaya göre), doğru şık yeşil, kırmızı yok, emoji yok; sabit px yerine oran ya da
BRIEF-DIKEY ölçüsü; altyazı + karaoke alt bantta (1400–1536); künye ve tema çifti (açık + koyu) `ortak/kunye.js` ile (çip
`KUNYE.cipler["04-hyperframes-hikaye"]`); sarı hap açık temada dolgu `RENK.vurguDolgu` (`#ffe066`), yazı `RENK.pilMetin` (`#1b2440`); 9 sn'den uzun boş
çerçeve yok; ekranda `T-shirt` tireli (seste `T shirt`); "kanal" sözü, QR ve süre "6 dk" yok.
`calistir.sh`: `[ -d /opt/homebrew/bin ] && export PATH="/opt/homebrew/bin:$PATH"`, yük `Y=$(yuk1)`, yakalama `1080 1920`.

Bu sahneye özel:
- Hikâye A (bilgi kartı). Tek kare, durağan, ses yok. Tarif BRIEF-S2 "Hikâye A" sütunu + `uretim-tutanagi/hikaye-taslak.md` §3:
  `Genel mi, şu an mı?` · kart 1 `She wears her coat` / `in the winter.` · `GENERAL` · küçük mont + kış bantları · kart 2 `She is wearing her` /
  `pink T-shirt today.` · `RIGHT NOW` · küçük tişört + today bandı · `today` (sarı hap) · `iki zamanda da geçebilir` · `Farkı anlam yapar.` ·
  `Tam ders:` / `profildeki bağlantı` · `@ydspublishing` hap. En uzun satır ≤ 24 karakter.
- Tek sarı öğe `today` hapı (rozet ve `@ydspublishing` hapı künye öğesidir); kartta `odak` yok. `today`'den `GENERAL` kartına bağ YOK.
- Altyazı ve karaoke YOK (ses yok); 1344–1536 bandı çağrı satırına ayrılır. Yaz kuralındaki altyazı maddesi bu sahnede geçersiz.
- mp4 render yasağı bu sahnede şöyle uygulanır: `video.mp4` ve birleştirme yok; tek kare yakalama (PNG) serbest, çünkü teslim PNG'dir.
  `calistir.sh` (S1 örnek kalıbı, `HEDEF` satırı): üret → tek kare yakala (1080×1920) → `--tema acik` paket köküne `hikaye-a.png` +
  kopyası `hikaye.png`, `--tema koyu` `k/hikaye-a-koyu.png`.
- Zaman çizelgesine girmez: `zaman.json` → `hikaye` alanı (kare 1); `sahneler[]`'e ekleme (birleştirmeyi bozar).

## Doğrula (zorunlu, geçmeden bitirme)
`qa-yerel.sh`, `cakisma-kapisi.mjs` ve `sahne-kare.mjs` sahneyi `zaman.json` → `sahneler[]` içinde arar; bu sahne bilerek
dışındadır (`hikaye` alanı). Bu yüzden qa-yerel'i koşma: qa-yerel t değerleri KÜRESEL anlatım saniyesidir, durağan karenin anlatımda
saniyesi yoktur. S1-VAR ölçümü: çakışma kapısı durağan sahnede 3/3 `HATA sahne bulunamadı` (çıkış 2); aracı değiştirme.
Doğrulama: `ONIZLE_YALNIZ=1 bash calistir.sh` (önizleme hazırlığı), sonra `bash calistir.sh --tema acik` ve `bash calistir.sh --tema koyu`
→ `hikaye-a.png` + `hikaye.png` + `k/hikaye-a-koyu.png` (1080×1920; `ffprobe` ile boyut). Betik tek kare yakalayamıyorsa dur ve hatayı aynen raporla; aracı değiştirme.
Üretilen PNG'lere (`sahneler/04-hyperframes-hikaye/k/`, `k/koyu/`) Read ile BAK: taşma, kesik yazı, üst üste binme, okunmaz kontrast, boş kare,
alt bantta altyazıyla çakışma, 1536 altı boş mu. En çok 4 düzeltme turu; geçmezse dur ve raporla.

## Rapor
`sahneler/04-hyperframes-hikaye/RAPOR.md`: olay listesi, kapı sonucu (son satırlar), bakılan kareler ve bulgu, agy koşu özeti yolu, açık noktalar.
Son mesajın en çok 10 satır: kapı çıkış kodu, kare yolları, agy koşu özeti, açık noktalar.
