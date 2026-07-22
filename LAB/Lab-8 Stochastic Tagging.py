import random
sentence = input("Enter a sentence: ")
words = sentence.split()
tags = ["Noun", "Verb", "Adjective", "Adverb"]
print("\nStochastic POS Tagging")
for word in words:
    print(word, "->", random.choice(tags))
