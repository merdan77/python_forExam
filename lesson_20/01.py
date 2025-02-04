okuvchylar = {"Nurberdi" : 17,
              "Batyr" : 15,
              "Selim" : 12
}

print(okuvchylar)

okuvchylar["Nurberdi"] = 18
print(okuvchylar)

okuvchylar.pop("Selim")
print(okuvchylar)

for i in okuvchylar:
    print(i)

for a in okuvchylar:
    print(okuvchylar[a])