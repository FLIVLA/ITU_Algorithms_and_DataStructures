import sys
import statistics

input = sys.stdin

nt = input[0].split(" ")
a = input[1].split(" ")
n = nt[0]
t = nt[1]

if int(t) == 1:
    for i in a:
        print(7)
        
elif int(t) == 2:
    if (int(a[0]) > int(a[1])): print("Bigger")
    elif (int(a[0]) == int(a[1])): print("Equal")
    else: print("Smaller")
    
elif int(t) == 3:
    print(statistics.median([int(a[0]),int(a[1]),int(a[2])]))

elif int(t) == 4:
    sum = 0
    for i in a:
        sum += int(i)
    print(sum)

elif int(t) == 5:
    evnNum = []
    for i in a:
        if int(i) % 2 == 0:
            evnNum.append(int(i))
    print(sum(evnNum))
    
elif int(t) == 7:
    i = 0
    for i in a: