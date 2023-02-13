poem = []
mostOccurrences = 0
line = input().lower().split()
while line[0]!="###":
    for word in line:
        poem.append(word)
    line = input().lower().split()
for wordIndex in range(len(poem)):
    occurrences = poem.count(poem[wordIndex])
    if occurrences > mostOccurrences:
        mostCommonWord = poem[wordIndex]
        mostOccurrences = occurrences
print(mostCommonWord)