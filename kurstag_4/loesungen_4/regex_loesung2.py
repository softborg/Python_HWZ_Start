import re


visa_pattern = '^4[0-9]{12}(?:[0-9]{3})?$'

visa_karte = '4369670089503161'

match = re.match(visa_pattern, visa_karte)

print(match)

visa_pattern2 = '4\\d{12}(\\d{3})?'
match = re.match(visa_pattern2, visa_karte)
print(match)

# 51-55: MasterCard Zahlen starten mit 2 Zahlen von 51 bis 55 oder mit dem Block 2221 bis 2720. Alle KK sind 16 Zahlen
mastercard_pattern = '(5[1-5][0-9]{14}|2(22[1-9][0-9]{12}|2[3-9][0-9]{13}|[3-6][0-9]{14}|7[0-1][0-9]{13}|720[0-9]{12}))'

masterkarte_karte = '5167990007674519'
match = re.match(mastercard_pattern, masterkarte_karte)
print(match)

