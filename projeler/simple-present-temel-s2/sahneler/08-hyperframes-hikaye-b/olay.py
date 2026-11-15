"""Sahne 08 hikâye karesi B (simple-present-temel-s2) olaylar.json: ses yok (durağan kare, anlatımdan bağımsız) -> boş liste."""
import json
from pathlib import Path

AD = Path(__file__).resolve().parent
(AD / "olaylar.json").write_text(json.dumps([], ensure_ascii=False))
print("olay 0")
