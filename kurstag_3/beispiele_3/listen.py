# Listen - sind Sammlungen von Elementen (dürfen unterschiedliche Datentypen sein)
# [] mit der öffnenden eckigen Klammer beginnt, mit einer schliessenden eckigen Klammer wird die Liste abgeschlossen

# Leere Liste anlegen
leere_liste = []
print(type(leere_liste))

# Element einer Liste hinzufügen
leere_liste.append('Hallo')
print(leere_liste)

# noch 2 Elemente hinzfügen
leere_liste.append('Max')
leere_liste.append(42)

print(leere_liste)

# Zugriff aus einzelnes Element: 1.Element wird mit index 0 angesprochen

print("Der 1.Element =", leere_liste[0])

# len - builtin --> Wieviele Elemente hat die Liste
print("Anzahle Elemente =", len(leere_liste))

# löschen eines Elementes
del (leere_liste[0])
print(leere_liste)

# Python List Methods
# append() - hinzufügen eines Element am Ende der Liste
# extend() - eine Liste an das Ende einer Liste hinzufügen
# insert() - in der Liste ein Element einfügen, der Rest "rutscht" um 1 Platz
# remove() - ein Element einer Liste löschen
# pop() - Element aus der Liste löschen und gibt diese Element als Rückgabewert zurück
# clear() - alle Element werden entfernt
# index() - gibt das erste zutreffende Element - Index zurück
# count() - Returns the count of number of items passed as an argument
# sort() - Sort die Liste absteigend
# reverse() - dreht die Liste von hinten nach vorn um
# copy() - erstellt eine Kopie einer Liste

# slicing - Liste zuschneiden

zahlen = [0,  1,  2,  3,  4,  5,  6,  7,  8,  9]
# index   0,  1,  2,  3,  4,  5,  6,  7,  8,  9
#        -10,-9, -8, -7, -6, -5, -4, -3, -2, -1

# liste[start:ende:schritt]

print(zahlen)  # alle Elemente
print(zahlen[-10])  # entspricht zahlen[0]
print(zahlen[0:6])  # alle Elemente von index 0 bis exklusive 6 (also 5)
print(zahlen[3:])  # alle Elemente von index 3 bis Ende
print(zahlen[:6:2]) # alle Elemente von 0 bis 6(exlusive) in 2er Schritten
print(zahlen[-7:-3]) # alle Elemente von -7 bis -3(exlusive)
print(zahlen[3:-1]) # alle Elemente von 3 bis -1(exlusive)
print(zahlen[::2]) # alle Elemente von Start bis Ende in 2er Schritten
