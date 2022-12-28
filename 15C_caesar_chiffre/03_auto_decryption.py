def shiftLetter(letter, shiftValue):
    if letter==" ":
        return(letter)
    shiftedLetter = chr(ord(letter)+shiftValue)
    if ord(shiftedLetter)>ord("Z"):
        shiftedLetter = chr(ord(shiftedLetter)-26)
    return shiftedLetter

def shift(string, shiftValue):
    shiftedString = ""
    for letter in string:
        shiftedString += shiftLetter(letter, shiftValue)
    return shiftedString

def getGoodness(string):
    currentStringGoodness = 0
    for letter in string:
        if not letter==" ":
            currentStringGoodness += letterGoodness[ord(letter)-ord("A")]
    return currentStringGoodness

def decrypt(string):
    stringGoodness = [0.0]*26
    for shiftValue in range(26):
        stringGoodness[shiftValue] = getGoodness(shift(string, shiftValue))
    return shift(string, stringGoodness.index(max(stringGoodness)))

string = input()
print(decrypt(string))