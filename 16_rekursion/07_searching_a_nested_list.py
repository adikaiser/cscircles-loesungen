def nestedListContains(NL, target):
    if isinstance(NL, int):
         return NL == target
    else:
        for element in NL:
            if nestedListContains(element, target):
                return True
        return False