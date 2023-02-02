import sys

a = ["5 8"]
for i in a:
    inp = i.split(" ")
    x = int(inp[0])
    y = int(inp[1])
    if (x >= y):
        print(x-y)
    else: print(y-x)
    