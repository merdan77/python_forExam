Program = {"hello" : "salam",
        "apple" : "alma",
        "lemon" : "limon",
        "bread" : "corek",
        "family" : "family",
        "father" : "kaka",
        "mother" : "eje",
        "flag" : "baydak",
        "pen" : "rucka",
        "water" : "suw",
        "dog" : "it"}

while True:
    print("""***My program***
    1.Show
    2.Add
    3.Edit
    4.Delete
    5.exit
    """)
    
    a = int(input("Birini Savla: "))
    if 1 == a:
        for i,j in Program.items():
            print(i, "-", j)
    elif 2 == a:
        eng = input("English world: ") 
        tkm = input("Turkmen world: ")
        Program[eng] = tkm
        print('Added')

    elif 3 == a:
        word = input("Enter the world English: ")
        word = input("Enter the world turkmen: ")
        Program[word] = word1
        print("Edited")

    elif 4 == a:
        soz = input("Enter the word in english: ")
        del program[soz]
        print("Deleted")

    elif 5 == a:
        print("Thank you using programmi: ")
        break

    else:
        print("Wrong comand...")  