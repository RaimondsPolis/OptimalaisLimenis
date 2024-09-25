import random

# a= random.randint(1,10)
# b = int(input("uzmini  skaitli 1 - 10: "))
# true = True
# while true:
#     if b == a:
#         true = False
#         print("Tu Uzminēji!")
#     if b < a:
#         b = int(input("vairāk "))
#     if b > a:
#         b = int(input("mazāk "))


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

uzminiskaitli()