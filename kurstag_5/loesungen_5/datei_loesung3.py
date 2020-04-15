"""
Datei Aufgabe 03

Öffnen sie die Datei 'hauptstadt.txt
Lesen alle Werte aus, Achtung \n je Zeile nicht mitlesen !!
Schreiben alle Werte in eine Liste und sortieren diese Alphabetisch
und geben diese auf der Kosonle aus.
Anschliessend schliessen sie die Datei
"""

# Datei Aufgabe 03 - Lösung

orte = []
with open('hauptstadt.txt', "r") as f:
    
    orte = f.read().splitlines()

if not f.closed:
    print('File is not closed')
else:
    print('File is closed')
print(orte)