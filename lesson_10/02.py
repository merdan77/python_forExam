jemi = 0
muk = 0

for i in range(1, 11):
    number = int(input(f"{i} - number: "))
    if number > 0:
        jemi += number
    elif number < 0:
        muk += 1
print(f"Poloziel sanlan jemi:", jemi)
print(f"Otrisatel sanlan jemi:", muk)