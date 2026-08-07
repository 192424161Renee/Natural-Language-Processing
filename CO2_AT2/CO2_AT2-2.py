# Morphological Parser

words = ["disagree", "agreement", "agreeable"]

print("-" * 120)
print("{:<15}{:<10}{:<12}{:<12}{:<15}{:<20}{:<12}".format(
    "Word", "Prefix", "Root", "Suffix",
    "Type", "Meaning", "Normalized"))
print("-" * 120)

for word in words:

    if word == "disagree":
        prefix = "dis-"
        root = "agree"
        suffix = "-"
        mtype = "Derivational"
        meaning = "Negative"

    elif word == "agreement":
        prefix = "-"
        root = "agree"
        suffix = "-ment"
        mtype = "Derivational"
        meaning = "Noun"

    elif word == "agreeable":
        prefix = "-"
        root = "agree"
        suffix = "-able"
        mtype = "Derivational"
        meaning = "Adjective"

    normalized = "agree"

    print("{:<15}{:<10}{:<12}{:<12}{:<15}{:<20}{:<12}".format(
        word, prefix, root, suffix,
        mtype, meaning, normalized))
