import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')
sentence = input("Enter a sentence: ")
words = word_tokenize(sentence)
tags = pos_tag(words)
print("\nPart-of-Speech Tags")
for word, tag in tags:
    print(word, ":", tag)
