O = input()
T = float(O[:-1])
if O[-1]=="C":
    print(str(T*9/5+32)+"F")
else:
    print(str((T-32)*5/9)+"C")