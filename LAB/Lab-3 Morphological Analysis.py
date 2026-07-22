import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
sentence = input("Enter a sentence: ")
words = word_tokenize(sentence)
tags = pos_tag(words)
print("\nMorphological Analysis")
print("----------------------")
for word, tag in tags:
    print(word, ":", tag)
