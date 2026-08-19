import spacy
nlp = spacy.load("en_core_web_sm")
sentence = "The intelligent student bought a new laptop from the computer store."
doc = nlp(sentence)
print("Sentence:")
print(sentence)
print("\nNoun Phrases and Their Meanings:")
print("-" * 50)
for chunk in doc.noun_chunks:
    print("Noun Phrase :", chunk.text)
    print("Root        :", chunk.root.text)
    print("Meaning     :", "Entity/Concept represented by", chunk.text)
    print()
