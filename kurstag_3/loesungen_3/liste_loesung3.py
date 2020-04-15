"""
Liste Aufgabe 03

zahlen = [54, 44, 57, 88, 66, 33]
1. Entfernen sie Element mit index -3
2. Fügen sie das entfernte Element an index 1 wieder ein
3. das entfernte Element bitte am Schluss Anhängen

--> Ihre Ausgabe sollte so aussehen:
[54, 44, 88, 57, 66, 33, 88]

"""

# Liste Aufgabe 03 - Lösung

zahlen = [54, 44, 57, 88, 66, 33]
element = zahlen.pop(-3)
zahlen.insert(2,element)
zahlen.append(element)
print(zahlen)
