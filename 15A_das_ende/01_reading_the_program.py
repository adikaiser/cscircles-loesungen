def getBASIC():
    program = []
    line = input()
    while not line.endswith("END"):
        program.append(line)
        line = input()
    program.append(line)
    return program