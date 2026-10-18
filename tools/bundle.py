"""Make a single-file copy of a game that opens straight from disk.

Every quoted relative path to a .glb or .mp3 in the page is swapped for a data: URI,
so the browser never has to fetch local files (which file:// pages can't do).

    python3 tools/bundle.py day-on-the-farm/index.html out/day-on-the-farm.html
"""
import base64
import os
import re
import sys

TYPES = {'.glb': 'model/gltf-binary', '.mp3': 'audio/mpeg'}


def bundle(src, dst):
    here = os.path.dirname(os.path.abspath(src))
    html = open(src, encoding='utf-8').read()

    def inline(m):
        path = os.path.normpath(os.path.join(here, m.group(2)))
        data = base64.b64encode(open(path, 'rb').read()).decode()
        return f"{m.group(1)}data:{TYPES[os.path.splitext(path)[1]]};base64,{data}{m.group(1)}"

    html = re.sub(r"""(['"])((?:\.\./|\./)?[\w./-]+\.(?:glb|mp3))\1""", inline, html)
    open(dst, 'w', encoding='utf-8').write(html)
    print(f'{dst}: {len(html) / 1e6:.1f} MB')


if __name__ == '__main__':
    bundle(sys.argv[1], sys.argv[2])
