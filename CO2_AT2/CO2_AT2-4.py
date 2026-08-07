# Morphological Parsing and Normalization

words = ["activate", "activation", "reactivation"]

print("-" * 120)
print("{:<15}{:<10}{:<15}{:<12}{:<25}{:<15}".format(
    "Word", "Prefix", "Root",
    "Suffix", "Derivation", "Normalized"))
print("-" * 120)

for word in words:

    if word == "activate":
        prefix = "-"
        root = "activate"
        suffix = "-"
        derivation = "Base"

    elif word == "activation":
        prefix = "-"
        root = "activate"
        suffix = "-ion"
        derivation = "Verb -> Noun"

    elif word == "reactivation":
        prefix = "re-"
        root = "activate"
        suffix = "-ion"
        derivation = "Prefix + Verb -> Noun"

    normalized = "activate"

    print("{:<15}{:<10}{:<15}{:<12}{:<25}{:<15}".format(
        word, prefix, root,
        suffix, derivation, normalized))
