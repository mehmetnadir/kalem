# S3 jüri düzeltmeleri — simple-present-temel-s3 · 15.11.2026 (istem P0202-S3-C)

Girdi: `juri/s3.dil.md` (DÜZELT, 4 madde), `juri/s3.kaynak-kural.md` (DÜZELT, 7 madde). 11 maddenin 11'i işlendi.
Dil 1 ile kaynak 1 aynı sorundur; dil 4 ile kaynak 4 aynı kartın satırıdır. Taslakların önceki hâli:
`~/Silinecekler/2026-11-15-0204/simple-present-temel-s3-taslak-onceki/` (`cp -p`).

## 1. Maddeler

| # | Madde | Yapılan | Kanıt |
|---|---|---|---|
| 1 | dil 1 + kaynak 1 — `goes` içinde yalnız `s` çiziliyor, kartta `goe` kalıyor | Üstü çizme `es` ekini kapsar (`go` + çizili `es`); ok `es`'ten `does`'a gider (`go-es` → `do-es`); çizili `es` düşer, kart `go` kalır. Kapak C ve hikâye A aynı biçimde. Ses metni değişmedi | `senaryo-taslak.md` §2 sahne 2 satırları · `kapak-taslak.md` §1 Kırmızı satırı, §5 çizimi · `hikaye-taslak.md` §3 yanlış satır |
| 2 | dil 2 — `Fiile ikinci s gelmez.` iki anlama gelir | Ses ve ekran: `Fiile s gelmez.` (jürinin ilk önerisi; ana cümle 7 parça 3 "Fiile s gelir."in karşıtı). Açıklama set B iki yerde aynı metin | `ortak/anlatim/senaryo.json` cümle 2 parça 2 · `senaryo-taslak.md` §2, §3, §5 (süre 2,20 → 1,60 tahmin) · `kapak-taslak.md` §1 · `aciklama-taslak.md` §4, §5 · `../aciklama-b.md` |
| 3 | dil 3 — YouTube başlığı önerilen kapağın sözünü yineliyor | Set A: başlık aynı, eşleşen kapak C → A (`kapak-a.png`). Set B: başlık `Does gelince fiile s gelir mi? \| YDT İngilizce #Shorts`; kapak B aynı kaldı | `aciklama-taslak.md` §3 elle adım satırı, §4 başlık, §5 tablo · `../aciklama-a.md` §1 · `../aciklama-b.md` §1 |
| 4 | dil 4 + kaynak 4 — hikâye B ipucu hitap taşıyor; kartta kural özeti yok (standart §6) | İpucu satırı (`Önce does'a bak.`) kalktı; yerine hitapsız kural özeti `Does varsa fiil yalın.` (Fredoka 700 56, ayrı satır y 980–1050; `Kaydet` hapı altında, madde 10). Eski alt bant `Cevap ve neden: dersin tamamında` kalktı; 1400–1550 boş. Kaynak jürisinin (a) yolu; konum emsal hikâye düzenine çekildi (bkz. §2) | `hikaye-taslak.md` §2, §4 tablosu, §5 · `istem/sahne/D-08-hyperframes-hikaye-b.md` |
| 5 | kaynak 2 — `canAlici[3]` S3'ün can alıcısı değil | `[3]` hiçbir yerde yazılmaz. `meta.kapak.canAlici` boş (`""`); tek kaynak ana `senaryo.json` cümle 7 parça 4. Ana `canAlici` listesine madde ekleme şef kararı (yazma kapsamı dışı) → §3 | `ortak/anlatim/senaryo.json` `meta.kapak` · `senaryo-taslak.md` §1 · `kapak-taslak.md` §1, §6 |
| 6 | kaynak 3 — 15 yaş dil kararı gerekçesiz | Hikâye §2'ye S2 hikâye §2 gerekçe tablosu alındı; açıklama §1 "Dil" satırına gerekçe bağı | `hikaye-taslak.md` §2 · `aciklama-taslak.md` §1 |
| 7 | kaynak 5 — ana kapak kartı 920 px ortalı, sağ 40 px platform bölgesinde | Kart 900×506, x 60–960, y 620–1126 (S1, S2 ve emsal ile aynı) | `senaryo-taslak.md` §2 sahne 4 · `../BRIEF-S3.md` · `istem/sahne/D-04-hyperframes-cagri.md` |
| 8 | kaynak 6 — "ana ders kapağı bu worktree'de yok" iddiası yanlış | Cümle çıktı. Yeni metin: dosya var, git'e girmez (`.gitignore` satır 27), başka makineye ayna ile gelir. Paket kopyası alındı | `senaryo-taslak.md` §1 · `ortak/kapak/ana-kapak.png` md5 `b51ced1b…` = `../../simple-present-temel/kapak.png` · `ana-kapak-koyu.png` |
| 9 | kaynak 7 — içerik yazısı 50 px tabanının altında | Soluk TR `O gitmez.` / `O gider mi?` Caveat 48 → 52. Çıkan ikincil öğeler: sahne 02 kart 2 küçük üstü çizili `goes` (Caveat 40), sahne 03 `doesn't go · Does she go?` satırı (Lexend 40), hikâye A küçük üstü çizili `goes` (Caveat 36). `Gönder` etiketi Lexend 700 ≥ 50 | `senaryo-taslak.md` §2 · `hikaye-taslak.md` §3 |
| 10 | kaynak 7 genişletme (S3-C gözü) — hikâye kartlarında `Kaydet` Lexend 48 (jüri listesinde yoktu); B kartında kural + hap 90 px banda iki öğe | `Kaydet` 48 → 52 (A ve B). B bantları yeniden dağıtıldı: başlık 88, kök ve şıklar 64, kural özeti ayrı satır 980–1050 (Fredoka 56), hap 1060–1140. İçerik yine 460–1140 | `hikaye-taslak.md` §3–§4 · `istem/sahne/D-05…`, `D-08…` |

