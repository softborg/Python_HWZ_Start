# Sets sind unsortiert und OHNE index, keine Duplikate erlaubt !
# Sets werden mit geschweiften Klammern angelegt {} 
kantone = {'AG', 'AG'}

# AG wurde nur 1 aufgenommen !
print("1:", kantone)

# Einzelene Elemente anhängen
kantone.add('BE')
kantone.add('BS')
kantone.add('BL')
kantone.add('TI')

# loop über set
for k in kantone:
    print("Der Kanton {}.".format(k))

# Mehrere Elemente gleichzeitig anhängen
kantone.update('GL', 'GE', 'LU', 'FR')
print("2:", kantone)


# leeres set anlegen
leeres_set = set()

# Anzahl Elemente im Set vorhanden - mit len-buitin
print("3. Anzahl: ", len(leeres_set))

