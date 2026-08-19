from deep_translator import GoogleTranslator

# Get English input from user
english_text = input("Enter English text: ")

# Translate English to French
french_text = GoogleTranslator(
    source="en",
    target="fr"
).translate(english_text)

# Display output
print("\nEnglish:")
print(english_text)

print("\nFrench:")
print(french_text)
