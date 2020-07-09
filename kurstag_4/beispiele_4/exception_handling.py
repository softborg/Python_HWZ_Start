# Ausnahme - Behandlung
# Konstruktion try except

# im Block 'try' wird ein Statement kontrolliert durchgeführt. Erfolgreich !
# Sollte dennoch ein Fehler geschehen, dann wird im 'except' Block eine Fehlermeldung
# abgefangen und kann behandelt werden
resulat = 0
try:
    resulat = 3 / 0
except ZeroDivisionError as e:
    print("ZeroDivisionError", e, resulat)
else:
    print("Die Division war erfolgreich")
finally:
    print("Abschluss Arbeiten", resulat)

