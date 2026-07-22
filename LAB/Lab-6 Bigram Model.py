text = input("Enter a sentence: ")
words = text.split()
print("\nBigrams are:")
for i in range(len(words)-1):
    print("(", words[i], ",", words[i+1], ")")
print("\nGenerated Text:")
for i in range(len(words)-1):
    print(words[i], words[i+1])
