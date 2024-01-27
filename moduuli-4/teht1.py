#Ohjelma joka tulostaa kolmella jaettavan luvun 1-1000 väliltä
currentCount = 1
while currentCount < 1000:
    if currentCount % 3 == 0:
        print(currentCount)
        currentCount += 1
    else:
        currentCount += 1