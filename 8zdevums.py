vards = input("Uzraksti vārdu: ")
burts = input("ievadi burtu: ")
redzets = 0
for i in vards:
    if i == burts:
        redzets +=1
print(redzets)