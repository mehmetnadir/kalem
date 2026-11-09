// Editör (onizle.js) ortak çekirdeğin (cekirdek.js) yardımcılarını yalnız C.<ad>( ile çağırır.
// 09.11: çıplak slotBul( çağrıları kaldı → arayuz her karede ReferenceError, editör açılmadı.
import { test } from "node:test";
import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const KOK = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..", "..");
const cekirdek = fs.readFileSync(path.join(KOK, "ortak/oynatici/cekirdek.js"), "utf8");
const editor = fs.readFileSync(path.join(KOK, "ortak/editor/onizle.js"), "utf8");

test("onizle.js çekirdek yardımcılarını çıplak adla çağırmaz", () => {
  const adlar = [...cekirdek.matchAll(/^\s{2}function ([A-Za-z_]\w*)\(/gm)].map((m) => m[1]);
  assert.ok(adlar.includes("slotBul") && adlar.includes("sahneYonet"), "çekirdek adları: " + adlar);
  const yerel = new Set([...editor.matchAll(/^\s*function ([A-Za-z_]\w*)\(/gm)].map((m) => m[1]));
  const ciplak = [];
  for (const ad of adlar) {
    if (yerel.has(ad)) continue;                      // editörün kendi sarmalayıcısı (ör. sahneNo)
    const re = new RegExp("(^|[^.\\w])" + ad + "\\(", "g");
    for (const m of editor.matchAll(re)) {
      const satir = editor.slice(0, m.index).split("\n").length;
      ciplak.push(ad + " @" + satir);
    }
  }
  assert.deepEqual(ciplak, [], "çıplak çağrı: " + ciplak.join(", "));
});

test("onizle.html çekirdeği mutlak yoldan yükler (/p/ altında göreli yol kırılır)", () => {
  const html = fs.readFileSync(path.join(KOK, "ortak/editor/onizle.html"), "utf8");
  assert.match(html, /src="\/ortak\/oynatici\/cekirdek\.js"/);
});
