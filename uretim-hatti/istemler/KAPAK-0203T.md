# İstem KAPAK-0203T — 02-03-ydt-temel ana ders kapakları (yalnız yatay, açık + koyu) · 15.11.2026

MAKİNE: Linux x86_64 (srv21), kullanıcı sef. K=`/home/sef/01dev/_worktrees/kalem-0204`. Node `~/.nvm/versions/node/v24.22.2/bin`.
KURALLAR: Yazma yalnız `K/projeler/02-03-ydt-temel/` altında. Var olan sahne kodunu, `zaman.json` ve `surumler.json` dosyalarını değiştirme.
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
- Görseller (şeffaf PNG, hazır): `K/projeler/02-03-ydt-temel/ortak/kapak/karakter.png`, `nesne.png` (kaynak `KAYNAK.json`). Dosya yoksa DUR ve yaz.
- Kapak metni (şef kararı, değiştirme): satır 1 `ÖNCE` · satır 2 `SİNYALE BAK` (vurgu satırı) · küçük satır `now · usually · these days` · rozet `YDT · TEMEL`.
- Sahne fikri: büyüteçle bakan karakter (sinyal sözcüğünü ara); trafik lambası küçük, karakterin yanında.

## Yap
1. `K/projeler/02-03-ydt-temel/sahneler/90-hyperframes-kapak/` kur (1920×1080 durağan kare).
   Bu sahneler `zaman.json` `sahneler[]` listesine GİRMEZ.
2. Kare çek: ana paket kökü `kapak.png` (açık) + `kapak-koyu.png` (koyu), 1920×1080. Kökte aynı adlı dosya varsa önce Silinecekler'e taşı.
3. Kapı (standart §5): `file` ile boyut; her PNG'ye Read ile bak; yatay kapağın 168 px genişliğe indirilmiş kopyası (`uretim-tutanagi/kapak-168.png`)
   okunuyor mu; büyük İ/Ş/Ğ Fredoka ile mi; yazı ile karakter üst üste binmiyor mu; sağ alt %15×%8 boş mu. Görselde beklenmeyen yazı, kırıntı,
   kesik kenar varsa rapora yaz (görseli sen düzeltme; çıkartma kenarındaki basamak emsaldeki yöntemle giderilir). Kusur varsa düzelt, yeniden çek (en çok 3 tur).
4. Rapor: `K/projeler/02-03-ydt-temel/uretim-tutanagi/KAPAK-RAPOR.md` (en çok 20 satır): dosyalar + boyut, emsalden farklar, kapı maddeleri, açık kalan.

Son mesajın en çok 8 satır: dosya yolları, kapı sonucu, kusur varsa ne kaldı.
