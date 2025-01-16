ihgarler={ "Mekan ": {"hunari : programist",
                    "bilimi" :"orta",
                    "yashy",:22}
"Oraz" : {"hunari : hasapchy",
                    "bilimi" :"yokary",
                    "yashy",:30}
ady=input("Ady:")
if ady in ishgarler:
    isleg=input("Doly maglumat:(howa/yok)")
    if isleg=="howa":
        print(ishgarler[ady])
    else:
        mag=input("hunari/bilimi/yashy")
        print(ishgarler[ady][mag])
    else:
        print(f"{ady}atly y\ishgar yok")