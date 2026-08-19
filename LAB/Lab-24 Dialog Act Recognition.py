def recognize_dialog_act(sentence):

    text = sentence.lower().strip()

    # Greeting
    if any(word in text for word in [
        "hello", "hi", "hey", "good morning", "good afternoon"
    ]):
        return "Greeting"

    # Goodbye
    elif any(word in text for word in [
        "bye", "goodbye", "see you", "see you later"
    ]):
        return "Goodbye"

    # Thanks
    elif any(word in text for word in [
        "thank you", "thanks", "thank"
    ]):
        return "Thanking"

    # Question
    elif text.endswith("?") or text.startswith(
        ("what", "why", "when", "where", "who", "how", "is", "are", "can")
    ):
        return "Question"

    # Request
    elif any(word in text for word in [
        "please", "could you", "would you", "can you"
    ]):
        return "Request"

    # Agreement
    elif any(word in text for word in [
        "yes", "okay", "sure", "correct", "alright"
    ]):
        return "Agreement"

    # Negative response
    elif any(word in text for word in [
        "no", "not", "never", "cannot"
    ]):
        return "Disagreement/Negative Response"

    else:
        return "Statement"


# Example conversation
conversation = [
    "Hello!",
    "How are you?",
    "Can you help me with my assignment?",
    "Sure, I can help you.",
    "Thank you!",
    "Goodbye!"
]

print("Dialog Act Recognition")
print("-" * 50)

for sentence in conversation:

    act = recognize_dialog_act(sentence)

    print(f"Text: {sentence}")
    print(f"Dialog Act: {act}")
    print()
