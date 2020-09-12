# coding=utf8

# Aufgabe 1 - Kreditkarte
# 1. erstellen sie folgende Klassen 'Kreditkarte', 'Visa' und 'Mastercard
# 2. beim Instanziieren soll die Kartennummer mitgegeben werden, die Kartennummer ist public
# 3. Die Klassen 'Visa' und 'Mastercard' erben von 'Kreditkarte' und haben keine eigene Implementation (pass)
# 4. Instanziieren sie jeweils eine Visa- und ein Mastercard
# 5. Geben sie jeweils die Kartennummer aus


class Kreditkarte:
    def __init__(self, kartennr):
        self.kartennr = kartennr


class Visa(Kreditkarte):
    pass


class Mastercard(Kreditkarte):
    pass


visa = Visa("412340998")
print(visa.kartennr)

mastercard = Mastercard("77770999")
print(mastercard.kartennr)
