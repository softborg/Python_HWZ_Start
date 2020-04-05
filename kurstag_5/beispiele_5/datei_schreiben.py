# Schreiben in eine Datei

# f = open("inhalt.txt", "w")
# f.write("Bern\n")
# f.write("Solothurn\n")
# f.write("Bellinzona\n")
# f.write("Chur\n")
# f.write("Basel\n")
# f.close()


#In einer Datei Zeilen anhängen am Ende mit Mode=a+
f = open("inhalt.txt", "a+")
f.write("Herisau\n")
f.write("Glarus\n")
f.write("Sion\n")
f.write("Freiburg\n")
f.write("Delsberg\n")
f.close()
