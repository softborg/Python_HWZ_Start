class Person:
    def __init__(self, vorname, nachname):
        self.__vorname = vorname
        self.__nachname = nachname

    @property
    def vorname(self):
        return self.__vorname

    def set_vorname(self, vorname):
        self.__vorname = vorname

    @property
    def ganzer_name(self):
        return self.__vorname + " " + self.__nachname


class Kunde(Person):
    pass


kunde = Kunde("Max", "Berger")
print(kunde.vorname)
kunde.set_vorname("Stefan")

print(kunde.ganzer_name)
