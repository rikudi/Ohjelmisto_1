leiviskat = float(input("Anna leiviskät:")) * 20
naulat = (float(input("Anna naulat:")) + leiviskat) * 32
luodit = float(input("Anna luodit:"))

luoditTotal = luodit + naulat
paino = luoditTotal * 13.3
kg = int(paino / 1000)
gramma = float("{:.2f}".format(paino % 1000))
print("paino:", kg, "kg:", gramma, "grammaa")