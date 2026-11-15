# RUNBOOK — 02-04-ydt-temel ("Simple Present vs Present Continuous", YDT temel) sunucuda uçtan uca

Ölçüm tarihi 14.11.2026 · salt okuma · kanıt düzeyi: "ölçtüm" = komut çıktısı, "okudum" = dosya içeriği, "ölçülmedi" = bakılmadı.
Ham çıktılar: `sunucu-ilk-ders/olc.out`, `olc2.out` (aynı klasör).
Mac üretim sırası kaynağı: 02-03 paketi (git yalnız 2 commit: b7b4856 paket iskeleti, a480a72 taşınabilirlik) + `_is/P1-RAPOR.md`,
`BRIEF.md` §4, `SES-DUZELTME.md`, skill `motion-grafik-ders`. Adım sırasını git değil dosya zamanları ve raporlar verir.

## Sunucu özeti (ölçtüm)

| Kalem | Değer |
|---|---|
| Makine | Linux x86_64, 24 çekirdek, 47 GB RAM (18 GB boş), disk %87 (99 GB boş), yük 3,4 |
| Araç | node 24.22.2 · ffmpeg/ffprobe 4.4.2 · google-chrome 157 · git 2.34 · rsync 3.2.7 · claude 2.1.325 · flock/setsid/runuser var |
| Eksik araç | `uv` YOK (el.py komutu `uv run` ile yazılı) |
| Python | `/usr/bin/python3` 3.10.12: numpy, PIL, pytest, requests VAR; soundfile, pyloudnorm YOK; faster_whisper YOK |
| Ayrı venv | `/opt/etk-whisper/.venv` (faster_whisper import OK; soundfile ve pyloudnorm YOK) + model `/opt/etk-whisper/modeller` = yalnız `faster-whisper-small` |
| Motor | kalem `motorlar/hyperframes/node_modules` 73 paket (hyperframes 0.8.226, gsap) · `motorlar/paperjs` (paper-core.js var) · `ses/node_modules` (tone) · `yardimci` (gl-transitions) |
| Chrome | `/usr/bin/google-chrome`, ayrıca `~/.cache/hyperframes/chrome/chrome-headless-shell`; önizleme 41012 + CDP 41333 çalışıyor |
| Depolar | kalem a480a72 (Mac ile aynı), dijital-anlatim f66a27f, conductor 2c9c5b6; sunucu kalem'de `/Users/nadir` geçen dosya 0 (grep) |
| Claude Code | `~/.claude/.credentials.json` VAR (içerik okunmadı); skill kopyası bayat: `motion-grafik-ders/SKILL.md` md5 Mac'ten farklı, "D-0204" (jüri) satırı yok |
| Anahtar | ortamda `ELEVEN*`, `KONTROL_ISCI_JETON`, `CHROME`, `ASR_*` YOK; kayit `scripts`/`src` içinde ElevenLabs vekil rotası bulunamadı |

## 1. Adım tablosu

Sütunlar: no · adım · Mac komutu · girdi · çıktı · kim · sunucuda hazır mı. Yol kökleri: K=`~/01dev/kalem`, D=`~/01dev/dijital-anlatim`, P=`$K/projeler/02-04-ydt-temel`.

