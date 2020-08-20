# coding=utf8
# Fit 5
MORSE = {'.-': 'a', '-...': 'b', '-.-.': 'c',
         '-..': 'd', '.': 'e', '..-.': 'f',
         '--.': 'g', '....': 'h', '..': 'i',
         '.---': 'j', '-.-': 'k', '.-..': 'l',
         '--': 'm', '-.': 'n', '---': 'o',
         '.--.': 'p', '--.-': 'q', '.-.': 'r',
         '...': 's', '-': 't', '..-': 'u',
         '...-': 'v', '.--': 'w', '-..-': 'x',
         '-.--': 'y', '--..': 'z', '-----': '0',
         '.----': '1', '..---': '2', '...--': '3',
         '....-': '4', '.....': '5', '-....': '6',
         '--...': '7', '---..': '8', '----.': '9'
         }


def morse_decoder(code):
    # Programmier - Aufgabe 5
    # Input: Morse Code
    # Bedingung 1: Einzelne Morsezeichen werden mit 1 Leerschlag von einander getrennt, Wort mit 3 Leerzeichen
    # Bedingung 2: Sollte das 1.Zeichen ein Buchstabe sein, dass muss dieser als Grossbuchstabe ausgegeben werden
    # Output: Klartext

    clear_text = ''
    split_words = code.split('   ')

    for words in split_words:
        split_letters = words.split(' ')
        for c in split_letters:
            clear_text += MORSE[c]
        clear_text += ' '

    clear_text = clear_text.rstrip()
    clear_text = clear_text.capitalize()

    return clear_text


if __name__ == '__main__':
    print("Beispiel mit Sos:")
    print(morse_decoder('... --- ...'))

    assert morse_decoder("... --- -- .   - . -..- -") == "Some text"
    assert morse_decoder("..--- ----- .---- ---..") == "2018"
    assert morse_decoder(".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--") == "It was a good day"
    print("Wenn alles korrekt ist, dann wird diese Zeile ausgegeben !")
