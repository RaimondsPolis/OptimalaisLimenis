class Grieziens():
    def __int__(spin, balva, maksa, macins):
        spin.prize = balva
        spin.cost = maksa
        spin.wallet = macins
    def play(spin):
        spin.wallet -=1
    def uzvara(spin):
        spin.wallet +=2
    def WinCon(spin):
        spin.Wcondition = 1
i = 1
import random
symbols = [1, 2, 3]

def spin():
    return random.choice(symbols)

roulette = Grieziens(2, 1, 10)

while i < 2:
    yes = input("do you want to gamble? Y/N  ")
    if yes == "N":
        i=3
        print(roulette.wallet + " credits left, GG!")   
    if yes == "Y":
        roulette.play()
        if roulette.Wcondition == spin:
            print("You win!")
            roulette.uzvara()
            print(roulette.wallet + " credits remaining. ")
        else:
            print("You lose!")
            print(roulette.wallet + " credits remaining. ")



