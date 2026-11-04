// node --test testler/test_onizle_sunucu.mjs
import { test, before, after } from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { baslat } from '../ortak/onizle-sunucu.mjs';

let kok, sunucu, taban;
const istek = async (yontem, yol, govde) => {
  const r = await fetch(taban + yol, { method: yontem,
    headers: govde ? { 'Content-Type': 'application/json' } : {}, body: govde
      ? JSON.stringify(govde) : undefined });
  return { kod: r.status, veri: await r.json() };
};

before(async () => {
  kok = fs.mkdtempSync(path.join(os.tmpdir(), 'onizle-test-'));
  const d = path.join(kok, 'projeler', 'deneme');
  fs.mkdirSync(d, { recursive: true });
  fs.writeFileSync(path.join(d, 'surumler.json'), JSON.stringify({ video: { kimlik: 'deneme' },
    surumler: [{ kimlik: 'ana-yatay', tur: 'ana-yatay', ad: 'Ana', durum: 'inceleme' }],
      revizyonlar: [] }));
  fs.writeFileSync(path.join(d, 'gorevler.json'), '[]');
  fs.writeFileSync(path.join(d, 'yorumlar.json'), '[]');
  fs.mkdirSync(path.join(kok, 'projeler', 'katalog'), { recursive: true });
  fs.writeFileSync(path.join(kok, 'projeler/katalog/gorevler.json'), '[]');
  fs.writeFileSync(path.join(kok, 'projeler/katalog/yorumlar.json'), '[]');
  fs.writeFileSync(path.join(kok, 'projeler/katalog.json'), JSON.stringify({ uniteler: [{ kod: '01',
    konular: [{ kod: 'GR-01-01', videolar: [{ kimlik: '01-01-ydt-temel' }] }] }] }));
  fs.writeFileSync(path.join(kok, 'a.bin'), Buffer.from('0123456789'));
  sunucu = await baslat({ kok, port: 0 });
  taban = `http://127.0.0.1:${sunucu.address().port}`;
});
after(() => { sunucu.close(); fs.rmSync(kok, { recursive: true, force: true }); });

test('liste: üç dosya döner', async () => {
  assert.deepEqual((await istek('GET', '/api/deneme/gorevler')).veri, []);
  assert.equal((await istek('GET', '/api/deneme/surumler')).veri.surumler.length, 1);
  assert.deepEqual((await istek('GET', '/api/deneme/yorumlar')).veri, []);
  assert.equal((await istek('GET', '/api/yok/gorevler')).kod, 404);
});

test('görev ekle: kimlik, varsayılanlar, dosya, günlük', async () => {
  const r = await istek('POST', '/api/deneme/gorev', { baslik: 'Deneme görevi', grup: 'motor',
    surum: 'ana-yatay' });
  assert.equal(r.kod, 201);
  assert.equal(r.veri.kimlik, 'g-1');
  assert.equal(r.veri.durum, 'acik');
  const dosya = JSON.parse(fs.readFileSync(path.join(kok, 'projeler/deneme/gorevler.json'),
    'utf8'));
  assert.equal(dosya[0].baslik, 'Deneme görevi');
  const gunluk = fs.readFileSync(path.join(kok, 'projeler/deneme/gorev-gunlugu.jsonl'), 'utf8');
  assert.match(gunluk, /gorev-ekle/);
  const k = await istek('POST', '/api/deneme/gorev', { baslik: 'Karar', tur: 'karar' });
  assert.equal(k.veri.kimlik, 'g-2');
  assert.equal(k.veri.atanan, 'Nadir');
});

test('geçersiz enum 400', async () => {
  assert.equal((await istek('POST', '/api/deneme/gorev', { baslik: 'x', grup: 'yok' })).kod, 400);
  assert.equal((await istek('POST', '/api/deneme/gorev', { baslik: 'x', durum: 'bitti' })).kod,
    400);
  assert.equal((await istek('POST', '/api/deneme/gorev', {})).kod, 400);
  assert.equal((await istek('PATCH', '/api/deneme/gorev/g-1', { durum: 'bitti' })).kod, 400);
  assert.equal((await istek('PATCH', '/api/deneme/gorev/g-1', { kimlik: 'g-9' })).kod, 400);
});

