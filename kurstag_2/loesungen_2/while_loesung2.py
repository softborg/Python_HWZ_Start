"""
while Aufgabe 02
Es sollen mittels einer Randomfunktion die Anzahl Versuche
von 1 bis 10 bestimmt werden.
[code]
import random

versuche = random.randint(1,10) # --> "würfelt zwischen 1 und 10
[/code]

In der While Schlaufe werden nun jedes Mal eine Zahl zwischen 1 und 100
gewürfelt und diese Zahl zum Totol addiert.
Zum Schluss werden die Werte ausgegeben:

Die Ausgabe sieht folgendermassen aus:
Anzahl Versuche: xx
Total: xxxx Druchschnitt:  xx.xx

"""

# while Aufgabe 02 - Loesung
import random

versuche = random.randint(1, 10)
zahl = 0
total = 0
while zahl < versuche:
    total += random.randint(1, 100)
    zahl += 1
print("Anzahl Versuche:", versuche)
print("Total:", total, "Druchschnitt: ", total / versuche)
