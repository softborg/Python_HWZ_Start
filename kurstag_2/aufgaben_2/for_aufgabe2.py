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
