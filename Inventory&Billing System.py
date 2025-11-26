# Inventory & Billing System (Pure Python)

# Inventory: product_name : [price, stock]
inventory = {
    "Pen": [10, 50],
    "Notebook": [40, 30],
    "Pencil": [5, 100],
    "Eraser": [8, 80]
}

cart = {}

def show_inventory():
    print("\n--- Available Products ---")
    for item, details in inventory.items():
        print(f"{item}: ₹{details[0]} (Stock: {details[1]})")
    print("--------------------------")

def add_to_cart():
    product = input("Enter product name: ").title()
    if product in inventory:
        qty = int(input("Enter quantity: "))
        if qty <= inventory[product][1]:
            cart[product] = cart.get(product, 0) + qty
            inventory[product][1] -= qty
            print(f"{qty} {product}(s) added to cart ✅")
        else:
            print("Not enough stock ❌")
    else:
        print("Product not found ❌")

def generate_bill():
    print("\n--- Final Bill ---")
    total = 0
    for product, qty in cart.items():
        price = inventory[product][0]
        cost = price * qty
        total += cost
        print(f"{product} x {qty} = ₹{cost}")
    print("-------------------")
    print(f"Total Amount: ₹{total}")
    print("-------------------")
    print("Thank you for shopping 🛒\n")

# Main Menu
while True:
    print("\n1. Show Inventory\n2. Add to Cart\n3. Generate Bill & Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        show_inventory()
    elif choice == "2":
        add_to_cart()
    elif choice == "3":
        generate_bill()
        break
    else:
        print("Invalid choice ❌")
