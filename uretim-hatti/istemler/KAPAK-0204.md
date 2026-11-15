# İstem KAPAK-0204 — 02-04-ydt-temel ana ders kapakları (yatay + dikey, açık + koyu) · 15.11.2026

MAKİNE: Linux x86_64 (srv21), kullanıcı sef. K=`/home/sef/01dev/_worktrees/kalem-0204`. Node `~/.nvm/versions/node/v24.22.2/bin`.
KURALLAR: Yazma yalnız `K/projeler/02-04-ydt-temel/` ve `K/projeler/02-04-ydt-temel-dikey/` altında. Var olan sahne kodunu, `zaman.json` ve `surumler.json`
dosyalarını değiştirme. Silme yok (eskiyi `~/Silinecekler/2026-11-15-kapak/` altına taşı). mp4 render YOK. git commit yok. Alt ajan yok.
Bayrak dosyası oluşturma; durma kancası sözleşme isterse `K/.claude/docs/sozlesme.md` dosyasına 1 satır ekle. API anahtarı yazma, `.env` okuma.
Görsel üretme (model çağrısı yok): görseller hazır, yalnız diz.

## Oku (sırayla, başka belge tarama)
1. `/home/sef/01dev/dijital-anlatim/.claude/docs/kapak-standardi.md` (tamamı; bağlayıcı).
2. Kalıp: `K/projeler/02-04-ydt-temel-s1/sahneler/05-hyperframes-kapak-b/` (durağan kapak sahnesi: `SPEC.md`, `uret.py`, `calistir.sh`,
   `proje/`; yazı tipi yükleme ve tema damgası buradan). Kare çekme yöntemi: `K/projeler/02-04-ydt-temel-s1/uretim-tutanagi/S1-VAR-RAPOR.md`
   (altyazısız `hyperframes snapshot` + koyu tema adımı).

## Girdi
- Görseller (şeffaf PNG, hazır): `K/projeler/02-04-ydt-temel/ortak/kapak/karakter.png` (896×1200), `nesne.png`; kaynak `KAYNAK.json`.
- Logo: paketin `ortak/logo/` dizini (ydspublishing yazı logosu; kısa paketindeki künye ile aynı dosya).
- Kapak metni (şef kararı, değiştirme): satır 1 `HER ZAMAN mı` · satır 2 `ŞİMDİ mi?` (vurgu satırı) · küçük satır `I live · I am living` · rozet `YDT · TEMEL`.
- Sahne fikri: karakter (kâküllü, gözlüklü öğrenci, iki avucu açık 'hangisi?' ifadesi) iki seçenek arasında; zıt yönlü iki ok tabelası küçük, karakterin yanında (iki zaman, iki yön). 'mı' ve 'mi' küçük harf kalır.

## Yap
1. `K/projeler/02-04-ydt-temel/sahneler/90-hyperframes-kapak/` kur (1920×1080 durağan kare) ve `K/projeler/02-04-ydt-temel-dikey/sahneler/90-hyperframes-kapak/` kur
   (1080×1920; görselleri ana paketten göreli yolla ya da kopyalayarak al — hangisi kalıpla ve ayna sunumuyla (`/p/<paket>/…`) çalışıyorsa;
   kopyalarsan `02-04-ydt-temel-dikey/ortak/kapak/` altına). Düzen, renk, çıkartma kenarı, boş bölgeler standart §2. İki düzen ayrı dizilir; kırpma yok.
   Bu sahneler `zaman.json` `sahneler[]` listesine GİRMEZ.
2. Dört kare çek: ana paket kökü `kapak.png` (açık) + `kapak-koyu.png` (koyu), 1920×1080; dikey paket kökü aynı adlar, 1080×1920.
   Kökte aynı adlı dosya varsa önce Silinecekler'e taşı.
3. Kapı (standart §5): `file` ile boyut; dört PNG'ye Read ile bak; yatay kapağın 168 px genişliğe indirilmiş kopyasını
   (`uretim-tutanagi/kapak-168.png`) üret ve Read ile bak — ana yazı okunuyor mu; büyük İ/Ş/Ğ doğru yazı tipinde mi; yazı ile karakter üst üste
   binmiyor mu; sağ alt %15×%8 boş mu; dikeyde üst %20 ve alt %20 yalnız zemin mi. Kusur varsa düzelt, yeniden çek (en çok 3 tur).
4. Rapor: `K/projeler/02-04-ydt-temel/uretim-tutanagi/KAPAK-RAPOR.md` (en çok 25 satır): dosyalar + boyut, kullanılan yöntem (komutlar), kapı maddeleri
   tek tek (sonuç + baktığın kare), açık kalan.

Kalite ölçüsü: bu kapak YouTube ana sayfasında yabancı kanalların kapaklarının yanında duracak. Yazı iri ve tek bakışta okunur; karakter yüzü
büyük; öğe sayısı az (yazı, karakter, nesne, logo, rozet — başka süs yok). Emoji yok.

Son mesajın en çok 8 satır: 4 dosya yolu, kapı sonucu, kusur varsa ne kaldı.
