// Geçiş kaynağı: önce ortak/gecis-ozel/<ad>.glsl (kendi şaderlerimiz), yoksa gl-transitions.
// Özel dosyanın ilk satırlarındaki "// kare: 32" ve "// ease: lineer|yumusak" üst bilgisi okunur.
const GL = "/motorlar/yardimci/node_modules/gl-transitions/gl-transitions.json";

export async function trBul(ad) {
  const r = await fetch(`/ortak/gecis-ozel/${ad}.glsl`);
  if (r.ok) {
    const glsl = await r.text();
    const ust = (a, v) => (glsl.match(new RegExp(`^// ${a}: *(\\S+)`, "m")) || [])[1] ?? v;
    return { name: ad, glsl, paramsTypes: {}, defaultParams: {}, ease: ust("ease", "yumusak"),
      kare: +ust("kare", 0) };
  }
  const tr = (await (await fetch(GL)).json()).find((t) => t.name === ad);
  if (!tr) throw new Error("geçiş yok: " + ad);
  return { ...tr, ease: "yumusak", kare: 0 };
}

export function fsKur(tr) {
  const par = Object.entries(tr.paramsTypes || {}).map(([k, t]) => `uniform ${t} ${k};`).join("\n");
  return `precision highp float; varying vec2 _uv; uniform sampler2D from, to; uniform float progress, ratio; ${par}
vec4 getFromColor(vec2 uv){ return texture2D(from, uv); } vec4 getToColor(vec2 uv){ return texture2D(to, uv); }
${tr.glsl}
void main(){ gl_FragColor = transition(_uv); }`;
}

export const yumusak = (x) => x * x * (3 - 2 * x);
export const yavasla = (tr) => (tr.ease === "lineer" ? (x) => x : yumusak);
