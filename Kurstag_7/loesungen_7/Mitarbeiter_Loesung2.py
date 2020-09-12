# coding=utf8

# Aufgabe 2 - Mitarbeiter
# 1. lege eine Klasse 'Mitarbeiter' an
# 2. beim Instanziieren eines Mitarbeiters soll 'name' und 'lohn' als Parameter mitgegeben werden
# der 'name' ist ein öffentliches Attribut, der 'lohn' ist ein privates Attribut
# 3. Lege eine Instanz Mitarbeiter an
# 4. Gib den Namen und den Lohn mittels einer Methode get_lohn() Was stellen sie jetzt fest ?


class Mitarbeiter:
    def __init__(self, name, lohn):
        self.name = name
        self.__lohn = lohn

    def get_lohn(self):
        return self.__lohn


m = Mitarbeiter("Stefan", 1000)
print("Der Mitarbeiter heisst {} und sein Lohn ist {}".format(m.name, m.get_lohn()))
