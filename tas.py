
import random

tas = random.randint(1, 6)

if tas == 6:
    print(tas)
    for i in range(1,3):
        tas = random.randint(1, 6)
        print(tas)
else:
    print(tas)
    exit
    


