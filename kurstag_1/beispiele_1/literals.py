a = 0b1010  # Binary Literals --> das binäre System, 0 oder 1 (Strom / kein Strom)
b = 100  # Decimal Literal   ---> das menschliche System
c = 0o310  # Octal Literal   --> das Computer - rechnen Zahlen von 0-7
d = 0x12c  # Hexadecimal Literal  ---> die Computersprache - "Zahlen" von 0-9 und A-F

# Float Literal
f1 = 21.3
f2 = 1.2e2

# Complex Literal
x = 53.4j

print("--- Zahlen Literals ---")
print(a, b, c, d)
print(f1, f2)
print(x, x.imag, x.real)

print("\n--- String Literals ---")

# String Literal
s = "This is Python"
char = "C"
mehrzeiliger_str = """This is a multiline string
 with more than one 
 line code."""
unicode = u"\u00dcnic\u00f6de"  # das führende u leitet einen Unicode ein gefolgt eines Strings im Unicode - Stil
raw_str = r"raw \n string"  # all Tabularzeichen werden ignoriert nur die Werte übernommen.

print(s)
print(char)
print(mehrzeiliger_str)
print(unicode)
print(raw_str)

# Boolean Literal
print("\n--- Boolen Literals ---")
wahr = True  # etwas ist wahr
falsch = False  # etwas ist nicht wahr

print(5 == 5)  # diese Aussage ist wahr -- 5 ist gleich 5
print(5 < 4)  # diese Aussage ist falsch -- 5 ist nicht kleiner als 4

# Sommlungen (Listen, Tupel, Dictonaries, set) Literal
print("\n--- Collection Literals ---")

farben = ["blau", "rot", "gelb"]  # list
zahlen = (1, 2, 3)  # tuple
kantone = {'BS': 'Basel Stadt', 'AI': 'Appenzell Innerroden', 'GL': 'Glaurs'}  # dictionary
vokale = {'a', 'e', 'i' , 'o', 'u'}  # set

print(farben)
print(zahlen)
print(kantone)
print(vokale)
