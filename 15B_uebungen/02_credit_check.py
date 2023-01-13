def check(S):
    checksum = 0
    if len(S) != 19:
        return False
    for i in range(len(S)):
        if (i+1)%5!=0 and S[i].isdigit():
            checksum += int(S[i])
        elif not S[i]==" ": return False
    return checksum%10==0