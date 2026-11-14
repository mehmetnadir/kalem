# İstem B — jüri (dil) · 02-04-ydt-temel · 14.11.2026

ROL (c) DİL denetçisi. Bak: İngilizce örneklerin dilbilgisi doğruluğu ve doğallığı, YDT temel düzeyine uygunluğu, Türkçe
açıklamaların doğruluğu ve akıcılığı, Türkçe karşılıklar, kısaltma yok, ses metni yazımı (`references/ses-tasarimi.md`, sözlük
`D/araclar/iki-dilli/ses-sozluk.json`: -ing, özne I, tire kuralı, rakam yerine sözcük). Seslendirmede yanlış okunabilecek yerleri işaretle.

MAKİNE: Linux x86_64 (srv21), kullanıcı sef. K=`/home/sef/01dev/_worktrees/kalem-0204`, D=`/home/sef/01dev/dijital-anlatim`.
Python `/usr/bin/python3 -I`. Skill `~/.claude/skills/motion-grafik-ders/`.
KURALLAR: SALT OKUMA denetçisisin; tek yazma izni aşağıdaki çıktı dosyası. Senaryoyu düzeltme, yalnız değerlendir. Alt ajan açma.
Silme yok, commit yok, ses/render yok. Yazanla aynı kişi değilsin (yapan ≠ denetleyen).

Denetlenen: `K/projeler/02-04-ydt-temel/uretim-tutanagi/senaryo-taslak.md` (ders 02-04-ydt-temel "Simple Present vs Present Continuous", YDT temel).
Yazarın girdi dökümü: `K/projeler/02-04-ydt-temel/uretim-tutanagi/istem/A-girdi.md`.
Biçim örneği (önceki dersin jüri sonucu): `K/projeler/02-03-ydt-temel/uretim-tutanagi/juri.md`.

Taslağın sonundaki "Açık noktalar" listesinde kendi alanına düşen maddeleri tek tek cevapla (madde no + cevap + kanıt).

Çıktı: `K/projeler/02-04-ydt-temel/uretim-tutanagi/juri/02-04-ydt-temel.dil.md` — ilk satır `KARAR: GEÇTİ` ya da `KARAR: DÜZELT`.
Sonra madde listesi: her madde = taslak satırı (bölüm + #) · sorun · kanıt (kaynak dosya + satır/slayt/zaman) · önerilen düzeltme.
Yalnız gerçek sorun yaz; zevk tercihi madde değildir. DÜZELT yalnız en az bir kanıtlı madde varsa.
Son mesajın en çok 8 satır: karar + madde sayısı + dosya yolu.
