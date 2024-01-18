vuosi = int(input("Anna vuosiluku:"))

#Check if remainder is zero when divided by four and remainder
if vuosi % 4 == 0 or (vuosi % 100 == 0 and vuosi % 400 == 0):
    print(vuosi, " on karkausvuosi")
else:
    print(vuosi, " ei ole karkausvuosi")
