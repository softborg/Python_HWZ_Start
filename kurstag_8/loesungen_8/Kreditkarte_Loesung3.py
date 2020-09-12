# coding=utf8

# Aufgabe 3 - Kreditkarte
# 1. erstellen sie folgende Klassen 'Kreditkarte', 'Visa' und 'Mastercard
# 2. beim Instanziieren soll die Kartennummer mitgegeben werden, die Kartennummer ist public
# 3. Die Klassen 'Visa' und 'Mastercard' erben von 'Kreditkarte' und haben jeweils einen eignen Initalisierung
# 4. Bei der Initalisierung der Visa Kartennummer wird die Endung "-1944" angefügt
# 5. Bei der Initalisierung der Mastercard Kartennummer wird die Endung "-1234" angefügt
# 6. Definieren sie innerhalb von Kreditkarte eine Methode validate() ohne Parameter - sie retourniert immer "Karte ok"
# 7. Instanziieren sie jeweils eine Visa- und ein Mastercard und eine Kreditkarte !
# 8. Validieren sie jede Kreditkarte


class Kreditkarte:
    def __init__(self, kartennr):
        self.kartennr = kartennr

    def validate(self):
        return "Kreditkarte ist gültig {}".format(self.kartennr)


class Visa(Kreditkarte):
    def __init__(self, kartennr):
        self.kartennr = kartennr + "-1944"


class Mastercard(Kreditkarte):

    def __init__(self, kartennr):
        self.kartennr = kartennr + "-1234"


visa = Visa("412340998")
print(visa.validate())

mastercard = Mastercard("77770999")
print(mastercard.validate())
