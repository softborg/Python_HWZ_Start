# coding=utf8

# Aufgabe 1 - Kreditkarte
# 1. erstellen sie folgende Klassen 'Kreditkarte', 'Visa' und 'Mastercard
# 2. beim Instanziieren soll die Kartennummer mitgegeben werden, die Kartennummer ist public
# 3. Die Klassen 'Visa' und 'Mastercard' erben von 'Kreditkarte' und haben keine eigene Implementation (pass)
# 4. Instanziieren sie jeweils eine Visa- und ein Mastercard
# 5. Geben sie jeweils die Kartennummer aus


class Kreis:
    pi = 3.1

    def __init__(self, radius):
        self.radius = radius

    @classmethod
    def change_pi(cls):
        cls.pi = 3.14


print(Kreis.pi)
Kreis.change_pi()
print(Kreis.pi)
