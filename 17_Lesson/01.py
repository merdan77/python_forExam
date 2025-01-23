hasap = 5
while True:
    print("TMCELL hyzmatlary")
    print("1.Balansyny barlamak")
    print("2.Balansyny doldurmak")
    hyzmat = input("Hyzmat gornusini saylan (1,2): ")
    if hyzmat == '1':
        tel_belgi =int(input("Telefon belginiz: "))
        if 60000000 <= tel_belgi <= 65999999:
            print(f"Sizin hasabynyzda {hasap} TMT bar")
        else:
            print("Yalnys telefon belgi girizdiniz")
    

    elif hyzmat == '2':
        tel_belgi =int(input("Telefon belginiz: "))
        if 60000000 <= tel_belgi <= 65999999:
            toleg_mocberi =int(input("Toleg mocberiniz (TMT): "))
            if 1 <= toleg_mocberi <= 50:
                hasap += toleg_mocberi
                print(f"Sizin hasabynyz {hasap} TMT")
            else:
                print(f"Toleg mukdary 1-50 TMT aralygy bolmaly")
        else:
            print("Yalnys telefon belgi girizdiniz")
    elif hyzmat == '3':
        break

    else:
        print("Yalny buyruk")