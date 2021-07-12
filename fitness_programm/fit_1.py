# coding=utf8
# Fit 1


def fill_list(array):
    """
        Ihr Programm soll zwei (20-stellige) int-Arrays mit Werten befüllen.
        Das erste Array soll mit Werten ab 5 in 5er-Schritten befüllt werden (5,10,15,...).
        Die Befüllung ist mit einer for-Schleife auszuführen!
        Das Programm soll die Summe und Mittelwert (Summe/Anzahl der Elemnte) als Tuple zurückgeben
    """
    n1 = [5 * (i+1) for i in range(10)]
    print("resultat", sum(n1), sum(n1)/len(n1))
    return sum(n1), sum(n1)/len(n1)


# Diese "asserts" helfen für die Selbstkontrolle, sind alle Asssert Ok - dann funktioniert ihr Prorgramm
if __name__ == '__main__':
    print('Fill-List:')
    print(fill_list([5, 10, 15, 20, 25, 30, 35, 40, 45, 50]))

    assert fill_list([5, 10, 15, 20, 25, 30, 35, 40, 45, 50]) == (275, 27.5), "(5, 10, 15, 20, 25, 30, 35, 40, 45, " \
                                                                              "50]=(275, 27.5)"

    print("Wenn alles korrekt ist, dann wird diese Zeile ausgegeben !")