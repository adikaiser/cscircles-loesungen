def countdownBy2(n):
    if n < 1:
        print('Blastoff!')
    else:
        print(n)
        countdownBy2(n - 2)