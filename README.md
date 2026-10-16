# GDF website

Hugo source for the [GDF dictionary](https://github.com/ulsit46420/gdf). The
dictionary data remains in `gdf`; this repository holds the site templates,
assets, and build scripts.

See [site/README.md](site/README.md) for local build instructions. The Pages
workflow in `gdf` checks out this repository and builds the site with the
dictionary files from the same `gdf` commit.

If this repository is private, `gdf` needs a `SITE_REPO_TOKEN` Actions secret
with read access to its contents. Public repositories can use the workflow's
default token.
