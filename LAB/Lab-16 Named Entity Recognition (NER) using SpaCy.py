import re
text = input("Enter text: ")
persons = re.findall(r'\b[A-Z][a-z]+\b', text)
years = re.findall(r'\b\d{4}\b', text)
locations = ["India", "Chennai", "Delhi", "Mumbai", "London", "Paris", "America", "Hawaii"]
print("\nNamed Entities:")
found = False
for person in persons:
    print(person, "-> PERSON")
    found = True
for location in locations:
    if location in text:
        print(location, "-> LOCATION")
        found = True
for year in years:
    print(year, "-> DATE")
    found = True
if not found:
    print("No named entities found.")
