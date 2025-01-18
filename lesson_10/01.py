sagat = int(input("Shu vagt sagat nace (0-23): "))
if sagat > 100 or sagat < 0:
    print("Na dogry")
elif sagat <= 5:
    print("Gije")
elif sagat <= 12:
    print("Irden")
elif sagat <= 18:
    print("Oylan")
elif sagat <= 23:
    print("Agsham")