# İstem B — jüri (kural) · 02-04-ydt-temel · 14.11.2026

ROL (b) KURAL denetçisi. Bak: skill `SKILL.md` (iskelet 8 bölüm ve süre payları, öğrenci 2 soru + 1 yanlış cevap),
`references/soru-ani.md`, `references/kliseler.md`, `references/hareket-sozlugu.md` (görsel fikirdeki olay adları gerçek mi),
`references/tempo-ve-pedagoji.md`, defter `D/.claude/docs/grammar-defter.md` son 120 satır (Nadir notları; D-0204, D-0205 kararları:
believe/think etiketsiz, these days mutlak değil vb.). Ayrıca: süre iddiası yok mu; konuşmada "YDT" kısaltması yok mu ("dil sınavı").

MAKİNE: Linux x86_64 (srv21), kullanıcı sef. K=`/home/sef/01dev/_worktrees/kalem-0204`, D=`/home/sef/01dev/dijital-anlatim`.
Python `/usr/bin/python3 -I`. Skill `~/.claude/skills/motion-grafik-ders/`.
KURALLAR: SALT OKUMA denetçisisin; tek yazma izni aşağıdaki çıktı dosyası. Senaryoyu düzeltme, yalnız değerlendir. Alt ajan açma.
Silme yok, commit yok, ses/render yok. Yazanla aynı kişi değilsin (yapan ≠ denetleyen).

Kararlar (Kovan defteri, sunucudaki grammar-defter.md'de yok; aynen):
- D-0204 (13.11): Senaryo onayı 3 kişilik jüride (kaynak, kural, dil); yazan jüride yok; 2 turda geçmeyen Nadir'e gelir. Ölçüt: kaynaklara ve ppt ders akışına uygunluk.
- D-0205 (13.11): Jüri çelişkisi şefte çözülür: kaynağın kuralı korunur; yanlış kategori etiketi verilmez (believe/think 'performative' denmez, yalnız recommend/promise/agree); kaynakta olmayan karşı kural eklenmez (these days/nowadays).

Denetlenen: `K/projeler/02-04-ydt-temel/uretim-tutanagi/senaryo-taslak.md` (ders 02-04-ydt-temel "Simple Present vs Present Continuous", YDT temel).
Yazarın girdi dökümü: `K/projeler/02-04-ydt-temel/uretim-tutanagi/istem/A-girdi.md`.
Biçim örneği (önceki dersin jüri sonucu): `K/projeler/02-03-ydt-temel/uretim-tutanagi/juri.md`.

Taslağın sonundaki "Açık noktalar" listesinde kendi alanına düşen maddeleri tek tek cevapla (madde no + cevap + kanıt).

Çıktı: `K/projeler/02-04-ydt-temel/uretim-tutanagi/juri/02-04-ydt-temel.kural.md` — ilk satır `KARAR: GEÇTİ` ya da `KARAR: DÜZELT`.
Sonra madde listesi: her madde = taslak satırı (bölüm + #) · sorun · kanıt (kaynak dosya + satır/slayt/zaman) · önerilen düzeltme.
Yalnız gerçek sorun yaz; zevk tercihi madde değildir. DÜZELT yalnız en az bir kanıtlı madde varsa.
Son mesajın en çok 8 satır: karar + madde sayısı + dosya yolu.
