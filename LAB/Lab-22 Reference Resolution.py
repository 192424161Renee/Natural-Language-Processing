import spacy

nlp = spacy.load("en_core_web_sm")

text = "John went to the library. He borrowed a book. The book was interesting. John returned it later."

doc = nlp(text)

# Store previously mentioned nouns
previous_nouns = []

pronouns = {
    "he", "she", "it", "they", "him", "her",
    "them", "his", "hers", "their", "its"
}

print("Text:")
print(text)

print("\nReference Resolution:")
print("-" * 50)

for token in doc:

    # Store nouns and proper nouns
    if token.pos_ in ["NOUN", "PROPN"]:
        previous_nouns.append(token.text)

    # Check pronouns
    if token.text.lower() in pronouns:

        if previous_nouns:
            reference = previous_nouns[-1]

            print(
                "Pronoun:", token.text,
                "-> Refers to:", reference
            )
