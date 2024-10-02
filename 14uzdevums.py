# izvadīt lielāko no 3 skaitļiem

a = int(input("Ievadi 1. skaitli: "))
b = int(input("Ievadi 2. skaitli: "))
c = int(input("Ievadi 3. skaitli: "))

if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
elif c>b and c>a:
    print(c)
else: print("wdf")