# Ein Tuple ist eine geordnete und uverändenderliche Sammlung
# Tuple Start mit '(' und Ende mit ')'

mein_tuple = ('Zug', 'Bern', 'Chur', 'Glarus', 'Liestal', 'Lausanne', 'Bern')
print("mein_tuple", mein_tuple)

# Ein Element ansprechen
print(mein_tuple[2])

# Teile der Elemente des Tuples ansprechen ab Start 1, dann 2, dann 3, 4 ist exlusive (dieser Index wird NICHT genutzt)
print(mein_tuple[1:4])

# Löschen des Tupel mit del-Builtin function
# del(mein_tuple[0]) # ---> führt zu Fehler

# Wie oft ist etwas vorhanden mit count(variable) - Achtung case-sensitive
print(mein_tuple.count('Bern'))

# Anwelcher Stelle ist das Elemente im Tupel - 1.Eintrag
print(mein_tuple.index('Bern'))

# Tupel via einer Liste ändern
meine_liste = list(mein_tuple)
meine_liste[0] = 'Stans'
mein_tuple = tuple(meine_liste)
print(mein_tuple)
