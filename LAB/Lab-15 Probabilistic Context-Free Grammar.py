import nltk
grammar = nltk.PCFG.fromstring("""
S -> NP VP [1.0]
NP -> 'John' [0.5] | 'Mary' [0.5]
VP -> V NP [1.0]
V -> 'likes' [1.0]
""")
parser = nltk.ViterbiParser(grammar)
sentence = input("Enter sentence: ").split()
for tree in parser.parse(sentence):
    print(tree)
    print("Probability:", tree.prob())
