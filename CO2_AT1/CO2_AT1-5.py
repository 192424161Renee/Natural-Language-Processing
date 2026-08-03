from nltk.stem import PorterStemmer
ps = PorterStemmer()
words = ["relational", "relation", "relate"]
print("=" * 120)
print("{:<15} {:<25} {:<20} {:<15}".format(
    "Input Word", "Applied Rule", "Intermediate Form", "Final Stem"))
print("=" * 120)
for word in words:
    if word == "relational":
        rule = "Remove -ational → -ate"
        intermediate = "relate"
    elif word == "relation":
        rule = "Remove -ion"
        intermediate = "relat"
    elif word == "relate":
        rule = "Remove final -e"
        intermediate = "relat"
    stem = ps.stem(word)
    print("{:<15} {:<25} {:<20} {:<15}".format(
        word, rule, intermediate, stem))
print("=" * 120)
