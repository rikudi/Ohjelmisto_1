#Ohjelma joka tulostaa kaksi erilaista numerolukon koodia
import random

#Generoi satunnaisen kokonaisluvun annettujen parametrien välillä
koodi_1 = random.randint(100, 999)
koodi_2 = ''.join(str(random.randint(1, 6)) for _ in range(4))

print(koodi_1, koodi_2)