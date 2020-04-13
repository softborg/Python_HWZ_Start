"""
for Aufgabe 02

Die Prüfziffer der GTIN (ehem. EAN) ist die letzte Ziffer - 13. Stelle, gelesen werden
die Zahlen rechts - nach links !

1. Die ungeraden Zahlen werden x 3 multipliziert
2. Die geraden Zahlen werden x 1 multipliziert
3. Alle Ergebnisse werden zum Total summiert.
4. Prüfzahl = das nächste höhere Vielfache von 10 ab dem Totol - Total --> ergibt die Prüfzahl
   90 (nächstes höheres 10 Vielfache) - 89 = 90 - 89 = 1 --> Prüfzahl
   63 (nächstes höheres 10 Vielfache) - 63 = 70 - 63 = 7 --> Prüfzahl
Beispiel: Zahlen

EAN1 = '544900009624-1' mit Prüfzahl
EAN2 = '544900009624' ohne Prüfzahl


"""
# for Aufgabe 02 - Lösung

EAN1 = '544900009624-1'
EAN2 = '544900009624'

summe = 0
for i in range(len(EAN2) - 1, -1, -1):
    if i % 2 == 0:
        summe += int(EAN2[i]) * 1
    else:
        summe += int(EAN2[i]) * 3

pruefziffer = (10 - summe % 10) % 10
print("Prüfziffer:", pruefziffer)
print("EAN1 = EAN2", EAN1 == str(EAN2)+"-"+str(pruefziffer), str(EAN2)+"-"+str(pruefziffer) )
