# Extrahieren sie alle Namen und Alter aus dem Text, speichern und geben es als Dictonary aus.
# Nutzen sie dazu Regex und Dictonary

import re

text = '''Max ist 42, seine Petra ist 40, Peter ist 12, bzw. Maria ist 10. '''

names = re.findall(r'[A-Z][a-z]*', text)
alter = re.findall(r'\d{1,2}', text)

# print(names)
# print(alter)

tabelle = {}
x = 0
for name in names:
    tabelle[name] = alter[x]
    x += 1
print(tabelle)
