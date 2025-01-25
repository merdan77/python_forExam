def store():
    products = {
        "milk": 4,
        "bread": 2,
        "apple": 3,
        "egg": 5,
        "cheese": 6,
        "Sausage": 8
    }
    total_cost = 0
    print("Welcome! We are glad to have you at our store! ")
    while True:
        print("\nProducts and their prices: ")
        for product, price in products.items():
            print(f"{product.capitalize()}: {price} TMT")
        choice = input("\Enter the prouct you want to buy or type 'done' to finish: ").lower()
        if choice == 'done':
            break
        elif choice in product:
            quantity = int(input("Enter the quantity: "))
            cost = product[choice] * quantity
            total_cost += cost
            print(f"{choice.capitalize()} x {quantity}: {cost} TMT")
        else:
            print("Sorry, that product is not avaliable. Please choose another. ")
    print(f"\Total cost: {total_cost} TMT")
store()