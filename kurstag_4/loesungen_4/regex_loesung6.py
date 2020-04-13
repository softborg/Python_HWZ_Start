# Aufgabe 06 - Aufgabe
# Bei Datumsangaben gibt Jahreszahlen mit Monatsangabe und Jahreszahlen ohne
# Montasangabe, beide Varianten sind gültig, wie lautet die Regex
# gültig: Jul. 2019 oder 2019
# gültig: Apr. 1990 oder 1990
# gültig: Okt. 1989 oder 1989
# daten = ["Jul. 2019", "1990", "Okt. 1989", "September 2018", "Nov. 2009"]

# Aufgabe 06 - Lösung
import re

daten = ["Jul. 2019", "1990", "Okt. 1989", "September 2018", "Nov. 2009"]

for d in daten:
    match = re.search(r"(([A-Z][a-z][a-z]\.\s)?([1-9]\d{3}))", d)
    if match is not None:
        print(match)