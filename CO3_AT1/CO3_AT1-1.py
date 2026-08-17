from collections import Counter
import re

# English text corpus
corpus = """
The student is studying computer science.
The student is reading a book.
The student is writing a program.
The student is learning Python.
The teacher is teaching computer science.
The teacher is reading a book.
The teacher is writing notes.
The student likes computer science.
The student likes programming.
The student is practicing programming.
"""

# --------------------------------------------------
# 1. Preprocessing and Tokenization
# --------------------------------------------------

sentences = re.split(r'[.!?]+', corpus.lower())

tokenized_sentences = []

for sentence in sentences:
    words = re.findall(r'\b[a-z]+\b', sentence)

    if words:
        tokenized_sentences.append(["<s>"] + words + ["</s>"])

# --------------------------------------------------
# 2. Generate N-gram Counts
# --------------------------------------------------

unigram_counts = Counter()
bigram_counts = Counter()
trigram_counts = Counter()

for sentence in tokenized_sentences:

    # Unigrams
    for word in sentence:
        unigram_counts[word] += 1

    # Bigrams
    for i in range(len(sentence) - 1):
        bigram = (sentence[i], sentence[i + 1])
        bigram_counts[bigram] += 1

    # Trigrams
    for i in range(len(sentence) - 2):
        trigram = (sentence[i], sentence[i + 1], sentence[i + 2])
        trigram_counts[trigram] += 1

# --------------------------------------------------
# 3. Probability Functions
# --------------------------------------------------

def unigram_probability(word):
    total = sum(unigram_counts.values())

    if unigram_counts[word] == 0:
        return 0

    return unigram_counts[word] / total


def bigram_probability(word1, word2):
    denominator = unigram_counts[word1]

    if denominator == 0:
        return 0

    return bigram_counts[(word1, word2)] / denominator


def trigram_probability(word1, word2, word3):
    denominator = bigram_counts[(word1, word2)]

    if denominator == 0:
        return 0

    return trigram_counts[(word1, word2, word3)] / denominator

# --------------------------------------------------
# 4. Display Counts and Probabilities
# --------------------------------------------------

print("\n" + "=" * 70)
print("N-GRAM FREQUENCY COUNTS AND PROBABILITIES")
print("=" * 70)

print("\nUNIGRAMS")
for word, count in unigram_counts.items():
    print(f"{word:<15} Count = {count:<3} Probability = {unigram_probability(word):.4f}")

print("\nBIGRAMS")
for pair, count in bigram_counts.items():
    probability = bigram_probability(pair[0], pair[1])
    print(f"{str(pair):<30} Count = {count:<3} Probability = {probability:.4f}")

print("\nTRIGRAMS")
for triple, count in trigram_counts.items():
    probability = trigram_probability(triple[0], triple[1], triple[2])
    print(f"{str(triple):<40} Count = {count:<3} Probability = {probability:.4f}")

# --------------------------------------------------
# 5. Top-5 Next Word Prediction
# --------------------------------------------------

def predict_next_words(text, n):

    words = re.findall(r'\b[a-z]+\b', text.lower())

    candidates = []

    if n == 1:
        for word in unigram_counts:
            if word not in ["<s>", "</s>"]:
                probability = unigram_probability(word)
                candidates.append((word, probability))

    elif n == 2:
        previous_word = words[-1]

        for word in unigram_counts:
            probability = bigram_probability(previous_word, word)

            if probability > 0 and word not in ["<s>", "</s>"]:
                candidates.append((word, probability))

    elif n == 3:

        if len(words) < 2:
            return []

        word1 = words[-2]
        word2 = words[-1]

        for word in unigram_counts:
            probability = trigram_probability(word1, word2, word)

            if probability > 0 and word not in ["<s>", "</s>"]:
                candidates.append((word, probability))

    candidates.sort(key=lambda x: x[1], reverse=True)

    return candidates[:5]

# --------------------------------------------------
# 6. User Selection of N
# --------------------------------------------------

try:
    n = int(input("\nEnter N (1, 2, or 3): "))

    if n not in [1, 2, 3]:
        print("Invalid N. Please choose 1, 2, or 3.")
    else:

        test_sentence = "The student is"

        predictions = predict_next_words(test_sentence, n)

        print("\n" + "=" * 70)
        print(f"TOP-5 PREDICTIONS FOR: '{test_sentence}'")
        print(f"N = {n}")
        print("=" * 70)

        if predictions:
            for i, (word, probability) in enumerate(predictions, 1):
                print(f"{i}. {word:<15} Probability = {probability:.4f}")
        else:
            print("No prediction available.")

# --------------------------------------------------
# 7. Demonstrate Unseen N-gram
# --------------------------------------------------

        print("\n" + "=" * 70)
        print("UNSEEN N-GRAM DEMONSTRATION")
        print("=" * 70)

        unseen_bigram = ("student", "football")
        unseen_probability = bigram_probability(
            unseen_bigram[0],
            unseen_bigram[1]
        )

        print(f"Bigram: {unseen_bigram}")
        print(f"Probability: {unseen_probability:.4f}")

        if unseen_probability == 0:
            print("Unseen bigram receives zero probability.")

except ValueError:
    print("Please enter a valid integer.")
