def postalValidate(S):
    S = S.replace(chr(32), '')
    if len(S) != 6:
        return False
    if not S[0].isalpha() or not S[2].isalpha() or not S[4].isalpha():
        return False
    if not S[1].isdigit() or not S[3].isdigit() or not S[5].isdigit():
        return False
    return S.upper()
