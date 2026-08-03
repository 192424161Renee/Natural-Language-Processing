words = ["unhappy", "happiness", "happily"]
print("=" * 90)
print("{:<15} {:<10} {:<15} {:<10} {:<15} {:<15}".format(
    "Input Word", "Prefix", "Root", "Suffix", "Type", "Normalized"))
print("=" * 90)
for word in words:
    prefix = "-"
    suffix = "-"
    root = ""
    morph_type = ""
    if word == "unhappy":
        prefix = "un-"
        root = "happy"
        suffix = "-"
        morph_type = "Derivational"
        normalized = "happy"
    elif word == "happiness":
        prefix = "-"
        root = "happy"
        suffix = "-ness"
        morph_type = "Derivational"
        normalized = "happy"
    elif word == "happily":
        prefix = "-"
        root = "happy"
        suffix = "-ly"
        morph_type = "Derivational"
        normalized = "happy"
    print("{:<15} {:<10} {:<15} {:<10} {:<15} {:<15}".format(
        word, prefix, root, suffix, morph_type, normalized))
print("=" * 90)
