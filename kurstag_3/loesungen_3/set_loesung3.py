"""
Set Aufgabe 03

Entferne aus einem Set
abc = {'A','B','C','D','E','F'}

in einem Statement folgende Elemente
{'D','E','F'}

sodass das abc nur noch: {'A','B','C'} enthält

Tipp: difference_update() ist ein Funktion von Set --> Google ?
"""

# Set Aufgabe Lösung 03
abc = {'A','B','C','D','E','F'}
abc.difference_update({'D','E','F'})

print(abc)
