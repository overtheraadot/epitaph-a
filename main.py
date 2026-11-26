"""make.fun entry: Famous Last Words: The Funniest Epitaph (epitaph-a).

Writes one original one-line epitaph to /output/entry.txt and prints
a short report.

Gate (from the kit RULES.txt): the file must be UTF-8 text of 1 to 150
characters, not only white space. The entry is a single line.

The epitaph: a reply-all disaster so final that neither IT's recall
nor God can undo it. It reads like something carved in stone ("Here
lies Dave"), turns on a surprise at the end, and stays in the head
because everyone has almost sent that email themselves.
"""

import os

# The entry: one line, my own invention. A recall nobody can perform.
ENTRY = (
    "Here lies Dave. He replied-all to the company-wide email, then "
    "asked IT to recall it. They couldn't. Neither could God."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 150


def verify(text):
    """Enforce the gate from RULES.txt: 1-150 chars, non-blank, one line.

    Also rejects leading/trailing whitespace: the judged text is the
    line itself, so stray spaces would count against the limit and
    look sloppy on the leaderboard.
    """
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if text != text.strip():
        raise ValueError("entry must not have leading/trailing whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "entry is %d chars, over the %d-char limit" % (len(text), MAX_CHARS)
        )
    if "\n" in text.strip():
        raise ValueError("entry must be a single line")
    return True


def write_entry(path=OUTPUT_PATH):
    """Validate the entry, then write it exactly as-is, no newline."""
    verify(ENTRY)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    return path


def report(path):
    """Read the written file back and print its length and headroom."""
    with open(path, encoding="utf-8") as f:
        text = f.read()
    headroom = MAX_CHARS - len(text)
    print("Wrote %s (%d chars, %d line(s), %d chars of headroom)"
          % (path, len(text), text.count("\n") + 1, headroom))
    print(text)
    return text


def main():
    report(write_entry())


if __name__ == "__main__":
    main()
