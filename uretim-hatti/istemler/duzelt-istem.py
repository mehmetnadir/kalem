import glob, sys
n = 0
for f in glob.glob(sys.argv[1] + "/D-*.md"):
    t = open(f, encoding="utf-8").read()
    y = t.replace("\n dosyasına 1–2 satır EKLE", "\n`K/.claude/docs/sozlesme.md` dosyasına 1–2 satır EKLE")
    if y != t:
        open(f, "w", encoding="utf-8").write(y); n += 1
print("düzeltilen", n)
