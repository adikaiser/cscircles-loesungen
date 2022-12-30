def countup(n):
    if n == 0:
        print('Blastoff!')
    else:
        countup(n - 1)
        print(n)