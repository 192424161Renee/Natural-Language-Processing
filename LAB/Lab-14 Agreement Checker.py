grammar = {
    ("He", "runs"),
    ("She", "runs"),
    ("I", "run"),
    ("They", "run"),
    ("We", "run")
}
subject = input("Enter Subject: ")
verb = input("Enter Verb: ")
if (subject, verb) in grammar:
    print("Sentence is Grammatically Correct")
else:
    print("Sentence is Incorrect")
