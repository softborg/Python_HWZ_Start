# coding=utf8
# Probe Programmier - Aufgabe 2
# Erstellen sie Klasse Binary die 2 statische Methoden convert_to_bin und convert_to_dec besitzt
# Diese Methoden können jeweils von Decimalsystem auf Binärsystem bzw. umgekehrt rechnen.

class Binary:

    @staticmethod
    def convert_to_bin(zahl):
        return bin(zahl)

    @staticmethod
    def convert_to_dec(binary):
        return int(binary,2)


if __name__ == '__main__':
    print("Convert to Binary und Decimal:")

    # Diese "asserts" helfen für die Selbstkontrolle, sind alle Asssert Ok - dann funktioniert ihr Prorgramm
    assert Binary.convert_to_bin(432) == '0b110110000'
    assert Binary.convert_to_dec('0b110000000') == 384

    print("Wenn alles korrekt ist, dann wird diese Zeile ausgegeben !")