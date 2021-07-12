# coding=utf8
# Fit 14
from typing import Iterable


def is_ascending(items: Iterable[int]) -> bool:
    # Programmier - Aufgabe 14
    # Input: Liste mit Zahlen
    # Bedingungen: die Liste ist korrekt, wenn die Zahlen aufsteigend sind und keine gleichen Werte enthält
    # Output: Geben sie True wenn die Liste aufsteigend ist, ansonsten False

    if len(set(items)) < len(items):
        return False

    if list(sorted(items)) == items:
        return True
    else:
        return False


if __name__ == '__main__':
    print("Zahlen aufsteigend ?")
    print(is_ascending([-5, 10, 99, 123456]))

    assert is_ascending([-5, 10, 99, 123456]) is True
    assert is_ascending([99]) is True
    assert is_ascending([4, 5, 6, 7, 3, 7, 9]) is False
    assert is_ascending([]) is True
    assert is_ascending([1, 1, 1, 1]) is False
    assert is_ascending([-5, -6]) is False

    print("Wenn alles korrekt ist, dann wird diese Zeile ausgegeben !")
