#Ohjelma joka muuntaa tuumat senttimetriksi niin kauan kuin syötetty tuumamäärä on negatiivinen
inches = float(input("Syötä tuumamäärä: "))
cm_multiplier = 2.54
while inches >= 0:
    print("Tuumat senttimetreinä: ", inches * cm_multiplier)
    inches = float(input("Syötä tuumamäärä: "))
print("Syötetty negatiivinen luku, suljetaan ohjelma")