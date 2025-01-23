def hasap_barlamak():
    belgi =int(input("Telefon belginiz: "))
    if (60000000 < belgi < 65999999) or (71000000 < belgi < 71999999):
        print(f"Sizin hasabynyz: 5 TMT ")
    else: 
        print("Nadogry belgi yazdynyz! ")

def hasap_doldurmak():
    belgi =int(input("Telefon belginiz:  "))
    if (60000000 < belgi < 65999999) or (71000000 < belgi < 71999999):
        toleg =float(input("Toleg mocberi(TMT):  "))
        if 0 < toleg < 50:
            print("Toleginiz kabul edildi")
            print(f"Sizin balansynyz: {5+ toleg} TMT")
        else:
            print("Yalnys toleg mocberi yazdynyz!")
    else:
        print("Nadogry belgi yazdynyz!")
def cykys():
    print("Hyzmatynyz ucin sagbolun!!! ")

while True:
    print("""
            TMCELL hyzmatlary:
            1.Hasap barlamak
            2.Hasap doldurmak
            3.Cykmak
                """)
    hyzmat =int(input("Hyzmat gornusini saylan (1, 2, 3): "))
    if hyzmat == 1:
        hasap_barlamak()
    elif hyzmat == 2:
        hasap_doldurmak()
    elif hyzmat == 3:
        cykys()
        break
    else:
        print("Nadogry hyzmat sayladynyz!")