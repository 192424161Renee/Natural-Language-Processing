import nltk
grammar = nltk.CFG.fromstring("""
S -> NP VP
NP -> 'Ram'
VP -> V NP
V -> 'likes'
""")
parser = nltk.ChartParser(grammar)
sentence = input("Enter sentence: ").split()
for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print()
