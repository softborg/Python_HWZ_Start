# Aufgabe 01
# Schreibe eine Regex, die auf alle Elemente zutrifft
# Vorgabe:
# texte = ["abababa","aaba", "aabbaa", "aba", "aabababa"]

# Aufgabe 01 - Lösung
import re
texte = ["abababa", "aaba", "aabbaa", "aba", "aabababa"]

for t in texte:
    match = re.match("a(ab)*a?", t)
    print(t, ":", match)
