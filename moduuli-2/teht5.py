leiviskat = float(input("Anna leiviskät:"))
naulat = float(input("Anna naulat:"))
luodit = float(input("Anna luodit:"))

luoditTotal = float(((leiviskat*20)+naulat)*32)
print(luoditTotal)

totalMass = float(luoditTotal * 13.3)

print(totalMass, "kg")
