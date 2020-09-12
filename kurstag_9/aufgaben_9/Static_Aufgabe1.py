# coding=utf8

# Aufgabe 1 - Static_Aufgabe
# 1. erstellen sie die Klasse Person
# 2. beim Instanziieren soll der Name und das Alter mitgegeben werden, der Name und Alter sind public
# 3. definieren sie statische Methode volljährig mit Parameter alter.
#    Diese Methode prüft ob jemand älter 18 ist → return True, ansonsten False.
# 4. rufen sie diese Methode volljährig auf und drucken das Ergebnis auf die Konsole


class Person:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter

    @staticmethod
    def volljaehrig(alter):
        return alter >= 18


print(Person.volljaehrig(17))
