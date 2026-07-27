grammar = {
    "S": [["a", "S", "b"], ["a", "b"]]
}
def parse(symbols, string):
    if not symbols and not string:
        return True
    if not symbols or not string:
        return False
    first = symbols[0]
    if first in grammar:
        for production in grammar[first]:
            if parse(production + symbols[1:], string):
                return True
        return False
    else:
        if first == string[0]:
            return parse(symbols[1:], string[1:])
        return False
sentence = input("Enter string: ").split()
if parse(["S"], sentence):
    print("String Accepted")
else:
    print("String Rejected")
