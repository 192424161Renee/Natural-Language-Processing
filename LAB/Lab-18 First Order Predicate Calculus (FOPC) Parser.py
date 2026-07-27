import re
expression = input("Enter logical expression: ")
pattern = r'([A-Z][a-zA-Z]*)\(([a-zA-Z, ]+)\)'
match = re.fullmatch(pattern, expression)
if match:
    predicate = match.group(1)
    arguments = match.group(2).split(',')
    print("Valid FOPC Expression")
    print("Predicate:", predicate)
    print("Arguments:", [arg.strip() for arg in arguments])
else:
    print("Invalid FOPC Expression")
