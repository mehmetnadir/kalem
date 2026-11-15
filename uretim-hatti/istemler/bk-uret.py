#!/usr/bin/python3 -I
"""Kol b taslak istemleri (BK-<kod>.md): pilot 6 kısa için deneme kolunun senaryo taslağı."""
from pathlib import Path

KISALAR = [
    ("0204S1", "02-04-ydt-temel-s1", "02-04-ydt-temel", "kanca", ""),
    ("0204S2", "02-04-ydt-temel-s2", "02-04-ydt-temel", "kapanis", ""),
    ("0204S3", "02-04-ydt-temel-s3", "02-04-ydt-temel", "kanca", "Bu dersin S1 kol b'si de kanca değiştirir; onunla aynı değeri seçme (S1 taslağı yazıldıysa oku)."),
    ("0202S1", "simple-present-temel-s1", "simple-present-temel", "kanca", ""),
    ("0202S2", "simple-present-temel-s2", "simple-present-temel", "kapanis", ""),
    ("0202S3", "simple-present-temel-s3", "simple-present-temel", "kanca", "Bu dersin S1 kol b'si de kanca değiştirir; onunla aynı değeri seçme (S1 taslağı yazıldıysa oku)."),
]

KANCA = """Değişken `kanca`: YALNIZ 1. sahne (ilk 3–4 sn: söz + ekran) değişir. Kol a'nın kanca türünü belirle (`soru` = tek soru cümlesi ·
`yanlis-cumle` = yanlış İngilizce cümle gösterip "hata nerede" · `kopru` = Türkçe söz → İngilizce karşılığı). Kol b için FARKLI bir tür seç ve
aynı bilgiye götüren yeni bir kanca yaz. Değer, kaydet ve çağrı sahneleri söz ve ekran olarak kol a ile BİREBİR aynı kalır; kanca cümlesi değer
sahnesinin ilk sözüne doğal bağlanmalı (bağlanmıyorsa değer sahnesinin YALNIZ ilk cümlesini uyarlayabilirsin; bunu açıkça işaretle, çünkü o
cümlenin sesi yeniden üretilir). Kanca değiştiği için kol b'nin A kapağı (kanca karesi) da değişir: `kapak-taslak.md` içine yalnız A kapağını yaz."""

KAPANIS = """Değişken `kapanis`: YALNIZ kaydet sahnesindeki kaydet kalıbı ve çağrı sahnesindeki giriş sözü değişir. Kol b değerleri SABİT (bütün
derslerde aynı çift sınanır): kaydet kalıbı `Ekran görüntüsü al, sınav günü bak.` · çağrı girişi `Konu burada bitmiyor.` Çekirdek cümle değişmez:
`Dersin tamamı YDS Publishing YouTube kanalında.` Kural özeti kartı, kanca ve değer sahneleri söz ve ekran olarak kol a ile BİREBİR aynı kalır.
Kaydet sahnesinin ekranı kalıba uymalı (ör. yer imi simgesi yerine ekran görüntüsü çerçevesi fikri; simge SVG, emoji yok)."""

