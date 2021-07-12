
import re

mastercard_pattern = '(5[1-5][0-9])'
masterkarte_karte = '5167990007674519'
match = re.match(mastercard_pattern, masterkarte_karte)

print(match)