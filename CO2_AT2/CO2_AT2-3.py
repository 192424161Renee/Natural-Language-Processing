# Morphology-Based Normalization

words = ["govern", "government", "governance"]

print("-" * 100)
print("{:<15}{:<15}{:<15}{:<20}{:<15}".format(
    "Word", "Root", "Affix",
    "Derivation Level", "Normalized"))
print("-" * 100)

for word in words:

    if word == "govern":
        root = "govern"
        affix = "-"
        level = "Base"

    elif word == "government":
        root = "govern"
        affix = "-ment"
        level = "Level-1"

    elif word == "governance":
        root = "govern"
        affix = "-ance"
        level = "Level-1"

    normalized = "govern"

    print("{:<15}{:<15}{:<15}{:<20}{:<15}".format(
        word, root, affix,
        level, normalized))
