def digitalRoot(n):
    if digitalSum(n) < 10:
        return digitalSum(n)
    else:
        return digitalRoot(digitalSum(n))