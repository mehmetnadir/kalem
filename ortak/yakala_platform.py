"""yakala.py platform seçimi (saf işlev; süreç başlatmaz, testler bunu sınar).
Mac dalı eskiden yakala.py'de gömülü olan değerlerle birebir aynıdır."""
import shutil

MAC_CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
LINUX_CHROME_ADAYLARI = ("google-chrome", "google-chrome-stable", "chromium", "chromium-browser")
MAC_BAYRAK = ["--use-angle=metal", "--enable-gpu", "--ignore-gpu-blocklist"]
# Linux: GPU yok -> yazılım GL (SwiftShader); sunucuda kök olmayan kullanıcı için sandbox kapalı.
LINUX_BAYRAK = ["--no-sandbox", "--use-angle=swiftshader", "--enable-unsafe-swiftshader",
                "--ignore-gpu-blocklist", "--font-render-hinting=none"]


def chrome_yolu(sistem, env, which=shutil.which):
    """CHROME ortam değişkeni her zaman kazanır; yoksa platform varsayılanı."""
    if env.get("CHROME"): return env["CHROME"]
    if sistem == "Darwin": return MAC_CHROME
    for ad in LINUX_CHROME_ADAYLARI:
        y = which(ad)
        if y: return y
    return LINUX_CHROME_ADAYLARI[0]


def gpu_bayraklari(sistem):
    return list(MAC_BAYRAK if sistem == "Darwin" else LINUX_BAYRAK)
