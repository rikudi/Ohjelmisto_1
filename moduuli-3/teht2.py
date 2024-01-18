LUX_str = str("LUX on parvekkeellinen hytti yläkannella")
A_str = str("A on ikkunallinen hytti autokannen yläpuolella")
B_str = str("B on ikkunaton hytti autokannen yläpuolella")
C_str = str("C on ikkunaton hytti autokanne alapuolella")

hytti_input = input("Syötä hyttiluokka:")

if hytti_input == "LUX":
    print(LUX_str)
elif hytti_input == "A":
    print(A_str)
elif hytti_input == "B":
    print(B_str)
elif hytti_input == "C":
    print(C_str)
else:
    print("Syötä kelvollinen hyttiluokka")

