# Frage 34:
#
#
class A:
    kontostand = 100

    @staticmethod
    def pay(summe):
        if summe < 0:
            raise ValueError("Wert ist kleiner als 0")
        else:
            A.kontostand -= summe


try:
    A.pay(10)
    print("Kontostand {}:".format(A.kontostand))
except ValueError as e:
    print(e)
