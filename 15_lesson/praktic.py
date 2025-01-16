dictionary = {
    'alma': '8',
    'uzum': '12',
    'hurma': '18',
    'banan': '25',
    'nar': '15'
}
summa = []
for i,j in dictionary.items():
    print(i,'-',j)
while True:
    haryt = input('Name almak isleyarsiniz? ')
    if haryt in dictionary:
        massa = int(input('Nace kg almak isleyarsiniz? '))
        x = int(dictionary[haryt]) * massa
        summa.append(x) 
    elif haryt == 'quit'.lower():
        break
    elif haryt not in dictionary:
        print(f"{haryt} bizde yok")
print('Siz',sum(summa),'manat tolemeli')
