import random
import string

TOTAL_ROUNDS = 10

print("=== Alphabet Guessing Game ===")
print("Rule: Your word must start with the given alphabet.\n")

for round_no in range(1, TOTAL_ROUNDS + 1):
    alphabet = random.choice(string.ascii_lowercase)

    print(f"Round {round_no}")
    print(f"Random Alphabet: {alphabet.upper()}")

    user_word = input("Enter a word: ").strip().lower()

    if user_word.startswith(alphabet):
        print("✅ Correct! Well done.\n")
    else:
        print("❌ Incorrect. Better luck next time.\n")

print("🎉 Game Over! Thanks for playing.")
