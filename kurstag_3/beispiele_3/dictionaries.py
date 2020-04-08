# Dictionary - Sammlung von Key / Value (Schlüssel / Wert) Pärchen innerhalb geschweiften Klammern

# leeres Dictionary
mein_dict = {}  # ACHTUNG nicht verwechseln mit set()

# Dictionry mit Werten gefüllt
kantone = {'BS': 'Basel Stadt'}
print(kantone)

# Element hinzufügen
kantone['SH'] = 'Schaffhausen'
print(kantone)

# Element update
kantone['GL'] = 'Genf' # Fehler GL ist Glarus
print("Kantone mit Fehler: ", kantone)
kantone['GL'] = 'Glaurs' # Korrektur
print(kantone)

# Element löschen
kantone['LI'] = 'Liechtenstein' # Fehler dieser Kanton gehört nicht zur Schweiz
print(kantone)
kantone.pop('LI')
print(kantone) # so, jetzt stimmts wieder

# Loop über alle Pärchen
for kanton in kantone.items():
    print(kanton)


# alle Keys lesen
for key in kantone.keys():
    print(key)

# alle Werte lesen
for val in kantone.values():
    print(val)
