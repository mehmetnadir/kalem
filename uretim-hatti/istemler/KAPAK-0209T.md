# İstem KAPAK-0209T — present-perfect-cont-temel ana ders kapakları (yatay + dikey, açık + koyu) · 15.11.2026

MAKİNE: Linux x86_64 (srv21), kullanıcı sef. K=`/home/sef/01dev/_worktrees/kalem-0204`. Node `~/.nvm/versions/node/v24.22.2/bin`.
KURALLAR: Yazma yalnız `K/projeler/present-perfect-cont-temel/` ve `K/projeler/present-perfect-cont-temel-dikey/` altında. Var olan sahne kodunu, `zaman.json` ve `surumler.json` dosyalarını değiştirme.
Silme yok (eskiyi `~/Silinecekler/2026-11-15-kapak/` altına taşı). mp4 render YOK. git commit yok. Alt ajan yok. Bayrak dosyası oluşturma;
durma kancası sözleşme isterse `K/.claude/docs/sozlesme.md` dosyasına 1 satır ekle. API anahtarı yazma, `.env` okuma. Görsel üretme: görseller hazır, yalnız diz.

## Oku
1. `/home/sef/01dev/dijital-anlatim/.claude/docs/kapak-standardi.md` (bağlayıcı).
2. BİTMİŞ emsal (üretici ve düzen tek kaynağı; Nadir'e gösterilen pilot): `K/projeler/simple-present-temel/sahneler/90-hyperframes-kapak/`
   (yatay) ve `K/projeler/simple-present-temel-dikey/sahneler/90-hyperframes-kapak/` (dikey) + `K/projeler/simple-present-temel/uretim-tutanagi/KAPAK-RAPOR.md`.
   İkinci emsal (soru biçimli metin, küçük harf `mi`): `K/projeler/02-04-ydt-temel/sahneler/90-hyperframes-kapak/` + o paketin KAPAK-RAPOR.md dosyası.
   Emsal üreticiyi KOPYALA, yalnız metin, görsel yolu ve gereken yerleşim ayarını değiştir (yeni tasarım yapma; kapaklar bir aile gibi görünmeli:
   aynı logo yeri, aynı rozet, aynı yazı tipi ve kutu, aynı çıkartma kenarı; açık temada logo tek renk siyah).

## Girdi
- Görseller (şeffaf PNG, hazır): `K/projeler/present-perfect-cont-temel/ortak/kapak/karakter.png`, `nesne.png` (kaynak `KAYNAK.json`). Dosya yoksa DUR ve yaz.
- Kapak metni (şef kararı, değiştirme): satır 1 `İKİ SAATTİR` · satır 2 `= HAVE BEEN` (vurgu satırı) · küçük satır `-dir … -yor → have been -ing` · rozet `YDT · TEMEL`.
- Sahne fikri: kitap başında yorgun ama gülümseyen karakter; çalar saat küçük, karakterin yanında.

## Yap
1. `K/projeler/present-perfect-cont-temel/sahneler/90-hyperframes-kapak/` kur (1920×1080 durağan kare).
   `K/projeler/present-perfect-cont-temel-dikey/sahneler/90-hyperframes-kapak/` kur (1080×1920; görseller emsaldeki yolla). İki düzen ayrı dizilir; kırpma yok.
   Bu sahneler `zaman.json` `sahneler[]` listesine GİRMEZ.
2. Kare çek: ana paket kökü `kapak.png` (açık) + `kapak-koyu.png` (koyu), 1920×1080; dikey paket (`present-perfect-cont-temel-dikey`) kökü aynı adlar, 1080×1920. Kökte aynı adlı dosya varsa önce Silinecekler'e taşı.
3. Kapı (standart §5): `file` ile boyut; her PNG'ye Read ile bak; yatay kapağın 168 px genişliğe indirilmiş kopyası (`uretim-tutanagi/kapak-168.png`)
   okunuyor mu; büyük İ/Ş/Ğ Fredoka ile mi; yazı ile karakter üst üste binmiyor mu; sağ alt %15×%8 boş mu; dikeyde üst %20 ve alt %20 yalnız zemin mi. Görselde beklenmeyen yazı, kırıntı,
   kesik kenar varsa rapora yaz (görseli sen düzeltme; çıkartma kenarındaki basamak emsaldeki yöntemle giderilir). Kusur varsa düzelt, yeniden çek (en çok 3 tur).
4. Rapor: `K/projeler/present-perfect-cont-temel/uretim-tutanagi/KAPAK-RAPOR.md` (en çok 20 satır): dosyalar + boyut, emsalden farklar, kapı maddeleri, açık kalan.

Son mesajın en çok 8 satır: dosya yolları, kapı sonucu, kusur varsa ne kaldı.
