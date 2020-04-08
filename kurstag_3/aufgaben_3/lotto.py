import random

lotto = set()

while len(lotto) < 6:
    lotto.add(random.randint(1,49))

print(sorted(lotto))
