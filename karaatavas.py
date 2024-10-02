alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
list = []
for i in alphabet:
    list.append(i)

vardu_saraksts = ["BANANA","ELEPHANT","NIGGER","HITLER","PROGRAMMING"]

num = int(input("Izvēlies skaitli no 0  - 4 (ieskaitot)"))
n = 0


name = vardu_saraksts[num]
hidden_word = []
for i in name:
    hidden_word.append("_ ")

true = True
while true:
    guess = input("Sāc minēt! ")
    for i in name:
        for j in list:
            if guess[0] == list[j]:
                hidden_word[i] = list[j]
    


# vards = input("Uzraksti vārdu: ")
# burts = input("ievadi burtu: ")
# redzets = 0
# for i in vards:
#     if i == burts:
#         redzets +=1
# print(redzets)

