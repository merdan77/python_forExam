okuw = int(input("Toparda nace okuvcy bar: "))
gecmedik = 0
ortaca = 0
gecen = 0

for i in range(1,okuw + 1):
    bal = int(input(f"{i} - okuvcyn synag bahasy: "))

    if bal < 50:
        gecmedik += 1
    elif bal >= 50:
        gecen += 1
    ortaca += bal

print(f"synagdan gecen:", gecen)
print(f"Gecmedik:", gecmedik)
print(f"Ortaca:", ortaca // okuw)