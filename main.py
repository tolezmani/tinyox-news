"""TinyOX news-summary-01 entry (Python 3.13, standard library only).

Copies the summary beside this file to /output/entry.txt. Deterministic:
same input bytes, same output bytes, every run. The entry self-checks the
gate before finishing: UTF-8 text of 1 to 2,000 characters, not only
white space.
"""

import os
import shutil

src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "summary.txt")
out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(src, encoding="utf-8") as f:
    text = f.read()
if not 1 <= len(text) <= 2000 or not text.strip():
    raise SystemExit("summary.txt fails the entry gate (1-2000 chars, non-blank)")
shutil.copyfile(src, os.path.join(out_dir, "entry.txt"))
