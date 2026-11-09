// Önizleme sunucusu koşullu istek ve ETag testleri — node --test araclar/test/
import { test } from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const KOK = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..');
const { baslat, dogrulayici, etagEslesir, imsEslesir, ifRangeGecerli } = await import(
  path.join(KOK, 'ortak', 'onizle-sunucu.mjs')
);

test('saf doğrulayıcı yardımcı fonksiyonları', () => {
  const d = dogrulayici({ size: 100, mtimeMs: 1700000000000 });
  assert.equal(d.etag, `W/"100-${(1700000000000).toString(36)}"`);
  assert.equal(d.sonMod, new Date(1700000000000).toUTCString());

  assert.equal(etagEslesir('*', d.etag), true);
  assert.equal(etagEslesir(d.etag, d.etag), true);
  assert.equal(etagEslesir(d.etag.replace(/^W\//, ''), d.etag), true);
  assert.equal(etagEslesir(`W/"farkli", ${d.etag}`, d.etag), true);
  assert.equal(etagEslesir('W/"farkli"', d.etag), false);

  assert.equal(imsEslesir(d.sonMod, 1700000000000), true);
  assert.equal(imsEslesir(new Date(1699999999000).toUTCString(), 1700000000000), false);

  assert.equal(ifRangeGecerli(d.etag, d.etag, 1700000000000), true);
  assert.equal(ifRangeGecerli('W/"baska"', d.etag, 1700000000000), false);
});

test('önizleme sunucusu koşullu istek akışı', { timeout: 5000 }, async () => {
  const gecici = fs.mkdtempSync(path.join(os.tmpdir(), 'kalem-onizle-test-'));
  const ortakDizin = path.join(gecici, 'ortak');
  fs.mkdirSync(ortakDizin, { recursive: true });

  const cssYol = path.join(ortakDizin, 'a.css');
  fs.writeFileSync(cssYol, Buffer.alloc(100, 0x61));
  const baslangicMtime = 1700000000;
  fs.utimesSync(cssYol, baslangicMtime, baslangicMtime);

  const sesYol = path.join(gecici, 'ses.bin');
  fs.writeFileSync(sesYol, Buffer.alloc(5000, 0x42));

  const projeDizin = path.join(gecici, 'projeler', 'demo');
  fs.mkdirSync(projeDizin, { recursive: true });
  fs.writeFileSync(path.join(projeDizin, 'gorevler.json'), '[]\n');

  const sunucu = await baslat({ kok: gecici, port: 0, adres: '127.0.0.1' });
  const port = sunucu.address().port;
  const temel = `http://127.0.0.1:${port}`;

  try {
    // (a) GET -> 200, ETag W/" ile başlar, Last-Modified var, Cache-Control no-cache
    const resA = await fetch(`${temel}/ortak/a.css`);
    assert.equal(resA.status, 200);
    const etagA = resA.headers.get('etag');
    assert.ok(etagA && etagA.startsWith('W/"'));
    const lmA = resA.headers.get('last-modified');
    assert.ok(lmA);
    assert.equal(resA.headers.get('cache-control'), 'no-cache');
    const govdeA = await resA.text();
    assert.equal(govdeA.length, 100);

    // (b) aynı ETag ile If-None-Match -> 304, gövde boş, ETag aynı
    const resB = await fetch(`${temel}/ortak/a.css`, {
      headers: { 'if-none-match': etagA },
    });
    assert.equal(resB.status, 304);
    assert.equal(resB.headers.get('etag'), etagA);
    assert.equal(resB.headers.get('cache-control'), 'no-cache');
    const govdeB = await resB.text();
    assert.equal(govdeB, '');

    // (c) If-Modified-Since = Last-Modified -> 304
    const resC = await fetch(`${temel}/ortak/a.css`, {
      headers: { 'if-modified-since': lmA },
    });
    assert.equal(resC.status, 304);
    assert.equal(resC.headers.get('etag'), etagA);
    const govdeC = await resC.text();
    assert.equal(govdeC, '');

    // (d) Range bytes=0-99 -> 206, Content-Range, ETag var; If-None-Match -> 304
    const resD1 = await fetch(`${temel}/ses.bin`, {
      headers: { range: 'bytes=0-99' },
    });
    assert.equal(resD1.status, 206);
    assert.equal(resD1.headers.get('content-range'), 'bytes 0-99/5000');
    const etagSes = resD1.headers.get('etag');
    assert.ok(etagSes && etagSes.startsWith('W/"'));
    const tamponD1 = await resD1.arrayBuffer();
    assert.equal(tamponD1.byteLength, 100);

    const resD2 = await fetch(`${temel}/ses.bin`, {
      headers: { range: 'bytes=0-99', 'if-none-match': etagSes },
    });
    assert.equal(resD2.status, 304);
    const govdeD2 = await resD2.text();
    assert.equal(govdeD2, '');

    // If-Range uymuyorsa Range yok sayılıp 200 tam gövde döner
    const resD3 = await fetch(`${temel}/ses.bin`, {
      headers: { range: 'bytes=0-99', 'if-range': 'W/"uyumsuz"' },
    });
    assert.equal(resD3.status, 200);
    const tamponD3 = await resD3.arrayBuffer();
    assert.equal(tamponD3.byteLength, 5000);

    // (e) dosya değişince (yaz + mtime ileri) eski ETag ile -> 200 yeni ETag
    fs.writeFileSync(cssYol, Buffer.alloc(120, 0x62));
    const yeniMtime = baslangicMtime + 100;
    fs.utimesSync(cssYol, yeniMtime, yeniMtime);

    const resE = await fetch(`${temel}/ortak/a.css`, {
      headers: { 'if-none-match': etagA },
    });
    assert.equal(resE.status, 200);
    const etagE = resE.headers.get('etag');
    assert.ok(etagE && etagE.startsWith('W/"'));
    assert.notEqual(etagE, etagA);
    const govdeE = await resE.text();
    assert.equal(govdeE.length, 120);

    // (f) /api/... yanıtında ETag YOK ve Cache-Control no-store
    const resF = await fetch(`${temel}/api/demo/gorevler`);
    assert.equal(resF.status, 200);
    assert.equal(resF.headers.get('etag'), null);
    assert.equal(resF.headers.get('cache-control'), 'no-store');
  } finally {
    await new Promise((coz) => sunucu.close(coz));
  }
});
