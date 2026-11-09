// Arayüz sözlüğü (madde 17) — tr/en arayüz metinleri ve dil çözümleme
"use strict";

export const DILLER = ["tr", "en"];

export const SOZLUK = {
  tr: {
    acikTema: "Açık tema",
    altyazi: "Altyazı",
    bolum: (n) => "Bölüm " + n,
    bolumler: "Bölümler",
    dersVideosu: "Ders videosu",
    dikeyGorunum: "Dikey görünüm",
    duraklat: "Duraklat",
    duraklatildi: "Duraklatıldı",
    hiz: (x) => "Hız " + x,
    hizCarpan: (x) => x + "× hız",
    hizKilitlendi: (x) => "Hız " + x + "× kilitlendi",
    hizKilitli: (x) => x + "× kilitli. Çıkmak için dokun",
    ilerleme: "İlerleme",
    izlemekIcinDokun: "İzlemek için dokun",
    koyuTema: "Koyu tema",
    normal: "Normal",
    oynat: "Oynat",
    oynatiliyor: "Oynatılıyor",
    oynatmaHizi: "Oynatma hızı",
    sahneTampon: (ad, m) => ad + " sahne tamponu " + m,
    saniyeGeri: (n) => n + " saniye geri",
    saniyeIleri: (n) => n + " saniye ileri",
    sesDuzeyi: "Ses düzeyi",
    sesHatasi: "Ses dosyası yüklenemedi.",
    sesIcinDokun: "Sesi açmak için dokun",
    sesiAc: "Sesi aç",
    sessiz: "Sessiz",
    tamEkran: "Tam ekran",
    tamEkranCift: "Tam ekran (yatay ve dikey)",
    tamEkrandanCik: "Tam ekrandan çık",
    tekrarDene: "Tekrar dene",
    tekrarIzle: "Tekrar izle",
    tema: "Tema",
    veriHatasi: (m) => "Video verisi yüklenemedi: " + m,
    yatayGorunum: "Yatay görünüm",
    yonUyumsuz: (p) => "yön çifti uyumsuz: " + p,
    yukleniyor: "Yükleniyor",
  },
  en: {
    acikTema: "Light theme",
    altyazi: "Subtitles",
    bolum: (n) => "Chapter " + n,
    bolumler: "Chapters",
    dersVideosu: "Lesson video",
    dikeyGorunum: "Portrait view",
    duraklat: "Pause",
    duraklatildi: "Paused",
    hiz: (x) => "Speed " + x,
    hizCarpan: (x) => x + "× speed",
    hizKilitlendi: (x) => "Speed " + x + "× locked",
    hizKilitli: (x) => x + "× locked. Tap to exit",
    ilerleme: "Progress",
    izlemekIcinDokun: "Tap to watch",
    koyuTema: "Dark theme",
    normal: "Normal",
    oynat: "Play",
    oynatiliyor: "Playing",
    oynatmaHizi: "Playback speed",
    sahneTampon: (ad, m) => ad + " scene buffer " + m,
    saniyeGeri: (n) => n + " seconds back",
    saniyeIleri: (n) => n + " seconds forward",
    sesDuzeyi: "Volume",
    sesHatasi: "Audio file could not be loaded.",
    sesIcinDokun: "Tap to unmute",
    sesiAc: "Unmute",
    sessiz: "Mute",
    tamEkran: "Full screen",
    tamEkranCift: "Full screen (landscape & portrait)",
    tamEkrandanCik: "Exit full screen",
    tekrarDene: "Retry",
    tekrarIzle: "Watch again",
    tema: "Theme",
    veriHatasi: (m) => "Video data could not be loaded: " + m,
    yatayGorunum: "Landscape view",
    yonUyumsuz: (p) => "orientation pair mismatch: " + p,
    yukleniyor: "Loading",
  },
};

export function sozlukSec(dil) {
  return SOZLUK[DILLER.includes(dil) ? dil : "tr"];
}

const dilKodu = (d) => {
  if (!d || typeof d !== "string") return "";
  const k = d.trim().slice(0, 2).toLowerCase();
  return DILLER.includes(k) ? k : "";
};

export function dilCoz(sec, belge) {
  const dSec = sec && dilKodu(sec.dil);
  if (dSec) return dSec;
  const dBelge = belge && dilKodu(belge.lang);
  if (dBelge) return dBelge;
  if (typeof document !== "undefined" && document.documentElement) {
    const dDoc = dilKodu(document.documentElement.lang);
    if (dDoc) return dDoc;
  }
  return "tr";
}
