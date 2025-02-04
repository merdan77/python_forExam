import random
a = ["Rejep", "Meret", "Oraz", "Anna"]
print(random.choice(a))

print(random.sample(a, 3))

print(a)
random.shuffle(a)
print(a)