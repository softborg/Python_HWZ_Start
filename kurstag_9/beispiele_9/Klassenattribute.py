# coding=utf8
"""
Zinssatz ist eine Klassenvariable
Sie ist fix an die Klasse gebunden.
Sie existiert ob es Instanzen gibt oder nicht
Verhindert Redundanz
"""


class Konto:
    # Klassenattribut
    zinssatz = 0.5

    def __init__(self, inhaber):
        self.inhaber = inhaber

    def say_hello(self):
        print("Hallo, ich bin", self.inhaber)


print(Konto.zinssatz)
k = Konto("Max")

print(Konto.zinssatz)

Konto.zinssatz = 0.75
print(Konto.zinssatz)

