def evenList(list):
    evenList = []
    for num in list:  # loopataan niin monesti kun listassa on lukuja
        if num % 2 == 0:  # tarkistetaan onko indeksin luku jakojäännös = 0
            evenList.append(num)
    return evenList

def main():
    originalList = [5, 66, 24, 87, 2, 19, 35, 32, 28] # esimerkki-lista
    newList = evenList(originalList)

    print(f"original list: {originalList} \n new list: {newList}")


if __name__ == "__main__":
    main()