| no | Adım | Mac'teki komut | Girdi | Çıktı | Kim | Sunucuda hazır mı |
|---|---|---|---|---|---|---|
| 0 | Künye + kaynak eşleme | elle: `katalog.json` / `katalog-durum.json` / `konu-adlari.json` okunur; GR-02-04 → pptx `sunum-3`, Vimeo 863572960 | `$D/varlik/grammar/katalog.json` | künye (BRIEF §0) | şef | KISMEN. katalog + döküm VAR (git). pptx YOK (aşağıda). Tutarsızlık: `katalog.json` 02-04-ydt-temel `proje: simple-present-temel`, `katalog-durum` `planli`; 02-04 paketi yok (`ls P` → yok) |
| 1 | Paket iskeleti | betik YOK; P1 ajanı 02-03'ten kopyaladı (`ortak/{kunye.js,kalem-canvas.js,tema.sh,tema_damga.py}`, `cizim/font/logo/hf_tema.py` = `../../present-continuous/ortak/…` sembolik bağ) + BRIEF/zaman/surumler/gorevler/yorumlar/harita-konum yazdı | 02-03 paketi | `P/` iskeleti | LLM ajanı (P1) | EVET (kopya + sembolik bağ sunucuda var: `present-continuous/ortak/{cizim,font,logo}` ölçtüm). Otomatik iskelet betiği yok: ölçülmedi/yok |
| 2 | Senaryo istemi derleme | elle: `_is/senaryo-model-1311/istem.md` (36 KB) = GİRDİ 1 künye + GİRDİ 2 pptx soru slaytları + GİRDİ 3 Vimeo dökümü + KURALLAR (skill aynen); betik yok | pptx metni, `863572960.md`, skill dosyaları | `istem.md` | şef | HAYIR (istem.md sunucuda yok: `_is/senaryo-model-1311` yok). 02-04 için yeniden derlenir; pptx metni gerekir (adım 0) |
| 3 | Senaryo taslağı (tablo) | `kredi-kos --bare` (Max API kredisi, Mac) → opus55/sonnet55; 02-03'te taslak `_is/senaryo-taslak/02-03-ydt-temel.md`, izlenen kopya `uretim-tutanagi/senaryo-taslak.md` (21,7 KB) | `istem.md` | `senaryo-taslak.md` (8 bölüm tablo) | LLM (Opus/Sonnet; ölçüm: Sonnet/Opus %86) | KISMEN. `kredi-kos` sunucuda var (`~/.local/bin`); `claude` 2.1.325 + kimlik dosyası var. `claude -p` koşulmadı (yasak) → çalışır mı: ölçülmedi |
| 4 | Jüri (3 salt okuma denetçi: kaynak, kural, dil; en çok 2 tur) | alt ajanlar (agy kapalı, Claude alt ajanı); çıktı `_is/senaryo-taslak/juri/<kimlik>.{kaynak,kural,dil}.md` + `<kimlik>.juri.md` → `uretim-tutanagi/juri.md` | taslak + pptx + döküm + skill | GEÇTİ/DÜZELT kaydı | LLM jüri | KISMEN. Sunucudaki skill bayat (jüri kuralı yok) → önce skill kopyala (eksik 6). Denetçi 1 pptx'e bakar → pptx gerekir |
| 5 | senaryo.json | elle (P1 ajanı): taslak tablosu → `cumleler[]{ses, parcalar:[[tr\|en\|sus,metin]…]}` (+`sesler`); IPA yok, `ses_metni()` çevirir | taslak | `P/ortak/anlatim/senaryo.json` | LLM ajanı (P1) | EVET (düz JSON; araç gerekmez). 02-03 örneği sunucuda var (md5 Mac ile aynı: e578d0d2…) |
| 6 | Ses sentezi + Whisper kapısı | `HIZ_EN=0.9 uv run --quiet --python 3.12 --with faster-whisper --with soundfile --with numpy --with pyloudnorm python -I $D/araclar/iki-dilli/el.py P/ortak/anlatim/senaryo.json P/ortak/anlatim/sentez.wav P/ortak/anlatim gsJ9nrlXYbPztJxC4fwc eleven_v4` | senaryo.json, `ses-sozluk.json` (git), ElevenLabs erişimi | `sentez.wav`, `sentez.wav.rapor.json`, `cumle-N.wav`, `sureler.json` | betik (ElevenLabs HTTP + faster-whisper) | HAYIR. Eksik: ElevenLabs anahtarı/vekil (ortam boş, Keychain yok), `soundfile`, `pyloudnorm`, `uv`, ASR modeli (`large-v3-turbo` yok; yalnız `small`). el.py `ASR_MODEL` ve `ASR_IPLIK` ortamını zaten okur (satır 21–22) |
| 7 | Ses düzeltme (kulak listesi) | `SES-DUZELTME.md`: IPA `/ɪŋ/`, "özne I → ay" (`ses-sozluk.json`), 3 tohum, seçim Whisper large-v3; yedek `_is/ses-duzeltme/yedek-1113/` | `cumle-N.wav`, ses-sozluk | düzeltilmiş cümleler, `SES-DUZELTME.md` | betik + şef/Nadir kulağı | HAYIR (adım 6 ile aynı eksikler; large-v3 yok). Kulak kararı insanda |
| 8 | Sözcük zamanları | `/usr/bin/python3 -I $P/ortak/anlatim/sozcuk_uret.py` | `sureler.json`, `senaryo.json` | `sozcukler.json`, `baslar.json` | betik | EVET (saf Python, `Path` tabanlı, Mac yolu yok; ölçtüm: grep) — adım 6 çıktısı olmadan girdisiz |
| 9 | Sahne zamanı | `/usr/bin/python3 -I $P/ortak/anlatim/zaman_uret.py` | `sozcukler.json`, BRIEF sahne planı | `P/zaman.json` | betik | EVET (aynı gerekçe) |
| 10 | anlatim.wav kur | `/usr/bin/python3 -I $P/ortak/anlatim/kur.py` | `cumle-N.wav`, `sozcukler.json`, `zaman.json` | `anlatim.wav` | betik (ffmpeg) | HAYIR (tek satır): `kur.py:12` `FFMPEG="/opt/homebrew/bin/ffmpeg"`; sunucuda `/usr/bin/ffmpeg` 4.4.2 var → `shutil.which("ffmpeg")` yap |
| 11 | m4a paket | `/usr/bin/python3 $K/araclar/ses-paketle.py …` (aac-96k-48000-mono; `.imza`) | `anlatim.wav` | `anlatim.m4a`, `.m4a.imza` | betik | EVET (ffmpeg_bul `shutil.which` yedeği var, satır 21–37 okudum); ffmpeg'te aac kodlayıcı: ölçülmedi |
| 12 | Altyazı + metin | `/usr/bin/python3 -I $K/araclar/altyazi_uret.py projeler/02-04-ydt-temel` ; `metin_uret.py` | senaryo, sureler, sozcukler | `altyazi.json`, `METIN.md` | betik | EVET (saf Python) |
| 13 | Sahne yazımı (P2; 14 sahne: 7 HyperFrames, 3 Paper.js/2 canvas… dağılım BRIEF §3) | LLM ajanı sahne başına `sahneler/NN-<motor>-<ad>/` yazar: HF → `uret.py`, `olay.py`, `yardim.py`; Paper.js/canvas → `sayfa.html`, `sahne-NN.js`/`sahne.js`, `kalem-paper.js`/`sahne-ortak.js`; hepsi `calistir.sh` | BRIEF §3 sahne tablosu, `zaman.json`, stil anayasası, `kalem-hatti.md`, 02-03 sahneleri örnek | sahne dizinleri | LLM ajanı (sahne yazarı) | KISMEN. Yazım yeri fark etmez (düz dosya). Sunucu Claude'u skill `motion-grafik-ders` + `kalem-hatti.md` okur (var, bayat); örnek sahneler sunucuda var (02-03, 195 izlenen dosya) |
| 14 | Sahne üretimi (önizleme hazırlığı + kare) | `bash P/sahneler/<sahne>/calistir.sh --tema acik` (`ONIZLE_YALNIZ=1` = yalnız hazırlık) | sahne dizini, `zaman.json`, motorlar | `proje/index.html`, `olaylar.json`, `video-acik.mp4`/`video-koyu.mp4` (tam koşu) | betik | EVET hazırlık: Mac `araclar/sunucu-qa.sh <paket> <sahne> <t,…> <koyu_t> --hazirla` bunu sunucuda koşturuyor (13.11). Tam koşu (yakala + ffmpeg): sunucuda 02-02 rc=0 (commit 0a843a3, okudum), 02-03/02-04 için ölçülmedi |
| 15 | Çakışma kapısı + açık/koyu kare QA | `araclar/sunucu-qa.sh <paket> <sahne> <açık t'ler> <koyu t> [--hazirla]` (flock 3 yuva, ~1 dk/sahne) | sahne + paket | `/home/sef/qa-kare/<paket>/<sahne>/*.png` (+Mac'e geri) | betik | EVET (41012 + 41333 çalışıyor; qa-kare 02-02/02-03 dizinleri var, ölçtüm). Not: betik Mac'ten `rsync`+ssh tetikler; sunucuda yerel koşu için `QA_HEDEF` yerine ssh'sız kip gerekir |
| 16 | Birleştirme (iki tema) | `araclar/toplu-birlestir.sh projeler/02-04-ydt-temel` → `birlestir.py … --tema acik\|koyu --gecis BookFlip --efekt hisirti` | `video-<tema>.mp4` ×14, `anlatim.m4a`, `ses/render.mjs` (Tone.js) | `cikti.mp4`, `cikti-koyu.mp4` | betik | KISMEN. `birlestir.py`, `ses/render.mjs`, gl-transitions var; `toplu-birlestir.sh:4` `PATH=/opt/homebrew/bin` (zararsız). Sunucuda tam koşu hiç yapılmadı; ffmpeg 4.4.2'de xfade/gl-transitions desteği: ölçülmedi |
| 17 | Tutanak (ön) | `/usr/bin/python3 -I $D/araclar/sema/tutanak_on.py uret projeler/02-04-ydt-temel --yaz` ; `kapi` ; `araclar/kapi-yaz.py --paket 02-04-ydt-temel` | paket + ses raporu | `uretim-tutanagi/{on.json,kapi.json}` | betik | KISMEN. Saf Python; Mac yolu yok (grep); ölçülmedi: `kapi` çıkışı |
| 18 | Tutanak (art) + ASR kıyası | `tutanak_art.py uret projeler/02-04-ydt-temel --tema acik --yaz --esik 0.85`; `araclar/cikti-yaz.py` | `cikti.mp4`, `cikti-koyu.mp4` | `art.json`, `ciktilar.json` | betik (Whisper) | HAYIR. `tutanak_art.py:29,278,299,705` `MLX_PYTHON_MAC=/Users/nadir/...` ve `HF_HOME=/Users/nadir/...` (setdefault; Linux'ta faster-whisper dalı olup olmadığı: ölçülmedi) + model eksiği |
| 19 | Test + test tutanağı | `PATH=/opt/homebrew/bin:$PATH node --test testler/*.mjs` + `/usr/bin/python3 -I -m pytest testler/` ; `test-tutanak kos` | kalem + dijital-anlatim | TT-… kimliği | betik | KISMEN. pytest + node var; `test-tutanak` var (`~/.local/bin`); çalışma ağacı imzası sunucuda ölçülmedi |
| 20 | Ayna (panel) | `araclar/ayna-gonder.sh 02-04-ydt-temel` (rsync → `~/kalem-ayna`, `kontrol-ayna-esitle.ts`) | paket | panelde sürüm | betik | KISMEN. Hedef zaten sunucu; Mac'ten tetiklenir. Sunucudan yerel eşitleme için rsync atlanır: ölçülmedi |
| 21 | Yayın (R2 / YouTube) | `yayinla.py hazirla/oynatici/giris/yukle` (rclone) | `cikti*.mp4`, manifest | R2 nesneleri | betik | HAYIR + ONAY. `yayinla.py:51` `RCLONE=/opt/homebrew/bin/rclone`; sunucuda `/usr/bin/rclone` var ama `~/.config/rclone` yok; R2 anahtarı yok. Mp4 render yalnız Nadir "yayınla" derse |

## 2. 02-04-ydt-temel kaynak dosyaları

| Kaynak | Yol | Git'te mi | Boyut | Sunucuda |
|---|---|---|---|---|
| pptx (ana; sunum-3 "uygun") | `$D/varlik/grammar/kaynak-pptx/YEDEK/Tenses/unit-1_sunum-3 uygun.pptx` | HAYIR (`.gitignore:74 varlik/grammar/kaynak-pptx/`; yalnız manifest `kaynak-pptx.manifest.tsv` izlenir) | 751,7 KB | YOK (`ls …/kaynak-pptx` → yok) |
| pptx (alternatif) | `…/Tenses/unit-1_sunum-3-NADIR-MSI.pptx` | HAYIR | 750,1 KB | YOK |
| Vimeo döküm (Whisper, 02 - tenses - 04, 1158 sn) | `$D/varlik/grammar/transkript-whisper/863572960.md` + `.json` | EVET | 23,8 KB + 499,5 KB | VAR |
| Komşu bağlam (02-03 kaynağı, yinelenmesin diye) | `…/kaynak-pptx/…/unit-1_sunum-2b uygun.pptx` (549,3 KB, git dışı); `transkript-whisper/863572892.md` (7,6 KB, git'te) | pptx HAYIR, döküm EVET | — | pptx YOK, döküm VAR |
| Katalog | `$D/varlik/grammar/{katalog.json, katalog-durum.json, konu-adlari.json}` | EVET | ölçülmedi | VAR |
| Kimlik | `02-04-ydt-temel` · kod `ING-YDT-GR-02-04-T` · GR-02-04 "02 - tenses - 04" | — | — | — |
| Ses sözlüğü | `$D/araclar/iki-dilli/ses-sozluk.json` | EVET | 2,1 KB | VAR |
| Önceki ders örnekleri | `$K/projeler/02-03-ydt-temel/uretim-tutanagi/{senaryo-taslak,juri,kulak-rapor,ses-duzeltme}.md` | EVET | 21,7 KB taslak | VAR |
| Senaryo kuralları | skill `motion-grafik-ders` + `references/*` | `~/.claude` (conductor deposu) | 54 + 500 satır | VAR ama bayat |
| 02-04 senaryo taslağı | yok (`_is/senaryo-taslak/` altında 02-04 yok) | — | — | — |

Not: pptx slayt metni çıkarma aracı Mac'te elle (python-pptx ya da ham zip XML) yapıldı; hangi araç: ölçülmedi. Sunucuda `python-pptx` import: ölçülmedi.

## 3. Eksikler ve en küçük çözüm

| # | Eksik | En küçük çözüm | Onay |
|---|---|---|---|
| 1 | pptx sunum-3 sunucuda yok (git dışı, 248 MB klasörün 1 dosyası) | Yalnız bu 1 dosya: `rsync -a "…/unit-1_sunum-3 uygun.pptx" sef@srv21:/home/sef/01dev/dijital-anlatim/varlik/grammar/kaynak-pptx/YEDEK/Tenses/` (751,7 KB). Alternatif: Mac'te slayt metnini `.md` çıkar, `varlik/grammar/` altına koy, izle | Hayır (telif içerik değil, kendi kaynak dosyamız; yine de Nadir'e bilgi) |
| 2 | ElevenLabs erişimi yok | `el.py` zaten `eleven_erisim.py` ile 3 yol destekler: `ELEVEN_VEKIL_URL`+`KONTROL_ISCI_JETON` ya da `ELEVENLABS_API_KEY`. Anahtarı ortam dosyasına koy (K-0202) | EVET (anahtar) |
| 3 | `soundfile`, `pyloudnorm` yok; `uv` yok | `/opt/etk-whisper/.venv`'e ya da yeni venv'e `pip install soundfile pyloudnorm` (faster_whisper venv'de var). el.py'yi `uv run` yerine o venv'in python'u ile koş | EVET (paket kurulumu; kullanıcı kuralı: pip yasak, açık izin ister). Sistem kitaplığı libsndfile: ölçülmedi |
| 4 | ASR modeli: `large-v3-turbo` yok, `small` var | Hızlı yol: `ASR_MODEL=<small yolu>` ile koş (el.py bunu destekliyor; önbellek etiketi ayrı kalır). Riski: kapı eşiği 0,85 `large-v3-turbo` ile ayarlı, `small` farklı skor verir → 02-03 cümleleriyle karşılaştır (3 cümle) | `small` için Hayır; `large-v3-turbo` indirme EVET (model indirme) |
| 5 | `kur.py:12` sabit `/opt/homebrew/bin/ffmpeg` | `FFMPEG = shutil.which("ffmpeg") or "/opt/homebrew/bin/ffmpeg"` (1 satır, test `testler/test_calistir_tasinabilir.py` benzeri) | Hayır |
| 6 | Sunucudaki skill `motion-grafik-ders` bayat (jüri adımı yok) | Mac'ten `rsync -a ~/.claude/skills/motion-grafik-ders/ sef@srv21:~/.claude/skills/motion-grafik-ders/` (veya conductor çekimi) | Hayır |
| 7 | `istem.md` sunucuda yok | 02-04 için yeniden derle (pptx metni + `863572960.md` + skill kuralları); eski istem yalnız şablon olarak Mac'ten kopyalanabilir | Hayır |
| 8 | `tutanak_art.py` Mac yolları (MLX, HF_HOME) + model | Linux dalı: `faster-whisper` + `ASR_MODEL` ortamı; `/Users/nadir/...` varsayılanlarını ortamdan oku. Kapsam: ölçülmedi (dosyayı baştan sona okumadım) | Hayır (kod), model için madde 4 |
| 9 | `yayinla.py:51` rclone yolu + R2 anahtarı | `shutil.which("rclone")`; R2 anahtarı sunucuya | EVET (canlı dağıtım + anahtar). Bu ders için gerekmez: mp4/yayın Nadir kararına kadar durur |
| 10 | Tam sahne render ve `birlestir.py` sunucuda 02-04 ölçeğinde koşmadı | Önce 1 sahne `calistir.sh` tam koşu, sonra 14 sahne `agir` yuvasında 3'lü; sonra `toplu-birlestir.sh` tek paket; xfade/BookFlip ffmpeg 4.4.2'de test | Hayır (render yerel dosya; mp4 yalnız "yayınla" sözüyle üretilir kuralı geçerli: ders önizlemesi yeter) |
| 11 | Katalog tutarsızlığı: `katalog.json` 02-04-ydt-temel `proje: simple-present-temel`; `katalog-durum` `planli`; `konu-adlari.json` notu "simple-present-temel paketini 02-04e bağlar" | Üretim öncesi `katalog-durum.json` 02-04-ydt-temel → `{"proje":"02-04-ydt-temel","durum":"uretimde"}` (02-03 örneği) + `grammar-katalog.py --kopya` | Hayır (kod+veri; katalog elle düzenlenmez kuralı: durum dosyası izinli) |
| 12 | Kaynak otoritesi: kalem `_is/` ve `projeler/*/_is/` git dışı → sunucuya git ile gelmez | Üretim çıktısı `_is/` yerine `uretim-tutanagi/` (izlenir) içine yazılsın; jüri dosyaları dahil | Hayır |
| 13 | Sunucuda `sunucu-qa.sh` / `ayna-gonder.sh` Mac'ten tetiklenir (ssh) | Sunucudaki şef oturumu için yerel kip (ssh'sız) ya da betik içinde `[ "$(uname)" = Linux ]` dalı | Hayır |

Onay gerektirenler: 2 (anahtar), 3 (pip), 4b (model indirme), 9 (R2). Gerisi onaysız.
Diğer riskler: disk %87 (99 GB boş; 14 sahne kare klasörleri geçici, `~/Silinecekler` yerine silme kuralı bakılır) · yük 3,4 ama "Y>24 bekle" döngüsü betiklerde var · sunucu kopyası 15 dk'da bir ff-only; yeni dosya (örn. 02-04 paketi) commit edilmeden sunucuya gitmez.

## 4. LLM adımları için sunucudaki Claude Code istem iskeletleri

Ortak başlık (hepsine): `MAKİNE: Linux x86_64 (srv21), kullanıcı sef. Yol kökü /home/sef/01dev. Python /usr/bin/python3 -I. Node ~/.nvm/versions/node/v24.22.2/bin. Yalnız isteneni yaz. Silme yok (~/Silinecekler). Render yok. Kaynakta olmayan kural ekleme. CLAUDE-GEREKÇE: kota (agy ToS 403).`
Hepsi önce skill `motion-grafik-ders` SKILL.md + `references/{stil-anayasasi,ses-tasarimi,hareket-sozlugu,tempo-ve-pedagoji,soru-ani,kliseler}.md` okur. Mevcut istem dosyaları: yalnız `…/02-03-ydt-temel/_is/senaryo-model-1311/{istem.md, juri/istem-p1-{opus,sonnet,nemotron}.md}` (Mac, git dışı, sunucuda yok). Sahne yazarı ve P1 istemi için dosya bulunamadı (P1 ajanı raporu `_is/P1-RAPOR.md` yalnız sonucu verir).

**A. Senaryo yazarı** (şablon: `istem.md`; 02-04 için yeniden derlenir)
```
Rol: YDT İngilizce dilbilgisi ders videosu senaryo yazarı. Çıktı yalnız Markdown tablosu:
| # | bölüm | konuşan | ses metni (söylenen) | ekran metni | görsel fikir | sözcük | tahmini sn |
GİRDİ 1 künye: kimlik 02-04-ydt-temel · GR-02-04 Tenses · "Simple Present vs Present Continuous" · YDT temel · yatay 16:9 ·
  Atakan (öğretmen) + Gökçe Deniz (öğrenci) · süre iddiası yok · önceki dersler: 02-01 PC, 02-02 SP, 02-03 ayrım alıştırması.
GİRDİ 2 pptx: <sunum-3 slayt metni, adım 0/eksik 1 sonrası>
GİRDİ 3 döküm: <863572960.md tamamı>
KURALLAR: skill motion-grafik-ders (aynen): iskelet kanca 15 sn → 3 örnek 90 sn → kural kartı 45 → karşıt çift 60 → tuzak 60 →
  ara özet 20 → mini soru 55 → kapanış 15; öğrenci 2 soru + 1 yanlış cevap; TR/EN parça işareti; [sus N sn]; YDT yerine "dil sınavı"; olay adları hareket sözlüğünden.
```
**B. Jüri ×3** (yazandan ayrı alt ajan, salt okuma, her biri GEÇTİ / DÜZELT + madde + kanıt; yazılacak dosya `projeler/02-04-ydt-temel/uretim-tutanagi/juri/<kimlik>.<kaynak|kural|dil>.md`)
- (a) kaynak: "pptx slayt akışı ve sırası, `863572960.md` kapsamı; eşleme tablosu (kaynak → taslak satırı); kaynakta olmayan kural var mı; gerekçesiz çıkarma var mı."
- (b) kural: "iskelet 8 bölüm, skill yasakları (`kliseler.md`), soru anı standardı (`soru-ani.md`), defter/Nadir notları (D-0204, D-0205: believe/think etiketsiz, these days mutlak değil), süre iddiası yok."
- (c) dil: "İngilizce örneklerin doğruluğu, YDT düzeyi, Türkçe karşılıklar, kısaltma yok, `-ing` ses metni yazımı (`ses-tasarimi.md`, `ses-sozluk.json`)."
Sonuç: üçü GEÇTİ → sentez; DÜZELT → yazar düzeltir, jüri yeniden bakar; 2 turda geçmezse `⏸ KARAR` ile Nadir'e.

**C. senaryo.json yazarı (P1 ajanı)**
```
Girdi: uretim-tutanagi/senaryo-taslak.md (jüri GEÇTİ). Çıktı: ortak/anlatim/senaryo.json (ders, baslik, duzen:"konu", seviye, kitle, sesler{ogretmen,ogrenci},
cumleler[]{ses, parcalar:[[tr|en|sus,metin]…]}). Ham sözcük yaz (are/is/have/I), IPA yazma. Rakam yok. Bölüm süreleri BRIEF §2 tablosuna işlenir.
Sentez/hesap yok: yalnız dosya yaz, `/usr/bin/python3 -I -c "import json;json.load(open(...))"` ile doğrula.
```
**D. Sahne yazarı (P2; sahne başına 1 ajan, en çok 3 eşzamanlı)**
```
Sahne: sahneler/NN-<motor>-<ad> (BRIEF §3 satırı: t_bas–t_son, cümle no, öneri). Örnek: 02-03-ydt-temel aynı rol sahnesi (dosya yapısını kopyala).
Kurallar: tek vurgu sarı #d9900f, doğru yeşil, kırmızı yok; emoji yok; yazı tabanı yatay 30 mantıksal px; olay söylendiği anda (sozcukler.json zamanı);
çakışma 0 px (BRIEF §2.6). calistir.sh kalıbı: `[ -d /opt/homebrew/bin ] && export PATH=…`, `yuk1()` (ortak/tema.sh). Doğrulama: `ONIZLE_YALNIZ=1 bash calistir.sh --tema acik` sonra
`araclar/sunucu-qa.sh`-eşdeğeri yerel kapı. `git commit` yok (şef).
```
**E. Kulak/ses düzeltme ajanı** (adım 7; yalnız ses anahtarı ve model eksikleri kapandıktan sonra): girdi `SES-DUZELTME.md` biçimi, `P1-RAPOR.md` KULAK listesi, `ses-sozluk.json` kuralları; çıktı yedek `_is/ses-duzeltme/yedek-<ggaa>/`.

## 5. Sonuç tablosu

| Adım grubu | Hazır mı |
|---|---|
| Sahne üretimi hazırlığı, kare QA, önizleme (14–15) | EVET (kanıtlı) |
| Zaman/altyazı/metin betikleri 8, 9, 12 | EVET (girdi gelince) |
| kur.py (10) | 1 satır düzeltmeyle |
| Ses sentezi + kapı (6–7) | HAYIR: anahtar, 2 paket, ASR modeli (onay gerekir) |
| Kaynak pptx (0, 2, 4) | HAYIR: 1 dosya kopyalanır |
| LLM adımları (3, 4, 5, 13) | KISMEN: Claude Code + kimlik var, skill bayat, `claude -p` ölçülmedi |
| Birleştirme, tutanak, yayın (16–21) | KISMEN/HAYIR: sunucuda koşu kanıtı yok; yayın onay ister |
