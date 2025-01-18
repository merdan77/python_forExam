soraglar = [
    ("Gujurly nacinji yylda acyldy?", ["2017", "2010", "1999", "2014"], "2014"),
    ("Gujurlyn SMM-my kim?", ["Resul Nuryyev", "Atajan Atayev", "Ayna Esenova", "Agabay Agabayev"], "Ayna Esenova"),
    ("2014 World cup-py haysy yurt gazandy?", ["Argentina", "Portugal", "Germany", "Russia"], "Germany"),
    ("Komp 5 agshamky kursda 3-nji komp-da kim otyryar?", ["Nurly", "Merjen", "Azim", "Resul"], "Azim"),
    ("Dunyade in kici yurt?", ["South Africa", "Ecuador", "North Korea", "Monaco"], "Monaco"),
    ("In gymmat kompaniya?", ["Airbus", "Apple", "Tesla", "Nvidia"], "Apple"),
    ("In govy rapper?", ["100", "600", "500", "200"], "200"),
    ("In bet serial?", ["Breaking bad", "Game of thrones", "Squid game", "Yali capkini"], "Game of thrones"),
    ("In govy ayal kompyuter mugallym?", ["Maysa Shad", "Maysa Mugallymdan govy mugallym yok", "Maysa Mugallymdan govy mugallym yok", "Maysa Mugallymdan govy mugallym yok"], "Maysa Shad"),
    ("Soraglary ozum tapdymmy?", ["yok", "hovo", "munkun", "belki"], "hovo")
]


bal = 0
dogry_jogap_sany = 0
yalnys_jogap_sany = 0
sorag_sany = 0  


for sorag in soraglar:
    
    print(f"Sorag: {sorag[0]}")
    jogaplar = sorag[1] 
    dogry_jogap = sorag[2]  

    
    print(f"1. {jogaplar[0]}")
    print(f"2. {jogaplar[1]}")
    print(f"3. {jogaplar[2]}")
    print(f"4. {jogaplar[3]}")

    
    ulanyjy_jogaby = int(input("Jogabyňyzy saýlaň (1-4): ")) - 1

    
    if jogaplar[ulanyjy_jogaby] == dogry_jogap:
        print("Dogry jogap!")
        bal += 10  
        dogry_jogap_sany += 1
    else:
        print(f"Ýalňyş jogap! Dogry jogap: {dogry_jogap}")
        bal -= 5  
        yalnys_jogap_sany += 1

    sorag_sany += 1  
    
    
    if sorag_sany == 10:
        break

    print()  

print("")
print(f"Oýun tamamlandy! 🎉🎊🎈🎇🎆✨✨🎉 \nJemi bal: {bal}")
print(f"Dogry jogaplaryň sany: {dogry_jogap_sany}")
print(f"Ýalňyş jogaplaryň sany: {yalnys_jogap_sany}")