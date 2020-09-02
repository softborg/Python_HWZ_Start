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

    # ältere Art einer Porperty
    def pin(self):
        return "Zugriff verboten"

    # ältere Art einer Porperty
    pin = property(pin)


k = Konto(20)
print(k.inhaber)
print(k.kontostand)
print(k.pin)
