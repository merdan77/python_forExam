def education_system():
    print("Welcome to the Education System")

    students = {}
    while True:
        name = input("Enter student's name (none): ").capitalize()

        if name == "Done":
            break

        grade = input(f"Enter{name}'s grade: ")

        students[name] = int(grade)
for i, j in students.items():
    if j >= 90:
        print(f"{i} has an A. Exselent work!")
    elif j >= 75:
        print(f"{i} has a B. Good job!")
    elif j >=60:
        print(f"{i}has a C.Needs improwement.")
    elif:
        print(f"{i}has failed. Additional support needed.")

    if students:
        average = sum(students.values()) / len(students)
        print(f"Class average: {avarege:2f}")

education_system()