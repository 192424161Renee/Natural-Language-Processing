from nltk.stem import PorterStemmer
ps = PorterStemmer()
text = input("Enter words: ")
words = text.split()
print("\nOriginal Word\tStemmed Word")
print("-----------------------------")
for word in words:
    print(word, "\t\t", ps.stem(word))
