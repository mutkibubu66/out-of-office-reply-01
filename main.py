#!/usr/bin/env python3
"""Write one funny one-line out-of-office reply to /output/entry.txt.

Pure stdlib Python 3.13. The reply must be a single line of 1-160
characters: a real away message a person would switch on, with the
laugh landing on the first read.
"""

import os

LINE = "Out of office until Monday \u2014 my auto-reply took over my job, and honestly, it's thriving."


def main() -> None:
    assert "\n" not in LINE, "entry must be a single line"
    assert 1 <= len(LINE) <= 160, f"entry must be 1-160 chars, got {len(LINE)}"
    assert LINE.strip() == LINE and LINE.strip(), "entry must not be blank"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
