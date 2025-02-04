import random
c = 0
p = 0
while True:
    a = input("Do you roll a dice? (yes/no) ")
    if a == "yes":
        comp = random.randrange(1, 6)
        player = random.randrange(1, 6)
        print(f"Computer: {comp}")
        print(f"Player: {player}")
        c += comp
        p += player

    elif a == "no":
        break

    else:
        print("Yalnysh komanda!")

print("***** FINAL SCORE *****")
print(f"Computer: {c}")
print(f"Player: {p}")
if p > c:
    print("Gutlayas utdynyz!")

elif p < c:
    print("Gynansakda Komp utdy!")

else:
    print(f"Dene den {c} = {p}")