# Ausnahme - Behandlung
# Konstruktion try except

# im Block 'try' wird ein Statement kontrolliert durchgeführt. Erfolgreich !
# Sollte dennoch ein Fehler geschehen, dann wird im 'except' Block eine Fehlermeldung
# abgefangen und kann behandelt werden
resulat = 0
try:
    resulat = 3 / 0
except ArithmeticError:
    print("ArithmeticError", resulat)
finally:
    print(" Abschluss Arbeiten", resulat)
