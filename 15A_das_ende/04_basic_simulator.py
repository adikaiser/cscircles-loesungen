def getBASIC():
    program = []
    line = input()
    while not line.endswith("END"):
        program.append(line)
        line = input()
    program.append(line)
    return program

def findLine(prog, target):
    for i in range(len(prog)):
        if prog[i].startswith(target): return i

def execute(prog):
    visited = [False]*len(prog)
    location = 0
    while True:
        if location == len(prog)-1: return "success"
        if visited[location]: return "infinite loop"
        visited[location] = True
        T = prog[location].split()[2]
        location = findLine(prog, T)

print(execute(getBASIC()))