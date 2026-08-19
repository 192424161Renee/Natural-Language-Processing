from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

text = """
Artificial intelligence is widely used in healthcare.
AI can help doctors analyze medical data.
Medical data contains important information about patients.
Patient information can be used to improve healthcare decisions.
"""

# Split text into sentences
sentences = [
    sentence.strip()
    for sentence in text.strip().split(".")
    if sentence.strip()
]

print("Sentences:")
for i, sentence in enumerate(sentences, 1):
    print(i, ".", sentence)

# Convert sentences to TF-IDF vectors
vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(sentences)

print("\nCoherence Scores:")
print("-" * 50)

scores = []

for i in range(len(sentences) - 1):

    score = cosine_similarity(
        vectors[i],
        vectors[i + 1]
    )[0][0]

    scores.append(score)

    print(
        f"Sentence {i} -> Sentence {i + 1}: "
        f"{score:.3f}"
    )

# Calculate average coherence
average_score = sum(scores) / len(scores)

print("\nAverage Coherence Score:", round(average_score, 3))

if average_score >= 0.5:
    print("Coherence Level: High")
elif average_score >= 0.2:
    print("Coherence Level: Moderate")
else:
    print("Coherence Level: Low")
