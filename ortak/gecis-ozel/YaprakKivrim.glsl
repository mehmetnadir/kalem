// kare: 32
// ease: yumusak
// Author: kalem (Claude, 06.11.2026) - özgün şader
// License: MIT
// Description: Sayfa sağ alt köşeden silindir gibi kıvrılarak kalkar; arkası (koyu krem) görünür,
//   alttaki sahne kıvrım gölgesinde kararır; ilerledikçe yarıçap küçülür.
// Silindir modeli: sayfa e doğrultusunda katlanır; c = kıvrım hattı, R = yarıçap.
//   x' >= c + R   : alttaki sahne (gölgeli)
//   c..c+R        : silindirin üst yayı (kâğıdın arkası); kaynak yoksa alt yay (ön yüz)
//   x' < c        : düz kalkmış yaprak (arka yüz) ya da düz sayfa (+ uç gölgesi)
const float PI = 3.14159265;
const vec3 ARKA = vec3(0.914, 0.886, 0.816);

float kenar(vec2 Q) { return min(min(Q.x, ratio - Q.x), min(Q.y, 1.0 - Q.y)); }
vec2 uvDe(vec2 Q) { return vec2(Q.x / ratio, Q.y); }

vec4 transition(vec2 uv) {
  vec2 P = vec2(uv.x * ratio, uv.y);
  float phi = 0.30;
  vec2 e = vec2(cos(phi), -sin(phi));
  vec2 pe = vec2(-e.y, e.x);
  float R = mix(0.24, 0.12, progress);
  float c = mix(ratio * e.x + 0.002, e.y - R - 0.25, progress);
  float x = dot(P, e);
  float y = dot(P, pe);
  float xm = min((ratio + y * e.y) / e.x, -y * e.x / e.y);
  float ext = max(xm - c, 0.0);
  float dx = x - c;

  if (dx >= 0.0 && dx <= R) {
    float s = clamp(dx / R, 0.0, 1.0);
    float th = PI - asin(s);
    vec2 Q = P + (R * th - dx) * e;
    if (kenar(Q) >= 0.0) {
      vec3 g = getFromColor(uvDe(Q)).rgb;
      vec3 col = mix(ARKA, g * vec3(0.94, 0.92, 0.86), 0.12);
      col *= 0.74 + 0.26 * (-cos(th));
      col *= 1.0 - 0.18 * (1.0 - smoothstep(0.0, 0.006, kenar(Q)));
      return vec4(col, 1.0);
    }
    float th2 = asin(s);
    Q = P + (R * th2 - dx) * e;
    if (kenar(Q) >= 0.0) {
      vec3 col = getFromColor(uvDe(Q)).rgb * (0.62 + 0.38 * cos(th2));
      return vec4(col, 1.0);
    }
  }

  if (dx < 0.0) {
    float x0 = 2.0 * c + PI * R - x;
    vec2 Q = P + (x0 - x) * e;
    float m = kenar(Q);
    if (m >= 0.0) {
      vec3 col = ARKA * 0.97;
      col = mix(col, getFromColor(uvDe(Q)).rgb * vec3(0.94, 0.92, 0.86), 0.10);
      col *= 1.0 - 0.18 * (1.0 - smoothstep(0.0, 0.006, m));
      return vec4(col, 1.0);
    }
    float wf = smoothstep(0.5 * PI * R, PI * R + 0.1, ext);
    float gol = 0.36 * wf * (1.0 - smoothstep(0.0, 0.10 + 0.4 * R, -m));
    return vec4(getFromColor(uv).rgb * (1.0 - gol), 1.0);
  }

  float kapsa = c + R * sin(min(ext / R, 1.5707963));
  float sd = max(x - kapsa, 0.0);
  float w = smoothstep(0.0, 0.5 * R, ext);
  float gol = 0.4 * w * exp(-sd / (0.9 * R + 0.03)) * (1.0 - smoothstep(0.82, 1.0, progress));
  return vec4(getToColor(uv).rgb * (1.0 - gol), 1.0);
}
