# Üretim hattı — istem şablonları ve yardımcı betikler

Kaynak: srv21 `/home/sef/is/uretim-0204/` çalışma dizininin kalıcı kopyası (15.11.2026). Sunucu dizini bunun türevidir.
Bağlayıcı standartlar: `~/01dev/dijital-anlatim/.claude/docs/` (huni-v2, kapak, youtube-surumu, huni-ab, juri-olcutleri).

| Dosya | Aşama | Ne zaman |
|---|---|---|
| `istemler/A-senaryo.md`, `S?-A.md`, `SN-A.md`, `P0202-S?-A.md` | A senaryo taslağı | ders ya da kısa başlarken |
| `istemler/B-juri-*.md`, `B2-juri-*.md` | B ders jürisi (kaynak, kural, dil; tur 2) | senaryo taslağı bitince |
| `istemler/S?-B-kural.md`, `S?-B-dil.md`, `S1-B.md` | B kısa jürisi (v2) | kısa taslağı ve çıktısı için |
| `istemler/S?-C.md`, `V2-S?-C.md`, `C-paket.md`, `P0202-C-*.md` | C paket üretimi (zaman.json, kapak, hikâye, açıklama) | jüri GEÇTİ sonrası |
| `istemler/D-*.md`, `D/D-NN-*.md`, `D-sahne-sablon.md` | D sahne yazımı (ders) | paket hazır olunca |
| `istemler/KAPAK-*.md`, `S1-KAPAK-A.md` | kapak üretimi | kapak-standardi.md |
| `istemler/hk/`, `bk/`, `hk-uret.py`, `bk-uret.py` | huni kolu (konu adayı, A/B kol b) | A/B planı |
| `istemler/DUZ-1.md`, `A2-duzelt.md`, `W-02-duzelt.md`, `duzelt-istem.py` | düzeltme turları | jüri DÜZELT sonrası |
| `istemler/RUNBOOK.md` | uçtan uca koşu defteri | hat kurarken |
| `betikler/kos.sh`, `kos-devam.sh` | sunucuda başsız iş başlatma | her iş |
| `betikler/sonra.sh`, `sonra2.sh`, `zincir*.sh`, `sahne-kuyruk*.sh` | zincir, kuyruk | biten yerine yenisi |
| `betikler/oku.py`, `bekle.sh` | sonuç oku, durum bekle | iş sonrası |
| `betikler/kontak.py`, `render-*.sh`, `olc*.sh` | kontak sayfası, ölçüm | görsel denetim |
| `betikler/kapasite*.sh`, `takili-bekci.sh` | kapasite, takılı bekleyici | izleme |

## Kullanım
- `kos.sh <ad> <model> <istem-dosyası>` — ayrık oturumda başsız Claude işi; çıktı `~/is/uretim-0204/<ad>.json`, `.err`, `.durum`, `.bitti`.
- `sonra.sh <beklenen-ad> <iş-adı>…` — beklenen iş `bitti 0` olunca her iş için `kos.sh` başlatır.
- `oku.py <ad> [karakter]` — iş sonucunu okur.
- `bekle.sh <durum-dosyası>…` — biri `bitti` olunca çıkar (en çok 90 dk).

## Sabit kurallar
1. Silme yok; eski koşu dosyası `eski/<zaman>/` altına taşınır.
2. `pgrep -f` ile bekleme yok (başsız oturum kendini eşler); durum dosyası ya da `bekle.sh` kullan.
3. mp4 yalnız Nadir'in açık sözüyle.
4. Kanca atlama bayrağı yok.
5. Jüri çıktıyı görür, içerik değişince yeniden koşar, modeli üreticiden farklıdır.

## YouTube yayın verisi kuralları (YV-DUZ, 16.11)
- Başlık kalıbı: temel `<Konu> | YDT İngilizce`; ileri `<Konu>: <2–4 sözcük> | YDT İngilizce İleri`. Alt başlık kapak metnini yinelemez (KS-4).
- Açıklama: damga bloğu "Bölümler:" satırıyla başlar. Sabit yorum ve gönderide aynı cümle ya da yan cümle en çok 2 derste geçer.
- Tutarlılık kapısı: `python3 uretim-hatti/betikler/yv-tutarlilik.py [--kilitli <paket,…>]` (çıkış 0 = geçti). Rapor: `raporlar/YV-DUZ-1511.md`.

## Üretim teknik notları (sözleşmeden taşındı, 16.11)

Sözleşme 150 satır sınırını aştı (157). Teknik ayrıntılar burada; sözleşmede tek gösterge satırı kalır.

