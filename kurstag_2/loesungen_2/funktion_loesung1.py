"""
Funktion Aufgabe 01

Mittels einer Funktion Grad Celsius in Fahrenheit umrechnen
Formel: Fahrenheit = Celisus * 9/5 + 32.0
Die Funktion gibt zurück: "Celsius xx beträgt in Fahrenheit xx."
Auf 2 Kommastellen gerundet bei Fahrenheit
"""


def c_to_f(celsius):
    text = "Celsius {0} beträgt in Fahrenheit {1:.2f}".format(celsius, (celsius * (9 / 5) + 32))
    return text


print(c_to_f(22))
