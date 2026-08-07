# Rule-Based Morphological Processing

words = ["analyzing", "analysis", "analytical"]

print("-" * 90)
print("{:<15}{:<15}{:<15}{:<15}{:<15}".format(
    "Input Word", "Root", "Affix", "Type", "Normalized"))
print("-" * 90)

for word in words:

    if word == "analyzing":
        root = "analyze"
        affix = "-ing"
        mtype = "Inflectional"

    elif word == "analysis":
        root = "analyze"
        affix = "-sis"
        mtype = "Derivational"

    elif word == "analytical":
        root = "analyze"
        affix = "-ical"
        mtype = "Derivational"

    normalized = "analyze"

    print("{:<15}{:<15}{:<15}{:<15}{:<15}".format(
        word, root, affix, mtype, normalized))
