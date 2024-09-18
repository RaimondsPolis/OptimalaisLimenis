N = 0
i=0
while 1000>N:
    if N % 3 == 0 or N % 5 == 0:
        i = i + N
    N +=1
print(i)