SABLON = """# İstem BK-{kod} — {paket} için A/B deneme kolu (kol b) senaryo taslağı · değişken: {degisken} · 15.11.2026

MAKİNE: Linux x86_64 (srv21), kullanıcı sef. K=`/home/sef/01dev/_worktrees/kalem-0204` (worktree), D=`/home/sef/01dev/dijital-anlatim`.
Python `/usr/bin/python3 -I`. Skill `~/.claude/skills/motion-grafik-ders/`.
KURALLAR: Yalnız isteneni yaz. Silme yok. Ses sentezi yok, ElevenLabs çağrısı yok, render yok, sahne kodu yok, git commit yok, alt ajan yok,
agy-filo yok. Yazma YALNIZ `K/projeler/{paket}b/uretim-tutanagi/` altında (yeni paket dizini; aç). Kol a paketine (`K/projeler/{paket}/`) DOKUNMA.
Kanca atlama bayrağı oluşturma (`/tmp/conductor-*`, `~/.conductor/*`); sözleşme kancası isterse `K/.claude/docs/sozlesme.md` dosyasına 1 satır ekle.

## Amaç
Kısa videolarda A/B testi yapılacak: aynı konunun iki video kolu yayınlanır, kazanan yönde iyileştirilir. Kol a = var olan `{paket}`.
Sen kol b'nin (`{paket}b`) TASLAĞINI yazarsın. İki kol arasında TEK değişken değişir; gerisi birebir aynıdır (yoksa sonuç okunmaz).

## Okuma
1. BAĞLAYICI: `D/.claude/docs/huni-ab-sozlesme.md` (tamamı) ve `D/.claude/docs/huni-v2-standart.md` (§1–§7, §9).
2. Kol a: `K/projeler/{paket}/` — `ortak/anlatim/senaryo.json` (cümleler, kadro), `zaman.json` (sahne süreleri), `surumler.json`,
   `uretim-tutanagi/senaryo-taslak.md`, `kapak-taslak.md`, jüri dosyaları (`uretim-tutanagi/juri/` ya da `*-duzeltme.md`; aynı hatayı yapma),
   sahne klasörlerindeki `SPEC.md` (ekran metinleri).
3. Ana ders: `K/projeler/{ders}/ortak/anlatim/senaryo.json` (kanca için dersin kendi örnek cümlelerinden yararlan; dersle çelişme).
{ek}

## Değişken
{degisken_metni}

## Yaz
1. `senaryo-taslak.md` — 4 sahnelik tablo (sahne, konuşan, ses metni TR/EN parçalar, ekran metni, görsel fikir). Değişmeyen sahnelerin satırına
   "kol a ile aynı" yaz ve kol a metnini aynen kopyala. Değişen satırları **kalın** işaretle. Kurallar: ilk söz ≤ 1 sn; ekran metni sesten önce
   gelmez; rakam sözcükle; kısaltma okunmaz ("YDT" yerine "dil sınavı"); "Tam ders" ve süre sözü yok; yeni Türkçe cümleyi "jüri bakacak" diye işaretle;
   İngilizce cümle dilbilgisi olarak kusursuz (yanlış cümle kancasında yanlış cümle gerçekten yanlış, doğrusu gerçekten doğru).
   Süre tahmini: kol a'nın ölçülmüş süresinden farkı hesapla (sn); toplam 28 sn'yi aşmasın.
2. `kol-b.json` — makine biçimi:
   `{{"paket": "{paket}b", "kol_a": "{paket}", "varyant": {{"grup": "s<N>", "kol": "b", "degisken": "{degisken}", "deger": "…"}},
   "kol_a_deger": "…", "degisen_sahneler": ["<kol a sahne klasörü adı>", …], "ayni_sahneler": ["…"], "yeni_cumleler": [{{"sahne": "…",
   "konusan": "ogretmen|ogrenci", "metin": "…"}}], "onbellekten_cumleler": ["…"], "sure_tahmini_sn": 0.0}}`.
   Yazdıktan sonra `/usr/bin/python3 -I -c "import json;json.load(open('…'))"` ile ayrıştır.
3. `kapak-taslak.md` — yalnız değişken `kanca` ise: kol b'nin A kapağı (başlık ≤ 4 sözcük, 2 satır; kanal katmanı var; altyazı yok).
4. Öz denetim (`BK-RAPOR.md`): (a) tek değişken kuralı sağlandı mı, satır satır fark tablosu (kol a ↔ kol b); (b) dilbilgisi: her yeni İngilizce
   cümle ve kural için "kesin / jüri bakacak"; (c) huni v2 §5 altı ölçüt kol b için evet/hayır; (d) kol b kol a'dan neden farklı sonuç verebilir
   (bir cümle, varsayım); (e) açık noktalar.

Son mesajın en çok 10 satır: kol a değeri → kol b değeri, yeni kanca ya da kapanış sözü, süre farkı, yeniden seslendirilecek cümle sayısı, emin olmadığın nokta.
"""

hedef = Path(__file__).resolve().parent / "bk"
hedef.mkdir(exist_ok=True)
for kod, paket, ders, degisken, ek in KISALAR:
    metin = SABLON.format(kod=kod, paket=paket, ders=ders, degisken=degisken, ek=("4. " + ek) if ek else "",
                          degisken_metni=KANCA if degisken == "kanca" else KAPANIS)
    (hedef / f"BK-{kod}.md").write_text(metin, encoding="utf-8")
print(len(KISALAR), "istem:", hedef)
