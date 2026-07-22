import re
sentence = input("Enter a sentence: ")
words = sentence.split()
print("\nRule-Based POS Tagging")
for word in words:
    if re.search("ing$", word):
        tag = "Verb"
    elif re.search("ly$", word):
        tag = "Adverb"
    elif re.search("ed$", word):
        tag = "Past Verb"
    elif re.search("s$", word):
        tag = "Plural Noun"
    else:
        tag = "Noun"
    print(word, "->", tag)
