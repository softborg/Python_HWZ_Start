# coding=utf8
# Fit 13


def is_all_upper(text: str) -> bool:
    # Programmier - Aufgabe 13
    # Input: text
    # Bedingungen: der Text ist gültig, wenn es nur GROSSBUCHSTABEN gibt
    # Output: Geben sie True zurück wenn nur Grossbuchstaben vorhanden sind, ansonsten False

    if text.isupper():
        return True
    else:
        return False


if __name__ == '__main__':
    print("Alles GROSSBUCHSTABEN ?")
    print(is_all_upper('ALL UPPER'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_all_upper('ALL UPPER') == True
    assert is_all_upper('all lower') == False
    assert is_all_upper('mixed UPPER and 666') == False
    assert is_all_upper('') == False

    print("Wenn alles korrekt ist, dann wird diese Zeile ausgegeben !")
