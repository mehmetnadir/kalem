// kare: 42
// ease: lineer
// Author: kalem (Claude, 06.11.2026) - özgün şader
// License: MIT
// Description: Tahta silgisi sahneyi 4 yatay vuruşla (zigzag, her vuruşta hafif açı) siler; silinen
//   yer krem zemine, gri lekeli izle döner. Tamamen silinince sonraki sahne gürültü eşiğiyle belirir.
//   p 0..0.70 silme, 0.70..1 belirme (ease lineer: silgi hızı şader içinde yumuşatılır).
const float PI = 3.14159265;
const vec3 KREM = vec3(0.969, 0.953, 0.918);
const vec2 YARI = vec2(0.075, 0.125);

float h21(vec2 p) { p = fract(p * vec2(123.34, 456.21)); p += dot(p, p + 45.32); return fract(p.x * p.y); }
float vn(vec2 p) {
  vec2 i = floor(p), f = fract(p); f = f * f * (3.0 - 2.0 * f);
  return mix(mix(h21(i), h21(i + vec2(1.0, 0.0)), f.x), mix(h21(i + vec2(0.0, 1.0)), h21(i + vec2(1.0, 1.0)), f.x), f.y);
}
float fbm(vec2 p) {
  float s = 0.0, a = 0.5;
  for (int i = 0; i < 4; i++) { s += a * vn(p); p = p * 2.03 + 17.1; a *= 0.5; }
  return s;
}
float kutu(vec2 p, vec2 b, float r) {
  vec2 d = abs(p) - b + r;
  return length(max(d, 0.0)) + min(max(d.x, d.y), 0.0) - r;
}
vec2 don(vec2 d, float t) { float c = cos(t), s = sin(t); return vec2(c * d.x + s * d.y, -s * d.x + c * d.y); }

vec4 transition(vec2 uv) {
  vec2 P = vec2(uv.x * ratio, 1.0 - uv.y);
  float p = progress;
  float s = clamp(p / 0.70, 0.0, 1.0);
  float unit = s * (4.0 + 3.0 * 0.18);
  float kf = min(floor(unit / 1.18), 3.0);
  float yerel = unit - kf * 1.18;
  float u = clamp(yerel, 0.0, 1.0);
  float yon = mod(kf, 2.0) < 0.5 ? 1.0 : -1.0;
  float ue = mix(u, u * u * (3.0 - 2.0 * u), 0.5);
  float xa = -0.12, xb = ratio + 0.12;
  float ex = yon > 0.0 ? mix(xa, xb, ue) : mix(xb, xa, ue);
  float yc = (kf + 0.5) * 0.25;
  float gec = smoothstep(0.0, 1.0, clamp((yerel - 1.0) / 0.18, 0.0, 1.0));
  yc = mix(yc, min(kf + 1.5, 3.5) * 0.25, gec) + 0.012 * sin(u * PI * 3.0 + kf) * (1.0 - gec);
  float aci = 0.10 * yon + 0.03 * sin(kf * 2.0);

  vec2 d = P - vec2(ex, yc);
  vec2 Q = don(d, aci);
  float bd = YARI.x - yon * Q.x;

  float jb = (fbm(vec2(P.x * 9.0, 3.1)) - 0.5) * 0.012;
  float kb = floor(clamp((P.y + jb) / 0.25, 0.0, 3.999));
  float alt = step(kb + 0.5, kf);
  float es = 1.0 - step(0.5, abs(kb - kf));
  float cizik = (fbm(P * vec2(30.0, 9.0)) - 0.5) * 0.03;
  float er = max(alt, es * smoothstep(-0.004, 0.012, bd + cizik));

  float taze = exp(-max(bd, 0.0) / 0.10) * es;
  float sm = clamp((fbm(P * vec2(5.0, 26.0) + 3.7) - 0.35) * 1.6, 0.0, 1.0);
  float leke = sm * (0.10 + 0.14 * taze) + fbm(P * 14.0) * 0.03;
  vec3 silik = mix(KREM, vec3(0.60, 0.59, 0.57), clamp(leke, 0.0, 1.0));
  vec3 col = mix(getFromColor(uv).rgb, silik, er);

  float gor = 1.0 - smoothstep(0.70, 0.72, p);
  if (gor > 0.0) {
    vec2 Qg = don(d - vec2(0.012, 0.016), aci);
    col *= 1.0 - 0.22 * gor * (1.0 - smoothstep(-0.005, 0.02, kutu(Qg, YARI, 0.012)));
    float sd = kutu(Q, YARI, 0.012);
    vec3 gov = vec3(0.878, 0.812, 0.659);
    float tut = kutu(Q, vec2(0.03, 0.07), 0.008);
    gov = mix(gov, vec3(0.788, 0.706, 0.541), 1.0 - smoothstep(-0.0015, 0.0015, tut));
    float ic = 1.0 - smoothstep(0.0, 0.003, abs(kutu(Q, YARI - 0.014, 0.008)));
    float ince = 1.0 - smoothstep(0.0, 0.003, abs(tut));
    vec3 mur = vec3(0.184, 0.165, 0.141);
    gov = mix(gov, mur, max(ic * 0.45, ince * 0.8));
    float kal = 1.0 - smoothstep(0.0, 0.0035, abs(sd + 0.002));
    gov = mix(gov, mur, kal);
    col = mix(col, gov, gor * (1.0 - smoothstep(-0.0015, 0.0015, sd)));
  }

  float t2 = clamp((p - 0.70) / 0.30, 0.0, 1.0);
  float r = fbm(P * 3.0 + 11.3);
  float a = smoothstep(r * 0.8, r * 0.8 + 0.2, t2 * 1.2);
  return vec4(mix(col, getToColor(uv).rgb, a), 1.0);
}
