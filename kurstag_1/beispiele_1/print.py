# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
#          |        |          |              |              |
#        Werte   Trennzeichen  Satzzeichen   Ausgabeort,  Ausgabe
# Wert(e) - 1 - n Werte
# Trennzeichen, z.B: Komma, Semicolon, Leerzeichen, Pipezeichen, beliebig, sep=',' - optionale Angabe
# Satzzeichen: '\n' = am Ende eine neue Zeile, '\t' = Tabulatoren
# Ausgabeort = 'sys.stdout' --> Konsole, 'sys.stderr' --> Error Konsole

# import Zeile um auf den sys.stderr zu schreiben
import sys

# print mit anschliessender neuer Zeile
print("Hallo")

print("Max", "Muster", sep='&')

# print alle Werte werden auf einer Zeile geschrieben mit Tabulator dazwischen.
print("Max", "Muster", end='\t')
print("7000", "Chur")

# print Fehler
print("Ein Fehler wurde gefunden", file=sys.stderr)
