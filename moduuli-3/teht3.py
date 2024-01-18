sukupuoli = input("Anna sukupuolesi:")
hemoglobiini = int(input("Anna hemoglobiiniarvo:"))

if sukupuoli == "Nainen" and (117 <= hemoglobiini <= 175):
    print("Hemomglobiiniarvosi on normaali")
elif sukupuoli == "Nainen" and (hemoglobiini > 175):
    print("Hemomglobiiniarvosi on korkealla")
elif sukupuoli == "Nainen" and (hemoglobiini < 117):
    print("Hemomglobiiniarvosi on alhainen")
elif sukupuoli == "Mies" and (117 <= hemoglobiini <= 175):
    print("Hemomglobiiniarvosi on normaali")
elif sukupuoli == "Mies" and (hemoglobiini > 175):
    print("Hemomglobiiniarvosi on korkealla")
elif sukupuoli == "Mies" and (hemoglobiini < 117):
    print("Hemomglobiiniarvosi on alhainen")
else:
    print("Tarkista syötetyt tiedot")