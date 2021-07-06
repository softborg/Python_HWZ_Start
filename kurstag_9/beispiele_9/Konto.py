# coding=utf8
class Konto(object):
    def __init__(self, kontostand):
        self._kontostand = kontostand
        self.inhaber = "Felix Muster"
        self.__pin = "-adsfadfj6663"

    def einzahlen(self, betrag):
        self._kontostand += betrag

    def auszahlen(self, betrag):
        self._kontostand -= betrag

    # neuere Art einer Property
    @property
    def kontostand(self):
        return self._kontostand

    @kontostand.setter
    def kontostand(self, betrag):
        self._kontostand = betrag

    # ältere Art einer Porperty
    def pin(self):
        return "Zugriff verboten"

    # ältere Art einer Porperty
    pin = property(pin)


k = Konto(20)
print(k.inhaber)
k.kontostand = 100
print(k.pin)
print(k.kontostand)
