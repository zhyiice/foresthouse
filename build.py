#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build script: concatenates src/ parts into a single self-contained index.html.
Only external dependency is three.min.js (classic UMD script, works from file://).
"""
import io, os, sys, time

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "src")
OUT = os.path.join(ROOT, "index.html")

PARTS = [
    "index.head.html",
    "js/00_quality.js",
    "js/01_utils.js",
    "js/02_textures.js",
    "js/03_sky.js",
    "js/04_terrain.js",
    "js/05_trees.js",
    "js/05b_cover.js",
    "js/06_cabin.js",
    "js/06b_interior.js",
    "js/07_props.js",
    "js/08_particles.js",
    "js/09_atmos.js",
    "js/09b_weather.js",
    "js/10_post.js",
    "js/11_controls.js",
    "js/13_audio.js",
    "js/12_main.js",
    "index.tail.html",
]

def read(p):
    with io.open(os.path.join(SRC, p), "r", encoding="utf-8") as f:
        return f.read()

chunks = []
for i, p in enumerate(PARTS):
    if p.startswith("index."):
        chunks.append("<!-- ===== %s ===== -->\n" % p + read(p))
    else:
        chunks.append("<script>\n/* ============================== %s ============================== */\n" % p
                      + "(function(APP){\n'use strict';\n" + read(p) + "\n})(window.APP = window.APP || {});\n</script>\n")

html = "".join(chunks)
with io.open(OUT, "w", encoding="utf-8", newline="\n") as f:
    f.write(html)

print("built %s  (%.1f KB, %d parts)" % (OUT, len(html.encode("utf-8")) / 1024.0, len(PARTS)))
