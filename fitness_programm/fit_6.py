# coding=utf8
# Fit 6


def checkio(number: int) -> int:

    # Programmier - Aufgabe 6
    # Input: Zahl
    # Bedingung 1: Multiplizier alle einzlnen Stellen einer Zahl
    # Bedingung 2: die 0 soll übersprungen werden
    # Output: Zahl Multiplikation aller einzelnen Stellen (Zahlen)

    str_number = str(number)
    result = 1

    for n in str_number:
        if n != '0':
            result *= int(n)
    return result


if __name__ == '__main__':
    print('Example:')
    print(checkio(123405))

    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    assert checkio(332) == 18
    print("Wenn alles korrekt ist, dann wird diese Zeile ausgegeben !")
