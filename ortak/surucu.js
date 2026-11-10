// Sayfa tarafı sürücü. kur() bir kez, kare(f) her kare için çağrılır; kare(f) çizilmiş canvas döndürür.
// Fontlar: Fell (IM Fell, başlık), Garamond (EB Garamond, metin) /ortak/font altından yüklenir.
// Canlı kip (?canli=1): kareler POST edilmez, görünür canvas'ta gerçek zamanlı oynar (render öncesi izleme).
//   ?ses=<wav yolu>&tbas=<sn>: anlatım sesi ve sahnenin küresel başlangıcı.
//   Üst sayfa {tip:"zaman", t} mesajı da yollayabilir (t = anlatım zamanı, sn).
//   ?mesaj=1 (editör iframe tamponu): kendi saati ve sesi YOK; yalnız mesaj zamanıyla çizer (mesaj gelene dek
//   kare 0). İlk kare çizilince üst sayfaya {tip:"hazir", tbas} yollar ({tip:"sor"} gelirse yeniden yollar).
//   {tip:"kare"} mesajı: o anki kareyi PNG indirir (yalnız canvas sahneleri).
//   Boşluk: durdur/sürdür · ok tuşları: ±1 kare (duraklamışken) · k: o anki kareyi PNG indir.
const CANLI = () => new URLSearchParams(location.search).get("canli") === "1" || globalThis.canli === true;

export function canliCekirdek({ fps, KARE, ciz, indir }) {
  const Q = new URLSearchParams(location.search);
  const tbas = parseFloat(Q.get("tbas") || "0"), sesYol = Q.get("ses");
  const MESAJ = Q.get("mesaj") === "1";
  const ses = MESAJ ? null : sesYol ? new Audio(sesYol) : document.querySelector("audio");
  const d = { dur: false, f: 0, mesajT: null, t0: performance.now() };
  const say = document.createElement("div");
  say.style.cssText = "position:fixed;left:8px;top:8px;padding:4px 10px;font:14px monospace;color:#fff;" +
    "background:rgba(0,0,0,.45);border-radius:6px;z-index:99;pointer-events:none";
  document.body.appendChild(say);
  const sar = (f) => { d.t0 = performance.now() - (f / fps) * 1000; if (ses) ses.currentTime = tbas + f / fps; };
  const oynat = () => { if (ses) ses.play().catch(() => {}); };
  const zaman = () => MESAJ ? (d.mesajT === null ? 0 : d.mesajT - tbas) : (d.mesajT !== null ? d.mesajT - tbas
    : ses && !ses.paused ? ses.currentTime - tbas : (performance.now() - d.t0) / 1000);
  addEventListener("message", (e) => {
    if (e.data && e.data.tip === "zaman") { d.mesajT = e.data.t; if (ses) ses.pause(); }
    else if (e.data && e.data.tip === "kare" && indir) indir(d.f);
    else if (e.data && e.data.tip === "sor" && hazir) parent.postMessage({ tip: "hazir", tbas }, "*");
  });
  addEventListener("keydown", (e) => {
    if (MESAJ) return;
    if (e.key === " ") {
      e.preventDefault(); d.dur = !d.dur;
      if (d.dur) { if (ses) ses.pause(); } else { sar(d.f); oynat(); }
    } else if (d.dur && (e.key === "ArrowRight" || e.key === "ArrowLeft"))
      d.f = Math.max(0, Math.min(KARE - 1, d.f + (e.key === "ArrowRight" ? 1 : -1)));
    else if (e.key === "k" && indir) indir(d.f);
  });
  sar(0); if (!MESAJ) oynat();
  let son = -1, mesgul = false, hata = "", hazir = false, onay = false;
  if (MESAJ) say.style.display = "none";
  const dongu = async () => {
    if (!d.dur) {
      let f = Math.floor(zaman() * fps);
      if (f >= KARE) { if (d.mesajT === null) { f = 0; sar(0); oynat(); } else f = KARE - 1; }
      d.f = Math.max(0, f);
    }
    if (d.f !== son && !mesgul) {
      mesgul = true;
      try { await ciz(d.f); } catch (e) { hata = "HATA " + e; }
      son = d.f; mesgul = false;
      if (!hazir && !hata) { hazir = true; parent.postMessage({ tip: "hazir", tbas }, "*"); }
    }
    if (MESAJ && hazir && !onay && d.mesajT !== null && !mesgul && son === d.f) {
      onay = true; parent.postMessage({ tip: "hazir", tbas, zamanli: true }, "*");
    }
    say.textContent = hata || `${d.f} / ${KARE}  ·  ${(d.f / fps).toFixed(2)} sn${d.dur ? "  (durdu)" : ""}`;
    requestAnimationFrame(dongu);
  };
  requestAnimationFrame(dongu);
}

