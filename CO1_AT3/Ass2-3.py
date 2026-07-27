import re
print("Enter the text (type END to finish):")
lines = []
while True:
    line = input()
    if line.upper() == "END":
        break
    lines.append(line)
text = "\n".join(lines)
while True:
    print("\n1.Search Word")
    print("2.Search Prefix")
    print("3.Search Suffix")
    print("4.Search Date")
    print("5.Search Phone Number")
    print("6.Search Hashtag")
    print("7.Search Mention")
    print("8.Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        word = input("Enter word: ")
        print(re.findall(r'\b' + word + r'\b', text))
    elif choice == "2":
        prefix = input("Enter prefix: ")
        print(re.findall(r'\b' + prefix + r'\w*', text))
    elif choice == "3":
        suffix = input("Enter suffix: ")
        print(re.findall(r'\b\w*' + suffix + r'\b', text))
    elif choice == "4":
        print(re.findall(r'\b\d{2}/\d{2}/\d{4}\b', text))
    elif choice == "5":
        print(re.findall(r'\b\d{10}\b', text))
    elif choice == "6":
        print(re.findall(r'#\w+', text))
    elif choice == "7":
        print(re.findall(r'@\w+', text))
    elif choice == "8":
        print("Program Ended")
        break
    else:
        print("Invalid Choice")
