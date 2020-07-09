# coding=utf8
# Programmier - Aufgabe 1


def calc_list(array):
    """
        Summiere die geraden Elemente (0,2, etc.) und multipliziere die erhalten Summe mit dem letzten Element.
        Das Ergebnis wird als int zurückgegeben
        Falls eine leere Liste übergeben wird, so wird 0 zurückgegeben ---> siehe auch asserts
    """


# Diese "asserts" helfen für die Selbstkontrolle, sind alle Asssert Ok - dann funktioniert ihr Prorgramm
if __name__ == '__main__':
    print('Calc-List:')
    print(calc_list([0, 1, 2, 3, 4, 5]))

    assert calc_list([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert calc_list([1, 3, 5]) == 30, "(1+5)*5=30"
    assert calc_list([6]) == 36, "(6)*6=36"
    assert calc_list([]) == 0, "Eine leere Liste= 0"

    print("Wenn alles korrekt ist, dann wird diese Zeile ausgegeben !")
