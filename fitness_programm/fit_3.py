# coding=utf8
# Fit 3


def split_list(items: list) -> list:
    # Programmier - Aufgabe 3
    # Input: Liste
    # Bedingungen: Eine Liste soll so aufgeteilt werden, dass die 1. Liste mehr Elemente enthält, als die 2. Liste
    # wenn dies nicht möglich ist, dann müssen beide Listen gleich gross sein (Anzahl Elemente), leere
    # Output: Liste mit 2 Listen
    # Vorbedingungen: Input Liste darf 0 sein, dann ist auch der Return mit 0 Listen gefüllt

    if len(items) == 0:
        return [[],[]]
    if len(items) % 2 == 0:
        return [items[0:int(len(items)/2)], items[int(len(items)/2)::]]
    else:
        return [items[0:int((len(items)+1)/2):], items[int((len(items)+1)/2)::]]


if __name__ == '__main__':
    print("Listen aufteilen:")
    print(split_list(''))

    # # Diese "asserts" helfen für die Selbstkontrolle, sind alle Asssert Ok - dann funktioniert ihr Prorgramm
    assert split_list([1, 2, 3, 4, 5, 6]) == [[1, 2, 3], [4, 5, 6]]
    assert split_list([1, 2, 3]) == [[1, 2], [3]]
    assert split_list([1, 2, 3, 4, 5]) == [[1, 2, 3], [4, 5]]
    assert split_list([1]) == [[1], []]
    assert split_list([]) == [[], []]
    print("Wenn alles korrekt ist, dann wird diese Zeile ausgegeben !")
