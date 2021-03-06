# coding=utf8
# Programmier - Aufgabe 2 - Lösung

import re
# Input: ein String mit 'Worten'
# Output: Die Ausgabe ist ein Boolean
# Vorbedingungen: Die Eingabe enthält Worte oder Zahlen. Es gibt keine Worte die aus Zahlen und Buchstaben bestehen
# 0 < len(words) < 100


def check_wort(words):
    return bool(re.search("\\D+ \\D+ \\D+", words))


# Diese "asserts" helfen für die Selbstkontrolle, sind alle Asssert Ok - dann funktioniert ihr Prorgramm
if __name__ == '__main__':
    print('Beispiel Wortcheck:')
    print(check_wort("Hallo Welt Max"))

    assert check_wort("Hallo Welt Max") == True, "Hallo"
    assert check_wort("Er ist 007 Bond") == False, "007 Bond"
    assert check_wort("1 2 3 4") == False, "Zahlen"
    assert check_wort("bla bla bla bla") == True, "Bla Bla"
    assert check_wort("Hoi") == False, "Hoi"
    print("Wenn alles korrekt ist, dann wird diese Zeile ausgegeben !")
