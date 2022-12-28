def execute(prog):
    visited = [False]*len(prog)
    location = 0
    while True:
        if location == len(prog)-1: return "success"
        if visited[location]: return "infinite loop"
        visited[location] = True
        T = prog[location].split()[2]
        location = findLine(prog, T)