from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
documents = [
    "Artificial Intelligence is the future",
    "Machine Learning is a branch of AI",
    "Python is used in Artificial Intelligence"
]
query = input("Enter search query: ")
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents + [query])
similarity = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])
scores = similarity.flatten()
ranking = sorted(enumerate(scores), key=lambda x: x[1], reverse=True)
print("\nDocument Ranking:")
for index, score in ranking:
    print(f"Document {index+1}: Score = {score:.3f}")
    print(documents[index])
    print()
