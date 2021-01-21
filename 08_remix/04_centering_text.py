width = int(input())  
while True:
    a = input()  # Wort, welches zentriert werden muss
    L = len(a)  # Länge des Wortes
    b = (width-L) // 2  # Berechnung, wieviele Punkte auf beiden Seiten des Wortes benötigt werden
    c = b  # Variable für die rechte Seite
    
    if ((width-L) % 2) != 0:  # Wenn die Anzahl Punkte auf beiden Seite nicht gleich ist...
        b = b + 1  # wird auf der linken Seite ein Punkt zusätzlich eingefügt
    if a == 'END':  
        break
        
    print('.' * b + a + '.' * c)