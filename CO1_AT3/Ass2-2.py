transition = {
    'q0': {'a': 'q1', 'b': 'q0'},
    'q1': {'a': 'q1', 'b': 'q2'},
    'q2': {'a': 'q1', 'b': 'q0'}
}
initial_state = 'q0'
final_state = 'q2'
n = int(input("Enter number of strings: "))
for i in range(n):
    string = input("Enter string: ")
    state = initial_state
    path = state
    for ch in string:
        if ch not in ['a', 'b']:
            print("Invalid Input")
            state = None
            break
        state = transition[state][ch]
        path += " -> " + state
    if state:
        print("Transition Path:", path)
        if state == final_state:
            print("Accepted")
        else:
            print("Rejected")
    print()
