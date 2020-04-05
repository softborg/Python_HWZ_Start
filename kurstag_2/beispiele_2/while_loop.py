# while -- Schlaufe: wiederhole solange die Statements wie die Bedingung True (ist)

i = 5
while i < 10:
    print("Der Wert von i = {}".format(i))
    i += 1

print('-' * 32)

# while --- Schlaufe: vorzeitig verlassen
# sobald j == 8 ist True ist wird break durchgeführt
j = 5
while j < 10:
    print("Der Wert von j = {}".format(j))
    j += 1
    if j == 8:
        print("ich break jetzt")
        break

print('-' * 32)

# while --- Schlaufe: mit Continue Rest überspringen
# sobald k % 2 false wird der "print" ausgelassen
k = 0
while k < 10:
    k += 1
    if k % 2 == 0:
        text = "Gerader Wert von k = {}".format(k)
    else:
        continue
    print(text)
