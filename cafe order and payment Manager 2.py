# Manu
Manu = {
    "Pizza" : 100,
    "Burger" : 60,
    "Coffee" : 50,
    "Momos" : 40,
    "Tea" : 20,
    "Water" : 20
}
# food Manu on output window

print("Food Manu of our retaurent")
print("Pizza = 100\nBurger = 60\nCoffee = 50\nMomos = 40\nTea = 20")

# Order From Customer & Payment calculation
Total_Amount = 0
list = []
list2 = []
i = 0
print("Enter Quantity of Each item which you want order")
for item in Manu :
    Quantity = int(input(f"Please Enter {item} Quantity:"))
    Amount = Manu[item]*Quantity
    Total_Amount += Amount
    list.append(Quantity)
    list2.append(item)

print("\n\nYour Order is :\n")
for Q in list :
    if Q == 0 :
        i += 1
        continue
    else :
        print(f"{Q} {list2[i]} ")
        i += 1

print(f"\nYour Payable Amount is {Total_Amount}\nThank You for coming in our Restaurent")

