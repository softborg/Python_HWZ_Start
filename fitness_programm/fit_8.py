# coding=utf8
# Fit 8


def popular_words(text: str, words: list) -> dict:
    # Programmier - Aufgabe 8
    # Input: Text der untersuchen ist, Liste aller Wörter die gezählt werden sollen
    # Output: Dictionary je Suchwort und Anzahl --> siehe Assert

    text = text.lower()
    splitted_words = text.split()
    answer = {}
    for word in words:
        answer[word] = splitted_words.count(word)
    return answer


if __name__ == '__main__':
    print("Beispiel:")
    print(popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']))

    assert popular_words('''
When I was One
I had just begun
When I was Two
I was nearly new
''', ['i', 'was', 'three', 'near']) == {
        'i': 4,
        'was': 3,
        'three': 0,
        'near': 0
    }
    print("Wenn alles korrekt ist, dann wird diese Zeile ausgegeben !")
