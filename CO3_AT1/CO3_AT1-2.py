from collections import Counter
import re

corpus = """
The student is studying computer science.
The student is reading a book.
The student is writing a program.
The student is learning Python.
The student is practicing programming.
The teacher is teaching computer science.
The teacher is reading a book.
The teacher is writing notes.
The teacher is explaining the lesson.
The student likes computer science.
The student likes programming.
The student is using Python.
"""

sentences = re.split(r'[.!?]+', corpus.lower())

tokenized_sentences = []

for sentence in sentences:
    words = re.findall(r'\b[a-z]+\b', sentence)

    if words:
        tokenized_sentences.append(
            ["<s>", "<s>"] + words + ["</s>"]
        )

unigram = Counter()
bigram = Counter()
trigram = Counter()

for sentence in tokenized_sentences:
    for word in sentence:
        unigram[word] += 1

    for i in range(len(sentence) - 1):
        bigram[(sentence[i], sentence[i + 1])] += 1

    for i in range(len(sentence) - 2):
        trigram[
            (sentence[i], sentence[i + 1], sentence[i + 2])
        ] += 1

total_words = sum(unigram.values())


def unigram_probability(word):
    return unigram[word] / total_words if unigram[word] > 0 else 0


def bigram_probability(w1, w2):
    denominator = unigram[w1]

    if denominator == 0:
        return 0

    return bigram[(w1, w2)] / denominator


def trigram_probability(w1, w2, w3):
    denominator = bigram[(w1, w2)]

    if denominator == 0:
        return 0

    return trigram[(w1, w2, w3)] / denominator


def unsmoothed_probability(words):
    if len(words) >= 2:
        probability = trigram_probability(
            words[-2], words[-1], words[-1]
        )

        if probability > 0:
            return probability

    if len(words) >= 1:
        probability = bigram_probability(
            words[-1], words[-1]
        )

        if probability > 0:
            return probability

    return unigram_probability(words[-1])


def backoff_probability(w1, w2, word):
    p3 = trigram_probability(w1, w2, word)

    if p3 > 0:
        return p3

    p2 = bigram_probability(w2, word)

    if p2 > 0:
        return p2

    return unigram_probability(word)


def interpolation_probability(w1, w2, word):
    lambda1 = 0.2
    lambda2 = 0.3
    lambda3 = 0.5

    p1 = unigram_probability(word)
    p2 = bigram_probability(w2, word)
    p3 = trigram_probability(w1, w2, word)

    return (
        lambda1 * p1 +
        lambda2 * p2 +
        lambda3 * p3
    )


def predict(query):
    words = re.findall(r'\b[a-z]+\b', query.lower())

    if len(words) == 0:
        return None

    if len(words) == 1:
        w1 = "<s>"
        w2 = words[-1]
    else:
        w1 = words[-2]
        w2 = words[-1]

    candidates = [
        word for word in unigram
        if word not in ["<s>", "</s>"]
    ]

    unsmoothed_scores = []
    backoff_scores = []
    interpolation_scores = []

    for word in candidates:

        p3 = trigram_probability(w1, w2, word)

        p2 = bigram_probability(w2, word)

        p1 = unigram_probability(word)

        unsmoothed_scores.append(
            (word, p3)
        )

        backoff_scores.append(
            (word, backoff_probability(w1, w2, word))
        )

        interpolation_scores.append(
            (word, interpolation_probability(w1, w2, word))
        )

    unsmoothed_scores.sort(
        key=lambda x: x[1],
        reverse=True
    )

    backoff_scores.sort(
        key=lambda x: x[1],
        reverse=True
    )

    interpolation_scores.sort(
        key=lambda x: x[1],
        reverse=True
    )

    print("\n" + "=" * 80)
    print("NEXT WORD PREDICTION")
    print("=" * 80)

    print("\nQuery:", query)

    print("\nUnsmoothed Model:")
    if unsmoothed_scores[0][1] == 0:
        print("No valid trigram found. Probability = 0")
    else:
        print(
            unsmoothed_scores[0][0],
            "Probability =",
            round(unsmoothed_scores[0][1], 4)
        )

    print("\nBackoff Model:")
    print(
        backoff_scores[0][0],
        "Probability =",
        round(backoff_scores[0][1], 4)
    )

    print("\nDeleted Interpolation Model:")
    print(
        interpolation_scores[0][0],
        "Probability =",
        round(interpolation_scores[0][1], 4)
    )

    print("\n" + "-" * 80)
    print("TOP-5 BACKOFF PREDICTIONS")
    print("-" * 80)

    for i, (word, probability) in enumerate(
        backoff_scores[:5], 1
    ):
        print(
            i, word,
            "Probability =",
            round(probability, 4)
        )

    print("\n" + "-" * 80)
    print("TOP-5 DELETED INTERPOLATION PREDICTIONS")
    print("-" * 80)

    for i, (word, probability) in enumerate(
        interpolation_scores[:5], 1
    ):
        print(
            i, word,
            "Probability =",
            round(probability, 4)
        )


query = input(
    "\nEnter a sentence/query: "
)

predict(query)
