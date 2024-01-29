# Ohjelma joka kysyy käyttäjältä pistemäärää, joka arvotaan neliön N-alueelle. Neliön sisällä on ympyrä A, jonka keskipiste on origo '0,0'
# Neliön kulmatpisteet ovat x ja y akselilla pisteissä (1, 1), (1, -1), (-1, 1), (-1, -1).
# Ohjelman on tarkoitus tarkistaa kuinka moni pisteistä osuu ympyrän sisälle ja laskea piin likiarvo.
import random

points_inside_circle = 0
points_total = 0
points = int(input("Syötä pistemäärä: "))
# jatketaan looppia niin kauan kuin points_total on pienempi kuin käyttäjän syöttämä luku
while points_total < points:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    # katsotaan onko pisteen sijainti pienempi kuin 1
    if x**2 + y**2 < 1:
        points_inside_circle += 1
    points_total += 1

# lasketaan piin arvo
pi_value = 4 * points_inside_circle / points
print("pi =", pi_value)