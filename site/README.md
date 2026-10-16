# EN2BGTERM — Hugo site

The source for the crawlable EN→BG dictionary website. It uses Hugo for pages
and Pagefind for search.

## Build locally

Install Hugo Extended, Node.js, npm, and uv. From this directory, run:

```bash
npm ci
DICT_SRC=../../gdf/README.md EXAMPLES_SRC=../../gdf/examples.md bash scripts/build.sh
```

The build parses the dictionary and examples into `data/terms.json`, renders
the site into `public/`, and creates the Pagefind index. Serve `public/` over
HTTP to test search.

The `gdf` repository owns the GitHub Pages workflow. It checks out this site
repository, passes local paths to its dictionary files, and publishes the
rendered output. `data/terms.json`, `public/`, and `resources/` are generated
and ignored by Git.
