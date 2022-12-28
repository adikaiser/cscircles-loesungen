def findLine(prog, target):
    for i in range(len(prog)):
        if prog[i].startswith(target): return i