import random


class Auto:
    def __init__ (self, modell, preis):
        self.modell = modell
        self.preis = preis

    def __calc_rabatt(self, prozent):
        return self.preis * (100 - prozent)/100 - random.random() * 1000

    def vk(self, prozent):
        return self.__calc_rabatt(prozent)



a = Auto("BMW", 23000)
print(a.vk(12))