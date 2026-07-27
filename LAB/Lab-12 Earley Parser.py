import nltk
grammar = nltk.CFG.fromstring("""
S -> NP VP
NP -> 'John'
VP -> V NP
V -> 'likes'
""")
parser = nltk.EarleyChartParser(grammar)
sentence = input("Enter sentence: ").split()
try:
    trees = list(parser.parse(sentence))
    if trees:
        print("Sentence Accepted")
        for tree in trees:
            print(tree)
    else:
        print("Sentence Rejected")
except ValueError:
    print("Sentence Rejected")
