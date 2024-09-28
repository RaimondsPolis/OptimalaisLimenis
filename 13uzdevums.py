import random
def preceUnPVN():
    PreceArPVN = int (input("ievadi preces cenu: "))
    PreceBezPVN = int (PreceArPVN)-(int (PreceArPVN) *(21/100))
    PVN = int (PreceArPVN)*(21/100)
    print(PreceBezPVN)
    print(PVN)

def pastastiParSevi():
    input("Mani sauc: ")
    input("Man patīk: ")
    input("My favourite holiday is: ")
    input("Mans dzimums ir: ")
    input("pasauli vajag: ")

def Pilngadiba():
    gads = int(input("ievadi gadu: "))
    if 2024-gads >=18:
        print("tev ir 18 vai vairāk gadu")
    else:
        print("tev ir mazāk par 18 gadiem")

def movement():
    for i in range(0, 4):
        wasd = input("kur iesi?(wasd): ")
        if wasd == "w":
            print("cilvēciņs iet uz priekšu")
        elif wasd == "a":
            print("cilvēciņš iet pa kreisi")
        elif wasd == "d":
            print("cilvēciņš iet pa labi")
        elif wasd == "s":
            print("cilvēciņš iet uz atpakaļu")
        elif wasd == "A":
            print("cilvēciņš iet pa kreisi")
        elif wasd == "D":
            print("cilvēciņš iet pa labi")
        elif wasd == "S":
            print("cilvēciņš iet uz atpakaļu")
        elif wasd == "W":
            print("cilvēciņs iet uz priekšu")
        else: print("ERROR!!!")

def thousand():
    for i in range(1,1001):
        print(i)

def repetition():
    true = True
    while true:
        true = False
        a = input("vai vēlies programmu atkārtot? y/n vai 1/0: ")
        if a == "y":
            true = True
        elif a =="1":
            true = True
        elif a == "Y":
            true = True

def uzminiskaitli():
    a= random.randint(1,10)
    b = int(input("uzmini  skaitli 1 - 10: "))
    true = True
    while true:
        if b == a:
            true = False
            print("Tu Uzminēji!")
        if b < a:
            b = int(input("vairāk "))
        if b > a:
            b = int(input("mazāk "))

def lettercount():
    vards = input("Uzraksti vārdu: ")
    burts = input("ievadi burtu: ")
    redzets = 0
    for i in vards:
        if i == burts:
            redzets +=1
    print(redzets)

def Divides():
    N = 0
    i=0
    while 1000>N:
        if N % 3 == 0 or N % 5 == 0:
            i = i + N
        N +=1
    print(i)

def fibonacci():
    maxnumber = int(input("Ievadi ciparu: "))

    x=0
    y=0
    r=0
    a=1
    b=2
    list = [1,2]

    while y<1:
        if a<b:
            a += b
            x=a
            list.append(x)
            if maxnumber<x:
                y=1
                a = a - b
            
        elif b<a:
            b += a
            x=b
            list.append(x)
            if maxnumber<x:
                y=1
                b = b - a
        
    for i in range(len(list)):
        if list[i]%2 == 0:
            r += list[i]

    print(a)
    print(b)
    print(list)
    print(r)

def Combinations():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    list = []
    for i in alphabet:
        list.append(i)

    for a in alphabet:
        for b in alphabet:
            print(f"{a}{b}")

def TwoToThe_N_Power():
    number = int(input("ievadi skaitli: "))
    a = 2
    for i in range(1, number):
        a *= 2
    print(a)


preceUnPVN()
pastastiParSevi()
Pilngadiba()
movement()
thousand()
repetition()
uzminiskaitli()
lettercount()
Divides()
fibonacci()
Combinations()
TwoToThe_N_Power()