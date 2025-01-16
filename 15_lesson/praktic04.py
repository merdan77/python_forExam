isgarler = { "Nurly": {"synag 1": 100,
                        "synag 2": 100,
                        "synag 3": 100},

              "Oraz": {"synag 1": 78,
                        "synag 2": 44,
                        "synag 3": 30 },
}

ady = input("Ady: ")
if ady in isgarler:
    isleg = input("Doly maglumat: (hawa/yok) ")
    if isleg == "hawa":
        print(isgarler[ady])
    else:
        mag = input("hunari/bilimi/yasy ")
        print(isgarler[ady][mag])
else:
    print(f"{ady} atly isgar yok")