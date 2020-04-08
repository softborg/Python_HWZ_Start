import re

pattern = '\\AZ\\w*h$'
test_string = 'Zürich'
result = re.match(pattern, test_string)

if result:
    print("Suche erfolgreich.", result)
else:
    print("Nichts gefunden.", result)

# .       - jedes Zeichen ausser New Line (\n)
# \d      - Zahlen (0-9)
# \D      - KEINE Zahlen (0-9)
# \w      - Buchstaben, Zahlen oder Zeichen (a-z, A-Z, 0-9, _)
# \W      - Buchstaben, Zahlen oder Zeichen
# \s      - Leerezeichen (Leerschlag, Tabulator, New Line (\n))
# \S      - KEIN Leerezeichen (Leerschlag, Tabulator, New Line (\n))
#
# \b      - Wortgrenze
# \B      - KEINE Wordgrenze
# ^       - Start eines String
# $       - Ende eines Stringes
#
# []      - gefundene Zeichen in der eckigen Klammer
# [^ ]    - NICHT gefundene Zeichen in der eckigen Klammer
# |       - Oder Zeichen
# ( )     - Gruppe
#
# Mengenangabe:
# *       - 0 und mehr
# +       - 1 und mehr
# ?       - 0 or 1
# {3}     - genau Anzahl
# {3,4}   - WerteAnzahl (kleinste Anzahl, maximale Anzahl)
#

# Beispiel Regex
# [a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+

# test_string = '''
#                 Apfel
#                 Affe
#                 Zuckerguss
#                 ampel'''
# pattern = re.compile('[Aa]\\w+l')
#
# matches = pattern.finditer(test_string)
# for match in matches:
#     print(match)

test_string = '''Guten Tag. Thema von heute ist Regex. Viel Erfolg.'''

pattern = re.compile('\\w*\\.')

matches = pattern.finditer(test_string)
for match in matches:
    print(match)
