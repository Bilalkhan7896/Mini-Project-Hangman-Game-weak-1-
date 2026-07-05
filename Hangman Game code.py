"""
Hangman Game
------------
A simple console-based Hangman game written in Python.

How it works:
- The computer randomly picks a word from a predefined list (or a word file).
- The player guesses one letter at a time.
- Each wrong guess draws another part of the hangman.
- The player wins by guessing the word before the hangman is fully drawn.
- The player loses if they run out of attempts.
"""

import random

# ---------------------------
# Word list (could also be loaded from data/words.txt)
# ---------------------------
WORD_LIST = [
    "python", "hangman", "programming", "computer", "keyboard",
    "developer", "function", "variable", "algorithm", "internet"
]

# ---------------------------
# ASCII art stages for the hangman drawing
# ---------------------------
HANGMAN_STAGES = [
    """
       ------
       |    |
       |
       |
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    ---------
    """
]

MAX_ATTEMPTS = len(HANGMAN_STAGES) - 1  # number of wrong guesses allowed


def choose_word(word_list):
    """Pick a random word from the list."""
    return random.choice(word_list).lower()


def display_word(word, guessed_letters):
    """Show the word with guessed letters revealed and others as underscores."""
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)


def get_guess(guessed_letters):
    """Prompt the player for a single valid letter guess."""
    while True:
        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter (a-z).")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
            continue

        return guess


def play_game():
    """Main game loop."""
    word = choose_word(WORD_LIST)
    guessed_letters = set()
    wrong_guesses = 0

    print("=" * 40)
    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters.")
    print("=" * 40)

    while wrong_guesses < MAX_ATTEMPTS:
        print(HANGMAN_STAGES[wrong_guesses])
        print("Word: " + display_word(word, guessed_letters))
        print(f"Wrong guesses left: {MAX_ATTEMPTS - wrong_guesses}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) or 'None'}")

        guess = get_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            wrong_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.")

        # Check win condition
        if all(letter in guessed_letters for letter in word):
            print(HANGMAN_STAGES[wrong_guesses])
            print(f"Congratulations! You guessed the word: '{word}'")
            return

    # Player lost
    print(HANGMAN_STAGES[wrong_guesses])
    print(f"Game over! You ran out of attempts. The word was: '{word}'")


def main():
    """Entry point: allows replaying the game."""
    while True:
        play_game()
        again = input("\nPlay again? (y/n): ").lower().strip()
        if again != "y":
            print("Thanks for playing Hangman!")
            break


if __name__ == "__main__":
    main()