test('durum değiştir (PATCH) ve eşzamanlı yazmada kimlik çakışmaz', async () => {
  const r = await istek('PATCH', '/api/deneme/gorev/g-1', { durum: 'uretimde', atanan: 'ajan' });
  assert.equal(r.kod, 200);
  assert.equal(r.veri.durum, 'uretimde');
  assert.equal((await istek('PATCH', '/api/deneme/gorev/g-99', { durum: 'onay' })).kod, 404);
  const hepsi = await Promise.all([1, 2, 3, 4, 5].map((i) => istek('POST', '/api/deneme/gorev',
    { baslik: `e${i}` })));
  assert.equal(new Set(hepsi.map((x) => x.veri.kimlik)).size, 5);
});

test('yorum ekle: görev üzerinden sürüm çıkar, t/sahne saklanır', async () => {
  const r = await istek('POST', '/api/deneme/yorum', { gorev: 'g-1', metin: 'Çizgi ince', t: 12.5,
    sahne: '02' });
  assert.equal(r.kod, 201);
  assert.equal(r.veri.kimlik, 'y-1');
  assert.equal(r.veri.surum, 'ana-yatay');
  assert.equal(r.veri.t, 12.5);
  assert.equal((await istek('POST', '/api/deneme/yorum', { metin: 'kime?' })).kod, 400);
  assert.equal((await istek('GET', '/api/deneme/yorumlar')).veri.length, 1);
});

test('sürüm ekle: türev görevi otomatik', async () => {
  const r = await istek('POST', '/api/deneme/surum',
    { tur: 'shorts', ad: 'Tanıtım kısa', kaynak: 'ana-yatay', senaryo_notu: 'spoiler yok' });
  assert.equal(r.kod, 201);
  assert.equal(r.veri.surum.kimlik, 'shorts-tanitim-kisa');
  assert.equal(r.veri.surum.durum, 'planli');
  assert.equal(r.veri.gorev.tur, 'turev');
  assert.equal(r.veri.gorev.surum, 'shorts-tanitim-kisa');
  const g = (await istek('GET', '/api/deneme/gorevler')).veri;
  assert.ok(g.some((x) => x.kimlik === r.veri.gorev.kimlik));
  assert.equal((await istek('POST', '/api/deneme/surum', { tur: 'film', ad: 'x' })).kod, 400);
});

test('katalog deposu: görev ve yorum video kimliğiyle saklanır', async () => {
  const g = await istek('POST', '/api/katalog/gorev', { video: '01-01-ydt-temel',
    baslik: 'Planlı iş' });
  assert.equal(g.kod, 201);
  assert.equal(g.veri.video, '01-01-ydt-temel');
  assert.equal((await istek('POST', '/api/katalog/gorev', { video: 'yok', baslik: 'x' })).kod, 400);
  assert.equal((await istek('POST', '/api/katalog/gorev', { baslik: 'x' })).kod, 400);
  const y = await istek('POST', '/api/katalog/yorum', { video: '01-01-ydt-temel', metin: 'Not' });
  assert.equal(y.kod, 201);
  assert.equal(y.veri.video, '01-01-ydt-temel');
  assert.equal((await istek('POST', '/api/katalog/yorum', { metin: 'kime?' })).kod, 400);
  assert.equal((await istek('GET', '/api/katalog/gorevler')).veri.length, 1);
  assert.equal((await istek('GET', '/api/deneme/gorevler')).veri.every((x) => x.video === 'deneme'),
    true);
});

test('statik: Range ve yol kaçışı', async () => {
  const r = await fetch(taban + '/a.bin', { headers: { Range: 'bytes=2-5' } });
  assert.equal(r.status, 206);
  assert.equal(await r.text(), '2345');
  assert.equal((await fetch(taban + '/%2e%2e/etc/passwd')).status >= 400, true);
});

test('port 3000 yasak, dolu port hata verir', async () => {
  await assert.rejects(baslat({ kok, port: 3000 }), /yasak/);
  await assert.rejects(baslat({ kok, port: sunucu.address().port }), /port dolu/);
});
