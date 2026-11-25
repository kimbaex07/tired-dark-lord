"""The Tired Dark Lord — a 100-word villain monologue.

Pure Python 3 stdlib. Writes the monologue to entry.txt in the
directory given by MAKEFUN_OUTPUT_DIR (default "/output").
"""

import os
import stat

MONOLOGUE = (
    "You know, dear hero, I built this throne from bones I polished "
    "myself. Forty years. Forty years of prophecies, betrayals, one "
    "loud volcano. And you walk in with that sword, that speech, that "
    "hair. Sit down. Just sit. The crown still pinches. The ravens "
    "stopped answering my letters. My curse needs a nap now. I had a "
    "plan, you know. A good one. Turn the rivers black, crown the "
    "moon, rule forever. But first, I was going to... hmm. What was "
    "it? Yes. Win. Go on, then. Strike. Or fetch the blanket, and "
    "we'll call it even."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(MONOLOGUE + "\n")
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
