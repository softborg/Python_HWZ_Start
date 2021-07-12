# coding=utf8
# Fit 2


def nur_worte_rueckwaerts(text: str) -> str:
    split_text = text.split(' ')  # mit split den Text in eine Liste umwandeln
    reversed_text = ' '.join(reversed(split_text))  # Drehen Reihenfolge der Wörter und wieder in einen String umwandeln
    return reversed_text[::-1] # dreht den text erneut um

    #return ' '.join(word[::-1] for word in text.split(" "))


if __name__ == '__main__':
    print("Example:")
    print(nur_worte_rueckwaerts(''))

    # # Diese "asserts" helfen für die Selbstkontrolle, sind alle Asssert Ok - dann funktioniert ihr Prorgramm
    assert nur_worte_rueckwaerts('') == ''
    assert nur_worte_rueckwaerts('welt') == 'tlew'
    assert nur_worte_rueckwaerts('hello world') == 'olleh dlrow'
    assert nur_worte_rueckwaerts('hello   world') == 'olleh   dlrow'
    assert nur_worte_rueckwaerts('Willkommen') == 'nemmoklliW'
    print("Wenn alles korrekt ist, dann wird diese Zeile ausgegeben !")
