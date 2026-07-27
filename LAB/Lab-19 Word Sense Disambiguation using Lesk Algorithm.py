from nltk.wsd import lesk
from nltk.tokenize import word_tokenize
sentence = input("Enter sentence: ")
word = input("Enter ambiguous word: ")
sense = lesk(word_tokenize(sentence), word)
if sense:
    print("Word Sense:", sense.name())
    print("Meaning:", sense.definition())
else:
    print("Sense not found.")
