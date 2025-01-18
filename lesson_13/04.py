N = int(input('How many students: '))
students = []

for i in range(1, N + 1):
    name = input(f'{i} - Name: ')
    students.append(name)

print(students)