print(f"Menu: \n1. Burger \n a. Regular - 120 TK\n b. Cheeseburger - 150 TK \n c. Veggie Burger - 130 TK\n2. Pizza \n a. Small - 200 TK \n b. Medium - 300 TK \n c. Large - 400 TK \n3. Salad \n a. Caesar Salad - 100 TK \n b. Greek Salad - 120 TK \n c. Garden Salad - 80 TK")
print()
item = int(input("What would you like to order?(Enter the number): "))

if item == 1:
    category = input("Which size of Burger would you like? (Enter the letter): ")
    if category == "a":
        price = 120
        print(f"Item: Regular Burger, Price {price} TK")
    elif category == "b":
        price = 150
        print(f"Item: Cheese Burger, Price {price} TK")
    elif category == "c":
        price = 130
        print(f"Item: Veggie Burger, Price {price} TK")
    else:
        print("Sorry Please select from the menu")

elif item == 2:
    category = input("Which size of Pizza would you like? (Enter the letter): ")
    if category == "a":
        price = 200
        print(f"Item: Small Pizza, Price {price} TK")
    elif category == "b":
        price = 300
        print(f"Item: Medium Pizza, Price {price} TK")
    elif category == "c":
        price = 400
        print(f"Item: Large Pizza, Price {price} TK")
    else:
        print("Sorry Please select from the menu")
elif item == 3:
    category = input("Which size of Salad would you like? (Enter the letter): ")
    if category == "a":
        price = 100
        print(f"Item: Caesar Salad, Price {price} TK")
    elif category == "b":
        price = 120
        print(f"Item: Greek Salad, Price {price} TK")
    elif category == "c":
        price = 80
        print(f"Item: Garden Salad, Price {price} TK")
    else:
        print("Sorry Please select from the menu")
