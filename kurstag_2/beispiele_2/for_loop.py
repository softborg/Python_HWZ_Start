# for range - "Zählschlaufe
# eine bestimmte Anzahl Iterationen von - bis - IntervalSchritte
start = 1
end = 10  # exklusiv dieser Wert
step = 1

for i in range(start, end, step):
    print("Der Wert von i ist {}".format(i))

print('-' * 32)

for i in range(10, -1, -1):
    print("Der Countdown ist {}.".format(i))

print('-' * 32)


# for Schleife geeignet um Werte aus einer Liste (dazu später mehr) auszulesen
# Liste aller Werte
noten = [6, 5, 3.5, 5.75, 4, 6, 5, 4.5, 4.25]

# Alle Noten totalisieren
total = 0

# jeder werte aus der Liste auslesen for wert in Liste :
for wert in noten:
    total += wert

# Ausgabe: Notendurchschnitt, mit len() builten Funktion erhält man z.B. die Anzahl Elemente in einer Liste
print("Der Notendurchschnitt ist {0:.4f} ".format(total / len(noten)))
