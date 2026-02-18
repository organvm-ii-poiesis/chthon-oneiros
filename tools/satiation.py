import sys
import random

# CHTHON-ONEIROS: The Semantic Satiation Engine
# Goal: Automate the "Infectious Phoneme" by repeating a seed word with mutations.

GLITCH_MAP = {
    "a": ["ᚪ", "@", "4"],
    "e": ["ᛖ", "3", "&"],
    "i": ["ᛁ", "1", "!"],
    "o": ["ᚩ", "0", "()"],
    "u": ["ᚢ", "µ", "v"],
    "s": ["ᛋ", "5", "$"]
}

def mutate_word(word, intensity):
    word_list = list(word)
    for i in range(len(word_list)):
        if random.random() < intensity:
            char = word_list[i].lower()
            if char in GLITCH_MAP:
                word_list[i] = random.choice(GLITCH_MAP[char])
    return "".join(word_list)

def generate_satiation(seed_word, count=1000):
    output = []
    for i in range(count):
        # Intensity increases every 100 iterations
        intensity = (i // 100) * 0.05
        mutated = mutate_word(seed_word, intensity)
        output.append(mutated)
    
    return " ".join(output)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python satiation.py <seed_word> [count]")
        sys.exit(1)
    
    word = sys.argv[1]
    count = int(sys.argv[2]) if len(sys.argv) > 2 else 1000
    
    print(f"--- INITIATING SATIATION FOR: {word} ---")
    result = generate_satiation(word, count)
    
    file_name = f"museum/satiation_{word.lower()}.md"
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(f"# EXHIBIT: THE INFECTIOUS PHONEME ({word.upper()})\n\n")
        f.write(result)
    
    print(f"Exhibit generated: {file_name}")
