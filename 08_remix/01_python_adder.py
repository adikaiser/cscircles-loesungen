S = input()
for position in range(0, len(S)):
   if S[position] == '+':  # Zahlen zwischen '+' trennen
      str1 = int(S[0:position])  # str1 in Integer umwandeln
      str2 = int(S[(position+1):len(S)])  # str2 in Integer umwandeln
      print(str1 + str2)