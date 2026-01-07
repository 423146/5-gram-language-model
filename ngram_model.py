import random
import re
from collections import defaultdict

# Load and preprocess text
def load_text(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read().lower()
    # remove punctuation and special characters
    text = re.sub(r"[^a-z\s]", "", text)
    return text.split()

# Build n-gram model (n = 5)
def build_ngram_model(words, n=5):
    model = defaultdict(list)
    for i in range(len(words) - n + 1):
        context = tuple(words[i:i+n-1])   # previous 4 words
        next_word = words[i+n-1]          # predicted word
        model[context].append(next_word)
    return model

# Generate text using the model
def generate_text(model, seed_text, length=30):
    seed_words = seed_text.lower().split()
    output = seed_words[:]

    for _ in range(length):
        context = tuple(output[-4:])
        if context in model:
            next_word = random.choice(model[context])
            output.append(next_word)
        else:
            break

    return " ".join(output)

# ---------------- MAIN PROGRAM ----------------

if __name__ == "__main__":
    # Load dataset
    words = load_text("austen.txt")

    # Build 5-gram model
    model = build_ngram_model(words, n=5)

    # Sample inputs
    samples = [
    "she was not very",
    "it was a very",
    "mr darcy was"
   ]


    # Generate outputs
    for sample in samples:
        print("\nInput :", sample)
        print("Output:", generate_text(model, sample))
