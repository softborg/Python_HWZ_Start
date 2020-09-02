# coding=utf8
# Fit 9
from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    # Programmier - Aufgabe 9
    # Input: eine Liste mit Inhalt
    # Output: Geben sie True zurück wenn alle Elemente den gleichen Inhalt haben, ansonsten False
    if len(elements) == 0:
        return True
    return elements.count(elements[0]) == len(elements)


if __name__ == '__main__':
    print("Beispiel alle Elemente denselben Inhalt:")
    print(all_the_same([1, 1, 1]))

    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same(['a', 'a', 'a']) == True
    assert all_the_same([]) == True
    assert all_the_same([1]) == True
    print("Wenn alles korrekt ist, dann wird diese Zeile ausgegeben !")
