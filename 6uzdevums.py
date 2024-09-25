def aaa():
    print("sssss")

true = True
while true:
    true = False
    a = input("vai vēlies programmu atkārtot? y/n vai 1/0: ")
    if a == "y":
        true = True
        aaa()
    elif a =="1":
        true = True
        aaa()
    elif a == "Y":
        true = True
        aaa()