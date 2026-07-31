import re
print("=" * 60)
print("      NLP - INFORMATION EXTRACTION USING REGULAR EXPRESSIONS")
print("=" * 60)
print("\nEnter the text:")
text = input()
# Email Addresses
emails = re.findall(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', text)
# Phone Numbers (Indian)
phones = re.findall(r'\b(?:\+91[- ]?)?[6-9]\d{9}\b', text)
# URLs
urls = re.findall(r'https?://[^\s]+', text)
# Dates (DD-MM-YYYY or DD/MM/YYYY)
dates = re.findall(r'\b\d{2}[-/]\d{2}[-/]\d{4}\b', text)
# Time (HH:MM or HH:MM:SS)
times = re.findall(r'\b\d{1,2}:\d{2}(?::\d{2})?\b', text)
# PIN Codes (6 digits)
pincodes = re.findall(r'\b\d{6}\b', text)
# Currency Amounts
currency = re.findall(r'₹\d+(?:,\d{3})*(?:\.\d{2})?|\$\d+(?:,\d{3})*(?:\.\d{2})?', text)
# Percentages
percentages = re.findall(r'\b\d+(?:\.\d+)?%', text)
# Hashtags
hashtags = re.findall(r'#\w+', text)
# Mentions
mentions = re.findall(r'@\w+', text)
# Capitalized Words (Proper Nouns)
capital_words = re.findall(r'\b[A-Z][a-z]+\b', text)
# Numbers
numbers = re.findall(r'\b\d+\b', text)
# Words
words = re.findall(r'\b\w+\b', text)
# Sentences
sentences = re.split(r'[.!?]+', text)
sentences = [s.strip() for s in sentences if s.strip()]

print("\n" + "=" * 60)
print("             EXTRACTED INFORMATION")
print("=" * 60)

print("\n1. Email Addresses")
print(emails)

print("\n2. Phone Numbers")
print(phones)

print("\n3. URLs")
print(urls)

print("\n4. Dates")
print(dates)

print("\n5. Time")
print(times)

print("\n6. PIN Codes")
print(pincodes)

print("\n7. Currency Values")
print(currency)

print("\n8. Percentages")
print(percentages)

print("\n9. Hashtags")
print(hashtags)

print("\n10. Mentions")
print(mentions)

print("\n11. Capitalized Words")
print(capital_words)

print("\n12. Numbers")
print(numbers)

print("\n13. Words")
print(words)

print("\n14. Sentences")
for i, sentence in enumerate(sentences, start=1):
    print(f"{i}. {sentence}")

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)

print("Total Emails      :", len(emails))
print("Total Phones      :", len(phones))
print("Total URLs        :", len(urls))
print("Total Dates       :", len(dates))
print("Total Times       :", len(times))
print("Total PIN Codes   :", len(pincodes))
print("Total Currency    :", len(currency))
print("Total Percentages :", len(percentages))
print("Total Hashtags    :", len(hashtags))
print("Total Mentions    :", len(mentions))
print("Total Words       :", len(words))
print("Total Sentences   :", len(sentences))

print("\nProgram Completed Successfully.")
