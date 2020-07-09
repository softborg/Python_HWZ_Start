# Extrahieren sie alle Namen und Alter aus dem Text, speichern und geben es als Dictonary aus.
# Nutzen sie dazu Regex und Dictonary

import re

text = '''Max ist 42, seine Petra ist 40, Peter ist 12, bzw. Maria ist 10. '''

# Regel 1: 1.Position muss ein Grossbuchstabe sein
# Regel 2: anschliessend dürfen beliebig viele Buchstaben folgen (0-n)
names = re.findall(r'[A-Z][a-z]*', text)

# Regel 1: finde alle Zahlen die 1 - oder 2stellig sind
alter = re.findall(r'\d{1,2}', text)

# print(names)
# print(alter)

tabelle = {}
x = 0
for name in names:
    tabelle[name] = alter[x]
    x += 1
print(tabelle)
