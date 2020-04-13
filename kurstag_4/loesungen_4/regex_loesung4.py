# Aufgaben 04
# Postleitzahlen in der Schweiz
# von 1000 bis 9999 mit einer Regex ausdrucken schreiben
# Vorgabe:
# plz = ["0900","1200","4000","9000", "75000", "A100"]

# Aufgabe 04 - Lösung
import re
plz = ["0900", "1200", "4000", "9000", "75000", "A100"]

for p in plz:
    match = re.search("[1-9][0-9]{3}", p)
    if match is not None:
        print(match.group())
