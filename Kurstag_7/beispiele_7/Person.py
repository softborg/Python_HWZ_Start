# -*- coding: utf-8 -*-


class Person:
    def __init__(self, vorname):
        self.vorname = vorname

    def vorstellen(self):
        print("Hallo, ich heisse", self.vorname)


person = Person("Max")
person.vorstellen()