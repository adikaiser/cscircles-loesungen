n = int(input())

for outer in range(1 , (n + 1)):
    # print("Aktueller Wert von outer: " + str(outer))
    for inner in range(1, (n+1)):
        # print("Aktueller Wert von inner: " + str(inner))
        if outer * inner == n:
            print(str(outer)+" times "+str(inner)+" equals "+str(n))