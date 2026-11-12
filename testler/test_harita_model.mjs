// node --test testler/test_harita_model.mjs
import { test } from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import { fileURLToPath } from 'node:url';
import path from 'node:path';
import * as M from '../ortak/editor/harita-model.js';

const kok = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const katalog = JSON.parse(fs.readFileSync(path.join(kok, 'projeler/katalog.json'), 'utf8'));
const agac = M.agacKur(katalog);
const pilotSurumler = { video: { kimlik: 'present-continuous' },
  surumler: [{ kimlik: 'ana-yatay', ad: 'Ana', durum: 'inceleme' }, { kimlik: 'dikey', ad: 'Dikey',
    durum: 'planli' }] };

test('katalog: 12 ünite, 153 konu, 195 kaynak, 612 video', () => {
  assert.deepEqual(M.sayimlar(agac), { unite: 12, konu: 153, kaynak: 195, video: 612 });
});

test('pilot videoya proje sürümleri bağlanır, projesiz videoya bağlanmaz', () => {
  M.projeBagla(agac, { 'present-continuous': { sv: pilotSurumler,
    gorevler: [{ kimlik: 'g-1' }] } });
  const pilot = agac.video.get('02-01-ydt-temel');
  assert.equal(pilot.proje, 'present-continuous');
  assert.equal(pilot.surumler.length, 2);
  assert.equal(agac.video.get('02-01-ydt-ileri').surumler.length, 0);
  const gor = M.videoGorevleri(pilot, { 'present-continuous': { gorevler: [{ kimlik: 'g-1' }] } },
    []);
  assert.equal(gor.length, 1);
  const depo = [{ kimlik: 'g-1', video: '02-01-ydt-ileri' }, { kimlik: 'g-2', video: 'baska' }];
  assert.equal(M.videoGorevleri(agac.video.get('02-01-ydt-ileri'), {}, depo).length, 1);
});

test('ünite durum dağılımı toplamı = ünite video sayısı; genel toplam 612', () => {
  let toplam = 0;
  for (const u of agac.uniteler) {
    const o = M.uniteOzet(u);
    const s = Object.values(o.dagilim).reduce((a, b) => a + b, 0);
    assert.equal(s, o.video);
    assert.equal(o.video, u.konular.length * 4);
    toplam += s;
  }
  assert.equal(toplam, 612);
  const u2 = M.uniteOzet(agac.unite.get('02'));
  const u2Ham = katalog.uniteler.find((u) => u.kod === '02');
  const u2BeklenenUretimde = (u2Ham?.konular || [])
    .flatMap((k) => k.videolar || [])
    .filter((v) => v.durum === 'uretimde').length;
  assert.equal(u2.dagilim.uretimde, u2BeklenenUretimde);
  assert.ok(u2.dagilim.uretimde > 0);
  assert.ok(u2.sureDk > 0 && u2.ortYuzde > 0);
});

test('konu özeti: süre ve izlenme kaynak videoların toplamı', () => {
  const o = M.konuOzet(agac.konu.get('02-01'));
  assert.equal(o.sure, 770 + 1003);
  assert.equal(o.izlenme, 1178 + 246);
});

test('URL: ?ac= çözümleme, üretme, ata kapanımı', () => {
  const s = M.urlCoz(agac, '02-01-ydt-temel');
  assert.deepEqual([...s].sort(), ['02', '02-01', '02-01-ydt-temel']);
  assert.equal(M.urlUret(M.urlCoz(agac, '02,02-01,02-01-ydt-temel')), '02,02-01,02-01-ydt-temel');
  assert.equal(M.urlCoz(agac, 'yok,99').size, 0);
  assert.equal(M.sonKimlik(agac, '02,02-01,yok'), '02-01');
  const sv = M.urlCoz(agac, '02-01-ydt-temel/ana-yatay');
  assert.ok(sv.has('02-01-ydt-temel/ana-yatay') && sv.has('02'));
});

test('açık-küme işlemleri: aç, kapa, değiştir, hepsi', () => {
  let s = M.hepsiniKapat();
  s = M.ac(s, '02'); assert.ok(s.has('02'));
  s = M.degistir(s, '02'); assert.equal(s.size, 0);
  s = M.degistir(s, '03'); assert.ok(s.has('03'));
  assert.equal(M.kapat(s, '03').size, 0);
  M.projeBagla(agac, { 'present-continuous': { sv: pilotSurumler, gorevler: [] } });
  const hepsi = M.hepsiniAc(agac);
  assert.equal(hepsi.size, 12 + 153 + 612 + 2);
  assert.equal(M.hepsiniKapat().size, 0);
});