### YouTube yayın verisi (YV)
- YouTube yayın verisi (YV, `youtube-yayin-verisi-sozlesme.md`): ana ve dikey pakette `youtube.json` + `youtube-aciklama.md`; `bolumler[].t` = sahne `t_bas` (kesirli, `zaman.json`), açıklama damgası en yakın saniyeye yuvarlanır (43,85 → 00:44); bildirim `t` = `baslar.json` cümle başı (02-04: 69,39 ≈ %26 · 184,54 ≈ %70); `surumler.json` `kapak` null iken gönderi görseli paket kökündeki `kapak.png` (15.11, 02-04 YV-0204T).
- YV, kısa ders (< 4 dk) ve `baslar.json` olmayan ana paket: cümle başları `ortak/anlatim/METIN.md` "başlar" sütunundan; %30 anı ilk 30 sn yasağına düşerse 30 sn sonrasındaki ilk cümle başı alınır (simple-present-temel: 28,04 → 43,91 ≈ %47); ≤ 3 dk dikey sürüm YouTube'da Shorts sayılır, bölüm ve bildirim orada işlemeyebilir → şef kararı (15.11, simple-present-temel YV-0202T).
- YV, temel ve ileri ders aynı konu (present-perfect-temel / -ileri, `surumler.json` `konu` alt başlıksız "Present Perfect"): düz kalıp iki videoya aynı başlığı verir → ileri başlıkta alt başlık dersin amaçlarından ("Present Perfect: since, for ve ago tuzağı | YDT İngilizce", şef onayı bekler); kısa paketinde açıklama yoksa taban ve utm 02-04/simple-present-temel emsalinden; bildirim 28,13 → 34,44 (cümle 4 başı, %36,7) (15.11, YV-0206I).
- YV, eski kodlu pilot paket (present-continuous: `surumler.json` `kod` = `ING-YDT-GR-01-PC`, katalogda `eskiKod`): `utm_campaign` katalog `kod` ve kısa yazımından (`ING-YDT-GR-02-01-T`); liste ilk öğesinde `onceki` null; cümle sahne başında başlıyorsa en yakın saniye damgası sözün ilk 0,02–0,19 sn'sini kaçırır (01:03 ← 62,81) → şef kararı (15.11, YV-0201T).
- YV, kısası olmayan ana paket (02-03-ydt-temel): bağlantı tabanı ve utm biçimi öteki dersin kısasından (`02-04-ydt-temel-s1`), adres `https://ydspublishing.com/grammar/<kimlik>`, `utm_campaign` = `surumler.json` `kod` büyük harf; komşu derste başlık çakışırsa konu = `surumler.json` `konu` alt başlığıyla ("…: ayrım alıştırması"); taban adres 15.11'de 404 (15.11, YV-0203T).

