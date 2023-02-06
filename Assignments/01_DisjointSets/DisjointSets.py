#============================================================================#
#-------------  Algorithms and Data Structures - Assignment 01 --------------#
#                      Frederik Lind - flin@itu.dk - 20921                   #
#                                 05.02.2023                                 #
#============================================================================#

# Assignment 01 - Disjoint Sets
#-- !'Move' Function not working as expected!

import sys

nums = sys.stdin.readlines()

n, m = nums[0].split(" ")
n = int(n)
m = int(m)

data = [i for i in range(n)]

def find(x):
    if data[x] != x:
        data[x] = find(data[data[x]])
    return data[x]

def move(s, t):
    S = find(s)
    T = find(t)
    if S != T:
        data[S] = T
       
for i in range(m):
    op, s, t = nums[i+1].split(" ")
    s, t = int(s), int(t)
    S, T = find(int(s)), find(int(t))
    
    if op == '2':
        move(s, t)
        
    if op == '0':
        print("1" if S==T else "0")
    
    if op == '1':
        data[S] = T