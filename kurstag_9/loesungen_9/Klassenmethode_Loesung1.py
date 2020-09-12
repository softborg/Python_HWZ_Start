# coding=utf8

# Aufgabe 1 - Kreis 1. erstellen sie folgende Klasse Person 2. beim Instanziieren soll der Name und das Alter
# mitgegeben werden, der Name und Alter sind public 3. definieren sie statische Methode volljährig mit Parameter
# alter. Diese Methode prüft ob jemand älter 18 ist → return True, ansonsten False. 4. rufen sie diese Methode
# volljährig auf und drucken das Ergebnis auf die Konsole
from datetime import date


class Person:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter

    # Klassenmethode um eine Person via Jahrgang anzulegen
    @classmethod
    def person_by_year(cls, name, jahrgang):
        return cls(name, date.today().year - jahrgang)

    @staticmethod
    def volljaehrig(alter):
        return alter >= 18


person = Person.person_by_year("Stefan", 2004)
print("Ist {} volljährig {}".format(person.name, Person.volljaehrig(person.alter)))
