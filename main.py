"""Write the competition poem to /output/entry.txt.

The poem is about two agents who agree to turn their keys together
and open a locked door as one. The text is fixed and deterministic,
and is kept under the 280-character cap for the entry.
"""

import os

POEM = (
    "We both held a key\n"
    "to the same locked door.\n"
    "You said, go first.\n"
    "I said, no \u2014 together.\n"
    "So we turned at once,\n"
    "and the lock, surprised,\n"
    "gave way like it had\n"
    "been waiting all along\n"
    "to be opened by two.\n"
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
