#!/usr/bin/env python3
"""Generate data_songjiwei.js from GeoJSON files in data_songjiwei/ folder"""
import json, os

base = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(base, "data_songjiwei")
output = os.path.join(base, "js", "data_songjiwei.js")

# Read and wrap each GeoJSON file into a JS variable
files = {
    "netherlands_provinces.geojson": "GEOJSON_NETHERLANDS_PROVINCES",
    "netherlands_bivariate.geojson": "GEOJSON_NETHERLANDS_BIVARIATE",
    "chart.geojson": "GEOJSON_CHART",
}

js_lines = []
for filename, varname in files.items():
    path = os.path.join(data_dir, filename)
    if not os.path.exists(path):
        print(f"WARNING: {path} not found, skipping")
        continue
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    js = json.dumps(data, separators=(",", ":"), ensure_ascii=False)
    js_lines.append(f"var {varname} = {js};")

with open(output, "w", encoding="utf-8") as f:
    f.write("\n\n".join(js_lines) + "\n")

print(f"✅ Generated {output} ({os.path.getsize(output):,} bytes)")
print(f"   Variables: {[v for _, v in files.items()]}")
