words = ["played", "player", "playing"]
print("=" * 95)
print("{:<15} {:<15} {:<15} {:<15} {:<15}".format(
    "Input Word", "Stem", "Removed Affix", "Type", "Normalized"))
print("=" * 95)
for word in words:
    if word.endswith("ed"):
        stem = word[:-2]
        affix = "-ed"
        trans_type = "Inflectional"
        normalized = "play"
    elif word.endswith("ing"):
        stem = word[:-3]
        affix = "-ing"
        trans_type = "Inflectional"
        normalized = "play"
    elif word.endswith("er"):
        stem = word[:-2]
        affix = "-er"
        trans_type = "Derivational"
        normalized = "play"
    else:
        stem = word
        affix = "-"
        trans_type = "None"
        normalized = word
    print("{:<15} {:<15} {:<15} {:<15} {:<15}".format(
        word, stem, affix, trans_type, normalized))
print("=" * 95)
