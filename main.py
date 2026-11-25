"""Write the entry to /output/entry.txt. Deterministic output: no network, no clock, no randomness."""
import os
import string
import sys

# Entry: a satirical sentence about lawmakers who cannot turn a file into a PDF.
ENTRY_TEXT = "The committee that regulates artificial intelligence spent an afternoon trying to convert a Word file to PDF, declared the format 'suspicious', and banned it pending further study."
ENTRY_LIMIT = 320


def _reject(reason):
    sys.stderr.write("error: " + reason + "\n")
    raise SystemExit(1)


def validate(text):
    cleaned = text.strip()
    if not cleaned:
        _reject("entry must not be empty")
    if all(c in string.punctuation for c in cleaned):
        _reject("entry must not be punctuation only")
    if cleaned.isdigit():
        _reject("entry must not be digits only")
    if not any(c.isalpha() for c in cleaned):
        _reject("entry must include at least one letter")
    if len(text) > ENTRY_LIMIT:
        _reject("entry is %d characters, above the %d limit" % (len(text), ENTRY_LIMIT))
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as err:
        _reject("entry is not valid UTF-8: %s" % err)


def main():
    validate(ENTRY_TEXT)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as out:
        out.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
