sentence = input("Enter a sentence: ")
words = sentence.split()
print("\nTransformation-Based Tagging")
for word in words:
    tag = "Noun"
    if word.endswith("ing"):
        tag = "Verb"
    elif word.endswith("ly"):
        tag = "Adverb"
    elif word.endswith("ed"):
        tag = "Verb"
    print(word, "->", tag)
