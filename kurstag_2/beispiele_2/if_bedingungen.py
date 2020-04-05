# if bedingung, wenn etwas zutrifft

# Wochentage 'Mo', 'Di' 'Mi', 'Do', 'Fr, 'Sa', 'So'

wochentag = 'So'

# if = keyword
# Aussage wochentag == 'So' --> Auswertung zu True: Bedingung erfüllt:
# : ende des Statement
# alle darunter eingerückten Statement hängen nun von der if Bedingung ab

# Ausgabe: Heute gibt es Sonntagszopf
if wochentag == 'So':
    print("Heute gibt es Sonntagszopf")


# if Bedingung nicht erfüllt, somit keine Ausgabe. ----> Aber was gibt es an den anderen Tagen ?
if wochentag == 'Mo':
    print("Heute gibt es Sonntagszopf")

print('-' * 32)

# Am Sonntag gibt es Zopf, an den anderen Tagen Brot.
# Lösung: if else Bedingung
wochentag = 'Mo'
if wochentag == 'So':
    print("Am {} gibt es Sonntagszopf".format(wochentag))
else:
    print("Am {} gibt es Brot".format(wochentag))

print('-' * 32)

# Am Samstag gibt es Gipfeli und Sonntag gibt es Zopf, an den anderen Tagen Brot.
# Lösung: if else Bedingung
wochentag = 'Sa'
if wochentag == 'So':
    print("Am {} gibt es Sonntagszopf".format(wochentag))
elif wochentag == 'Sa':
    print("Am {} gibt es Gipfeli".format(wochentag))
else:
    print("Am {} gibt es Brot".format(wochentag))
