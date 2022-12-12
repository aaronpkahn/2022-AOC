import re
import math

def GetLines(FileName):
    with open(FileName) as f:
        return [[int(n) for n in re.search(r'(\d+)-(\d+),(\d+)-(\d+)', l.strip()).groups()] for l in list(f.readlines()) if l.strip() != '']

def doit(fname):
    total = 0
    for i, (a,b, x,y) in enumerate(GetLines(fname)):
        if (a <= x and b >= y) or (x <= a and y >= b): total += 1
    return total

def doit2(fname):
    total = 0
    for i, (a,b, x,y) in enumerate(GetLines(fname)):
        if (a <= x and b >= x) or (a <= y and b >= y) or (x <= a and y >= a) or (x <= b and y >= b): total += 1
    return total

print(doit('input.txt'))
print(doit2('input.txt'))
