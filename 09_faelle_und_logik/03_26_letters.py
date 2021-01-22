letter = input()
if int(ord(letter) >= ord('A')) and int(ord(letter) <= ord('Z')):
    print((ord(letter)-65)+1)
else:
    print("invalid")