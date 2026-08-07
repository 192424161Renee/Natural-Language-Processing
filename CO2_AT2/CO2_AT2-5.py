# Inflectional Morphology-Based Normalization

words = ["create", "creates", "creating"]

print("-" * 110)
print("{:<15}{:<12}{:<22}{:<15}{:<15}".format(
    "Word", "Suffix",
    "Grammar Category",
    "Root", "Normalized"))
print("-" * 110)

for word in words:

    if word == "create":
        suffix = "-"
        grammar = "Base Form"
        root = "create"

    elif word == "creates":
        suffix = "-s"
        grammar = "3rd Person Singular"
        root = "create"

    elif word == "creating":
        suffix = "-ing"
        grammar = "Present Participle"
        root = "create"

    normalized = "create"

    print("{:<15}{:<12}{:<22}{:<15}{:<15}".format(
        word, suffix,
        grammar, root,
        normalized))
