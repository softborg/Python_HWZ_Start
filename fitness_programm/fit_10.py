# coding=utf8
# Fit 10


def is_acceptable_password(password: str) -> bool:
    # Programmier - Aufgabe 10
    # Input: ein Passwort, welches validiert werden muss
    # Bedingungen: Passwort muss länger als 6 sein, ein Passwort muss mindesten 1 Zahl haben,
    # darf aber nicht nur aus Zahlen bestehen:
    # Ausnahme: wenn ein Passwort länger als 10 Zeichen besteht, dann ist alles erlaubt
    # Output: Geben sie True zurück wenn das Passwort die Kriterien erfüllt, ansonsten False

    if len(password) < 6:
        return False
    if len(password) > 9:
        return True
    digit_found = False
    char_found = False

    for s in password:
        if s.isdigit():
            digit_found = True
        if s.isalpha():
            char_found = True

    if digit_found and char_found:
        return True
    else:
        return False


if __name__ == '__main__':
    print("Password check:")
    print(is_acceptable_password('short'))

    assert is_acceptable_password('short') == False
    assert is_acceptable_password('short54') == True
    assert is_acceptable_password('muchlonger') == True
    assert is_acceptable_password('ashort') == False
    assert is_acceptable_password('muchlonger5') == True
    assert is_acceptable_password('sh5') == False
    assert is_acceptable_password('1234567') == False
    assert is_acceptable_password('12345678910') == True
    print("Wenn alles korrekt ist, dann wird diese Zeile ausgegeben !")
