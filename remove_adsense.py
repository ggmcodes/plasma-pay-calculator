#!/usr/bin/env python3
"""Remove all Google AdSense code (loader + auto-ads push calls) from every HTML page.
Switching plasma to Mediavine Journey (Jul 2026). Reversible via git if needed."""
import re
from pathlib import Path

ROOT = Path(__file__).parent

# 1. AdSense loader script (both variants: /pagead/js/adsbygoogle.js and /pagead/js),
#    possibly split across two lines. Matches the whole <script ...></script> + trailing newline.
loader_re = re.compile(
    r'[ \t]*<script\s+async\s+src="https://pagead2\.googlesyndication\.com/pagead/js[^"]*"\s+crossorigin="anonymous"\s*>\s*</script>[ \t]*\n?'
)
# 2. The "// Initialize ads" comment line (whole line)
comment_re = re.compile(r'^[ \t]*//[ \t]*Initialize ads[ \t]*\n', re.MULTILINE)
# 3. The auto-ads push line (whole line) — leaves the surrounding page <script> block intact
push_re = re.compile(r'^[ \t]*\(adsbygoogle = window\.adsbygoogle \|\| \[\]\)\.push\(\{\}\);[ \t]*\n', re.MULTILINE)

changed = 0
for f in ROOT.rglob("*.html"):
    if "node_modules" in str(f):
        continue
    c = f.read_text(encoding="utf-8")
    orig = c
    c = loader_re.sub("", c)
    c = comment_re.sub("", c)
    c = push_re.sub("", c)
    if c != orig:
        f.write_text(c, encoding="utf-8")
        changed += 1

print(f"Files changed: {changed}")
