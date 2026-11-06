// node --test testler/test_editor_yol.mjs
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { createRequire } from 'node:module';

const Y = createRequire(import.meta.url)('../ortak/editor/yol.js');

test('projeAdi: yeni ve eski adresten okunur, başka yol null', () => {
  assert.equal(Y.projeAdi('/p/present-continuous/harita.html'), 'present-continuous');
  assert.equal(Y.projeAdi('/projeler/deneme/onizle.html'), 'deneme');
  assert.equal(Y.projeAdi('/api/deneme/gorevler'), null);
  assert.equal(Y.projeAdi('/'), null);
});

test('projeYolu: veri dizini mutlak yol', () => {
  assert.equal(Y.projeYolu('present-continuous'), '/projeler/present-continuous/');
});

test('editorYolu: sorgu metin ya da nesne, ad verilmezse yoldan', () => {
  assert.equal(Y.editorYolu('harita.html', 'ac=02&sec=02', 'x'), '/p/x/harita.html?ac=02&sec=02');
  assert.equal(Y.editorYolu('onizle.html', { surum: 'ana-yatay', t: 3 }, 'x'),
    '/p/x/onizle.html?surum=ana-yatay&t=3');
  assert.equal(Y.editorYolu('harita.html', '', 'x'), '/p/x/harita.html');
});

test('editorYolu: ad verilmezse konumdan okunur', () => {
  globalThis.location = { pathname: '/p/deneme/onizle.html' };
  try {
    assert.equal(Y.editorYolu('harita.html'), '/p/deneme/harita.html');
  } finally { delete globalThis.location; }
});

test('ciktiYolu: sürüm önizlemesinden proje videosu, önizlemesiz sürüm null', () => {
  assert.equal(Y.ciktiYolu('/p/present-continuous-s1/onizle.html'),
    '/projeler/present-continuous-s1/cikti.mp4');
  assert.equal(Y.ciktiYolu('/projeler/x/onizle.html?t=3', true), '/projeler/x/cikti-koyu.mp4');
  assert.equal(Y.ciktiYolu(null), null);
  assert.equal(Y.ciktiYolu('/api/x/surumler'), null);
});

test('yeniAdres: eski editör adresi yeniye, diğerleri aynen', () => {
  assert.equal(Y.yeniAdres('/projeler/x/onizle.html?a=1'), '/p/x/onizle.html?a=1');
  assert.equal(Y.yeniAdres('/projeler/x/cikti.mp4'), '/projeler/x/cikti.mp4');
  assert.equal(Y.yeniAdres(null), null);
});
