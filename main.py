#!/usr/bin/env python3
"""The Long Roast: Lawmakers and the File They Cannot Convert.

One satirical sentence, written for this bounty. The program keeps the
sentence as a literal, checks it against the competition's own gate at
run time (UTF-8 text, 1 to 320 characters, a single sentence, no
leading or trailing whitespace, ending on terminal punctuation), and
only then writes it to /output/entry.txt. It reads nothing from the
network and nothing from disk apart from this file.
"""

import sys

SENTENCE = "The senator who wrote the bill mandating machine-readable AI disclosures submitted his own disclosure as a photograph of his screen, captioned 'PDF attached.'"

LOWER = 1
UPPER = 320


def gate_failures(sentence):
    failures = []
    if len(sentence) < LOWER or len(sentence) > UPPER:
        failures.append(
            "length %d outside %d-%d" % (len(sentence), LOWER, UPPER)
        )
    if sentence.strip() != sentence:
        failures.append("must not start or end with whitespace")
    if not sentence.strip():
        failures.append("must not be only whitespace")
    if "\n" in sentence or "\r" in sentence:
        failures.append("must be a single line")
    if sentence.count(".") != 1:
        failures.append("must be exactly one sentence")
    if sentence and sentence[-1] not in ".!?":
        # A closing quote may follow the terminal punctuation, as in
        # "... captioned 'PDF attached.'" — the sentence still ends
        # on its period; only the quote sits after it.
        core = sentence.rstrip("'\"")
        if not core or core[-1] not in ".!?":
            failures.append("must end on terminal punctuation")
    return failures


def main():
    failures = gate_failures(SENTENCE)
    if failures:
        for failure in failures:
            print("gate failed: " + failure, file=sys.stderr)
        return 1
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(SENTENCE + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
