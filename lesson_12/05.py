soz = str(input('Enter the string: '))

letters = 0
cap_letters = 0
small_letters = 0
digits = 0
spaces = 0

for i in soz:
    if i.isalpha():
        letters += 1
        if i.isupper():
            cap_letters += 1
        elif i.islower():
            small_letters += 1
    elif i.isdigit():
        digits += 1
    else:
        spaces += 1
print(f"Letters: {letters}")
print(f"Capital Letters: {cap_letters}")
print(f"Small Letters: {small_letters}")
print(f"Digits: {digits}")
print(f"Spaces: {spaces}")