# mittels input('Wert') werden Eingaben (immer als String) des Users gelesen
# input ist ein builtin-function von Python bereit gestellt

# Frage: Wie heissen sie ?
print("Wie heissen Sie?")
name = input()

# Ausgaben: Willkommen [name=Eingabe des Users]
print("Willkommen", name)

# Frage: Wie gross sind sie in cm ?
print("Wie gross sind sie in cm ?")

# Eingabe wird von String nach int oder float konvertiert - sofern es sich um Zahlen handelt, ansonsten Error
groesse = int(input())
print(groesse)
# Ausgaben: Sind
print("Sie sind ", groesse/100, " Meter gross")
#print("Sie sind {groesse} Meter gross".format(groesse=groesse/100))