test('derinlik: konu -> ünite+konu açık, video kapalı', () => {
  const s = M.derinlik(agac, 'konu');
  assert.ok(s.has('02') && s.has('02-01'));
  assert.ok(!s.has('02-01-ydt-temel'));
  const u = M.derinlik(agac, 'unite');
  assert.ok(u.has('02') && !u.has('02-01'));
  const v = M.derinlik(agac, 'video');
  assert.ok(v.has('02-01-ydt-temel') && !v.has('02-01-ydt-temel/ana-yatay'));
  assert.ok(M.derinlik(agac, 'hepsi').has('02-01-ydt-temel/ana-yatay'));
  assert.throws(() => M.derinlik(agac, 'x'));
});

test('arama "tenses - 01": yol açılır, eşleşmeyen canlı değil', () => {
  const r = M.arama(agac, 'Tenses - 01');
  assert.ok(r.eslesen.has('02-01'));
  assert.ok(r.ac.has('02') && r.ac.has('02-01'));
  assert.ok(r.canli.has('02-01-ydt-temel') && r.canli.has('02'));
  assert.ok(!r.canli.has('01'));
  assert.equal(M.arama(agac, '  ').aktif, false);
  assert.ok(M.arama(agac, 'ING-YDT-GR-02-01-T').eslesen.has('02-01-ydt-temel'));
  assert.ok(M.arama(agac, '02-01-maarif-ileri').ac.has('02-01'));
});

test('filtre: kitle ve video durumu', () => {
  const v = agac.video.get('02-01-ydt-temel');
  assert.ok(M.videoGecer(v, { kitle: 'ydt', vdurum: 'uretimde' }));
  assert.ok(!M.videoGecer(v, { kitle: 'maarif' }));
  assert.ok(M.videoGecer(v, {}));
  assert.equal(M.filtreAktif({}), false);
});

test('yol: video, konu, sürüm atalarını döndürür', () => {
  assert.deepEqual(M.yol(agac, '02-01-ydt-temel'), ['02', '02-01', '02-01-ydt-temel']);
  assert.deepEqual(M.yol(agac, '02-01-ydt-temel/ana-yatay'), ['02', '02-01', '02-01-ydt-temel',
    '02-01-ydt-temel/ana-yatay']);
});

test('kırıntı: Harita > ünite > konu > video, bağlantı ac/sec taşır', () => {
  const k = M.kirinti(katalog, '02,02-01,02-01-ydt-temel');
  assert.equal(k.length, 4);
  assert.equal(k[0].ad, 'Harita');
  assert.match(k[1].ad, /^02 /);
  assert.equal(k[2].ad, '02-01 tenses - 01');
  assert.equal(k[3].ad, 'YDT temel');
  assert.deepEqual([k[1].ac, k[1].sec], ['02', '02']);
  assert.deepEqual([k[3].ac, k[3].sec], ['02,02-01,02-01-ydt-temel', '02-01-ydt-temel']);
  assert.equal(M.kirintiAdresi(k[1]), 'harita.html?ac=02&sec=02');
  assert.equal(M.kirintiAdresi(k[0]), 'harita.html');
  assert.deepEqual(M.projeYolu(katalog, 'present-continuous'), ['02', '02-01', '02-01-ydt-temel']);
  assert.deepEqual(M.projeYolu(katalog, 'yok'), []);
});

test('sec çözümü: video panel açar, ünite/konu açmaz; bilinmeyen null', () => {
  const v = M.secCoz(agac, '02-01-ydt-temel');
  assert.ok(v.panel && v.ac.has('02') && v.ac.has('02-01') && !v.ac.has('02-01-ydt-temel'));
  const u = M.secCoz(agac, '02');
  assert.ok(!u.panel && u.ac.has('02'));
  const q = M.secCoz(agac, '02-01');
  assert.ok(!q.panel && q.ac.has('02') && !q.ac.has('02-01'));
  assert.equal(M.secCoz(agac, 'yok'), null);
});
