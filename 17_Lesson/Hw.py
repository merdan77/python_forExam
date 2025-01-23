def harytlary_gorkez (harytlar):
    if not harytlar:
        print("Dukan bos! ")
    else:
        print("Dukandaky ahli harytlary: ")
        for haryt in harytlar:
            print(f"Ady:{haryt['ady']}, Bahasy: {haryt['bahasy']} manat, Mukdary:{haryt ['mukdary']} kg")

def haryt_satyn_al(harytlar):
    ady =input("Satyn almak isleyan harydyn adyny girizin: ")
    mukdary =float(input("Satyn almak isleyan mukdarynyzy (kg) girizin:  "))
    tapyldy = False
    for haryt in harytlar:
        if haryt ['ady'] == ady:
            tapyldy = True
            if haryt ['mukdary'] >= mukdary:
                haryt ['mukdary'] -= mukdary
                jemi = mukdary * haryt ['bahasy']
                print(f"Satyn alys gutardy! Jemi toleg: {jemi} manat")
            else:
                print("Dukanda yeterlik haryt yok!")
            break
        if not tapyldy:
            print("Haryt tapylmady! ")

def taze_haryt_gos(harytlar):
    ady = input("Taze harydyn adyny girizin: ")
    bahasy =float(input("Harydyn bahasyny girizin (manat): "))
    mukdary = float(input("Harydyn mukdary girizin (kg): "))
    harytlar.append({"ady":ady, "bahasy": bahasy, "mukdary": mukdary})
    print("Taze haryt dukana gosukldy!")

def harydyn_bahasyny_uytget(harytlar):
    ady =input("Bahasyny uytgetmek isleyan harydyn adyny girizin:  ")
    taze_baha = float(input("Taze bahany girizin (manat):  "))
    tapyldy = False
    for haryt in harytlar:
        if haryt ['ady'] == ady:
            tapyldy = True
            haryt['bahasy'] = taze_baha
            print("Harydyn bahasy tazelendi! ")
            break
    if not tapyldy:
        print("Haryt tapylmady!")

def harydy_ayyr(harytlar):
    ady =input("Ayyrmak isleyan harydyn adyny girizin: ")
    tapyldy = False
    for haryt in harytlar:
        if haryt ['ady'] == ady:
            tapyldy = True
            harytlar.remove(haryt)
            print("Haryt dukanda ayryldy!")
            break
    if not tapyldy:
        print("Haryt tapalmady! ")

def mukdary_artdyr(harytlar):
    ady = input("Mukdary artdyrmak isleyan harydyn girizin:  ")
    gosmaca_mukdar =float(input("Nace kilogram gosmak isleyarsiniz? "))
    tapyldy = False
    for haryt in harytlar:
        if haryt ['ady'] == ady:
            tapyldy = True
            haryt ['mukdary'] += gosmaca_mukdar
            print("Harydyn mukdary tazelendi!  ")
            break
    if not tapyldy:
        print("Haryt tapylmady! ")

def kassany_gorkez(harytlar):
    jemi =sum(haryt['bahasy'] * haryt ['mukdary'] for haryt in harytlar)
    print(f"Dukan kassasynyn jemi: {jemi} manat")

def dukan_dolandyrmak():
    harytlar = []

    while True:
        print("\Dukan dolandyrmak ucin menu: ")
        print("1. Harytlar gorkezmek ")
        print("2. Haryt satyn almak ")
        print("3. Taze haryt gosmak ")
        print("4. Harydyn bahasyny uytgetmek ")
        print("5. Harydy ayyrmak ")
        print("6. Mukdary artdyrmak ")
        print("7. Kassany gorkezmek ")
        print("8. Cykmak ")

        saylaw = input("Saylawynyzy girizin: ")

        if saylaw == "1":
            harytlary_gorkez(harytlar)
        elif saylaw == "2":
            haryt_satyn_al(harytlar)
        elif saylaw == "3":
            taze_haryt_gos(harytlar)
        elif saylaw == "4":
            harydyn_bahasyny_uytget(harytlar)
        elif saylaw == "5":
            harydy_ayyr(harytlar)
        elif saylaw == "6":
            mukdary_artdyr(harytlar)
        elif saylaw == "7":
            kassany_gorkez(harytlar)
        elif saylaw == "8":
            print("Programmadan cykylyar... ")
            break
        else:
            print("Nadogry saylaw! Tazeden synanysyn. ")

dukan_dolandyrmak()