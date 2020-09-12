class Sichtschutz:

    def __init__(self, public, proteced, private):
        self.public = public
        self._protected = proteced
        self.__private = private


name = "Stefan"
lohn = 1000
pin = "geheimzahl"

s = Sichtschutz(name, lohn, pin)

print(s.name)
print(s.lohn)
print(s.pin)  # --> führt zu Fehler, da Pin ausserhalb der eignen Klasse angesprochen wurde.
