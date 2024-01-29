#Ohjelma joka kysyy käyttäjältä arpakuutioiden lukumäärän, heittää niitä kerran ja tulostaa silmälukujen summan
import random
dice = int(input("Syötä arpakuutioiden määrä: "))
total = 0
# loopataan niin kauan kunnes i = dice
for i in range(dice):
    throw = random.randint(1,6)
    print(f"heitto: {throw}")
    total += throw
print(f"summa: {total}")
