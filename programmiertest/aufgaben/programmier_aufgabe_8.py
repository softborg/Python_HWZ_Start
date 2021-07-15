# coding=utf8
# Programmier - Aufgabe 8

"""

Die Klasse A ist gegeben und muss unverändert übernommen werden
Beim Testen stürzt das Programm jeweils ab.

Verbessern sie den "Testcode" (main-Programm) so, dass die Fehlermeldung "Wert ist kleiner als 0" erscheint,
aber das Programm weiterläuft bis zum print("Wenn alles korrekt....)

"""


class A:
    kontostand = 100

    @staticmethod
    def pay(summe):
        if summe < 0:
            raise ValueError("Wert ist kleiner als 0")
        else:
            A.kontostand -= summe


# Diese "asserts" helfen für die Selbstkontrolle, sind alle Asssert Ok - dann funktioniert ihr Programm
if __name__ == '__main__':
    A.pay(10)
    assert A.kontostand == 90, "Kontostand ist 90 "
    A.pay(-5)
    assert A.kontostand == 90, "Kontostand ist 90 "

    print("Wenn alles korrekt ist, dann wird diese Zeile ausgegeben !")
