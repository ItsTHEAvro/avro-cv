#!/usr/bin/env bash
# Usage: scripts/bundle.sh [cv-picture|cv|resume]
set -euo pipefail

TEMPLATE="${1:-cv-picture}"
cd "$(dirname "$0")/.."

OUT=build/cv-bundle.txt
mkdir -p build
: > "$OUT"

for f in AGENTS.md data/*.yaml \
         "templates/$TEMPLATE/$TEMPLATE-template.tex" \
         "templates/$TEMPLATE/style-$TEMPLATE-template.sty"; do
  printf '\n===== %s =====\n' "$f" >> "$OUT"
  cat "$f" >> "$OUT"
done

echo "Bundle ready: $OUT"