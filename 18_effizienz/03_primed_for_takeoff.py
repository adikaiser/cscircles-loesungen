isPrime = [True] * 1000001
isPrime[0] = isPrime[1] = False
for i in range(2, int(1000000 ** 0.5) + 1):
    if isPrime[i]:
        for j in range(i * 2, 1000001, i):
            isPrime[j] = False