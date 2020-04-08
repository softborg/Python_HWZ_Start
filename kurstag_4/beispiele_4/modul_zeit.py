import datetime

# jetzt Zeitpunkt
jetzt = datetime.datetime.now()
print(jetzt)

# 2020-04-06 14:30:32.602166  - im Format yyyy-MM-DD hh:mm:ss.

# Nur Datum
datum = datetime.date.today()
print(datum)  # im Format yyyy-MM-DD

# eigenes Datum setzen
mein_datum = datetime.date(2019, 11, 23)
print(mein_datum)

# Datum heute - einzel
heute = datetime.date.today()
print("Aktuelles Jahr:", heute.year)
print("Aktueller Monat:", heute.month)
print("Aktueller Tag:", heute.day)

# Zeit setzen (Stunde = 0, Minute = 0, Sekunge = 0)
stunde_0 = datetime.time()
print("a =", stunde_0)

# Zeit setzen (Stunde, Minute und Sekunde)
start_unterricht = datetime.time(9, 0, 0)
print("Start Unterricht =", start_unterricht)

# Zeit setzen (Stunde, Minute und Sekunde) mit benannten Variablen
ende_unterricht = datetime.time(hour=12, minute=15, second=0)
print("Ende Unterricht =", ende_unterricht)

# Zeit setzen (Stunde, Minute, Sekunde und Millisekunde)
exakter_zeitpunkt = datetime.time(12, 15, 0, 0)
print("Exakter Zeitpunkt =", exakter_zeitpunkt)

# Rechnen mit Datum und Zeit
t1 = datetime.date(year=2019, month=5, day=1)
t2 = datetime.date(year=2018, month=5, day=1)
dauer = t1 - t2
print("Dauer 1 =", dauer)

t1 = datetime.timedelta(hours=12, minutes=5, seconds=0)
t2 = datetime.timedelta(hours=12, minutes=0, seconds=30)
dauer = t1 - t2
print("Dauer 2 =", dauer)


# DateTime Object formatieren in String mittels: strftime()
jetzt = datetime.datetime.now()

uhrzeit = jetzt.strftime("%H:%M:%S")
print("Uhrzeit:", uhrzeit)

# dd.mm.YY H:M:S Format
datum3 = jetzt.strftime("Datum: %m.%d.%Y Zeit: %H:%M:%S")
print("Datum 3:", datum3)

datum4 = jetzt.strftime("Datum: %d.%m.%Y Zeit: %H:%M:%S")
print("Datum 4:", datum4)

# Aus String in Datum umwandeln mittels: strptime()
datum5 = jetzt.strptime("31.12.2010", "%d.%m.%Y")
print("Datum 5: {} und der Type {} ".format(datum5, type(datum5)))