### Huni A/B kol b
- Huni A/B kol b kopya paket (`kapanis`, simple-present-temel-s2b KBC-0202S2): `cp -a` kol a'nın `ortak/{cizim,font,logo,hf_tema.py}` bağlarını (ve `logo/` içi `yds-publishing-koyu-zemin.svg` bağını) bağ olarak taşır, kopya kapısı bağ açan `-L` bayrağını bloklar → bağ Silinecekler'e, hedef `cp -a` ile yerine; değişmeyen sahne 02 (Paper.js) ve `ortak/kunye.js` `KOK` kol a'yı `/projeler/<kol a>/` mutlak yoluyla yükler, bayt aynılığı için değişmez (kol a taşınırsa kol b 02 kırılır); yeniden sentezde kol b süresi kol a ile aynı çıktı (25,73), `zaman.json` bayt aynı (15.11).
- Huni A/B kol b `kapanis` = `ekran-goruntusu` (02-04-ydt-temel-s2b KBC-0204S2): kaydet sahnesinde yer imi yerine elle yazılan vizör (`cizim/vizor.svg`: 4 köşe + deklanşör karesi, kutu x 102–242, y 1120–1260); kalıp 3 parça kendi çapasında (`Ekran` köşeler `cizgi`, `al` deklanşör `tik` + Today hapı çerçeveye, `sınav` satır 2); altyazı paket içi `ortak/anlatim/altyazi_uret.py projeler/<paket>` ile (araclar sürümü `T shirt` parçasında 9 parçaya kayar); süre 29,41 → 29,49, yeni ses 4 parça (15.11).
- Huni A/B kol b `kanca` = `yanlis-cumle` (simple-present-temel-s1b KBC-0202S1): kopya `cp -a --dereference` (bağsız, 413 dosya); sahne 01 kapak `MY BROTHER` / `GO.` + kırmızı kalem ✗ (SVG, `--kirmizi`), `Kardeşim gider:` + `go` kartı yerine yanlış cümle kartı (kutuHazir 70,630,880,220 eşi); sahne 02 değiştiği için `ortak/kunye.js` `KOK` ve 02 içe aktarımları kol b yoluna döner (kol a sözcük zamanını okumasın); uçuşta satır 2 kutusu rozete 6 px pay içinde değdi → `ucus_ayrik` 10 → 14; 03/04 `proje/` kol b zamanıyla yeniden üretilince bayt aynı, yalnız `zamanlar.json` küresel sn kayar (15.11).
- Huni A/B kol b `kanca` = `soru` (02-04-ydt-temel-s1b KBC-0204S1): kol a sahne 02 başı (kare 0–100) cümle 1 kuyruğudur (karaoke, iki `yor` kutusu); kol b'de sahne 01'e geçer, sahne 02 yalnız yol + KARE/T_BAS + çapasız `HAZIR` kutularla kırpılır (kare 0 ↔ kol a kare 100: altyazı üstü 0 farklı piksel). Kanca sahnesinde başlık boyu kol a'ya sabitlenir (dar `AYNI MI?` formülle 161 → satır 1'e 5 px). Kapı ızgarası (t_bas + k/4) kol a'nın atladığı geçiş anını yakalayabilir (`-um.` × `yor çip`, kol a'da 8,37–8,43 sn aynı): miras uyarı, içerik değişmez.
- Huni A/B kol b `kanca` = `yanlis-cumle` (02-04-ydt-temel-s3b KBC-0204S3): kanca ayrı cümle 1 ("Hata nerede?", 1,04 sn); ilk söz `sozcuk_uret.py` `ILK` ile kayma kare katı seçilir (0,41 + 1,04 + 0,55 = 2,00 → tam 1,00 sn = 30 kare), sahne 01 = cümle 2 başı + 2,00 = 4,00, sahne 02/08/03 `proje/` bayt aynı, son hal kol a karesiyle piksel aynı; el.py DIL durumu yeni TR parçadan sonra önbellek EN parçasını `tr` sayı kuralıyla kıyaslar (0,92, yeniden sentez yok); kol a cümle N → kol b N+1 (`cumle-N.wav` adla farklı, sha256 aynı); değişmeyen 08/03 `uret.py` cümle numarasını sabit okur → kol b'de yeniden koşturulmaz (15.11).
- Huni A/B kol b `kanca` = `soru` (simple-present-temel-s3b KBC-0202S3): yalnız sahne 01 değişir; kapak kartı `He goes.`, "Olumsuzda" sözüyle şapka + kayma + kırpmayla `doesn't` girer, kart kol a kartına yakınsar (`devir.json` yalnız `t` farklı, son kare kol a ile piksel aynı); başlık B kol a'ya sabit (133), İ noktası için hap üstü uzar; İ noktası tek `<text>` kutusunu köşeye dek yükseltir, yarım çerçeve köşe yayı kesişir → `Gİ` + `DER?` iki parça (kapı 0); son sözcük sonu ses bitişini aşabilir (3,32 > 3,24) → çıkış içerik sonuna bağlanır; kayma 0,65 sn = 19,5 kare (tam kare değil, sahne 02–04 ses eşlemesi yarım kare içinde) (15.11).

### Sahne düzeltme dersleri (DUZ3-0201I önerisi, 16.11)
- Ders ortasında cümle uzayınca sonraki canvas sahneleri (`sahne-ortak.js` `Sahne`) yeniden zamanlanmaz: zaman.json `t_bas` yenilenir,
  sahne `TBAS` eski kalır, `kayma: -Δ` sözcükleri eski çerçeveye çevirir; dikeyde altyazı çağrısı `zm(f) - this.kayma` olmalı (yoksa
  altyazı Δ kadar kayar). Δ 0,1 sn katına yuvarlanır (3 kare; kare sınırları tam sayı kalır) (16.11, present-continuous-ileri DUZ3).
- `paperTopla` (kalem-paper.js) `item.bounds` okur; `oge({topla})` ile küçülen grubun çizgileri ölçeksiz konumda ölçülür. Toplanan sahnenin
  yanına yazılan kart dışı yazı yanlış "yazı × cizgi" hatası verir (present-continuous-ileri-dikey 03, `aynı anda`) (16.11).
- Dikey HF `yardim.altyazi_svg` 3. satırı 2.'ye ekler, taşar; uzun parça üreteçte cümle sınırından bölünmeli (`alt_bol`, `altyazi-bol.js`
  kuralı: dilim ilk sözcüğünün t0'ında açılır) (16.11, present-continuous-ileri-dikey 06).
- Ana pakette ses metni değişince dikey eşteki sabit yazılmış metinler (HF altyazı `<text>`, sahne 02 `cumle([...])`, satır dizisi) ayrıca
  taranır; 13.11 c1 düzeltmesi dikeye 3 gün taşınmamıştı (16.11).
