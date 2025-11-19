# ---------------------------
# Vending Machine Program
# ---------------------------

# Menu items stored using dictionaries
menu = {
    1: {"name": "chips", "price": 1.50},
    2: {"name": "candy bar", "price": 3.75},
    3: {"name": "soda", "price": 2.75},
    4: {"name": "water", "price": 2.00}
}

# Cart to store selected items
cart = []

# Display menu
print("Welcome to G's Vending Machine!")
print("Menu:\n")

for item_num, details in menu.items():
    print(f"{item_num}. {details['name']} - ${details['price']:.2f}")

print("\n=============================\n")

# User input loop
while True:
    choice = input("Enter item number or 'done': ").lower().strip()

    if choice == "done":
        break 
 
    if choice.isdigit():
        item_num = int(choice)

        if item_num in menu:
            cart.append(menu[item_num])
            print(f"Added {menu[item_num]['name']} - ${menu[item_num]['price']:.2f} to cart")
        else:
            print("Invalid item number, please try again.")
    else:
        print("Invalid input. Please enter a number or 'done'.")

# Print receipt
print("\n========== RECEIPT ==========")

if not cart:
    print("No items selected.")
else:
    total_sum = 0

    for item in cart:
        item_name = item['name']
        item_price = item['price']
        print(f"{item_name:15} ${item_price:.2f}")
        total_sum += item_price

    print("-----------------------------")
    print(f"{'TOTAL':15} ${total_sum:.2f}")

print("Thank you for using the vending machine!")


