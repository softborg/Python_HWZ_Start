# index beginnt bei 0 ={0} ist ein Platzhalter und wird mit dem 1. Parameter ersetzt und so weiter..
print('Ich heisse {0} {1}'.format('Max', 'Muster'))
# Output: Ich heisse Max Muster

# die Verwendung der Platzhalter ist beliebig auch die Reihenfolge, Entscheidend ist die Reihenfolger der Werte
print('Ich heisse {1} and {0}'.format('Max', 'Muster'))
# Output: Ich heisse Muster Max

# benannte Platzhalter {name des Platzhalters}, bei den Werten wird der Wert dem Platzhalter zugewiesen
print('Guten Tag {name}, {greeting}'.format(greeting='Guten Tag', name='Stefan'))
#  Guten Tag, Stefan
