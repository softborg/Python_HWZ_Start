"""
# for Aufgabe 01

Erstellen sie folgenden Output.
Natürlich nicht zeicnen :-)
-------------------------
| Zahl | Quadrat| Potenz|
-------------------------
|    1 |      1 |     2 |
|    2 |      4 |     4 |
|    3 |      9 |     8 |
|    4 |     16 |    16 |
|    5 |     25 |    32 |
|    6 |     36 |    64 |
|    7 |     49 |   128 |
|    8 |     64 |   256 |
|    9 |     81 |   512 |
|   10 |    100 |  1024 |
-------------------------
"""
# for Aufgabe 01 - Loesung

formatString = "| {zahl:4d} | {quadrat:6d} | {potenz:5d} |"

print("-"*25)
print("| Zahl | Quadrat| Potenz|")
print("-"*25)
for i in range(1,11):
    print(formatString.format(zahl=i, quadrat=i*i, potenz=2**i))
print("-"*25)