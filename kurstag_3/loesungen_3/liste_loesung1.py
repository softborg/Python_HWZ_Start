"""
liste Aufgabe 01
Durchsuchen sie eine Kantonsliste nach einem bestimmten Kanton, sobald sie fündig
geworden sind, geben sie den Index der Fundstelle aus. Wird nichts gefunden, dann
soll - 1 als Index angezeigt werden.

Vorgabe:
kanton_liste = ['Basel-Stadt', 'Bern', 'Genf', 'Glarus', 'Thurgau', 'Aargau', 'Zürich']
kanton = Thurgau (dieser Kanton soll gesucht werden)
"""

# liste Aufgabe 01 - Lösung

kanton_liste = ['Basel-Stadt', 'Bern', 'Genf', 'Glarus', 'Thurgau', 'Aargau', 'Zürich']
kanton = 'Thurgau'

found = -1
i = 0
while i < len(kanton_liste):
    if kanton_liste[i] == kanton:
        found = i
        break
    i += 1
# Ausgabe
print("Kanton gefunden an Index: ", found)
