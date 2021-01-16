# Ziel: gib die Zahl der Sekunden in einer Woche an
SekundenProMinute = 60
SekundenProStunde = SekundenProMinute * 60 # todo: überprüfe dies!
SekundenProTag = SekundenProStunde * 24
TageProWoche = 5
TageProWoche = TageProWoche + 2 # Sind die Wochenenden deaktiviert?
print(SekundenProTag * TageProWoche)