def hailstone(n):
    print(n)
    if n % 2 == 0:
         hailstone(n//2)
    elif n != 1:
         hailstone(3 * n + 1)