words = ["writes", "writing", "written"]
print("=" * 120)
print("{:<12} {:<30} {:<12} {:<12} {:<15} {:<12}".format(
    "Input Word", "State Transition", "Root", "Suffix",
    "Pattern", "Normalized"))
print("=" * 120)
for word in words:
    if word == "writes":
        transition = "Start → Verb → -s → Final"
        root = "write"
        suffix = "-s"
        pattern = "Regular"
        normalized = "write"
    elif word == "writing":
        transition = "Start → Verb → -ing → Final"
        root = "write"
        suffix = "-ing"
        pattern = "Regular"
        normalized = "write"
    elif word == "written":
        transition = "Start → Verb → Irregular → Final"
        root = "write"
        suffix = "-en"
        pattern = "Irregular"
        normalized = "write"
    print("{:<12} {:<30} {:<12} {:<12} {:<15} {:<12}".format(
        word, transition, root, suffix, pattern, normalized))
print("=" * 120)
