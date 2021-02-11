# Dezimalwert des Space-Zeichen wird in der Variable x gespeichert.
# Die Variable x dient als unserer Zählvariable.
x = ord(' ') 

# Mit jeder Iteration der äusseren For-Schleife werden je eine Zeile für die 
# ASCII-Zeichen und eine Zeile für Dezimalwerte der ASCII-Zeichen erzeugt. 
for i in range(0,6): 
    print('chr:'+' ', end=' ')
    # Mit der ersten, inneren For-Schleife werden pro Zeile 16 ASCII-Zeichen erzeugt. 
    for j in range(x,x+16):
        print(chr(j)+'  ', end=' ')
    print()   
    print('asc:', end=' ')
    # Mit der zweiten, inneren For-Schleife werden pro Zeile die 16 dazugehörigen ASCII-Dezimalwerte erzeugt. 
    for u in range(x,x+16):
        if u >= 100:
            print(str(u), end=' ')
        else:
            print(str(u)+' ', end=' ')
    print()
    # Die Zählvariable wird nach dem Durchlaufen der äusseren For-Schleife um 16 erhöht. 
    x += 16

