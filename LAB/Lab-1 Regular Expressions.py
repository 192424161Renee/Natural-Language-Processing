import re
text = input("Enter a sentence: ")
result = re.search("Python", text)
if result:
    print("Pattern Found")
else:
    print("Pattern Not Found")
words = re.findall(r"\w+", text)
print("Words in the sentence:")
print(words)
