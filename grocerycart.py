



print("===== Welcome to Group Two's Grocery Shop =====")
print()
# Step-2: Initialize the grocery item list and a storage for selected items(cart)
grocery = {
    'Tomatoes': 6,
    'Grapes': 13,
    'Nuts': 5,
    'Onions': 8,
    'Butter': 11,
    'Carrots': 7,
    'Cookies': 5,
    'Potatoes':7
}
# Initialize the cart that contain the name, quantity and subtotal of the item selected(nested dictionary)
cart = {}
print("=" * 50)
print("Available items:")
for item, price in grocery.items():
    print(f"  - {item.title()}: ${price:.2f}")
print("=" * 50)
# Step-3: Get user input and quantity by using a while loop
while True:
    # Get customer input
    selected_grocery = input('Please enter grocery name from the grocery list or checkout to finish: ').strip().title()
    # Check if the customer have finished selecting or not
    if selected_grocery.lower() == 'checkout':
        break
    # Check if the selected item is in the grocery list
    elif selected_grocery not in grocery:
        print(f'Invalid item number selected, there no {selected_grocery} in the grocery list. Please try again.')
        print()
        continue
    # Check for the quantity for the selected item from the grocery
    selected_grocery_qty = input(f'Please enter the quantity for {selected_grocery} item = ')
    try:
        # Change the quantity input to float
        selected_grocery_qty_float = float(selected_grocery_qty)
        # Check the valid input for the quantity
        if selected_grocery_qty_float <= 0:
            print('The selected grocery quantity must be greater than zero. Please enter a valid input.')
            print()
            continue
    except ValueError:
        print('Invalid input. Please enter a valid input for the selected item.')
        print()
        continue
    # Check if the selected item from the grocery is in the cart and update the quantity and subtotal price.
    # Get the price from the grocery list
    price = grocery[selected_grocery]
    # Calculate the subtotal
    subtotal = price * selected_grocery_qty_float
    # Check the selected item in the cart and update
    if selected_grocery in cart:
        cart[selected_grocery]['selected_quantity'] += selected_grocery_qty_float
        cart[selected_grocery]['subtotal'] += subtotal
    else:
        cart[selected_grocery] = {'selected_quantity': selected_grocery_qty_float, 'subtotal': subtotal}
        print(f"{selected_grocery_qty_float} unit of {selected_grocery} is added to cart with Subtotal: ${subtotal:.2f}")
        print()
# Step-4: Print the Receipt
print()
print('          ======================= RECEIPT ======================= ')
total_sum = 0
for item in cart:
    selected_quantity = cart[item]['selected_quantity']
    subtotal = cart[item]['subtotal']
    unit_price = grocery[item]
    print(f'Item_name: {item:8} -----  Qty={selected_quantity} ----- Unit_price=${unit_price:.2f} ----- Subtotal= ${subtotal:.2f}')
    total_sum += subtotal
print('_' * 80)
print(f"{'Total Sum':15} ------------------------------------------------------    ${total_sum:.2f}")
print('_' * 80)
print('        ****************  Thank you for coming!  ****************')




