"""TinyOX news-summary-01 entry (Python 3.13, standard library only).

Copies the summary beside this file to /output/entry.txt. Deterministic:
same input bytes, same output bytes, every run.
"""

import os
import shutil

src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "summary.txt")
out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
shutil.copyfile(src, os.path.join(out_dir, "entry.txt"))
