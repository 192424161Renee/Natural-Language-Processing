def check_string(string):
    state = 0
    for ch in string:
        if state == 0:
            if ch == 'a':
                state = 1
            else:
                state = 0
        elif state == 1:
            if ch == 'b':
                state = 2
            elif ch == 'a':
                state = 1
            else:
                state = 0
        elif state == 2:
            if ch == 'a':
                state = 1
            else:
                state = 0
    if state == 2:
        print("String Accepted")
    else:
        print("String Rejected")
text = input("Enter a string: ")
check_string(text)
