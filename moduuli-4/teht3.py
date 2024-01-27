#Ohjelma kysyy lukuja kunnes syöte on tyhjä merkkijono. Tulostaa syötetyistä luvuista pienimmän ja suurimman

syote = input("Syötä luku:")                #kysytään käyttäjältä syötettä
inputs = []                                 #alustetaan tyhjä taulukko "inputs"

while syote != "":                          #toistetaan while looppia niin kauan kun käyttäjän syöte ei ole tyhjä merkkijono ("")
    a = int(syote)                          #muutetaan saatu syöte merkkijonosta kokonaisluvuksi (str-->int) ja sijoitetaan muuttujaan "a"
    inputs.append(a)                        #append-metodilla lisätään muuttujan a-arvo taulukkoon inputs
    print("Syötteet:", inputs)              #printataan taulukkoa havainnollistamiseksi
    syote = input("Syötä luku:")            #kysytään syötettä uudestaan

    isoin = max(inputs)                     #Tuo suurimman luvun inputs-listasta ja sijoittaa muuttujaan isoin
    pienin = min(inputs)                    #Tuo pienimmän luvun inputs-listasta ja sijoittaa muuttujaan pienin
print("Isoin: ", isoin, "Pienin: ", pienin) #Lopuksi tulostetaan konsoliin pienin ja suurin