## 2. Jüri önerisinden ayrılan yer

| Madde | Jüri önerisi | Yapılan | Neden |
|---|---|---|---|
| 4 | (a) alt bant (y 1400–1550) yerine kural özeti; dil 4: ipucu `İpucu: önce does` | kural özeti içerik bandında (y 980–1050), ipucu satırının yerinde; alt bant boş | emsal hikâye düzeni y 1400–1920'yi boş tutar (`../../02-04-ydt-temel-s1/BRIEF-S1.md` "Hikâye kareleri"). Kural özeti ve `önce does` ipucu aynı bilgiyi verir; iki satır yinelenirdi. Kuralın kendisi hitapsızdır: dil 4'ün iki koşulu da sağlanır |
| Rozet (madde değil; dil açık nokta 2, kaynak açık nokta 2) | standart §2 `YDT · TEMEL` doğru | künye rozeti `YDT · BASIC` | istem S3-C "Rozet emsaldeki gibi"; emsal 02-04-ydt-temel-s1 `YDT · BASIC`. Taslaklarda künye satırları buna çekildi |

## 3. Uygulanmayan / şef ya da Nadir kararı

| Konu | Neden |
|---|---|
| Ana `simple-present-temel/surumler.json` `canAlici` listesine "Olumsuzda ve soruda does girer, s ona geçer" maddesini eklemek (kaynak 2 ilk öneri) | ana paket yazma kapsamı dışı; şef kararı. Eklenirse `meta.kapak.canAlici` o maddeyi birebir alır |
| Ses sözlüğüne marka kaydı (dil açık nokta 6, kaynak açık nokta 6) | `dijital-anlatim` dosyası, kapsam dışı. `kisaltma.YDS` → `YeDeSe` yeterli; cümle 4 önbellekten gelir (`S3-C-RAPOR.md`) |
| Yayın dersi `02-02-ydt-temel` olursa çağrı kapağı ve can alıcı kaynağı (kaynak açık nokta 1) | istem S3-C kararı uygulandı: öğe `02-02-ydt-temel`, ana paket `simple-present-temel` (kadro, ses, kapak) |
