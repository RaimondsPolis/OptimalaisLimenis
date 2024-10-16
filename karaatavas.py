import random

def randomVards():
    words = ['alus', 'ugunskurs', 'latvija', 'burgers', 'programmesana', 'karatavas', 'skola']
    return random.choice(words)# vajag 2 mainīgos tapēc viens ir 'word' otrs ir 'vards'

def raditVardu(vards, minetieBurti):
    return ' '.join([burts if burts in minetieBurti else '_' for burts in vards])

def raditKaratavas(meginajumi):
    stages = [ #negribeju rakstīt 'fazes', stages jūtas pareizāk :)
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
    return stages[meginajumi]

def spelet():
    vards = randomVards()
    minetieBurti = []
    meginajumi = 6
    print("SVEICINĀTS ELLĒ!!! MUHAHAHAHAHAHAHAHHAHAHAAA")

    while meginajumi > 0:
        print(raditKaratavas(meginajumi))
        print(f"Mināmais vārds: {raditVardu(vards, minetieBurti)}")
        print(f"Nepareizi minējumi līdz nāvei: {meginajumi}")
        minejums = input("Mini burtus: ").lower()# .lower() ir lai ievadītais burts būtu lowercase

        if minejums in minetieBurti:
            print("Šo burtu jau esi minējis!")
        elif minejums in vards:
            minetieBurti.append(minejums)
        else:
            meginajumi -= 1
            minetieBurti.append(minejums)
            print(f"{minejums} nav šaja vārdā ")

        if all(letter in minetieBurti for letter in vards):
            print("\n Apsveicu, nenomiri! :)")
            print(f'pareizais vārds bija "{vards}"')
            break  
    
    if meginajumi == 6:
        print("Woah dude, tev palaimējās, jeb tu esi filthy cheater???")

    if meginajumi == 0:
        print(raditKaratavas(meginajumi))
        print(f"\n Tu nomiri! pareizais vārds bija '{vards}'.")

if __name__ == "__main__": # šis bija mācīts programmēšana II pie Britālas
    spelet()
