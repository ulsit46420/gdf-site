#!/usr/bin/env bash
# Full build: parse data -> Hugo build -> Pagefind index.
#
# Set DICT_SRC and EXAMPLES_SRC to local files in the dictionary checkout.
# The gdf Pages workflow sets both paths explicitly.
set -euo pipefail

cd "$(dirname "$0")/.."

echo "==> Parsing source markdown -> data/terms.json"
uv run --no-project python scripts/build_data.py

echo "==> Building site with Hugo"
# --cleanDestinationDir removes stale output (e.g. renamed term slugs) so reruns
# don't leave orphaned pages for Pagefind to index.
hugo --gc --minify --cleanDestinationDir

echo "==> Indexing with Pagefind"
npx pagefind --site public

echo "==> Done. Serve ./public over HTTP (Pagefind needs HTTP, not file://)."
