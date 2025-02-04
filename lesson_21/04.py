import random
o = ["Picture", "Number"]
n = 0
p = 0
for i in range(1, 11):
    number = random.choice(o)
    if number == "Number":
        n += 1
    else:
        p += 1
    print(f"{i} {number}")

print(f"NUMBER: {n}")
print(f"PICTURE: {p}")

if n > p:
    print("Kop cykan NUMBER")
elif n < p:
    print("Kop cykan PICTURE")