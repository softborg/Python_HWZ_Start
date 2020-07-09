# coding=utf8
# Programmier - Aufgabe 3


def index2(text, symbol):
    """
        Gib den 2.ten Index des gesuchten Zeichen zurück.
        Wenn nichts gefunden wird, dann soll 'None' zurückgegeben werden.
    """


if __name__ == '__main__':
    print('Beispiel für index2:')
    print(index2("sms", "s"))

    # Diese "asserts" helfen für die Selbstkontrolle, sind alle Asssert Ok - dann funktioniert ihr Prorgramm
    assert index2("sms", "s") == 2, "1"
    assert index2("Stockholm", "o") == 6, "2"
    assert index2("Hallo", "l") == 3, "3"
    assert index2("Hallo Meier", " ") is None, "4"
    assert index2("Hallo Herr Meier", " ") == 10, "5"
    print("Wenn alles korrekt ist, dann wird diese Zeile ausgegeben !")
