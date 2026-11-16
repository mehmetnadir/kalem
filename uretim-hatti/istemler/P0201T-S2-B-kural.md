# İstem P0201T-S2-B-kural — jüri (kaynak-kural) · present-continuous-s2 huni seti · 16.11.2026

ROL (a+b) KAYNAK ve KURAL denetçisi. Bak: can alıcı bilgi ve örnek ana dersle (senaryo.json, canAlici, jüri kararları) birebir tutarlı mı, dilbilgisi kuralı doğru mu; kalıp kuralları = `D/.claude/docs/huni-v2-standart.md` (ilk söz ≤ 1 sn; 4 sahne: kanca → değer → kaydet → çağrı; hedef 22–26 sn, kabul 35 sn, platform 60 sn; süre sözü ve "Tam ders" yok; çağrı sözü birebir "Dersin tamamı YDS Publishing YouTube kanalında."; kanal katmanı ilk kareden son kareye; kimlik @ydspublishing; rozet `YDT · TEMEL` / `YDT · İLERİ`); açıklamada uydurma adres yok, yer tutucular açık; UTM şeması huni-plan §6 ile aynı; 15 yaş dil kararı gerekçeli.

MAKİNE: Linux x86_64 (srv21), kullanıcı sef. K=`/home/sef/01dev/_worktrees/kalem-0204`, D=`/home/sef/01dev/dijital-anlatim`.
Python `/usr/bin/python3 -I`. Skill `~/.claude/skills/motion-grafik-ders/`.
KURALLAR: SALT OKUMA denetçisisin; tek yazma izni aşağıdaki çıktı dosyası. Taslağı düzeltme, yalnız değerlendir. Alt ajan açma.
Silme yok, commit yok, ses/render yok. Yazanla aynı kişi değilsin (yapan ≠ denetleyen).

Denetlenen (dizin `K/projeler/present-continuous-s2/uretim-tutanagi/`): ÇIKTI dosyaları (aşağıdaki GİRDİ); taslak md ve yazarın raporu yalnız karşılaştırma içindir.
Kaynak: ana ders `K/projeler/present-continuous/` (`ortak/anlatim/senaryo.json`, `surumler.json`, `uretim-tutanagi/juri.md`).
Kalıp: `D/.claude/docs/huni-v2-standart.md` (bağlayıcı; çelişirse bu geçer), `D/.claude/docs/dikey-senaryo-kalibi.md` §4–§5, `D/.claude/docs/huni-plan-1211.md` §4–§7.

GİRDİ — jüri TASLAĞI değil ÇIKTIYI görür (D-0338): son `senaryo.json`, ses dökümü (`sureler.json`, `sozcukler.json`), açıklama dosyaları (`aciklama*.md`), `surumler.json` ve kareler (her kip ve yön: açık + koyu, yatay + dikey, her kapak ve hikâye karesi). Taslak yalnız karşılaştırma içindir; hüküm ÇIKTIYA göre verilir. Bakılamayan dosya ya da kare = KALDI.
ÖLÇÜT: `D/.claude/docs/juri-olcutleri.md` — ilgili alt başlığın BÜTÜN maddelerine evet/hayır + kanıt.
JÜRİ KURALLARI: içerik her değiştiğinde jüri yeniden koşar. "Kaldı" maddesi kayda bırakılıp geçilmez; `KARAR: DÜZELT` yazılır. Kaynağa uygun ≠ doğru: kuralı bağımsız doğrula, ana dersteki hatayı da raporla (D-0205). Jüri modeli üretici oturumun modelinden farklıdır; tutanağa `MODEL: <ad>` satırı yaz.

Taslakların "Açık noktalar" listesinde kendi alanına düşen maddeleri tek tek cevapla (madde no + cevap + kanıt).

Çıktı: `K/projeler/present-continuous-s2/uretim-tutanagi/juri/s2.kaynak-kural.md` — ilk satır `KARAR: GEÇTİ` ya da `KARAR: DÜZELT`.
Sonra madde listesi: her madde = dosya + satır · sorun · kanıt (kaynak dosya + satır) · önerilen düzeltme.
Yalnız gerçek sorun yaz; zevk tercihi madde değildir. DÜZELT yalnız en az bir kanıtlı madde varsa.
Son mesajın en çok 8 satır: karar + madde sayısı + dosya yolu.

Emsal (jüriden geçmiş, 02-04 dersinin S1 kısası): `K/projeler/02-04-ydt-temel-s1/uretim-tutanagi/` — `S1-duzeltme.md` (7 madde) ve jüri dosyaları. Aynı hata burada tekrarlanmışsa madde yaz. Sürümler (A/B/C) gerçekten farklı mı, her biri kuralları ayrı ayrı sağlıyor mu bak.
