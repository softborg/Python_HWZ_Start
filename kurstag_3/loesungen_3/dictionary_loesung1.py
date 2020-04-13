"""
dictionary Aufgabe 01

1.Erstellen / Initialisieren sie ein Dictionary mit den Wertepaaren

Italien: Rom
Frankreich: Paris

2. erstellen ein 2tes Dictionary und hängen es dem 1.Dictionary an
Schweden: Stockholm
Norwegen: Oslo
Russland: Moskau
Australien: Syndey

3. Ergänzen sie folgende Wertepaare
Deutschland: Berlin
Schweiz: Bern
Spanien: Madrid

4. Korrigieren sie den Australien - Eintrag: Canberra (ist die Hauptstadt) bitte vorher prüfen
ob Australien überhaupt im Dictionary existiert.
"""

# Dictionary Aufgabe 01 - Lösung

hauptstaedte = {"Italien": "Rom", "Frankreich": "Paris"}

for hauptstadt in hauptstaedte.items():
    print(hauptstadt)

print("*" * 32)
hauptstaedte_2 = {"Schweden": "Stockholm", "Norwegen": "Oslo", "Russland": "Moskau", "Australien": "Sydney"}

hauptstaedte.update(hauptstaedte_2)

for hauptstadt in hauptstaedte.items():
    print(hauptstadt)

print("*" * 32)

hauptstaedte["Deutschland"] = "Berlin"
hauptstaedte["Schweiz"] = "Bern"
hauptstaedte["Spanien"] = "Madrid"

for hauptstadt in hauptstaedte.items():
    print(hauptstadt)
print("*" * 32)

if "Australien" in hauptstaedte:
    hauptstaedte['Australien'] = "Canberra"

for hauptstadt in hauptstaedte.items():
    print(hauptstadt)
print("*" * 32)
