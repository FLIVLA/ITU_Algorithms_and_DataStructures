# KATTIS - #Alphabet Spam

# Prints ratios of whitespace (_), lowercase, uppercase and symbols (ASCII 33 -126)
# present in input string.

def is_symbol(s):
    ascii = ord(s)
    if ascii >= 33 & ascii <= 126:
        return True
    else: return False

#line = "Welcome_NWERC_participants!"
line = input()

w,l,u,s = 0,0,0,0
for i in range(0, len(line)):
    if line[i] == "_": w += 1
    elif line[i].islower(): l += 1
    elif line[i].isupper(): u += 1
    elif is_symbol(line[i]): s += 1
d = len(line)

print (w,l,u,s)
result = [w/d, l/d, u/d, s/d]
for num in result:
    print(num)