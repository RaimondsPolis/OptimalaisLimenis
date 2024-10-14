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
    print("SVEICINĀTS ELLĒ!!! MUHAHAHAHAHAHAHAHHAHAHAAA")

    while attempts > 0:
        print(display_hangman(attempts))
        print(f"Mināmais vārds: {display_word(word, guessed_letters)}")
        print(f"Nepareizi minējumi līdz nāvei: {attempts}")
        guess = input("Mini burtus: ").lower()

        if guess in guessed_letters:
            print("Šo burtu jau esi minējis!")
        elif guess in word:
            guessed_letters.append(guess)
        else:
            attempts -= 1
            guessed_letters.append(guess)
            print(f"{guess} nav šaja vārdā ")

        if all(letter in guessed_letters for letter in word):
            print(f"\n Apsveicu, nenomiri! :)")
            break  
    
    if attempts == 6:
        print("Woah dude, tev palaimējās, jeb tu esi filthy cheater???")

    if attempts == 0:
        print(display_hangman(attempts))
        print(f"\n Tu nomiri! pareizais vārds bija '{word}'.")

if __name__ == "__main__":
    play_hangman()
