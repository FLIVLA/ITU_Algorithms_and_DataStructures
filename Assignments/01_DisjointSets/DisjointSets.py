#============================================================================#
#-------------  Algorithms and Data Structures - Assignment 01 --------------#
#                      Frederik Lind - flin@itu.dk - 20921                   #
#                                 05.02.2023                                 #
#============================================================================#

#Assignment 01 - Disjoint Sets

input = input()
n, m = input.split(" ")

# Create sets {0}, {1}, ..., {n-1}:
col = set()
for i in range(int(n)):
    col.add(frozenset([i]))

# Find the set that x belongs to
def find_set(x):
    for M in col:
        if x in M: return M
    assert False

# Operations m
for i in range(int(m)):
    op, s, t = input[i].split()
    S = find_set(int(s))
    T = find_set(int(t))
    
    if op == "0":
        if S == T: print("1")
        else: print("0")
    
    if op == "1":
        col.remove(S)
        col.remove(T)
        col.add(S.union(T))
    
    if op == "2":
        S.remove(s)
        T.union(s)
        