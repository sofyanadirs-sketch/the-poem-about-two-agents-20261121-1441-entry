"""the-poem-about-two-agents-20261121-1441 entry: write one original poem
about two agents agreeing to entry.txt.

Python 3.13, standard library only, no network, deterministic:
two runs write byte-identical output.
"""

import os
from pathlib import Path

# The conceit: two agents, each with its own compass, argue on one map
# until their lines cross and draw a third road neither of them planned.
# Neither surrenders its pen; agreement is a road they sign together,
# and the map itself, surprised, follows.
POEM = """Two minds, one map.
You drew north, I drew east —
we argued in ink until the lines crossed
and made a third road neither of us owned.

I kept my pen. You kept yours.
We signed the same wrong turn together,
and the map, surprised, agreed to follow.
Two yeses, one road."""

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

# The gate: 1 to 280 characters (Unicode code points), at least one
# non-whitespace character. Fail loudly instead of writing an invalid entry.
if not 1 <= len(POEM) <= 280 or not POEM.strip():
    raise ValueError(f"poem must be 1-280 chars, got {len(POEM)}")


def main() -> None:
    out_dir = Path(OUTPUT_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    # Write exact UTF-8 bytes: no added trailing newline, no translation.
    (out_dir / "entry.txt").write_bytes(POEM.encode("utf-8"))


if __name__ == "__main__":
    main()
