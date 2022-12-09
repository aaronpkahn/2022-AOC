import re

def GetLines(FileName):
    with open(FileName) as f:
        return [re.search(r'(\S)\s+(\S)', l).groups() for l in list(f.readlines()) if l.strip() != '']

def doit(fname):
    scores = [3,0,6]
    total = 0
    for (charo, charp) in GetLines(fname):
        o = ord(charo)-65
        p = ord(charp)-88
        total += p+1+scores[(o-p) % 3]
    return total

def doit2(fname):
    scores = [2,0,1]
    total = 0
    for (charo, charp) in GetLines(fname):
        o = ord(charo)-65
        p = ord(charp)-88
        val = ((o+scores[p])%3)+1+p*3
        total += val
    return total

print(doit('input.txt'))
print(doit2('input.txt'))