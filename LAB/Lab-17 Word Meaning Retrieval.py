import nltk
from nltk.corpus import wordnet
try:
    wordnet.synsets("test")
except LookupError:
    print("Downloading WordNet resources...")
    nltk.download('wordnet')
    nltk.download('omw-1.4')
word = input("Enter a word: ")
synsets = wordnet.synsets(word)
if synsets:
    print("\nSynsets and Meanings:\n")
    for i, syn in enumerate(synsets, start=1):
        print(f"Synset {i}:")
        print("Name      :", syn.name())
        print("Meaning   :", syn.definition())
        print("Examples  :", syn.examples())
        print("-" * 50)
else:
    print("No synsets found for the given word.")
