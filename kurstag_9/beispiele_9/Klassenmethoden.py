# coding=utf8
"""
change_zins ist eine Klassenmethoden
Sie ist fix an die Klasse gebunden.
"""


class Konto:
    zinssatz = 0.5

    def __init__(self, betrag):
        self.saldo = betrag

    @classmethod
    def change_zins(cls):
        print("Der neue Zins beträgt:", cls.zinssatz * 0.99)


print(Konto.zinssatz)
k = Konto(100)
Konto.change_zins()

