"""
while Aufgabe 03
Jeder Buchstabe im Wort: Dampfschiffraddampfer soll nach Vokal bzw. Konsonant
untersucht werden. Geben sie jeweils den Buchstaben aus und schreiben, ob es
Konsonant oder ein Vokal ist.

text = "Dampfschiffraddampfer"
 Tipp 1. mit len() --> wird die Länge des Wortes ermittelt.
 Tipp 2. mit text[0]= wird das 'D' im Wortangesprochen
"""

# Lösung while Aufgabe
text = "Dampfschiffraddampfer"

i = 0
while i < len(text):

    if text[i] == 'a' or text[i] == 'i' or text[i] == 'e' or text[i] == 'o' or text[i] == 'u':
        print("Vokal gefunden im Wort", text[i])
    else:
        print("Konsonant gefunden im Wort", text[i])
    i += 1