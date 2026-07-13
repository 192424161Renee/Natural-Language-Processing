import re

# Product List
products = [
    "Apple iPhone 15",
    "Apple Watch",
    "Samsung Galaxy S24",
    "Samsung TV",
    "Dell Laptop",
    "HP Laptop",
    "Lenovo Laptop",
    "Sony Headphones",
    "Boat Earbuds",
    "Apple AirPods",
    "Canon Camera",
    "Nikon Camera"
]

keyword = input("Enter search keyword: ")

# Exact Search
exact = [p for p in products if re.fullmatch(keyword, p, re.IGNORECASE)]

# Prefix Search
prefix = [p for p in products if re.match(keyword, p, re.IGNORECASE)]

# Suffix Search
suffix = [p for p in products if re.search(keyword + r"$", p, re.IGNORECASE)]

# Partial Search
partial = [p for p in products if re.search(keyword, p, re.IGNORECASE)]

# Case-Insensitive Search
case_insensitive = partial

print("\n===== Search Results =====")

print("\nExact Match:")
for p in exact:
    print(p)

print("\nPrefix Match:")
for p in prefix:
    print(p)

print("\nSuffix Match:")
for p in suffix:
    print(p)

print("\nPartial Match:")
for p in partial:
    print(p)

print("\nCase-Insensitive Match:")
for p in case_insensitive:
    print(p)

print("\n===== Search Report =====")
print("Exact Matches          :", len(exact))
print("Prefix Matches         :", len(prefix))
print("Suffix Matches         :", len(suffix))
print("Partial Matches        :", len(partial))
print("Case-Insensitive Match :", len(case_insensitive))
