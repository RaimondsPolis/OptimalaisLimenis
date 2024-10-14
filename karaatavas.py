import random

def get_random_word():
    words = ['alus', 'ugunskurs', 'latvija', 'burgers', 'programmesana', 'karatavas', 'skola']
    return random.choice(words)

def display_word(vards, minetieBurti):
    return ' '.join([burts if burts in minetieBurti else '_' for burts in vards])

def display_hangman(attempts):
    stages = [
        """
            +---+
            |   |
            O   |
           /|\  |
           / \  |
                |
        =========

        """,
        """
           +---+
           |   |
           O   |
          /|\  |
          /    |
               |
        ========
        """,
        """
           +---+
           |   |
           O   |
          /|\  |
               |
               |
        ========
        """,
        """
           +---+
           |   |
           O   |
          /|   |
               |
               |
        ========
        """,
        """
           +---+
           |   |
           O   |
           |   |
               |
               |
        ========
        """,
        """
           +---+
           |   |
           O   |
               |
               |
               |
        ========
        """,
        """
           +---+
           |   |
               |
               |
               |
               |
        ========
        """
    ]
    return stages[attempts]

def spelet():
    vards = get_random_word()
    minetieBurti = []
    attempts = 6
    print("SVEICINĀTS ELLĒ!!! MUHAHAHAHAHAHAHAHHAHAHAAA")

    while attempts > 0:
        print(display_hangman(attempts))
        print(f"Mināmais vārds: {display_word(vards, minetieBurti)}")
        print(f"Nepareizi minējumi līdz nāvei: {attempts}")
        guess = input("Mini burtus: ").lower()

        if guess in minetieBurti:
            print("Šo burtu jau esi minējis!")
        elif guess in vards:
            minetieBurti.append(guess)
        else:
            attempts -= 1
            minetieBurti.append(guess)
            print(f"{guess} nav šaja vārdā ")

        if all(letter in minetieBurti for letter in vards):
            print("\n Apsveicu, nenomiri! :)")
            print(f'pareizais vārds bija "{vards}"')
            break  
    
    if attempts == 6:
        print("Woah dude, tev palaimējās, jeb tu esi filthy cheater???")

    if attempts == 0:
        print(display_hangman(attempts))
        print(f"\n Tu nomiri! pareizais vārds bija '{vards}'.")

if __name__ == "__main__":
    spelet()
