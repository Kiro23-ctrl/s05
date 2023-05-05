shopping_cart = {}
total_cost = 0.0
print("Welcome to the online store! Let's start shopping!")
while True:
    item_name = input("Please enter the name of the item: ")
    while not item_name.strip():
        print("Error: Item name cannot be empty.")
        item_name = input("Please enter the name of the item: ")
    while True:
        try:
            item_price = float(input("Please enter the price of the item: "))
            if item_price <= 0:
                print("Error: Price must be a positive number.")
            else:
                break
        except ValueError:
            print("Error: Price must be a number.")
    shopping_cart[item_name] = item_price
    total_cost += item_price
    print(f"{item_name} was added to your shopping cart.")
    choice = input("Do you want to add another item? (y/n): ")
    if choice.lower() != 'y':
        break
print(f"Thank you for shopping with us! Your total cost is ${total_cost:.2f}.")