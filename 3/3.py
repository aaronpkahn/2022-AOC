import re
import math

def GetLines(FileName):
    with open(FileName) as f:
        return [l.strip() for l in list(f.readlines()) if l.strip() != '']

def doit(fname):
    total = 0
    for line in GetLines(fname):
        half = math.floor(len(line)/2)
        first = set(line[0:half])
        for item in line[half:]:
            if item in first:
                val = ord(item)
                total += val - (96 if val > 96 else 38)
                break
    return total

def doit2(fname):
    total = 0
    intersection = set()
    for i, line in enumerate(GetLines(fname)):
        lineset = set(line)
        if i % 3 == 0:
            intersection = lineset
            continue
        intersection = lineset & intersection
        if i % 3 == 2:
            letter = intersection.pop()
            val = ord(letter)
            total += val - (96 if val > 96 else 38)
    return total

print(doit('input.txt'))
print(doit2('input.txt'))
