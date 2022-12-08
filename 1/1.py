def GetLines(FileName):
    with open(FileName) as f:
        return [l.strip() for l in list(f.readlines())]
        #return list(map(int, f.readlines()))

def doit(fname):
    lines = GetLines(fname)
    current = 0
    max = 0
    for line in lines:
        if line == '':
            if current > max:
                max = current
            current = 0
            continue
        current += int(line)
    return max

def doit2(fname):
    lines = GetLines(fname)
    current = 0
    max = [0,0,0]
    for line in lines:
        if line == '':
            for i, n in enumerate(max):
                if current > n:
                    max[i] = current
                    break
            current = 0
            continue
        current += int(line)
    return max

print(doit('input.txt'))
print(sum(doit2('input.txt')))
