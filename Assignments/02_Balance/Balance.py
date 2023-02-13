#============================================================================#
#-------------  Algorithms and Data Structures - Assignment 02 --------------#
#                      Frederik Lind - flin@itu.dk - 20921                   #
#                                 13.02.2023                                 #
#============================================================================#

# Assignment 02 - Balance

import sys

symbols = input()

#in1 = "([(())])[]"
#in2 = ")("
#in3 = "[)"
#in4 = "(("
#in5 = "[(])"
#in6 = "[])[])"
#in7 = "("

def b(s):
    symbols = []
    for c in s:
        if c in ['(', '[']:
            symbols.append(c)
        elif c in [')', ']']:
            if not symbols:
                return "0"
            if (c == ')' and symbols[-1] == '(') or (c == ']' and symbols[-1] == '['):
                symbols.pop()
            else:
                return "0"
    return "1" if not symbols else "0"

print(b(symbols))