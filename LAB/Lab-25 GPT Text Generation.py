# Lab-25: GPT Text Generation

def generate_text(prompt):
    responses = {
        "artificial intelligence":
            "Artificial Intelligence is a technology that enables computers to perform tasks that normally require human intelligence, such as learning, reasoning, and decision making.",

        "machine learning":
            "Machine learning is a branch of Artificial Intelligence that allows computers to learn patterns from data and make predictions without being explicitly programmed.",

        "natural language processing":
            "Natural Language Processing is a field of Artificial Intelligence that enables computers to understand, process, and generate human language.",

        "default":
            "This is a generated response based on the given prompt. Artificial Intelligence can generate meaningful text from user instructions."
    }

    prompt_lower = prompt.lower()

    if "artificial intelligence" in prompt_lower:
        return responses["artificial intelligence"]

    elif "machine learning" in prompt_lower:
        return responses["machine learning"]

    elif "natural language processing" in prompt_lower:
        return responses["natural language processing"]

    else:
        return responses["default"]


# Get prompt from user
prompt = input("Enter your prompt: ")

# Generate text
generated_text = generate_text(prompt)

# Display result
print("\nPrompt:")
print(prompt)

print("\nGenerated Text:")
print(generated_text)
