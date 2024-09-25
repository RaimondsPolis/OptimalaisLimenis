alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
list = []
for i in alphabet:
    list.append(i)

for a in alphabet:
    for b in alphabet:
        print(f"{a}{b}")