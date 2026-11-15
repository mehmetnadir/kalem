# İstem S1-A — 02-04-ydt-temel-s1 kısa video senaryo taslağı + hikâye karesi + açıklama metni · 15.11.2026

BAĞLAYICI STANDART: üretimden önce `D/.claude/docs/` altından oku — `huni-v2-standart.md` (kısa), `kapak-standardi.md` (kapak, hikâye), `youtube-surumu-standart.md` (YouTube sürümü), `huni-ab-sozlesme.md` (A/B kolu). Bu istemdeki eski (v1) söz bunlarla çelişirse standart geçer. mp4 yalnız Nadir'in açık sözüyle. D=`/home/sef/01dev/dijital-anlatim`.

MAKİNE: Linux x86_64 (srv21), kullanıcı sef. K=`/home/sef/01dev/_worktrees/kalem-0204` (worktree), D=`/home/sef/01dev/dijital-anlatim`.
Python `/usr/bin/python3 -I`. Skill `~/.claude/skills/motion-grafik-ders/`.
KURALLAR: Yalnız isteneni yaz. Silme yok. Ses sentezi yok, ElevenLabs çağrısı yok, render yok, sahne kodu yok, git commit yok,
alt ajan yok. Yazma yalnız `K/projeler/02-04-ydt-temel-s1/uretim-tutanagi/` altında (dizini sen aç).
Nadir 15.11: "bu video için burada görünenlerin hepsini istiyorum" → huni seti: dikey kısa (Shorts/Reels/TikTok), hikâye karesi,
kapak, açıklama + UTM.

## Okuma
1. Ana ders: `K/projeler/02-04-ydt-temel/` — `ortak/anlatim/senaryo.json` (ses kimlikleri `sesler`, cümleler), `surumler.json`
   (`video.canAlici`, `amaclar`, `kod`, `kitle`, `konu`), `BRIEF.md`, `uretim-tutanagi/senaryo-taslak.md`, `uretim-tutanagi/juri/`.
   Ana ders süresi: 265,7 sn (cikti.mp4, ffprobe; yuvarlak "dört buçuk dakika").
2. Kalıp: `D/.claude/docs/dikey-senaryo-kalibi.md` §4 (kapak) ve §5 (Shorts 15–30 sn); `D/.claude/docs/huni-plan-1211.md` §2, §4, §6, §7.
3. En yeni örnek (biçim tek kaynağı): `K/projeler/present-continuous-ileri-s1/` (BRIEF-S1.md, ortak/anlatim/senaryo.json, surumler.json:
   "süre iddiası kaldırıldı"). Eski örnek `K/projeler/simple-present-temel-s1/` ("6 dk" hatası var; kopyalama).

## Yaz
1. `uretim-tutanagi/senaryo-taslak.md` — 15–30 sn, 3 sahne (kapak · örnek · tam ders çağrısı). Tablo: sahne, konuşan, ses metni
   (Türkçe/İngilizce parçalar), ekran metni, görsel fikir. Can alıcı: ana dersin kancası — Türkçe "yaşıyorum" iki zamana karşılık gelir
   (I live = kalıcı, I am living = geçici); ana ders kanca sahnesi ve `canAlici` ile tutarlı. İlk söz ≤ 1 sn. Rakam yazma (sözcükle).
   Kapanış: present-continuous-ileri-s1 ile aynı ilke — süre iddiası ya yok ya da ölçülmüş süreden ("dört buçuk dakika"); "6 dk" yok,
   "kanal" sözü ve QR yok, kimlik `@ydspublishing` (karar A 05.11). Ses kimliği ana dersin öğretmen sesi.
2. `uretim-tutanagi/kapak-taslak.md` — kapak (1080×1920): başlık en çok 4 sözcük iki satır, can alıcı kısa kod (ör. "yaşıyorum = live /
   am living"), görsel, rozet; dikey-senaryo-kalibi §4 kurallarıyla.
3. `uretim-tutanagi/hikaye-taslak.md` — hikâye karesi (1080×1920, durağan PNG; ≤ 15 sn MP4 isteğe bağlı): üst satır, alt satır, can alıcı,
   "tam ders" çağrısı; huni-plan §7 dil kararı (Instagram/TikTok veliye ve öğretmene seslenir; YDT kitlesi 17–18 yaş yasak dışında —
   hangisini seçtiğini gerekçesiyle yaz).
4. `uretim-tutanagi/aciklama-taslak.md` — huni-plan §4 açıklama şablonu ve §6 UTM şeması: YouTube, Instagram, TikTok için ayrı metin
   (platform kısıtları §5: Instagram/TikTok açıklamada bağlantı tıklanmaz → "profildeki bağlantı"). Doldurulamayan alan (YouTube uzun
   video adresi henüz yok; platform adresi bulamazsan) `{UZUN_VIDEO_URL}` gibi açık yer tutucuyla kalır ve listelenir; uydurma adres yok.
   Platform adresini K, D ve `~/01dev` belgelerinde ara (grammar-kapi); bulduğun kaynağı yaz.
5. `uretim-tutanagi/S1-A-RAPOR.md` — yazılanlar, sahne süreleri tahmini, kararlar ve gerekçe, açık noktalar (Nadir'e soru gerekiyorsa tek
   satırda, önerinle).

Son mesajın en çok 12 satır.
