def plural(word):
    if word.endswith("y"):
        return word[:-1] + "ies"
    elif word.endswith(("s", "x", "z", "ch", "sh")):
        return word + "es"
    else:
        return word + "s"
noun = input("Enter a singular noun: ")

print("Plural Form:", plural(noun))
