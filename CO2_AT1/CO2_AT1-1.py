words = ["connected", "connecting", "connection"]
print("=" * 75)
print("{:<15} {:<15} {:<15} {:<15} {:<15}".format(
    "Input Word", "Root", "Suffix", "Type", "Normalized"))
print("=" * 75)
for word in words:
    if word.endswith("ed"):
        root = word[:-2]
        suffix = "-ed"
        suffix_type = "Inflectional"
        normalized = "connect"
    elif word.endswith("ing"):
        root = word[:-3]
        suffix = "-ing"
        suffix_type = "Inflectional"
        normalized = "connect"
    elif word.endswith("ion"):
        root = word[:-3]
        suffix = "-ion"
        suffix_type = "Derivational"
        normalized = "connect"
    else:
        root = word
        suffix = "-"
        suffix_type = "None"
        normalized = word
    print("{:<15} {:<15} {:<15} {:<15} {:<15}".format(
        word, root, suffix, suffix_type, normalized))
print("=" * 75)
