from collections import Counter
import re
import math

training_corpus = """
the student is reading a book
the student is studying computer science
the student is learning python
the student is writing a program
the teacher is reading a book
the teacher is teaching computer science
the teacher is explaining the lesson
the student likes computer science
the student likes programming
the student is practicing programming
"""

test_corpus = """
the student is reading
the teacher is teaching
the student is learning
the teacher is writing
"""

def tokenize(text):
    return re.findall(r'\b[a-z]+\b', text.lower())

train_sentences = [
    tokenize(sentence)
    for sentence in training_corpus.split("\n")
    if sentence.strip()
]

test_sentences = [
    tokenize(sentence)
    for sentence in test_corpus.split("\n")
    if sentence.strip()
]

unigram = Counter()
bigram = Counter()
trigram = Counter()

for sentence in train_sentences:

    words = ["<s>", "<s>"] + sentence + ["</s>"]

    for word in words:
        unigram[word] += 1

    for i in range(len(words) - 1):
        bigram[(words[i], words[i + 1])] += 1

    for i in range(len(words) - 2):
        trigram[
            (words[i], words[i + 1], words[i + 2])
        ] += 1

total_words = sum(unigram.values())
vocabulary = set(unigram.keys())
vocabulary_size = len(vocabulary)


def unigram_probability(word):
    return unigram[word] / total_words


def bigram_probability(w1, w2):
    if unigram[w1] == 0:
        return 0

    return bigram[(w1, w2)] / unigram[w1]


def trigram_probability(w1, w2, w3):
    if bigram[(w1, w2)] == 0:
        return 0

    return trigram[(w1, w2, w3)] / bigram[(w1, w2)]


def smoothed_unigram_probability(word):
    return (unigram[word] + 1) / (
        total_words + vocabulary_size
    )


def smoothed_bigram_probability(w1, w2):
    return (bigram[(w1, w2)] + 1) / (
        unigram[w1] + vocabulary_size
    )


def smoothed_trigram_probability(w1, w2, w3):
    return (trigram[(w1, w2, w3)] + 1) / (
        bigram[(w1, w2)] + vocabulary_size
    )


def calculate_entropy(sentence, n, smoothing=False):

    words = ["<s>", "<s>"] + sentence
    log_probability = 0
    count = 0

    for i in range(2, len(words)):

        word = words[i]

        if n == 1:
            if smoothing:
                probability = smoothed_unigram_probability(word)
            else:
                probability = unigram_probability(word)

        elif n == 2:
            if smoothing:
                probability = smoothed_bigram_probability(
                    words[i - 1], word
                )
            else:
                probability = bigram_probability(
                    words[i - 1], word
                )

        else:
            if smoothing:
                probability = smoothed_trigram_probability(
                    words[i - 2],
                    words[i - 1],
                    word
                )
            else:
                probability = trigram_probability(
                    words[i - 2],
                    words[i - 1],
                    word
                )

        if probability == 0:
            return float("inf")

        log_probability += math.log2(probability)
        count += 1

    return -log_probability / count


print("=" * 80)
print("N-GRAM ENTROPY EVALUATION")
print("=" * 80)

for n in [1, 2, 3]:

    print("\n" + "-" * 80)
    print("N-GRAM MODEL:", n)
    print("-" * 80)

    for sentence in test_sentences:

        entropy = calculate_entropy(
            sentence,
            n,
            smoothing=False
        )

        smoothed_entropy = calculate_entropy(
            sentence,
            n,
            smoothing=True
        )

        print(
            "Sentence:",
            " ".join(sentence)
        )

        if math.isinf(entropy):
            print("Unsmoothed Entropy: Infinite")
        else:
            print(
                "Unsmoothed Entropy:",
                round(entropy, 4)
            )

        print(
            "Smoothed Entropy:",
            round(smoothed_entropy, 4)
        )

        if math.isinf(entropy):
            print(
                "Interpretation: High uncertainty due to unseen N-grams."
            )
        elif entropy < 2:
            print(
                "Interpretation: Low uncertainty and predictable sequence."
            )
        else:
            print(
                "Interpretation: Higher uncertainty and less predictable sequence."
            )

print("\n" + "=" * 80)
print("OVERALL ENTROPY")
print("=" * 80)

for n in [1, 2, 3]:

    total_entropy = 0
    total_smoothed_entropy = 0
    valid_count = 0

    for sentence in test_sentences:

        entropy = calculate_entropy(
            sentence,
            n,
            smoothing=False
        )

        smoothed_entropy = calculate_entropy(
            sentence,
            n,
            smoothing=True
        )

        if not math.isinf(entropy):
            total_entropy += entropy
            valid_count += 1

        total_smoothed_entropy += smoothed_entropy

    if valid_count > 0:
        average_entropy = total_entropy / valid_count
    else:
        average_entropy = float("inf")

    average_smoothed_entropy = (
        total_smoothed_entropy / len(test_sentences)
    )

    print("\nN =", n)

    if math.isinf(average_entropy):
        print("Average Unsmoothed Entropy: Infinite")
    else:
        print(
            "Average Unsmoothed Entropy:",
            round(average_entropy, 4)
        )

    print(
        "Average Smoothed Entropy:",
        round(average_smoothed_entropy, 4)
    )

print("\n" + "=" * 80)
print("ENTROPY INTERPRETATION")
print("=" * 80)

print(
    "Low entropy indicates that the next word is more predictable."
)

print(
    "High entropy indicates greater uncertainty in word prediction."
)

print(
    "Unseen N-grams produce zero probability and infinite entropy "
    "in an unsmoothed model."
)

print(
    "Smoothing assigns non-zero probabilities to unseen events, "
    "making entropy finite and predictions more reliable."
)
