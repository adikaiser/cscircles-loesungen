S = input()
for position in range(0, len(S)):
   if S[position] == '+':  # Zahlen zwischen '+' trennen
      str1 = int(S[0:position])  # entspricht Substring vor + Symbol
      str2 = int(S[(position+1):len(S)])  # entspricht Substring nach + Symbol
      print(str1 + str2)