import random

def get_random_word():
    words = ['python', 'hangman', 'challenge', 'programming', 'computer', 'artificial', 'intelligence']
    return random.choice(words)

def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def display_hangman(attempts):
    stages = [
        """
           -----
           |   |
           O   |
          /|\  |
          / \  |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|\  |
          /    |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|\  |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        ---------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        ---------
        """,
        """
           -----
           |   |
               |
               |
               |
               |
        ---------
        """
    ]
    return stages[attempts]

def play_hangman():
    word = get_random_word()
    guessed_letters = []
    attempts = 6
    print("Welcome to Hangman!")

    while attempts > 0:
        print(display_hangman(attempts))
        print(f"Word: {display_word(word, guessed_letters)}")
        print(f"Attempts left: {attempts}")
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter!")
        elif guess in word:
            guessed_letters.append(guess)
            print(f"Good guess! '{guess}' is in the word.")
        else:
            attempts -= 1
            guessed_letters.append(guess)
            print(f"Sorry, '{guess}' is not in the word.")

        if all(letter in guessed_letters for letter in word):
            print(f"\nCongratulations! You've guessed the word '{word}' correctly!")
            break

    if attempts == 0:
        print(display_hangman(attempts))
        print(f"\nGame Over! The word was '{word}'.")

if __name__ == "__main__":
    play_hangman()