// HyperFrames sayfaları: gsap zaman çizelgesi (paused) canlı kipte kare sayacına bağlanır.
export function canliHF(tl, fps = 30) {
  const kok = document.getElementById("root"), sure = parseFloat(kok.dataset.duration);
  const gen = parseFloat(kok.dataset.width) || 1920;    // dikey sahne: data-width/height
  const yuk = parseFloat(kok.dataset.height) || 1080;
  const olc = () => {
    kok.style.transformOrigin = "0 0";
    kok.style.transform = `scale(${Math.min(innerWidth / gen, innerHeight / yuk)})`;
  };
  document.body.style.overflow = "hidden"; olc(); addEventListener("resize", olc);
  tl.pause();
  canliCekirdek({ fps, KARE: Math.ceil(sure * fps), ciz: (f) => { tl.time(f / fps, false); } });
}

export async function surucu(kur, kare, KARE = 240, fps = 30) {
  const yerel = /^(localhost|127\.0\.0\.1|\[::1\]|10\.\d+\.\d+\.\d+|192\.168\.\d+\.\d+)$/
    .test(location.hostname);                    // POST /log yalnız yerel sunucuda (10.11)
  const log = (m) => (yerel ? fetch("/log", { method: "POST", body: String(m) })
    : Promise.resolve());
  try {
    for (const [ad, dosya, stil] of [["Fell", "IMFeENrm28P.ttf", "normal"], ["Fell", "IMFeENit28P.ttf", "italic"], ["Garamond", "EBGaramond.ttf", "normal"], ["Garamond", "EBGaramond-Italic.ttf", "italic"]]) {
      const f = new FontFace(ad, `url(/ortak/font/${dosya})`, { style: stil }); await f.load(); document.fonts.add(f);
    }
    await kur();
    if (CANLI()) return canliKare(kare, KARE, fps);
    for (let f = 0; f < KARE; f++) {
      const cv = await kare(f);
      const b = await new Promise((ok) => cv.toBlob(ok, "image/png"));
      await fetch("/kare?i=" + f, { method: "POST", body: b });
    }
    await fetch("/bitti", { method: "POST", body: "tamam" });
  } catch (e) { await log("HATA " + (e.stack || e)); await fetch("/bitti", { method: "POST", body: "hata " + e }); }
}

// Canlı kip: sahne canvas'ı gizlenir, kare(f) çıktısı görünür canvas'a kopyalanır; boyut kare canvas'ından
// (yatay 1920x1080, dikey 1080x1920) — sabit 1920x1080 dikey sahneyi 16:9'a eziyordu (04.11).
function canliKare(kare, KARE, fps) {
  document.querySelectorAll("body > canvas").forEach((c) => { c.style.display = "none"; });
  document.body.style.cssText += ";margin:0;background:#111;overflow:hidden";
  const cv = document.createElement("canvas"); cv.width = 1920; cv.height = 1080;
  cv.style.cssText = "display:block;margin:auto;max-width:100vw;height:auto;max-height:100vh";
  document.body.appendChild(cv);
  // alpha:false (10.11, ölçümle): tuval her karede tam kopyayla dolar, saydamlık gerekmez; opak katman
  // compositor'da harmanlanmaz. Başsız cpu4: sahne 22 → 28 kare/sn. Bu tuvale metin çizilmez
  // (opak tuvalde LCD metin AA riski yok).
  const g = cv.getContext("2d", { alpha: false });
  canliCekirdek({
    fps, KARE,
    ciz: async (f) => {
      const c = await kare(f);
      if (cv.width !== c.width || cv.height !== c.height) { cv.width = c.width; cv.height = c.height; }
      g.drawImage(c, 0, 0);
    },
    indir: (f) => cv.toBlob((b) => {
      const a = document.createElement("a"); a.href = URL.createObjectURL(b);
      a.download = "kare-" + String(f).padStart(4, "0") + ".png"; a.click();
    }, "image/png"),
  });
}
