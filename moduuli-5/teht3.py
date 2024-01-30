n = int(input("Syötä luku: "))

if n > 1:
    for i in range(2, int(n/2)):
        if(n % i) == 0:
            print("ei ole alkuluku")
            break
    else:
        print("on alkuluku")
else:
    print("ei ole alkuluku")