# /// script
# requires-python = ">=3.14"
# dependencies = ["terminology-indexes @ git+https://github.com/maturabg/terminology-indexes@lib-v0.1.0"]
# ///
"""Smoke test of the index library: download the latest release, search, check.

    uv run enrichment/index_smoke.py [DEST_DIR]

Set GH_TOKEN if the index repo is private.
"""

import os
import sys
import tempfile
from pathlib import Path

from terminology_indexes import LinkRecord, __version__, download_release, load_providers


def main() -> int:
    dest = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(tempfile.mkdtemp(prefix="index-"))
    index = download_release(dest, token=os.environ.get("GH_TOKEN"))
    with load_providers(index) as registry:
        print(f"terminology-indexes {__version__}, providers: {', '.join(registry.providers)}")
        hits = registry.search_all("decorator", lang="en")
        for h in hits:
            print(f"  {h.match:5}  {h.source}  {h.title}  {h.url}  [{h.snapshot_version}]")
        if not hits or hits[0].match != "exact":
            print("FAIL: no exact hit for 'decorator'", file=sys.stderr)
            return 1
        top = hits[0]
        result = registry.check(LinkRecord(top.source, top.external_id, top.url, top.snapshot_version))
        print(f"  check: {result.status} {result.reason}")
        if result.status != "ok":
            print("FAIL: check of the top hit is not ok", file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
