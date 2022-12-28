import re
import math

def GetLines(FileName):
    with open(FileName) as f:
        return [l for l in list(f.readlines()) if l.strip() != '']

def parseit(lines):
    stacklines = []
    stacks = []
    stackline = ''
    instructions = []
    for line in lines:
        if re.match(r'.*\d', line):
            stackline = line
            break
        stacklines.append(line)
    for i, n in enumerate(stackline):
        if not re.match(r'\d', n):
            continue
        num = int(n)-1
        stack = []
        for line in stacklines:
            ch = line[i]
            if re.match(r'[A-Z]', ch):
                stack.append(ch)
        stacks.append(stack)
    for line in lines:
        s = re.search(r'move (\d+) from (\d) to (\d)', line.strip())
        if not s: continue
        g = s.groups()
        instructions.append((int(g[0]), int(g[1])-1, int(g[2])-1))
    return stacks, instructions

def doit(fname):
    stacks, instructions = parseit(GetLines(fname))
    for (qty, fr, to) in instructions:
        for _ in range(qty):
            stacks[to].insert(0,stacks[fr].pop(0))
    return ''.join([ s[0] for s in stacks])

def doit2(fname):
    stacks, instructions = parseit(GetLines(fname))
    for (qty, fr, to) in instructions:
        stacks[to] = stacks[fr][0:qty] + stacks[to]
        stacks[fr] = stacks[fr][qty:]
    return ''.join([ s[0] for s in stacks])

print(doit('input.txt'))
print(doit2('input.txt'))
