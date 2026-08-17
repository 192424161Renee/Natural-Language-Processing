from collections import Counter, defaultdict
import re

training_data = [
    [("the", "DT"), ("student", "NN"), ("is", "VBZ"),
     ("reading", "VBG"), ("a", "DT"), ("book", "NN")],

    [("the", "DT"), ("teacher", "NN"), ("is", "VBZ"),
     ("teaching", "VBG"), ("computer", "NN"), ("science", "NN")],

    [("she", "PRP"), ("is", "VBZ"), ("writing", "VBG"),
     ("a", "DT"), ("program", "NN")],

    [("he", "PRP"), ("plays", "VBZ"),
     ("football", "NN")],

    [("the", "DT"), ("student", "NN"),
     ("quickly", "RB"), ("completed", "VBD"),
     ("the", "DT"), ("assignment", "NN")],

    [("they", "PRP"), ("are", "VBP"),
     ("learning", "VBG"), ("python", "NN")]
]

lexicon = {
    "the": "DT",
    "a": "DT",
    "an": "DT",
    "student": "NN",
    "teacher": "NN",
    "book": "NN",
    "computer": "NN",
    "science": "NN",
    "program": "NN",
    "football": "NN",
    "assignment": "NN",
    "python": "NN",
    "she": "PRP",
    "he": "PRP",
    "they": "PRP",
    "we": "PRP",
    "i": "PRP",
    "is": "VBZ",
    "are": "VBP",
    "am": "VBP",
    "plays": "VBZ",
    "reading": "VBG",
    "writing": "VBG",
    "teaching": "VBG",
    "learning": "VBG",
    "completed": "VBD",
    "quickly": "RB",
    "in": "IN",
    "on": "IN",
    "and": "CC",
    "but": "CC"
}

tag_counts = Counter()
word_tag_counts = Counter()
transition_counts = Counter()

for sentence in training_data:

    previous_tag = "<START>"

    for word, tag in sentence:
        tag_counts[tag] += 1
        word_tag_counts[(word, tag)] += 1
        transition_counts[(previous_tag, tag)] += 1
        previous_tag = tag


def tokenize(sentence):
    return re.findall(r"\b[a-zA-Z]+\b", sentence.lower())


def rule_based_tagger(sentence):

    words = tokenize(sentence)
    tags = []

    for word in words:

        if word in lexicon:
            tag = lexicon[word]

        elif word.endswith("ly"):
            tag = "RB"

        elif word.endswith("ing"):
            tag = "VBG"

        elif word.endswith("ed"):
            tag = "VBD"

        elif word.endswith("s"):
            tag = "NNS"

        elif word.endswith(("ful", "ous", "ive", "al")):
            tag = "JJ"

        elif word in ["in", "on", "at", "by", "with", "from"]:
            tag = "IN"

        elif word in ["and", "or", "but"]:
            tag = "CC"

        else:
            tag = "NN"

        tags.append((word, tag))

    return tags


def stochastic_tagger(sentence):

    words = tokenize(sentence)
    tags = []

    previous_tag = "<START>"

    possible_tags = list(tag_counts.keys())

    for word in words:

        best_tag = None
        best_score = -1

        for tag in possible_tags:

            word_probability = (
                word_tag_counts[(word, tag)] + 1
            ) / (
                tag_counts[tag] + len(lexicon)
            )

            transition_probability = (
                transition_counts[(previous_tag, tag)] + 1
            ) / (
                sum(
                    transition_counts[
                        (previous_tag, t)
                    ]
                    for t in possible_tags
                ) + len(possible_tags)
            )

            score = (
                word_probability *
                transition_probability
            )

            if score > best_score:
                best_score = score
                best_tag = tag

        tags.append((word, best_tag))
        previous_tag = best_tag

    return tags


def transformation_based_tagger(sentence):

    tagged = rule_based_tagger(sentence)

    for i in range(len(tagged)):

        word, tag = tagged[i]

        previous_tag = tagged[i - 1][1] if i > 0 else None
        previous_word = tagged[i - 1][0] if i > 0 else None

        if (
            previous_tag == "PRP"
            and tag == "NN"
            and word.endswith("ing")
        ):
            tagged[i] = (word, "VBG")

        elif (
            previous_tag in ["VBZ", "VBP"]
            and tag == "NN"
            and word.endswith("ing")
        ):
            tagged[i] = (word, "VBG")

        elif (
            previous_tag == "PRP"
            and tag == "NN"
            and word in [
                "plays",
                "reads",
                "writes",
                "runs"
            ]
        ):
            tagged[i] = (word, "VBZ")

        elif (
            previous_word in ["is", "are", "am"]
            and tag == "NN"
            and word.endswith("ing")
        ):
            tagged[i] = (word, "VBG")

    return tagged


def display(title, tagged):

    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)

    for word, tag in tagged:
        print(f"{word:<15} {tag}")


test_sentences = [
    "The student is reading a book",
    "She is writing a program",
    "He plays football",
    "They are learning Python"
]

for sentence in test_sentences:

    print("\n\n" + "#" * 70)
    print("INPUT:", sentence)
    print("#" * 70)

    rule_result = rule_based_tagger(sentence)
    stochastic_result = stochastic_tagger(sentence)
    transformation_result = transformation_based_tagger(sentence)

    display("RULE-BASED TAGGER", rule_result)
    display("STOCHASTIC TAGGER", stochastic_result)
    display(
        "TRANSFORMATION-BASED TAGGER",
        transformation_result
    )

print("\n" + "=" * 70)
print("PENN TREEBANK TAGSET")
print("=" * 70)

print("NN  = Noun")
print("NNS = Plural Noun")
print("VB  = Base Verb")
print("VBD = Past Tense Verb")
print("VBG = Gerund/Present Participle")
print("VBP = Non-3rd Person Present Verb")
print("VBZ = 3rd Person Singular Verb")
print("JJ  = Adjective")
print("RB  = Adverb")
print("PRP = Personal Pronoun")
print("DT  = Determiner")
print("IN  = Preposition")
print("CC  = Coordinating Conjunction")

print("\n" + "=" * 70)
print("COMPARISON")
print("=" * 70)

print("Rule-Based: Simple and interpretable but depends on predefined rules.")
print("Stochastic: Uses statistical probabilities and contextual information.")
print("Transformation-Based: Corrects initial tags using contextual rules.")
print("Best Approach: Transformation-based tagging generally improves")
print("the initial rule-based results when suitable correction rules exist.")
