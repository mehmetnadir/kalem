# SPEC — `altyaziDilimle` (ortak/kunye.js) · 02-04-ydt-temel-dikey · 15.11.2026

Dosya (yalnız bu): `/home/sef/01dev/_worktrees/kalem-0204/projeler/02-04-ydt-temel-dikey/ortak/kunye.js`
Başka dosyaya dokunma. Silme yok. Test, render, git yok.

## Sorun
`kunyeHazirla()` altyazı parçalarını (`ortak/anlatim/altyazi.json`, alanlar `{cumle, dil, t0, t1, metin, konusan}`) okur.
02-04'te 13 parça 2 satıra sığmaz; en uzunu 226 karakter (cümle 8). `altyaziCiz` 36 px'e küçülür, 3 satırı aşınca
3. satırı yatay taşırır ve sözcük sırasını bozar (ölçüldü). `kunyeHazirla` içinde şu satır HAZIR (dokunma):
`altyazi = altyaziDilimle(altyazi, soz);` — `soz` = `ortak/anlatim/sozcukler.json` dizisi `{cumle, sozcuk, t0, t1}`.
Eksik olan yalnız `altyaziDilimle` işlevi.

## Yaz
`function altyaziSar(ctx, metin, genislik) {` satırının HEMEN ÜSTÜNE, modül düzeyinde (export YOK) `function altyaziDilimle(liste, soz)`.
Üstüne 1 satır yorum: amaç (2 satıra sığmayan parça sözcük zamanıyla dilimlenir; sözcük sayısı tutmazsa karakter oranı).

Davranış:
1. Ölçüm: `document.createElement("canvas").getContext("2d")`, font `500 ${KUNYE.altyaziYazi}px Lexend`,
   genişlik `W - 2 * KUNYE.kenar`. "Sığar" = dosyadaki `altyaziSar(ctx, metin, genislik)` sonucu en çok 2 satır.
2. Sığan parça olduğu gibi çıktıya girer (aynı nesne).
3. Sığmayan parça: sözcükler `metin.split(" ")`. Açgözlü gruplama: grup, bir sonraki sözcük eklenince sığmayacaksa kapanır.
   Her dilim parçanın bütün alanlarını taşır (`{...p}`), yalnız `metin`, `t0`, `t1` değişir.
4. Dilim zamanı: `soz` içinden `cumle === p.cumle` ve `p.t0 - 0.06 <= t0 < p.t1` olan sözcükler. Bunların sayısı parça
   sözcük sayısına EŞİTSE i. sözcüğün zamanı `z[i].t0`; eşit değilse (cümle 3 ve 9 TR parçasında sözcük eksik)
   `p.t0 + (p.t1 - p.t0) * (ilk i sözcüğün " " ile birleşik uzunluğu) / p.metin.length`.
5. Dilim `t0` = ilk sözcüğün zamanı (ilk dilimde bu `p.t0`'a eşit ya da çok yakın). Son olmayan dilimin `t1` = sonraki dilimin
   ilk sözcük zamanı − 0,4 (sebep: `altyaziMetin` `t < t1 + 0.35` kullanır; böylece sonraki dilim tam başlangıcında görünür).
   Son dilimin `t1` = `p.t1`.
6. Dönüş: düz dizi, zaman sırası korunur. `try/catch`, `Math.random`, `Date`, konsol yazısı yok.

## Biçim
2 boşluk girinti, satır ≤ 120 karakter (dosyanın kendi stili), `const`/ok işlevi; dosyadaki başka satır DEĞİŞMEZ.

## Kabul
1. `cp <dosya> /tmp/p1dikey/k.mjs && ~/.nvm/versions/node/v24.22.2/bin/node --check /tmp/p1dikey/k.mjs` çıkış 0.
2. `git -C /home/sef/01dev/_worktrees/kalem-0204 diff --stat` bu dosya dışında yeni değişiklik göstermez (paket git'te izlenmiyor;
   `ls -la` ile yalnız kunye.js mtime değişmeli).
Şef sonra tarayıcıda cümle 8 (t 120) ve cümle 7 (t 105) altyazısını çizip bakar.
