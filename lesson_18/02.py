def login_system(dogry_ulanyjy, dogry_parol,maks_ymtylma):
    ymtylma_sany = 0

    while ymtylma_sany < maks_ymtylma:
        ulanyjy_ady = input("Ulanyjy adyny girizin: ")
        parol = input("Paroly girizin: ")

        if ulanyjy_ady == dogry_ulanyjy and parol == dogry_parol:
            print("Hos geldiniz")
            return

        else:
            ymtylma_sany += 1
            print("Ulanyjy ady yada parol nadogry! ")
    if ymtylma_sany == maks_ymtylma:
        print("Hasaba girmane bolan mumkinciliginiz gutardy.")

login_system("user123","parol1456",3)